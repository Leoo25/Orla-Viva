# Orla Viva 🌊

Projeto Django para gestão e recomendação de eventos e locais na orla de Praia Grande.

## 🚀 Como Iniciar (Codespaces)

Este projeto foi configurado para rodar automaticamente no GitHub Codespaces com PostgreSQL e Tailwind CSS.

### 1. Configuração Inicial (Apenas na primeira vez)

Ao criar um novo Codespace, abra o terminal e execute este script único. Ele configura o banco de dados (resolvendo permissões), instala dependências e prepara os arquivos estáticos:

```bash
# Copie e cole TUDO isso no terminal:
sudo service postgresql start && \
# Configura Postgres para aceitar conexões locais (Modo TRUST)
PG_CONF=$(sudo -u postgres psql -c 'SHOW hba_file;' -t | xargs) && \
echo "host all all 127.0.0.1/32 trust" | sudo tee $PG_CONF && \
echo "host all all ::1/128 trust" | sudo tee -a $PG_CONF && \
sudo service postgresql restart && \
# Cria Banco e Usuário
sudo -u postgres psql -c "CREATE DATABASE orla_viva_db;" 2>/dev/null || true && \
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'gordo78';" 2>/dev/null || true && \
# Instala Dependências
source venv/bin/activate && \
pip install -r requirements.txt && \
cd theme/static_src && npm install && cd ../.. && \
python manage.py tailwind build && \
python manage.py migrate && \
echo "✅ Tudo pronto! Agora rode: python manage.py runserver"