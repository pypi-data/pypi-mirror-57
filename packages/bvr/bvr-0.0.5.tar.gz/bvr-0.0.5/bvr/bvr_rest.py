import functools
from time import sleep


def handle_sleeper(countdown, before_after, func, seconds, *args, **kwargs):
    if countdown is True:
        countdown_sleeper(before_after, func, seconds, *args, **kwargs)
    else:
        simple_sleeper(before_after, func, seconds, *args, **kwargs)


def simple_sleeper(before_after, func, seconds, *args, **kwargs):
    sleep(seconds)
    msg = ("RESTING_{}: {} second(s) | "
           "FUNCTION: {} | "
           "ARGS: {} | "
           "KWARGS: {} ").format(before_after,
                                 seconds,
                                 func.__name__,
                                 args,
                                 kwargs)
    print(msg)


def countdown_sleeper(before_after, func, seconds, *args, **kwargs):
    for i in range(0, seconds):
        sleep(1)
        msg = ("RESTING_{}: {}/{} second(s) | "
               "FUNCTION: {} | "
               "ARGS: {} | "
               "KWARGS: {} ").format(before_after,
                                     seconds - i,
                                     seconds,
                                     func.__name__,
                                     args,
                                     kwargs)
        print(msg)


def bvr_rest_after(arg=None, seconds=5, countdown=False):
    seconds = int(seconds)

    def bvr_rest_after_decorator(func):
        @functools.wraps(func)
        def bvr_rest_after_wrapper(*args, **kwargs):
            before_after = "AFTER"
            return_value = func(*args, **kwargs)
            handle_sleeper(countdown, before_after, func, seconds, *args, **kwargs)

            return return_value

        return bvr_rest_after_wrapper

    if callable(arg):
        return bvr_rest_after_decorator(arg)

    return bvr_rest_after_decorator


def bvr_rest_before(arg=None, seconds=5, countdown=False):
    seconds = int(seconds)

    def bvr_rest_before_decorator(func):
        @functools.wraps(func)
        def bvr_rest_before_wrapper(*args, **kwargs):
            before_after = "BEFORE"
            handle_sleeper(countdown, before_after, func, seconds, *args, **kwargs)
            return_value = func(*args, **kwargs)

            return return_value

        return bvr_rest_before_wrapper

    if callable(arg):
        return bvr_rest_before_decorator(arg)

    return bvr_rest_before_decorator
