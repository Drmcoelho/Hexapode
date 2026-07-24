from pathlib import Path
import re

BG='#F7F4EC'; PAPER='#FFFDF8'; GRAPH='#2B2E34'; MUTED='#6A727A'; RULE='#DCD2BE'; BLUE='#1D4E7A'; TEAL='#1696A3'; GREEN='#2E7D69'; TERR='#C45A3C'; RED='#B2473F'; AMBER='#D39A2E'; PURPLE='#76659A'; SAND='#E8E1D1'
ROOT=Path('assets/advanced/A022')
ASSETS=[
('211','Traqueia avançada','Traqueia em corte longitudinal e transversal com anéis em C, músculo traqueal, mucosa e carina.',['Anéis cartilaginosos em C','Músculo traqueal','Mucosa ciliada','Carina'],['Respira','Ventila','ViaAerea','Emergências','Pediatria']),
('212','Brônquios avançados','Assimetria dos brônquios principais, ramificações lobares e implicações para aspiração e intubação seletiva.',['Brônquio principal direito','Brônquio principal esquerdo','Brônquios lobares','Ângulo da carina'],['Respira','Ventila','ViaAerea','Emergências','Pediatria']),
('213','Bronquíolos avançados','Transição de brônquio pequeno para bronquíolo terminal e respiratório, sem cartilagem e com músculo liso.',['Perda de cartilagem','Músculo liso','Bronquíolo terminal','Bronquíolo respiratório'],['Respira','Ventila','Pneumologia','Farmacologia','Pediatria']),
('214','Ácino pulmonar avançado','Organização tridimensional do ácino do bronquíolo respiratório aos ductos e sacos alveolares.',['Bronquíolo respiratório','Ducto alveolar','Saco alveolar','Unidade de troca'],['Respira','Ventila','Pneumologia','Fisiologia','Patologia']),
('215','Alvéolo avançado','Microanatomia alveolar com pneumócitos, surfactante, macrófago e membrana alvéolo-capilar.',['Pneumócito I','Pneumócito II','Surfactante','Macrófago alveolar','Capilar'],['Respira','Ventila','Pneumologia','Fisiologia','Patologia']),
('216','Pleura avançada','Folhetos pleurais, recessos, pressão subatmosférica e acoplamento mecânico pulmão-parede.',['Pleura visceral','Pleura parietal','Espaço pleural','Pressão pleural','Recesso costofrênico'],['Respira','Ventila','Trauma','Emergências','Ultrassom']),
('217','Diafragma avançado','Arquitetura muscular, tendão central, zonas de aposição e excursão respiratória.',['Cúpulas','Tendão central','Zona de aposição','Inspiração','Expiração'],['Respira','Ventila','Fisiologia','Ultrassom','Reabilitação']),
('218','Caixa torácica avançada','Mecânica tridimensional das costelas e esterno nos movimentos de alça de balde e bomba d’água.',['Esterno','Costelas','Alça de balde','Bomba d’água','Eixo vertebral'],['Respira','Ventila','Trauma','Anatomia','Reabilitação']),
('219','Intercostais avançados','Camadas intercostais, orientação de fibras, feixe neurovascular e função respiratória.',['Intercostal externo','Intercostal interno','Intercostal íntimo','Feixe VAN','Espaço seguro'],['Respira','Ventila','Trauma','Procedimentos','Anestesia']),
('220','Árvore traqueobrônquica avançada','Mapa integrado das gerações da via aérea da traqueia aos ácinos, com calibres e zonas funcionais.',['Traqueia','Zona condutora','Bronquíolo terminal','Zona respiratória','Ácinos'],['Respira','Ventila','Pneumologia','Anatomia','Pediatria'])]

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def head(title,desc):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1200" role="img" aria-labelledby="t d"><title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc><rect width="1600" height="1200" fill="{BG}"/><text x="72" y="90" font-family="Arial" font-size="24" font-weight="700" fill="{BLUE}">HEXÁPODE · ANATOMIA RESPIRATÓRIA AVANÇADA</text><text x="72" y="158" font-family="Georgia" font-size="54" font-weight="700" fill="{GRAPH}">{esc(title)}</text><text x="74" y="204" font-family="Arial" font-size="22" fill="{MUTED}">{esc(desc)}</text><line x1="72" y1="236" x2="1528" y2="236" stroke="{RULE}" stroke-width="3"/><rect x="70" y="275" width="970" height="750" rx="28" fill="{PAPER}" stroke="{RULE}" stroke-width="3"/>'
def panel(labels):
 s=f'<rect x="1080" y="300" width="430" height="700" rx="24" fill="{PAPER}" stroke="{RULE}" stroke-width="3"/><text x="1120" y="360" font-family="Arial" font-size="28" font-weight="700" fill="{BLUE}">LEITURA ESTRUTURAL</text>'
 for i,l in enumerate(labels):
  y=430+i*105;c=[TEAL,BLUE,TERR,GREEN,AMBER][i%5]
  s+=f'<circle cx="1135" cy="{y-8}" r="13" fill="{c}"/><text x="1170" y="{y}" font-family="Arial" font-size="23" fill="{GRAPH}">{esc(l)}</text><line x1="1170" y1="{y+20}" x2="1450" y2="{y+20}" stroke="{RULE}" stroke-width="2"/>'
 return s
def foot(a): return f'<text x="72" y="1150" font-family="Arial" font-size="20" fill="{MUTED}">HEX-A022-{a} · Hexápode · camada avançada</text></svg>'

def drawing(i):
 if i==0:
  s=f'<path d="M430 330 C390 500 390 760 430 900" fill="none" stroke="{SAND}" stroke-width="130"/><path d="M430 330 C390 500 390 760 430 900" fill="none" stroke="{TEAL}" stroke-width="92"/><path d="M430 330 C390 500 390 760 430 900" fill="none" stroke="{PAPER}" stroke-width="55"/>'
  for y in range(365,850,65): s+=f'<path d="M340 {y} Q430 {y-28} 520 {y}" fill="none" stroke="{BLUE}" stroke-width="18" stroke-linecap="round"/>'
  return s+f'<path d="M420 895 L300 990 M420 895 L550 990" stroke="{TEAL}" stroke-width="65" stroke-linecap="round"/><circle cx="770" cy="560" r="180" fill="{SAND}" stroke="{BLUE}" stroke-width="5"/><path d="M650 560 A120 120 0 1 1 890 560" fill="none" stroke="{BLUE}" stroke-width="34"/><path d="M650 560 Q770 700 890 560" fill="none" stroke="{TERR}" stroke-width="26"/><circle cx="770" cy="560" r="82" fill="{PAPER}" stroke="{TEAL}" stroke-width="7"/>'
 if i==1:
  return f'<path d="M520 320 V470" stroke="{TEAL}" stroke-width="74" stroke-linecap="round"/><path d="M520 470 L330 730 M520 470 L760 700" stroke="{TEAL}" stroke-width="74" stroke-linecap="round"/><path d="M330 730 L220 900 M330 730 L410 930 M760 700 L680 910 M760 700 L900 850" stroke="{TEAL}" stroke-width="48" stroke-linecap="round"/><path d="M520 470 L760 700" stroke="{RED}" stroke-width="7" stroke-dasharray="16 13"/><path d="M520 470 L330 730" stroke="{BLUE}" stroke-width="7" stroke-dasharray="16 13"/><text x="250" y="1000" font-family="Arial" font-size="24" fill="{MUTED}">Direito mais vertical · esquerdo mais horizontal</text>'
 if i==2:
  s=f'<path d="M170 600 C310 470 430 470 560 600 S820 730 960 590" fill="none" stroke="{TERR}" stroke-width="120" stroke-linecap="round"/><path d="M170 600 C310 470 430 470 560 600 S820 730 960 590" fill="none" stroke="{PAPER}" stroke-width="72" stroke-linecap="round"/><path d="M220 390 H900" stroke="{BLUE}" stroke-width="8"/><polygon points="900,390 860,365 860,415" fill="{BLUE}"/><text x="250" y="350" font-family="Arial" font-size="24" fill="{BLUE}">calibre ↓ · cartilagem desaparece · músculo liso persiste</text>'
  return s
 if i==3:
  s=f'<path d="M260 380 C420 420 500 530 560 660" fill="none" stroke="{TEAL}" stroke-width="52" stroke-linecap="round"/>'
  for x,y,r in [(600,660,95),(730,620,88),(700,760,92),(840,720,86),(560,800,78)]: s+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#F4DDD9" stroke="{TERR}" stroke-width="7"/><circle cx="{x}" cy="{y}" r="{r-28}" fill="{PAPER}" stroke="{TEAL}" stroke-width="4"/>'
  return s+f'<path d="M250 930 C430 850 600 900 940 840" fill="none" stroke="{BLUE}" stroke-width="16"/><path d="M250 970 C430 890 600 940 940 880" fill="none" stroke="{RED}" stroke-width="16"/>'
 if i==4:
  return f'<circle cx="520" cy="630" r="290" fill="#F4DDD9" stroke="{TERR}" stroke-width="8"/><circle cx="520" cy="630" r="210" fill="{PAPER}" stroke="{TEAL}" stroke-width="6"/><path d="M320 460 Q520 370 720 460" fill="none" stroke="{GREEN}" stroke-width="18" stroke-dasharray="20 12"/><circle cx="400" cy="430" r="34" fill="{BLUE}"/><circle cx="640" cy="440" r="34" fill="{BLUE}"/><circle cx="370" cy="770" r="34" fill="{PURPLE}"/><circle cx="690" cy="750" r="34" fill="{PURPLE}"/><path d="M250 930 C420 820 650 820 900 930" fill="none" stroke="{BLUE}" stroke-width="30"/><path d="M250 970 C420 860 650 860 900 970" fill="none" stroke="{RED}" stroke-width="30"/>'
 if i==5:
  return f'<path d="M220 900 Q420 330 800 420 Q970 470 950 870" fill="#D8ECEB" stroke="{TEAL}" stroke-width="8"/><path d="M250 900 Q440 380 790 465 Q910 500 900 860" fill="{PAPER}" stroke="{BLUE}" stroke-width="7"/><path d="M285 900 Q450 430 775 510 Q850 535 845 850" fill="none" stroke="{RED}" stroke-width="14"/><path d="M310 900 Q460 470 760 550 Q800 565 795 840" fill="none" stroke="{GREEN}" stroke-width="8" stroke-dasharray="18 12"/><text x="280" y="980" font-family="Arial" font-size="23" fill="{MUTED}">Acoplamento mecânico pulmão–parede pela pressão pleural</text>'
 if i==6:
  return f'<path d="M190 760 Q520 420 940 760" fill="none" stroke="{TERR}" stroke-width="90"/><path d="M190 760 Q520 500 940 760" fill="none" stroke="{AMBER}" stroke-width="18" stroke-dasharray="18 14"/><ellipse cx="560" cy="675" rx="155" ry="70" fill="{SAND}" stroke="{BLUE}" stroke-width="6"/><path d="M260 350 V560 M840 350 V560" stroke="{TEAL}" stroke-width="12"/><polygon points="260,560 240,520 280,520" fill="{TEAL}"/><polygon points="840,560 820,520 860,520" fill="{TEAL}"/><text x="300" y="980" font-family="Arial" font-size="25" fill="{GRAPH}">Contração → descida das cúpulas → aumento do volume torácico</text>'
 if i==7:
  s=f'<path d="M540 330 V930" stroke="{GRAPH}" stroke-width="28"/>'
  for j,y in enumerate(range(390,900,70)): s+=f'<path d="M{220+j*8} {y} Q540 {y+80} {870-j*5} {y}" fill="none" stroke="{SAND}" stroke-width="30"/><path d="M{220+j*8} {y} Q540 {y+80} {870-j*5} {y}" fill="none" stroke="{BLUE}" stroke-width="5"/>'
  return s+f'<path d="M230 720 H120 M850 720 H980" stroke="{TEAL}" stroke-width="10"/><polygon points="120,720 155,700 155,740" fill="{TEAL}"/><polygon points="980,720 945,700 945,740" fill="{TEAL}"/>'
 if i==8:
  return f'<path d="M180 400 H950 M180 640 H950 M180 880 H950" stroke="{SAND}" stroke-width="42"/><path d="M180 450 L950 760 M180 590 L950 900" stroke="{TERR}" stroke-width="30" opacity=".8"/><path d="M180 610 L950 300 M180 850 L950 540" stroke="{RED}" stroke-width="25" opacity=".65"/><path d="M200 665 H930" stroke="{BLUE}" stroke-width="14"/><circle cx="420" cy="665" r="18" fill="{AMBER}"/><circle cx="510" cy="665" r="18" fill="{RED}"/><circle cx="600" cy="665" r="18" fill="{BLUE}"/><text x="245" y="1000" font-family="Arial" font-size="22" fill="{MUTED}">Feixe VAN no sulco costal · acesso junto ao bordo superior da costela inferior</text>'
 s=f'<path d="M500 310 V460" stroke="{TEAL}" stroke-width="54"/><path d="M500 460 C360 540 300 620 250 930 M500 460 C640 540 720 630 820 930" fill="none" stroke="{TEAL}" stroke-width="46" stroke-linecap="round"/>'
 for x,y,q in [(390,570,-1),(610,570,1),(330,690,-1),(680,700,1),(270,820,-1),(760,820,1)]: s+=f'<path d="M{x} {y} l{q*110} 90 M{x} {y} l{q*60} 125" stroke="{BLUE if y<700 else GREEN}" stroke-width="{26 if y<700 else 16}" stroke-linecap="round"/>'
 for x,y in [(135,950),(230,1000),(820,990),(930,940)]: s+=f'<circle cx="{x}" cy="{y}" r="34" fill="#F4DDD9" stroke="{TERR}" stroke-width="5"/>'
 return s

for i,(aid,title,desc,labels,consumers) in enumerate(ASSETS):
 d=ROOT/f'HEX-A022-{aid}';d.mkdir(parents=True,exist_ok=True)
 svg=head(title,desc)+drawing(i)+panel(labels)+foot(aid)
 (d/'base-art.svg').write_text(svg,encoding='utf-8')
 meta=f'''id: HEX-A022-{aid}\nconcept: {title}\ncycle: A022\nlayer: advanced\nstatus: generated\nprompt: >-\n  Prancha avançada Hexápode sobre {title.lower()}, expandindo o conceito canônico com microanatomia, relações funcionais e aplicação transversal.\nalt: {desc}\noverlay:\n  embedded_in: base-art.svg\n  title: {title}\n  labels: [{', '.join(labels)}]\nconsumers: [{', '.join(consumers)}]\ncanonical_source: assets/canonical/G002/HEX-G002-{int(aid)-200:03d}\nexports_pending: [base-art.png, thumbnail.webp]\nreview_gates: {{visual_consistency: pending, clinical_accuracy: pending, didactic_function: pending, accessibility: pending, responsive_legibility: pending, metadata_completeness: complete, no_duplication: pending}}\n'''
 (d/'asset.yml').write_text(meta,encoding='utf-8')

m=Path('manifests/assets.yml'); text=m.read_text(encoding='utf-8')
text=text.replace('  next_cycle: A022','  next_cycle: A023').replace('  completed_assets: 210','  completed_assets: 220')
line='  - {id: A022, range: 211-220, theme: Anatomia Respiratória I Avançada, status: generated, source_root: assets/advanced/A022}\n'
if 'id: A022' not in text: text=text.replace('  - {id: A021, range: 201-210, theme: Identidade Visual Avançada, status: generated, source_root: assets/advanced/A021}\n','  - {id: A021, range: 201-210, theme: Identidade Visual Avançada, status: generated, source_root: assets/advanced/A021}\n'+line)
block='cycles:\n  A022:\n    layer: A\n    range: 211-220\n    theme: Anatomia Respiratória I Avançada\n    status: generated\n    exports_pending: [base-art.png, thumbnail.webp]\n    assets:\n'
for aid,title,*_ in ASSETS: block+=f'      - {{id: HEX-A022-{aid}, concept: {title}, status: generated, source: assets/advanced/A022/HEX-A022-{aid}/base-art.svg, metadata: assets/advanced/A022/HEX-A022-{aid}/asset.yml}}\n'
text=re.sub(r'cycles:\n.*?(?=cycle_generation_rule:)',block,text,flags=re.S)
m.write_text(text,encoding='utf-8')
