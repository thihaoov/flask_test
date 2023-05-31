from flask import Blueprint, jsonify

cms_blueprint = Blueprint('cms', __name__)

@cms_blueprint.route('/cms_endpoint', methods=['POST'])
def handle_cms_endpoint():
    # CMS logic goes here
    response = {'message': 'CMS endpoint executed successfully'}
    return jsonify(response)

@cms_blueprint.route('/register', methods=['POST'])
def client_register():
    # CMS logic goes here
    response = {'message': 'Register endpoint executed successfully'}
    return jsonify(response)