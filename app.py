from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from database import db
from models.user import User
from models.refeicao import Refeicao


app = Flask(__name__)
app.config['SECRET_KEY'] = 'charlesdobronx22'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/teste', methods=['GET'])
def hello_world():
    return jsonify({"mensagem": "hello world"})

if __name__ == "__main__":
    app.run(debug=True)