from flask import Blueprint, request, jsonify
from services.progresso_services import registrar_progresso, listar_progresso, atualizar_progresso, deletar_progresso

progresso_bp = Blueprint('progresso', __name__)

@progresso_bp.route('/', methods=['POST'])
def registrar():
    dados = request.json
    novo = registrar_progresso(dados)
    return jsonify(vars(novo)), 201

@progresso_bp.route('/', methods=['GET'])
def listar():
    return jsonify([vars(p) for p in listar_progresso()]), 200

@progresso_bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    atualizado = atualizar_progresso(id, dados)
    if atualizado:
        return jsonify(vars(atualizado)), 200
    return jsonify({"erro": "Progresso não encontrado."}), 404

@progresso_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    if deletar_progresso(id):
        return jsonify({"mensagem": "Progresso deletado."}), 200
    return jsonify({"erro": "Progresso não encontrado."}), 404