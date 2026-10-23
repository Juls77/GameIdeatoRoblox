# Retention-Systeme (D1, D7, D30)

Seit 2026 misst der RFY-Algorithmus Retention über **Day 1, Day 2–7 und Day 8–28** **[Q: DevForum RFY-Update, Juni 2026]** → ein Plan braucht Mechaniken für *alle drei* Fenster. Median-Benchmarks großer Spiele: D1 10,3 %, D7 1,6 %, D30 0,5 % **[Q: GameAnalytics 2026 Roblox Report]**.

Mechanik-Wirksamkeit ist meist **[Erfahrungswert]**; wo es Roblox-Daten gibt, sind sie markiert.

## D1 – „Warum morgen wiederkommen?“
| Mechanik | Wie konkret | Referenz |
|---|---|---|
| Offline-Fortschritt / Timer | Pflanzen wachsen weiter, Tycoon produziert offline (gedeckelt, z. B. max. 8 h) | Grow a Garden |
| Shop-Restock | Seltene Items rotieren alle X Min/Stunden → „vielleicht ist heute der seltene dabei“ | Grow a Garden (~5 Min) |
| Daily Reward mit Vorschau | Kalender 7 Tage, Tag 7 = großer Reward, **morgiger Reward sichtbar** | Viele Simulatoren |
| Unfertiges Ziel | Session endet mit fast vollem Balken („92 % bis Zone 3“) | Allgemein |
| Experience Notifications | Opt-in-Push: „Deine Ernte ist reif 🌻“ – nur für 13+ und erst ab 100 Visits verfügbar **[Q: Roblox Creator Docs „Experience notifications“]** | Grow-/Idle-Spiele |
| Freunde | Erste Koop-Erfahrung am Tag 1 → Spieler kommt mit Freund zurück | 99 Nights |

**Fairness-Regel (Kinder):** Daily Streaks dürfen nicht hart bestrafen. Verpasster Tag = Streak pausiert oder fällt um 1 Stufe, nicht auf 0 zurück; kein „Streak retten für Robux“ bei Zielgruppe < 13 (Verlustangst ist eines der in Studien kritisierten Muster **[Q: USENIX SOUPS 2025 „How Predatory Monetization Designs Manifest…“; ACM CHI 2025]**).

## D2–7 – „Ich habe ein Wochenprojekt“
| Mechanik | Wie konkret |
|---|---|
| Wöchentliche Quests / Missionen | 5–7 Aufgaben, die in 3–4 Sessions schaffbar sind, Reward = Event-Währung oder Kosmetik |
| Sammel-Index | „23/60 Pets entdeckt“, Belohnung bei 25 %, 50 %, 75 %, 100 % |
| Erster Rebirth | Ende Woche 1 realistisch erreichbar |
| Wöchentliches Update | Neue Pets/Samen/Map-Teil zu festem Wochentag+Uhrzeit (Ritual) – Grow a Garden-Spikes entstanden, als Millionen gleichzeitig zu Updates einloggten **[Q: Dexerto, 2025]** |
| Wochen-Leaderboard | Reset jeden Montag, Top-100 bekommen Titel/Rahmen |
| Gruppe/Clan beitreten | Roblox-Gruppen-Bonus (z. B. +10 % Coins) – nur kleiner Bonus, kein Zwang |

## D8–28 / D30 – „Ich gehöre hierher“
| Mechanik | Wie konkret |
|---|---|
| Trading | Mit Schutz: Trade-Lizenz/Freischaltung, Wertwarnung, Trade-Historie (wie Adopt Me! **[Q: Wikipedia Adopt Me!]**) |
| Saison/Events (2–6 Wochen) | Event-Währung, limitierte Kosmetik, Event-Pass (TDS: Battle Pass 499 R$, Fortschritt auch gratis **[Q: Sportskeeda TDS, 2024]**) |
| Endgame-Ziele | Seltene Mutationen, Prestige-Stufen, Boss-Raids |
| Identität/Status | Titel, Aura, Basis-Design, Rebirth-Zahl sichtbar |
| Social Graph | Freundesliste im Spiel, Koop-Bonus, gemeinsame Basis/Insel |
| Content-Kadenz | Großes Update alle 2–4 Wochen; Blox Fruits verliert laut Drittanalyse Spieler an Konkurrenz mit wöchentlichen Updates (2–3-Monats-Zyklus) **[Q: rowatcher „Blox Fruits vs Sailor Piece“, 2026 – Einzelquelle]** |

## Event-Typen (LiveOps-Baukasten)
| Typ | Dauer | Aufwand | Effekt |
|---|---|---|---|
| Admin-Abuse / Live-Event (Entwickler spielt live, spawnt Effekte) | 30–60 Min | gering | Hoher CCU-Peak, Clips; Grow a Garden & Steal a Brainrot nutzen solche Events **[Erfahrungswert]** |
| Wetter/Server-Event (zufällig, serverweit) | 5–15 Min | gering | Kurzfristige Aufregung, Gesprächsstoff |
| Wochenend-Boost (2x Coins) | 48 h | sehr gering | Wochenend-Peaks verstärken |
| Saison-Event (Halloween, Winter, Sommer) | 2–4 Wochen | hoch | Rückkehrer, Event-Pass |
| Collab/Brand | 1–3 Wochen | hoch, Partner nötig | Dress to Impress: Charli XCX (Aug 2024), Lady Gaga (Aug 2025), Wicked (Nov 2025) **[Q: rowatcher DTI-Artikel]** |
| Limitierte Items | Event-Dauer | mittel | Langfristiger Trading-Wert (Adopt Me! Halloween-/Winter-Pets **[Q: Adopt Me Fandom]**) |

## Update-Kadenz (Empfehlung, [Erfahrungswert])
- **Launch–Woche 8:** wöchentlich ein kleines Update (fester Tag, z. B. Samstag 17:00 MEZ / 11:00 EST – Zeit, wenn Schüler in EU+US frei haben).
- Alle 2–4 Wochen ein „großes“ Update mit neuem System/Zone.
- Countdown im Spiel zum nächsten Update (echter Countdown – nicht zurückspringend, siehe Richtlinien in `monetization.md`).
- Update-Log im Spiel (Icon-basiert) + Titel-Tag `[UPDATE 🌋]` im Spielnamen (gängige Praxis, siehe Fisch-Titel wie „Fisch 🐟 [CHAPEL]“ **[Q: rowatcher Fisch]**).

## Social Hooks
- **Invite-Prompt** (`SocialService:PromptGameInvite`): Spiele mit In-Experience-Invite-Prompts haben laut Roblox **6x mehr einladende User und 8x mehr Invites** **[Q: DevForum „Player Invite Prompts“, Roblox]**. Belohnung für Einladen nur, wenn der Freund *spielt* (nicht nur klickt) – und keine irreführenden Invite-Texte.
- **Koop-Bonus:** +X % wenn Freund im Server (fördert Co-Play-Signal).
- **Gemeinsame Ziele:** Server-weites Event-Ziel („Alle zusammen 1 Mio Äpfel → Boss erscheint“).

## Anti-Patterns
- FOMO-Druck bei Kindern (harte Streak-Resets, „nur noch 2 Min!“ mit Fake-Timer).
- Pflicht-Login-Grind (Spieler muss täglich 30 Min spielen, um nicht zurückzufallen).
- Events, die nur Zahlende abschließen können.
- Updates ohne Ankündigung (verschenkt den Rückkehr-Peak).

## Quellen
- DevForum RFY 2026: https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575
- GameAnalytics 2026: https://www.gameanalytics.com/reports/2026-roblox-report
- Creator Docs – Experience notifications: https://create.roblox.com/docs/production/promotion/experience-notifications
- DevForum – Player Invite Prompts: https://devforum.roblox.com/t/player-invite-prompts/2170724
- Dexerto – Grow a Garden Rekord: https://www.dexerto.com/roblox/roblox-game-grow-a-garden-suddenly-shatters-several-all-time-player-count-records-3196238/
- Wikipedia – Adopt Me!: https://en.wikipedia.org/wiki/Adopt_Me!
- Sportskeeda – TDS Event Pass: https://sportskeeda.com/roblox-news/tower-defense-simulator-hexscape-event-pass-all-rewards-premium-price
- rowatcher – Blox Fruits vs Sailor Piece: https://rowatcher.com/news/blox-fruits-vs-sailor-piece-which-anime-rpg-is-actually-growing-faster-in-2026
- rowatcher – Dress to Impress: https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits
- USENIX SOUPS 2025: https://www.usenix.org/system/files/soups2025-song.pdf
- ACM CHI 2025: https://dl.acm.org/doi/10.1145/3706598.3713170
