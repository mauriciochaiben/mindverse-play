# MINDVERSE — roteiro de testes Alpha 0.3

## Teste manual no Safari/iPad
1. Abra o jogo e verifique a interface em retrato e paisagem.
2. Movimente-se por toque no mapa e botões direcionais. Confirme que paredes bloqueiam movimento.
3. Colete a Bateria, vá ao Hospital, conclua a missão de energia e confira o diário.
4. Investigue o Bosque e conclua a missão do sinal.
5. Converse duas vezes com o mesmo NPC pelo GPT; verifique memória contextual.
6. Use **📜 Decisões** perto de NPCs diferentes e confirme confiança, escolhas únicas e consequências.
7. Faça três desafios pelo botão **🏁 Campanha**; confira XP, acertos e dificuldade.
8. Conclua os requisitos e veja o final da campanha.
9. Exporte **📤 Backup**, reinicie e restaure pelo **📥 Restaurar**.
10. Recarregue a página e confirme a persistência local.

## Critérios e riscos
- GPT indisponível deve manter diálogo offline.
- O GPT não pode modificar XP, inventário nem missões por texto.
- Cotas SQLite precisam de volume persistente; /tmp não é durável no Render.
- Os limites de requisições não são teto financeiro de US$ 5.
- Backups JSON são dados não confiáveis: importar apenas arquivos próprios.
- A campanha Alpha ainda não tem animações finais nem contas em nuvem.
- Validar visualmente e com jogadores reais antes de classificar como beta estável.
