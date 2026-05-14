
from fre_core.utils import load_json, unique

class ContextInterpreter:
    def __init__(self):
        self.knowledge = load_json("fre_core/data/isp_knowledge.json")
        self.patterns = self.knowledge["patterns"]
        self.graph = self.knowledge["semantic_graph"]

    def match(self, normalized, category):
        found = []

        for code, terms in self.patterns[category].items():
            if any(term in normalized for term in terms):
                found.append(code)

        return unique(found)

    def infer_graph(self, entities):
        links = []

        for item in entities.get("equipment", []):
            if item in self.graph:
                for target in self.graph[item]:
                    links.append({"source": item, "target": target})

        for app in entities.get("apps", []):
            key = app.lower()
            if key in self.graph:
                for target in self.graph[key]:
                    links.append({"source": key, "target": target})

        return links

    def interpret(self, normalized, entities, relations):
        context = {
            "problems": self.match(normalized, "problems"),
            "actions": self.match(normalized, "actions"),
            "results": self.match(normalized, "results"),
            "relations": relations,
            "semantic_links": self.infer_graph(entities)
        }

        for rel in relations:
            if rel["intent"] not in context["actions"]:
                context["actions"].append(rel["intent"])

        # Inferência TV/celular/app
        if ("celular" in normalized and ("funciona" in normalized or "funcionou" in normalized or "normal" in normalized)) and any(x in normalized for x in ["tv", "iptv", "tvbox", "youtube", "netflix"]):
            if "PROBLEMA_LOCAL_DISPOSITIVO" not in context["problems"]:
                context["problems"].append("PROBLEMA_LOCAL_DISPOSITIVO")
            if "DIAGNOSTICO_COMPARATIVO" not in context["actions"]:
                context["actions"].append("DIAGNOSTICO_COMPARATIVO")
            if "INTERNET_OK" not in context["results"]:
                context["results"].append("INTERNET_OK")

        # IPTV/TVBox tende a terceiro
        if any(x in normalized for x in ["iptv", "tvbox", "lista iptv"]):
            if "FALHA_TERCEIRO" not in context["problems"]:
                context["problems"].append("FALHA_TERCEIRO")

        # Resultado comum
        if "voltou" in normalized or "normalizou" in normalized or "funcionou" in normalized:
            if "NORMALIZADO" not in context["results"]:
                context["results"].append("NORMALIZADO")

        return context
