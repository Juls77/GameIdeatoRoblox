# Onboarding / First-Time User Experience (FTUE)

Warum das zählt: Der RFY-Algorithmus bewertet seit 2026 die **First Play Bounce Rate** als eines der wichtigsten Signale **[Q: Roblox Creator Docs „Discovery“; DevForum RFY-Update, Juni 2026]**. Wer in der ersten Session abspringt, schadet direkt der Sichtbarkeit. Roblox selbst empfiehlt kurze Tutorials/Tooltips statt langer Tutorials und nennt Core Loop, FTUE und Performance als Hebel für D1 **[Q: Roblox Creator Docs „Retention“]**.

Zeitmarken unten sind **[Erfahrungswert]** bzw. Community-Faustregeln (BLOXG: „etwas Spaßiges innerhalb ~10 Sek, erster Reward innerhalb 60 Sek“ **[Q: bloxg.com Retention Guide]**; Spaceport: erste 10 Sek entscheidend, visuelle Hinweise statt Text **[Q: spaceport.xyz Blog]**). Keine dieser Zeitmarken ist durch eine öffentliche Studie belegt – sie sind konsistente Praxiswerte.

## Phase 0: Vor dem Spawn (Ladezeit)
- Mobile-Ladezeit messen; Ziel **< 10–15 Sek** bis spielbar **[Schätzung]**. Instance Streaming nutzen, Startbereich klein und leicht halten.
- **Kein Hauptmenü mit „Play“-Button**, keine Intro-Cutscene beim ersten Join. Jeder zusätzliche Klick vor dem Spielen kostet Spieler.
- Custom Loading Screen nur, wenn er Spiel-Fantasie zeigt und < 5 Sek dauert.

## Phase 1: Die ersten 30 Sekunden – „Ich verstehe, was ich tun soll“
| Sek | Ziel | Umsetzung |
|---|---|---|
| 0–3 | Orientierung | Spawn mit Blick auf das Kernobjekt (Baum, Dropper, erste Tür). Kamera nicht frei drehen lassen müssen. |
| 3–10 | Erste Aktion ohne Text | Leuchtender Pfeil/Beam + pulsierendes Objekt + Hand-Icon (Mobile: Tap-Animation). Aktion = 1 Tap. |
| 10–15 | Sofortiges Feedback | Partikel, Sound, Zahl fliegt ins HUD (+5 🪙). Kamera-Shake leicht. |
| 15–30 | Zweite/dritte Wiederholung, Zähler füllt sich | Fortschrittsbalken „5/10 → Upgrade“ sichtbar. |

Regel: **Zeigen, nicht erklären.** Max. 3–4 Wörter Text pro Hinweis („Tippe zum Ernten!“), für 6–9-Jährige besser nur Icons.

## Phase 2: Bis Minute 2 – „Ich werde stärker“
- **Erstes Upgrade** spätestens bei ~60 Sek, mit spürbarem Effekt (doppelt so schnell, sichtbar größeres Werkzeug).
- Pfeil führt zum Shop/Upgrade-Button; Button pulsiert, sobald bezahlbar.
- **Erster „Wow“-Moment**: etwas Seltenes/Großes passiert garantiert (erstes Pet schlüpft mit Animation, erster Raum öffnet sich, Basis wächst sichtbar).
- Kein Kauf-Prompt in dieser Phase.

## Phase 3: Bis Minute 10 – „Ich habe ein Ziel“
- **Ziel setzen**: nächste Zone/Meilenstein mit sichtbarem Tor („Zone 2: 1.000 🪙“) und Balken.
- **Zweiter Loop-Layer** freischalten (z. B. Pets, Rebirth-Vorschau, Koop-Run) – Spieler sieht, dass es mehr gibt.
- **Social-Signal**: andere Spieler sichtbar mit coolen Items (zeigt Langzeitziel und Shop-Wert), Freunde-einladen-Button einführen (nicht erzwingen).
- **Daily Reward / Offline-Ertrag** am Ende der ersten Session ankündigen: „Komm morgen wieder: 🎁 Tag 2“.
- **Shop sichtbar machen** (nicht pushen): Spieler entdeckt 2x-Pass/Starter-Pack von selbst. Erstes Angebot frühestens nach erstem Erfolgserlebnis (z. B. erster Meilenstein), nie direkt nach Tod/Fehlschlag.

## Unlock-Zeitplan (Vorlage)
| Zeit | Freigeschaltet |
|---|---|
| 0:00 | Kernaktion |
| 0:45–1:00 | Erstes Upgrade |
| 2:00 | Verkaufen / zweite Ressource |
| 3–5:00 | Zweite Zone oder erstes Pet/Item |
| 5–8:00 | Sekundärsystem (Quests, Index) |
| 8–10:00 | Ziel für morgen (Daily/Offline), Hinweis auf Rebirth |
| Session 2+ | Trading, Rebirth, Events, Koop-Modi |

## Fehler, die Spieler sofort vertreiben
1. Textwand-Tutorial oder Dialog mit NPC vor der ersten Aktion.
2. Leerer Spawn ohne klaren nächsten Schritt.
3. Pflicht-Menüs (Klasse/Team/Einstellungen) vor dem Spielen.
4. Lange Ladezeit/Ruckeln auf Mobile.
5. Thumbnail verspricht etwas, das im ersten Moment nicht da ist (→ Bounce, verschlechtert PTR-Vertrauen).
6. Sofort Kauf-Popup oder „Premium“-Banner.
7. Sofortiger Tod/Verlust (PvP-Spawnkill, Diebstahl in Minute 1 – Steal-Spiele brauchen Schonzeit/Lock für Neue).
8. Steuerung nur per Tastatur (E zum Interagieren ohne Mobile-Button).
9. Leere Server (Social-Spiele): Bot-NPCs oder kleinere Server-Größe beim Launch.
10. UI verdeckt das Spielfeld auf kleinen Handys.

## Messen
Jeden FTUE-Schritt als Funnel-Event loggen (`AnalyticsService:LogOnboardingFunnelStepEvent`, API-Namen im Creator Hub prüfen) und im Dashboard die Abbruchstufe identifizieren. Roblox-Forum-Empfehlung: Fokus auf „New User First Session Retention“ in den Engagement-Analytics, weil D1 und Playtime stark vom ersten Durchgang abhängen **[Q: DevForum „Game's retention and average session time extremely low“, 2026]**.

## Quellen
- Roblox Creator Docs – Retention: https://create.roblox.com/docs/production/analytics/retention
- Roblox Creator Docs – Discovery: https://create.roblox.com/docs/discovery
- BLOXG Retention Guide: https://bloxg.com/guides/roblox-player-retention
- Spaceport – First 2 Minutes: https://www.spaceport.xyz/blog/how-to-hook-players-in-the-first-2-minutes-game-retention-tips-for-roblox-devs
- DevForum Thread: https://devforum.roblox.com/t/game%E2%80%99s-retention-and-average-session-time-extremely-low/4269329
