# Plan-Vorlage

Fülle alle 15 Abschnitte. Leitfragen in *kursiv* sind für dich, nicht für den Output. Jede Entscheidung bekommt eine kurze Begründung (Benchmark, Plattform-Mechanik oder Referenzspiel). Zahlen: belegte Benchmarks mit Quelle, eigene Werte als „Schätzung“/„Zielwert“.

---

## 1. Pitch & Hook
- **Pitch (1 Satz):** „[Titel] ist ein [Genre], in dem du [Kernaktion], um [Ziel] – [Twist].“
- **Klick-Hook:** Warum klickt jemand im Feed drauf? (Bild + Titel-Versprechen)
- **Erzähl-Hook:** Was erzählt der Spieler am nächsten Tag seinen Freunden / welcher Moment landet auf TikTok?

## 2. Zielgruppe
| | |
|---|---|
| Kernalter | |
| Sekundär | |
| Motivation (Top 3) | |
| Geräte | Mobile-first (≈80 % Aktivität) … |
| Content-Maturity-Label (Ziel) | + Folge: sichtbar für Roblox Kids / Select / Standard? |
| Design-Anpassungen daraus | Textmenge, Session-Länge, PvP ja/nein, Zufallsmechaniken, Kommunikation |

## 3. Referenzspiele
| Spiel | Was wir übernehmen | Was wir bewusst anders machen |
|---|---|---|
3–5 Zeilen.

## 4. Core Game Loop
Tabelle Mikro / Kern / Session / Täglich / Langfristig + Mermaid-Diagramm (Vorlage in `core-loops.md`).

## 5. Progression & Economy
- Währungen (Name, Quelle, Senke)
- Upgrade-Kurven mit Formel und 3–5 Beispielwerten (Stufe 1, 5, 10, 25 …) und Zeit pro Upgrade
- Zonen/Meilensteine mit Kosten
- Rebirth/Prestige: wann, Kosten, Belohnung
- Endgame (≥ 2 Systeme)
- Inflationsschutz (Sinks, Limits, Anti-Dupe)

## 6. Die ersten 10 Minuten
Tabelle mit Zeitmarken: **0:00–0:10, 0:10–0:30, 0:30–1:00, 1–2, 2–3, 3–5, 5–8, 8–10** → *Was sieht der Spieler · Was tut er · Was bekommt er · Was wird freigeschaltet*. Danach: Session-Ende-Hook (was er beim Verlassen sieht), Fehler, die wir explizit vermeiden.

## 7. Retention-Systeme
| Fenster | Mechanik | Konkrete Ausgestaltung (Zahlen) | Referenz |
|---|---|---|---|
| D1 | | | |
| D2–7 | | | |
| D8–30 | | | |

## 8. Social & Viralität
- Multiplayer-Interaktion (wie, wie oft, ohne Chat-Abhängigkeit)
- Einladen (Prompt, Belohnung, Bedingung)
- Trading (ja/nein, Schutzmechanismen)
- **Mind. 3 Clip-Momente** (was passiert, warum teilbar, in ≤ 15 Sek verständlich)
- Creator-Tauglichkeit (Challenges, Codes, Creator-Server)

## 9. Monetarisierung
Tabelle: Produkt · Typ (Pass/Product/Abo) · Preis R$ · Nutzen · Begründung · Wann/Wo angeboten.
Dann: Creator Rewards (früher Premium Payouts) – relevant? · Rewarded Ads – ja/nein + Altersgrenze · Regional Pricing an · **Bewusst NICHT verkauft** (mit Begründung) · Richtlinien-Check (Odds, Timer, Rabatte, PolicyService) · Umsatz-Szenario nur mit offengelegten Annahmen.

## 10. LiveOps & Update-Plan
- Launch-Inhalt (genau: Zonen, Items, Systeme)
- Woche 1–8 Tabelle: Woche · Update · Ziel-KPI (welches Problem löst es)
- 3–5 Event-Ideen mit Mechanik
- Fester Update-Tag/-Uhrzeit

## 11. Icon, Thumbnail, Titel
- 3 Titelvorschläge (mit Begründung, Favorit markieren)
- Icon-Beschreibung (Motiv, Farben, Emotion)
- 3–4 Thumbnail-Varianten für Personalisierung (je Hook)
- Beschreibungstext (erste Zeile + Bullets)

## 12. KPI-Ziele
| KPI | Benchmark (Quelle) | Ziel Soft-Launch | Ziel Launch | Wenn schlechter → Maßnahme |
|---|---|---|---|---|
D1, D7, D30, Session-Länge, Sessions/Tag, PTR/Bounce (relativ zu Peer-Benchmark), Payer-Conversion, ARPPU, FTUE-Funnel-Abbruch.

## 13. Technische Umsetzung
- Module/Services-Liste (siehe `technical-constraints.md`)
- DataStore-Schema (Lua-Tabelle)
- Mobile-Optimierung (konkret für dieses Spiel)
- Anti-Exploit (die 3–5 kritischsten Remotes und wie validiert)
- Server-Größe, Places, Teleports

## 14. Roadmap
- **MVP** (was genau, Aufwand in Personentagen/Wochen)
- **Soft Launch** (Ziel-KPIs als Gate für nächste Phase, Dauer)
- **Launch** (Marketing-Aktionen)
- Feature-Liste MoSCoW: Must / Should / Could / Won't (jetzt) – mit Aufwand S/M/L

## 15. Risiken & Unsicherheiten
| Risiko | Wahrscheinlichkeit | Auswirkung | Gegenmaßnahme / Früherkennung |
|---|---|---|---|
Mindestens: Hook trägt nicht (PTR), Retention, Konkurrenz/Klone, Scope, Richtlinien/Label, Exploits. Abschließend: **größte offene Annahme**, die als Erstes getestet werden muss.
