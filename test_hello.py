"""Testing first homework with greetings."""
import pytest

from first_hello_by_lang import say_hello

test_data_hello = (
    ('ru', 'Привет'),
    ('en', 'Hi'),
    ('sdljaljd', 'Hi'),
)


@pytest.mark.parametrize('lang, expected', test_data_hello)
def test_say_hello(lang: str, expected: str) -> None:
    """Test say_hello function.

    Args:
        lang: a language to greet in.
        expected: a greeting expected by test
    """
    assert say_hello(lang) == expected
