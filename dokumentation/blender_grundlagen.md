[Home](../README.md)
| [Veranstaltungsziele](./veranstaltungsziele.md)
| [Git Grundlagen](./git_grundlagen.md)
| Blender Grundlagen
| [Themengebiete](./themengebiete.md)
| [Liste zu modellierender Assets](./asset_liste.md)
| [Weitere Tools](./tools.md)
| [Links](./links.md)

# Blender Grundlagen

Dieser Abschnitt ist primär als Checkliste zu verstehen. Sie entält alle wichtigen Funktionen und Shortcuts, die in der Lehrveranstaltung vermittelt werden sollen.

## Tipps
- Große Modelle führen Blender an seine Grenzen. Modus- oder Layout-Wechsel können mitunter zu Abstürzen führen!

## Notation
In den nachfolgenden Abschnitten werden folgende Sonderzeichen verwendet
- Das + Symbol deutet an, dass 2 oder mehr Aktionen gleichzeitig gedrückt/ausgeführt werden müssen
- Das > Symbol wird dazu verwendet, um anzudeuten, dass eine Aktion innerhalb eines Dropdown-Menüs oder Untermenüs zu finden ist
- Das , Symbol außerhalb von Klammern, wird dazu verwendet, um aufeinanderfolgende Aktionen voneinander zu trennen
- Das : Symobl wird dazu verwendet, um Beschreibungen (links) von Aktionsfolgen (rechts) zu trennen
- Spitze Klammern, wie z.B. <Relativer Pfad>, beschreiben Platzhalter
- Runde Klammern, wie z.B. (<Kommentar>), beschreiben, in welchem Kontext bestimmte Aktionen ausführbar sind
- Eckige Klammern, wie z.B. [<Aktion>, <Aktion>] beschreiben eine Reihe von Auswahlmöglichkeiten. Eine der erwähnten Aktionen ist dabei zu wählen, um das gewünschte Ergebnis zu erreichen

## Navigation
- Linke Maustaste: Selektion
- Mittlere Maustaste: Rotation
- Mittlere Maustaste + Shift: Translation
- Rechte Maustaste: Öffnen von Context Menüs
- Tabulator Taste: Wechseln zwischen aktivem/letzten Modus (meistens befindet man sich im Object Mode) und Edit Mode
- Objekt Transformation: G, G + [X, Y, Z], G + Shift + [X, Y, Z]
- Objekt Rotation: R, R + [X, Y, Z], R + Shift + [X, Y, Z]
- Objekt Skalierung: S, S + [X, Y, Z], S + Shift + [X, Y, Z]
- Triangulierung: Strg + T
- Vertices, Edges, Faces extrudieren: E
- Alles Auswählen: A
- Auswahl Invertieren: Strg + I
- Objekte duplizieren: Shift + D
- Objekte duplizieren und Beziehung zu Original bewahren: Alt + D
- Objekte joinen: Strg + J
- Dialog zum Löschen von Objekten öffnen: X
- Sofortiges Löschen von Objekten: Entf
- Viewpoint Shading wechseln: Z, Shift + Z
- Linke Sidebar öffnen/schließen: T
- Rechte Sidebar öffnen/schließen: N
- Animation starten/pausieren: Leertaste
- Suche öffnen (früher Leertaste): F3 
- Bild rendern: Strg + F12
- (Edit Mode) Kanten/Flächen unterteilen: Subdivide
- (Edit Mode) Kanten/Flächen unterteilen (aka LoopCut): Strg + R: 
- (Edit Mode) Objekt aufspalten: Separate
- (Edit Mode) Zusammenhängende Polygone selektieren: L
- (Edit Mode) Weiche/Harte Kanten: Shading > Flat Faces / Smooth Faces
- (Edit Mode) Normalen ändern: Normals > [Flip, Recalculate Outside, Recalculate Inside]
- Cursor zurücksetzen: Shift + C
- (Edit Mode) Gegenüberliegende Kanten verbinden:
- (Vertex-Select): Strg + E > Bridge Edge Loops
- (Edge-Select): [Rechte Maustaste, Strg + E] > Bridge Edge Loops
- (Face-Select): Strg + E > Bridge Edge Loops
- (Face-Select): Bridge Faces
- Kante zw. 2 Vertices hinzufügen: F
- Fläche zw. N Vertices hinzufügen: F
- Fläche zw. N Kanten hinzufügen: F
- (Edit Mode) Form in Koordinatenebene angleichen: Mesh > Symmetrize
- Material anlegen/zuweisen
- Textur anlegen + UVs vergeben
- Referenz-Bilder importieren
- (Object Mode) Eltern-Kind-Beziehung festlegen: Strg + P
- (Object) Transformationen anwenden: Strg+A
- Box Select: B
- Circle Select: C
- (Edit Mode) Select Edge Loops: Alt + Linke Maustaste
- Zu existierender Menge selektierter Objekte hinzufügen: Shift gedrückt halten + \<Shortcut\>
- Vertex Doubles entfernen (früher Remove Doubles): Mesh > Cleanup > Merge By Distance
- Ein und Ausblenden von Objekten: (H) bzw. (Alt+H)
- Origin verschieben
    - (Edit Mode) Snap Vertices →Cursor to Selected
    - (Object Mode) Set Origin → Origin to 3D 
    - Shift + S → Cursor to Active oder Cursor to Selected
    - Bsp.: Rotation, wenn Origin an Objekt-Ecke liegt
    - Bsp.: Skalierung, wenn Origin an Objekt-Ecke liegt

## Perspektiven
- User Perspective ↔ User Orthographic: 5
- Orthographische Ansichten von der Seite: 1, 3, 7
- Orthographische Ansichten von der gegenüberliegenden Seite: Strg + [1, 3, 7]
- Gegenüberliegende Ansicht: 9
- In/Aus Kamera-Ansicht wechseln: 0
- Rotation um 15 Grad: 2, 4, 6, 8

## Transformation orientation
- Global vs. Local
- Pivot Point
- Snap
- Proportional Editing

## Modes
- Object Mode
- Edit Mode
- Sculpt Model
- Vertex Paint
- Weight Paint
- Texture Paint

## Viewpoint Shading
- Wireframe
- Solid
- Look Dev
- Rendered

## Szenenobjekte
- Kamera
- Lichtquelle
- Default Cube

## Windows
- 3D Viewport
- Property Window
- Outliner
- Timeline

## Layout
- Aktives (Default) Layout
- Modelling
- Sculpting
- UV Editing
- Texture Paint
- Shading
- Animation
- Rendering
- Composition
- Scripting

## Blender Preferences
Eine Liste aller aktivierten Einstellungen. Die meisten Einstellungen sind dabei bereits standardmäßig aktiv. Doch es befinden sich auch Tools in dieser Liste, die manuell zu aktivieren sind. 
- AddCurve: Extra Objects
- AddMesh: BoltFactory
- AddMesh: Extra Objects
- AddMesh: Simple Asset Manager
- Import-Export: FBX format
- Import-Export: Images as Planes
- Import-Export: STL format (SVG) 1.1 format
- Import-Export: Scalable Vector Graphics
- Import-Export: Stanford PLY format
- Import-Export: UV Layout
- Import-Export: Wavefront OBJ format
- Import-Export: Web3D X3D/VRML2 format
- Import-Export: gltf 2.0 format
- Mesh: 3D Print Toolbox
- Mesh: LoopTools
- Mesh: tinyCAD Mesh Tools
- Object: Bool Tool
- Render: Cycles Render Engine

## Import und Export von Modellen
- FBX Format
- GLB/GLTF Format
- Wichtigste Einstellung: Selected Objects

## Modifier
- Array
- Boolean
- Mirror
- Solidify
- Subdivision Surface

## Lichtquellen
- Point Light
- Sun Light
- Spot Light
- Area Light
