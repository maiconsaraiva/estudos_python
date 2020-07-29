"""
Decoradores (Decorators)

O que são?

- Decorators são funções;
- Decorators envolvem outras funções, e aprimoram seus comportamentos;
- Decorators também são exemplos de HOF (Higher Order Functions);
- Decorators tem uma sintaxe própria, usando o "@" (Syntax Sugar / Açucar Sintático)


- Não confunda Decorators com Decorator Function
  - Decorator Function é a função propriamente dita que é usada para decorar a função desejada
  - Decorator é o uso/aplicação do Decorator Function na função desejada.

"""


# Decorators como funções (forma não recomendada, sintaxe não recomendada, Sem Açucar Sintático)
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo(a) à Geek University')


# Testando 1 (forma não recomendada)
teste = seja_educado(saudacao)
teste()


# Decoradores com Syntax Sugar / Açucar Sintático

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


# O "@" é o chamado Açucar Sintático (Existe em Python, Java Ruby e outras que usam iterators)
@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando 2
apresentando()


"""
Exemplo prático:
Imagime que você um site e 4 itens de menu
|-------------------------------------------|
|Home | Serviços | Produtos | Administrativo|
|-------------------------------------------|

links:
/home
/servicos
/produtos
/admin

# Obs: Não é código funcional, é apenas um exemplo

def checa_login(request):
    if not request.usuario:
        redirect('/home')
    usuarios_admins = ['maicon', 'glenda']
    it not request.usuario in usuarios_admins:
        redirect('/home')


def home(request):
    return 'Pode acessar a Home'


def servicos(request):
    return 'Pode acessar serviços'


def produtos(request):
    return 'Pode acessar Produtos'

@checa_login  # << Neste exemplo a função que dá acesso ao admin checa antes o login do usuário.
def admin(request):
    return 'Pode acessar Admin'

Supondo que você queira que apenas usuários com acesso administrativos possam acessar o menu Administrativo
"""
