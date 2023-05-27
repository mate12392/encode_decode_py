def func_check(method, key):
    params = {"method": method, "key": key}

    not_none_params = {k: v for k, v in params.items() if v is not None}

    return not_none_params
