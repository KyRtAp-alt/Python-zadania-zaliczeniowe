import functools

def log_parameters(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_args = func.__code__.co_varnames[:func.__code__.co_argcount]
        param_info = {name: type(value).__name__ for name, value in zip(func_args, args)}
        param_info.update({k: type(v).__name__ for k, v in kwargs.items()})
        print(f"Function '{func.__name__}' called with parameters: {param_info}")
        return func(*args, **kwargs)
    return wrapper

@log_parameters
def example_function(a, b, c=3, d="default"):
    return a + b + c

example_function(1, 2, d="Hi")