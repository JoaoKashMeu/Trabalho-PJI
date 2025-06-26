from flask import Blueprint, request, jsonify
from services.usuario_services import criar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/', methods=['POST'])
def criar():
    dados = request.json
    novo = criar_usuario(dados)
    if novo is None:
        return jsonify({"erro": "Usuário já cadastrado."}), 409
    return jsonify(vars(novo)), 201

@usuario_bp.route('/', methods=['GET'])
def listar():
    return jsonify([vars(u) for u in listar_usuarios()]), 200

@usuario_bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    atualizado = atualizar_usuario(id, dados)
    if atualizado:
        return jsonify(vars(atualizado)), 200
    return jsonify({"erro": "Usuário não encontrado."}), 404

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    if deletar_usuario(id):
        return jsonify({"mensagem": "Usuário deletado."}), 200
    return jsonify({"erro": "Usuário não encontrado."}), 404