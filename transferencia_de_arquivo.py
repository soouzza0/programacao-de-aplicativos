pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"] 
concluidos = []
print(f"arquivo antigo pendente{pendentes}concluido{concluidos}")
pendentes.pop(0)
concluidos.append("relatorio.pdf")
print(f"arquivo novo pendente{pendentes}concluido{concluidos}")