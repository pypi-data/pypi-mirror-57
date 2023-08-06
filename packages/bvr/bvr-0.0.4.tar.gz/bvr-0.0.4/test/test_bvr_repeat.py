from bvr.bvr_repeat import bvr_repeat
from math import pi


def test_bvr_repeat_called_as_decorator(capsys):

    @bvr_repeat
    def repeat():
        return 2

    return_value = repeat()

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/2 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 2/2 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_callable_returning_decorator(capsys):

    @bvr_repeat()
    def repeat():
        return 2

    return_value = repeat()

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/2 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 2/2 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_decorator_with_args(capsys):

    @bvr_repeat
    def repeat(value):
        return value

    return_value = repeat(2)

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/2 | FUNCTION: repeat | ARGS: (2,) | KWARGS: {}" in system_output
    assert "REPEAT: 2/2 | FUNCTION: repeat | ARGS: (2,) | KWARGS: {}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_callable_returning_decorator_with_args(capsys):

    @bvr_repeat()
    def repeat(value):
        return value

    return_value = repeat(2)

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/2 | FUNCTION: repeat | ARGS: (2,) | KWARGS: {}" in system_output
    assert "REPEAT: 2/2 | FUNCTION: repeat | ARGS: (2,) | KWARGS: {}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_decorator_with_kwargs(capsys):

    @bvr_repeat
    def repeat(value):
        return value

    return_value = repeat(value=2)

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/2 | FUNCTION: repeat | ARGS: () | KWARGS: {'value': 2}" in system_output
    assert "REPEAT: 2/2 | FUNCTION: repeat | ARGS: () | KWARGS: {'value': 2}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_callable_returning_decorator_with_kwargs(capsys):

    @bvr_repeat()
    def repeat(value):
        return value

    return_value = repeat(value=2)

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/2 | FUNCTION: repeat | ARGS: () | KWARGS: {'value': 2}" in system_output
    assert "REPEAT: 2/2 | FUNCTION: repeat | ARGS: () | KWARGS: {'value': 2}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_callable_returning_decorator_with_repeat_5_times(capsys):

    @bvr_repeat(times=5)
    def repeat():
        return 2

    return_value = repeat()

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/5 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 2/5 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 3/5 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 4/5 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 5/5 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_callable_returning_decorator_with_repeat_0_times(capsys):

    @bvr_repeat(times=0)
    def repeat():
        return 2

    return_value = repeat()

    system_output = capsys.readouterr().out

    assert return_value is None  # None because it was called None times
    assert "" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_callable_returning_decorator_with_repeat_1_times(capsys):

    @bvr_repeat(times=1)
    def repeat():
        return 2

    return_value = repeat()

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/1 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_callable_returning_decorator_with_repeat_3_point_5_times(capsys):

    @bvr_repeat(times=3.5)  # Should take floor of 3.5 = 3
    def repeat():
        return 2

    return_value = repeat()

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/3 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 2/3 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 3/3 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name


def test_bvr_repeat_called_as_callable_returning_decorator_with_repeat_pi_times(capsys):

    @bvr_repeat(times=pi)  # Should take floor of math.pi = 3
    def repeat():
        return 2

    return_value = repeat()

    system_output = capsys.readouterr().out

    assert return_value == 2
    assert "REPEAT: 1/3 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 2/3 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert "REPEAT: 3/3 | FUNCTION: repeat | ARGS: () | KWARGS: {}" in system_output
    assert repeat.__name__ == "repeat"  # Important for decorators to not override method name
