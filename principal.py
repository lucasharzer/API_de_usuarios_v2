from flask import Flask
from flask_restful import Api
from recursos.usuario import Usuarios, Usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuarios/<string:usuario_id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)

#http://127.0.0.1:5000/ 