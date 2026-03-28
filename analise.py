import pandas as pd

# Carregar dados
df = pd.read_csv("dados.csv")

print("📊 Dados carregados:")
print(df)

# Peso médio
media_peso = df["peso"].mean()
print(f"\n📈 Peso médio: {media_peso:.2f} kg")

# Caminhões com excesso
excesso = df[df["status"] == "EXCESSO"]
print(f"\n🚨 Caminhões com excesso de peso: {len(excesso)}")

# Maior peso registrado
maior_peso = df["peso"].max()
print(f"\n⚖️ Maior peso registrado: {maior_peso} kg")

# Agrupar por data
por_dia = df.groupby("data")["peso"].mean()
print("\n📅 Média de peso por dia:")
print(por_dia)

# Exportar relatório
por_dia.to_csv("relatorio_por_dia.csv")

print("\n✅ Relatório gerado: relatorio_por_dia.csv")