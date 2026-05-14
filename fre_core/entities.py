
import re
from fre_core.utils import load_json, unique

class EntityExtractor:
    def __init__(self):
        self.knowledge = load_json("fre_core/data/isp_knowledge.json")
        self.entities = self.knowledge["entities"]

    def find_equipment(self, text):
        low = text.lower()
        found = []

        for eq, aliases in self.entities["equipments"].items():
            if any(alias.lower() in low for alias in aliases):
                found.append(eq)

        return unique(found)

    def find_list(self, text, key):
        low = text.lower()
        return [item for item in self.entities[key] if item.lower() in low]

    def extract_signal(self, text):
        m = re.search(r"(?:sinal|potencia|potência|dbm)?\s*(-\d{1,2}(?:\.\d+)?)\s*(?:dbm)?", text)
        if not m:
            return None

        value = float(m.group(1))

        if value <= -27:
            status = "potência óptica crítica/baixa"
        elif value >= -8:
            status = "potência óptica elevada"
        else:
            status = "potência óptica dentro de faixa operacional"

        return {"value": value, "status": status}

    def extract(self, normalized, corrected):
        merged = normalized + " " + corrected

        return {
            "equipment": self.find_equipment(merged),
            "brands": self.find_list(merged, "brands"),
            "models": self.find_list(merged, "models"),
            "apps": self.find_list(merged, "apps"),
            "signal": self.extract_signal(normalized)
        }
