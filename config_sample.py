from collections import defaultdict
from datetime import datetime
from pytz import timezone
# 大会スタート日時．現在4/15にしていますが，大会スタート前に5/1にしてください．
CONTEST_START = timezone('Asia/Tokyo').localize(
    datetime(year=2019, month=4, day=15, hour=0, minute=0))
INITIAL_CAPITAL = 10000 # 大会の初期資金．現物を初期資金に含める場合は，JPY+現物の大会開始時の時価
USER_NAME = "hoge" # 参加者の名前．@なしのTwitterIDを使用してください．
PL_SERVER_URL = 'http://hoge' # 大会参加者用部屋で案内します．
WEBHOOK_URL = "hogehoge" # ご自身で設定した損益通知部屋のwebhookのURL
KEY = "hugahuga" # LiquidのAPIキー
SECRET = "piyopiyo" # LiquidのAPIシークレット
# 自分が取引に使う基軸通貨と，BTCJPY以外の「現物」を取引する場合はその通貨を入れる．
# レバレッジ取引の場合は，基軸通貨のみTrueで良いが，現物取引の場合は現物をTrueにする．
# BTCJPYのレバレッジ取引→'JPY': Trueで他はFalse
# XRPJPYのレバレッジ取引→'JPY': Trueで他はFalse
# BTCJPYの現物取引→'JPY':True，'BTC': Trueで他はFalse
# XRPJPYの現物取引→'JPY': True, 'XRP': Trueで他はFalse
# BTCJPYの現物取引とBTCUSDの現物取引→'JPY':True，'USD: True, 'BTC': Trueで他はFalse
# BTCJPYのレバレッジ取引とBTCUSDのレバレッジ取引→'JPY':True，'USD: True,で他はFalse
# BTCJPYのレバレッジ取引とBTCUSDの現物取引→'JPY':True，'USD: True, 'BTC': Trueで他はFalse
FUNDING_CURRENCIES = defaultdict(bool, {'JPY': True, 'BTC': False,
                      'ETH': False, 'USD': False, 'QASH': False, 'XRP': True})
