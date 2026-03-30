from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from database import db
from models.user import User
from models.refeicao import Refeicao
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/user', methods=['POST'])
def criar_usuario():
    data = request.json
    nome = data.get("nome")
    senha = data.get("senha")

    if nome and senha:
        senha_criptografada = generate_password_hash(senha)

        new_user = User(nome=nome, senha=senha_criptografada)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"mensagem": "usuário criado com sucesso"})
    
    return jsonify({"mensagem": "nao foi possivel criar seu usuário"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    nome = data.get("nome")
    senha = data.get("senha")

    user = User.query.filter_by(nome=nome).first()

    if user and check_password_hash(user.senha, senha):
        login_user(user)
        return jsonify({"mensagem": "login feito com sucesso"})

    return jsonify({"mensagem": "Nao foi possivel fazer login"}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"mensagem": "logout realizado com sucesso"})

@app.route('/refeicao', methods=['POST'])
def criar_refeicao():
    data = request.json
    nome = data.get("nome")
    descricao = data.get("descricao")
    user_id = data.get("user_id")

    if nome and descricao and user_id:
        nova_refeicao = Refeicao(nome=nome, descricao=descricao, user_id=user_id)
        db.session.add(nova_refeicao)
        db.session.commit()
        return jsonify({"mensagem": f"refeicao registrada ao usuario {user_id} com sucesso"})
    
    return jsonify({"mensagem": "dados invalidos"}), 400

@app.route('/refeicao/<int:id>', methods=['PUT'])
@login_required 
def alterar_refeicao(id):
    refeicao = db.session.get(Refeicao, id)#busca a refeicao pelo ID

    if not refeicao:
        return jsonify({"mensagem": "nao existem refeicoes disponíveis"}), 404

    if current_user.role != 'admin':
        return jsonify({"mensagem": "voce nao tem permissao pra editar essa refeicao"}), 403
    
    data = request.json
    refeicao.nome = data.get("nome", refeicao.nome)
    refeicao.descricao = data.get("descricao", refeicao.descricao)
    refeicao.user_id = data.get("user_id", refeicao.user_id)
    refeicao.dieta = data.get("dieta", refeicao.dieta)

    db.session.commit()
    return jsonify({"mensagem": "refeicao atualizada com sucesso"})

@app.route('/refeicao/<int:id>', methods=['DELETE'])
@login_required
def deletar_refeicao(id):
    refeicao = db.session.get(Refeicao, id)

    if not refeicao:
        return jsonify({"mensagem": "nao foi possivel achar a refeicao"}), 404

    if current_user.role != 'admin':
        return jsonify({"mensagem": "voce nao tem permissao pra deletar"}), 403

    db.session.delete(refeicao)
    db.session.commit()
    return jsonify({"mensagem": "refeicao deletada com sucesso"})

@app.route('/user/<int:id>', methods=['GET'])
@login_required
def listar_refeicoes_usuario(id):
    user = db.session.get(User, id)

    if not user:
        return jsonify({"mensagem": "nao foi encontrado nenuhm usuario"}), 404

    refeicao = Refeicao.query.filter_by(user_id=id).all()

    lista_de_refeicoes = []
    for r in refeicao:
        lista_de_refeicoes.append({
            "nome": r.nome,
            "descricao": r.descricao,
            "dieta": r.dieta,
            "id": r.id,
            "user_id": r.user_id
        })
    return jsonify({
        "id": user.id,
        "nome": user.nome,
        "refeicoes": lista_de_refeicoes
    })

@app.route('/refeicao/<int:id>', methods=['GET'])
def listar_refeicao(id):
    refeicao = db.session.get(Refeicao, id)

    if not refeicao:
        return jsonify({"mensagem": "Nao foi encontrado sua refeicao"}), 404

    return jsonify({
        "id": refeicao.id,
        "nome": refeicao.nome,
        "descricao": refeicao.descricao,
        "dieta": refeicao.dieta
    })


if __name__ == "__main__":
    app.run(debug=True)