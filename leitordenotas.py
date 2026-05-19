import json

dados = {
  "matematica": 8.5,
  "portugues": 9.0,
  "soma" : 0
}


matematica = dados["matematica"]
portugues = dados["portugues"]


soma = matematica + portugues
dados["soma"] = soma

with open("notas.json", "a", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)

print("Notas carregadas:")
print(f"Matemática: {matematica}")
print(f"Português: {portugues}")
print(f"Soma das notas: {soma}")