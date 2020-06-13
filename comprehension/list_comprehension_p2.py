"""
List Comprehension

- Podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

"""

numeros = [1, 2, 3, 4, 5, 10, 20, 30, 50]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)  # [2, 4, 10, 20, 30, 50]

impares = [numero for numero in numeros if numero % 2 != 0]
print(impares)  # [1, 3, 5]

# outro
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)  # [0.5, 4, 1.5, 8, 2.5, 20, 40, 60, 100]
