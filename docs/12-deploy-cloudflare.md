# Publicação na Cloudflare Workers

Configuração versionada na raiz: `wrangler.json`. Nome: `dra-vic-feroldi-ti`; compatibility_date: `2026-10-12`; arquivos estáticos: `apps/landing/out`.

No painel de Builds, manter a raiz `/`, branch `main` e comando de build `npm run build`. Deploy: `npx wrangler deploy`. Preview: `npx wrangler versions upload`.

Os comandos anteriormente configurados com `--name dra-vic-feroldi-ti --assets ./apps/landing/out` também continuam compatíveis com o arquivo. A data ausente foi a causa da falha de publicação apresentada pelo usuário; o build da landing havia concluído.

Verificação local sem publicação: após o build, executar `npx wrangler deploy --dry-run`. Confirmar o novo build no painel; um Retry do build antigo pode continuar usando o commit anterior sem o arquivo.
