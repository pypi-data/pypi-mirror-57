from bvr.bvr_rest import bvr_rest_before_after


def test_bvr_rest_before_after_called_as_decorator(capsys):

    @bvr_rest_before_after
    def rest_before_after():
        return 2

    return_value = rest_before_after()

    captured_ouput = capsys.readouterr().out

    assert return_value == 2
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_ouput
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} " in captured_ouput
    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_called_as_callable_returning_decorator(capsys):

    @bvr_rest_before_after()
    def rest_before_after():
        return 2

    return_value = rest_before_after()

    captured_ouput = capsys.readouterr().out

    assert return_value == 2
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_ouput
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} " in captured_ouput
    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_called_as_decorator_with_function_args(capsys):

    @bvr_rest_before_after
    def rest_before_after(msg):
        print(msg)
        return msg

    return_value = rest_before_after("Hello")

    captured_ouput = capsys.readouterr().out

    assert return_value == "Hello"
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before_after | ARGS: ('Hello',) | KWARGS: {} \n" in captured_ouput
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_before_after | ARGS: ('Hello',) | KWARGS: {} " in captured_ouput
    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_called_as_callable_returning_decorator_with_function_args(capsys):

    @bvr_rest_before_after()
    def rest_before_after(msg):
        print(msg)
        return msg

    return_value = rest_before_after("Hello")

    captured_ouput = capsys.readouterr().out

    assert return_value == "Hello"
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before_after | ARGS: ('Hello',) | KWARGS: {} \n" in captured_ouput
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_before_after | ARGS: ('Hello',) | KWARGS: {} " in captured_ouput
    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_called_as_decorator_with_function_kwargs(capsys):

    @bvr_rest_before_after
    def rest_before_after(msg):
        print(msg)
        return msg

    return_value = rest_before_after(msg="Hello")

    captured_ouput = capsys.readouterr().out

    assert return_value == "Hello"
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {'msg': 'Hello'} \nHello\n" in captured_ouput
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {'msg': 'Hello'} " in captured_ouput
    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_called_as_callable_returning_decorator_with_function_kwargs(capsys):

    @bvr_rest_before_after()
    def rest_before_after(msg):
        print(msg)
        return msg

    return_value = rest_before_after(msg="Hello")

    captured_ouput = capsys.readouterr().out

    assert return_value == "Hello"
    assert "RESTING_BEFORE: 5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {'msg': 'Hello'} \nHello\n" in captured_ouput
    assert "RESTING_AFTER: 5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {'msg': 'Hello'} " in captured_ouput
    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_with_countdown_true(capsys):

    @bvr_rest_before_after(countdown=True)
    def rest_before_after():
        return 2

    return_value = rest_before_after()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_BEFORE: 5/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 4/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 3/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 2/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 1/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output

    assert "RESTING_AFTER: 5/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 4/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 3/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 2/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 1/5 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output

    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_with_countdown_true_and_non_default_seconds(capsys):

    @bvr_rest_before_after(seconds=2, countdown=True)
    def rest_before_after():
        return 2

    return_value = rest_before_after()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_BEFORE: 2/2 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_BEFORE: 1/2 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output

    assert "RESTING_AFTER: 2/2 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output
    assert "RESTING_AFTER: 1/2 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \n" in captured_output

    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_with_countdown_false_and_non_default_seconds(capsys):

    @bvr_rest_before_after(seconds=2)
    def rest_before_after():
        print('Hello')
        return 2

    return_value = rest_before_after()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_BEFORE: 2 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \nHello\n" in captured_output
    assert "RESTING_AFTER: 2 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} " in captured_output

    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name


def test_bvr_rest_before_after_should_case_float_to_int(capsys):

    @bvr_rest_before_after(seconds=2.23)
    def rest_before_after():
        print('Hello')
        return 2

    return_value = rest_before_after()

    captured_output = capsys.readouterr().out

    assert return_value == 2

    assert "RESTING_BEFORE: 2 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} \nHello" in captured_output
    assert "RESTING_AFTER: 2 second(s) | FUNCTION: rest_before_after | ARGS: () | KWARGS: {} " in captured_output

    assert rest_before_after.__name__ == "rest_before_after"  # Important for decorators to not override method name
