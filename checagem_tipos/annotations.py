"""
Annotations

# Correto:
texto: str

# Errado:
texto:str
texto : str

# Correto:
) -> str:

# Errado:
)->str:
) ->str:
)-> str:


# Correto
alinhamento: bool = True

# Errado:
alinhamento:bool=True
alinhamento: bool=True
alinhamento:bool = True
alinhamento:bool= True
"""
import math
from datetime import datetime


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)  # {'raio': <class 'float'>, 'return': <class 'float'>}

# Annotations servem também para variáveis, properties, entre outros.
nome: str = 'Maicon Saraiva'
idade: int = 30
vivo: bool = True
nascimento: datetime = datetime(1990, 7, 23, 0, 0, 0, 0)
