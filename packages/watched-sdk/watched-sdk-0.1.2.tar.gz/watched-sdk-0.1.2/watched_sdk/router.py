import json
import os
import sys
import threading
import traceback
from uuid import uuid4

from watched_schema import validators

from flask import Blueprint, request

from .cache import get_cache
from .common import logger
from .context import Context
from .views import render


class TunnelResponse:
    def __init__(self, r):
        self.r = r

    @property
    def error(self):
        return self.r['error']

    @property
    def status_code(self):
        return self.r['status']

    @property
    def url(self):
        return self.r['url']

    @property
    def headers(self):
        return self.r['headers']

    def json(self):
        return self.r['json']

    @property
    def text(self):
        if 'text' not in self.r and 'json' in self.r:
            return json.dumps(self.json())
        return self.r['text']

    @property
    def content(self):
        if 'raw' not in self.r:
            return self.text
        return self.r['raw'].decode('base64')


class HttpContext(Context):
    def __init__(self, addon, action):
        super(HttpContext, self).__init__(addon, action)
        self.result_channel = None
        self.event = threading.Event()

    def send(self, status, body):
        if self.result_channel:
            data = json.dumps([status, body])
            get_cache().set('task:response:'+self.result_channel, data)
        else:
            self.response = status, body
            self.event.set()

    def fetch_remote(self, url, timeout=30, **kwargs):
        # Create and send task
        id = str(uuid4())
        task = {
            'id': id,
            'action': 'fetch',
            'url': url,
            'params': kwargs,
        }
        validators['task']['task'](task)
        get_cache().set('task:wait:'+id, '1')
        print('task.create', id)
        self.send(428, task)

        # Wait for result
        data = get_cache().wait_key('task:result:'+id, timeout, True)
        result_channel, result = json.loads(data)
        if not result_channel:
            raise ValueError('Missing result_channel')
        self.result_channel = result_channel
        print('task.result.get', result["id"])
        validators['task']['result'](result)
        return TunnelResponse(result)


def validate_response(ctx, status, response):
    if status == 500:
        validators['models']['apiError'](response)
    elif status == 428:
        validators['task']['task'](response)
    else:
        ctx.schema['response'](response)


def task(ctx, result):
    validators['task']['result'](result)

    # Make sure the key exists to prevent spamming
    if not get_cache().get('task:wait:'+result['id']):
        raise ValueError('Task wait key '+result['id']+' does not exists')
    get_cache().delete('task:wait:'+result['id'])

    # Set the result
    logger.warning('task.result.set %r', result['id'])
    result_channel = str(uuid4())
    raw = json.dumps([result_channel, result])
    get_cache().set('task:result:'+result['id'], raw)

    # Wait for the response
    data = get_cache().wait_key('task:response:'+result_channel)
    status, response = json.loads(data)
    validate_response(ctx, status, response)
    return json.dumps(response), status, {'Content-Type': 'application/json'}


def run(addon, action):
    ctx = HttpContext(addon, action)
    req = request.json
    if req.get('kind') == 'taskResult':
        return task(ctx, req)

    class Thread(threading.Thread):
        def run(self):
            try:
                status, response = 200, ctx.run(req)
            except Exception as e:
                status, response = 500, {"error": e.args[0]}
                traceback.print_exc()
            validate_response(ctx, status, response)
            ctx.send(status, response)

    Thread().start()
    ctx.event.wait()
    status, response = ctx.response
    return json.dumps(response), status, {'Content-Type': 'application/json'}


def create_blueprint(addon):
    bp = Blueprint(addon.id, __name__)

    @bp.route('/', methods=['GET'])
    def index():
        if request.args.get('wtchDiscover'):
            response = {
                'watched': True,
                'hasRepository': addon.addon_has_repository
            }
            return json.dumps(response), 200, {'Content-Type': 'application/json'}
        return render(addon)

    @bp.route('/<action>', methods=['POST'])
    def action(action):
        return run(addon, action)

    return bp
