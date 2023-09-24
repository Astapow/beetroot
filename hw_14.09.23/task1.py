def logger(func):
    def wrapper(*args, **kwargs):
        print(f"called with {args}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(2, 3)
square_all(2, 4, 5)
