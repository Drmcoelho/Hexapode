from pathlib import Path
import re

BG='#F7F4EC'; PAPER='#FFFDF8'; GRAPH='#2B2E34'; MUTED='#6A727A'; RULE='#DCD2BE'; BLUE='#1D4E7A'; TEAL='#1696A3'; GREEN='#2E7D69'; TERR='#C45A3C'; RED='#B2473F'; AMBER='#D39A2E'; PURPLE='#76659A'; SAND='#E8E1D1'
ROOT=Path('assets/advanced/A021')
ASSETS=[
('201','Paleta oficial aplicada','Aplicação semântica da paleta Hexápode em anatomia, fisiologia, alertas e interface.'),
('202','Tipografia aplicada','Hierarquia tipográfica responsiva para títulos, corpo, legendas e dados clínicos.'),
('203','Biblioteca de ícones aplicada','Sistema iconográfico transversal com anatomia, fisiologia, risco e ações clínicas.'),
('204','Corpo humano masculino aplicado','Mapa anatômico masculino esquemático com integração entre regiões e sistemas.'),
('205','Corpo humano feminino aplicado','Mapa anatômico feminino esquemático com integração entre regiões e sistemas.'),
('206','Corpo infantil aplicado','Referência pediátrica esquemática com proporções, regiões e marcos de crescimento.'),
('207','Grid editorial aplicado','Malha de 12 colunas, espaçamento e adaptações responsivas para atlas e painéis.'),
('208','Sistema de setas aplicado','Linguagem visual de fluxos, causalidade, feedback, migração e decisão clínica.'),
('209','Sistema de cores aplicado','Mapeamento semântico de cor para estrutura, fluxo, lesão, alerta e interface.'),
('210','Templates aplicados','Família de templates para capítulos, comparações, algoritmos, casos e monitorização.'),
]
CONSUMERS='[Respira, Ventila, Cardio, Trauma, Neuro, Nefrologia, Ultrassom, Farmacologia, Pediatria, Emergências, Educação]'

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def card(x,y,w,h,t,c=BLUE): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{PAPER}" stroke="{RULE}" stroke-width="3"/><text x="{x+24}" y="{y+44}" font-family="Arial" font-size="25" font-weight="700" fill="{c}">{esc(t)}</text>'
def base(title,desc,aid,body):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1200" role="img" aria-labelledby="t d"><title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc><rect width="1600" height="1200" fill="{BG}"/><text x="72" y="90" font-family="Arial" font-size="24" font-weight="700" fill="{BLUE}">HEXÁPODE · CAMADA AVANÇADA</text><text x="72" y="162" font-family="Georgia" font-size="58" font-weight="700" fill="{GRAPH}">{esc(title)}</text><text x="74" y="208" font-family="Arial" font-size="24" fill="{MUTED}">{esc(desc)}</text><line x1="72" y1="238" x2="1528" y2="238" stroke="{RULE}" stroke-width="3"/>{body}<text x="72" y="1150" font-family="Arial" font-size="20" fill="{MUTED}">HEX-A021-{aid} · Hexápode · avançado</text></svg>'''
def palette():
 s=''; rows=[('Estrutura',BLUE),('Fluxo',TEAL),('Resposta segura',GREEN),('Tecido',TERR),('Lesão',RED),('Alerta',AMBER),('Neutro',SAND)]
 for i,(n,c) in enumerate(rows): y=300+i*95; s+=f'<rect x="90" y="{y}" width="90" height="58" rx="12" fill="{c}"/><text x="205" y="{y+38}" font-family="Arial" font-size="24" fill="{GRAPH}">{n}</text>'
 for i,(t,c) in enumerate([('Anatomia',BLUE),('Fisiologia',TEAL),('Estados',RED)]):
  x=450+i*350;s+=card(x,300,310,650,t,c)+f'<circle cx="{x+155}" cy="560" r="95" fill="{SAND}" stroke="{c}" stroke-width="8"/><path d="M{x+70} 760 H{x+240}" stroke="{c}" stroke-width="14"/><polygon points="{x+240},760 {x+205},740 {x+205},780" fill="{c}"/>'
 return s
def typography():
 s=card(80,290,520,700,'Escala tipográfica'); samples=[('Título editorial',54,'Georgia',BLUE),('Título de seção',38,'Georgia',GRAPH),('Subtítulo informativo',29,'Arial',TEAL),('Corpo de texto',23,'Arial',GRAPH),('Legenda e anotação',18,'Arial',MUTED),('DADO 82 mmHg',30,'Courier New',BLUE)]
 for i,(t,fs,f,c) in enumerate(samples): s+=f'<text x="120" y="{410+i*90}" font-family="{f}" font-size="{fs}" fill="{c}">{t}</text>'
 s+=card(650,290,400,700,'Responsividade')
 for i,(w,l) in enumerate([(330,'Desktop'),(250,'Tablet'),(170,'Mobile')]): y=410+i*180;s+=f'<rect x="690" y="{y}" width="{w}" height="130" rx="14" fill="{PAPER}" stroke="{BLUE}" stroke-width="3"/><text x="710" y="{y+35}" font-family="Arial" font-size="20" fill="{BLUE}">{l}</text><line x1="710" y1="{y+65}" x2="{680+w-20}" y2="{y+65}" stroke="{GRAPH}" stroke-width="5"/>'
 s+=card(1100,290,400,700,'Combinação canônica')+f'<text x="1160" y="540" font-family="Georgia" font-size="92" fill="{GRAPH}">Aa</text><text x="1300" y="500" font-family="Arial" font-size="28" fill="{BLUE}">Georgia + Arial</text><text x="1300" y="550" font-family="Arial" font-size="21" fill="{MUTED}">clássico e técnico</text>'
 return s
def icons():
 s=''; groups=[('Anatomia',BLUE),('Fisiologia',GREEN),('Respiração',TEAL),('Cardio',RED),('Neuro',PURPLE),('Nefro',BLUE),('Trauma',AMBER),('Farmaco',GREEN),('Alertas',RED)]
 for i,(t,c) in enumerate(groups):
  x=80+(i%3)*500;y=290+(i//3)*250;s+=card(x,y,450,215,t,c)
  for j in range(4): cx=x+70+j*95;cy=y+135;s+=f'<circle cx="{cx}" cy="{cy}" r="28" fill="none" stroke="{c}" stroke-width="5"/><path d="M{cx-15} {cy} H{cx+15} M{cx} {cy-15} V{cx+15}" stroke="{c}" stroke-width="4"/>'
 return s
def body(kind):
 s=card(80,290,300,720,'Mapa regional')+card(1240,290,280,720,'Integração sistêmica')
 child=kind=='child'; female=kind=='female'
 for k,cx in enumerate([650,1030]):
  hr=74 if child else 58;tw=(175 if female else 210)*(0.82 if child else 1);th=255 if child else 310;y=360
  s+=f'<circle cx="{cx}" cy="{y}" r="{hr}" fill="{SAND}" stroke="{BLUE}" stroke-width="4"/><path d="M{cx-tw/2} {y+hr+25} Q{cx} {y+hr-5} {cx+tw/2} {y+hr+25} L{cx+tw*.42} {y+hr+th} Q{cx} {y+hr+th+40} {cx-tw*.42} {y+hr+th} Z" fill="{PAPER}" stroke="{GRAPH}" stroke-width="5"/><ellipse cx="{cx-42}" cy="{y+190}" rx="43" ry="68" fill="#D8ECEB" stroke="{TEAL}" stroke-width="4"/><ellipse cx="{cx+42}" cy="{y+190}" rx="43" ry="68" fill="#D8ECEB" stroke="{TEAL}" stroke-width="4"/><path d="M{cx} {y+210} C{cx-28} {y+175} {cx-60} {y+230} {cx} {y+275} C{cx+60} {y+230} {cx+28} {y+175} {cx} {y+210}Z" fill="#F4DDD9" stroke="{RED}" stroke-width="4"/><ellipse cx="{cx}" cy="{y+350}" rx="80" ry="55" fill="#ECE5F4" stroke="{PURPLE}" stroke-width="4"/><path d="M{cx-tw/2} {y+160} L{cx-175} {y+520}" stroke="{GRAPH}" stroke-width="27" stroke-linecap="round"/><path d="M{cx+tw/2} {y+160} L{cx+175} {y+520}" stroke="{GRAPH}" stroke-width="27" stroke-linecap="round"/><path d="M{cx-65} {y+hr+th} L{cx-78} {y+770}" stroke="{TERR}" stroke-width="32" stroke-linecap="round"/><path d="M{cx+65} {y+hr+th} L{cx+78} {y+770}" stroke="{TERR}" stroke-width="32" stroke-linecap="round"/>'
 return s
def grid():
 s=card(80,290,300,700,'Regras de grid')+card(1240,290,280,700,'Responsivo');x=430;y=300;W=760;H=620;s+=f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="{PAPER}" stroke="{BLUE}" stroke-width="4"/>'
 for i in range(13): xx=x+i*W/12;s+=f'<line x1="{xx}" y1="{y}" x2="{xx}" y2="{y+H}" stroke="#BFD1E0" stroke-width="2" stroke-dasharray="8 8"/>'
 for xx,yy,w,h,c in [(465,365,175,180,BLUE),(660,365,220,180,TEAL),(900,365,250,180,AMBER),(465,575,380,250,GREEN),(870,575,280,250,PURPLE)]:s+=f'<rect x="{xx}" y="{yy}" width="{w}" height="{h}" rx="18" fill="{c}" opacity=".18" stroke="{c}" stroke-width="3"/>'
 return s
def arrows():
 s=''; rows=[('Fluxo',TEAL,350),('Bidirecional',BLUE,470),('Causal',GRAPH,590),('Inibição',RED,710),('Feedback',GREEN,830)]
 for n,c,y in rows:s+=f'<text x="90" y="{y-25}" font-family="Arial" font-size="24" fill="{GRAPH}">{n}</text><path d="M120 {y} H450" stroke="{c}" stroke-width="10"/><polygon points="450,{y} 420,{y-18} 420,{y+18}" fill="{c}"/>'
 s+=card(560,290,420,700,'Fluxo fisiológico')+card(1040,290,480,700,'Decisão clínica')
 for x,y,t in [(620,470,'Entrada'),(820,470,'Troca'),(620,690,'Resposta'),(820,690,'Saída')]:s+=f'<rect x="{x}" y="{y}" width="130" height="70" rx="14" fill="{PAPER}" stroke="{BLUE}" stroke-width="4"/><text x="{x+65}" y="{y+43}" text-anchor="middle" font-family="Arial" font-size="20" fill="{GRAPH}">{t}</text>'
 return s
def colors():
 s='';rows=[('Estrutura',BLUE),('Fluxo',TEAL),('Oxigenação','#38A8A0'),('Resposta segura',GREEN),('Lesão',RED),('Alerta',AMBER),('Neutralidade','#9BA0A5'),('Interface','#526E9B')]
 for i,(n,c) in enumerate(rows):y=300+i*82;s+=f'<rect x="90" y="{y}" width="80" height="48" rx="10" fill="{c}"/><text x="195" y="{y+32}" font-family="Arial" font-size="24" fill="{GRAPH}">{n}</text>'
 s+=card(470,290,540,690,'Matriz de aplicação')
 for r in range(7):
  for c in range(6):cx=520+c*75;cy=430+r*70;col=rows[r][1];s+=f'<circle cx="{cx}" cy="{cy}" r="15" fill="{col}" opacity="{1 if (r+c)%3==0 else .25}"/>'
 s+=card(1050,290,440,690,'Estados de interface')
 for i,(n,c) in enumerate([('Estável',GREEN),('Monitorização',BLUE),('Atenção',AMBER),('Crítico',RED),('Insuficiente','#9BA0A5')]):y=430+i*105;s+=f'<text x="1090" y="{y}" font-family="Arial" font-size="23" fill="{GRAPH}">{n}</text><rect x="1270" y="{y-28}" width="170" height="32" rx="16" fill="{c}"/>'
 return s
def templates():
 s='';ts=['Abertura','Infográfico','Revisão rápida','Comparação','Algoritmo','Parâmetros','Caso clínico','Tabela','Monitorização']
 for i,t in enumerate(ts):x=80+(i%3)*500;y=290+(i//3)*245;s+=card(x,y,450,210,t)+f'<rect x="{x+30}" y="{y+100}" width="150" height="75" rx="12" fill="{SAND}"/><rect x="{x+205}" y="{y+105}" width="205" height="18" rx="9" fill="{BLUE}" opacity=".25"/><rect x="{x+205}" y="{y+140}" width="165" height="14" rx="7" fill="{MUTED}" opacity=".25"/>'
 return s
RENDER={'201':palette,'202':typography,'203':icons,'204':lambda:body('male'),'205':lambda:body('female'),'206':lambda:body('child'),'207':grid,'208':arrows,'209':colors,'210':templates}
for aid,title,desc in ASSETS:
 d=ROOT/f'HEX-A021-{aid}';d.mkdir(parents=True,exist_ok=True)
 (d/'base-art.svg').write_text(base(title,desc,aid,RENDER[aid]()),encoding='utf-8')
 meta=f'''id: HEX-A021-{aid}
concept: {title}
cycle: A021
layer: advanced
status: generated
prompt: >-
  Prancha avançada Hexápode sobre {title.lower()}, composição editorial 4:3, paleta canônica, diagramas vetoriais e aplicação transversal.
alt: {desc}
overlay:
  title: {title}
  subtitle: {desc}
  labels: [{title.replace(' aplicado','').replace(' aplicada','')}]
consumers: {CONSUMERS}
exports_pending: [base-art.png, thumbnail.webp]
review_gates: {{visual_consistency: pending, clinical_accuracy: pending, didactic_function: pending, accessibility: pending, responsive_legibility: pending, metadata_completeness: complete, no_duplication: pending}}
'''
 (d/'asset.yml').write_text(meta,encoding='utf-8')

m=Path('manifests/assets.yml');text=m.read_text(encoding='utf-8')
text=re.sub(r'next_cycle: A021','next_cycle: A022',text)
text=re.sub(r'completed_assets: 200','completed_assets: 210',text)
idx='  - {id: A021, range: 201-210, theme: Identidade Visual Avançada, status: generated, source_root: assets/advanced/A021}\n'
text=text.replace('cycles:\n',idx+'cycles:\n',1)
asset_lines='\n'.join(f'      - {{id: HEX-A021-{a}, concept: {t}, status: generated, source: assets/advanced/A021/HEX-A021-{a}/base-art.svg, metadata: assets/advanced/A021/HEX-A021-{a}/asset.yml}}' for a,t,_ in ASSETS)
block=f'''cycles:
  A021:
    layer: A
    range: 201-210
    theme: Identidade Visual Avançada
    status: generated
    exports_pending: [base-art.png, thumbnail.webp]
    assets:
{asset_lines}
'''
text=re.sub(r'cycles:\n.*?cycle_generation_rule:',block+'cycle_generation_rule:',text,flags=re.S)
m.write_text(text,encoding='utf-8')
