"""Conteúdo da proposta v1.1, ajustado ao preço e volume informados pelo usuário."""
def build_pages(page,p,h,call,tbl):
    page('PROPOSTA | VERSÃO 1.1','Presença digital e\natendimento pelo WhatsApp',
         'Dra. Victoria Nunes Feroldi | proposta ajustada para uma operação pequena',[
    call('<b>Investimento inicial informado pelo prestador: R$ 600.</b> Landing page por R$ 400 e implantação do bot/chat por R$ 200. Serviços externos são pagos separadamente.'),
    tbl(['Entrega / operação','Valor ou premissa'],[
    ['Landing page','R$ 400, pagamento único'],
    ['Bot/chat de atendimento','R$ 200, pagamento único'],
    ['Total de desenvolvimento','R$ 600'],
    ['Volume informado','Cerca de 20 pessoas atendidas por mês'],
    ['Operação recomendada, API direta + 1 atendente','Reserva de R$ 150-180/mês em serviços'],
    ],[.61,.39]),
    p('A mensalidade acima é estimativa de fornecedores, sem honorários recorrentes de manutenção e antes de tributos/câmbio efetivo. Usa dólar de planejamento de R$ 6,00. Não é preço fixo garantido dos serviços.'),
    h('Recomendação para começar'),
    p('Landing estática; bot por menus no número central; uma caixa de atendimento humano; coleta fiscal protegida. IA pode ser acrescentada se necessária. Para o volume atual, não é preciso contratar dois atendentes nem Vercel Pro para servir a landing estática.'),
    p('Se manter o aplicativo WhatsApp Business no mesmo número for obrigatório, a rota de coexistência precisa ser validada. Ela não está garantida no orçamento da integração direta e pode elevar a mensalidade.'),
    p('<b>Pesquisa:</b> 6 de outubro de 2026. Valores comerciais informados pelo prestador. Esta versão substitui a v1.0 e separa investimento inicial de despesas recorrentes com fornecedores.'),
    ])

    page('02 | ESCOPO','O que será desenvolvido','O mesmo fluxo, com infraestrutura proporcional ao volume atual.',[
    h('Landing page - R$ 400'),
    p('Evolução do esboço existente: apresentação, formação, processo de atendimento, locais, FAQ e contato. Identidade Inter/Lora e verde esmeralda, claro/escuro, versão móvel, acessibilidade, correção do FAQ e metadados. Sem preços públicos, depoimentos ou promessa de resultados.'),
    tbl(['Destino','Modalidade / contato'],[
    ['Online','Particular, quarta 8h-12h. (12) 99793-2353.'],
    ['Taubaté','Clínica Fator Humano, particular e convênio. (12) 99160-1313.'],
    ['Campos do Jordão','Presencial particular; local/horários com a equipe. (12) 99658-3276.'],
    ],[.28,.72]),
    h('Bot/chat - R$ 200'),
    p('Primeiro atendimento: apresentação e agendamento. Acompanhamento: agendamento, solicitações ou urgência. Particular: Online, Taubaté ou Campos; dados fiscais e encaminhamento. Convênio: somente Taubaté, sem formulário fiscal. Online informa R$ 400 e pagamento antes da consulta, conforme o protótipo.'),
    p('Solicitações informa que documentos e receitas dependem de consulta/indicação médica. Urgência usa texto fixo aprovado, orientação de procura de serviço presencial e SAMU 192. Voltar/menu e entrada inválida tratados. Não haverá diagnóstico ou confirmação automática de agenda/pagamento.'),
    h('Operação e dados'),
    p('Implantação em um número central, ainda a confirmar. Links das clínicas continuam diretos e seus números não recebem bots nesta versão. Atendente assume no central com bot pausado; retomada explícita. Testar deduplicação e falha de envio.'),
    p('Formulário fiscal HTTPS por link temporário, sem CPF no chat/URL; validação e acesso autenticado pela responsável. Definir finalidade, retenção e exclusão. Revisar publicidade da pós-graduação e cards com a doutora, conforme orientações CFM consultadas. [S02, S14-S16]'),
    call('O preço reduzido foi escolhido pelo prestador e não elimina os cuidados de acesso, proteção de dados e atendimento humano. Integração com agenda, pagamentos, nota fiscal, áudio e painel próprio completo ficam fora da primeira versão.'),
    ])

    page('03 | CUSTO MENSAL','Mensalidade da estrutura enxuta','API direta, um número e uma pessoa atendendo pela caixa web.',[
    p('20 pessoas não equivalem necessariamente a 20 conversas. Para simular, consideramos uma conversa por pessoa/mês, com 10 mensagens de entrada e 10 de saída: 200 entradas + 200 saídas. Sem campanhas, áudios ou lembretes proativos.'),
    tbl(['Serviço','Premissa de preço','Estimativa mensal'],[
    ['Landing estática Cloudflare','Ativos estáticos gratuitos [S19, S21]','R$ 0'],
    ['Backend Cloudflare Workers','Plano pago base de US$ 5 [S19]','R$ 30'],
    ['Banco D1','Dentro da franquia incluída [S20]','R$ 0 adicional'],
    ['Caixa Chatwoot Cloud','1 atendente x US$ 19 [S07-S08]','R$ 114'],
    ['Domínio .br','R$ 40/ano [S12]','R$ 3,33 de provisão'],
    ['Mensagens Meta','200 saídas de serviço [S01, S03]','R$ 0-8,16'],
    ['Total de serviços','Antes de tributos/excedentes','R$ 147,33-155,49'],
    ],[.39,.35,.26]),
    p('Fórmula: (US$ 5 + US$ 19) x R$ 6 + R$ 40/12 = R$ 147,33. Domínio é pago anualmente, não mensalmente. Backend e banco exigem adaptação/teste no runtime e observação de limites; não incluem armazenamento grande de mídia.'),
    h('Por que a faixa das mensagens?'),
    p('A página pública Meta informa serviço gratuito na janela; a 360dialog anuncia cobrança desde outubro de 2026 a US$ 0,0068/saída no Brasil e franquia de 1.000 mensagens de serviço/número. Com 200 saídas, o cenário com franquia também dá zero; sem franquia, 200 x 0,0068 x 6 = R$ 8,16. A tarifa da conta será confirmada antes da conexão. [S01, S03]'),
    call('<b>Reserva prática: R$ 150-180/mês.</b> O limite superior inclui aproximadamente 15% de folga sobre R$ 155,49. Tributos, variação cambial e excedentes seguem as faturas; não há garantia de teto. Não foi incluída uma cobrança de manutenção do prestador.'),
    p('<b>IA, se usada:</b> a referência anterior de 10 mil tokens de entrada e 2 mil de saída acumulados/conversa resulta em aproximadamente R$ 0,86/mês para 20 conversas com GPT-4.1 mini. Sem áudio/ferramentas, uso mínimo/prepagamento e regras do fornecedor a conferir. O modelo não está escolhido. [S13]'),
    ])

    page('04 | ALTERNATIVAS','O que pode mudar a mensalidade','A rotina do aplicativo define a escolha da integração.',[
    tbl(['Cenário','Custo calculado','Condição'],[
    ['API direta + caixa web, Workers pago','R$ 147-155/mês','Reserva recomendada R$ 150-180. App no mesmo número não garantido.'],
    ['API direta + caixa web, Workers gratuito','R$ 117-125/mês','Economiza R$ 30; validar limites. Menos margem de execução e sem compromisso de disponibilidade.'],
    ['Twilio + caixa web, Workers pago','R$ 159-167/mês','Adiciona R$ 12 para 400 mensagens x US$ 0,005 x R$ 6. Coexistência não comprovada.'],
    ['360dialog + aplicativo, Workers pago','R$ 352-360/mês','EUR 49 x R$ 6,50, sem Chatwoot. Só se coexistência e pausa pelo app forem comprovadas.'],
    ],[.38,.23,.39]),
    p('Alternativas usam o mesmo domínio e volume da página anterior, antes de tributos e folga. São cenários mutuamente alternativos, não assinaturas que devem ser somadas. Valores arredondados; fontes S04-S08 e S19-S20.'),
    h('Se ela quiser continuar respondendo pelo celular'),
    p('Coexistência permite aplicativo e API no mesmo número na rota documentada pela 360dialog, mas depende da conta e tem limitações de dispositivos/eco. Não basta remover a caixa web do orçamento: ainda precisamos de um meio comprovado para o humano assumir e o bot pausar. Confirmar esse requisito antes da implantação. [S05]'),
    h('Economia sem criar uma obrigação maior'),
    p('Bot por menus dispensa IA para executar o PDF. Landing estática dispensa servidor Next.js sempre ativo; ajustar exportação e imagens. Uma única caixa humana basta como premissa inicial. Não implantar três números nem painel completo próprio para este piloto.'),
    h('Operação e suporte'),
    p('Custo mensal aqui é de serviços. Manutenção de código, atendimento técnico e novas funcionalidades não têm mensalidade definida pelo prestador nesta versão. A responsável continua atendendo pacientes, confirmando agenda/pagamento e emitindo documentos/nota. Crescimento do uso exigirá nova conferência do orçamento.'),
    call('Exemplo do primeiro ano na opção recomendada: R$ 600 de desenvolvimento + US$ 24 x 6 x 12 + R$ 40 de domínio + até R$ 8,16 x 12 em mensagens = R$ 2.368-2.466. Projeção sem folga, impostos, mão de obra recorrente ou opcionais.'),
    ])

    page('05 | ACEITE','Validação e condições de entrega','R$ 600 de desenvolvimento; serviços externos separados.',[
    p('<b>Contratante:</b> Dra. Victoria Nunes Feroldi.<br/><b>Prestador:</b> __________________________________________'),
    h('Critérios para validar'),
    p('[  ] Landing com três destinos corretos, sem São José ou preços públicos.<br/>[  ] Layout móvel/desktop, claro/escuro, teclado e FAQ sem cortes revisados.<br/>[  ] Formação, avisos, conteúdo e dados de contato aprovados pela doutora.<br/>[  ] Todos os caminhos do fluxo, voltar/menu e erros testados com dados fictícios.<br/>[  ] Formulário fiscal com token expirável, acesso protegido e retenção definida.<br/>[  ] Atendimento humano no central com pausa/retomada do bot demonstradas.<br/>[  ] Falha de envio, webhook repetido e recuperação testados; instruções entregues.'),
    h('Decisões antes de conectar'),
    p('Número automatizado: ________________________________________<br/>Manter aplicativo no mesmo número: [  ] sim  [  ] não  [  ] a definir<br/>Rota: [  ] direta  [  ] Twilio  [  ] 360dialog  [  ] outra: __________<br/>Atendente responsável e horário: ______________________________<br/>IA: [  ] sem IA no início  [  ] usar IA, consumo separado<br/>Limite mensal de serviços aprovado: R$ ________________________'),
    h('Condições comerciais'),
    p('Landing: <b>R$ 400</b>. Bot/chat: <b>R$ 200</b>. Total: <b>R$ 600</b>.<br/>Forma de pagamento: ________________________________________<br/>Tributos do desenvolvimento: _________________________________<br/>Início e prazo acordados: _____________________________________<br/>Suporte/correção pós-entrega: __________________________________'),
    p('Domínio, contas e faturamento de terceiros sob titularidade/acesso acordados com a contratante. Serviços pagos conforme faturas; o limite aprovado orienta alertas e eventual pausa/revisão, não altera preços externos. Mudanças de escopo serão acertadas antes da execução.'),
    call('O aceite inclui a versão 1.1 e a rota assinalada após a prova técnica. Não conectar o número atual sem confirmar acesso, tarifa, funcionamento humano e eventual coexistência. Dados, privacidade e conteúdo devem estar validados para o piloto.'),
    p('Contratante: ________________________ Data: ____/____/______<br/><br/>Prestador: __________________________ Data: ____/____/______'),
    ])

    page('06 | FONTES','Referências da pesquisa','Fontes de preços e requisitos; consulta em 6 de outubro de 2026.',[('sources',)])
