import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Dictionary of strings to replace
replacements = {
    # Nav
    '<a class="nav-logo" href="#hero">JMMD</a>': '<a class="nav-logo" href="#hero">JMMD</a>\n  <button id="langToggle" class="lang-toggle">EN / ES</button>',
    '<li><a href="#positioning">Positioning</a></li>': '<li><a href="#positioning" data-i18n="nav_pos">Positioning</a></li>',
    '<li><a href="#operate">How I Operate</a></li>': '<li><a href="#operate" data-i18n="nav_op">How I Operate</a></li>',
    '<li><a href="#experience">Experience</a></li>': '<li><a href="#experience" data-i18n="nav_exp">Experience</a></li>',
    '<li><a href="#casestudy">Case Study</a></li>': '<li><a href="#casestudy" data-i18n="nav_case">Case Study</a></li>',
    '<li><a href="#system">30-Day Plan</a></li>': '<li><a href="#system" data-i18n="nav_sys">30-Day Plan</a></li>',
    '<li><a href="#closing">Let\'s Talk</a></li>': '<li><a href="#closing" data-i18n="nav_talk">Let\'s Talk</a></li>',

    # Hero
    '<div class="hero-eyebrow">Operations Lead · Build → Stabilize → Scale</div>': '<div class="hero-eyebrow" data-i18n="hero_eyebrow">Operations Lead · Build → Stabilize → Scale</div>',
    '<div class="hero-role">Systems · Workflows · AI-Enabled Execution</div>': '<div class="hero-role" data-i18n="hero_role">Systems · Workflows · AI-Enabled Execution</div>',
    '<a>Medellín, Colombia · Remote-Ready</a>': '<a data-i18n="location">Medellín, Colombia · Remote-Ready</a>',
    '<span>Scroll</span>': '<span data-i18n="scroll">Scroll</span>',
    '<h2 class="hero-statement">How I think.<br>How I operate.<br>What you get.</h2>': '<h2 class="hero-statement" data-i18n="hero_statement">How I think.<br>How I operate.<br>What you get.</h2>',
    '<p class="hero-sub">A portfolio of operational thinking —<br>not a list of job titles.</p>': '<p class="hero-sub" data-i18n="hero_sub">A portfolio of operational thinking —<br>not a list of job titles.</p>',
    '<div class="hero-tag">15+ Years · LATAM · U.S. · Europe</div>': '<div class="hero-tag" data-i18n="hero_tag">15+ Years · LATAM · U.S. · Europe</div>',

    # 01 POSITIONING
    '<div class="section-tag reveal">01 · Positioning</div>': '<div class="section-tag reveal" data-i18n="pos_tag">01 · Positioning</div>',
    '<h2 class="section-title reveal">I don\'t manage tasks.</h2>': '<h2 class="section-title reveal" data-i18n="pos_title">I don\'t manage tasks.</h2>',
    '<p class="section-sub reveal">I close the gap between decisions and execution.</p>': '<p class="section-sub reveal" data-i18n="pos_sub">I close the gap between decisions and execution.</p>',
    '<p>Most operations don\'t break because of bad strategy. They break between priorities, communication, and follow-through.</p>': '<p data-i18n="pos_p1">Most operations don\'t break because of bad strategy. They break between priorities, communication, and follow-through.</p>',
    '<p>Things get delayed. Ownership becomes unclear. The CEO ends up carrying operational noise instead of focusing on decisions.</p>': '<p data-i18n="pos_p2">Things get delayed. Ownership becomes unclear. The CEO ends up carrying operational noise instead of focusing on decisions.</p>',
    '<p><strong>That\'s the gap I operate in.</strong></p>': '<p><strong data-i18n="pos_p3">That\'s the gap I operate in.</strong></p>',
    '<p>I\'ve built systems for payroll operations at 15,000-person scale, coordinated 200+ monthly shipments across 12 international vendors, and built an AI-enabled B2B SaaS product from zero — as a solo operator. Curiosity has always pushed me further than the job description. That\'s not a credential. It\'s a pattern.</p>': '<p data-i18n="pos_p4">I\'ve built systems for payroll operations at 15,000-person scale, coordinated 200+ monthly shipments across 12 international vendors, and built an AI-enabled B2B SaaS product from zero — as a solo operator. Curiosity has always pushed me further than the job description. That\'s not a credential. It\'s a pattern.</p>',
    '<p>"If I have 5 hours to cut a tree, I\'ll spend 3 sharpening the axe."</p>': '<p data-i18n="quote_axe">"If I have 5 hours to cut a tree, I\'ll spend 3 sharpening the axe."</p>',
    '<div class="pillar-title">Execution at speed</div>': '<div class="pillar-title" data-i18n="pil1_t">Execution at speed</div>',
    '<div class="pillar-desc">Delays compound fast in multi-stakeholder environments. Execution needs to keep up.</div>': '<div class="pillar-desc" data-i18n="pil1_d">Delays compound fast in multi-stakeholder environments. Execution needs to keep up.</div>',
    '<div class="pillar-title">Structure from chaos</div>': '<div class="pillar-title" data-i18n="pil2_t">Structure from chaos</div>',
    '<div class="pillar-desc">I build systems that don\'t rely on constant supervision. They outlive my involvement.</div>': '<div class="pillar-desc" data-i18n="pil2_d">I build systems that don\'t rely on constant supervision. They outlive my involvement.</div>',
    '<div class="pillar-title">Proactive, not reactive</div>': '<div class="pillar-title" data-i18n="pil3_t">Proactive, not reactive</div>',
    '<div class="pillar-desc">I surface problems before they become bottlenecks. That\'s where the real value is.</div>': '<div class="pillar-desc" data-i18n="pil3_d">I surface problems before they become bottlenecks. That\'s where the real value is.</div>',

    # 02 HOW I OPERATE
    '<h2 class="operate-title">How I<br>Operate</h2>': '<h2 class="operate-title" data-i18n="op_title">How I<br>Operate</h2>',
    '<p class="operate-subtitle">My mental framework — not a job description.</p>': '<p class="operate-subtitle" data-i18n="op_sub">My mental framework — not a job description.</p>',
    '<cite>— The principle I operate by</cite>': '<cite data-i18n="op_cite">— The principle I operate by</cite>',
    '<div class="principle-label">Triage first.</div>': '<div class="principle-label" data-i18n="pr1_t">Triage first.</div>',
    '<div class="principle-desc">I decide what moves now, what waits, and what doesn\'t matter. Nothing enters execution without a clear priority.</div>': '<div class="principle-desc" data-i18n="pr1_d">I decide what moves now, what waits, and what doesn\'t matter. Nothing enters execution without a clear priority.</div>',
    '<div class="principle-label">Build the system, not just the fix.</div>': '<div class="principle-label" data-i18n="pr2_t">Build the system, not just the fix.</div>',
    '<div class="principle-desc">If a problem repeats, the system is broken. I document and structure it so it doesn\'t depend on me again.</div>': '<div class="principle-desc" data-i18n="pr2_d">If a problem repeats, the system is broken. I document and structure it so it doesn\'t depend on me again.</div>',
    '<div class="principle-label">Close loops visibly.</div>': '<div class="principle-label" data-i18n="pr3_t">Close loops visibly.</div>',
    '<div class="principle-desc">A task isn\'t done when it\'s sent. It\'s done when it\'s confirmed. I track open loops so nothing disappears.</div>': '<div class="principle-desc" data-i18n="pr3_d">A task isn\'t done when it\'s sent. It\'s done when it\'s confirmed. I track open loops so nothing disappears.</div>',
    '<div class="principle-label">Translate context to action.</div>': '<div class="principle-label" data-i18n="pr4_t">Translate context to action.</div>',
    '<div class="principle-desc">Ideas are useless without ownership. I turn conversations into tasks, owners, and deadlines — immediately.</div>': '<div class="principle-desc" data-i18n="pr4_d">Ideas are useless without ownership. I turn conversations into tasks, owners, and deadlines — immediately.</div>',
    '<div class="principle-label">Minimal hand-holding.</div>': '<div class="principle-label" data-i18n="pr5_t">Minimal hand-holding.</div>',
    '<div class="principle-desc">I clarify once, early. After that, I execute and adapt without waiting.</div>': '<div class="principle-desc" data-i18n="pr5_d">I clarify once, early. After that, I execute and adapt without waiting.</div>',

    # 03 EXPERIENCE
    '<div class="section-tag reveal">03 · Relevant Experience</div>': '<div class="section-tag reveal" data-i18n="exp_tag">03 · Relevant Experience</div>',
    '<h2 class="section-title reveal">Not a CV.</h2>': '<h2 class="section-title reveal" data-i18n="exp_title">Not a CV.</h2>',
    '<p class="section-sub reveal">Operational impact, in context.</p>': '<p class="section-sub reveal" data-i18n="exp_sub">Operational impact, in context.</p>',
    '<div class="exp-role">Operations & Admin Manager</div>': '<div class="exp-role" data-i18n="exp1_role">Operations & Admin Manager</div>',
    '<div class="exp-company">Editorial Amolca · 2021–2025</div>': '<div class="exp-company" data-i18n="exp1_co">Editorial Amolca · 2021–2025</div>',
    '<li>12+ international vendors · 200+ monthly shipments · LATAM, U.S., Europe</li>': '<li data-i18n="exp1_b1">12+ international vendors · 200+ monthly shipments · LATAM, U.S., Europe</li>',
    '<li>Centralized tracking system (Notion + Excel) → reduced follow-up overhead ~20%</li>': '<li data-i18n="exp1_b2">Centralized tracking system (Notion + Excel) → reduced follow-up overhead ~20%</li>',
    '<li>AI-assisted workflows → translation turnaround cut by 60–70%</li>': '<li data-i18n="exp1_b3">AI-assisted workflows → translation turnaround cut by 60–70%</li>',
    '<div class="exp-role">Head of Personnel Administration</div>': '<div class="exp-role" data-i18n="exp2_role">Head of Personnel Administration</div>',
    '<div class="exp-company">Government of Táchira · 2009–2012</div>': '<div class="exp-company" data-i18n="exp2_co">Government of Táchira · 2009–2012</div>',
    '<li>Payroll & HR for 15,000 individuals — zero-error execution at scale</li>': '<li data-i18n="exp2_b1">Payroll & HR for 15,000 individuals — zero-error execution at scale</li>',
    '<li>Decision-ready workforce briefings for senior leadership</li>': '<li data-i18n="exp2_b2">Decision-ready workforce briefings for senior leadership</li>',
    '<li>Audit-ready documentation across multiple government agencies</li>': '<li data-i18n="exp2_b3">Audit-ready documentation across multiple government agencies</li>',
    '<div class="exp-role">Executive & Operations Assistant</div>': '<div class="exp-role" data-i18n="exp3_role">Executive & Operations Assistant</div>',
    '<div class="exp-company">E-Commerce Operator · 2021</div>': '<div class="exp-company" data-i18n="exp3_co">E-Commerce Operator · 2021</div>',
    '<li>Sole operational support in high-volume digital commerce environment</li>': '<li data-i18n="exp3_b1">Sole operational support in high-volume digital commerce environment</li>',
    '<li>Daily financial tracking, reconciliations, and executive coordination</li>': '<li data-i18n="exp3_b2">Daily financial tracking, reconciliations, and executive coordination</li>',
    '<li>High-accountability, minimal structure — exactly the EA-to-CEO profile</li>': '<li data-i18n="exp3_b3">High-accountability, minimal structure — exactly the EA-to-CEO profile</li>',
    '<div class="exp-role">Founder & Operations Lead</div>': '<div class="exp-role" data-i18n="exp4_role">Founder & Operations Lead</div>',
    '<div class="exp-company">RadLeadX (B2B SaaS) · 2026–Present</div>': '<div class="exp-company" data-i18n="exp4_co">RadLeadX (B2B SaaS) · 2026–Present</div>',
    '<li>Built end-to-end validation workflows and AI pipelines — solo, zero-to-one</li>': '<li data-i18n="exp4_b1">Built end-to-end validation workflows and AI pipelines — solo, zero-to-one</li>',
    '<li>No playbook → built operational systems from first principles</li>': '<li data-i18n="exp4_b2">No playbook → built operational systems from first principles</li>',
    '<li>Live proof: curiosity + execution = functional product in market</li>': '<li data-i18n="exp4_b3">Live proof: curiosity + execution = functional product in market</li>',

    # 04 CASE STUDY
    '<div class="section-tag reveal">04 · Case Study</div>': '<div class="section-tag reveal" data-i18n="case_tag">04 · Case Study</div>',
    '<h2 class="section-title reveal">Cutting Time-to-Market<br>With AI-Powered Workflows</h2>': '<h2 class="section-title reveal" data-i18n="case_title">Cutting Time-to-Market<br>With AI-Powered Workflows</h2>',
    '<div class="case-stat-label">Translation<br>turnaround time</div>': '<div class="case-stat-label" data-i18n="case_s1">Translation<br>turnaround time</div>',
    '<div class="case-stat-label">Total book<br>editing cycle</div>': '<div class="case-stat-label" data-i18n="case_s2">Total book<br>editing cycle</div>',
    '<div class="case-stat-label">Months from<br>contract to launch</div>': '<div class="case-stat-label" data-i18n="case_s3">Months from<br>contract to launch</div>',
    '<div class="case-label">Situation</div>': '<div class="case-label" data-i18n="case_l1">Situation</div>',
    '<div class="case-body">Translation was fully manual — outsourced to external teams, split across multiple translators for longer titles. Time-to-market ranged from 10 to 20 months. No internal control over quality consistency or delivery speed.</div>': '<div class="case-body" data-i18n="case_b1">Translation was fully manual — outsourced to external teams, split across multiple translators for longer titles. Time-to-market ranged from 10 to 20 months. No internal control over quality consistency or delivery speed.</div>',
    '<div class="case-label">What I Did</div>': '<div class="case-label" data-i18n="case_l2">What I Did</div>',
    '<div class="case-body">Researched and piloted AI-assisted translation tools. Ran a blind test with clinical and translation reviewers — without disclosing the method — to get unbiased quality feedback. Refined the workflow based on their input, then structured a handoff process that integrated seamlessly into the existing editorial cycle.</div>': '<div class="case-body" data-i18n="case_b2">Researched and piloted AI-assisted translation tools. Ran a blind test with clinical and translation reviewers — without disclosing the method — to get unbiased quality feedback. Refined the workflow based on their input, then structured a handoff process that integrated seamlessly into the existing editorial cycle.</div>',
    '<div class="case-label">Result</div>': '<div class="case-label" data-i18n="case_l3">Result</div>',
    '<div class="case-body">External reviewers validated translation quality independently. Delivery cycles dropped from 10–20 months to 6 months — in some cases less. The workflow was fully adopted by the editorial team and now runs without my involvement.</div>': '<div class="case-body" data-i18n="case_b3">External reviewers validated translation quality independently. Delivery cycles dropped from 10–20 months to 6 months — in some cases less. The workflow was fully adopted by the editorial team and now runs without my involvement.</div>',
    '<strong>Pattern:</strong> diagnose the gap → build the structure → remove myself as the bottleneck.': '<strong data-i18n="case_pat1">Pattern:</strong> <span data-i18n="case_pat2">diagnose the gap → build the structure → remove myself as the bottleneck.</span>',

    # 05 30-DAY SYSTEM
    '<div class="section-tag reveal">05 · 30-Day Operating System</div>': '<div class="section-tag reveal" data-i18n="sys_tag">05 · 30-Day Operating System</div>',
    '<h2 class="section-title reveal">From chaos to<br>structured execution.</h2>': '<h2 class="section-title reveal" data-i18n="sys_title">From chaos to<br>structured execution.</h2>',
    '<p class="section-sub reveal">Goal: a system that runs without constant oversight.</p>': '<p class="section-sub reveal" data-i18n="sys_sub">Goal: a system that runs without constant oversight.</p>',
    '<span class="phase-period">Week 1–2</span>': '<span class="phase-period" data-i18n="sys_w1">Week 1–2</span>',
    '<span class="phase-tag">Diagnose</span>': '<span class="phase-tag" data-i18n="sys_t1">Diagnose</span>',
    '<div class="phase-name">Phase 1: Diagnose</div>': '<div class="phase-name" data-i18n="sys_n1">Phase 1: Diagnose</div>',
    '<div class="phase-goal">Understand how the system actually works.</div>': '<div class="phase-goal" data-i18n="sys_g1">Understand how the system actually works.</div>',
    '<li>Map how work flows across people, tools, and decisions</li>': '<li data-i18n="sys1_b1">Map how work flows across people, tools, and decisions</li>',
    '<li>Identify communication gaps and decision bottlenecks</li>': '<li data-i18n="sys1_b2">Identify communication gaps and decision bottlenecks</li>',
    '<li>Audit inbox, calendar, and execution flow</li>': '<li data-i18n="sys1_b3">Audit inbox, calendar, and execution flow</li>',
    '<li>Detect recurring friction before changing anything</li>': '<li data-i18n="sys1_b4">Detect recurring friction before changing anything</li>',
    '<span class="phase-period">Week 3–4</span>': '<span class="phase-period" data-i18n="sys_w2">Week 3–4</span>',
    '<span class="phase-tag">Structure</span>': '<span class="phase-tag" data-i18n="sys_t2">Structure</span>',
    '<div class="phase-name">Phase 2: Structure</div>': '<div class="phase-name" data-i18n="sys_n2">Phase 2: Structure</div>',
    '<div class="phase-goal">Turn chaos into a working system.</div>': '<div class="phase-goal" data-i18n="sys_g2">Turn chaos into a working system.</div>',
    '<li>Define priorities, ownership, and execution rules</li>': '<li data-i18n="sys2_b1">Define priorities, ownership, and execution rules</li>',
    '<li>Build tracking systems with real-time visibility</li>': '<li data-i18n="sys2_b2">Build tracking systems with real-time visibility</li>',
    '<li>Implement inbox & task triage (Action / FYI / Decision)</li>': '<li data-i18n="sys2_b3">Implement inbox & task triage (Action / FYI / Decision)</li>',
    '<li>Establish lightweight async-first operating rhythms</li>': '<li data-i18n="sys2_b4">Establish lightweight async-first operating rhythms</li>',
    '<span class="phase-period">Ongoing</span>': '<span class="phase-period" data-i18n="sys_w3">Ongoing</span>',
    '<span class="phase-tag">Scale</span>': '<span class="phase-tag" data-i18n="sys_t3">Scale</span>',
    '<div class="phase-name">Phase 3: Scale</div>': '<div class="phase-name" data-i18n="sys_n3">Phase 3: Scale</div>',
    '<div class="phase-goal">Make execution consistent and independent.</div>': '<div class="phase-goal" data-i18n="sys_g3">Make execution consistent and independent.</div>',
    '<li>Optimize CEO/founder time as a strategic resource</li>': '<li data-i18n="sys3_b1">Optimize CEO/founder time as a strategic resource</li>',
    '<li>Remove myself as a bottleneck through systems</li>': '<li data-i18n="sys3_b2">Remove myself as a bottleneck through systems</li>',
    '<li>Identify patterns and turn them into SOPs</li>': '<li data-i18n="sys3_b3">Identify patterns and turn them into SOPs</li>',
    '<li>Ensure operations run without constant supervision</li>': '<li data-i18n="sys3_b4">Ensure operations run without constant supervision</li>',

    # 06 TOOLS
    '<div class="section-tag reveal">06 · Tool Stack</div>': '<div class="section-tag reveal" data-i18n="tool_tag">06 · Tool Stack</div>',
    '<h2 class="section-title reveal">Tools I use<br>to run operations.</h2>': '<h2 class="section-title reveal" data-i18n="tool_title">Tools I use<br>to run operations.</h2>',
    '<div class="tool-desc">Calendar, Gmail, Docs, Sheets. I use it to create shared visibility and control execution flow — not just manage communication.</div>': '<div class="tool-desc" data-i18n="tool1_d">Calendar, Gmail, Docs, Sheets. I use it to create shared visibility and control execution flow — not just manage communication.</div>',
    '<div class="tool-desc">Wikis, SOPs, and tracking systems. I design structures teams can navigate without asking — reducing dependency and increasing clarity.</div>': '<div class="tool-desc" data-i18n="tool2_d">Wikis, SOPs, and tracking systems. I design structures teams can navigate without asking — reducing dependency and increasing clarity.</div>',
    '<div class="tool-desc">Advanced level. Dashboards, reconciliations, and operational reporting — turning raw data into decision-ready insights.</div>': '<div class="tool-desc" data-i18n="tool3_d">Advanced level. Dashboards, reconciliations, and operational reporting — turning raw data into decision-ready insights.</div>',
    '<div class="tool-desc">Pipeline and stakeholder management. Used to structure communication, automate follow-ups, and maintain accountability across partners.</div>': '<div class="tool-desc" data-i18n="tool4_d">Pipeline and stakeholder management. Used to structure communication, automate follow-ups, and maintain accountability across partners.</div>',
    '<div class="tool-desc">ChatGPT, Gemini, Claude, Perplexity. Used daily for research synthesis, structured thinking, and workflow acceleration — not as a shortcut, but as leverage.</div>': '<div class="tool-desc" data-i18n="tool5_d">ChatGPT, Gemini, Claude, Perplexity. Used daily for research synthesis, structured thinking, and workflow acceleration — not as a shortcut, but as leverage.</div>',
    '<div class="tool-desc">Asana, ClickUp, or equivalent. I adapt to existing systems and optimize execution flow — ensuring tasks translate into outcomes, not just activity.</div>': '<div class="tool-desc" data-i18n="tool6_d">Asana, ClickUp, or equivalent. I adapt to existing systems and optimize execution flow — ensuring tasks translate into outcomes, not just activity.</div>',
    '<p class="tools-note reveal">Tools don\'t solve operations — systems do. These are the ones I use to build them.</p>': '<p class="tools-note reveal" data-i18n="tool_note">Tools don\'t solve operations — systems do. These are the ones I use to build them.</p>',

    # 07 CLOSING
    '<div class="section-tag reveal">07 · Closing Position</div>': '<div class="section-tag reveal" data-i18n="close_tag">07 · Closing Position</div>',
    '<h2 class="closing-big reveal">Execution is where<br>most companies break.<br><em style="color:var(--gold)">That\'s where I operate.</em></h2>': '<h2 class="closing-big reveal" data-i18n="close_title">Execution is where<br>most companies break.<br><em style="color:var(--gold)">That\'s where I operate.</em></h2>',
    '<p class="closing-body reveal">I\'m not here to manage tasks or protect a calendar. I\'m here to make sure priorities move, decisions land, and nothing critical gets lost between intent and execution.</p>': '<p class="closing-body reveal" data-i18n="close_b1">I\'m not here to manage tasks or protect a calendar. I\'m here to make sure priorities move, decisions land, and nothing critical gets lost between intent and execution.</p>',
    '<p class="closing-italic reveal">Across logistics, government operations, and startup environments, I\'ve learned to see what matters, structure what doesn\'t, and execute without friction.</p>': '<p class="closing-italic reveal" data-i18n="close_b2">Across logistics, government operations, and startup environments, I\'ve learned to see what matters, structure what doesn\'t, and execute without friction.</p>',
    '<p>"The dark moments of our life are not to be forgotten — they are the memory that reminds us the human spirit is relentless, and capable of overcoming the intolerable."</p>': '<p data-i18n="close_q">"The dark moments of our life are not to be forgotten — they are the memory that reminds us the human spirit is relentless, and capable of overcoming the intolerable."</p>',
    '<div class="cta-heading">Let\'s talk.</div>': '<div class="cta-heading" data-i18n="cta_h">Let\'s talk.</div>',
    '<p class="cta-note">If you need someone who thinks like an operator and acts like a partner — we should talk.</p>': '<p class="cta-note" data-i18n="cta_n">If you need someone who thinks like an operator and acts like a partner — we should talk.</p>',

    # Footer
    '<p>Jesús Manuel Moncada-Depablos · Operations Lead · 2026</p>': '<p data-i18n="foot_1">Jesús Manuel Moncada-Depablos · Operations Lead · 2026</p>',
    '<span>Medellín, Colombia · Remote-Ready</span>': '<span data-i18n="foot_2">Medellín, Colombia · Remote-Ready</span>'
}

for k, v in replacements.items():
    if k not in html:
        print(f"NOT FOUND: {k}")
    html = html.replace(k, v)

html = html.replace('<script src="script.js" defer></script>', '<script src="translations.js"></script>\n<script src="script.js" defer></script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
