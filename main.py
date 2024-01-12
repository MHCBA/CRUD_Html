from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.orm.attributes import flag_modified

from function_py.validador import validar_valor
from class_pessoa.create_base import User # importando a classe User que é responsavel por selecionar o banco de dados e criar um, caso não exista.
from function_py.delete import excluir_valores
from function_py.validador_formulario import validar_valor_forms


engine = create_engine("postgresql://postgres:cTI*x64]@localHost:5432/Michell_teste", echo=True) #cria conexão com banco de dados
Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__) #instaciando a variavel app


@app.route('/')  #criando rota para a variavel app
def home():
    return redirect(url_for('index'))



@app.route('/home/')
def index():
    return render_template('2024.html')


#criar
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    mensagem = ''
    if request.method == 'POST':
        idade_request = request.form['idade']
        nome_request = request.form['nome']
        idade_request = request.form['idade']
        email_request = request.form['email']
        senha_request = request.form['senha']
        print(nome_request, idade_request, email_request, senha_request)
        validar = validar_valor_forms(idade_request)
        if validar == True:
            novo_usuario = User(
                nome = nome_request,
                idade = idade_request,
                email = email_request,
                senha = senha_request)
            
            session.add_all([novo_usuario])
            session.commit()
            mensagem = 'valores validos'
        elif validar == False:
            mensagem = 'valor idade: invalido'
    
    return render_template('formulario.html', mensagem=mensagem)


@app.route('/sobremim')
def sobremim():
    return render_template('sobremim.html')


#ler
@app.route('/lista_usuarios')
def lista_usuarios():
    dados_p = select(User)
    dados = session.scalars(dados_p)
    print('.............:', dados)
    return render_template('lista_usuarios.html', dados_p=dados_p,dados=dados)


@app.route('/alterar', methods=['GET', 'POST'] )
def alterar():
    # selecionar todos os usuários
    dados_p = select(User)
    dados = session.scalars(dados_p)

    # selecionar usuário por id
    # if request.method == 'POST':
    selecione_request = request.form.get('selecione')
    print('retorno de select.........:', selecione_request)

    user_selected = session.get(User, selecione_request)
    print("result with get...............", user_selected)
        
    # print('retorno de select.......:', selecione_request)
    return render_template('alterar.html', dados=dados, user_selected=user_selected, selecione_request=selecione_request)


@app.route('/alterar_2/<id>', methods=['GET', 'POST'])
def alterar_2(id):
    dados_p = select(User)
    dados = session.scalars(dados_p)
    coluna = request.form.get('coluna')
    novo_valor = request.form.get('atualizado')
    mensagem = ''
    user_selected = session.get(User, id)
    validado = validar_valor(coluna, novo_valor)
    if novo_valor != None and validado == True:
        mensagem = f'O valor {novo_valor} é válido para a coluna {coluna}.'
        user = session.query(User).get(id)
        setattr(user, coluna, novo_valor)

        # Informe ao SQLAlchemy que a coluna foi modificada
        flag_modified(user, coluna)

        # Commit para salvar as alterações no banco de dados
        session.commit()
    elif novo_valor != None and validado == False:
        mensagem = f'O valor {novo_valor} não é válido para a coluna {coluna}.'
    print('OPÇÃO RECEBIDA NO BACKEND: ', coluna, novo_valor)

    print('ID-------------', user_selected)
    return render_template('alterar_2.html',mensagem=mensagem, id=id, user_selected=user_selected, novo_valor=novo_valor, dados=dados)

    
@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    mensagem = ''
    coluna = request.form.get('coluna')
    if request.method == 'POST':
        mensagem = excluir_valores(coluna, id)
    print('@@@@@@@@@@@@@ ------->', coluna)
    user_selected = session.get(User, id)
    
    return render_template('delete.html', id=id, user_selected=user_selected, mensagem=mensagem)


if __name__ == '__main__': # rodar a rota
    app.run(debug = True)

    