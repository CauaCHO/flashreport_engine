# Arquitetura FRE Semantic Core

```txt
Texto bruto
↓
Correção operacional
↓
Normalização
↓
Tokenização
↓
Morfologia básica
↓
Extração de entidades
↓
Relações verbo → alvo
↓
Grafo semântico ISP
↓
Inferência contextual
↓
Classificação
↓
Relatório técnico
```

## Camadas futuras

```txt
PyTorch
Transformers
Tokenizer treinado/adaptado
Embeddings
FAISS/Chroma
ONNX export
```

## Stack recomendada

- Python: lógica principal
- scikit-learn: classificador inicial
- PyTorch: treinamento futuro
- Transformers: modelos futuros
- sentence-transformers: embeddings
- ONNX: exportação futura
