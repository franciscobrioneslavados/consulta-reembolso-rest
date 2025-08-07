from flask import Blueprint, request, jsonify
from models import db, Boleta
import logging

bp = Blueprint('routes', __name__)

@bp.route('/boletas', methods=['POST'])
def create_boleta():
    try:
        data = request.get_json()
        boleta = Boleta(**data)
        db.session.add(boleta)
        db.session.commit()
        logging.info(f'Boleta creada: {boleta.id_}')
        return jsonify({"message": "Boleta creada", "id": boleta.id_}), 201
    except Exception as e:
        logging.error(f'Error creando boleta: {str(e)}')
        return jsonify({"error": "Error al crear boleta"}), 500

@bp.route('/boletas/<int:id_>', methods=['GET'])
def get_boleta(id_):
    boleta = Boleta.query.get(id_)
    if not boleta:
        return jsonify({"error": "Boleta no encontrada"}), 404
    return jsonify({
        "id_": boleta.id_,
        "id_boleta": boleta.id_boleta,
        "key_boleta": boleta.key_boleta,
        "procesa_isapre": boleta.procesa_isapre,
        "response_isapre": boleta.response_isapre,
        "key_response_isapre": boleta.key_response_isapre,
        "procesa_seguro": boleta.procesa_seguro,
        "response_seguro": boleta.response_seguro,
        "half": boleta.half
    })

@bp.route('/boletas', methods=['GET'])
def get_all_boletas():
    boletas = Boleta.query.all()
    return jsonify([
        {
            "id_": b.id_,
            "id_boleta": b.id_boleta,
            "key_boleta": b.key_boleta,
            "procesa_isapre": b.procesa_isapre,
            "response_isapre": b.response_isapre,
            "key_response_isapre": b.key_response_isapre,
            "procesa_seguro": b.procesa_seguro,
            "response_seguro": b.response_seguro,
            "half": b.half
        } for b in boletas
    ])

@bp.route('/boletas/<int:id_>', methods=['PUT'])
def update_boleta(id_):
    boleta = Boleta.query.get(id_)
    if not boleta:
        return jsonify({"error": "Boleta no encontrada"}), 404
    data = request.get_json()
    for key, value in data.items():
        if hasattr(boleta, key):
            setattr(boleta, key, value)
    db.session.commit()
    logging.info(f'Boleta actualizada: {id_}')
    return jsonify({"message": "Boleta actualizada"})

@bp.route('/boletas/<int:id_>', methods=['DELETE'])
def delete_boleta(id_):
    boleta = Boleta.query.get(id_)
    if not boleta:
        return jsonify({"error": "Boleta no encontrada"}), 404
    db.session.delete(boleta)
    db.session.commit()
    logging.info(f'Boleta eliminada: {id_}')
    return jsonify({"message": "Boleta eliminada"})