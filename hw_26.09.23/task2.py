def my_range(*args):
    start, end, step = 0, None, 1

    if len(args) == 1:
        end = args[0]
    elif len(args) == 2:
        start, end = args
    elif len(args) == 3:
        start, end, step = args
        if step < 0:
            start, end = end, start
    else:
        raise TypeError(f'my_range expected at most 3 arguments, got {len(args)}')

    current = start
    while (end is None) or (current < end if step > 0 else current > end):
        yield current
        current += step
