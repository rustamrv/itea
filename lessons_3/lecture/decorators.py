from functools import wraps


def decorator(number=3):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(name):
            print('-' * number)
            res = func(name)
            print("-" * number)
            return res

        return wrapper
    return actual_decorator


@decorator(33)
def target_f(name):
    print(f"Hello world, {name}")
from functools import wraps


def decorator(number=3):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(name):
            print('-' * number)
            res = func(name)
            print("-" * number)
            return res

        return wrapper
    return actual_decorator


@decorator(33)
def target_f(name):
    print(f"Hello world, {name}")
    return "Nice"


# decorator(target_f)()
res = target_f("Rustam")
print(res)