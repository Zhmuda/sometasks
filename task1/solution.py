def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for i, (arg_name, arg_type) in enumerate(zip(annotations.keys(), annotations.values())):
            if i >= len(args):
                break
            arg_value = args[i]
            if not isinstance(arg_value, arg_type):
                raise TypeError(f"Argument '{arg_name}' must be {arg_type}, not {type(arg_value)}")
        for arg_name, arg_value in kwargs.items():
            if arg_name in annotations:
                arg_type = annotations[arg_name]
                if not isinstance(arg_value, arg_type):
                    raise TypeError(f"Argument '{arg_name}' must be {arg_type}, not {type(arg_value)}")
        return func(*args, **kwargs)
    return wrapper
