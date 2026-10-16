# Primeira versão da landing — 07/10/2026

Direção visual: uma página calma e editorial, com títulos Lora e texto Inter. Paleta: branco #FFFFFF, cinza #F9FAFB, texto #111827, secundário #4B5563, verde #047857 e fundo #ECFDF5. O verde mais escuro nos botões mantém contraste com o texto branco. Modo escuro com fundo #0F172A e acento #34D399.

Layout: cabeçalho → apresentação e moldura de foto → biografia → abordagem → modalidades e contatos → dúvidas → rodapé. Evitar blocos repetidos e efeitos decorativos excessivos; o destaque é a moldura vertical da foto e os contatos fáceis de encontrar.

Revisão do modo claro: substituir os grandes fundos brancos por verde acinzentado #EAF2ED, cinza #E3E7E5 e verde #D6EBDF. Superfícies de cabeçalho e cards #F1F4F2; espaço da foto #C1D9CC. O modo escuro mantém sua paleta.

Foto e logo são placeholders explícitos; biografia em lorem ipsum. Fontes Inter e Lora locais reaproveitadas do esboço. Domínio pretendido: dravictorianunesferoldi.com.br, ainda não contratado. A prévia usa noindex; alterar apenas quando o conteúdo estiver aprovado para publicação.

A página exporta arquivos estáticos, sem coletar dados de pacientes. Cada local mantém seu próprio WhatsApp. Não há formulário fictício. O bot será desenvolvido separadamente.

Antes de publicar: substituir foto/logo/biografia, confirmar contatos e horários com a doutora, revisar identificação profissional e informações de privacidade, contratar domínio e habilitar indexação.

Validação: build estático, TypeScript e lint aprovados; navegação sem overflow horizontal em 320, 390, 768 e 1440px; três links de WhatsApp distintos; FAQ nativo expansível e persistência do tema; revisão visual de desktop, celular e tema escuro. Nenhum envio de mensagens foi realizado.

Auditoria das dependências: cinco alertas altos no encadeamento de desenvolvimento do eslint-config-next → fast-glob → micromatch → braces, originados em uma mesma vulnerabilidade de padrões profundamente aninhados. A versão publicada de braces consultada continua sendo 3.0.3; a correção automática sugeriria downgrade incompatível do ESLint Next. Não afeta código JavaScript entregue pela landing estática; acompanhar atualização antes de futuras alterações das ferramentas. Não aplicar `npm audit fix --force` indiscriminadamente.
