# Monetarisierung auf Roblox

Stand: Oktober 2026. **[Q: …]** belegt; **[Schätzung]/[Erfahrungswert]** = Praxis. Preisempfehlungen sind Startwerte zum Testen, keine belegten Optima.

## Inhalt
1. Einnahmequellen & Auszahlungslogik
2. Was verkauft sich: Game Passes vs. Developer Products
3. Preispunkte
4. Richtlinien & Kinderschutz (Pflichtteil jedes Plans)
5. Pay-to-Win: wo die Grenze liegt
6. Plan-Vorlage für den Monetarisierungsabschnitt
7. Quellen

---

## 1. Einnahmequellen

| Quelle | Mechanik | Zahlen |
|---|---|---|
| **Game Passes** | Einmalkauf, permanent | Creator erhält **70 %** der Robux beim Verkauf im eigenen Spiel **[Q: Roblox Creator Docs „Earning on Roblox“]** |
| **Developer Products** | Wiederholt kaufbar (Währung, Boosts, Skips) | gleiche Logik wie Passes; Kauf immer über `ProcessReceipt` abwickeln, nicht `PromptProductPurchaseFinished` **[Q: Creator Docs „Developer Products“]** |
| **Subscriptions** | Monatliches Abo mit wiederkehrendem Nutzen | Preisänderung max. alle 60 Tage, Erhöhung erst nach 30 Tagen Vorankündigung; nach Kauf keine Zusatzaufgaben verlangen (Battle Passes ausgenommen); nicht auf Kauf außerhalb Roblox verweisen **[Q: Creator Docs „Subscriptions“/„Monetization“]** |
| **Creator Rewards** (ersetzt seit 24.07.2025 die alten **Premium Payouts**/Engagement-Based Payouts) | **Daily Engagement:** 5 Robux, wenn ein *Active Spender* (≥ $9,99 Ausgaben in 60 Tagen) ≥ 10 Min am Tag im Spiel ist – nur für die ersten 3 Spiele, die er an dem Tag startet. **Audience Expansion:** 35 % der ersten $100 Käufe neuer/zurückkehrender User (60+ Tage inaktiv) in deren ersten 2 Monaten. 60 Tage Haltefrist **[Q: DevForum „Introducing Creator Rewards“, 2025]** | → **„Premium Payouts“ gibt es so nicht mehr.** Plan muss Creator Rewards nennen |
| **Rewarded Video Ads** | Opt-in, bis zu 30 Sek, Spieler erhält In-Game-Belohnung | Start April 2025 mit Google; ~100 Publisher bis Juli 2025 **[Q: Roblox Newsroom April 2025; Earnings Call Q2 2025]**; Studio-Plugin für Q4 2026 angekündigt **[Q: MediaPost/eMarketer 2026]**. Ads werden nach Roblox-Praxis nur an ältere Nutzer ausgespielt – Altersgrenzen vor Einbau im Creator Hub prüfen **[zu prüfen]** |
| **Private Server** | Monatlich, Robux | Wichtig bei Roleplay (Brookhaven) und Grind-Spielen |
| **Regional Pricing** | Roblox passt Preise lokal an (30–100 % des Basispreises) | Beispiel: 1.000 R$ US → 700 Brasilien, 500 Indien; Tests: Ausgaben +17 % Mexiko, +26 % Brasilien, +52 % Philippinen **[Q: Roblox Newsroom, April 2025; Creator Docs „Managed pricing“]** – immer aktivieren |
| **Price Optimization** | Roblox testet Preise automatisch | Median +4 % Einnahmen; Slap Battles „über 15 %“ **[Q: Roblox Newsroom, 2025]** |

### DevEx (Auszahlung in $)
- **$0,0038 pro Robux** seit 05.09.2025 (vorher $0,0035; ältere Robux werden zuerst zum alten Satz ausgezahlt) **[Q: Roblox, Sept 2025; Digiday RDC 2025]**.
- **+42 %** für Ausgaben von verifizierten US-Spielern 18+ in qualifizierten Spielen ab 08.06.2026 (effektiv 26,6 % → 37,8 % des Spend) **[Q: Roblox Newsroom, April 2026]**.
- Voraussetzungen: 13+, verifizierte E-Mail, Mindestbetrag (30.000 Robux laut mehreren 2025/26-Quellen; eine Verbraucherseite nennt 100.000 – im Creator Hub prüfen) **[Q: bloxodes / acs.org.au, widersprüchlich]**.
- Ab Ende 2026: Roblox Wallet mit USD-Auszahlung für berechtigte US-Creator 18+ **[Q: RDC 2026 Berichterstattung]**.

**Rechenbeispiel für Pläne:** 1 verkaufter 199-R$-Pass → 139 R$ an Creator → ≈ $0,53 nach DevEx (0,0038 $/R$).

## 2. Was verkauft sich?

### Game Passes (permanent) – typische Bestseller **[Erfahrungswert]**
1. **2x Währung / 2x XP** – Kernmultiplikator, leicht verständlich
2. **VIP** – Bündel aus Chat-Tag, VIP-Bereich, kleinem Boost, Kosmetik
3. **Komfort**: Auto-Collect, Auto-Sell, mehr Inventar/Pet-Slots, schnelleres Laufen/Teleport
4. **Kosmetik/Status**: Trails, Auren, Titel, exklusive Farben
5. **Zugang**: Private Server-Feature, Bereiche, Fahrzeuge (Roleplay)
6. **Notifier/Info-Pässe**: Blox Fruits „Fruit Notifier“ 2.700 R$ – gilt bei Spielern als Pay-to-Win **[Q: rowatcher, 2026]**

### Developer Products (wiederholt)
1. **Starter Pack** (einmalig limitiert als Product mit Kauf-Flag): großer Wert-Eindruck, niedriger Preis
2. **Währungspakete** (Staffelung mit Mengenbonus)
3. **Zeitlich begrenzte Boosts** (30 Min 2x Luck)
4. **Skips** (Stage-Skip im Obby, Timer-Skip) – bei Kindern sparsam
5. **Revive/Second Chance** (Horror/Survival) – nur, wenn Tod nicht künstlich herbeigeführt wird
6. **Server-weite Boosts / Gifts** („Kauf 2x Luck für den ganzen Server“) – sozial positiv, erzeugt Dank statt Neid

### Abos
Sinnvoll, wenn täglicher, wiederkehrender Nutzen existiert (tägliche Gems, Daily-Bonus-Kiste ohne Zufall, Event-Pass-Premium). Bei < 13-Zielgruppe zurückhaltend.

## 3. Preispunkte

Robux-Pakete (US, Web/Store, Drittquellen): **400 R$ ≈ $4,99 · 800 ≈ $9,99 · 1.700 ≈ $19,99 · 4.500 ≈ $49,99 · 10.000 ≈ $99,99**; 800 gilt als häufig gekauft **[Q: creation.dev, 2026 – sekundär, prüfen]**. Preise so legen, dass sie *in* ein Paket passen.

| Typ | Startpreis-Empfehlung | Begründung |
|---|---|---|
| Kleine Kosmetik / Trail | 49–99 R$ | Impulskauf, auch mit Restguthaben |
| 2x Coins / 2x XP Pass | 149–299 R$ | Kernnutzen, hohe Conversion |
| Komfort-Pass (Auto-Collect, +Slots) | 99–249 R$ | |
| VIP-Pass | 299–499 R$ | Bündel-Wert; PS99 VIP 1.299 R$ als Obergrenze-Beispiel eines Top-Spiels **[Q: creation.dev/rowatcher]** |
| Starter Pack (einmalig) | 49–149 R$ | Erster Kauf senkt Hemmschwelle für weitere **[Erfahrungswert]** |
| Währungspakete | 25 / 99 / 249 / 499 / 999 / 2.499 R$ mit +0 / +10 / +20 / +30 / +40 / +50 % Bonus | Staffelung |
| Event-/Battle-Pass | 299–499 R$ | TDS: 499 R$ **[Q: Sportskeeda 2024]** |
| Private Server | 0–200 R$/Monat | Roleplay/Grind: niedrig halten oder gratis |

Diese Bereiche decken sich mit einer Developer-Guide-Empfehlung (Kosmetik 25–75, Utility 49–149, Multiplikator 99–249, VIP 199–499 R$) **[Q: creation.dev „How to price game passes“ – ohne Verkaufsdaten]**. Nach Launch über Price Optimization testen.

## 4. Richtlinien & Kinderschutz (in jedem Plan berücksichtigen)

### Offizielle Roblox-Monetarisierungsrichtlinien **[Q: Roblox Creator Docs „Monetization“, Stand 2026]**
- Spieler dürfen **nicht getäuscht, verwirrt oder unter Druck gesetzt** werden zu kaufen.
- **Rabatt nicht echt**, wenn ein Item dauerhaft „im Angebot“ zum selben Preis ist. **Rabatt nicht fair**, wenn er nur sehr kurz angeboten wird, um zur Eile zu drängen.
- **Countdown-Timer** müssen korrekt sein und dürfen für dasselbe Item nicht automatisch neu starten.
- **Keine falsche Knappheit** („fast ausverkauft“, „nur kurz verfügbar“, wenn nicht wahr).
- **Zufallsmechaniken offenlegen.**
- Kein Verweis auf Käufe außerhalb Roblox.

### Bezahlte Zufallsitems (Lootboxen, Eggs für Robux, Gacha)
- **Odds pro Ergebnis numerisch vor dem Kauf anzeigen, Summe 100 %; jedes Ergebnis muss einen Nutzen haben (keine Nieten); bei verschachtelten Boxen Odds aller Endergebnisse** – global seit Mai 2026, angestoßen durch koreanische Regeln **[Q: DevForum „Clarifying Requirements for Paid Random Items“, Mai 2026; TechTimes Juni 2026]**.
- **Region-Gating via `PolicyService:GetPolicyInfoForPlayerAsync` → `ArePaidRandomItemsRestricted`**: UK unter 18 seit Aug 2024 **[Q: DevForum „Update on Paid Random Items Restriction for UK Users Under 18“]**; Brasilien unter 18 seit 17.03.2026 und unverifizierte Erwachsene seit 31.03.2026 **[Q: DevForum, 2026 – sekundär]**; Australien: Beschränkung für Minderjährige (Quellen widersprüchlich: unter 15 bzw. unter 18) **[Q: The Conversation 2025; ACM CHI 2025]**.
- Verstöße → Entfernung des Spiels, Account-Sperre möglich **[Q: zehn-studio26, 2026 – sekundär]**.
- Gratis verdiente Zufallsitems (Eggs für Soft Currency) sind weniger reguliert, aber Odds trotzdem anzeigen (Vertrauen, und weil Booster gegen Robux sie indirekt monetarisieren) **[Erfahrungswert]**.

### Kontext: öffentliche Kritik
- University of Sydney (Okt 2025–Feb 2026, 15 umsatzstärkste Spiele): **14 irreführende/unfaire Praktiken**, u. a. Fake-„Tagesrabatte“, aufgeblähte „Wert“-Preise, verschleierte Preise über virtuelle Währungen **[Q: University of Sydney, Mai 2026]**.
- Studien zu Dark Patterns bei Kindern: UI-Manipulation, Überforderung, versteckte Kaufinfos, Verlustangst, sozialer Druck **[Q: USENIX SOUPS 2025; ACM CHI 2025]**.
→ Ein Plan, der solche Muster nutzt, ist ethisch und regulatorisch riskant. Der Skill empfiehlt sie **nie**.

### Ethische Leitlinien des Skills (strenger als das Minimum)
| Tu | Lass |
|---|---|
| Robux-Preis überall direkt anzeigen | Preise nur in Gems zeigen, die man mit Robux kauft |
| Kaufangebote nach Erfolgsmomenten | Angebote direkt nach Tod/Verlust/Diebstahl („Rache-Pack!“) |
| Echte, angekündigte Event-Zeiträume | Fake-Timer, „letzte Chance“-Popups in Schleife |
| Free-Weg zu allem Gameplay-Relevanten | Stärkste PvP-Items nur gegen Robux |
| Bei < 13: keine bezahlten Zufallsitems | Robux-Eggs/Gacha für Kinder-Zielgruppe |
| Kauf-Prompt max. 1x pro Session ungefragt | Prompt-Spam, Prompts über dem Spielfeld |
| Server-Geschenke, Kosmetik, Komfort | Streak-Rettung für Robux, Energie-Systeme mit Bezahl-Refill bei Kindern |
| Revive/Second Chance (Horror, Survival) nur **passiv**: kleiner Button im Zuschauer-/Geist-Screen, kein Popup, kein Countdown, max. 1x pro Run, gleichwertige Gratis-Alternative (Mitspieler kann befreien) | Revive-Popup mit Timer im Moment des Todes, „Jetzt weitermachen oder alles verlieren!“, mehrfach kaufbar, Tod künstlich herbeigeführt |

**Abwägung Revives:** Kauf direkt nach Misserfolg ist genau das Muster, das Dark-Pattern-Studien kritisieren (Verlustangst) **[Q: USENIX SOUPS 2025]**. Gleichzeitig ist der Revive Genre-Standard (Doors). Deshalb nur die passive Form; bei einer Kernzielgruppe unter 13 lieber ganz weglassen und stattdessen Mitspieler-Revives stärken.

## 5. Pay-to-Win
- **PvP / Wettbewerb:** Nur Kosmetik + Komfort verkaufen. Stats-Vorteile zerstören Fairness, Community und Creator-Videos („P2W“-Rufe in Kommentaren).
- **PvE / Simulator:** Multiplikatoren akzeptiert (Zeitersparnis), solange Free-Spieler dasselbe erreichen. Faustregel: Ein zahlender Spieler ist ≤ 2–3x schneller, nicht 10x **[Erfahrungswert]**.
- **Steal-/Raid-Spiele:** Verteidigungs-Vorteile gegen Robux (längerer Lock, unbesiegbare Wände) machen Free-Spieler zur Beute → hoher Frust; lieber Kosmetik, Basis-Deko, Komfort.
- **Trading-Spiele:** Robux-Items, die direkt handelbar sind, schaffen Echtgeld-Märkte und Scam-Anreize → nur, wenn Trading stark abgesichert ist.

## 6. Plan-Vorlage (Abschnitt 9)
```
| Produkt | Typ | Preis (R$) | Nutzen | Warum dieser Preis | Wann angeboten |
|---|---|---|---|---|---|
| Starter Pack | Dev Product (1x) | 99 | 5.000 Coins + Pet + Trail | Wert-Eindruck, passt in 400er-Paket | nach erstem Meilenstein (~Min 8) |
...
Creator Rewards: [Einschätzung, ob Zielgruppe Active Spender enthält]
Rewarded Ads: [ja/nein, Platzierung, Altersgrenze]
Bewusst NICHT verkauft: [Liste + Begründung]
Umsatzerwartung: [nur als Szenario mit Annahmen, z. B. 3 % Payer, ARPPU-Bandbreite]
```

## 7. Quellen
- Creator Docs – Monetization: https://create.roblox.com/docs/production/monetization
- Creator Docs – Developer Products: https://create.roblox.com/docs/production/monetization/developer-products
- Creator Docs – Subscriptions: https://create.roblox.com/docs/production/monetization/subscriptions
- Creator Docs – Earning on Roblox: https://create.roblox.com/docs/en-us/production/earning-on-roblox
- Creator Docs – Managed pricing: https://create.roblox.com/docs/production/monetization/managed-pricing
- DevForum – Creator Rewards: https://devforum.roblox.com/t/introducing-creator-rewards-earn-more-by-growing-the-community/3777628
- DevForum – Paid Random Items (Mai 2026): https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622
- DevForum – UK Paid Random Items: https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-uk-users-under-18/3072183
- TechTimes – Korea Odds: https://www.techtimes.com/articles/319148/20260626/koreas-loot-box-rules-push-roblox-disclose-item-odds-worldwide.htm
- Roblox Newsroom – Regional Pricing: https://about.roblox.com/newsroom/2025/04/roblox-launches-regional-pricing-for-in-experience-items
- Roblox Newsroom – Rewarded Video: https://about.roblox.com/newsroom/2025/04/roblox-scales-video-ads-partners-with-google
- eMarketer – Rewarded video tools: https://www.emarketer.com/content/roblox-expands-rewarded-video-tools-creators-advertisers
- Roblox Newsroom – DevEx +42 %: https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42
- Digiday – RDC 2025: https://digiday.com/media/robloxs-growth-comes-with-growing-pains-between-creators-and-ad-sales/
- University of Sydney: https://www.sydney.edu.au/news-opinion/news/2026/05/17/inside-the-pay-to-play-world-of-roblox-targeting-children-.html
- The Conversation: https://theconversation.com/literally-just-child-gambling-what-kids-say-about-roblox-lootboxes-and-money-in-online-games-250387
- creation.dev – Game Pass Pricing: https://www.creation.dev/learn/how-to-price-game-passes-roblox
- Sportskeeda – TDS Pass: https://sportskeeda.com/roblox-news/tower-defense-simulator-hexscape-event-pass-all-rewards-premium-price
