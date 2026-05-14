
from fre_core.engine import FRESemanticCore

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt
    from rich import box
except Exception:
    Console = None

fre = FRESemanticCore()

def show(result):
    if Console:
        console = Console()
        table = Table(title="FRE Semantic Core", box=box.ROUNDED)
        table.add_column("Campo", style="bold cyan")
        table.add_column("Valor")

        table.add_row("Original", result["original"])
        table.add_row("Corrigido", result["corrected"])
        table.add_row("Normalizado", result["normalized"])
        table.add_row("Tokens", str(result["tokens"]))
        table.add_row("Entidades", str(result["entities"]))
        table.add_row("Relações", str(result["relations"]))
        table.add_row("Contexto", str(result["context"]))
        table.add_row("Confiança", str(result["confidence"]) + "%")

        console.print(table)
        console.print(Panel(result["report"], title="Relatório Técnico", border_style="green"))
    else:
        print(result)

if __name__ == "__main__":
    print("=== FRE Semantic Core ===")
    print("Comandos: :sair | :testes")

    tests = [
        "subi na cto troquei o conector ai o sinal baxo na onu e a internet vorto",
        "cliente falou que travava tudo troquei canal e voltou",
        "youtube trava na tv mas no celular funciona normal era iptv",
        "cliente sem intenet trokei ponta voutou"
    ]

    while True:
        text = input("\nTexto do técnico > ").strip()

        if text == ":sair":
            break

        if text == ":testes":
            for t in tests:
                show(fre.process(t))
            continue

        if text:
            show(fre.process(text))
