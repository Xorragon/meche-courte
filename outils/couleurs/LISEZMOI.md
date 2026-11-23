# Couleurs de perso

Scripts qui fabriquent les planches assets/perso-<clé>-<n>.png (à lancer depuis la racine du dépôt) :
- recolor.py : Capuche (sweat gris recoloré).
- recolor2.py : rotation de teinte, réglages par perso dans CFG (Mage, Gloop, Gavroche). `python3 outils/couleurs/recolor2.py mage`.
- recolor3.py : tous les autres persos, réglages dans couleurs.py. `python3 outils/couleurs/recolor3.py ninja golem`.
  - mode `teinte` (T) : rotation de teinte d'une plage de couleur ; mode `gris` (G) : zone blanche, grise ou noire teintée.
  - `skip` : zones exclues, en fractions du cadre, éventuellement pour certaines poses (visage, cheveux…).
  - Écrit aussi les pastilles : lignes CHAR_VARS dans char_vars.txt, à coller (ou remplacer) dans jeu.html.

Les aperçus apercu-*.png et char_vars.txt ne sont pas à garder (.gitignore).
