web: gunicorn utilities_stats.wsgi --log-file -
worker: celery -A utilities_stats worker --without-gossip --without-mingle --without-heartbeat