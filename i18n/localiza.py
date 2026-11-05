"""Depois do traduzir.py: localiza os dados de exemplo no cache EN/ES (nomes, cidades, pastas, valores, datas).
Uso: python3 i18n/localiza.py && python3 <skill>/scripts/traduzir.py . en es && python3 i18n/arquivos.py
O PT continua com os dados brasileiros; EN e ES recebem nomes e formatos do mercado (ES = América Latina)."""
import json, pathlib, re

R = pathlib.Path(__file__).resolve().parent
NOMES = {
    "en": [("Madeireira Pinho Forte", "Strong Pine Lumber"), ("Pinho Forte Lumber", "Strong Pine Lumber"),
           ("Madeireira", "Lumber yard"), ("Ferragens Silva", "Silva Hardware"), ("Contabilidade Rocha", "Rocha Accounting"),
           ("Contabilidade", "Accounting"), ("Padaria Trigo Bom", "Golden Wheat Bakery"), ("Marcenaria Lopes", "Lopez Woodworks"),
           ("Clínica Vida", "Vida Clinic"), ("Lima Advocacia", "Lima Law Office"), ("exemplo.com", "example.com"),
           ("batel furniture store", "downtown furniture store"), ("Batel", "Downtown"), ("Curitiba", "Denver"), ("curitiba", "denver"),
           ("meus-agentes/relatorio-site", "my-agents/site-report"), ("meus-agentes/contatos", "my-agents/contacts"),
           ("meus-agentes/notas", "my-agents/invoices"), ("meus-agentes/clientes", "my-agents/clients"), ("meus-agentes", "my-agents"),
           ("relatorio-site", "site-report"), ("relatorio.md", "report.md"), ("tarefas.md", "tasks.md"), ("tarefas.txt", "tasks.txt"),
           ("novos.txt", "new.txt"), ("contatos.csv", "contacts.csv"), ("rascunhos.md", "drafts.md"), ("contas.md", "bills.md"),
           ("clientes/modelo/", "clients/template/"), ("plano.md", "plan.md"), ("diario.txt", "log.txt"),
           ("<code>semana</code>", "<code>week</code>"), ("semana folder", "week folder"), ("An task", "A task"),
           ("Ana Souza", "Anna Scott"), ("ana@example.com", "anna@example.com"), ("Roberto Lima", "Robert Lee"), ("roberto@example.com", "robert@example.com"),
           ("Lima Law Office", "Lee Law Office"), ("Marta Reis", "Martha Reese"), ("marta@example.com", "martha@example.com"),
           ("Silva Hardware", "Miller Hardware"), ("Rocha Accounting", "Baker Accounting"), ("Ana Decor", "Anna Decor"),
           ("11/04/2026", "Nov 4, 2026"), (", in English)", ")"), (" (in English)", "")],
    "es": [("Madeireira Pinho Forte", "Maderera Pino Fuerte"), ("Maderera Pinho Forte", "Maderera Pino Fuerte"),
           ("Madeireira", "Maderera"), ("Ferragens Silva", "Ferretería Silva"), ("Contabilidade Rocha", "Contabilidad Rocha"),
           ("Padaria Trigo Bom", "Panadería Trigo Bueno"), ("Marcenaria Lopes", "Carpintería López"),
           ("Lima Advocacia", "Lima Abogados"), ("exemplo.com", "ejemplo.com"),
           ("tienda de muebles batel", "mueblería del centro"), ("Curitiba", "Guadalajara"), ("curitiba", "guadalajara"),
           ("meus-agentes/relatorio-site", "mis-agentes/informe-sitio"), ("meus-agentes/contatos", "mis-agentes/contactos"),
           ("meus-agentes/notas", "mis-agentes/facturas"), ("meus-agentes/clientes", "mis-agentes/clientes"), ("meus-agentes", "mis-agentes"),
           ("relatorio-site", "informe-sitio"), ("relatorio.md", "informe.md"), ("tarefas.md", "tareas.md"), ("tarefas.txt", "tareas.txt"),
           ("novos.txt", "nuevos.txt"), ("contatos.csv", "contactos.csv"), ("rascunhos.md", "borradores.md"), ("contas.md", "cuentas.md"),
           ("clientes/modelo/", "clientes/plantilla/"), ("plano.md", "plan.md"), ("diario.txt", "registro.txt"),
           ("notas: siga o AGENTS.md com os arquivos da pasta semana", "facturas: sigue AGENTS.md con los archivos de la carpeta semana"),
           ("Lección ", "Clase "), ("Ana Souza", "Ana Sánchez"), ("Marta Reis", "Marta Reyes"), ("lista lista", "lista terminada"),
           ("Checklist", "Lista de verificación"), ("corrección duplicada", "corrección repetida"), ("correcciones duplicadas", "correcciones repetidas"), (", en inglés)", ")"), ("lecciones", "clases"), ("Lecciones", "Clases"), ("la lección", "la clase"), ("La lección", "La clase"),
           ("esta lección", "esta clase"), ("cada lección", "cada clase"), ("una lección", "una clase")],
}
MES = {"10": "Oct", "11": "Nov", "12": "Dec"}
VALOR = re.compile(r"(?<![\d.,])(\d{1,3}(?:\.\d{3})*),(\d{2})(?![\d])")
DATA = re.compile(r"(?<![\d/])(\d{2})/(\d{2})(?:/(\d{4}))?(?![\d/])")


def data_en(m):
    a, b, ano = m.groups()
    if b in MES:            # dd/mm
        d, mes = int(a), MES[b]
    elif a in MES and int(b) > 12:   # mm/dd já convertido pelo tradutor
        d, mes = int(b), MES[a]
    else:
        return m.group(0)
    return f"{mes} {d}" + (f", {ano}" if ano else "")


for lang, nomes in NOMES.items():
    f = R / f"{lang}.json"
    cache = json.loads(f.read_text())
    n = 0
    for k, v in cache.items():
        nv = v
        for a, b in nomes:
            nv = nv.replace(a, b)
        nv = VALOR.sub(lambda m: m.group(1).replace(".", ",") + "." + m.group(2), nv)
        if lang == "en":
            nv = DATA.sub(data_en, nv)
        if nv != v:
            cache[k] = nv
            n += 1
    f.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
    print(lang, n, "textos localizados")
