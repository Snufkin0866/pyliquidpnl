# -*- coding: utf-8 -*-
import pyliquid
import config

key = config.KEY
secret = config.SECRET
api = pyliquid.API(key, secret)
FUNDING_CURRENCIES = config.FUNDING_CURRENCIES

def get_rates():
    product_id = {'BTC':5, 'ETH':29, 'XRP':83, 'QASH':50, 'BCH':41}
    rate = {}
    rate['JPY'] = 1
    rate['USD'] = 112
    
    for f in FUNDING_CURRENCIES:
        if FUNDING_CURRENCIES[f]:
            if f != 'JPY' and f != 'USD':
                rate[f] = float(api.get_a_product(id=product_id[f])['last_traded_price'])    
    return rate

def calc_INITIAL_CAPITAL():
    INITIAL_CAPITAL = 0
    rate = get_rates()
    balance = api.get_all_acountbalance()
    for b in balance:
        if b['currency'] in rate.keys():
            INITIAL_CAPITAL += float(b['balance']) * rate[b['currency']]

    print(f'INITIAL_CAPITAL : {int(INITIAL_CAPITAL)}')

if __name__ == '__main__':
    calc_INITIAL_CAPITAL()
    