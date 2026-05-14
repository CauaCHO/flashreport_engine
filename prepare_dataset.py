
"""
Cria um dataset inicial de exemplo para você substituir/expandir depois.
"""

from pathlib import Path
import pandas as pd

out = Path("dataset/processed/train.csv")
out.parent.mkdir(parents=True, exist_ok=True)

data = [
    ["cliente sem internet troquei conector voltou", "SUBSTITUICAO_CONECTOR"],
    ["subi na cto refiz ponta sinal voltou", "SUBSTITUICAO_CONECTOR"],
    ["troquei roteador antigo por zte ax3000 melhorou", "SUBSTITUICAO_ROTEADOR"],
    ["youtube trava na tv mas celular funciona normal", "FALHA_TERCEIRO"],
    ["iptv travando internet normal", "FALHA_TERCEIRO"],
    ["cliente falou que travava tudo troquei canal voltou", "ALTERACAO_CANAL_WIFI"],
    ["wifi ruim alterei canal ficou bom", "ALTERACAO_CANAL_WIFI"],
    ["cliente ausente nao atendeu", "CLIENTE_AUSENTE"],
    ["link loss sem sinal fibra", "LINK_LOSS"],
    ["sinal baixo na onu refiz conector", "SINAL_BAIXO"]
]

df = pd.DataFrame(data, columns=["text", "label"])
df.to_csv(out, index=False)

print("Dataset criado em:", out)
