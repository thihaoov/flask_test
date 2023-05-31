from flask import Flask, request, jsonify
from routes.business_routes import business_blueprint
from routes.cms_routes import cms_blueprint
from routes.processing_routes import processing_blueprint

app = Flask(__name__)

app.register_blueprint(business_blueprint)
app.register_blueprint(cms_blueprint)
app.register_blueprint(processing_blueprint)

@app.route('/', methods=['GET', 'POST'])
def main():
    return "home page"

@app.route('/example', methods=['POST'])
def example():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')

    response = {'message': [param1, param2]}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)