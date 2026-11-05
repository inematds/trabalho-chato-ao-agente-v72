# Entregue o trabalho chato a um agente (v7.2)

Curso aberto e gratuito do INEMA.CLUB, formato INEMA Learning v7.2, em PT, EN e ES.

- PT: https://inematds.github.io/trabalho-chato-ao-agente-v72/
- EN: https://inematds.github.io/trabalho-chato-ao-agente-v72/en/
- ES: https://inematds.github.io/trabalho-chato-ao-agente-v72/es/

Para dono de pequena empresa ou autônomo que usa ChatGPT/Claude no chat e não programa: achar a tarefa chata da semana, escrever a ficha do agente, regras de segurança (só leitura, só rascunho, login é seu, dinheiro passa por você), modelo leve × topo e um plano de 30 dias com diário de conferência. Toda prática tem o caminho no chat; o terminal (Claude Code ou Codex) é opcional. Tudo pela assinatura, sem API paga.

## As aulas

1. Ache a tarefa chata certa
2. A ficha do agente em uma página
3. O relatório da semana sem abrir o painel
4. Contato novo vira rascunho, nunca envio
5. Nota e boleto: o dinheiro passa por você
6. Cliente novo: o checklist que para quando falha
7. Modelo leve para a rotina, topo para o difícil
8. Do primeiro agente à pequena equipe em 30 dias

## O processo, do início ao fim

1. ⚙️ Criar a pasta: `~/.claude/skills/formato-curso-v72/scripts/novo-curso.sh ~/projetos/trabalho-chato-ao-agente-v72 "<nome>"`.
2. 🧠 Plano das aulas em `PLANO.md` (objetivo, diagrama, prática e conferidor de cada aula).
3. 🧠 Conteúdo em `conteudo/pt/curso.json` e `conteudo/pt/aulas/NN-<slug>.json`; conferidores testados com `python3 conferir.py <aula> --exemplo` e `--errado`.
4. 🤖 Imagens: heros pelo Codex image_gen (`codex exec`, assinatura) e capa composta com título em serifa (Playwright) → `assets/img/`.
5. ⚙️ Portão PT: `python3 gerar.py && python3 validar.py --links` e `node ~/.claude/skills/formato-curso-v72/scripts/conferir-tela.cjs .`.
6. 🤖 Revisor independente (Agent novo, persona do público) → nota em `~/projetos/wifi/scripts/revisor-nota.py`; corrigir e revisar de novo até ≥ 8.
7. 🤖 Tradução: `python3 ~/.claude/skills/formato-curso-v72/scripts/traduzir.py . en es --publico "..."` (tradutor central, assinatura), glossário em `i18n/glossario.json`, cache em `i18n/<lang>.json`; depois `python3 i18n/localiza.py` (nomes, cidades, valores, datas e pastas do exemplo por mercado), o `traduzir.py` de novo (regrava do cache) e `python3 i18n/arquivos.py` (nomes de arquivo do conferidor); varreduras das Lessons.
8. ⚙️ Portão nos 3 idiomas: `python3 gerar.py --lang en|es`, `python3 validar.py --links --lang en|es`, `conferir-tela.cjs .`.
9. 🤖 Um revisor por idioma (EN, ES).
10. ⚙️ Publicar: commit (autor `inematds`) + push; GitHub Pages da raiz da `main`.
