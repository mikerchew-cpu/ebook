#!/usr/bin/env python3
"""Generate 60-slide Coming Storm PPT — Swiss Style, IKB theme."""

import re, os

SKILL_ROOT = os.path.expanduser("~/Desktop/github/.agents/skills/guizang-ppt-skill")
TEMPLATE = os.path.join(SKILL_ROOT, "assets/template-swiss.html")
OUTPUT = os.path.expanduser("~/Desktop/github/coming-storm-ppt/index.html")

# Read template
with open(TEMPLATE) as f:
    html = f.read()

# Find markers for replacement
aside_pat = re.compile(r'<title>.*?</title>')
title_html = '<title>The Coming Storm · Power, Conflict, and Lessons from History · Geopolitical Briefing</title>'
html = aside_pat.sub(title_html, html)

# Build all 60 slides
slides = []

def S(cls, animate, inner):
    return f'<section class="slide {cls}" data-animate="{animate}">\n{inner}\n</section>'

def cover():
    return S("accent", "hero", '''<div class="canvas-card">
    <canvas class="ascii-bg" aria-hidden="true"></canvas>
    <div class="chrome-min"><div class="l">The Coming Storm · Geopolitical Briefing</div><div class="r">IKB · 26.06 · 01 / 60</div></div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:2.6vh">
      <div data-anim="kicker" class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em">POWER · CONFLICT · WARNINGS FROM HISTORY</div>
      <h1 data-anim="title" style="align-self:center;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(11.6vw,19vh);line-height:.94;letter-spacing:-.025em;color:#fff">The Coming Storm<br><span style="font-style:italic;font-weight:300">Power, Conflict, and Lessons from History</span></h1>
      <div data-anim="bottom" style="display:grid;grid-template-rows:auto auto;gap:1.6vh;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh">
        <div data-anim="lead" class="lead" style="max-width:52ch;color:rgba(255,255,255,.86)">Moving Beyond Superpower Predictability to Multi-Polar Volatility — A Structural Analysis Based on Odd Arne Westad (2026)</div>
        <div style="display:flex;justify-content:space-between;align-items:end">
          <div class="t-meta" style="color:rgba(255,255,255,.6)">Briefing Document · June 2026</div>
          <div class="t-meta" style="color:rgba(255,255,255,.6)">→ swipe / arrow keys</div>
        </div>
      </div>
    </div>
  </div>''')

def duo(cls, tag, title, left_tag, left_ttl, left_desc, right_tag, right_ttl, right_desc, num):
    return S(cls, "duo-mirror", f'''<div class="canvas-card">
    <div class="chrome-min"><div class="l">{tag}</div><div class="r">{num} / 60</div></div>
    <div style="flex:0 0 auto;display:flex;flex-direction:column;gap:1.4vh;margin-bottom:1.4vh">
      <div class="t-meta">{" · ".join(tag.split(" · ")[-1:])}</div>
      <h2 class="h-xl-zh" style="font-size:min(5vw,9vh)">{title}</h2>
    </div>
    <div class="duo-compare" style="margin-top:2vh">
      <div class="col">
        <div class="col-tag"><span class="num">01</span>{left_tag}</div>
        <div class="col-ttl" style="font-size:min(2.4vw,4.6vh)">{left_ttl}</div>
        <div class="col-desc">{left_desc}</div>
      </div>
      <span class="vrule"></span>
      <div class="col">
        <div class="col-tag"><span class="num">02</span>{right_tag}</div>
        <div class="col-ttl" style="font-size:min(2.4vw,4.6vh)">{right_ttl}</div>
        <div class="col-desc">{right_desc}</div>
      </div>
    </div>
  </div>''')

def ledger(cls, tag, title, rows, num):
    rows_html = ""
    for label, desc, icon in rows:
        rows_html += f'''<div class="ledger-row" style="display:grid;grid-template-columns:auto 1fr auto;gap:2vw;align-items:center;padding:2vh 0;border-bottom:1px solid var(--border-subtle)">
      <div class="ledger-num" style="font-family:var(--sans);font-weight:200;font-size:min(5.2vw,9vh);line-height:.9;letter-spacing:-.04em;color:var(--{"accent" if "accent" in label else "text-primary"});font-feature-settings:'tnum'">{label.replace("·accent·", "")}</div>
      <div class="ledger-label" style="font-weight:400;font-size:max(15px,1.1vw);line-height:1.5">{desc}</div>
      <i data-lucide="{icon}" style="width:1.8vw;height:1.8vw;stroke-width:1.4;opacity:.6"></i>
    </div>'''
    return S(cls, "stacked-ledger", f'''<div class="canvas-card">
    <div class="chrome-min"><div class="l">{tag}</div><div class="r">{num} / 60</div></div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:2.6vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:.8vh">
        <div class="t-meta">{tag.split(" · ")[-1]}</div>
        <h2 class="h-xl-zh" style="font-size:min(4.8vw,8.6vh)">{title}</h2>
      </div>
      <div data-anim="ledger" class="stacked-ledger" style="display:flex;flex-direction:column;gap:0;flex:1">{rows_html}</div>
    </div>
  </div>''')

def four_cards(cls, tag, title, cards, num):
    cards_html = ""
    for i, (ttl, desc) in enumerate(cards):
        accent = ' card-accent' if i == len(cards)-1 else ' card-fill'
        cards_html += f'''<div class="fc-col{accent}" style="padding:2.4vh 1.6vw;display:flex;flex-direction:column;gap:1.2vh">
      <div class="t-meta" style="color:var(--{"accent-on" if i == len(cards)-1 else "text-helper"});letter-spacing:.12em;margin-bottom:.6vh">— {["ONE","TWO","THREE","FOUR","FIVE","SIX"][i]}</div>
      <h4 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(17px,1.6vw);line-height:1.15;letter-spacing:-.01em">{ttl}</h4>
      <p class="t-body-sm">{desc}</p>
    </div>'''
    return S(cls, "four-cards", f'''<div class="canvas-card">
    <div class="chrome-min"><div class="l">{tag}</div><div class="r">{num} / 60</div></div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:2.6vh">
      <div data-anim="line">
        <div style="width:80px;height:2px;background:var(--accent);margin-bottom:2.4vh"></div>
        <div class="t-meta">{tag.split(" · ")[-1]}</div>
        <h2 class="h-xl-zh" style="font-size:min(4.2vw,7.6vh)">{title}</h2>
      </div>
      <div data-anim="up" class="four-cards" style="display:grid;grid-template-columns:repeat({len(cards)},1fr);gap:1.6vw;flex:1;align-content:start">{cards_html}</div>
    </div>
  </div>''')

def statement(cls, tag, title, body, num):
    return S(cls, "statement-rise", f'''<div class="canvas-card">
    <div class="chrome-min"><div class="l">{tag}</div><div class="r">{num} / 60</div></div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:2vh;text-align:center">
      <div class="t-meta" style="color:var(--text-helper);letter-spacing:.22em">{tag.split(" · ")[-1]}</div>
      <h1 class="h-statement" style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(7.4vw,13vh);line-height:1.05;letter-spacing:-.03em;max-width:90%">{title}</h1>
      <p class="lead" style="max-width:64ch;margin-top:1.6vh">{body}</p>
    </div>
  </div>''')

def whynow(cls, tag, title, cols, num):
    cols_html = ""
    for i, (ctitle, cdesc, cnum) in enumerate(cols):
        accent = "color:var(--accent)" if i == len(cols)-1 else ""
        cols_html += f'''<div class="why-col" style="display:flex;flex-direction:column;gap:1.2vh;padding:1.6vh 1.2vw">
      <div class="t-cat" style="color:var(--accent)">{"ARGUMENT " + str(i+1)}</div>
      <h4 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(17px,1.5vw);line-height:1.2">{ctitle}</h4>
      <p class="t-body-sm" style="flex:1">{cdesc}</p>
      <div class="why-num-bottom" style="font-family:var(--sans);font-weight:200;font-size:min(6.4vw,11vh);line-height:.9;letter-spacing:-.04em;margin-top:auto;{accent}">{cnum}</div>
    </div>'''
    return S(cls, "why-now", f'''<div class="canvas-card">
    <div class="chrome-min"><div class="l">{tag}</div><div class="r">{num} / 60</div></div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:2.6vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:.8vh">
        <div class="t-meta">{tag.split(" · ")[-1]}</div>
        <h2 class="h-xl-zh" style="font-size:min(4.6vw,8.2vh)">{title}</h2>
      </div>
      <div data-anim="up" class="why-now-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.6vw;flex:1;align-content:start">{cols_html}</div>
    </div>
  </div>''')

def closing():
    return S("split", "split-statement", '''<div class="canvas-card">
    <div class="split-half">
      <div class="half b-accent" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between;position:relative;overflow:hidden">
        <canvas class="ascii-bg" aria-hidden="true"></canvas>
        <div class="chrome-min" style="margin-bottom:0;position:relative;z-index:1"><div class="l">60 / 60</div><div class="r">CLOSING</div></div>
        <div data-anim="manifesto" style="display:flex;flex-direction:column;gap:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em;margin-bottom:1.6vh">MANIFESTO</div>
          <h2 style="font-family:var(--sans),var(--sans-zh);font-size:min(7.4vw,13vh);line-height:.94;letter-spacing:-.025em;font-weight:200;color:#fff">Heed the warnings.<br/>Choose <span style="font-style:italic;font-weight:300">diplomacy</span>.</h2>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(14px,1vw);line-height:1.6;color:rgba(255,255,255,.82);font-weight:400;max-width:36ch;margin-top:1.4vh">De-escalation over complacency — the central lesson of 1914 for our multi-polar era.</div>
        </div>
        <div data-anim="signature" style="display:flex;justify-content:space-between;align-items:end;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.62)">Based on Odd Arne Westad · The Coming Storm (2026)</div>
          <div class="t-meta" style="color:rgba(255,255,255,.62)">26.06</div>
        </div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div class="chrome-min"><div class="l">TAKEAWAYS</div><div class="r">03 RULES</div></div>
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:0">
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9;color:var(--text-primary)">01</div>
            <div><h3 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(18px,1.8vw);line-height:1.2;letter-spacing:-.015em;color:var(--text-primary);margin-bottom:1vh">Restore Crisis Communication</h3><p style="font-family:var(--sans),var(--sans-zh);font-size:max(16px,.94vw);line-height:1.6;color:var(--text-secondary);font-weight:400">Establish reliable hotlines and military-to-military dialogues across all major flashpoints.</p></div>
          </div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9;color:var(--text-primary)">02</div>
            <div><h3 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(18px,1.8vw);line-height:1.2;letter-spacing:-.015em;color:var(--text-primary);margin-bottom:1vh">Modernize Global Governance</h3><p style="font-family:var(--sans),var(--sans-zh);font-size:max(16px,.94vw);line-height:1.6;color:var(--text-secondary);font-weight:400">Adapt multilateral institutions to reflect today's multi-polar balance of power.</p></div>
          </div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.6vh 0;border-top:1px solid var(--border-subtle);border-bottom:2px solid var(--accent)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.4vw,7.8vh);line-height:.9;color:var(--accent)">03</div>
            <div><h3 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(18px,1.8vw);line-height:1.2;letter-spacing:-.015em;color:var(--accent);margin-bottom:1vh">Practice Active Peacecraft</h3><p style="font-family:var(--sans),var(--sans-zh);font-size:max(16px,.94vw);line-height:1.6;color:var(--text-secondary);font-weight:400">Peace is not a default state — it requires continuous diplomatic effort, institutional investment, and strategic empathy.</p></div>
          </div>
        </div>
        <div data-anim="foot" class="t-meta" style="color:var(--text-helper);text-align:right">→ END OF BRIEFING</div>
      </div>
    </div>
  </div>''')

# Generate slides
slides.append(cover())

# Slides 2-20: Part I
slides.append(duo("light", "Part I · The Multi-Polar Landscape", "The Eras of Strategic Predictability",
  "BIPOLAR STABILITY", "1945–1991",
  "The Cold War system featured high structural predictability. The United States and the Soviet Union operated within well-understood strategic boundaries, maintaining direct communication lines and a shared fear of nuclear escalation through devastating proxy conflicts in the Global South.",
  "MULTI-POLAR REALITY", "2016–Present",
  "The current system features a crowded field of heavily armed, assertive powers: the United States, China, Russia, India, the European Union, Turkey, Japan, and Brazil. Lacking centralized guardrails, the global system has grown highly fragile and volatile.",
  "02"))

slides.append(four_cards("light", "Part I · China's Strategic Calculus", "The Drive for Primacy", [
    ("The Power Shift", "Driven by decades of historic economic growth since the 1978 opening, Beijing has transitioned from an integrated participant in global supply chains into an assertive revisionist power seeking regional dominance."),
    ("Strategic Objectives", "Core goals center on securing absolute sovereignty over its immediate maritime periphery, transforming the PLA into a world-class force, and building parallel financial and trade structures to insulate itself from Western pressure."),
    ("Systemic Friction", "This rapid accumulation of power creates deep security anxieties among neighboring states and directly challenges long-standing American naval and strategic dominance across the Indo-Pacific."),
    ("Revisionist Dynamic", "This sets up a classic revisionist-versus-status-quo struggle that shapes modern international relations, echoing the structural tensions that preceded past great power conflicts.")
], "03"))

slides.append(ledger("light", "Part I · Data: China's Power Accumulation", "Measuring the Chinese Vector", [
    ("30%", "Global manufacturing output share — unmatched industrial surge capacity far outpacing Western economies", "factory"),
    ("370+", "PLAN battleforce ships — world's largest navy by hull count (US Navy: ~290)", "ship"),
    ("120+", "Countries where China is the leading trading partner via Belt and Road investments", "globe")
], "04"))

slides.append(statement("light", "Part I · The United States: The Status Quo Power in Transition", "The American Position: Managing Decline and Primacy",
    "The United States remains the world's preeminent military and financial power, but faces a dual challenge: managing deep polarization at home while sustaining an expansive global alliance network abroad. Washington must simultaneously deter Russia in Europe, counter China in the Indo-Pacific, and maintain stability across the Middle East. Domestic populist shifts have introduced unpredictability into American foreign policy, creating anxieties among allies regarding the long-term reliability of US security guarantees.",
    "05"))

slides.append(ledger("light", "Part I · Data: US Defense and Fiscal Realities", "Quantifying American Global Reach", [
    ("$900B+", "Annual defense budget supporting a global network of over 750 military bases across 80 nations", "shield"),
    ("32", "NATO member states integrating US-led security policy across Europe and the North Atlantic", "users"),
    ("120%", "National debt-to-GDP ratio — rising fiscal pressure limits long-term defense spending flexibility", "trending-down")
], "06"))

slides.append(statement("light", "Part I · Russia's Revisionism: Asymmetric Disruptions", "Russia's Strategy of Controlled Breakdown",
    "Driven by deep historical grievances regarding the collapse of the Soviet Union and NATO's eastward expansion, Moscow pursues an aggressive foreign policy to re-establish an exclusive sphere of influence across Eurasia. Recognizing its economic and conventional military limitations, Russia relies on asymmetric tools: cyber warfare, election interference, gray-zone provocations, and persistent nuclear signaling. Blocked from Western markets, Moscow has decisively shifted toward Asia and deepened its comprehensive partnership with China.",
    "07"))

slides.append(whynow("light", "Part I · Data: Russia's War Economy", "The Material Reality of Russian Power", [
    ("Total War Mobilization", "Russia dedicates roughly 6-7% of GDP to defense, supporting an annual munitions output of over 3 million artillery shells — outpacing combined Western manufacturing.", "6–7%"),
    ("Nuclear Arsenal", "Moscow maintains the world's largest active nuclear stockpile with approximately 5,580 warheads, serving as the ultimate insurance policy for aggressive regional actions.", "5,580"),
    ("Sanctions Resilience", "Over 80% of Russian crude oil now flows to China and India via alternative shipping networks, ensuring steady revenue for prolonged military operations.", "80%")
], "08"))

slides.append(statement("light", "Part I · India's Strategic Autonomy", "The Swing State of the Century",
    "Rejecting formal military alliances, New Delhi practices multi-alignment — deepening security ties with the West to counter China while maintaining vital defense and energy relationships with Russia. India faces an assertive China along its disputed northern border, driving expanded defense cooperation through the Quad. As a natural bridge between Western economies and the developing world, India uses its growing economic weight to reshape multilateral organizations and champion a more balanced multi-polar order.",
    "09"))

slides.append(ledger("light", "Part I · Data: India's Rise", "The Statistical Footprint", [
    ("1.43B", "Population — world's most populous nation, with over 40% under the age of 25 providing a powerful demographic dividend", "users"),
    ("6–7%", "Annual GDP growth — world's fastest-growing major economy, on track to become third-largest before the decade ends", "trending-up"),
    ("$83B", "Third-largest military budget globally, focused on naval modernization and high-altitude border defense", "shield")
], "10"))

slides.append(statement("light", "Part I · Turkey: The Independent Pivot", "Neo-Ottoman Strategic Autonomy",
    "Under increasingly nationalist leadership, Turkey has shifted from a predictable Western flank state into an independent, assertive regional actor projecting power across the Middle East, North Africa, and the Black Sea. While remaining a critical NATO member, Ankara frequently challenges Western policies — buying Russian defense systems, launching independent operations in Syria, and maintaining pragmatic ties with Moscow. Turkey leverages its geography as a strategic intermediary.",
    "11"))

slides.append(ledger("light", "Part I · Data: Turkey's Footprint", "Quantifying Regional Influence", [
    ("2nd", "Largest standing military in NATO after the US — over 350,000 active-duty personnel", "users"),
    ("30+", "Countries operating the Bayraktar TB2 drone — reshaping conflicts in Nagorno-Karabakh, Libya, and Ukraine", "drone"),
    ("Bosphorus", "Sovereign control over the straits, regulating naval traffic into the Black Sea — critical strategic leverage", "anchor")
], "12"))

slides.append(duo("light", "Part I · Japan: Ending Pacifism", "Confronting Vulnerability",
  "THE END OF ISOLATION", "Post-War Pacifism (1947–2022)",
  "Japan maintained a strictly defensive posture under Article 9 of its constitution, limiting defense spending to 1% of GDP and avoiding offensive capabilities or foreign military deployments beyond UN peacekeeping.",
  "THE DEFENSE SHIFT", "Active Deterrence (2022–Present)",
  "Facing a rapidly modernizing Chinese military, routine North Korean missile tests, and a revanchist Russia, Tokyo is carrying out its most radical security policy shift since WWII — moving to 2% GDP defense spending, acquiring counterstrike capabilities, and deepening alliance integration.",
  "13"))

slides.append(howmany := """<section class="slide light" data-animate="timeline-walk">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">Part I · Japan's Historic Re-Armament</div><div class="r">14 / 60</div></div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:2.6vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:.8vh">
        <div class="t-meta">QUANTIFYING THE SHIFT</div>
        <h2 class="h-xl-zh" style="font-size:min(4.4vw,8vh)">The Numerical Scale of Japan's Defense Shift</h2>
      </div>
      <div class="timeline-h" data-anim="tl" style="flex:1">
        <span class="tl-h-axis" style="position:absolute;left:5%;right:5%;top:50%;height:1px;background:repeating-linear-gradient(to right,currentColor 0 4px,transparent 4px 8px);opacity:.35"></span>
        <div class="tl-row" style="position:relative;width:100%;display:grid;grid-template-columns:repeat(3,1fr);align-items:center">
          <div class="th-node up" style="position:relative;display:flex;justify-content:center">
            <span class="dot" style="width:8px;height:8px;border-radius:50%;background:var(--accent);z-index:1;position:relative"></span>
            <div class="label" style="position:absolute;left:50%;transform:translateX(-50%);bottom:calc(50% + 22px);width:16vw;text-align:center;display:flex;flex-direction:column;gap:.4vh">
              <span class="yr" style="font-family:var(--mono);font-size:max(14px,.78vw);letter-spacing:.05em;color:var(--text-helper);font-weight:500">2% GDP</span>
              <span class="name" style="font-family:var(--sans);font-size:max(16px,1.05vw);font-weight:400;color:var(--text-primary)">Defense Target</span>
              <span class="desc" style="font-family:var(--sans),var(--sans-zh);font-size:max(14px,.84vw);color:var(--text-secondary)">World's 3rd largest defense budget</span>
            </div>
          </div>
          <div class="th-node up" style="position:relative;display:flex;justify-content:center">
            <span class="dot" style="width:8px;height:8px;border-radius:50%;background:var(--accent);z-index:1;position:relative"></span>
            <div class="label" style="position:absolute;left:50%;transform:translateX(-50%);bottom:calc(50% + 22px);width:16vw;text-align:center;display:flex;flex-direction:column;gap:.4vh">
              <span class="yr" style="font-family:var(--mono);font-size:max(14px,.78vw);letter-spacing:.05em;color:var(--accent);font-weight:500">400</span>
              <span class="name" style="font-family:var(--sans);font-size:max(16px,1.05vw);font-weight:400;color:var(--text-primary)">Tomahawk Missiles</span>
              <span class="desc" style="font-family:var(--sans),var(--sans-zh);font-size:max(14px,.84vw);color:var(--text-secondary)">Plus extended-range Type-12 (1,000km+)</span>
            </div>
          </div>
          <div class="th-node up" style="position:relative;display:flex;justify-content:center">
            <span class="dot" style="width:8px;height:8px;border-radius:50%;background:var(--accent);z-index:1;position:relative"></span>
            <div class="label" style="position:absolute;left:50%;transform:translateX(-50%);bottom:calc(50% + 22px);width:16vw;text-align:center;display:flex;flex-direction:column;gap:.4vh">
              <span class="yr" style="font-family:var(--mono);font-size:max(14px,.78vw);letter-spacing:.05em;color:var(--accent);font-weight:500">1945→</span>
              <span class="name" style="font-family:var(--sans);font-size:max(16px,1.05vw);font-weight:400;color:var(--text-primary)">Carrier Aviation</span>
              <span class="desc" style="font-family:var(--sans),var(--sans-zh);font-size:max(14px,.84vw);color:var(--text-secondary)">Izumo-class refit for F-35B operations</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>""")
slides.append(howmany)

slides.append(statement("light", "Part I · The European Union: Fragmented Power", "An Economic Giant Seeking Strategic Voice",
    "Russia's full-scale invasion of Ukraine shocked the EU out of post-Cold War security assumptions, forcing a painful reassessment of dependence on Russian energy and American security guarantees. Europe remains structurally divided on strategic autonomy — frontline states favor keeping NATO as primary defense. The EU faces serious headwinds from high energy costs, falling industrial competitiveness, and deep economic exposure to the Chinese market.",
    "15"))

slides.append(ledger("light", "Part I · Data: EU Power Profile", "Assessing the European Matrix", [
    ("$18T", "Combined EU GDP — world-class regulatory and economic influence lacking unified military power", "landmark"),
    ("$300B+", "Combined annual defense spending, driven by sharp increases in Germany, Poland, and Baltic states", "trending-up"),
    ("90%+", "EU dependence on China for critical rare earth elements — major vulnerability for green energy transition", "alert-triangle")
], "16"))

slides.append(statement("light", "Part I · Brazil: The Global South's Pragmatic Voice", "Non-Alignment and Resource Wealth",
    "Brazil follows a long-standing diplomatic tradition of non-intervention and universal engagement, explicitly refusing to join Western sanctions against Russia or take sides in the US-China rivalry. As a founding BRICS member, Brazil promotes multi-polar financial architecture. Its massive agricultural and mineral wealth — the world's largest exporter of soy, beef, and poultry — guarantees independence from Great Power pressure during international crises.",
    "17"))

slides.append(ledger("light", "Part I · Data: Brazil's Resource Weight", "The Material Drivers of Brazilian Diplomacy", [
    ("#1", "World's largest exporter of soy, beef, and poultry — vital to global food security", "wheat"),
    ("3.5M", "Barrels of oil per day from offshore pre-salt fields — strategic energy independence", "droplet"),
    ("$100B+", "Annual exports to China — more than 3× the volume shipped to the United States", "globe")
], "18"))

slides.append(duo("light", "Part I · Case Study: De-Dollarization", "Financial Architecture Under Pressure",
  "THE WEAPONIZATION OF FINANCE", "Western Sanctions Overreach",
  "The freezing of over $300 billion in Russian central bank assets in 2022 served as a major warning to non-Western states, demonstrating the vulnerability of relying entirely on Western financial infrastructure for reserve holdings and cross-border settlement.",
  "ALTERNATIVE INFRASTRUCTURE", "CIPS and Bilateral Networks",
  "China, Russia, and India have rapidly expanded alternative cross-border payment networks like CIPS to bypass SWIFT. While the US dollar remains dominant, non-dollar bilateral trade is rising steadily, slowly eroding the effectiveness of Western sanctions.",
  "19"))

slides.append(four_cards("light", "Part I · Systemic Friction", "The Fragility of Unregulated Power", [
    ("Institutional Decline", "Vital multilateral institutions like the UN Security Council and WTO are increasingly paralyzed by Great Power rivalries, leaving the system without trusted arbiters to manage disputes."),
    ("The Populist Catalyst", "Domestic political survival is increasingly tied to populist nationalism, rewarding aggressive posturing and penalizing the quiet compromises necessary for effective diplomacy."),
    ("The Risk Matrix", "With expanding military forces, growing domestic pressures, and fading diplomatic communication lines, the modern system has become deeply volatile."),
    ("Crisis Potential", "This multi-polar layout creates an environment where a minor regional dispute can quickly spiral into a major global crisis — the core structural warning of our era.")
], "20"))

# Part II divider
slides.append(statement("light", "Part II · Current Geopolitical Flashpoints", "Mapping the Modern Fault Lines",
    "Modern global instability is concentrated along geographical fault lines where the vital interests of nuclear-armed Great Powers directly collide. These flashpoints are deeply interconnected — a major crisis in the Taiwan Strait would immediately drain Western military resources, creating strategic opportunities elsewhere. The combination of long-range precision weaponry, advanced cyber capabilities, and compressed decision-making timelines makes managing these friction points exceptionally difficult.",
    "21"))

slides.append(statement("light", "Part II · The Taiwan Strait", "The Center of the US-China Rivalry",
    "Beijing views Taiwan as an unalienable part of its sovereign territory with unification labeled a core national goal. For the United States, Taiwan serves as a critical democratic anchor within the First Island Chain, controlling maritime chokepoints regulating access to the wider Western Pacific. Taiwan's near-monopoly on advanced semiconductor manufacturing introduces a vital layer of economic urgency — a conflict would instantly freeze global high-tech industries.",
    "22"))

slides.append(ledger("light", "Part II · Data: Taiwan Balance of Power", "The Balance of Forces Across the Strait", [
    ("1,000+", "Short and medium-range ballistic missiles targeting Taiwan's defensive infrastructure", "target"),
    ("160km", "Volatile water crossing required for cross-strait invasion — a complex amphibious operation", "waves"),
    ("$10T", "Projected global economic shock from a major Taiwan war — roughly 10% of global GDP", "trending-down")
], "23"))

slides.append(statement("light", "Part II · TSMC and Global Vulnerability", "The Microchip Chokepoint",
    "Taiwan Semiconductor Manufacturing Company produces over 90% of the world's most advanced microchips, critical for everything from smartphones to precision-guided missiles and AI infrastructure. This concentration acts as a 'Silicon Shield' — both Washington and Beijing have a massive stake in preventing physical destruction of the island's foundries. Western export controls targeting China's access to advanced chip equipment have accelerated Beijing's push for technology self-reliance, turning semiconductors into a central point of competition.",
    "24"))

slides.append(duo("light", "Part II · The South China Sea", "Freedom of Navigation vs. Sovereignty",
  "NINE-DASH LINE CLAIMS", "Historic Sovereignty Assertion",
  "Beijing claims historic sovereignty over roughly 80% of the South China Sea, conflicting with EEZs of the Philippines, Vietnam, Malaysia, and Taiwan. The PLA has fortified a network of artificial islands with long-range anti-ship missiles and runways.",
  "ESCALATION RISK", "Incident-Driven Crisis",
  "Regular close encounters between Chinese and regional navies create continuous risk of escalation. The United States' Mutual Defense Treaty commitments to allies like the Philippines add a treaty-trigger dimension to every maritime confrontation.",
  "25"))

slides.append(ledger("light", "Part II · Data: South China Sea", "The Stakes of Maritime Transit", [
    ("$3.4T", "Annual maritime trade passing through the South China Sea — nearly one-third of global shipping", "ship"),
    ("11B", "Barrels of estimated oil reserves beneath the sea bed, driving offshore drilling competition", "droplet"),
    ("12nm", "Distance within which the US Navy conducts FONOPs, challenging Beijing's maritime assertions", "navigation")
], "26"))

slides.append(statement("light", "Part II · The Korean Peninsula", "The Permanent Nuclear Shadow",
    "Pyongyang views its nuclear and ballistic missile arsenal as the sole guarantee of regime survival, rejecting denuclearization. North Korea has deepened strategic partnerships, signing a mutual defense pact with Russia in 2024 — exchanging conventional munitions for advanced military technology. This growing threat forces Washington, Seoul, and Tokyo into tighter defense integration, which Beijing views as encirclement.",
    "27"))

slides.append(ledger("light", "Part II · Data: North Korea's Arsenal", "Quantifying the Military Threat", [
    ("50–90", "Active nuclear warheads with steady fissile material production to expand inventory", "radioactive"),
    ("13,000km", "Hwasong-17/18 ICBM range — putting the entire continental US within strike range", "target"),
    ("6,000+", "Artillery systems positioned within range of the Seoul Metropolitan Area", "crosshair")
], "28"))

slides.append(duo("light", "Part II · The Sino-Indian Border", "High-Altitude Friction",
  "THE LINE OF ACTUAL CONTROL", "3,488km Disputed Border",
  "India and China share a poorly defined Himalayan border where competing territorial interpretations have led to recurring tense military standoffs. Both sides are building all-weather roads, forward airfields, and military outposts along the LAC.",
  "STRATEGIC CONSEQUENCES", "Shifting Alliances",
  "Persistent border friction has permanently altered New Delhi's strategic view, forcing India away from non-alignment and closer to Western security frameworks like the Quad — a major strategic shift in the Indo-Pacific balance.",
  "29"))

slides.append(ledger("light", "Part II · Data: Himalayan Standoff", "The Material Reality", [
    ("50,000+", "Soldiers permanently deployed by each side along the Ladakh front since the 2020 Galwan clash", "users"),
    ("14,000ft", "Altitude of military operations — requiring specialized training and complex logistics", "mountain"),
    ("Major", "South Asian rivers (Indus, Brahmaputra) originating on the Tibetan Plateau — water security at risk", "droplet")
], "30"))

slides.append(statement("light", "Part II · The War in Ukraine", "The Ukrainian Cauldron",
    "The ongoing war has become a defining conflict over the future of European security, directly pitting Russian revanchism against Western institutional alignment. The conflict has shifted into a high-intensity industrial war of attrition, pressing both sides' manufacturing capacity. Ongoing Western military aid runs up against Moscow's red lines, creating a constant risk of spillover into direct NATO-Russia confrontation.",
    "31"))

slides.append(ledger("light", "Part II · Data: Costs of the War", "Mapping the Economic and Human Toll", [
    ("10,000–20,000", "Russian artillery shells fired daily during peak combat — illustrating the logistical demands of modern warfare", "crosshair"),
    ("$250B+", "Combined US and European financial, humanitarian, and military aid to Ukraine since February 2022", "trending-up"),
    ("6M+", "Refugees displaced across Europe — the largest refugee crisis on the continent since WWII", "users")
], "32"))

slides.append(four_cards("light", "Part II · The Middle East", "Proxy Wars and State Breakdown", [
    ("The Proxy Network", "Iran projects influence through its 'Axis of Resistance' — Hezbollah, Hamas, the Houthis — challenging Israeli security and American presence indirectly without direct state confrontation."),
    ("Deterrence Crisis", "Intense conventional and asymmetric exchanges between Israel and Iran have undermined regional stability, showing that old deterrence models are failing to prevent direct state-on-state clashes."),
    ("Global Vulnerabilities", "Regional conflicts directly threaten vital maritime chokepoints — particularly Bab el-Mandeb and the Strait of Hormuz — where disruptions trigger energy shocks and supply chain delays worldwide."),
    ("Defense Spending", "The Middle East maintains some of the highest defense expenditures globally relative to GDP, with Saudi Arabia and Israel regularly spending over 5-7% of GDP on security.")
], "33"))

slides.append(ledger("light", "Part II · Data: Middle East Chokepoints", "The Strategic Value of Energy Flows", [
    ("20M", "Barrels of oil per day through the Strait of Hormuz — roughly 20% of global petroleum consumption", "droplet"),
    ("10–14", "Extra days added to shipping routes when Red Sea disruptions force Cape of Good Hope diversions", "clock"),
    ("5–7%", "GDP percentage spent on defense by Saudi Arabia and Israel — among the highest globally", "shield")
], "34"))

slides.append(duo("light", "Part II · The Arctic", "The New Frontier of Competition",
  "THE POLAR OPENING", "Climate Change and New Routes",
  "Accelerating climate change and receding polar ice are opening maritime transit routes and providing access to massive untapped subsea mineral and energy reserves. The Northern Sea Route cuts transit distances between East Asia and Europe by up to 40%.",
  "MILITARIZATION", "NATO Expansion and Russian Bases",
  "Moscow has modernized over 50 Soviet-era military outposts across its Arctic coastline. With Finland and Sweden joining NATO, the Arctic has emerged as a direct military friction zone requiring strengthened northern defenses.",
  "35"))

slides.append(ledger("light", "Part II · Data: Arctic Resources", "The Wealth and Weapons of the North", [
    ("13%", "World's undiscovered oil reserves held in the Arctic — plus 30% of undiscovered natural gas", "droplet"),
    ("50+", "Modernized Soviet-era military outposts across Russia's Arctic coastline with S-400 air defenses", "shield"),
    ("40%", "Transit distance reduction between East Asia and Europe via the Northern Sea Route vs Suez Canal", "navigation")
], "36"))

slides.append(four_cards("light", "Part II · Cyber and Space", "The Invisible War Zones", [
    ("The Gray Zone", "Modern Great Power competition plays out continuously in cyber and space domains. Attacks often remain below the threshold of open war but can still cause significant strategic damage."),
    ("Space Dependence", "Modern militaries depend on space assets for precision positioning, navigation, timing, and secure communications — making satellites prime targets for neutralization."),
    ("Infrastructure Vulnerabilities", "Digital integration into civilian infrastructure leaves power grids, financial networks, and water treatment systems vulnerable to state-sponsored cyber disruptions."),
    ("ASAT Capabilities", "Four nations — the US, Russia, China, and India — have demonstrated kinetic anti-satellite weapons, capable of destroying orbital infrastructure during a crisis.")
], "37"))

slides.append(ledger("light", "Part II · Data: Cyber and Space", "The Expanding Footprint of Warfare", [
    ("10,000+", "Active satellites in orbit — driven by commercial expansion like Starlink, now critical to military operations", "satellite"),
    ("4", "Nations with demonstrated kinetic ASAT capabilities — the US, Russia, China, and India", "target"),
    ("Millions", "Daily cyber scans and digital probes by major powers against the critical infrastructure of rivals", "shield")
], "38"))

slides.append(statement("light", "Part II · Gray-Zone Coercion", "Case Study: Second Thomas Shoal",
    "The deliberate grounding of the BRP Sierra Madre by Manila in 1999 created a unique outpost to assert sovereign rights over Second Thomas Shoal. Beijing uses its Coast Guard and maritime militia to block Philippine resupply missions with water cannons and ramming tactics — applying pressure while avoiding direct US military response. This gray-zone friction creates a continuous risk of miscalculation that could force a formal request for American intervention, testing Washington's commitments.",
    "39"))

slides.append(four_cards("light", "Part II · Compound Crisis", "The Danger of Synchronized Crises", [
    ("Horizontal Escalation", "Modern flashpoints are deeply interconnected. A major conflict in one theater can spark secondary crises as revisionist powers take advantage of strained global attention."),
    ("Strategic Overstretch", "Simultaneous tensions across Eastern Europe, the Taiwan Strait, and Middle Eastern shipping lanes threaten to overwhelm Western military capabilities and political focus."),
    ("Systemic Fragility", "The international community faces danger not just from individual disputes but from a coordinated breakdown of order across multiple fronts simultaneously."),
    ("Path to Crisis", "This interconnected fragility increases the risk that a manageable regional dispute escalates into a wider global conflict — the compound crisis scenario.")
], "40"))

# Part III
slides.append(statement("light", "Part III · The Dark Mirror of 1914", "The Structural Fluidity of the Belle Époque",
    "In the decades before 1914, Europe split into rigid opposing alliance networks — the Triple Entente and Triple Alliance — turning local disputes into systemic threats. Rapid industrial expansion drove intense competition for colonies, resources, and naval dominance. The European elite believed deep economic integration made major war impossible. This shared complacency left them blind to how fragile their security arrangements actually were. The structural parallels to today are unmistakable.",
    "41"))

slides.append(ledger("light", "Part III · Data: The Great War", "The Scale of the July Crisis Breakdown", [
    ("10", "Days from Austria-Hungary's mobilization against Serbia to five major empires being fully at war", "clock"),
    ("20M+", "Deaths in the First World War, with 21 million wounded — demonstrating industrialized warfare's destructive power", "trending-down"),
    ("1M+", "Casualties in just five months at the Battle of the Somme — human lives treated as anonymous numbers", "crosshair")
], "42"))

# Slide 43 - Timeline
slides.append("""<section class="slide light" data-animate="timeline-walk">
  <div class="canvas-card">
    <div class="chrome-min"><div class="l">Part III · The July Crisis of 1914</div><div class="r">43 / 60</div></div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;gap:2.6vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:.8vh">
        <div class="t-meta">HOW A REGIONAL INCIDENT SPARKED GLOBAL WAR</div>
        <h2 class="h-xl-zh" style="font-size:min(4.4vw,8vh)">The Sarajevo Assassination and Systemic Collapse</h2>
      </div>
      <div class="timeline-h" data-anim="tl" style="flex:1">
        <span class="tl-h-axis" style="position:absolute;left:5%;right:5%;top:50%;height:1px;background:repeating-linear-gradient(to right,currentColor 0 4px,transparent 4px 8px);opacity:.35"></span>
        <div class="tl-row" style="position:relative;width:100%;display:grid;grid-template-columns:repeat(4,1fr);align-items:center">
          <div class="th-node up" style="position:relative;display:flex;justify-content:center">
            <span class="dot" style="width:8px;height:8px;border-radius:50%;background:var(--ink);z-index:1;position:relative"></span>
            <div class="label" style="position:absolute;left:50%;transform:translateX(-50%);bottom:calc(50% + 22px);width:16vw;text-align:center;display:flex;flex-direction:column;gap:.4vh">
              <span class="name" style="font-family:var(--sans);font-size:max(16px,1.05vw);font-weight:400;color:var(--text-primary)">Assassination</span>
              <span class="desc" style="font-family:var(--sans),var(--sans-zh);font-size:max(14px,.84vw);color:var(--text-secondary)">June 28 — Archduke Franz Ferdinand killed in Sarajevo</span>
            </div>
          </div>
          <div class="th-node up" style="position:relative;display:flex;justify-content:center">
            <span class="dot" style="width:8px;height:8px;border-radius:50%;background:var(--ink);z-index:1;position:relative"></span>
            <div class="label" style="position:absolute;left:50%;transform:translateX(-50%);bottom:calc(50% + 22px);width:16vw;text-align:center;display:flex;flex-direction:column;gap:.4vh">
              <span class="name" style="font-family:var(--sans);font-size:max(16px,1.05vw);font-weight:400;color:var(--text-primary)">Blank Check</span>
              <span class="desc" style="font-family:var(--sans),var(--sans-zh);font-size:max(14px,.84vw);color:var(--text-secondary)">Germany backs Vienna; Russia mobilizes for Serbia</span>
            </div>
          </div>
          <div class="th-node up" style="position:relative;display:flex;justify-content:center">
            <span class="dot" style="width:8px;height:8px;border-radius:50%;background:var(--ink);z-index:1;position:relative"></span>
            <div class="label" style="position:absolute;left:50%;transform:translateX(-50%);bottom:calc(50% + 22px);width:16vw;text-align:center;display:flex;flex-direction:column;gap:.4vh">
              <span class="name" style="font-family:var(--sans);font-size:max(16px,1.05vw);font-weight:400;color:var(--text-primary)">Diplomatic Failure</span>
              <span class="desc" style="font-family:var(--sans),var(--sans-zh);font-size:max(14px,.84vw);color:var(--text-secondary)">Rigid planning + poor communication eliminate compromise</span>
            </div>
          </div>
          <div class="th-node up accent" style="position:relative;display:flex;justify-content:center">
            <span class="dot" style="width:8px;height:8px;border-radius:50%;background:var(--accent);z-index:1;position:relative"></span>
            <div class="label" style="position:absolute;left:50%;transform:translateX(-50%);bottom:calc(50% + 22px);width:16vw;text-align:center;display:flex;flex-direction:column;gap:.4vh">
              <span class="name" style="font-family:var(--sans);font-size:max(16px,1.05vw);font-weight:400;color:var(--accent)">Systemic Collapse</span>
              <span class="desc" style="font-family:var(--sans),var(--sans-zh);font-size:max(14px,.84vw);color:var(--text-secondary)">July 28 — Austria declares war; alliances trigger chain reaction</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>""")

slides.append(duo("light", "Part III · Modern Jingoism", "Digital Echo Chambers and Nationalism",
  "THE DIGITAL CATALYST", "Social Media Polarization",
  "Modern social media algorithms prioritize outrage and conflict, amplifying hyper-nationalist rhetoric and reducing public support for quiet diplomatic compromises. Complex international disputes are reduced to simplistic black-and-white narratives.",
  "POPULIST DRIVERS", "Domestic Political Incentives",
  "Political leaders use aggressive foreign policy stances to rally domestic support, creating rigid positions that make international concessions look like weakness. This structural shift narrows the space available for crisis diplomacy.",
  "44"))

slides.append(statement("light", "Part III · Technological Acceleration", "War at the Speed of Cyber and Hypersonics",
    "The deployment of hypersonic missiles and autonomous strike drones cuts flight times between rivals to minutes, severely limiting the time leaders have to verify data and make decisions. Incorporating artificial intelligence into early-warning systems introduces unpredictable risks. Automated assessments can misinterpret military exercises or accidental sensor data as an incoming attack, making policymakers dependent on pre-planned responses and increasing the danger of accidental escalation.",
    "45"))

slides.append(four_cards("light", "Part III · The Illusion of Rationality", "Personality and Psychology in Crises", [
    ("Flawed Rational Actor Models", "History shows international decisions are deeply shaped by the personal fears, biases, and hubris of individual leaders — not cold rational calculation."),
    ("Autocratic Isolation", "In centralized regimes, leaders operate in echo chambers cut off from objective information, increasing the likelihood of highly risky decisions."),
    ("Democratic Constraints", "Constant electoral cycles and intense media scrutiny drive reactive, short-term foreign policy designed for domestic political gain rather than long-term stability."),
    ("Volatile Personalities", "When nuclear-armed great powers are led by unpredictable individuals with varying risk tolerances, the margin for error shrinks dramatically.")
], "46"))

slides.append(statement("light", "Part III · The Fatalism Trap", "The Psychology of Geopolitical Resignation",
    "One of the most dangerous dynamics in modern geopolitics is the growing belief among elites that a major conflict between Great Powers has become inevitable — a shift that turns worst-case scenarios into self-fulfilling prophecies. The security dilemma traps both sides in an escalatory spiral: defensive actions by one state are interpreted as offensive threats by its rivals, accelerating military spending and undermining security. When leaders believe war is certain, they face structural pressure to launch preemptive strikes.",
    "47"))

slides.append(duo("light", "Part III · The Failure of Deterrence", "Why Hard Power is Not Enough",
  "THE DETERRENCE FALLACY", "Over-Reliance on Military Power",
  "An over-reliance on building military power can provoke the exact aggressive responses it is intended to prevent, as rivals feel forced to challenge what they see as encirclement.",
  "THE COST OF FAILURE", "When Deterrence Collapses",
  "Clear communication of red lines is exceptionally difficult in a multi-polar system with vastly different risk tolerances. When deterrence fails, it does so suddenly and completely, leaving no tools to defuse the crisis.",
  "48"))

slides.append(statement("light", "Part III · The Case for Active Peacecraft", "Peace as an Active Process",
    "True peace is not simply the temporary absence of war — it is an active, demanding process requiring continuous diplomatic effort, institutional investment, and strategic compromise. Re-establishing dependable communication channels and hotlines between Great Power militaries is critical to preventing minor accidents from turning into major conflicts. The international community must prioritize modernizing multilateral organizations to reflect today's multi-polar reality rather than the outdated power balances of 1945.",
    "49"))

slides.append(four_cards("light", "Part III · Crisis Communication", "Restoring Hotlines and Strategic Transparency", [
    ("Direct Hotlines", "Maintaining operational, continuous communications links between heads of state and top military commanders is essential to managing fast-moving geopolitical crises."),
    ("Military Transparency", "Regular, structured dialogues between opposing military leaderships clarify doctrine, reduce misunderstandings during exercises, and build predictable behavioral patterns."),
    ("Crisis Standards", "Shared protocols for handling close maritime or aerial encounters provide a framework to de-escalate incidents before they require high-level political intervention."),
    ("Data Swaps", "Exchanging information on nuclear stockpiles, missile tests, and military exercises helps lower suspicion and prevents destabilizing surprises.")
], "50"))

slides.append(statement("light", "Part III · The Power of Interpersonal Diplomacy", "Personal Relations as Strategic Stabilizers",
    "Face-to-face meetings between top leaders are vital to reducing misjudgments and helping policymakers understand the core anxieties and domestic pressures driving their rivals. Diplomatic engagement requires a willingness to recognize a competitor's basic security concerns, even when their political values remain completely incompatible. Moving sensitive negotiations away from public arenas allows diplomats to explore creative compromises without facing immediate domestic political backlash.",
    "51"))

slides.append(four_cards("light", "Part III · Revitalizing Multilateral Institutions", "Adapting Global Governance to Multi-Polarity", [
    ("Reform Frameworks", "Global institutions must reflect the rise of new powers like India, Brazil, and regional leaders — moving past the post-WWII arrangements that dominate today."),
    ("Empowering Middle Powers", "Middle powers play a vital role as trusted mediators and stable buffers in disputes, helping to check the aggressive tendencies of dominant Great Powers."),
    ("Rebuilding Norms", "Basic shared rules in emerging arenas like cyber warfare, autonomous weapons, and space activities are essential to prevent unregulated competition."),
    ("Inclusive Governance", "Expanding permanent representation in multilateral bodies to reflect modern economic and demographic realities strengthens institutional legitimacy.")
], "52"))

slides.append(statement("light", "Part III · Strategic Empathy", "Seeing Through the Rival's Eyes",
    "Strategic empathy is not about accepting or condoning a rival's behavior — it is the objective practice of understanding the historical grievances and fears that drive their choices. Framing complex rivalries as simple moral battles blinds a nation to seeing where its own actions provoke defensive responses. By identifying a rival's core security requirements, states can design deterrence policies that protect vital interests while avoiding the total encirclement that forces an opponent into a desperate corner.",
    "53"))

slides.append(whynow("light", "Part III · The Economics of Peace", "Balancing Derisking with Connection", [
    ("The Risk of Decoupling", "While building resilient supply chains is prudent, total economic decoupling eliminates important financial incentives for maintaining peace between Great Powers.", "Risk"),
    ("Preserving Commercial Ties", "Deep, well-regulated trade relationships create a shared economic stake in stability, ensuring the financial costs of conflict remain high for all sides.", "Shared"),
    ("Coordinated Interdependence", "Strategic stability is enhanced when rival powers remain dependent on the broader global trading system, making cooperative participation more attractive than military expansion.", "Stability")
], "54"))

slides.append(four_cards("light", "Part III · Arms Control in the New Era", "Modernizing Non-Proliferation and Verification", [
    ("Multi-Party Frameworks", "Old two-party arms control models must expand to include emerging nuclear states, particularly China's rapidly growing arsenal."),
    ("Regulating Novel Technologies", "International rules for hypersonic delivery vehicles, cyber weapons, and space-based platforms are essential to prevent dangerous arms races."),
    ("Practical Transparency", "Advance notifications of missile tests and shared data on nuclear stockpiles help lower suspicion between rivals."),
    ("Verified Reductions", "Building on New START and INF frameworks, verifiable warhead limits must adapt to today's multi-party nuclear landscape.")
], "55"))

slides.append(duo("light", "Part III · Managing Domestic Nationalism", "Countering Jingoism and Political Rhetoric",
  "RESPONSIBLE LEADERSHIP", "Avoiding Xenophobic Rhetoric",
  "Political elites have an obligation to avoid using hyper-nationalist rhetoric for short-term gain. Such language limits flexibility during real crises and narrows the space for compromise.",
  "BALANCED NARRATIVES", "Educating Publics on War's True Cost",
  "Ensuring diverse, balanced media perspectives on international affairs checks simplistic narratives. Educating publics about the immense human cost of past conflicts defends against romanticized aggression.",
  "56"))

slides.append(four_cards("light", "Part III · Civil Society", "Rebuilding Transnational Connections", [
    ("Track Two Diplomacy", "Non-governmental channels through academic networks, business groups, and cultural institutions maintain vital links when formal diplomacy stalls."),
    ("Educational Exchanges", "International student exchanges and cross-border research collaborations build long-term connections that challenge hostile stereotypes."),
    ("Public Accountability", "Civil society organizations track foreign policy decisions, reminding leaders of their accountability and pushing back against policies leading toward war."),
    ("Cultural Connection", "Sustained cultural exchange programs create human-level relationships that transcend political tensions between rival nations.")
], "57"))

slides.append(whynow("light", "Part III · Guardrails Against the Storm", "Operational Priorities for Global Stability", [
    ("Immediate Guardrails", "Crisis hotlines, maritime protocols, and regular military-to-military de-escalation talks across all major flashpoints must be established now.", "Hotlines"),
    ("Diplomatic Commitments", "Reinvesting in bilateral diplomacy, practicing strategic empathy, and supporting multilateral governance reforms to adapt systems to multi-polarity.", "Diplomacy"),
    ("Long-Term Anchors", "Maintaining economic connections, modernizing arms control, and managing domestic nationalist rhetoric to reduce the systemic risk of war.", "Anchors")
], "58"))

slides.append(statement("light", "Part III · Conclusion: Heeding History", "Choosing De-Escalation Over Complacency",
    "The central lesson of the pre-1914 breakdown is that global conflict is never truly inevitable — it is the result of repeated choices, structural neglect, and an absence of diplomatic will. Modern leaders cannot assume that deep economic ties or nuclear deterrence will automatically prevent catastrophe. Peace requires continuous, active management. By recognizing the structural risks of our crowded multi-polar world and choosing active diplomacy over passive drift, we can defuse the coming storm.",
    "59"))

slides.append(closing())

# Now insert slides into template
slide_block = "\n\n".join(slides)
html = html.replace('<!-- SLIDES_HERE · 在此处粘贴 <section class="slide ..."> 页面块', slide_block + '\n\n<!-- SLIDES_HERE · 在此处粘贴 <section class="slide ..."> 页面块')

with open(OUTPUT, 'w') as f:
    f.write(html)

print(f"Generated 60-slide deck → {OUTPUT}")
print(f"Total lines: {html.count(chr(10))}")
