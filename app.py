from flask import Flask
from views.alert import alert_blueprint

app = Flask(__name__)


app.register_blueprint(alert_blueprint, url_prefix="/alerts")

if __name__ == '__main__':
    app.run(debug=True, port=4999)
