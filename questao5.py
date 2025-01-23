def inverter_string(texto):
  texto_invertido = ""
  for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

texto = input("Digite uma string: ")
print(inverter_string(texto))