web: gunicorn gestion_pedidos.wsgi

web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn gestion_pedidos_v4_jwt.wsgi && python manage.py tailwind install