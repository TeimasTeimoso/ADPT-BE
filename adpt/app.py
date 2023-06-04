from flask import Flask
from routes import routes
from logger import configure_logger

app = Flask(__name__)

app.register_blueprint(routes)

@app.route('/')
def index():
    return 'Welcome to the ADPT API!'

if __name__ == '__main__':
    app.run()

