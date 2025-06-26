from flask import Blueprint, request, jsonify
from services.estatistica_services import gerar_estatistica, listar_estatisticas

estatistica_bp = Blueprint('estatisticas', __name__)

@estatistica_bp.route('/', methods=['POST'])
def gerar():
    dados = request.json
    nova = gerar_estatistica(dados)
    return jsonify(vars(nova)), 201

@estatistica_bp.route('/', methods=['GET'])
def listar():
    return jsonify([vars(e) for e in listar_estatisticas()]), 200