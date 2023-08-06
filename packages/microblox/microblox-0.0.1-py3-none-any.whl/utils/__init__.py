def read_config_from_dict(params:list, d: dict) -> dict:
    """
    Reads the configuration parameters from given dictionary
    """
    config = {}
    for key in params:
        val = getattr(d, key, None)
        config[key] = val
        if not val:
            print('WARNING: Variable {} not found in given dictionary.'.format(key))
    
    return config

def read_config_from_env(params:list) -> dict:
    """
    Reads the configuration parameters from environment variables
    """
    import os

    return read_config_from_dict(params, os.environ)

