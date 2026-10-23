# Spielidee: „Uphill Ball Rush“ (Arbeitstitel) – Beschreibung aus Referenzvideo

> Diesen Text komplett an Claude Code geben (Skill `roblox-game-architect`).
> Auftrag: **Analysiere diese Idee mit dem Skill und plane sie als Roblox-Spiel. Danach baue einen spielbaren Prototyp (Level 1 + Level 2) in Luau.**

---

## 1. Kurzfassung (1 Satz)
Ein kurzes **Zeitrennen bergauf**: Der Spieler sprintet eine kurvige, wellige Rampe über den Dächern einer Stadt hinauf, während ihm **ununterbrochen bunte Kugeln in allen Größen entgegenrollen**. Ziel ist eine Kristallkuppel mit einem goldenen Ring oben am Ende der Strecke. Je schneller man ist, desto besser die **Medaille (Diamond → Gold → Rock → Coal)**.

Genre: Obby/Runner + Zeitrennen (Speedrun) mit Physik-Hindernissen, ähnlich wie „Donkey Kong-Fässer“ mal „Marble Madness“.

## 2. Was man im Video sieht (genaue Beobachtung)

### Spielfigur
- Humanoide Figur, **glänzend türkis/cyan, wie verchromt oder aus Glas** (Mannequin-Look, keine Kleidung, kein Gesicht).
- Third-Person-Kamera **direkt hinter und leicht über** der Figur. Die Kamera blickt bergauf und folgt den Kurven der Strecke.
- Die Figur rennt, springt und wird von großen Kugeln **umgeworfen, sie wird zur Ragdoll** und rutscht oder fällt ein Stück zurück. Danach steht sie wieder auf und läuft weiter.

### Strecke (Level 1)
- Ein **breites, schwebendes Band**, ca. 3–4 Spielerbreiten, das sich als **Serpentine bergauf** windet.
- Oberfläche: **grüner Rasen mit hell/dunkel gestreiften Querbahnen** (wie ein Fußballrasen). Die Fläche ist **wellig**, mit Buckeln und Mulden quer zur Laufrichtung.
- **Rote, runde Gummi-Banden (Wülste)** an beiden Rändern als Geländer. An manchen Stellen fehlen sie, dort kann man herunterfallen.
- Abschnitte mit anderem Untergrund:
  - eine **gelbe, flache, schräge Rampe bzw. Brücke** (glatter Untergrund),
  - ein **Wasser-/Eisabschnitt in Türkis** mit glänzender, spiegelnder Oberfläche. Dort rutscht oder schwimmt die Figur und kommt langsamer voran.
- Am Ende ist das **Ziel eine große, türkis-transparente Kuppel mit Schachbrettmuster (geodätische Kuppel)**. In ihr schwebt ein **rotierender goldener Ring bzw. eine Münze**. Wer hindurchläuft, hat das Level geschafft und der Bildschirm blitzt türkis auf.

### Hindernisse: rollende Kugeln
- Von oben (aus dem Ziel bzw. vom Streckenende) rollen **ständig Kugeln die Strecke herunter**, auf den Spieler zu.
- **Größen sehr unterschiedlich**: kleine Murmeln (ca. 0,5 Studs) bis riesige Kugeln (fast so groß wie die Figur oder größer, ca. 6–10 Studs).
- **Farben**: Pink/Magenta, Türkis, Orange-Rot, Grün, Gelb, Dunkelrot. Viele haben ein **verspieltes Muster aus Kreisen und Ornamenten**, wie Bowling- oder Hüpfbälle.
- Kugeln kommen mal einzeln, mal als **dichte „Lawine“ in einer Reihe** (Kette vieler kleiner Kugeln) und sammeln sich in Mulden.
- Kleine Kugeln stören nur leicht. **Große Kugeln werfen den Spieler um (Ragdoll) und schieben ihn zurück.** Man muss ausweichen, seitlich vorbeilaufen oder drüberspringen.

### Umgebung / Look
- Die Strecke schwebt **zwischen und über Gebäuden einer japanischen Großstadt** (Tokio-Gasse): Hochhäuser, Stromleitungen und Kabelgewirr, Ladenschilder („ramen“, „SALES SERVICE RENT“), Ziegeldächer und Plakate.
- Strahlend **blauer Himmel mit Wolken**, hell und sehr farbig. Der Stil mischt realistische Stadt mit knallbunten Spielelementen.

### HUD (Bildschirmanzeige)
- **Oben links: Laufender Timer** mit Millisekunden, z. B. `12.393`. Darunter in Klammern **die Grenzzeit der aktuell noch erreichbaren Medaille**, z. B. `(13.999)`.
- **Daneben ein Medaillen-Icon und Text**, die sich live ändern, sobald man zu langsam wird:
  | Medaille | Grenzzeit Level 1 | Icon |
  |---|---|---|
  | **Diamond!** | ≤ 9.000 s | türkiser Diamant |
  | **Gold!** | ≤ 10.999 s | Goldbarren |
  | **Rock!** | ≤ 13.999 s | witziges Rocker-Portrait (Wortspiel Rock = Stein/Rockmusik) |
  | **Coal** | ≤ 99.999 s | Kohlebrocken (ohne Ausrufezeichen, also schlechteste Stufe) |
- **Unten links: ein blaues Sechseck-Edelstein-Icon.** In bestimmten Abschnitten wird daraus eine **Zahl (2 → 1)**. Vermutlich ein Zähler für die verbleibenden Abschnitte bzw. Checkpoints bis zum Ziel, eventuell auch für Leben. *(Im Video nicht eindeutig. Vorschlag: als „verbleibende Checkpoints“ umsetzen.)*
- **Unten Mitte: ein blauer Stern**, vermutlich ein Touch-Button (Sprung/Dash) für Mobile.

### Ablauf
1. Level startet, der Timer läuft ab 00.000.
2. Spieler rennt bergauf, weicht Kugeln aus, wird evtl. umgeworfen.
3. Die Medaille fällt im HUD live ab, wenn die Grenzzeiten überschritten werden.
4. Ziel-Kuppel erreicht: Blitz-Effekt, **sofort nächstes Level**. Der Timer startet neu.
5. **Level 2**: eine **Holzrinne/Rutsche aus braunem Holz** (U-förmige Halfpipe), über Dächern mit einem Ziegelschornstein. Gelbe Querstreifen (Boost-Pads oder Stufen), kleinere bunte Kugeln, ein türkiser Wasserabschnitt seitlich. Diamond-Grenze **28.999 s**, also ein längeres Level.

## 3. Was daraus für Roblox werden soll

### Core Loop
Level starten → bergauf rennen und Kugeln ausweichen → Ziel → Medaille + Zeit → bessere Medaille jagen oder nächstes Level → neue Welt freischalten.

### Muss im Prototyp drin sein
- **2 Level** wie oben (grüne Rasen-Serpentine, Holzrinne), modular aus Streckenteilen gebaut.
- **Kugel-Spawner** am Streckenende: zufällige Größe, Farbe und Intervall, gelegentliche „Lawinen-Wellen“. Die Kugeln sind physikalisch (`Ball`-Parts, mit Masse und Reibung) und werden unten bzw. nach X Sekunden **despawnt** (Pooling für Performance).
- **Treffer-Logik**: Große Kugel trifft Spieler → Ragdoll für ca. 1–1,5 s + Rückstoß bergab. Kleine Kugeln geben nur einen Schubs.
- **Untergründe**: Rasen normal, gelbe Rampe glatt, Wasser/Eis langsam und rutschig (über `CustomPhysicalProperties` / WalkSpeed).
- **Herunterfallen** → Respawn am letzten Checkpoint, der Timer läuft weiter.
- **Timer + Live-Medaille im HUD** (Diamond/Gold/Rock/Coal mit Grenzzeiten pro Level).
- **Ziel-Kuppel** mit rotierendem Goldring, Partikel/Flash, Medaillen-Anzeige, „Weiter“ / „Nochmal“.
- **Bestzeiten speichern** (DataStore) + **globales Leaderboard pro Level** (OrderedDataStore).
- **Mobile-tauglich**: großer Sprung-Button, Kamera folgt automatisch bergauf.
- Zeit wird **serverseitig gemessen** (Anti-Cheat), Kugeln spawnen auf dem Server.

### Ideen für später (Skill soll bewerten)
- Mehr Welten (Strand, Schnee, Süßigkeiten, Lava), jeweils mit neuem Untergrund-Gimmick.
- Medaillen-Sammlung als Fortschritt (Diamond in allen Leveln = Bonuswelt).
- Skins für die Figur (Chrom, Gold, Neon, Glas), Trails, Kugel-Designs.
- **Multiplayer-Rennen**: 4–8 Spieler gleichzeitig auf derselben Strecke. Kugeln werfen auch Gegner um, dadurch entstehen Clip-Momente.
- Tägliche Herausforderung (zufällige Kugel-Muster), Ghost-Replay der eigenen Bestzeit.

## 4. Auftrag an Claude Code
1. Den Skill `roblox-game-architect` auf diese Idee anwenden: Reality-Check, Score und den Plan mit 15 Abschnitten.
2. Danach einen **spielbaren Prototyp** bauen: Rojo-Projektstruktur (`src/server`, `src/client`, `src/shared`) in Luau. Die Strecke wird prozedural oder modular per Script erzeugt, damit sie ohne Studio-Handarbeit testbar ist. Dazu Kugel-Spawner, Ragdoll-Treffer, Timer/Medaillen-HUD, Checkpoints, Ziel, DataStore-Bestzeiten und Leaderboard.
3. Grenzzeiten in einer Config-Datei (`LevelConfig`), damit sie leicht anpassbar sind.
4. Kurz erklären, wie ich das Projekt in Roblox Studio öffne und teste.
