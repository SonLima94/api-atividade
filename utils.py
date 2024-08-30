from models import Pessoas

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Lima',idade=29)
    print(pessoa)
    pessoa.save()

#Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Rayrison').first()
    print(pessoa.idade)
#Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lima').first()
    pessoa.nome = 'Son'
    pessoa.save()

#Exclui dados da tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Son').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('Rayrison', '1234')
    insere_usuario('Lima', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()