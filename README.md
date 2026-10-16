# Ecossistema da Dra. Victoria Nunes Feroldi

Monorepo para divulgação e atendimento administrativo da doutora, com o WhatsApp como principal canal de comunicação com pacientes.

A primeira landing está implementada em `apps/landing`. O atendimento automático permanece em planejamento. A documentação distingue informações do esboço, propostas de arquitetura e decisões ainda pendentes.

## Executar a landing

Na raiz: `npm install`, depois `npm run dev`. Para verificar: `npm run lint` e `npm run build`. O build exporta o site estático em `apps/landing/out`, pronto para uma hospedagem estática.

O cabeçalho usa o nome e CRM, sem placeholder de logo. A apresentação usa uma imagem ilustrativa de ambiente acolhedor; a biografia, a formação e a abordagem usam o conteúdo fornecido pela doutora. O domínio pretendido é `dravictorianunesferoldi.com.br` e ainda não foi contratado. A prévia está com indexação desabilitada; habilitar somente na publicação aprovada.

## Documentação

- [Visão e escopo](docs/01-visao-e-escopo.md)
- [Arquitetura do monorepo](docs/02-arquitetura.md)
- [Atendimento pelo WhatsApp](docs/03-atendimento-whatsapp.md)
- [Plano de execução e decisões pendentes](docs/04-plano-de-execucao.md)
- [Resumo do protótipo de WhatsApp v2](docs/05-resumo-prototipo-whatsapp-v2.md)
- [Requisitos consolidados da landing e do atendimento](docs/06-requisitos-consolidados.md)
- [Pesquisa de viabilidade e proposta](docs/07-pesquisa-e-proposta.md)
- [Proposta resumida para a doutora](docs/08-proposta-resumida.md)
- [Primeira landing e pendências de publicação](docs/09-primeira-landing.md)

## Proposta para validação

PDF: [Proposta de desenvolvimento](output/pdf/proposta-desenvolvimento-victoria-feroldi.pdf).

A proposta v1.6 tem duas páginas com linguagem direta: R$ 500 pela landing e R$ 200 pelo bot/chat, total R$ 700. O volume informado é cerca de 20 pessoas por mês. A previsão total mensal é R$ 200-230: serviços de R$ 150-180 (incluindo uma caixa humana Chatwoot de aproximadamente R$ 114) + R$ 50 pela manutenção com correções pontuais do fluxo existente. Novas funcionalidades e integrações serão orçadas à parte. Rotas com coexistência têm outro custo. Tarifa, câmbio, elegibilidade e prazo de suporte ainda precisam ser confirmados. A pesquisa detalhada permanece no documento 07; os honorários atuais estão na proposta resumida, documento 08.

## Referência existente

A proposta também compara a alternativa para a doutora assumir o chat pelo aplicativo WhatsApp Business: integração via 360dialog, sem Chatwoot, com previsão total de R$ 400-430/mês incluindo R$ 50 de manutenção. Elegibilidade do número, sincronização e pausa do bot precisam ser validadas. As opções são alternativas, não custos cumulativos; o desenvolvimento permanece em R$ 700.

A landing page de esboço em `C:/dev/lp_vic` foi usada como referência. A nova versão em `apps/landing` reaproveita os contatos e fontes, com layout refeito e sem alterar o esboço original.

A especificação do atendimento foi localizada em `Prototipo_WhatsApp_Victoria_v2.pdf` e analisada integralmente. O resumo em `docs/05-resumo-prototipo-whatsapp-v2.md` registra o fluxo e as lacunas para a implementação; propostas adicionais nos demais documentos não são requisitos do PDF.

A orientação atual do usuário exclui São José dos Campos. O documento `docs/06-requisitos-consolidados.md` reúne os prompts históricos e as correções atuais e prevalece sobre referências antigas conflitantes.





