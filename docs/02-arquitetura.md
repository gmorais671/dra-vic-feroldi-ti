# Arquitetura proposta

Status: proposta inicial. Ainda não foram escolhidos provedor de WhatsApp, modelo de IA, banco, hospedagem ou gerenciador de workspaces.

Atualização de dimensionamento: após informar cerca de 20 pessoas/mês, a proposta v1.1 considera landing estática e backend serverless pequeno, com D1 e uma caixa humana. A estrutura lógica abaixo continua como referência; os fornecedores e a rotina do número serão confirmados antes da implementação. Consulte `07-pesquisa-e-proposta.md` para os custos atuais.

## Organização futura

```text
vic_feroldi_project/
  docs/
  apps/
    landing/           # evolução do esboço em C:/dev/lp_vic
    atendimento/       # backend do fluxo e integração com WhatsApp
    painel/            # opcional, se a caixa de entrada escolhida não bastar
  packages/
    design-system/     # tokens e componentes visuais compartilháveis
    contracts/         # contratos de eventos e integrações
    atendimento-core/ # regras, estados e conteúdo aprovado
```

As pastas de aplicação serão criadas quando a implementação começar. O painel próprio e os pacotes compartilhados só devem nascer quando houver necessidade concreta; o MVP pode operar com landing, backend e uma caixa de entrada existente.

## Percurso principal

```text
Paciente → landing page → WhatsApp
Paciente → WhatsApp → integração oficial → backend do atendimento
Backend → fluxo + informações aprovadas → resposta pelo WhatsApp
Backend → fila/caixa de entrada humana → equipe
Backend ↔ agenda, somente quando existir integração validada
```

O WhatsApp também deve funcionar para quem chega diretamente ao número, sem visitar a landing page.

## Responsabilidades

| Componente | Responsabilidade |
| --- | --- |
| Landing | Conteúdo público, localização, contato e descoberta por buscadores |
| Integração WhatsApp | Recebimento de eventos, envio de mensagens e status de entrega |
| Motor do fluxo | Controlar etapas, dados necessários e ações permitidas |
| Camada de IA | Interpretar linguagem livre e formular respostas dentro das regras |
| Caixa de entrada | Permitir atendimento humano, assumir e devolver conversas |
| Persistência | Estado, responsável atual, eventos processados e registros necessários |
| Agenda | Disponibilidade e confirmação de horários, quando integrada |

Separar conteúdo público de configurações privadas. Telefone publicado na landing não implica que a equipe controla esse número ou que ele esteja habilitado para a API.

## Confiabilidade

- Validar autenticidade dos eventos recebidos conforme a integração escolhida.
- Deduplicar eventos por identificador do provedor e processar mensagens em ordem por conversa.
- Usar fila e tentativas controladas de envio, com tratamento de falhas definitivas.
- Evitar respostas simultâneas do bot e da equipe mediante estado explícito de responsabilidade.
- Diferenciar mensagem enviada, entregue e lida quando o provedor disponibilizar esses eventos.
- Confirmar agendamento somente após resposta válida da agenda ou confirmação humana.
- Manter fluxo utilizável quando a IA estiver indisponível: opções fixas e encaminhamento humano.

## Dados e acesso

Coletar apenas dados necessários ao fluxo administrativo. Antes do piloto, definir campos, finalidade, pessoas com acesso, retenção e procedimento de exclusão. Não usar conversas reais como fixtures ou documentação no Git.

Segredos ficam em configuração privada do ambiente. Logs e ferramentas de análise devem evitar texto integral de conversas e dados sensíveis. Envio de conteúdo a fornecedores de IA exige uma decisão explícita sobre quais dados são necessários e quais podem ser removidos.

Configurações e regras devem ser versionadas para permitir identificar qual fluxo produziu uma resposta. Dev, homologação e produção precisam de credenciais e destinos separados.

## Decisões para o início da implementação

1. Canal piloto, controle do número e forma de atendimento humano.
2. Integração oficial direta ou parceiro, incluindo possibilidade de manter a operação atual do número.
3. Necessidade de IA no primeiro piloto e dados que poderão ser enviados ao modelo.
4. Ferramenta atual de agenda e nível de automação autorizado.
5. Hospedagem, custos recorrentes e responsáveis pela operação.
6. Gerenciador do monorepo, após conferir compatibilidade do esboço.
