from flask import Flask, request
from flask_restful import Resource, Api
from controllers import pessoa

app = Flask(__name__)
api = Api(app)


class Pessoas(Resource):
    def __init__(self):
        self.response = {}

    def get(self):

        self.response = {
            'nome': pessoa.create_nome(),
            'cpf': pessoa.create_cpf(),
            'nc_data': pessoa.create_data()
        }

        return self.response


# Rotas
api.add_resource(Pessoas, '/pessoa/')

if __name__ == '__main__':
    app.run(debug=True)
