# Mèche Courte : le site

- `index.html` : la page d'accueil du jeu
- `jeu.html` : le jeu (contre l'ordi, à deux sur un clavier, en ligne avec un pote)
- `assets/` : les images de la page d'accueil
- `favicon.svg` : l'icône d'onglet

## Mettre le site en ligne (gratuit, environ 2 minutes)

1. Va sur https://app.netlify.com/drop
2. Glisse le dossier `meche-courte-site` (ou le fichier .zip) dans la zone de dépôt.
3. Netlify donne une adresse du type `https://nom-au-hasard.netlify.app`.
4. Crée un compte gratuit et clique sur « Claim » pour garder le site : sans ça, il est supprimé au bout d'une heure.
5. Dans les réglages du site, tu peux changer le nom pour avoir par exemple `meche-courte.netlify.app`.

Pour mettre à jour le site plus tard : sur la page du site dans Netlify, onglet « Deploys », glisse le nouveau dossier.

## Jouer en ligne

1. Ouvre `jeu.html` sur le site en ligne et choisis « En ligne avec un pote ».
2. Clique sur « Créer une partie » : un code de 4 caractères s'affiche. Envoie-le à ton pote, ou copie le lien d'invitation.
3. Ton pote entre le code et clique sur « Rejoindre ».

La connexion passe directement entre les deux navigateurs, grâce au service gratuit de mise en relation PeerJS.
Le jeu en ligne a besoin d'internet. Passe par l'adresse du site plutôt que d'ouvrir le fichier en double-cliquant : le lien d'invitation ne fonctionne que sur le site en ligne.
