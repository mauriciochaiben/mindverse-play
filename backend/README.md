# MINDVERSE — API de NPCs com GPT

Este serviço Python é separado do jogo estático hospedado no GitHub Pages.

## Implantação
1. Hospede a pasta `backend/` em um serviço Python HTTPS (por exemplo, Render, Railway ou outro host FastAPI).
2. Instale `requirements.txt` e inicie com `uvicorn main:app --host 0.0.0.0 --port $PORT` (configure a porta conforme o provedor).
3. Configure **somente no serviço**, como segredo, `OPENAI_API_KEY`. Nunca a envie ao navegador nem a inclua no GitHub.
4. Configure `ALLOWED_ORIGINS=https://mauriciochaiben.github.io` e opcionalmente `OPENAI_MODEL=gpt-4.1-mini`.
5. Verifique `GET /health` (configured=true) e teste `POST /npc/chat`.
6. No jogo, toque em **⚙️ GPT** e informe a URL HTTPS pública do backend, sem caminho final. A URL é salva no navegador.

## Segurança
O backend valida o NPC, limita mensagens a 500 caracteres e aplica um limite simples de 15 requisições/minuto por IP **em memória**. Em produção, adicione autenticação anônima com cotas, proteção antiabuso no gateway, monitoramento de gastos e rate limiting compartilhado. CORS não é autenticação. Não inclua a chave no HTML.
