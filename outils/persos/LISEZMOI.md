# Planches de persos

Scripts à lancer depuis la racine du dépôt. Les planches envoyées par le joueur (1024 × 1024) sont lues dans le dossier `PLANCHES` (par défaut `/mnt/user-data/uploads/`), sous le nom `<id>-image.png`.

1. `buildN.py` : découpe et détourage d'un lot (liste `CH` = clé du perso + id du fichier). Écrit `outils/persos/vN/metaN.pkl` (dossier à créer, non gardé dans le dépôt).
2. `atlas_walk.py N` : planche `assets/perso-<clé>.png` + `outils/persos/vN/rectsN.json` (haut et bas : 2 premiers pas seulement). Fusionner ensuite le JSON dans `CHAR_RECTS` de jeu.html et **changer `SPR_V`** si des planches existantes sont refaites.
3. `unl8.py` / `unlshop.py` (+ `shoptiers.py`) : images de déblocage `assets/unlock-<clé>.jpg`.

Couleurs de perso : voir `outils/couleurs/`.
