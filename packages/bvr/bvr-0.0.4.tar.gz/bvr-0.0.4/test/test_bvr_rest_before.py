from bvr.bvr_rest import bvr_rest_before


def test_bvr_rest_before_called_as_decorator(capsys):

    @bvr_rest_before
    def rest_before():
        return 2

    return_value = rest_before()

    assert return_value == 2
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} " in capsys.readouterr().out
    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_called_as_callable_returning_decorator(capsys):

    @bvr_rest_before()
    def rest_before():
        return 2

    return_value = rest_before()

    assert return_value == 2
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} " in capsys.readouterr().out
    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_called_as_decorator_with_function_args(capsys):

    @bvr_rest_before
    def rest_before(msg):
        print(msg)
        return msg

    return_value = rest_before("Hello")

    assert return_value == "Hello"
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before | ARGS: ('Hello',) | KWARGS: {} " in capsys.readouterr().out
    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_called_as_callable_returning_decorator_with_function_args(capsys):

    @bvr_rest_before()
    def rest_before(msg):
        print(msg)
        return msg

    return_value = rest_before("Hello")

    assert return_value == "Hello"
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before | ARGS: ('Hello',) | KWARGS: {} " in capsys.readouterr().out
    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_called_as_decorator_with_function_kwargs(capsys):

    @bvr_rest_before
    def rest_before(msg):
        print(msg)
        return msg

    return_value = rest_before(msg="Hello")

    assert return_value == "Hello"
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {'msg': 'Hello'} \nHello" in capsys.readouterr().out
    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_called_as_callable_returning_decorator_with_function_kwargs(capsys):

    @bvr_rest_before()
    def rest_before(msg):
        print(msg)
        return msg

    return_value = rest_before(msg="Hello")

    assert return_value == "Hello"
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {'msg': 'Hello'} \nHello" in capsys.readouterr().out
    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_with_countdown_true(capsys):

    @bvr_rest_before(countdown=True)
    def rest_before():
        return 2

    return_value = rest_before()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_BEFORE: 5/5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 4/5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 3/5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 2/5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 1/5 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \n" in captured_output

    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_with_countdown_true_and_non_default_seconds(capsys):

    @bvr_rest_before(seconds=2, countdown=True)
    def rest_before():
        return 2

    return_value = rest_before()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_BEFORE: 2/2 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 1/2 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \n" in captured_output

    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_with_countdown_false_and_non_default_seconds(capsys):

    @bvr_rest_before(seconds=2)
    def rest_before():
        print('Hello')
        return 2

    return_value = rest_before()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_BEFORE: 2 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \nHello" in captured_output

    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name


def test_bvr_rest_before_should_case_float_to_int(capsys):

    @bvr_rest_before(seconds=2.23)
    def rest_before():
        print('Hello')
        return 2

    return_value = rest_before()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_BEFORE: 2 second(s) | FUNCTION: rest_before | ARGS: () | KWARGS: {} \nHello" in captured_output

    assert rest_before.__name__ == "rest_before"  # Important for decorators to not override method name
