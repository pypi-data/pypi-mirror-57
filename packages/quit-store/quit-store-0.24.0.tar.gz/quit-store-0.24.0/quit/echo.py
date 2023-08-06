from flask import Flask
from flask_uwsgi_websocket import GeventWebSocket

app = Flask(__name__.split('.')[0])

print("name is: {}".format(__name__.split('.')[0]))
print(app.name)
print(app.import_name)

websocket = GeventWebSocket(app)

@websocket.route('/echo')
def echo(ws):
    while True:
        msg = ws.receive()
        ws.send(msg)

@app.route('/hello')
def hallo():
    return 'Hello'

if __name__ == '__main__':
    app.run(gevent=100)
