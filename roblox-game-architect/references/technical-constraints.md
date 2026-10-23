# Technische Rahmenbedingungen & Machbarkeit

Kennzeichnung: **[Q: …]** belegt (meist Roblox Creator Docs), **[Erfahrungswert]/[Schätzung]** sonst.

## 1. Mobile & Low-End
~80 % der Aktivität ist mobil **[Q: Roblox-Zahlen 2024 via pocketgamer.biz]** – viele Kinder spielen auf älteren Android-Geräten/Tablets.

| Thema | Vorgabe |
|---|---|
| **Instance Streaming** | Standardmäßig an für neue Places; lädt Inhalte regional, spart Speicher. Skripte müssen mit fehlenden Instanzen umgehen (`WaitForChild`, Model-Streaming-Modi) **[Q: Creator Docs „Instance streaming“]** |
| Große Welten | In mehrere Places aufteilen, per Teleport verbinden **[Q: Creator Docs „Design for performance“]** |
| Materialien | Eingebaute Materialien statt vieler Custom-Texturen **[Q: ebd.]** |
| Part-/Instanz-Anzahl | Wiederholte Deko als MeshParts/Instancing, unsichtbare Collider vereinfachen; Startbereich besonders leicht **[Erfahrungswert]** |
| Effekte | Partikel/Lichter mit Limit; Grafikqualität-Option; keine dauerhaft laufenden Partikel bei vielen Spielern **[Erfahrungswert]** |
| UI | Scale statt Offset, `UIAspectRatioConstraint`, Safe Area (Notch), große Touch-Ziele; Test auf 16:9 *und* 4:3-Tablets **[Erfahrungswert]** |
| Steuerung | `ContextActionService`/`ProximityPrompt` mit Touch-Buttons; nie nur Tastatur |
| Profiling | MicroProfiler, Developer Console (F9), Performance-Dashboard im Creator Hub **[Q: Creator Docs „Performance optimization“]** |

## 2. Server
- Spielerzahl pro Server frei wählbar (`Players.MaxPlayers` / Game Settings); öffentlich dokumentierte Obergrenze in Recherche nicht verifiziert – Hits laufen typischerweise mit **6–30** (Koop/Social) bzw. **8–12** (Runden-Horror) Spielern **[Erfahrungswert]**. Voice-Chat offiziell bis 50 Spieler **[Q: DevForum „Voice chat server size“]**.
- Kleine Server beim Soft-Launch → Server füllen sich schneller (Social-Spiele wirken lebendig).
- Lobby + Match-Places via `TeleportService` (reservierte Server für Koop-Runden/Freundesgruppen).
- `MessagingService` für serverübergreifende Ankündigungen (seltene Drops, Live-Events).

## 3. Datenspeicherung (DataStore)
- Max. **4 MB pro Key** (4.194.304 Zeichen); Key-/Store-Namen max. 50 Zeichen; Durchsatzlimits pro Key über 60-Sek-Fenster; Request-Budget per `GetRequestBudgetForRequestType` abfragbar **[Q: Creator Docs „Error codes and limits“]**.
- 2026: Open-Cloud- und In-Game-APIs teilen sich ein Budget; Speicherlimits erhöht **[Q: DevForum „Unifying Data Stores … Increasing Storage Limits“, 2026 – Zahlen vor Nutzung prüfen]**. Über Limits: kostenpflichtige Extended Services **[Q: DevForum „Announcing Roblox Extended Services“]**.

**Empfohlene Struktur (ein Key pro Spieler):**
```lua
PlayerData_v1 = {
  version = 1,              -- für Migrationen
  currency = { coins = 0, gems = 0 },
  progression = { rebirths = 0, zone = 1, upgrades = { speed = 0, capacity = 0 } },
  inventory = { pets = { [uid] = { id = "dog", rarity = 3, level = 1 } } }, -- UIDs gegen Dupes
  collection = { discovered = { dog = true } },
  daily = { streak = 0, lastClaim = 0 },
  purchases = { processedReceipts = { } }, -- PurchaseId-Historie (idempotent)
  settings = { music = true },
  meta = { firstJoin = 0, lastJoin = 0, playtime = 0 },
}
```
- **Session-Locking** gegen Dupes beim Serverwechsel – bewährt: Community-Module **ProfileStore/ProfileService** **[Erfahrungswert]**.
- Autosave alle 2–5 Min + bei `PlayerRemoving` + `game:BindToClose` **[Erfahrungswert]**.
- Käufe: `MarketplaceService.ProcessReceipt` **idempotent** (PurchaseId speichern, erst nach erfolgreichem Speichern `PurchaseGranted` zurückgeben) **[Q: Creator Docs „Developer Products“]**.
- Globale Leaderboards: `OrderedDataStore`, selten aktualisieren (z. B. alle 60–120 Sek).
- Trading: serverseitig atomar (beide Inventare in einer Transaktion via `UpdateAsync`/Session-Lock), Trade-Log speichern.

## 4. Anti-Exploit
Grundsatz: **Der Client lügt.** Jedes RemoteEvent/RemoteFunction ist ein Angriffspunkt; ProximityPrompts ebenso **[Q: Creator Docs „Securing the client-server boundary“]**.
- Server ist autoritativ für Währung, Inventar, Schaden, Cooldowns.
- Jedes Remote prüft: **Typ, Größe/Struktur** (auch gültige, aber übergroße Eingaben), **Berechtigung/Kontext** (Distanz zum Shop, Item besessen, Charakter lebt), **Plausibilität**, **Rate-Limit** **[Q: ebd.]**.
- Kampf: Client meldet Schussursprung + behaupteten Treffpunkt; Server prüft Nähe zum Charakter (mit Latenztoleranz) und Sichtlinie **[Q: ebd.]**.
- Bewegung: Server-Sanity-Checks für Speed/Teleport (tolerant, sonst Lag-Kicks).
- Remotes umbenennen = nur Verschleierung, keine Sicherheit **[Q: DevForum-Diskussion]**.
- Economy-Monitoring: `LogEconomyEvent` → Ausreißer (plötzlich 1000x Coins) finden.

## 5. Systeme/Module (Standardaufteilung)
```
ServerScriptService/
  Services/ DataService, EconomyService, ShopService (ProcessReceipt), ProgressionService,
            DailyRewardService, QuestService, EventService, TradeService, AnalyticsService,
            PolicyService-Wrapper (Paid Random Items, Ads)
ReplicatedStorage/
  Shared/ Config (Preise, Kurven, Odds – eine Quelle!), Remotes, Util
StarterPlayerScripts/
  Controllers/ UIController, InputController (Touch/PC/Gamepad), FeedbackController (VFX/SFX), TutorialController
```
Alle Balancing-Zahlen in **einer Config-Datei** → schnelle LiveOps-Anpassungen ohne Code-Änderungen.

## 6. Was ist mit kleinem Team realistisch? [Schätzung]
| Team | Realistischer MVP-Scope | Zeit bis Soft-Launch |
|---|---|---|
| Solo-Anfänger | Obby mit Twist, kleiner Simulator/Tycoon mit 1 Loop + 1 Meta-System, 2–3 Zonen | 4–8 Wochen |
| Solo erfahren / 2 Leute | Simulator/Grow-Game mit Pets, Rebirth, Daily, Shop; Koop-Survival mit 1 Map | 6–12 Wochen |
| 3–5 Leute | Koop-Horror mit prozeduralen Räumen, Tycoon mit PvP-Steal, kleines Roleplay | 2–4 Monate |
| 5+ mit Budget | Open World, PvP mit Matchmaking, Trading-Economy | 4–9 Monate |

**Immer machbar mit wenig Aufwand:** Daily Rewards, Codes, Wochenend-Boosts, Thumbnail-Varianten, Invite-Prompt, Funnel-Analytics.
**Teuer:** Trading (Sicherheit!), Kampf-Netcode, große Welten, viele 3D-Assets, Story-Content.
**Asset-Hilfen:** Creator Store (Assets prüfen – Freemodels mit Backdoor-Skripten sind ein bekanntes Risiko **[Erfahrungswert]**), Roblox-KI-Tools (Scene Generator angekündigt RDC 2026 **[Q: Roblox Newsroom]**).

## Quellen
- Creator Docs – Instance streaming: https://create.roblox.com/docs/workspace/streaming
- Creator Docs – Design for performance: https://create.roblox.com/docs/performance-optimization/design
- Creator Docs – Performance optimization: https://create.roblox.com/docs/performance-optimization
- Creator Docs – Data store limits: https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits
- DevForum – Unifying Data Stores: https://devforum.roblox.com/t/unifying-data-stores-open-cloud-and-game-apis-and-increasing-storage-limits/4739240
- DevForum – Extended Services: https://devforum.roblox.com/t/announcing-roblox-extended-services/3621439
- Creator Docs – Client-server boundary: https://create.roblox.com/docs/scripting/security/client-server-boundary
- Creator Docs – Developer Products: https://create.roblox.com/docs/production/monetization/developer-products
- DevForum – Voice chat server size: https://devforum.roblox.com/t/voice-chat-server-size/3190671
- pocketgamer.biz – Mobile: https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue
