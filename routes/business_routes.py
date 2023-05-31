from flask import Blueprint, jsonify

business_blueprint = Blueprint('business', __name__)

@business_blueprint.route('/business_endpoint', methods=['POST'])
def handle_business_endpoint():
    # Business logic goes here
    response = {'message': 'Business endpoint executed successfully'}
    return jsonify(response)

@business_blueprint.route('/register_plan', methods=['POST'])
def register_plan_endpoint():
    # Business logic goes here
    response = {'message': 'Register plan endpoint executed successfully'}
    return jsonify(response)