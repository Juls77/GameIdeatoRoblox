# Testbericht roblox-game-architect

Getestet am 23.10.2026 mit drei bewusst unterschiedlichen Ideen. Die Prompts und Prüfkriterien liegen in `roblox-game-architect/evals/` und können mit `claude plugin eval` erneut ausgeführt werden. Die Läufe wurden inline ausgeführt (der Skill-Autor hat den Skill selbst angewendet), nicht von unabhängigen Subagenten, und es gab keinen Vergleichslauf ohne Skill.

| Test | Idee | Score im Reality-Check | Prüfkriterien erfüllt |
|---|---|---|---|
| 1 | Architektur-Tycoon (2 Personen) | 6,5/10, kein Pivot, aber 3 harte Anpassungen | 6/6 |
| 2 | Horror-Coop in der Schule (Solo) | 6/10, mit Unique Hook „lernender Hausmeister“ | 6/6 |
| 3 | Realistischer Steuer-Simulator (schwach) | 2/10 → 3 Pivots, Plan für „Paper Panic“ | 5/5 |

## Gefundene Schwächen (Iteration 1) und Verbesserungen

| Befund | Wo | Verbesserung im Skill |
|---|---|---|
| Ökonomie-Zahlen widersprachen sich: Kostenkurve r=1,18 ergab ~5 h bis zum Rebirth, im Text standen 60–90 Min | Test 1 | Neues Script `scripts/economy_sim.py` und Pflicht-Selbstprüfung (Schritt 5) in SKILL.md: Kurve, FTUE-Zeitmarken und Rebirth-Zeit müssen zusammenpassen |
| Ein Revive-Kauf wurde direkt nach dem Tod angeboten, obwohl die eigene Richtlinie „keine Angebote nach Misserfolg“ verlangt | Test 2 | `monetization.md` regelt Revives jetzt genauer: nur passiv, kein Popup oder Countdown, max. 1x pro Run, Gratis-Alternative; bei Zielgruppe unter 13 weglassen |
| Der Pivot-Plan war in LiveOps und Roadmap nur Fließtext und dadurch weniger umsetzbar | Test 3 | SKILL.md: Pivot-Pläne brauchen denselben Standard (alle 15 Abschnitte, Tabellen); sie dürfen kürzer, aber nicht vager sein |

Iteration 2 hat die drei Beispiel-Outputs mit den verbesserten Regeln nachgezogen. Die Zahlen in Test 1 stammen jetzt aus der Simulation.

## Bekannte Grenzen
- Plattformregeln ändern sich schnell: Der Algorithmus wurde 2025 und 2026 umgebaut, die Regeln zu bezahlten Zufallsitems im Mai 2026. Die Referenzen sollten etwa alle 3–6 Monate aktualisiert werden.
- Öffentliche Genre-Benchmarks (ARPDAU, D1 pro Genre) gibt es kaum. Der Skill kennzeichnet solche Werte als Schätzung.
- Einige Angaben sind ausdrücklich als „zu prüfen“ markiert, z. B. die Altersgrenzen für Rewarded Ads, das DevEx-Minimum und die maximale Servergröße.
