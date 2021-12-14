# Sumomo_Logic

Sumomo_Logicは、可視化しづらいファイル形式のデータを可視化を目指したWebサービスです。
(開発中)
## 動作確認
Python==3.8.2
Django==4.0
django-environ==0.8.1
tika==1.24
pip==21.3.1

## Installation

```bash
git clone https://github.com/Hirakawa0123/Sumomo_Logic.git
```

## Setup
※Pythonがインストール済みであることを前提に記載しております。


```python
cd Sumomo_Logic/

source setup.sh

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
## Usage

開発中