# Plattform & Algorithmus: Discovery, Signale, Benchmarks

Stand der Recherche: Oktober 2026. Kennzeichnung: **[Q: Quelle, Datum]** = belegte Zahl; **[Schätzung]** / **[Erfahrungswert]** = nicht öffentlich belegt.

## Inhalt
1. Wie Spieler ein Spiel finden (Oberflächen)
2. Recommended For You (RFY) – Entwicklung der Signale
3. Was daraus fürs Design folgt
4. Benchmarks (Retention, Session, Monetarisierung)
5. KPI-Diagnose: Wenn ein Wert schlecht ist
6. Quellen

---

## 1. Discovery-Oberflächen

| Oberfläche | Funktion | Hebel für Entwickler |
|---|---|---|
| Home → **Recommended For You** (RFY) | Personalisierte Empfehlung, größter organischer Traffic-Treiber | Retention, Play-Through-Rate, Bounce-Rate, Spend (siehe 2.) |
| Home → Sorts (z. B. Trending, Up-and-Coming) | Kurzfristige Momentum-Listen | Spitzen durch Updates/Creator-Videos; Dead Rails kam so auf Home **[Q: GameAnalytics Blog „Dead Rails and the hit makers formula“, 2025]** |
| Suche | Spieler suchen nach Genre/Trendbegriffen | Titel + Beschreibung mit Genre-Keywords („Tycoon“, „Obby“, „Simulator“) **[Erfahrungswert]** |
| Freunde („Friends are playing“, Join) | Social Graph | Koop-Anreize, Invite-Prompts |
| **Moments** (Kurzvideo-Feed) | Spieler clippen Gameplay, Zuschauer joinen direkt | Clip-würdige Momente designen. Beta seit RDC 2025, in den USA voll verfügbar seit RDC 2026 **[Q: Roblox Newsroom RDC 2025, Sept 2025; RDC 2026, Sept 2026]** |
| Externe Social Media (TikTok/YouTube) | Größter Viralitätshebel außerhalb Roblox | siehe `virality-social.md` |
| Sponsored Ads / Ads Manager | Bezahlte Reichweite | Nur sinnvoll, wenn Retention schon solide ist (Ads verstärken, sie reparieren nichts) **[Erfahrungswert]** |

Ab Ende 2026 kommen Browser-Play (Chrome) und perspektivisch Standalone-Apps hinzu **[Q: Roblox Newsroom „RDC 2026: The World Needs More Play“, Sept 2026]** – relevant, weil der Einstieg reibungsloser wird und die ersten 30 Sekunden noch wichtiger werden.

## 2. Recommended For You – Signale

### Version Dezember 2025 (7-Tage-Fenster)
**[Q: DevForum „Boost Your Discovery with the Improved Recommended For You Algorithm and Analytics for Creators“, global ausgerollt Dez 2025]**
- Qualified Play-Through Rate (qPTR) – Anteil der Impressions, die zu einem „qualifizierten“ Spiel führen
- 7-Tage-Play-Days und Playtime pro User – **Playtime gedeckelt auf max. 60 Min pro User, pro Spiel, pro Tag**
- Spend-Signale (Spend Days, Robux pro User)
- **Intentional Co-Play Days** – neu, weil „Nutzer mit höherer Spielfrequenz, Spend und Interaktion mit Freunden eine höhere Wahrscheinlichkeit langfristiger Retention haben“
- D1/D7-Retention
- Neuer Analytics-Tab „Home Recommendations“

### Version 2026 (28-Tage-Fenster) – aktuell
**[Q: DevForum „Recommended For You Algorithm Improvements That Better Value Long-Term Retention“, ca. 15. Juni 2026 laut Dubit; Roblox Creator Docs „Discovery“, abgerufen Okt 2026]**
- Retention wird über **Day 1, Day 2–7 und Day 8–28** gemessen (statt nur 7 Tage)
- **qPTR entfernt**, ersetzt durch **Play-Through Rate (PTR)** und **First Play Bounce Rate** – Klickverhalten und Session-Qualität werden getrennt gemessen. Hohe Bounce-Rate ist ein negatives Signal **[Q: Dubit „What makes a new Roblox game take off?“, 2026]**
- Docs-Priorisierung: PTR und First-Play-Bounce-Rate „Most important“; Spend Days und Robux pro User „Important“
- **Signale zählen nur User, die organisch über RFY kamen**
- **Signale sind Durchschnitte pro User, keine Summen** – kleine Spiele mit engagierten Spielern sind nicht benachteiligt

> Hinweis: Mehrere Drittseiten widersprechen sich bei Details. Maßgeblich sind DevForum + Creator Docs. Vor einem Launch kurz prüfen, ob sich wieder etwas geändert hat (2025 und 2026 je ein großer Umbau).

## 3. Was daraus fürs Design folgt

| Signal | Design-Konsequenz |
|---|---|
| PTR (Klick → Spielen) | Icon/Thumbnail/Titel müssen Versprechen *und* Genre sofort zeigen; Thumbnail-Personalisierung nutzen (≥ 2 Thumbnails) |
| First Play Bounce Rate | Die ersten 30–60 Sek entscheiden. Kein Ladebildschirm-Menü, kein Textwall, sofortige Aktion (siehe `onboarding-ftue.md`) |
| D1 / D2–7 / D8–28 | Gründe für Rückkehr am nächsten Tag (Timer, Daily, Restock) **und** in Woche 2–4 (Sammelziele, Events, Rebirth-Meta, soziale Bindung) |
| Playtime-Cap 60 Min/Tag (Version 2025) | Endlos-Sessions bringen über 60 Min/Tag kein zusätzliches Signal → lieber **mehrere Sessions pro Tag** designen (Restock, Offline-Ertrag) |
| Co-Play | Mechaniken, die Freunde *absichtlich* zusammen spielen lassen (Koop-Ziele, Trading, gemeinsame Basis) |
| Spend Days | Viele kleine, faire Kaufanlässe > ein teurer Pass; Kauf soll an mehreren Tagen sinnvoll sein |

## 4. Benchmarks

### Retention (große Spiele, 1M+ MAU)
**[Q: GameAnalytics „2026 Roblox Benchmark Report“, Daten Aug 2025 – Jul 2026, 500+ Titel mit 1M+ MAU]**

| Metrik | p25 | Median | p99 |
|---|---|---|---|
| D1 | 8,4 % | 10,3 % | 22,2 % |
| D7 | 1,0 % | 1,6 % | 9,1 % |
| D30 | 0,3 % | 0,5 % | 4,7 % |

Wichtig: GameAnalytics hält die oft zitierten „20 % D1 = gut, 40 % = exzellent“ für **inflationiert**, weil diese Werte meist aus kleinen Stichproben bereits beworbener Spiele stammen **[Q: GameAnalytics 2026 Report]**. Genre-Seiten wie BLOXG (850+ beworbene Spiele) nennen D1 ≥ 20 % „gut“, ≥ 30 % „stark“ **[Q: bloxg.com Retention Benchmarks, 2026]** – nicht direkt vergleichbar (Selektionsbias, andere Messmethode). Roblox' eigene Analytics haben seit Okt 2025 Retention nach Akquisequelle und wählbare Benchmark-Sets **[Q: DevForum „Analytics: View retention by acquisition source and select your benchmark set“, Okt 2025]** → für eigene Ziele immer den Roblox-Peer-Benchmark im Dashboard heranziehen.

**Zielwerte für Pläne (Schätzung, abgeleitet):**

| | Warnsignal | Solide | Sehr gut |
|---|---|---|---|
| D1 (Roblox-Dashboard, organisch) | < 8 % | 10–15 % | > 20 % |
| D7 | < 1 % | 2–4 % | > 6 % |
| D30 | < 0,3 % | 0,5–1,5 % | > 3 % |

Achtung: Für einen **frischen Soft-Launch mit kleinem Publikum** sind Werte stark verrauscht; erst ab einigen tausend neuen Spielern pro Kohorte ernst nehmen **[Erfahrungswert]**.

### Session-Länge
- Median-Session 7,28 Min; p75 14,85 Min; p90 26,30 Min **[Q: GameAnalytics 2026 Report via gamedevreports Substack, 2026]**. Eine andere Darstellung desselben Reports nennt Median pro Spiel 9,8 Min, p90 14,7 Min – Session-Werte unter 10 Min sind bei großen Titeln normal.
- Reife-Leiter: **0–6 Min = fragil** (D1 < 10 %, ~1 Session/Tag, kaum ARPPU); **7–18 Min** = hält Aufmerksamkeit, aber nicht Frequenz; **19+ Min = Hits** mit zweistelligem D1 und ~2 Sessions/Tag. 25+ Min monetarisiert *nicht automatisch* besser als 19–24 Min **[Q: GameAnalytics „The 2025 Roblox Benchmark Report“, 2025]**.
- Durchschnittlicher Spieler öffnet Roblox ~3x täglich **[Q: GameAnalytics 2026]** → Spiele, die mehrere kurze Rückkehr-Anlässe bieten, passen zum Nutzungsmuster.

### Monetarisierung
**[Q: GameAnalytics 2026 Report, Aug 2025 – Jul 2026]**
- Nur **3,8 %** der getrackten Spieler zahlten im Zeitraum.
- ARPPU (Median pro Titel) **$0,70**; Top 10 % $2,33; Top 5 % $4,80; p99 $55,31.
- Definitionen: ARPPU = Umsatz / zahlende User; ARPDAU = Umsatz / DAU; Conversion = Anteil DAU mit Kauf am Tag **[Q: GameAnalytics Docs „Metrics“]**.

**Zielwerte für Pläne (Schätzung):** Payer-Conversion (kumuliert über 30 Tage) 2–5 % als realistisches Ziel; tägliche Conversion meist deutlich unter 1 %. ARPDAU stark genre-abhängig (Simulatoren/Pet-Games höher, Obbies/Roleplay niedriger) – immer mit dem Peer-Benchmark im Roblox-Dashboard vergleichen, da es keine verlässlichen öffentlichen Genre-ARPDAU-Zahlen gibt.

### Plattform-Größe
- 123 Mio DAU in Q2 2026 (+10 % YoY), 29 Mrd Stunden im Quartal **[Q: Roblox Q2 2026 Shareholder Letter, Juli 2026]**; Rekord-Quartal Q3 2025 mit ~151,5 Mio DAU (Viral-Hits Grow a Garden/Steal a Brainrot) **[Q: jitendra.co Stats-Zusammenfassung, 2026 – sekundär]**.

## 5. KPI-Diagnose: Wenn ein Wert schlecht ist

| Symptom | Wahrscheinliche Ursache | Konkrete Maßnahmen |
|---|---|---|
| Niedrige PTR (Klicks) | Thumbnail/Icon/Titel unklar oder generisch | 3–4 Thumbnail-Varianten in Personalisierung; Genre-Wort in Titel; Gesicht/Emotion + ein klares Objekt; Trend-Thema prüfen |
| Hohe First-Play-Bounce | FTUE langsam/verwirrend, Ladezeit, Thumbnail verspricht etwas anderes | Funnel-Events (siehe unten) auswerten, erste Aktion < 10 Sek, Ladezeit Mobile messen, Thumbnail ehrlich machen |
| D1 schlecht, Session ok | Kein Grund zurückzukommen | Offline-Ertrag/Timer, Daily Reward mit Vorschau „morgen: X“, unfertiges Ziel am Session-Ende sichtbar lassen |
| D1 ok, D7 bricht ein | Content zu schnell durch / Progression flacht ab | Mehr Meta-Ziele (Index, Rebirth), wöchentliches Update, Kurve prüfen |
| D7 ok, D30 schlecht | Kein Endgame/Social | Trading, Gilden/Koop, saisonale Events, Leaderboards |
| Session < 7 Min | Loop zu dünn oder frustrierend | Zweiten Loop-Layer früher freischalten, Mikro-Rewards verdichten |
| Conversion niedrig | Kein relevanter Kaufanlass oder schlechtes Timing | Starter Pack nach erstem Erfolg, Shop-Vorschau früh, Pass-Nutzen sichtbar machen (andere Spieler mit Pass) |
| ARPPU niedrig | Nur Billig-Items | Mittlere Preisstufe (399–799 R$) und Bundles ergänzen, Regional Pricing aktivieren |

**Funnel-Tracking:** Mit `AnalyticsService:LogOnboardingFunnelStepEvent` (Onboarding-Schritte) und `LogProgressionEvent`/`LogEconomyEvent` eigene Funnel bauen – so sieht man im Roblox-Dashboard, bei welchem Schritt neue Spieler abspringen **[Q: Roblox Creator Docs Analytics, Stand 2026 – API-Namen vor Verwendung prüfen]**.

## 6. Quellen
- Roblox Creator Docs – Discovery: https://create.roblox.com/docs/discovery
- DevForum – RFY Dez 2025: https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441
- DevForum – RFY 2026 (28 Tage): https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575
- Dubit – What makes a new Roblox game take off?: https://dubit.io/library/what-makes-a-new-roblox-game-take-off
- GameAnalytics 2026 Roblox Report: https://www.gameanalytics.com/reports/2026-roblox-report
- GameAnalytics 2025 Roblox Report: https://www.gameanalytics.com/reports/2025-roblox-report
- gamedevreports Substack – Zusammenfassung GA 2026: https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox
- DevForum – Retention nach Akquisequelle (Okt 2025): https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157
- BLOXG Retention Benchmarks: https://bloxg.com/statistics/roblox-retention-benchmarks
- Roblox Q2 2026 Shareholder Letter: https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Earnings-Shareholder-Letter.pdf
- GameAnalytics – Dead Rails: https://www.gameanalytics.com/blog/dead-rails-and-the-hit-makers-formula
- Roblox Newsroom RDC 2025: https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025
- Roblox Newsroom RDC 2026: https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play
