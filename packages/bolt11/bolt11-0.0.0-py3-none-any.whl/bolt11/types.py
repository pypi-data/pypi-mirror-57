from decimal import Decimal


class Bitcoin(Decimal):

    @property
    def sats(self) -> int:
        return (self * 10 ** 8).to_integral_exact()


class Bech32(str):
    __slots__ = ('hrp', 'data')


class LightningInvoice(Bech32):
    pass
