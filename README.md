# FRE Semantic Core — Training Ready

Motor semântico operacional ISP separado de Telegram e separado de Ollama.

## Objetivo

Este projeto não tenta ser um ChatGPT. Ele é uma base para um especialista operacional ISP.

Ele já possui:

- Correção operacional de texto
- Normalização linguística
- Tokenização
- Extração de entidades
- Relações verbo → alvo
- Grafo semântico operacional
- Inferência contextual
- Geração de relatório técnico
- Estrutura para treinamento posterior
- Classificador clássico inicial com scikit-learn
- Preparação futura para PyTorch, Transformers, embeddings e ONNX

## Rodar

```bash
pip install -r requirements.txt
python main.py
```

## Testar exemplos

Dentro do sistema:

```txt
:testes
```

## Preparar dataset inicial

```bash
python prepare_dataset.py
```

## Treinar classificador inicial

```bash
python train_classifier.py
```

## Dataset esperado

Arquivo:

```txt
dataset/processed/train.csv
```

Formato:

```csv
text,label
"cliente sem internet troquei conector voltou",SUBSTITUICAO_CONECTOR
"youtube trava na tv celular funciona",FALHA_TERCEIRO
```

## Próxima evolução

Quando você tiver mais relatórios reais:

1. Exporta os textos.
2. Limpa e coloca em `dataset/processed/train.csv`.
3. Treina o classificador.
4. Depois adiciona embeddings/sentence-transformers.
5. Depois exporta para ONNX se quiser performance.
