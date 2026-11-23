import pickle, json, sys, numpy as np
V = sys.argv[1]
from PIL import Image
meta = pickle.load(open(f'outils/persos/v{V}/meta{V}.pkl', 'rb'))
out = {}; checks = []
for key, m in meta.items():
    walk, big = m['walk'], m['big']
    H = 150 if key == 'astral' else 128
    s = H / float(np.median([fr.height for g in walk for fr in g]))
    def sc(im, f): return im.resize((max(1, round(im.width * f)), max(1, round(im.height * f))), Image.LANCZOS)
    # haut et bas : seulement les 2 premiers pas de la bande de marche (cycle 1er, 2e, 1er, 2e ; à l'arrêt le 2e).
    # (la grande pose immobile du haut de la planche n'est plus utilisée : dessinée à une autre échelle, elle
    #  faisait un effet zoom / dézoom à chaque pas)
    frames = {
        'down': [sc(walk[0][0], s), sc(walk[0][1], s)],
        'up': [sc(walk[2][0], s), sc(walk[2][1], s)],
        'right': [sc(f, s) for f in walk[3]],
    }
    bomb = sc(m['bomb'], 72 / m['bomb'].height)
    bg = sc(big[0], 220 / big[0].height)
    items = [(d, i, fr) for d in ('down', 'up', 'right') for i, fr in enumerate(frames[d])] + [('bomb', 0, bomb), ('big', 0, bg)]
    W = sum(it[2].width + 2 for it in items); Hh = max(it[2].height for it in items)
    atlas = Image.new('RGBA', (W, Hh), (0, 0, 0, 0)); x = 0; rects = {}
    for d, i, fr in items:
        atlas.alpha_composite(fr, (x, 0))
        a = np.array(fr)[..., 3]; rows = np.nonzero(a.max(1) > 40)[0]; bot = rows.max() + 1
        band = (a[int(fr.height * .25):int(fr.height * .8)] > 40).sum(0).astype(float)
        cum = np.cumsum(band); ax = float(np.searchsorted(cum, cum[-1] / 2)) if cum[-1] else fr.width / 2
        rects.setdefault(d, []).append([x, 0, fr.width, fr.height, round(ax, 1), int(bot)])
        x += fr.width + 2
    for d in ('down', 'up'): rects[d].append(rects[d][0])
    q = atlas.quantize(colors=255, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE) if key != 'astral' else atlas
    q.save(f'./assets/perso-{key}.png', optimize=True)
    out[key] = rects; checks.append((key, atlas))
json.dump(out, open(f'outils/persos/v{V}/rects{V}.json', 'w'))
# planche de contrôle sur fond d'herbe
Wc = max(a.width for _, a in checks) + 20; sheet = Image.new('RGBA', (Wc, sum(a.height + 10 for _, a in checks) + 10), (70, 120, 60, 255)); y = 10
for k, a in checks: sheet.alpha_composite(a, (10, y)); y += a.height + 10
sheet.save(f'outils/persos/v{V}/check-all.png'); print(sheet.size)
