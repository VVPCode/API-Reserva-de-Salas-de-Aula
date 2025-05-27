from flask import Blueprint, request, jsonify
from models.reserva import Reserva
from database import db
import requests
from datetime import datetime



reserva_bp = Blueprint('reserva_bp', __name__)

# URL da API de gerenciamento (ajuste conforme o ambiente)
API_GERENCIAMENTO_URL = "http://host.docker.internal:5000/turmas"

@reserva_bp.route('/reservas', methods=['GET'])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([r.to_dict() for r in reservas]), 200


@reserva_bp.route('/reservas', methods=['POST'])
def criar_reserva():
    dados = request.json
    id_turma = dados.get('id_turma')
    sala = dados.get('sala')
    data_reserva_str = dados.get('data_reserva')
    horario_str = dados.get('horario')

    if not (id_turma and sala and data_reserva_str and horario_str):
        return jsonify({"erro": "Dados incompletos"}), 400

    # Conversão das datas e horários
    try:
        data_reserva = datetime.strptime(data_reserva_str, '%Y-%m-%d').date()
        horario = datetime.strptime(horario_str, '%H:%M').time()
    except ValueError:
        return jsonify({"erro": "Formato de data ou horário inválido"}), 400

    # Validação da turma
    try:
        response = requests.get(f"{API_GERENCIAMENTO_URL}/{id_turma}")
        if response.status_code != 200:
            return jsonify({"erro": "ID da turma inválido"}), 400
    except requests.exceptions.RequestException:
        return jsonify({"erro": "Erro na comunicação com API de gerenciamento"}), 500

    nova_reserva = Reserva(
        id_turma=id_turma,
        sala=sala,
        data_reserva=data_reserva,
        horario=horario
    )

    db.session.add(nova_reserva)
    db.session.commit()

    return jsonify(nova_reserva.to_dict()), 201
