
import re
from fre_core.utils import load_json, remove_accents

class LanguageProcessor:
    def __init__(self):
        self.rules = load_json("fre_core/data/language_rules.json")

    def correct(self, text):
        fixed = text

        for old, new in self.rules["phrase_fixes"].items():
            fixed = re.sub(re.escape(old), new, fixed, flags=re.IGNORECASE)

        tokens = re.findall(r"[A-Za-zÀ-ÿ0-9_\.\-]+|[^\w\s]", fixed, flags=re.UNICODE)
        out = []

        for token in tokens:
            out.append(self.rules["word_fixes"].get(token.lower(), token))

        result = ""
        for token in out:
            if token in ".,;:!?":
                result = result.rstrip() + token + " "
            else:
                result += token + " "

        return re.sub(r"\s+", " ", result).strip()

    def normalize(self, text):
        low = remove_accents(text.lower())

        for old, new in self.rules["normalization"].items():
            low = low.replace(old, new)

        low = re.sub(r"[^a-z0-9\.\-\s\/]", " ", low)
        return re.sub(r"\s+", " ", low).strip()

    def tokenize(self, normalized):
        return normalized.split()
