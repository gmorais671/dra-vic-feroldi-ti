# Atendimento pelo WhatsApp

Status: propostas técnicas preliminares. A especificação foi localizada em `Prototipo_WhatsApp_Victoria_v2.pdf`, com 21 páginas. Consulte [o resumo do protótipo](05-resumo-prototipo-whatsapp-v2.md) para o fluxo especificado. As sugestões técnicas deste documento complementam o PDF e dependem de decisões de implementação.

## Estratégia proposta

Usar o fluxo especificado como autoridade para etapas e decisões. Adicionar IA quando ela melhorar a compreensão de mensagens livres, preservando regras explícitas para ações e respostas. Informações de horários, valores, convênios e locais devem vir de uma base aprovada, com data de revisão.

A IA não pode inventar disponibilidade, preços ou confirmação de consulta. Mensagens do paciente são entrada do fluxo, não autorização para alterar regras, acessar outras conversas ou executar ações fora do escopo.

## Integração

Preferência inicial: WhatsApp Business Platform, diretamente ou por parceiro. A plataforma oficial oferece APIs para comunicação, automação e integração com sistemas de atendimento.

Segundo a política consultada, respostas livres são permitidas dentro da janela de 24 horas após uma mensagem do usuário; fora dela, o envio exige templates aprovados. A política também prevê permissão para contatos subsequentes e caminhos claros para atendimento humano. Esses pontos afetam lembretes e retomadas de conversa.

Fontes oficiais consultadas em 6 de outubro de 2026:

- [WhatsApp Business Platform](https://whatsappbusiness.com/products/business-platform/)
- [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/)

Antes de contratar ou conectar o número, validar regras vigentes, elegibilidade, custos e compatibilidade com a operação atual. Não assumir que o número usado hoje poderá continuar no aplicativo nas mesmas condições.

## Canais encontrados no esboço

| Canal | Encaminhamento atual | Decisão pendente |
| --- | --- | --- |
| Online | WhatsApp específico da consulta online | Confirmar se é o canal piloto e quem atende |
| Taubaté | WhatsApp da Clínica Fator Humano | Confirmar controle do número e participação da clínica |
| Campos do Jordão | WhatsApp distinto para presencial | Confirmar controle do número e responsável |

Os números constam em `C:/dev/lp_vic/components/data.ts`. Não unificar esses destinos sem validar o funcionamento das equipes.

## Roteiro para mapear a especificação original

Para cada etapa, registrar:

| Campo | Conteúdo esperado |
| --- | --- |
| Identificador | Nome estável da etapa |
| Entrada | Evento ou mensagem que ativa a etapa |
| Mensagem | Texto aprovado ou instruções limitadas de geração |
| Dados | Campos necessários, finalidade e validação |
| Transição | Condições para seguir, voltar, encerrar ou transferir |
| Ação | Consulta de informação ou operação autorizada |
| Exceção | Resposta incompreendida, falha, silêncio ou pedido humano |
| Responsável | Quem revisa a regra e recebe encaminhamentos |

O fluxo original começa pela distinção entre primeiro atendimento e acompanhamento. Os caminhos de agendamento e solicitações convergem para particular/convênio, modalidade/local e contato da equipe responsável. Particular inclui coleta de dados para nota fiscal; urgência apresenta orientação fixa. O PDF não define integração automática com agenda.

## Atendimento humano

Estados sugeridos: `automacao`, `aguardando_humano`, `humano` e `encerrado`.

- Permitir pedido de atendimento humano em qualquer etapa.
- Transferir quando a solicitação estiver fora do escopo, houver falhas repetidas ou faltar informação aprovada.
- Enviar à equipe um resumo administrativo e as informações necessárias, evitando repetir perguntas ao paciente.
- Ao transferir, suspender o diálogo automatizado; eventual confirmação de recebimento deve ser controlada.
- Informar disponibilidade real da equipe, sem prometer atendimento imediato fora do horário.
- Retomar a automação apenas por regra explícita ou ação da equipe.
- Tratar inatividade separadamente de conclusão bem-sucedida.

## Casos mínimos de validação

1. Nova conversa e paciente em acompanhamento, conforme fluxo original.
2. Modalidades/cidades e encaminhamento ao canal correto.
3. Mensagem livre, ambígua, repetida e tentativa de alterar as regras do assistente.
4. Pedido humano, fora do horário e resposta da equipe com bot pausado.
5. Webhook repetido, falha de envio e indisponibilidade da IA.
6. Tentativa de contato fora da janela permitida e desistência de receber mensagens.
7. Solicitação clínica ou possível urgência, conforme protocolo aprovado pela doutora.
8. Áudio, imagem e documento: decidir suporte ou instrução de alternativa antes do piloto.
9. Pedido de horário sem agenda integrada: registrar solicitação sem confirmar consulta.
