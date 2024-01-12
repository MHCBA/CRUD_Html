from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from class_pessoa.create_base import User
from sqlalchemy import delete
engine = create_engine("postgresql://postgres:cTI*x64]@localHost:5432/Michell_teste", echo=True) #cria conexão com banco de dados
Session = sessionmaker(bind=engine)
session = Session()
def excluir_valores(coluna, id):
    user = session.query(User).get(id)

    if coluna == 'tudo':
        # Excluir todos os valores do usuário
        session.delete(user)
    session.commit()
    return 'Usuario deletado!'