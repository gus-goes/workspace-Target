def calcular_percentual(faturamento_por_estado):
  total = sum(faturamento_por_estado.values())
  for estado, valor in faturamento_por_estado.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")

# Dados do enunciado
faturamento = {
  'SP': 67836.43,
  'RJ': 36678.66,
  'MG': 29229.88,
  'ES': 27165.48,
  'Outros': 19849.53
}
calcular_percentual(faturamento)