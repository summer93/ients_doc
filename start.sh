
docker pull doej/nginx_flask_uwsgi:v0.1
docker run --name xx -v /ients_doc:/ients_doc -v /ients_doc/nginx/ients-doc.conf:/etc/nginx/conf.d/ients-doc.conf -p 8099:8077 uwsgi --ini /ients_doc/web/flask-uwsgi.ini & nginx
