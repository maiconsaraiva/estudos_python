"""
Teste de velocidade com expressões geradoras

# Generators
def nums():
    for num in range(1, 10):
        yield num

gen = nums()

print(gen)  # <generator object nums at 0x011FB4F8>
print(next(gen))  # 1
print(next(gen))  # 2


# Generator Expression (visto nas aulas sobre generators)
gen2 = (num for num in range(1, 10))
print(gen2)  # <generator object <genexpr> at 0x0125B488>

"""

# Realizando Teste de Velocidade
import time

gen_inicio = time.time()

print(sum(num for num in range(10_000_000)))  # 10 milhões
gen_duracao = time.time() - gen_inicio

# List Comprehension
# Obs: No List Comprehension, deu o erro MemoryError ao executar com um range de 100 milhões,
# e a memóriua usada pelo Python subiu rápido para mais de 1gb. Para conseguir executar o teste completo, diminui para 10 milhões
list_inicio = time.time()
print(sum([num for num in range(10_000_000)]))
list_duracao = time.time() - list_inicio

print(f'Generator Expression, time: {gen_duracao}')  # 1.0457348823547363
print(f'List Comprehension, time: {list_duracao}')  # 0.9194178581237793
