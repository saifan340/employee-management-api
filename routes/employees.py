from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Employee

emp_bp = Blueprint('employees', __name__)

@emp_bp.route('/employees', methods=['POST'])
@jwt_required()
def add_employee():
    data = request.get_json()
    user_id = get_jwt_identity()

    name = data.get('name')
    position = data.get('position')

    if not name or not position:
        return jsonify({"error": "Missing data"}), 400

    new_emp = Employee(name=name, position=position, user_id=user_id)
    db.session.add(new_emp)
    db.session.commit()

    return jsonify({"message": "Employee added"}), 201

@emp_bp.route('/employees', methods=['GET'])
@jwt_required()
def get_employees():
    user_id = get_jwt_identity()

    employees = Employee.query.filter_by(user_id=user_id).all()

    result = []
    for emp in employees:
        result.append({
            "id": emp.id,
            "name": emp.name,
            "position": emp.position
        })

    return jsonify(result)

@emp_bp.route('/employees/<int:id>', methods=['PUT'])
@jwt_required()
def update_employee(id):
    user_id = get_jwt_identity()
    emp = Employee.query.filter_by(id=id, user_id=user_id).first()

    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()

    emp.name = data.get('name', emp.name)
    emp.position = data.get('position', emp.position)

    db.session.commit()

    return jsonify({"message": "Employee updated"})

@emp_bp.route('/employees/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_employee(id):
    user_id = get_jwt_identity()
    emp = Employee.query.filter_by(id=id, user_id=user_id).first()

    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    db.session.delete(emp)
    db.session.commit()

    return jsonify({"message": "Employee deleted"})