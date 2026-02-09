from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class HealthCheck(Resource):
    def get(self):
        return {'status': 'ok', 'message': 'Backend is running'}

api.add_resource(HealthCheck, '/api/health')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
