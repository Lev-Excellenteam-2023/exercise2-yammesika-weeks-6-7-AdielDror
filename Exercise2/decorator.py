from functools import wraps


def type_check(correct_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """A wrapper function"""

            for arg in args:
                if not isinstance(arg, correct_type):
                    raise TypeError(f"Expected type {correct_type}, but got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(3))  # Output: 6
print(times2("hello"))  # Raises a TypeError: Expected type <class 'int'>, but got <class 'str'>


