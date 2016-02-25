def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return 'Welcome to MuxiStudio!'



[uwsgi]
socket = 公网IP:9090
master = true
vhost = true 
no-stie = true 
workers = 2 
reload-mercy = 10
vacuum = true
max-requests = 1000
limit-as = 512
buffer-sizi = 30000
pidfile = /var/run/uwsgi.pid
daemonize = /website/uwsgi.log
