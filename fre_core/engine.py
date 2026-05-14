
from fre_core.language import LanguageProcessor
from fre_core.entities import EntityExtractor
from fre_core.parser import SemanticParser
from fre_core.context import ContextInterpreter
from fre_core.report import ReportGenerator

class FRESemanticCore:
    def __init__(self):
        self.language = LanguageProcessor()
        self.entities = EntityExtractor()
        self.parser = SemanticParser()
        self.context = ContextInterpreter()
        self.reporter = ReportGenerator()

    def confidence(self, context, entities):
        score = 0

        if context["problems"]:
            score += 30
        if context["actions"]:
            score += 30
        if context["results"]:
            score += 25
        if context["relations"]:
            score += 10
        if entities["equipment"] or entities["apps"]:
            score += 5

        return min(score, 100)

    def process(self, text):
        corrected = self.language.correct(text)
        normalized = self.language.normalize(corrected)
        tokens = self.language.tokenize(normalized)
        relations = self.parser.parse_relations(normalized)
        morphology = self.parser.morphology(normalized)
        entities = self.entities.extract(normalized, corrected)
        context = self.context.interpret(normalized, entities, relations)
        report = self.reporter.generate(context, entities, normalized)

        return {
            "original": text,
            "corrected": corrected,
            "normalized": normalized,
            "tokens": tokens,
            "morphology": morphology,
            "entities": entities,
            "relations": relations,
            "context": context,
            "confidence": self.confidence(context, entities),
            "report": report
        }
