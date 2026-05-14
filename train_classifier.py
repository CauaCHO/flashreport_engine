
"""
Treinamento inicial de classificador clássico.

Formato esperado:
dataset/processed/train.csv

Colunas:
text,label

Exemplo:
"cliente sem internet troquei conector voltou",SUBSTITUICAO_CONECTOR
"youtube trava na tv celular funciona",FALHA_TERCEIRO
"""

from pathlib import Path
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

DATASET = Path("dataset/processed/train.csv")
MODEL_PATH = Path("models/fre_intent_classifier.joblib")

if not DATASET.exists():
    raise FileNotFoundError("Crie o arquivo dataset/processed/train.csv com colunas text,label")

df = pd.read_csv(DATASET)

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))

MODEL_PATH.parent.mkdir(exist_ok=True)
joblib.dump(model, MODEL_PATH)

print("Modelo salvo em:", MODEL_PATH)
