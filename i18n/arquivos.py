"""Depois do traduzir.py: troca o nome sugerido dos arquivos do conferidor por idioma (o tradutor não mexe em 'arquivo')."""
import json, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
M = {"en": {"tarefas.txt": "tasks.txt", "ficha-agente.txt": "agent-sheet.txt", "relatorio.txt": "report.txt",
            "contas.txt": "bills.txt", "modelos.txt": "models.txt"},
     "es": {"tarefas.txt": "tareas.txt", "ficha-agente.txt": "ficha-agente.txt", "relatorio.txt": "informe.txt",
            "contas.txt": "cuentas.txt", "modelos.txt": "modelos.txt"}}
for lang, m in M.items():
    for f in sorted((R / "conteudo" / lang / "aulas").glob("*.json")):
        d = json.loads(f.read_text()); mudou = False
        for s in d["secoes"]:
            if s.get("tipo") == "conferidor" and s.get("arquivo") in m:
                s["arquivo"] = m[s["arquivo"]]; mudou = True
        if mudou:
            f.write_text(json.dumps(d, ensure_ascii=False, indent=2)); print(lang, f.name)
