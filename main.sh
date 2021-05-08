#!/bin/bash

echo Which website will you run?

read website

if [website=CryptoAnalysis]
then
  cd CryptoAnalysis
  pipenv run python manage.py runserver
elif [website=DjangoStore]
then
  cd DjangoStore
  pipenv run python manage.py runserver
else
  echo That is not a valid input.
fi
