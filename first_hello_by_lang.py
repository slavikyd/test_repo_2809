"""Saying hello in different languages."""


def say_hello(lang: str) -> str:
    """Get greeting in a given language.

    Args:
        lang: given language to greet in.

    Returns:
        str: a greeting in a given language, defaults to 'Hi'.
    """
    greetings = {
        'ru': 'Привет',
        'en': 'Hi',
        'es': 'Hola',
        'fr': 'Salut',
        'ge': 'Hallo',
        'kl': 'nuqneH',
    }
    greeting = greetings.get(lang)
    return greeting if greeting else 'Hi'
