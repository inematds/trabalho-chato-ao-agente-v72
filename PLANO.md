# PLANO — Entregue o trabalho chato a um agente (v7.2)

**Público:** dono de pequena empresa ou autônomo, 35–55 anos, usa ChatGPT/Claude no chat, não programa.
**Promessa:** achar a tarefa chata e repetitiva da semana e entregá-la a um agente com uma ficha de uma página, regras de segurança (só leitura, só rascunho, você faz o login, você aprova), uma regra de qual modelo usar e uma prova de que funcionou.
**Caminhos em toda prática:** (a) no chat: Projeto do ChatGPT ou do Claude (ou Gem) com a ficha nas instruções, você exporta/cola os dados; (b) no terminal (opcional): Claude Code ou Codex numa pasta com os arquivos exportados.
**Honestidade:** o chat não abre o seu Search Console nem o seu e-mail: você exporta/cola, o agente lê e escreve o rascunho. Modo agente que usa o navegador existe em alguns planos, mas a ficha e as regras são as mesmas. Sem números de fornecedor de modelo; modelos citados só os conferidos (Codex CLI 0.164: gpt-6-luna, gpt-6.1-terra, gpt-6.1-sol, gpt-6-astra em `/model`; Claude Code: `--model sonnet|opus`). Sem API paga. Sem citar fonte.

| # | slug | título | objetivo (≤160) | diagrama | prática / pronto quando | interação |
|---|---|---|---|---|---|---|
| 1 | achar | Ache a tarefa chata certa | montar a lista das suas tarefas repetitivas e escolher a primeira para o agente: muito tempo, muita chatice, pouco risco | semana → lista → nota → primeira | entrevista no chat (prompt) → tabela com ≥5 linhas | conferidor: linhas numeradas com risco (baixo/médio/alto) e decisão (sim/depois/não) |
| 2 | ficha | A ficha do agente em uma página | escrever a ficha do seu primeiro agente com papel, contexto, passos, regras e primeira tarefa | papel → contexto → passos → regras → entrega | ficha da tarefa da aula 1 colada no Projeto | conferidor: 7 campos + regras citam rascunho e parar |
| 3 | relatorio | O relatório semanal sem abrir o painel | transformar a exportação do Search Console (ou dos seus números) num relatório de até 250 palavras com números conferidos | exportar → colar → ler → relatório → conferir | dados de exemplo no bloco → relatório; conferidor confere que os números certos vieram | conferidor termos (números do exemplo) |
| 4 | leads | Contato novo vira rascunho, nunca envio | montar o agente que registra cada contato novo e deixa a resposta como rascunho para você aprovar | chegou → registra → rascunho → portão você → envia você | 3 contatos de exemplo (1 spam) → planilha + 2 rascunhos | simportao (rascunho com erro) |
| 5 | notas | Nota e boleto: dinheiro passa por você | fazer o agente ler notas e boletos e montar a lista de contas a pagar, marcando repetida e total que não bate | ler → conferir soma → repetida? → lista rascunho → você paga | 4 notas de exemplo → tabela com a repetida e a divergente marcadas | conferidor termos |
| 6 | cliente | Cliente novo: o checklist que para quando falha | escrever o checklist de cliente novo que o agente percorre em ordem, parando no passo que falha sem duplicar nada | 5 passos em ordem + para no erro | checklist próprio → ensaio com cliente fictício | simfila (falha + retomada sem refazer) |
| 7 | roteamento | Modelo leve para a rotina, topo para o difícil | escrever a regra que decide qual modelo faz cada tarefa e classificar as suas tarefas em leve ou topo | tarefa → pergunta → leve / topo → avisa | regra no Projeto/AGENTS.md + 5 tarefas classificadas | conferidor cada_plano (leve/topo) |
| 8 | plano | Do primeiro agente à pequena equipe em 30 dias | montar o plano de 4 semanas com conferência diária no começo e amostragem depois | mapa 4 semanas | gerador com datas + diário de conferência | mapa + gerador |

Imagens: Codex image_gen (capa V15 + 9 heros), reserva flux2-klein + Pillow. Scratch: `scratchpad/trabalho-chato-ao-agente-v72-img/`.
Glossário (i18n): chato = boring/tedioso; ficha do agente = agent sheet / ficha del agente; portão = gate / puerta de control? (usar "aprovação"); rascunho = draft / borrador.
