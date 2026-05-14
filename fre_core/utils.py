
import json
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

def load_json(path):
    p = BASE / path
    return json.loads(p.read_text(encoding="utf-8"))

def save_json(path, data):
    p = BASE / path
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def remove_accents(text):
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))

def unique(items):
    out = []
    for item in items:
        if item and item not in out:
            out.append(item)
    return out
