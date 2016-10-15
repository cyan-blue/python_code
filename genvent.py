from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
import gevent

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/block')
def block():
    gevent.sleep(60)
    return 'Hello World!'


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
