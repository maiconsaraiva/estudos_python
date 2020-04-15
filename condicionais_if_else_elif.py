"""
Estruturas condicionais
if (Se), else (Se não), elif (Se não, se)
"""

idade = int(input("Sua idade?"))

if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')

"""
Exemplo de como seria a estrutura acima em Delphi:
var
  idade : integer;
begin
  idade := InputQuery('Qual a sua idade?','Idade',0);
  
  if idade >= 18 then
    ShowMessage('Você é maior de idade!');
  else
    ShowMessage('Você é menor de idade!');  
end;
"""

# Uso do elif
if idade >= 18:
    print('Você é adulto!')
elif (idade < 18) and (idade > 12):
    print('Você é adolescente!')
else:
    print('Você é uma criança!')


