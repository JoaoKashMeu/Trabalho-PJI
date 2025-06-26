from flask import Flask
from routes.usuario_routes import usuario_bp
from routes.licao_routes import licao_bp
from routes.exercicio_routes import exercicio_bp
from routes.progresso_routes import progresso_bp
from routes.estatistica_routes import estatistica_bp

app = Flask(__name__)

app.register_blueprint(usuario_bp, url_prefix='/usuarios')
app.register_blueprint(licao_bp, url_prefix='/licoes')
app.register_blueprint(exercicio_bp, url_prefix='/exercicios')
app.register_blueprint(progresso_bp, url_prefix='/progresso')
app.register_blueprint(estatistica_bp, url_prefix='/estatisticas')

if __name__ == '__main__':
    app.run(debug=True)