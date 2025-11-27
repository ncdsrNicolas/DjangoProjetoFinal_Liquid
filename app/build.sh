#!/usr/bin/env bash
# Script de build para Render

# Aplica migrações
python manage.py migrate --noinput

# Coleta arquivos estáticos
python manage.py collectstatic --noinput
