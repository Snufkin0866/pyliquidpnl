from collections import defaultdict
from datetime import datetime
from pytz import timezone

CONTEST_START = timezone('Asia/Tokyo').localize(
    datetime(year=2019, month=4, day=15, hour=0, minute=0))
WEBHOOK_URL = "hogehoge"
KEY = "hugahuga"
SECRET = "piyopiyo"
FUNDING_CURRENCIES = defaultdict(bool, {'JPY': True, 'BTC': False,
                      'ETH': False, 'USD': False, 'QASH': False})
