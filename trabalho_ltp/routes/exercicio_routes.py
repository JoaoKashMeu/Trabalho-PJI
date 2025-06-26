from flask import Blueprint, request, jsonify
from services.exercicio_services import criar_exercicio, listar_exercicios

exercicio_bp = Blueprint('exercicios', __name__)

@exercicio_bp.route('/', methods=['POST'])
def criar():
    dados = request.json
    novo = criar_exercicio(dados)
    return jsonify(vars(novo)), 201

@exercicio_bp.route('/', methods=['GET'])
def listar():
    return jsonify([vars(e) for e in listar_exercicios()]), 200