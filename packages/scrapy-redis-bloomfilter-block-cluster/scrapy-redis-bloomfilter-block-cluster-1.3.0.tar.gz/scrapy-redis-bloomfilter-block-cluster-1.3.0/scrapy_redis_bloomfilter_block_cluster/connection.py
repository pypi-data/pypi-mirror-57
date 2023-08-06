import six

from scrapy.utils.misc import load_object

from . import defaults


# Shortcut maps 'setting name' -> 'parmater name'.
SETTINGS_PARAMS_MAP = {
    'REDIS_URL': 'url',
    'REDIS_HOST': 'host',
    'REDIS_PORT': 'port',
    'REDIS_ENCODING': 'encoding',
}


def get_redis_from_settings(settings):
    """Returns a redis client instance from given Scrapy settings object.

    This function uses ``get_client`` to instantiate the client and uses
    ``defaults.REDIS_PARAMS`` global as defaults values for the parameters. You
    can override them using the ``REDIS_PARAMS`` setting.

    Parameters
    ----------
    settings : Settings
        A scrapy settings object. See the supported settings below.

    Returns
    -------
    server
        Redis client instance.

    Other Parameters
    ----------------
    REDIS_URL : str, optional
        Server connection URL.
    REDIS_HOST : str, optional
        Server host.
    REDIS_PORT : str, optional
        Server port.
    REDIS_ENCODING : str, optional
        Data encoding.
    REDIS_PARAMS : dict, optional
        Additional client parameters.

    """
    params = defaults.REDIS_PARAMS.copy()
    params.update(settings.getdict('REDIS_PARAMS'))
    # XXX: Deprecate REDIS_* settings.
    for source, dest in SETTINGS_PARAMS_MAP.items():
        val = settings.get(source)
        if val:
            params[dest] = val

    # Allow ``redis_cls`` to be a path to a class.
    if isinstance(params.get('redis_cls'), six.string_types):
        params['redis_cls'] = load_object(params['redis_cls'])

    return get_redis(**params)


def from_settings(settings):
    """
    根据settings中的配置来决定返回集群还是单机连接方式
    :param settings:
    :return:
    """
    if "REDIS_CLUSTER_NODES" in settings or 'REDIS_CLUSTER_URL' in settings:
        return get_redis_cluster_from_settings(settings)
    return get_redis_from_settings(settings)


def get_redis(**kwargs):
    """Returns a redis client instance.

    Parameters
    ----------
    redis_cls : class, optional
        Defaults to ``redis.Redis``.
    url : str, optional
        If given, ``redis_cls.from_url`` is used to instantiate the class.
    **kwargs
        Extra parameters to be passed to the ``redis_cls`` class.

    Returns
    -------
    server
        Redis client instance.

    """
    redis_cls = kwargs.pop('redis_cls', defaults.REDIS_CLS)
    url = kwargs.pop('url', None)
    if url:
        return redis_cls.from_url(url, **kwargs)
    else:
        return redis_cls(**kwargs)


# 集群连接配置
REDIS_CLUSTER_SETTINGS_PARAMS_MAP = {
    'REDIS_CLUSTER_URL': 'url',
    'REDIS_CLUSTER_HOST': 'host',
    'REDIS_CLUSTER_PORT': 'port',
    'REDIS_CLUSTER_ENCODING': 'encoding',
}


def get_redis_cluster_from_settings(settings):
    params = defaults.REDIS_PARAMS.copy()
    params.update(settings.getdict('REDIS_CLUSTER_PARAMS'))
    params.setdefault('startup_nodes', settings.get('REDIS_CLUSTER_NODES'))
    params.setdefault('cluster_password', settings.get('REDIS_CLUSTER_PASSWORD'))
    # XXX: Deprecate REDIS_* settings.
    for source, dest in REDIS_CLUSTER_SETTINGS_PARAMS_MAP.items():
        val = settings.get(source)
        if val:
            params[dest] = val

    return get_redis_cluster(**params)


def get_redis_cluster(**kwargs):
    """返回一个redis集群的操作游标
    :param redis_nodes:
    :return:
    """
    redis_cluster_cls = kwargs.get('redis_cluster_cls', defaults.REDIS_CLUSTER_CLS)
    url = kwargs.pop('url', None)
    redis_nodes = kwargs.pop('startup_nodes', None)
    cluster_password = kwargs.pop('cluster_password', None)
    if redis_nodes:
        return redis_cluster_cls(startup_nodes=redis_nodes, password=cluster_password, **kwargs)
    if url:
        return redis_cluster_cls.from_url(url, **kwargs)
    return redis_cluster_cls(**kwargs)
