# -*- coding: utf-8 -*-
# Título: App Principal
# Descrição: Inicialização do servidor Flask e registro das Blueprints
# Data: 28/04/2026
# _author_ = "Rafael Neves Nascimento"
# _email_ = "rafael.nascimento6@aluno.cps.sp.gov.br"
# _turma_ = "DSM - 3º Semestre / Noturno"
# _version_ = "1.0.0"

from flask import Flask
from rotas import rotas_bp
import paginas  # Importa o arquivo sem acento

app = Flask(__name__)

# Registra as duas Blueprints no aplicativo
app.register_blueprint(rotas_bp)
app.register_blueprint(paginas.paginas_bp)

if __name__ == '__main__':
    app.run(debug=True)