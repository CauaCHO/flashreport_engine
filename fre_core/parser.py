
from fre_core.utils import load_json

class SemanticParser:
    def __init__(self):
        self.knowledge = load_json("fre_core/data/isp_knowledge.json")
        self.verbs = self.knowledge["verbs"]

    def parse_relations(self, normalized):
        tokens = normalized.split()
        relations = []

        for i, token in enumerate(tokens):
            if token in self.verbs:
                window = tokens[i+1:i+9]

                for target, intent in self.verbs[token].items():
                    if target in window:
                        relations.append({
                            "verb": token,
                            "target": target,
                            "intent": intent
                        })

        return relations

    def morphology(self, normalized):
        tokens = normalized.split()
        possible_verbs = [t for t in tokens if t in self.verbs or t.endswith("ei") or t.endswith("ou")]
        possible_nouns = [t for t in tokens if t not in possible_verbs and len(t) > 2]

        return {
            "tokens": tokens,
            "possible_verbs": possible_verbs,
            "possible_nouns": possible_nouns
        }
