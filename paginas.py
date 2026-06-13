# -*- coding: utf-8 -*-
# Título: App Principal
# Descrição: Inicialização do servidor Flask e registro das Blueprints
# Data: 28/04/2026
# _author_ = "Rafael Neves Nascimento"
# _email_ = "rafael.nascimento6@aluno.cps.sp.gov.br"
# _turma_ = "DSM - 3º Semestre / Noturno"
# _version_ = "1.0.0"

from flask import Blueprint, render_template

# Criando a blueprint com nome simples para evitar problemas de rota no core do Flask
paginas_bp = Blueprint('paginas', __name__)

@paginas_bp.route('/', methods=['GET'])
@paginas_bp.route('/home', methods=['GET'])
def home():
    # O Flask busca automaticamente dentro de 'templates', então indicamos a subpasta física
    return render_template('páginas/layout.html', title='Página Inicial')