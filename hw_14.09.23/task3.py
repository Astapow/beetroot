def arg_rules(type_: type, max_length: int, contains: list):
    def first_wrapper(func):
        def second_wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    return False
                if len(arg) >= max_length:
                    return False
                if contains in args:
                    return True
            return func(*args, **kwargs)

        return second_wrapper

    return first_wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))

print(create_slogan('S@SH05'))


