# Visão e escopo

Planejamento inicial em 6 de outubro de 2026.

## Objetivo

Facilitar que pacientes encontrem a Dra. Victoria Nunes Feroldi, identifiquem a modalidade de atendimento e recebam orientações administrativas pelo WhatsApp, com continuidade humana quando necessário.

O resultado esperado é reduzir trabalho repetitivo, organizar solicitações e tornar o encaminhamento ao canal correto mais claro. Metas numéricas serão definidas após conhecer o volume atual de conversas.

## Informações confirmadas pelo usuário

- O WhatsApp é a principal fonte de comunicação da doutora com pacientes.
- Já existe uma especificação do fluxo de atendimento.
- Já foram criados um design system e um esboço da landing page.
- Este repositório reunirá a documentação e, posteriormente, os projetos em subpastas de um monorepo.

## Inventário do esboço

Referência consultada: `C:/dev/lp_vic`.

| Elemento | Encontrado nos arquivos |
| --- | --- |
| Aplicação | Next.js, React e TypeScript; Tailwind CSS |
| Tipografia | Inter para texto e Lora para títulos serifados |
| Cores | Verde floresta `#047857`, esmeralda `#059669`, menta `#ecfdf5` |
| Temas | Claro e escuro |
| Seções | Apresentação, sobre, áreas de cuidado, processo, locais, FAQ e contato |
| Canais | WhatsApps distintos para online, Taubaté e Campos do Jordão |
| Busca e compartilhamento | Metadados, canonical, Open Graph e JSON-LD já esboçados |
| Imagem | Foto de perfil ainda representada por placeholder |

Fontes locais: `package.json`, `app/globals.css`, `app/layout.tsx`, `app/page.tsx` e `components/data.ts`.

Os arquivos contêm contatos, CRM, endereço, horários e um domínio. Os prompts posteriormente enviados pelo usuário confirmam os dados de contato e atendimento consolidados em `06-requisitos-consolidados.md`; o domínio ainda precisa ser confirmado. A especificação visual também está registrada nesses prompts. São José dos Campos foi explicitamente excluído do escopo pelo usuário.

## Escopo proposto para a primeira versão

1. Landing page responsiva que apresente a doutora e encaminhe ao WhatsApp correto.
2. Atendimento administrativo automatizado em um canal piloto a confirmar.
3. Execução do fluxo existente, respostas com informações aprovadas e registro do estado da conversa.
4. Transferência para a equipe com contexto e interrupção das respostas automáticas enquanto um humano atende.
5. Monitoramento de falhas e métricas operacionais mínimas.

Agendamento inicialmente pode ser uma solicitação encaminhada à equipe. A confirmação automática depende de integração real com a agenda e de regras de disponibilidade definidas.

## Limites de produto propostos

O assistente deve se apresentar como assistente virtual da equipe. Seu papel inicial é administrativo: informações, encaminhamento e organização de solicitações. Diagnóstico, prescrição, alteração de tratamento e avaliação clínica ficam fora do escopo.

Mensagens com possíveis situações de urgência exigem texto e encaminhamento definidos pela doutora. O sistema não deve prometer monitoramento contínuo ou usar classificação automática como garantia de segurança.

## Indicadores

- Tempo até a primeira resposta e até o atendimento humano.
- Solicitações administrativas resolvidas pelo fluxo.
- Transferências para a equipe e seus motivos.
- Solicitações de agendamento e confirmações, separadamente.
- Falhas de envio, respostas duplicadas e conversas abandonadas.

Cliques na landing page e mensagens recebidas são eventos diferentes; atribuição entre eles dependerá do mecanismo adotado, sem incluir dados de saúde em analytics.
