## Description
最小限の部品構成で、Rasberry Piを移動可能にするために、ボディのデザインと簡単なスクリプトを作成しました。
デザインデータは`/body_design`ディレクトリに置いています。pdf形式とdxf形式のデータを置いていますので、レーザー加工業者で加工してくお使いください。

ボディのデザインはこんな感じ。

<img src="https://i.gyazo.com/aef038bd3d01c9f087ff54fb89f166bc.jpg" width="320">

こんな感じで動きます。

[![Image from Gyazo](https://i.gyazo.com/01551400dce30a9c4d7ba219a2bd7e5d.gif)](https://gyazo.com/01551400dce30a9c4d7ba219a2bd7e5d)


## Installation

**pigpio**
```
sudo apt install pigpio
sudo pip3 install pigpio
```

## Getting started
1. `body_design`のデータからレーザー加工機でボディのパーツを作成。素材は4mmのものを使ってください。
2. ボディのパーツを組み立てます。この時、バッテリーとRaspberry Piも一緒に組み立てます。
3. Raspberry Piの初期設定をする
4. 以下の手順でスクリプトを動かします。
```
# pigpiod起動
make gpio

# サーボモーターの動作確認
make servo_test

# Webサービス(Flask)起動
make app
```

Qiitaで解説してます。
<link>

## 参考URL
サーボモーターの仕様
- https://www.adafruit.com/product/2442
- https://www.addicore.com/FS90R-Servo-p/ad314.htm
