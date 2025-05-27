from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

@app.route('/')
def home():
    return jsonify({"message": "API is running - versão teste automático!"}), 200


@app.route('/login', methods=['POST'])
def login():
    access_token = create_access_token(identity="usuario_exemplo")
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "Você acessou um recurso protegido"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
