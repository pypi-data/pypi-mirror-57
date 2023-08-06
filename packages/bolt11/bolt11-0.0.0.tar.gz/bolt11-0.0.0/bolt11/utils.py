import re

from .types import Bitcoin


def _btc_to_amount(btc: Bitcoin) -> str:
    """ Given an amount in bitcoin, shorten it.
    """
    btc = int(btc * 10 ** 12)

    for unit in ['p', 'n', 'u', 'm', '']:
        if btc % 1000 == 0:
            btc //= 1000
        else:
            break

    return f'{btc}{unit}'


def _amount_to_btc(amount: str) -> Bitcoin:
    """ Given a shortened amount, convert it into bitcoin.
    """
    if not re.fullmatch(r'\d+[pnum]?', amount):
        raise ValueError(f'Invalid amount "{amount}"')

    try:
        num = {
            'p': 10 ** 12,
            'n': 10 ** 9,
            'u': 10 ** 6,
            'm': 10 ** 3,
        }[amount[-1]]
        return Bitcoin(amount[:-1]) / num

    except KeyError:
        return Bitcoin(amount)
