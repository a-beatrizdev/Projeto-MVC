from app.models import categoria 
from app.models import produto
from app.models import usuarios

# Gerar a migrations
# python -m alembic revision --autogenerate -m "Criar tabela categorias e produtos."

#Aplicar a migration 
# python -m alembic upgrade head 