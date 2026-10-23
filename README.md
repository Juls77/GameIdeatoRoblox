# GameIdeatoRoblox – Claude-Code-Skill `roblox-game-architect`

Macht aus einer (auch groben) Spielidee ein durchgeplantes, auf Roblox zugeschnittenes Spielkonzept. Dazu gehören ein ehrlicher Reality-Check mit Score und gegebenenfalls Pivots sowie ein Plan mit 15 Abschnitten: Core Loop, Economy, die ersten 10 Minuten, Retention, Monetarisierung mit Robux-Preisen, LiveOps, KPIs, Technik und Roadmap.

## Installation
```bash
cp -r roblox-game-architect ~/.claude/skills/
```
Danach in Claude Code einfach eine Roblox-Idee beschreiben, z. B. „Ich will ein Roblox-Spiel über …“.

## Struktur
```
roblox-game-architect/
├── SKILL.md                      # Workflow, Qualitätsregeln, Selbstprüfung, Ausgabeformat
├── scripts/economy_sim.py        # Prüft Upgrade-Kurven gegen Zeitziele
├── evals/                        # 3 Testfälle mit Prüfkriterien (claude plugin eval)
└── references/
    ├── platform-algorithm.md     # Discovery/RFY 2025→2026, Benchmarks, KPI-Diagnose
    ├── audiences.md              # Altersgruppen, Kids/Select-Konten, Labels, Geräte
    ├── core-loops.md             # 10 Loop-Muster, Economy, Rebirth, Inflation
    ├── onboarding-ftue.md        # Erste 30 Sek / 2 Min / 10 Min
    ├── retention.md              # D1 / D2–7 / D8–30, Events, Update-Kadenz
    ├── monetization.md           # Passes, Products, Creator Rewards, DevEx, Richtlinien
    ├── virality-social.md        # Clip-Momente, Creator, Icon/Thumbnail/Titel
    ├── genre-playbooks.md        # 12 Genres
    ├── case-studies.md           # 15 Top-Spiele nach einheitlichem Schema
    ├── technical-constraints.md  # Mobile, DataStore, Anti-Exploit, Team-Scope
    └── plan-template.md          # Vorlage mit 15 Abschnitten
examples/                         # 3 Test-Outputs + Testbericht
```

Recherchestand: Oktober 2026. Belegte Zahlen tragen Quelle und Datum, alle anderen Werte sind als Schätzung oder Erfahrungswert markiert.
