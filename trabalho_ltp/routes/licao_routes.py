from flask import Blueprint, request, jsonify
from services.licao_service import criar_licao, listar_licoes, atualizar_licao, deletar_licao

licao_bp = Blueprint('licoes', __name__)

@licao_bp.route('/', methods=['POST'])
def criar():
    dados = request.json
    nova = criar_licao(dados)
    if nova is None:
        return jsonify({"erro": "Lição já cadastrada."}), 409
    return jsonify(vars(nova)), 201

@licao_bp.route('/', methods=['GET'])
def listar():
    return jsonify([vars(l) for l in listar_licoes()]), 200

@licao_bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    atualizada = atualizar_licao(id, dados)
    if atualizada:
        return jsonify(vars(atualizada)), 200
    return jsonify({"erro": "Lição não encontrada."}), 404

@licao_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    if deletar_licao(id):
        return jsonify({"mensagem": "Lição deletada."}), 200
    return jsonify({"erro": "Lição não encontrada."}), 404