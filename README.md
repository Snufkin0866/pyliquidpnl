# pyliquidpnl
## 概要
- Liquid bot大会用損益通知，保存，描画スクリプトです．短時間で，動くことだけを目的に作ったので基本ベタ書きです．
## 機能
- Liquidの各funding currency口座のオープンポジションの損益，オープンポジションの損益を含めたトータルの証拠金残高，オープンポジション
を含まない証拠金残高（確定損益のみの証拠金残高）をSQLiteに保存する．なお，損益計算にはGET/trading_accountsのエンドポイントを使用．
- 保存した残高およびオープンポジションの損益をmatplotlibで描画する．
## 使い方
- 使い方はそれほど難しくありません．やることは大きく分けて，1. configファイルの編集2. cronの設定．（cronでなくても定時実行できればなんでも良い）です．
- python versionは3系です．特別なライブラリは必要ありませんが，pyliquidが必要です．
- pyliquid.pyと同じディレクトリに置いてください．
pyliquid→https://github.com/Snufkin0866/pyliquid
- config_sample.pyをリネームしたconfig.pyにAPI情報と，Discordの損益部屋で取得したWEBHOOKURLを入力してください．なお，WEBHOOKの名前は参加者様の名前と
同じ名前でお願いします．また，configの各設定項目の説明はconfig.py内にコメントアウトして書いてあります．
- **configのUSER_NAMEはTwitter IDと同じものにしてください．なお，@はなしでお願いします．これを違う名前にすると，トータルの損益が記録されません．**
- configのFUNDINC_CURRENCIESにはレバレッジ取引オンリーの場合，JPY以外False，BTCJPYの現物取引の場合はBTCとJPY以外をFalse，それ以外の例えばQashを証拠金として扱う場合には，該当する通貨をTrueにしてください．また，アルト現物を扱う場合はconfigのFUNDINC_CURRENCIESにその通貨を追加してください.
例：BCH: True
- pyliquid_pnl.pyがあるディレクトリにdataというディレクトリを作ってください．
- describe_graphのデフォルト引数にopen_positionというのがあり，これをFalseにするとopen_positionのPLは表示されなくなります．
- コマンドライン引数の1番目の引数（0番目=デフォルトで入っているもの）で挙動を制御します．大会参加者は5分以内の時間解像度で定期的に，
```
python pyliquid_pnl.py save
```
を回してください．また，毎日23:45に
```
python pyliquid_pnl.py send_discord
```
を回してください．cronを使うといいと思います．

- cron設定の例：
```
*/2 * * * * ~/anaconda3/bin/python ~/pyliquidpnl/pyliquid_pnl.py save
45 23 * * * ~/anaconda3/bin/python ~/pyliquidpnl/pyliquid_pnl.py send_discord
```
