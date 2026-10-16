# Requisitos consolidados da landing e do atendimento

## Autoridade e fontes

Este documento consolida os prompts enviados pelo usuário, os três anexos `Texto colado.txt`, o PDF v2 e a correção atual que exclui São José dos Campos. A orientação atual do usuário prevalece sobre versões anteriores. O PDF original e o esboço em `C:/dev/lp_vic` permanecem preservados.

Os textos sobre publicidade médica são tratados aqui como requisitos editoriais do projeto fornecidos pelo usuário, não como parecer sobre a legislação vigente. A revisão normativa ficará na etapa de viabilidade e preparação para publicação.

### Resultado posterior da pesquisa de viabilidade

A pesquisa em `07-pesquisa-e-proposta.md` identificou ajustes propostos para validação: divulgação da pós-graduação acompanhada de NÃO ESPECIALISTA conforme orientação oficial consultada; revisão de cards de doenças; e coleta de CPF/dados fiscais em formulário protegido acessado pelo bot, em vez de pedir identificadores completos no chat. Esses pontos complementam/corrigem a redação histórica abaixo e devem orientar o detalhamento antes da publicação. A proposta considera um número central automatizado e dois atendentes como premissas ainda não confirmadas pelo usuário.

Correção comercial posterior: o prestador definiu R$ 400 pela landing e R$ 200 pelo bot/chat, total R$ 600, e informou cerca de 20 pessoas atendidas por mês. A proposta v1.1 em `07-pesquisa-e-proposta.md` substitui o dimensionamento acima por um atendente como premissa inicial, landing estática e backend pequeno. Manutenção de mão de obra não tem mensalidade definida; custos externos são separados.

## Identificação e conteúdo

- Nome: Dra. Victoria Nunes Feroldi.
- Formação apresentada: médica pós-graduada em psiquiatria ou médica com pós-graduação em psiquiatria.
- Identificação profissional: CRM-SP 246645.
- E-mail: dravictoriaferoldi@gmail.com.
- Nunca atribuir título de especialista ou usar a designação profissional vedada nos prompts, incluindo em FAQ, metadados, alt text ou dados estruturados.
- Não prometer cura, resultados ou garantias; não usar depoimentos de pacientes ou comunicação sensacionalista/estigmatizante.
- Não inventar trajetória, instituições, credenciais, RQE ou biografia.
- Tom acolhedor, claro, informativo e respeitoso.
- Não publicar preços de consultas/convênios ou detalhes de coleta para nota fiscal na landing.
- Informar que o site não substitui consulta e que site/WhatsApp não são canais de urgência.

Texto de referência dos prompts finais: “Em caso de emergência, procure um pronto-socorro ou ligue 192 (SAMU). Para apoio emocional imediato, ligue 188 (CVV).” Manter a distinção entre emergência e apoio emocional, inclusive nas versões abreviadas.

## Modalidades e contatos atuais

| Modalidade/local | Atendimento | Horários | WhatsApp |
| --- | --- | --- | --- |
| Online / central da doutora | Particular, telemedicina | Quarta, 8h–12h | (12) 99793-2353 |
| Taubaté — Clínica Fator Humano | Particular e convênio | Segunda e quinta, 8h–17h; sexta, 8h–14h | (12) 99160-1313 |
| Campos do Jordão | Presencial particular | Informados pela equipe | (12) 99658-3276 |

Endereço de Taubaté: Rua Cel. Gomes Nogueira, 66, Centro, Taubaté-SP, CEP 12010-120. Endereço de Campos do Jordão: informado pela equipe no agendamento.

São José dos Campos está fora do escopo, inclusive para bot, landing, FAQ, menus, dados estruturados e configuração de contatos.

Os números estão definidos como destinos públicos pelos prompts. Isso não define quais contas terão automação nem comprova acesso à API ou administração dos números das clínicas.

## Jornada pública

A versão final dos prompts usa encaminhamento direto ao WhatsApp de cada modalidade/local. O CTA global deve levar à seção de locais, para evitar direcionar um paciente presencial ao número online por engano.

1. Encontrar e conhecer a doutora.
2. Escolher modalidade/local.
3. Abrir o WhatsApp correspondente com mensagem administrativa pré-preenchida.
4. Informar se é primeiro atendimento ou acompanhamento, conforme operação do canal.
5. Confirmar horários com a equipe responsável.

Não apresentar seleção de modalidade ou clique em botão como consulta confirmada. O formulário genérico de contato dos prompts iniciais não entra no escopo inicial: a versão final prioriza WhatsApp e e-mail.

## Estrutura da landing

1. Header com monograma, navegação, acesso aos locais e alternância de tema.
2. Hero com identificação profissional, proposta de cuidado, CTA e imagem profissional.
3. Sobre, apenas com informações de trajetória fornecidas/confirmadas.
4. Áreas de cuidado: ansiedade, depressão, esgotamento profissional, sono, luto e saúde mental, com linguagem sem promessas.
5. Como funciona: modalidade/local → WhatsApp correspondente → primeiro atendimento/acompanhamento → confirmação com a equipe.
6. Locais e canais: três cards com os destinos definidos.
7. FAQ: formação e cuidado, telemedicina, canal correto, documentos médicos e urgência.
8. Contato por WhatsApp/e-mail e rodapé com identificação e avisos.

A comparação profissional no FAQ deve usar a formação correta da doutora, eliminando a formulação contraditória presente no primeiro prompt. O aviso sobre urgência aparece no hero, na seção de agendamento e no rodapé.

## Identidade visual

Preservar Inter para texto, Lora para títulos, verde esmeralda, superfícies claras, cantos arredondados e espaçamento generoso. Melhorar hierarquia, composição e consistência sem descaracterizar essa base.

| Token | Claro | Escuro |
| --- | --- | --- |
| Fundo principal | `#FFFFFF` | `#0F172A` |
| Fundo alternativo | `#F9FAFB` | `#1E293B` |
| Destaque | `#ECFDF5` | `#064E3B` |
| Texto principal | `#111827` | `#F9FAFB` |
| Texto secundário | `#4B5563` | `#9CA3AF` |
| Bordas | `#E5E7EB` | `#334155` |
| Primário | `#059669` | `#10B981` |
| Hover/CTA | `#047857` | `#34D399` |

As cores são a base de marca, não prova automática de contraste. Validar cada combinação real de texto, fundo, ícone e foco; ajustar a aplicação dos tokens quando necessário para atender ao objetivo WCAG AA.

Tema inicial claro, escolha manual persistente e toggle acessível em desktop/mobile. A preferência do sistema não deve substituir a escolha manual. A implementação atual desabilita tema automático do sistema; manter como padrão de planejamento.

## Qualidade verificável

- Mobile primeiro, sem rolagem horizontal, menus ou CTAs encobertos pelo header.
- Navegação por teclado, foco visível e controles com nomes acessíveis.
- FAQ com borda envolvendo pergunta e resposta completas; expansão sem altura fixa que corte texto. Conferir respostas longas nos dois temas.
- Respeitar movimento reduzido; transições discretas.
- Metadados pt-BR, URL canônica e compartilhamento com domínio confirmado.
- Dados estruturados coerentes com o conteúdo e os locais reais, sem inventar clínica própria ou especialização. JSON-LD é dado, não elemento visual sujeito a contraste.
- Foto placeholder pode permanecer durante desenvolvimento; foto e direitos de uso precisam ser definidos para a versão pública. Não inventar retrato real da doutora.
- Links de WhatsApp corretos para cada local, com mensagens administrativas e sem dados sensíveis na URL.
- Sem dados de pacientes em analytics, Git ou conteúdo público.
- Código modular, conteúdo centralizado e segredos fora do frontend.
- Conferir build, lint, navegação, links, acessibilidade e layout antes da publicação.

## Bot: fluxo atual após a correção

```text
Entrada
├── Primeiro atendimento → apresentação → Agendamento
└── Em acompanhamento
    ├── Agendamento
    ├── Solicitações → orientações → Agendamento
    └── Urgência → orientação fixa e retorno ao menu

Agendamento
├── Particular
│   ├── Online → dados NF → informação de valor/pagamento → equipe
│   ├── Taubaté → dados NF → equipe
│   └── Campos do Jordão → dados NF → equipe
└── Convênio
    └── Taubaté → equipe, sem formulário NF
```

Mantêm-se as regras do PDF para dados fiscais, documentos médicos e consulta online particular de R$ 400,00 com pagamento antes da consulta. Esse valor pertence ao fluxo privado; não deve aparecer na landing. O PDF não exige agenda, pagamento ou nota fiscal automatizados.

## Decisão de integração ainda pendente

Há duas jornadas compatíveis com partes das fontes: a landing leva diretamente às três equipes; o bot central orienta e encaminha às equipes. Precisamos definir onde a automação ficará.

Proposta para comparar na pesquisa: automatizar primeiro o número central da doutora, mantendo os destinos próprios de Taubaté e Campos do Jordão. Isso evita pressupor implantação em três números, mas ainda depende da confirmação do usuário sobre a operação desejada. Links públicos para três números não significam três bots.

## Próximas etapas

Atualização de 07/10/2026: primeira landing implementada em `apps/landing`, com foto e logo como placeholders e biografia em lorem ipsum. Domínio pretendido `dravictorianunesferoldi.com.br`, ainda não contratado. Pesquisa concluída e preservada no documento 07; proposta resumida em duas páginas no documento 08/PDF. A página foi validada localmente; publicação e conexão do WhatsApp real permanecem pendentes.

1. Pesquisar viabilidade e custos usando o fluxo corrigido: bot por menus versus bot com interpretação por IA, custo inicial e mensal.
2. Definir número automatizado, atendimento humano, coleta/armazenamento fiscal e manutenção da operação atual.
3. Importar a landing para `apps/landing`, revisar conteúdo e reconstruir os componentes que precisarem de melhoria.
4. Validar a landing em preview e o bot com conversas fictícias antes de publicar ou conectar o canal real.

Stack dos prompts: Next.js App Router, TypeScript, Tailwind, Inter/Lora, lucide-react, next/image e next-themes. A versão instalada e suas instruções locais deverão orientar a implementação; não aplicar configurações de versões antigas apenas porque constam dos prompts históricos.
