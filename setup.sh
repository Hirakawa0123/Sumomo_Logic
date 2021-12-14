#!/bin/sh

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install django

pip install django-environ

pip install tika

find django/base/migrations/ -type f | grep -v -E '__init__.py' | xargs rm -rf

cd django/

mkdir secrets

touch secrets/.env

cat <<EOF > secrets/.env
SECRET_KEY=XzXkLzuFDpGJG2aXrSDUd5C8shn7C4ka3ZR9UEwTgRGNQZCkVp
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3
EOF