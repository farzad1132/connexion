from connexion.decorators.parameter import get_function_arguments

import decorator


@decorator.decorator
def the_decorator(f, *args, **kwargs):
    return f(*args, **kwargs)


def stub_function(foo, bar):
    """stub function to be used in tests."""
    pass


def kwargs_function(*args, **kwargs):
    pass


def test_get_proper_argument_list():
    """Test get the proper argument list of the decorated function."""

    assert len(get_function_arguments(stub_function)[0]) == 2
    assert get_function_arguments(stub_function) == (['foo', 'bar'], False)

    decorated_stub_function = the_decorator(stub_function)
    assert len(get_function_arguments(decorated_stub_function)[0]) == 2
    assert get_function_arguments(decorated_stub_function) == (['foo', 'bar'], False)


def test_get_kwargs():
    assert get_function_arguments(kwargs_function) == ([], True)
