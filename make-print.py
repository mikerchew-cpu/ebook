#!/usr/bin/env python3
"""Create print version by extracting slides via data-animate."""

import re

with open('/Users/mikerchew/Desktop/github/coming-storm-ppt/index.html') as f:
    html = f.read()

d = html.find('<div id="deck">')
n = html.find('<div id="nav">')
deck_content = html[d+len('<div id="deck">'):n]

# Extract real slides (those with data-animate)
slides = re.findall(
    r'<section class="slide[^"]*"[^>]*data-animate="[^"]*"[^>]*>.*?</section>',
    deck_content, re.DOTALL
)

print(f'Extracted {len(slides)} slides')

# Build the fixed-pixel CSS
css_base = """
@page { size:1920px 1080px; margin:0; }
* { box-sizing:border-box; margin:0; padding:0; }
:root {
  --paper:#fafaf8; --ink:#0a0a0a; --grey-1:#f0f0ee; --grey-2:#d4d4d2;
  --grey-3:#737373; --accent:#002FA7; --accent-on:#ffffff;
  --text-primary:#0a0a0a; --text-secondary:#525252; --text-helper:#737373;
  --border-subtle:#e0e0e0;
  --sans:Inter,Helvetica Neue,Helvetica,Arial,system-ui,sans-serif;
  --sans-zh:"PingFang SC","Noto Sans SC","Microsoft YaHei UI",sans-serif;
  --mono:"JetBrains Mono","SF Mono","Consolas",monospace;
}
body { background:#fff; margin:0 auto; font-family:var(--sans),var(--sans-zh); }
.slide{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;break-after:page;
  background:var(--paper);color:var(--ink);padding:60px 96px 75px 96px;
  display:flex;flex-direction:column;font-size:20px;line-height:1.5}
.slide.accent{background:#002FA7;color:#fff}
.slide.dark{background:#0a0a0a;color:#fff}
.slide.grey{background:#f0f0ee}
.slide.split .canvas-card{padding:0;flex-direction:row;display:flex;width:100%;height:100%}
.split-half{display:grid;grid-template-columns:1fr 1fr;width:100%;height:100%}
.split-half>.half{padding:60px 65px 48px;display:flex;flex-direction:column}
.split-half>.half.b-accent{background:#002FA7;color:#fff}
.split-half>.half.b-ink{background:#0a0a0a;color:#fff}
.canvas-card{width:100%;height:100%;display:flex;flex-direction:column;position:relative}
canvas{display:none!important}
.chrome-min{display:flex;justify-content:space-between;font-family:var(--mono);font-size:14px;
  font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--text-helper);margin-bottom:40px;flex:0 0 auto}
.slide.accent .chrome-min,.slide.dark .chrome-min{color:rgba(255,255,255,.62)}
.t-meta{font-family:var(--mono);font-size:14px;font-weight:500;letter-spacing:.14em;
  text-transform:uppercase;color:var(--text-helper);line-height:1.45}
.slide.accent .t-meta{color:rgba(255,255,255,.7)}
.t-cat{font-family:var(--mono);font-size:14px;font-weight:600;letter-spacing:.15em;
  text-transform:uppercase;color:var(--text-helper);line-height:1.3}
.t-cat.accent{color:#002FA7}
.lead{font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:28px;line-height:1.4;
  letter-spacing:-.005em;opacity:.86}
.slide.accent .lead{color:rgba(255,255,255,.86)}
.h-xl-zh{font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:60px;line-height:1.05;letter-spacing:-.025em}
.h-statement{font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:80px;line-height:1.05;letter-spacing:-.015em;text-align:center}
.duo-compare{display:grid;grid-template-columns:1fr 1px 1fr;gap:0 50px;flex:1;align-items:stretch}
.duo-compare .vrule{background:#d4d4d2;width:1px;align-self:stretch}
.duo-compare .col{display:flex;flex-direction:column;gap:14px;padding:0 8px}
.duo-compare .col-tag{font-family:var(--mono);font-size:14px;letter-spacing:.16em;
  text-transform:uppercase;color:#737373;display:flex;align-items:center;gap:10px}
.duo-compare .col-tag .num{font-weight:600;color:#0a0a0a;border:1px solid #0a0a0a;padding:.2em .6em}
.duo-compare .col-ttl{font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:40px;line-height:1;letter-spacing:-.03em}
.duo-compare .col-desc{font-family:var(--sans),var(--sans-zh);font-size:18px;line-height:1.55;opacity:.78}
.four-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.fc-col{padding:22px 24px;display:flex;flex-direction:column;gap:12px;background:#f5f5f4}
.fc-col.card-accent{background:#002FA7;color:#fff}
.fc-col.card-accent .t-meta{color:rgba(255,255,255,.7)}
.fc-col.card-fill{background:#f5f5f4}
.stacked-ledger{display:flex;flex-direction:column;gap:0}
.ledger-row{display:grid;grid-template-columns:auto 1fr auto;gap:30px;align-items:center;padding:18px 0;border-bottom:1px solid #e0e0e0}
.ledger-num{font-family:var(--sans);font-weight:200;font-size:72px;line-height:.9;letter-spacing:-.04em;font-feature-settings:'tnum';color:var(--accent)}
.ledger-label{font-weight:400;font-size:20px;line-height:1.5}
.why-now-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.why-col{display:flex;flex-direction:column;gap:12px;padding:14px 18px}
.why-num-bottom{font-family:var(--sans);font-weight:200;font-size:72px;line-height:.9;letter-spacing:-.04em;margin-top:auto}
.timeline-h{position:relative;flex:1;display:flex;align-items:center}
.tl-h-axis{position:absolute;left:5%;right:5%;top:50%;height:1px;background:repeating-linear-gradient(to right,currentColor 0 4px,transparent 4px 8px);opacity:.35}
.tl-row{position:relative;width:100%;display:grid;grid-template-columns:repeat(4,1fr);align-items:center}
.th-node{position:relative;display:flex;justify-content:center}
.th-node .dot{width:8px;height:8px;border-radius:50%;z-index:1;position:relative;background:#0a0a0a}
.th-node.accent .dot{background:#002FA7}
.th-node .label{position:absolute;left:50%;transform:translateX(-50%);bottom:calc(50% + 20px);width:280px;text-align:center;display:flex;flex-direction:column;gap:4px}
.th-node .name{font-family:var(--sans);font-size:18px;font-weight:400}
.th-node .desc{font-family:var(--sans),var(--sans-zh);font-size:15px;color:#525252}
.th-node .yr{font-family:var(--mono);font-size:14px;font-weight:500;color:#737373}
.card-fill{background:#f5f5f4;padding:22px 26px;display:flex;flex-direction:column;gap:12px}
.card-accent{background:#002FA7;color:#fff;padding:22px 26px;display:flex;flex-direction:column;gap:12px}
.grid-12{display:grid;grid-template-columns:repeat(12,1fr);gap:20px}
.span-4{grid-column:span 4}
.span-6{grid-column:span 6}
.span-8{grid-column:span 8}
.span-12{grid-column:span 12}
.t-body-sm{font-family:var(--sans),var(--sans-zh);font-size:17px;font-weight:400;color:#525252;line-height:1.55}
[data-lucide]{width:20px;height:20px;display:inline-block;flex-shrink:0}
.rule{width:100%;height:1px;background:currentColor;opacity:.18;margin:0}
.four-cards .t-meta{font-family:var(--mono);font-size:13px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:#737373;margin-bottom:6px}
h4{font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:22px;line-height:1.15;letter-spacing:-.01em}
i{font-style:normal}
p.t-body-sm{font-size:17px;line-height:1.55}
"""

head = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1920">
<title>The Coming Storm · Geopolitical Briefing (PDF)</title>
<style>{css_base}</style>
</head>
<body>
'''

with open('/Users/mikerchew/Desktop/github/coming-storm-ppt/print.html', 'w') as f:
    f.write(head)
    for s in slides:
        f.write(s + '\n\n')
    f.write('</body>\n</html>')

print(f'Written: print.html with {len(slides)} slides')
