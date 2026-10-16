"""Proposta voltada à doutora; pesquisa técnica preservada no documento 07."""
def build_pages(page,p,h,call,tbl):
    page('PROPOSTA DE DESENVOLVIMENTO','Seu site e seu atendimento\nno WhatsApp','Dra. Victoria Nunes Feroldi · Versão para validação · 7 de outubro de 2026',[
      p('Uma presença online clara e um atendimento mais organizado, para ajudar seus pacientes a encontrar informações e chegar ao canal certo de agendamento.'),
      h('1. Site de apresentação - R$ 500'),
      p('Site adaptado para celular e computador, com apresentação da doutora, locais e modalidades de atendimento, dúvidas frequentes e botões de WhatsApp. Terá versões clara e escura.'),
      p('Atendimento online, em Taubaté e em Campos do Jordão. Cada modalidade terá o contato correto. São José dos Campos fica fora do projeto.'),
      h('2. Atendimento automático - R$ 200'),
      p('Assistente no WhatsApp central para orientar novos pacientes e pacientes em acompanhamento, apresentar as opções de agendamento e encaminhar ao atendimento responsável. Uma pessoa poderá assumir a conversa quando necessário.'),
      p('O fluxo seguirá o protótipo já preparado. Será um atendimento administrativo: não realizará consultas, diagnósticos ou prescrição de medicamentos.'),
      call('<b>Investimento para desenvolver: R$ 700 no total.</b><br/>R$ 500 pelo site + R$ 200 pelo atendimento automático. Os serviços para manter tudo online são pagos à parte.'),
      h('O que ficará para depois'),
      p('Agenda integrada, cobrança automática, emissão de nota fiscal, atendimento por áudio e automação dos números das clínicas. Esses itens não fazem parte desta primeira versão.'),
      h('Antes de publicar'),
      p('Enviar foto, logo e biografia; confirmar contatos e horários; contratar <b>dravictorianunesferoldi.com.br</b>; aprovar os textos e o fluxo. A primeira prévia terá imagens e biografia provisórias.'),
      h('Aceite do projeto'),
      p('Escolher como a doutora assumirá as conversas, aprovar o site e testar o fluxo. Confirmar custos, prazo, pagamento e condições de suporte antes da ativação.'),
      p('<b>Aprovação da doutora:</b> ____________________ &nbsp; <b>Data:</b> ____/____/______'),
      p('Pesquisa: 06-07/10/2026. Referências: <link href="https://www.chatwoot.com/pricing" color="#047857">Chatwoot</link> e <link href="https://docs.360dialog.com/docs/get-started/pricing" color="#047857">360dialog</link>. Câmbio de referência: US$ 1 = R$ 6; EUR 1 = R$ 6,50.'),
    ])
    page('CUSTOS E APROVAÇÃO','Quanto custa manter\ntudo funcionando?','Estimativa para cerca de 20 pessoas atendidas por mês no WhatsApp.',[
      call('<b>Para a doutora assumir a conversa quando necessário:</b><br/>Escolha uma das alternativas abaixo. O bot pausa enquanto ela responde. Os totais incluem os serviços e R$ 50/mês de manutenção.'),
      tbl(['Como a doutora responde','Total mensal estimado'],[
        ['Painel no navegador (Chatwoot)','R$ 200 a R$ 230'],
        ['Aplicativo WhatsApp Business (via 360dialog)','R$ 400 a R$ 430'],
      ],[.66,.34]),
      p('<b>Opção 1 - Painel no navegador:</b> contratar o Chatwoot por cerca de R$ 114/mês para uma pessoa. A doutora lê e responde às mensagens pelo painel. Esse valor já está incluído no total de R$ 200 a R$ 230.'),
      p('<b>Opção 2 - Pelo próprio WhatsApp Business:</b> manter o aplicativo e o bot no mesmo número exige uma integração compatível. A alternativa pesquisada, 360dialog, custa a partir de 49 euros/mês. O total previsto é R$ 400 a R$ 430, sem contratar o Chatwoot. É preciso confirmar a elegibilidade do número e testar a integração antes de ativar.'),
      h('Custos comuns às duas opções'),
      tbl(['Serviço','Custo estimado'],[
        ['Hospedagem do site','R$ 0/mês'],
        ['Estrutura do assistente','R$ 30/mês'],
        ['Mensagens do WhatsApp','R$ 0 a R$ 8/mês'],
        ['Domínio .com.br','Cerca de R$ 40/ano'],
        ['Manutenção do fluxo existente','R$ 50/mês'],
      ],[.66,.34]),
      p('Esses custos já estão incluídos nos totais acima; não devem ser somados novamente. O domínio é pago anualmente, com provisão considerada na faixa mensal.'),
      p('<b>Manutenção - R$ 50/mês:</b> correções pontuais de problemas no fluxo existente. Novas funções, integrações e mudanças de escopo serão orçadas à parte. Prazo de resposta será combinado na contratação.'),
      p('Os totais são estimativas, sujeitos a câmbio, tributos, tarifas e uso. A opção pelo aplicativo considera o fornecedor pesquisado; outros fornecedores podem ter preços diferentes.'),
    ])
