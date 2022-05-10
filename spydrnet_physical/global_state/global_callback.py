_container_merged_instance = list()


def _call_merged_instance(*args, **kwargs):
    for func in _container_merged_instance:
        func(*args, **kwargs)


def register_merged_instance(method):
    _register(_container_merged_instance, method)


def _register(container_to_register, method):
    ''' TODO: look into inlining this function perhaps, not not be necessary since is won't be called often.'''
    assert method not in container_to_register
    container_to_register.append(method)


def _deregister(container_to_deregister, method):
    ''' TODO: look into inlining this function perhaps, may not be necessary since it won't be called often.'''
    assert method in container_to_deregister
    container_to_deregister.remove(method)
