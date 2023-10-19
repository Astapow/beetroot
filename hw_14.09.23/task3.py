def arg_rules(type_: type, max_length: int, contains: list):
    def first_wrapper(func):
        def second_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for arg in args:
                if not isinstance(arg, type_):
                    return False

                if len(arg) >= max_length:
                    return False

                for item in contains:
                    if item in arg:
                        return result

                    return False

            return result

        return second_wrapper

    return first_wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('SaSHa') is False

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

assert create_slogan(1) is False
