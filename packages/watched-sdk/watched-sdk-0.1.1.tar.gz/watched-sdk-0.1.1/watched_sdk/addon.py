from watched_schema import validators

from flask import Blueprint

from .cache import get_cache


def hard_copy(obj):
    if isinstance(obj, (set, list, tuple)):
        return list(map(hard_copy, obj))
    if isinstance(obj, dict):
        return {key: hard_copy(value) for key, value in obj.items()}
    return obj


class BasicAddon(object):
    # Some items which can be used for automatic tests (see test.py)
    test_items = None

    addon_type = None
    addon_actions = ['addon']
    addon_has_repository = False

    props = None

    def __init__(self, props=None):
        if props is not None:
            if self.props is not None:
                raise ValueError(
                    'Define either props in constructor, or PROPS on class level')
        else:
            props = self.props
        props['type'] = self.addon_type
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


class RepositoryAddon(BasicAddon):
    addon_type = "repository"
    addon_actions = ['addon', 'repository']

    def __init__(self, props=None):
        super(RepositoryAddon, self).__init__(props)
        self.addons = [self]
        self.urls = []

    def add_addon(self, addon):
        addon.addon_has_repository = True
        self.addons.append(addon)

    def add_url(self, url):
        self.urls.append(url)

    def repository(self, ctx, **kwargs):
        result = []
        kwargs['index'] = True
        for addon in self.addons:
            props = addon.addon(ctx, **kwargs)
            props['metadata'] = {'url': f'./{addon.id}'}
            result.append(props)
        for url in self.urls:
            # TODO: Load props from remote repo via a POST /addon call
            raise NotImplementedError()
        return result


class WorkerAddon(BasicAddon):
    addon_type = "worker"
    addon_actions = ['addon', 'directory',
                     'item', 'source', 'subtitle', 'resolve']

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


class IptvAddon(BasicAddon):
    addon_type = "iptv"


class BundleAddon(BasicAddon):
    addon_type = "bundle"
