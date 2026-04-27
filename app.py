from flask import Flask
from flask_jwt_extended import JWTManager
from extensions import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'secret-key'

db.init_app(app)
jwt = JWTManager(app)

from models import *
from routes.auth import auth_bp
from routes.employees import emp_bp
from routes.salaries import salaries_bp

app.register_blueprint(auth_bp)
app.register_blueprint(emp_bp)
app.register_blueprint(salaries_bp)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)