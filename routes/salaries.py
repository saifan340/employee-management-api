from flask import Blueprint, jsonify

salaries_bp = Blueprint('salaries', __name__)

@salaries_bp.route('/salaries', methods=['GET'])
def get_salaries():
    return jsonify({"message": "Salaries works!"})