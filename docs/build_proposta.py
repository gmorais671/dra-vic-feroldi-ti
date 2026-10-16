"""Gera a proposta e sua versão Markdown a partir do conteúdo abaixo.
Preços pesquisados em 06/10/2026; projeções não são cotação comercial.
"""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, Color, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output' / 'pdf' / 'proposta-desenvolvimento-victoria-feroldi.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
for name, file in [('Body','segoeui.ttf'),('Bold','segoeuib.ttf'),('Italic','segoeuii.ttf'),('Serif','georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')

SOURCES = [
('S01','Meta | preços da plataforma','https://whatsappbusiness.com/products/platform-pricing/','Página pública consultada: serviço gratuito na janela de atendimento. Diverge do comunicado recente do provedor S03.'),
('S02','Meta | política de mensagens','https://whatsappbusiness.com/policy/','Janela de 24h, templates, encaminhamento humano e restrição de identificadores completos.'),
('S03','360dialog | atualização de cobrança','https://360dialog.com/blog/whatsapp-service-message-charging-october-2026/','Comunicado do provedor: cobrança desde 01/10/2026, franquia de 1.000 mensagens de serviço/número e Brasil a US$ 0,0068. Confirmação comercial pendente.'),
('S04','360dialog | planos','https://360dialog.com/pricing','Regular: EUR 49 por número/mês, mais tarifas Meta. Assinatura de API; caixa humana e compatibilidade são avaliadas por rota.'),
('S05','360dialog | coexistência','https://docs.360dialog.com/docs/resources/phone-numbers/coexistence','Aplicativo e API no mesmo número, com requisitos e limitações de sincronização e dispositivos.'),
('S06','Twilio | preços WhatsApp','https://www.twilio.com/en-us/whatsapp/pricing','US$ 0,005 por mensagem recebida ou enviada, além das tarifas Meta aplicáveis.'),
('S07','Chatwoot | preços Cloud','https://www.chatwoot.com/pricing','Startups: US$ 19/agente/mês; gratuito limitado a live chat. Cloud hospedado nos EUA.'),
('S08','Chatwoot | bot externo e humano','https://app.chatwoot.com/hc/user-guide/articles/1677497472-how-to-use-agent-bots','Webhooks, API e passagem da conversa para agente humano; validar habilitação no plano escolhido.'),
('S09','Render | base de infraestrutura','https://render.com/articles/how-much-does-cloud-application-hosting-cost-for-small-businesses','Referência oficial de US$ 13/mês: serviço sempre ativo + Postgres pequeno; capacidade a validar.'),
('S10','Vercel | preços','https://vercel.com/pricing','Pro a partir de US$ 20/mês, com excedentes conforme uso e equipe.'),
('S11','Vercel | restrições Hobby','https://vercel.com/docs/plans/hobby','Hobby destinado a uso pessoal não comercial; não adotado nesta proposta.'),
('S12','Registro.br | renovação anual','https://registro.br/dominio/processo-de-liberacao/resultado/','Página oficial cita manutenção normal de R$ 40 por ano; confirmar no registro do domínio disponível.'),
('S13','OpenAI | GPT-4.1 mini','https://developers.openai.com/api/docs/models/gpt-4.1-mini','Referência de cálculo: US$ 0,40/1M tokens de entrada e US$ 1,60/1M de saída. Não é escolha definitiva do modelo.'),
('S14','CFM | publicidade e identificação','https://publicidademedica.cfm.org.br/','Orientação sobre identificação e expressão NÃO ESPECIALISTA para divulgação de pós-graduação sem RQE.'),
('S15','CFM | proibições gerais','https://publicidademedica.cfm.org.br/manual/aplicacao-pratica/capitulo-10','Revisar anúncio de tratamento de doenças específicas por não especialista e promessas de resultados.'),
('S16','LGPD | texto legal','https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm','Dados de saúde são sensíveis; observar finalidade, necessidade, segurança e regras de tratamento/transferência.'),
('S17','360dialog | mensagens livres e cobradas','https://docs.360dialog.com/docs/get-started/pricing/free-vs-billed-messaging','Documentação do provedor diferencia permissão de envio e cobrança; também diverge da página pública Meta.'),
('S18','360dialog | mensagens interativas','https://docs.360dialog.com/partner/messaging/sending-and-receiving-messages/text-messages/interactive-messages','Listas e botões têm limites; as telas do PDF precisam de adaptação à interface real.'),
]

PAGES = []
def page(kicker,title,subtitle,blocks):
    PAGES.append(dict(kicker=kicker,title=title,subtitle=subtitle,blocks=blocks))
def p(text): return ('p',text)
def h(text): return ('h',text)
def call(text): return ('call',text)
def tbl(headers,rows,widths): return ('table',headers,rows,widths)

from proposta_resumida import build_pages
SOURCES = [s for s in SOURCES if s[0] in ('S01','S02','S03','S04','S05','S06','S07','S08','S12','S13','S14','S15','S16')]
SOURCES.extend([
('S19','Cloudflare | Workers e ativos estáticos','https://developers.cloudflare.com/workers/platform/pricing/','Plano pago a partir de US$ 5/mês; ativos estáticos gratuitos. Free é alternativa sujeita aos limites.'),
('S20','Cloudflare | D1','https://developers.cloudflare.com/d1/platform/pricing/','Banco com franquias de leituras, escritas e armazenamento; excedentes pagos ou bloqueios no Free.'),
('S21','Cloudflare | Next.js estático','https://developers.cloudflare.com/pages/framework-guides/nextjs/deploy-a-static-nextjs-site/','Guia oficial para exportação estática; funções de servidor e imagens precisam de adaptação.')])
build_pages(page,p,h,call,tbl)

# O conteúdo cabe em páginas determinadas, com validação explícita de overflow.
W,H=595.276,841.89
LEFT=46; WIDTH=W-92
GREEN=HexColor('#047857'); INK=HexColor('#182f2a'); MUTED=HexColor('#52665f'); MINT=HexColor('#ecf6f0')
styles={
 'p':ParagraphStyle('p',fontName='Body',fontSize=10.1,leading=14.6,textColor=INK,spaceAfter=9),
 'h':ParagraphStyle('h',fontName='Bold',fontSize=11.5,leading=16,textColor=GREEN,spaceAfter=6),
 'call':ParagraphStyle('call',fontName='Body',fontSize=10.1,leading=14.4,textColor=INK),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=9.2,leading=12.4,textColor=INK),
 'thead':ParagraphStyle('thead',fontName='Bold',fontSize=9.1,leading=12.2,textColor=white),
 'src':ParagraphStyle('src',fontName='Body',fontSize=8.2,leading=10.6,textColor=INK),
}
c=canvas.Canvas(str(OUT),pagesize=(W,H))
c.setTitle('Proposta de desenvolvimento - Dra. Victoria Nunes Feroldi')
c.setAuthor('Planejamento do ecossistema Victoria Feroldi')
markdown=['# Proposta resumida para a doutora\n','Data: 7 de outubro de 2026. Versão 1.6.\n']
metrics=[]
def draw_para(text,kind,y):
    obj=Paragraph(text,styles[kind]); _,ht=obj.wrap(WIDTH,700)
    if y-ht<54: raise ValueError(f'Overflow página {c.getPageNumber()}, {kind}: {text[:70]}')
    obj.drawOn(c,LEFT,y-ht)
    return y-ht-(styles[kind].spaceAfter or 9)

for n,pg in enumerate(PAGES,1):
    c.setFillColor(GREEN); c.rect(0,H-7,W,7,fill=1,stroke=0)
    c.setFont('Bold',8); c.setFillColor(GREEN); c.drawString(LEFT,H-43,pg['kicker'])
    title=Paragraph(escape(pg['title']).replace('\n','<br/>'),ParagraphStyle('title',fontName='Serif',fontSize=26 if n==1 else 25,leading=31,textColor=INK))
    _,th=title.wrap(WIDTH,120); title.drawOn(c,LEFT,H-65-th)
    y=H-65-th-14
    sub=Paragraph(pg['subtitle'],ParagraphStyle('subtitle',fontName='Body',fontSize=10.3,leading=14.5,textColor=MUTED))
    _,sh=sub.wrap(WIDTH,80); sub.drawOn(c,LEFT,y-sh); y-=sh+23
    markdown.append('\n## '+pg['title'].replace('\n',' ')+'\n\n'+pg['subtitle']+'\n')
    for b in pg['blocks']:
        kind=b[0]
        if kind in ('p','h'):
            y=draw_para(b[1],kind,y)
            clean=b[1].replace('<br/>','\n').replace('<b>','**').replace('</b>','**')
            markdown.append(('\n### ' if kind=='h' else '\n')+clean+'\n')
        elif kind=='call':
            para=Paragraph(b[1],styles['call']); _,ht=para.wrap(WIDTH-28,700)
            bh=ht+24
            if y-bh<54: raise ValueError(f'Overflow callout {n}')
            c.setFillColor(MINT); c.roundRect(LEFT,y-bh,WIDTH,bh,8,fill=1,stroke=0)
            c.setFillColor(GREEN); c.rect(LEFT,y-bh+8,3,bh-16,fill=1,stroke=0)
            para.drawOn(c,LEFT+14,y-12-ht); y-=bh+12
            markdown.append('\n> '+b[1].replace('<b>','**').replace('</b>','**')+'\n')
        elif kind=='table':
            headers,rows,widths=b[1:]
            data=[[Paragraph(escape(x),styles['thead']) for x in headers]]
            data += [[Paragraph(escape(x),styles['cell']) for x in row] for row in rows]
            t=Table(data,colWidths=[WIDTH*x for x in widths],hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),GREEN),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,1),(-1,-1),[HexColor('#f4f7f5'),white]),('LINEBELOW',(0,0),(-1,-1),.35,HexColor('#dae5de'))]))
            _,ht=t.wrap(WIDTH,700)
            if y-ht<54: raise ValueError(f'Overflow table {n}')
            t.drawOn(c,LEFT,y-ht); y-=ht+13
            markdown.append('\n| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows)+'\n')
        elif kind=='sources':
            for sid,label,url,note in SOURCES:
                text=f'<b>{sid}</b> - <link href="{escape(url)}" color="#047857"><u>{escape(label)}</u></link><br/>{escape(note)}'
                obj=Paragraph(text,styles['src']); _,ht=obj.wrap(WIDTH,700)
                if y-ht<54: raise ValueError(f'Overflow sources {sid}')
                obj.drawOn(c,LEFT,y-ht); y-=ht+8
                markdown.append(f'\n- [{sid} - {label}]({url}): {note}\n')
    metrics.append((n,round(y,1)))
    c.setStrokeColor(HexColor('#dce7e0')); c.line(LEFT,43,W-LEFT,43)
    c.setFillColor(MUTED); c.setFont('Body',7.4)
    c.drawString(LEFT,28,'VICTORIA FEROLDI | Proposta para validação | 07/10/2026')
    c.drawRightString(W-LEFT,28,f'{n:02d} / {len(PAGES):02d}')
    c.showPage()
c.save()
(ROOT/'docs'/'08-proposta-resumida.md').write_text('\n'.join(markdown),encoding='utf-8')
print('PDF:',OUT)
print('Limites inferiores do conteúdo:',metrics)
