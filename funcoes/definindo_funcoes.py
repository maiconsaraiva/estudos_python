"""
Definindo funções

- São pequenas partes do nosso código que executam uma tarefa específica;
- Pode ou não receber entrada de dados (parâmetros) e retornar uma saída de dados;
- Muito úteis quando precisamos executar rotinas simulares diversas vezes. Usando uma função, evitamos a repetição de
código

Obs: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a
função seja simplificada.

As funções seguem uma das premissas do Zen do Python:
- DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

Já utilizamos várias funções de que iniciamos o curso:
- print()
- len()
- min()
- max()
- count()
- E muitas outras.


Em Python a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_de_codigos_da_funcao

Para definir uma função e específica os tipos de entrada e saída de dados usamos:

def nome_da_funcao(parametro1 : int, parametro2: str) -> int
    bloco_de_codigos_da_funcao
    # Obs: o retorno foi específicado que é um "int"

Regras:
- Sempre use letras minúsculas no nome da função;
- Se for um nome composto, mantenha em minusculo e separe as palavras por "_" (underline). É chamado de Snake Case;
- Os parâmetros de entrada são opcionais, se tiver mais de um, cada um deles fica separado por um a vírgula;
- Os parâmetros também podem ser opcionais, neste caso define-se no escopo da função um valor default para aquele
  parâmetro, caso ele não seja passado na chamada da função;
- bloco_de_codigos_da_funcao: Também chamados de corpo da função ou implementação, é onde o processamento da função
  acontece.

Obs: Veja que para definir uma função, utilizamos a palavra reservada "def" informando ao Python que estamos definindo
uma função. Também abrimos o bloco com o já conhecido ":" (dois pontos) que utilizamos no Python para definir blocos.

Obs2: Em python podemos criar uma variável do tipo de uma função e executar esta função através da variável. (mas seu
uso não é muito comum)

"""


# Exemplo: definindo uma função
def diz_oi():
    print('Oi')


# Utilizando a função (chamada de execução)
diz_oi()

# ATENÇÃO: Nunca esqueça de usar o parenteses ao executar uma função.
# No exemplo abaixo, não dará erro, mas também não será executada a função diz_oi()
diz_oi


# Executando diz_oi n vezes
for n in range(1, 11):
    print(n)
    diz_oi()


# Exemplo cirando variável que aponta para a função (não é recomendado)
diz = diz_oi
diz()
