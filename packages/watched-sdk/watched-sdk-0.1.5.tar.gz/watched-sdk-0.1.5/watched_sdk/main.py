import json

from flask import Flask

from .common import logger
from .context import Context
from .router import create_blueprint
from .test import test_addons
from .addon import BasicAddon, RepositoryAddon


def _parse(args):
    req = {}
    for arg in args:
        key, value = arg.split('=', 1)
        try:
            value = json.loads(value)
        except Exception:
            pass
        req[key] = value
    return req


def _start(root_addon, addons, *args):
    app = Flask(__name__)

    blueprints = {}

    def mount(addon, path):
        logger.info('Mounting %s (%s) on %s',
                    addon.id, addon.type, path)
        if addon.id not in blueprints:
            blueprints[addon.id] = create_blueprint(addon)
        app.register_blueprint(blueprints[addon.id], url_prefix=path)

    if root_addon is not None:
        mount(root_addon, '/')
    for addon in addons:
        if addon is not root_addon:
            mount(addon, f'/{addon.id}')

    @app.route('/health', methods=['GET'])
    def health():
        return 'OK'

    app.run('0.0.0.0', 3000, debug=True if 'debug' in args else False)


def _call(root_addon, addons, *args):
    data = _parse(args)

    if root_addon is None:
        default_addon_id = None
    else:
        default_addon_id = root_addon.id
        if root_addon not in addons:
            addons.append(root_addon)

    addon_id = data.pop('addon_id', default_addon_id)
    if addon_id:
        addons = [a for a in addons if a.id == addon_id]
    if not addons:
        raise ValueError(f'Addon "{addon_id}" not found')
    addon = addons[0]

    action = data.pop('action', 'addon')
    ctx = Context(addon, action)
    response = ctx.run(data)
    print(json.dumps(response, indent=2))


def main(appdata, *args):
    """The main function of the WATCHED SDK.
    - `call`: Test your addon on the command line.
    - `test`: Run automatic tests on your addons.
    - `start`: Starts a HTTP server on port 3000.
    - `start debug`: Starts a HTTP server on port
      3000 with debug options enabled (automatic
      reloading etc.)

    The `appdata` parameter. It can be one of this values:
    - If it's a `RepositoryAddon`, the repository will be
      mounted at `/`, and all containing addons will be
      on `/{addon.id}`.
    - If it's any other kind of `Addon`, it will be mounted
      on `/`.
    - If it's a list of addons, all of them will be mounted
      on `/{addon.id}`. There will be nothing on `/`.
    """
    if isinstance(appdata, RepositoryAddon):
        root_addon = appdata
        addons = root_addon.addons
        for addon in addons:
            if addon is not root_addon:
                addon.addon_has_repository = True
    elif isinstance(appdata, BasicAddon):
        root_addon = appdata
        addons = []
    else:
        root_addon = None
        addons = appdata

    if root_addon is not None:
        root_addon.addon_is_root_addon = True

    try:
        cmd = args[0]
    except IndexError:
        cmd = None

    if cmd == 'start':
        _start(root_addon, addons, *args[1:])
    elif cmd == 'call':
        _call(root_addon, addons, *args[1:])
    elif cmd == 'test':
        if root_addon is not None and root_addon not in addons:
            addons.append(root_addon)
        test_addons(addons, *args[1:])
    else:
        raise ValueError('Usage: watched_sdk <start|call|test> [...]')
