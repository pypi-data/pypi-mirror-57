from watched_schema import validators

from flask import Blueprint

from .cache import get_cache


def hard_copy(obj):
    if isinstance(obj, (set, list, tuple)):
        return list(map(hard_copy, obj))
    if isinstance(obj, dict):
        return {key: hard_copy(value) for key, value in obj.items()}
    return obj


class Addon(object):
    # Some items which can be used for automatic tests (see test.py)
    test_items = None

    has_repository = False

    def __init__(self):
        props = {'type': 'worker'}
        props.update(self.get_props())
        self.props = validators['models']['addon'](props)

    def get_props(self):
        raise NotImplementedError()

    def __getitem__(self, key):
        return self.props[key]

    @property
    def id(self):
        return self.props["id"]

    @property
    def type(self):
        return self.props["type"]

    def get_cache(self, key):
        return get_cache().get([self.id, key])

    def set_cache(self, key, value, ttl=24 * 3600):
        return get_cache().set([self.id, key], value, ttl)

    def delete_cache(self, key):
        return get_cache().delete([self.id, key])

    def addon(self, ctx, **kwargs):
        return hard_copy(self.props)

    def directory(self, ctx, **kwargs):
        raise NotImplementedError()

    def item(self, ctx, **kwargs):
        raise NotImplementedError()

    def source(self, ctx, **kwargs):
        raise NotImplementedError()

    def subtitle(self, ctx, **kwargs):
        raise NotImplementedError()

    def resolve(self, ctx, **kwargs):
        raise NotImplementedError()


class Repository(Addon):
    def __init__(self, props):
        self.addons = []
        self.addons.append(self)

        props['type'] = 'repository'
        self.get_props = lambda: props

        super(Repository, self).__init__()

    def register(self, addon):
        addon.has_repository = True
        self.addons.append(addon)

    def addon(self, ctx, index=False, **kwargs):
        props = super(Repository, self).addon(ctx, **kwargs)
        if not index:
            kwargs['index'] = True
            props['addons'] = []
            for addon in self.addons:
                if addon is self:
                    continue
                p = addon.addon(ctx, **kwargs)
                p['metadata'] = {'url': f'./{addon.id}'}
                props['addons'].append(p)
        return props
