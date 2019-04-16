from collections import defaultdict
from datetime import datetime

CONTEST_START = datetime(2019,4,15)
WEBHOOK_URL = "hogehoge"
KEY = "hugahuga"
SECRET = "piyopiyo"
FUDNING_CURRENCIES = defaultdict(bool, {'JPY': True, 'BTC': False,
                      'ETH': False, 'USD': False, 'QASH': False})
