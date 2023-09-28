"""Testing first homework with greetings."""
import pytest

from first_hello_by_lang import say_hello

en_greeting = 'Hi'
test_data_hello = (
    ('ru', 'Привет'),
    ('en', en_greeting),
    ('sdljaljd', en_greeting),
    ('asdsad', en_greeting),
    ('sdljaasdsdgdafljd', en_greeting),
    ('oiuajsd', en_greeting),
    ('oqwehqh', en_greeting),
)


@pytest.mark.parametrize('lang, expected', test_data_hello)
def test_say_hello(lang: str, expected: str) -> None:
    """Test say_hello function.

    Args:
        lang: a language to greet in.
        expected: a greeting expected by test
    """
    assert all((say_hello(lang), expected))
