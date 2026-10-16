# Plano de execução

## Etapa 1 — Consolidar requisitos

- Incorporar a especificação original do atendimento, com versão e responsável pela aprovação.
- Confirmar canal piloto, responsáveis, horários de atendimento e operação atual do WhatsApp.
- Revisar informações públicas do esboço e localizar eventual referência separada do design system.
- Definir se o MVP apenas recebe solicitações ou também confirma consultas.
- Registrar quais dados serão coletados, quem poderá acessá-los e por quanto tempo serão mantidos.

Critério de conclusão: fluxo compreensível e exemplos aprovados, com respostas previstas para exceções e encaminhamento humano.

## Etapa 2 — Organizar o monorepo e evoluir a landing

- Importar o esboço para `apps/landing`, respeitando suas instruções locais e verificando compatibilidade das dependências.
- Formalizar os tokens e componentes existentes; extrair pacote compartilhado quando houver consumidor adicional.
- Revisar conteúdo, imagem definitiva, contatos e domínio com a doutora.
- Conferir navegação por celular, acessibilidade, metadados e destinos dos botões de WhatsApp.
- Preparar ambiente de visualização para revisão antes da publicação.

Critério de conclusão: landing revisável, execução local documentada e contatos validados. Recursos de SEO apoiam descoberta; não garantem posição em buscadores.

## Etapa 3 — Implementar e simular o atendimento

- Escolher integração e comprovar recebimento/envio no ambiente de teste.
- Implementar estados e mensagens do fluxo original.
- Conectar a caixa de entrada humana e verificar suspensão/retomada do bot.
- Acrescentar IA apenas para necessidades identificadas no fluxo.
- Validar duplicação de eventos, falhas, retomadas e limites do assistente com dados fictícios.

Critério de conclusão: cenários de atendimento passam em homologação e a equipe consegue assumir conversas.

## Etapa 4 — Piloto e operação

- Validar configuração do número sem comprometer o atendimento já existente.
- Revisar textos, privacidade, acessos, templates necessários e encaminhamentos com os responsáveis.
- Começar em um canal com acompanhamento da equipe e mecanismo para pausar a automação.
- Monitorar falhas e revisar resultados antes de expandir para outros canais.

Critério de conclusão: atendimento consistente, custos observados e operação humana praticável. Integração com agenda e painel próprio entram conforme necessidade comprovada.

## Registro de decisões

| Tema | Situação |
| --- | --- |
| Repositório | Documentação criada no diretório indicado pelo usuário |
| Esboço da landing | Localizado em `C:/dev/lp_vic`; migração futura |
| Design system | Tokens e componentes no esboço; prompts de cores, fontes e temas consolidados no documento 06 |
| Fluxo original | PDF v2 localizado e lido; resumo em `05-resumo-prototipo-whatsapp-v2.md` |
| Canal piloto | Pendente; proposta inicial é começar com um canal |
| Bot ou IA | Proposta de fluxo explícito com IA auxiliar; decisão após analisar a especificação |
| WhatsApp | Preferência por integração oficial; fornecedor pendente |
| Agenda | Ferramenta e permissões de automação pendentes |
| Caixa de entrada | Avaliar ferramenta existente antes de criar painel |
| Stack e infraestrutura | Pendente; aproveitar esboço onde adequado |
| Publicação | Domínio e hospedagem precisam ser confirmados |
| Locais atuais | Online, Taubaté e Campos do Jordão; São José dos Campos excluído por orientação do usuário |
| Prompts da landing | Lidos e consolidados em `06-requisitos-consolidados.md`; versões antigas são referências históricas |

## Próximo passo

Definir o canal piloto e esclarecer as lacunas registradas no resumo do PDF. Em seguida, pesquisar viabilidade, custo inicial e custos mensais para bot por menus e eventual camada de IA, usando o fluxo documentado como escopo.
