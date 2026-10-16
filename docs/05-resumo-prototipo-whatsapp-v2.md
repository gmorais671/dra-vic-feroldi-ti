# Resumo do protótipo de WhatsApp v2

Fonte: `../Prototipo_WhatsApp_Victoria_v2.pdf`, 21 páginas, lidas e conferidas visualmente. Este documento distingue requisitos do PDF de observações para implementação.

**Correção posterior do usuário:** São José dos Campos não faz mais parte do projeto. As menções abaixo descrevem o PDF original, que permanece preservado como fonte histórica. Para implementação, particular inclui apenas Online, Taubaté e Campos do Jordão; convênio inclui apenas Taubaté. Consulte `06-requisitos-consolidados.md`.

## Fluxo especificado

O paciente inicia a conversa e escolhe entre **Primeiro atendimento** e **Já estou em acompanhamento**.

### Primeiro atendimento (páginas 4–11)

Recebe uma apresentação da consulta, modalidades e orientação de que o canal não atende urgências. Ao escolher **Agendar consulta**, segue para **Particular** ou **Convênio**.

### Em acompanhamento (páginas 12–20)

Escolhe **Agendamento de consulta**, **Solicitações** ou **Urgência**.

- Agendamento usa a mesma escolha entre particular e convênio.
- Solicitações informa que receitas, atestados, relatórios, declarações e demais documentos são avaliados em consulta e emitidos quando houver indicação médica. Não há emissão de documentos ou renovação de receitas por esse WhatsApp. Em seguida, oferece particular ou convênio para agendar a consulta necessária.
- Urgência informa que o canal não atende urgências/emergências, orienta buscar pronto-socorro ou serviço próximo e menciona SAMU 192 para risco imediato à vida. Oferece retorno ao menu inicial.

### Particular

Modalidades: **Online**, **São José dos Campos**, **Taubaté** e **Campos do Jordão**.

Todo atendimento particular solicita dados para emissão de nota fiscal:

- Nome completo.
- CPF.
- Data de nascimento.
- Telefone.
- Endereço completo: rua, número, complemento, bairro, cidade, estado e CEP.

Após a coleta:

- Online informa valor de **R$ 400,00**, pagamento antes da consulta e atendimento por telemedicina no horário agendado após confirmação do pagamento. Há opção para continuar ao agendamento.
- Presencial encaminha à equipe responsável pela unidade selecionada.

### Convênio

Oferece **São José dos Campos** e **Taubaté**. Não apresenta formulário de nota fiscal. Encaminha à equipe para consultar convênios atendidos, horários disponíveis e agendar.

## Regras gerais (página 21)

- Telas secundárias devem oferecer Voltar e Menu inicial. A tela de urgência mostra apenas retorno ao menu, uma diferença a esclarecer em relação à regra geral.
- Online é exclusivamente particular.
- Online custa R$ 400,00, com pagamento anterior à consulta, conforme o protótipo.
- Particular exige coleta dos dados para nota fiscal; convênio não exibe esse formulário.
- Documentos médicos dependem de consulta e indicação médica.
- No fim da escolha de modalidade/local, o bot envia o contato correspondente para agendamento.
- Números e links das unidades serão configurados na implementação; o PDF não os fornece.

## Interpretação do escopo

O documento descreve um bot administrativo por menus, com mensagens fixas, coleta de dados e encaminhamento. Não exige IA generativa para cumprir o fluxo apresentado.

Solicitar dados para nota fiscal não equivale a emitir a nota automaticamente. Informar pagamento antecipado não equivale a cobrar ou conferir o pagamento automaticamente. Encaminhar ao contato da equipe não equivale a confirmar horário ou transferir o histórico da conversa.

O PDF não especifica integrações de agenda, pagamentos, sistema fiscal, prontuário ou caixa de entrada humana. Esses recursos, se desejados, acrescentam escopo.

## Lacunas para implementar e orçar

1. Número que recebe o bot e contatos de destino para online, Taubaté e Campos do Jordão, conforme correção posterior do usuário.
2. Encaminhamento por link para outro número ou continuidade com equipe no mesmo número; necessidade de compartilhar contexto entre equipes.
3. Coleta dos dados por perguntas no chat ou formulário; validação, confirmação, armazenamento e acesso pela equipe responsável.
4. Dados para NF de pacientes recorrentes: pedir novamente ou reutilizar cadastro confirmado.
5. Meio de pagamento, responsável por confirmar e contato final do atendimento online.
6. Tratamento de texto livre, áudio, anexos, escolhas inválidas, interrupções e retorno posterior à conversa.
7. Pedido de humano em qualquer etapa, horários da equipe e suspensão do bot quando um humano atende.
8. Procedimento para mensagem de urgência enviada fora da opção de menu correspondente.
9. Destino dos dados para NF quando o paciente muda de modalidade ou abandona o fluxo.
10. Navegação da tela de urgência: apenas Menu inicial ou também Voltar.

## Diferença em relação à landing existente

O esboço em `C:/dev/lp_vic/components/data.ts` apresenta online, Taubaté e Campos do Jordão. O PDF também inclui São José dos Campos, mas o usuário retirou essa cidade do escopo. Os três destinos da landing estão alinhados à correção atual; o fluxo implementado deve excluir a cidade removida.

## Base para a pesquisa de viabilidade e custos

Comparar um bot que executa exatamente os menus do PDF com uma opção que acrescenta IA para interpretar linguagem livre. Separar investimento inicial de custos recorrentes: integração do WhatsApp, mensagens quando tarifadas, hospedagem, armazenamento, eventual caixa de entrada, eventual IA e manutenção.

As estimativas dependerão do volume mensal, quantidade de números automatizados, usuários da equipe, necessidade de manter o aplicativo atual e integrações adicionais. O resumo não contém cotação ou valores de fornecedores.
