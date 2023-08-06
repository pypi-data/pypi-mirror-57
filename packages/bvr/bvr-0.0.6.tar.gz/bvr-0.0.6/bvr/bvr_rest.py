import functools
from time import sleep


BEFORE = "BEFORE"
AFTER = "AFTER"


def handle_sleeper(countdown, before_after, func, seconds, *args, **kwargs):
    if countdown is True:
        countdown_sleeper(before_after, func, seconds, *args, **kwargs)
    else:
        simple_sleeper(before_after, func, seconds, *args, **kwargs)


def simple_sleeper(before_after, func, seconds, *args, **kwargs):
    msg = ("RESTING_{}: {} second(s) | "
           "FUNCTION: {} | "
           "ARGS: {} | "
           "KWARGS: {} ").format(before_after,
                                 seconds,
                                 func.__name__,
                                 args,
                                 kwargs)

    print(msg)
    sleep(seconds)


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
            return_value = func(*args, **kwargs)
            handle_sleeper(countdown, AFTER, func, seconds, *args, **kwargs)

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
            handle_sleeper(countdown, BEFORE, func, seconds, *args, **kwargs)
            return_value = func(*args, **kwargs)

            return return_value

        return bvr_rest_before_wrapper

    if callable(arg):
        return bvr_rest_before_decorator(arg)

    return bvr_rest_before_decorator


def bvr_rest_before_after(arg=None, seconds=5, countdown=False):
    seconds = int(seconds)

    def bvr_rest_before_after_decorator(func):
        @functools.wraps(func)
        def bvr_rest_before_after_wrapper(*args, **kwargs):
            handle_sleeper(countdown, BEFORE, func, seconds, *args, **kwargs)

            return_value = func(*args, **kwargs)

            handle_sleeper(countdown, AFTER, func, seconds, *args, **kwargs)

            return return_value

        return bvr_rest_before_after_wrapper

    if callable(arg):
        return bvr_rest_before_after_decorator(arg)

    return bvr_rest_before_after_decorator
