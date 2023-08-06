from bvr.bvr_rest import bvr_rest_after


def test_bvr_rest_after_called_as_decorator(capsys):

    @bvr_rest_after
    def rest_after():
        return 2

    return_value = rest_after()

    assert return_value == 2
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} " in capsys.readouterr().out
    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_called_as_callable_returning_decorator(capsys):

    @bvr_rest_after()
    def rest_after():
        return 2

    return_value = rest_after()

    assert return_value == 2
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} " in capsys.readouterr().out
    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_called_as_decorator_with_function_args(capsys):

    @bvr_rest_after
    def rest_after(msg):
        print(msg)
        return msg

    return_value = rest_after("Hello")

    assert return_value == "Hello"
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_after | ARGS: ('Hello',) | KWARGS: {} " in capsys.readouterr().out
    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_called_as_callable_returning_decorator_with_function_args(capsys):

    @bvr_rest_after()
    def rest_after(msg):
        print(msg)
        return msg

    return_value = rest_after("Hello")

    assert return_value == "Hello"
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_after | ARGS: ('Hello',) | KWARGS: {} " in capsys.readouterr().out
    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_called_as_decorator_with_function_kwargs(capsys):

    @bvr_rest_after
    def rest_after(msg):
        print(msg)
        return msg

    return_value = rest_after(msg="Hello")

    assert return_value == "Hello"
    assert "Hello\nRESTING_AFTER: 5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {'msg': 'Hello'} " in capsys.readouterr().out
    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_called_as_callable_returning_decorator_with_function_kwargs(capsys):

    @bvr_rest_after()
    def rest_after(msg):
        print(msg)
        return msg

    return_value = rest_after(msg="Hello")

    assert return_value == "Hello"
    assert "Hello\nRESTING_AFTER: 5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {'msg': 'Hello'} " in capsys.readouterr().out
    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_with_countdown_true(capsys):

    @bvr_rest_after(countdown=True)
    def rest_after():
        return 2

    return_value = rest_after()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_AFTER: 5/5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 4/5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 3/5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 2/5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 1/5 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} \n" in captured_output

    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_with_countdown_true_and_non_default_seconds(capsys):

    @bvr_rest_after(seconds=2, countdown=True)
    def rest_after():
        return 2

    return_value = rest_after()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_AFTER: 2/2 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 1/2 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} \n" in captured_output

    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_with_countdown_false_and_non_default_seconds(capsys):

    @bvr_rest_after(seconds=2)
    def rest_after():
        print('Hello')
        return 2

    return_value = rest_after()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "Hello\nRESTING_AFTER: 2 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} " in captured_output

    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name


def test_bvr_rest_after_should_case_float_to_int(capsys):

    @bvr_rest_after(seconds=2.23)
    def rest_after():
        print('Hello')
        return 2

    return_value = rest_after()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "Hello\nRESTING_AFTER: 2 second(s) | FUNCTION: rest_after | ARGS: () | KWARGS: {} " in captured_output

    assert rest_after.__name__ == "rest_after"  # Important for decorators to not override method name
