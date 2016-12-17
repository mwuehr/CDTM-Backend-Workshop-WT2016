from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, Fabi rocks!'

if __name__ == '__main__':
    addr = "localhost"
    port = 1337
    debug = True
    app.run(host=addr, port=port, debug=debug)