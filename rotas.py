# -*- coding: utf-8 -*-
# Título: App Principal
# Descrição: Inicialização do servidor Flask e registro das Blueprints
# Data: 28/04/2026
# _author_ = "Rafael Neves Nascimento"
# _email_ = "rafael.nascimento6@aluno.cps.sp.gov.br"
# _turma_ = "DSM - 3º Semestre / Noturno"
# _version_ = "1.0.0"

from flask import Blueprint, request, render_template

# Criando a blueprint chamada 'rotas' conforme a nota do exercício
rotas_bp = Blueprint('rotas', __name__)

# --- Desafio 1 ---
# Crie uma rota chamada "/message" que retorne "Cadastro Salvo com sucesso"
@rotas_bp.route('/message', methods=['GET'])
def message():
    return "Cadastro Salvo com sucesso"

# --- Desafio 2 ---
# Crie uma segunda rota chamada "/message/<status>" e retorne segundo a tabela
@rotas_bp.route('/message/<status>', methods=['GET'])
def message_status(status):
    # Tabela de status do enunciado mapeada em um dicionário (Mensagem, Código HTTP)
    tabela_status = {
        "200": ("200 OK: Sucesso geral.", 200),
        "201": ("201 Created: Sucesso na criação.", 201),
        "400": ("400 Bad Request: Erro do cliente (sintaxe).", 400),
        "401": ("401 Unauthorized: Falta autenticação.", 401),
        "404": ("404 Not Found: Recurso não encontrado.", 404),
        "500": ("500 Internal Server Error: Erro no servidor.", 500)
    }
    
    # Se o status digitado na URL existir na tabela, retorna a mensagem e o código correto
    if status in tabela_status:
        mensagem, codigo = tabela_status[status]
        return mensagem, codigo
    
    # Caso digitem um status que não está no PDF
    return "Status não encontrado na tabela do exercício.", 400


# --- Desafio 3 ---
# Rota de login que exibe o formulário em GET e valida em POST
@rotas_bp.route('/auth/login', methods=['GET', 'POST'])
def auth_login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
    
        if usuario == "genivaldo" and senha == "jerusa":
            return "200 OK: Sucesso geral.", 200
        
        return "401 Unauthorized: Falta autenticação.", 401

    return render_template('login.html')

from flask import jsonify # Certifique-se de que o jsonify esteja importado lá em cima se necessário

# --- Desafio 4: Validação de CPF (POST) ---
# Recebe nome e cpf de um cliente e faz uma validação simples
@rotas_bp.route('/cliente/valida', methods=['POST'])
def valida_cpf():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    
    # Tratamento simples tirando pontos e traços para validar se tem 11 números
    cpf_limpo = str(cpf).replace(".", "").replace("-", "").strip() if cpf else ""
    
    if len(cpf_limpo) == 11 and cpf_limpo.isdigit():
        return jsonify({
            'status': 200,
            'mensagem': "200 OK: Sucesso geral. CPF válido."
        }), 200
    else:
        return jsonify({
            'status': 400,
            'mensagem': "400 Bad Request: Erro do cliente (sintaxe). CPF inválido."
        }), 400


# --- Desafio 5: Conversão de Temperatura (GET Dinâmico) ---
# Recebe um float na URL e converte de Celsius para Fahrenheit
@rotas_bp.route('/convert/celsius/<float:temp>', methods=['GET'])
def converte_temperatura(temp):
    # Fórmula exigida: F = C * 1.8 + 32
    fahrenheit = temp * 1.8 + 32
    return jsonify({
        'valor_original_celsius': temp,
        'conversao_fahrenheit': fahrenheit
    }), 200


# --- Desafio 6: Filtro de Busca via Querystring (GET) ---
# Captura o parâmetro 'q' que vem depois da interrogação (?q=termo)
@rotas_bp.route('/search', methods=['GET'])
def search():
    q = request.args.get('q') # Captura o parâmetro de busca
    
    if q: # Se o parâmetro estiver presente e não vazio
        return f"Você pesquisou por: {q}", 200
        
    # Se 'q' estiver ausente ou vazio
    return "Parâmetro de busca obrigatório", 400

# --- Desafio 7: Validação de Maioridade (POST) ---
# O servidor recebe nome e idade. Barra menores de 18 anos.
@rotas_bp.route('/api/register', methods=['POST'])
def api_register():
    # Coletando os dados enviados por formulário
    nome = request.form.get('nome')
    idade_raw = request.form.get('idade')
    
    if not idade_raw:
        return jsonify({"erro": "Idade é obrigatória"}), 400
        
    idade = int(idade_raw)
    
    if idade < 18:
        return jsonify({"erro": "Cadastro permitido apenas para maiores de idade"}), 403
        
    return f"Usuário {nome} cadastrado", 201


# --- Desafio 8: Simulador de Estoque (GET) ---
# Retorna uma lista de dicionários contendo produtos.
@rotas_bp.route('/products', methods=['GET'])
def products():
    # Lista fixa de dicionários com id, nome e preco
    lista_produtos = [
        {"id": 1, "nome": "Teclado Mecânico", "preco": 350.00},
        {"id": 2, "nome": "Mouse Gamer", "preco": 180.00},
        {"id": 3, "nome": "Monitor 144hz", "preco": 1200.00}
    ]
    
    # REGRA: Se a lista estiver vazia, retorna status 204 No Content
    if not lista_produtos:
        return "", 204
        
    return jsonify(lista_produtos), 200


# --- Desafio 9: Header de Segurança Personalizado (GET) ---
# Verifica se existe o cabeçalho X-Api-Key correto
@rotas_bp.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    # Capturando o header personalizado
    api_key = request.headers.get('X-Api-Key')
    
    if api_key == "secret123":
        return "Acesso ao painel administrativo liberado", 200
        
    return "Unauthorized", 401