import json

def analisar_faturamento(dados_json):
  faturamentos = [dia['valor'] for dia in dados_json if dia['valor'] > 0]
  menor_valor = min(faturamentos)
  maior_valor = max(faturamentos)
  media = sum(faturamentos) / len(faturamentos)
  dias_acima_media = sum(1 for valor in faturamentos if valor > media)
  return menor_valor, maior_valor, dias_acima_media

# Assumindo que os dados estão em um arquivo 'faturamento.json'
with open('dados.json', 'r') as f:
  dados = json.load(f)
  menor, maior, dias = analisar_faturamento(dados)
  print(f"Menor valor: {menor}")
  print(f"Maior valor: {maior}")
  print(f"Dias acima da média: {dias}")