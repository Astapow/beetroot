def stop_words(words: list):
    def first_wrapper(func):
        def second_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for item in words:
                result = result.replace(item, "*")
            return result

        return second_wrapper

    return first_wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steve"))

