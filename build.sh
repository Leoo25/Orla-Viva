#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala as dependências do Python
pip install -r requirements.txt

# Instala as dependências do Tailwind e compila o CSS
# (Isso é essencial porque a pasta theme existe no seu projeto)
python manage.py tailwind install
python manage.py tailwind build

# Coleta os arquivos estáticos (CSS, Imagens, JS)
python manage.py collectstatic --no-input

# Aplica as migrações no Banco de Dados
python manage.py migrate