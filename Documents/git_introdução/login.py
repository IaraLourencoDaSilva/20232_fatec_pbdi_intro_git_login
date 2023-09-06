import psycopg
##print(psycopg)

class Usuario: ##Classe apenas para explicar o usuario
    def __init__(self, login,senha): ##construtor da classe 
        self.login = login ## identificando o login, ou seja, o que existe  
        self.senha = senha ## identificando o senha, ou seja, o que existe  

def existe(usuario): ##Verificar se existe o usuario
    ## Abrir conexão com o PostgreSQL 
    with psycopg.connect(
        host='localhost',
        port='5432',
        dbname='20232_pbdi_login_python',
        user='postgres',
        password='123456'
    ) as conexao:
        print(conexao)
        ## Obter um cursor 
        with conexao.cursor() as cursor:
            ## usando o cursor, executar um comando select
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
                (usuario.login,usuario.senha)
            )
            ## usando o cursor, verificar o resultado
            resultado = cursor.fetchone()
            ## devolve True ou False
            return resultado != None ## Para simplificar a condição abaixo
            ##if resultado == None:
              ##  return False
            ## return True

##Teste 
##usuario = Usuario('admin', 'admin') ## Esta instanciando um usuario, ou seja, verificando se ele usuario existe no banco 
##print(existe(usuario))
def insercao(usuario):
    with psycopg.connect(
        host='localhost',
        port='5432',
        dbname='20232_pbdi_login_python',
        user='postgres',
        password='123456'
    ) as conexao:
        print(conexao)
        with conexao.cursor() as cursor:
            cursor.execute(
                'INSERT INTO tb_usuario (login, senha) VALUES(%s,%s)',
                (usuario.login,usuario.senha)
            )

def menu():
    texto = '1-Login\n2-Logoff\n3-inserir\n0-Sair' ##\n para pular linha
    usuario = None ## sempre que ele estiver logado 
    op= int(input(texto))
    while op!= 0:
        if op ==1:
            login = input("Digite o login")
            senha = input("Digite a senha")
            usuario = Usuario(login, senha)
            ##exibir Usuario NOK de acordo com 
            ##o método existe. Use o operador ternário
            print('Usuário Ok' if existe(usuario) else 'Usuário NOK')
        elif op == 2:
            usuario = None
            print('Usuário Ok')
        elif op == 3:
            login = input("Digite o login")
            senha = input("Digite a senha")
            insercao(Usuario(login,senha))
            print('Inserido com Sucesso')
        op = int(input(texto))
    else:
        print('Sair')

menu()