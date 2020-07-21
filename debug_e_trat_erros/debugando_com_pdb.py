"""
Aula 77 - Debugando código Python com o PDB (Python Debugger)

- IDE's como Pycharm e VS Code já tem integração natia com o PDB. Quando usamos as funções de debug dessas ferramentas
  o PDB do Python é acionado automaticamente.
- E quando não estivermos usando uma IDE é possível fazer o debug importando e usando o PDB nos códigos.
- A utilização de print's para debugar é uma prática ruim para debugar código. No Python, podemos usar o PDB para
  debugar de forma profissional.


Como fazer:
  1. incluir o import: import PDB
  2. incluir o "break" point do PDB: pdb.set_trace()
  3. Feito isso, ao rodar a aplicação, ela será pausada no local indicado;
  4. A partir dai, poderemos ir navegando linha a linha do código, tal como nas IDE's. Porém, diferente dos atalhos
     que facilitam a navegação nas IDE's (F7, F8, etc.) no PDB essa navegação é feita via comandos.
     Comandos básicos do PDB:
     l -> Lista onde estamos no código
     n -> Próxima linha
     p -> imprime variável
     c -> continua a execução (finaliza o debugging)


O debug de forma manual é interessante e necessário, quando precisamos debugar um código que está em produção, mas não
há uma IDE ou ambiente de desenvolvimento instalado.

Observações
- Opcionalmente, o import do PDB pode ser feito diretamente na linha que queremos utilizar, junto ao set_trace().
  Ex: import pdb; pdb.set_trace()
  Repare que neste caso específico o ";" (ponto e vírgula) é usado para permitir os dois comandos.
  Esse uso é comum quando queremos inserir o PDB somente para debugar, e depois já removemos.

- À partir da versão 3.7 do Python, o PDB foi incorporado de forma nativa, como built-in (integrada).
  Não precisamos mais fazer o import. Podemos simplesmente incluir a função breakpoint()

- Cuidado com conflito entre nomes de variáveis e os comandos do PDB. Se houver esse conflito, o comando terá
  prioridade, porém podemos usar o comando "p" do PDB para imprimir a variável,
  basta usar a sintaxe: p nome_variavel

- Evite colocar nomes simples demais em variáveis, sempre tente dar nomes significativos.
"""

"""
# Exemplo 1:
import pdb


def dividir(a, b):
    return float(a) / float(b)


try:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    res = dividir(num1, num2)
    pdb.set_trace()
    print(res)
except (ValueError, ZeroDivisionError) as err:
    print(f'Divisão inválida: {err}')
"""

"""
# Exemplo 2, com o PDB sendo importando diretamente na linha que será usado.
try:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    import pdb; pdb.set_trace()
    res = num1 / num2
    print(res)
except (ValueError, ZeroDivisionError) as err:
    print(f'Divisão inválida: {err}')
"""

# Exemplo 3, usando o breakpoint(), nativo à partir do Python 3.7
try:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    breakpoint()
    res = num1 / num2
    print(res)
except (ValueError, ZeroDivisionError) as err:
    print(f'Divisão inválida: {err}')

