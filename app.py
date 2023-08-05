from flask import Flask
from adpt.routes.text import routes

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def index():
    return 'Welcome to the ADPT API!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

