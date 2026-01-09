from Bai2.TGNgoaiTe.NgoaiTe import EXCHANGE_RATES
def vnd_to_foreign(vnd_amount):
    result = {}
    for currency , rate in EXCHANGE_RATES.items():
        result[currency] = vnd_amount / rate
    return result