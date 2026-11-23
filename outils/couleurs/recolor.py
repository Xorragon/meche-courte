import numpy as np, colorsys, sys
from PIL import Image
SRC = './assets/perso-capuche.png'
# variantes : (nom, teinte 0-1, saturation, gain de luminosité)
VARS = [('Rouge', 0.995, 0.62, 0.95), ('Bleu', 0.60, 0.55, 0.95), ('Vert', 0.36, 0.45, 0.88), ('Violet', 0.76, 0.42, 0.95),
        ('Moutarde', 0.12, 0.62, 1.05), ('Rose', 0.92, 0.38, 1.08), ('Noir', 0.62, 0.10, 0.45)]
def mask_of(rgb):
    mx = rgb.max(-1); mn = rgb.min(-1); s = (mx - mn) / np.maximum(mx, 1e-3)
    return (s < 0.2) & (mx > 0.28) & (mx < 0.86), mx
def recolor(im, h, sat, gain):
    a = np.array(im.convert('RGBA')).astype(float); rgb = a[..., :3] / 255
    m, v = mask_of(rgb)
    m &= a[..., 3] > 30
    # seulement les grandes zones grises (le sweat) : pas le blanc des yeux, les semelles, le motif du t-shirt
    from scipy import ndimage as ndi
    lab, n = ndi.label(m); sz = ndi.sum(m, lab, range(1, n + 1))
    m = np.isin(lab, [k + 1 for k, z in enumerate(sz) if z >= MIN_AREA])
    if BOMB: x, y, w, hh = BOMB; m[y:y + hh, x:x + w] = False
    v2 = np.clip(v * gain, 0, 1)
    # HSV -> RGB vectorisé
    H = np.full(v.shape, h); S = np.full(v.shape, sat)
    i = np.floor(H * 6).astype(int) % 6; f = H * 6 - np.floor(H * 6)
    p = v2 * (1 - S); q = v2 * (1 - f * S); t = v2 * (1 - (1 - f) * S)
    out = np.zeros(rgb.shape)
    for k, (r, g, b) in enumerate([(v2, t, p), (q, v2, p), (p, v2, t), (p, q, v2), (t, p, v2), (v2, p, q)]):
        sel = i == k; out[sel] = np.stack([r[sel], g[sel], b[sel]], -1)
    rgb2 = np.where(m[..., None], out, rgb)
    a[..., :3] = rgb2 * 255
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGBA')
im = Image.open(SRC)
import json, re
html = open('./jeu.html').read(); i = html.index('const CHAR_RECTS = ') + 19; j = html.index(';\n', i)
BOMB = json.loads(html[i:j])['capuche']['bomb'][0][:4]; MIN_AREA = 260
for n, (name, h, s, g) in enumerate(VARS, 1):
    r = recolor(im, h, s, g)
    r.quantize(colors=255, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(f'./assets/perso-capuche-{n}.png', optimize=True)
    r.save(f'outils/couleurs/apercu-capuche-{n}.png')
# planche de contrôle : la grande pose et les pas de chaque variante
rows = [im.convert('RGBA')] + [Image.open(f'outils/couleurs/apercu-capuche-{n}.png') for n in range(1, len(VARS) + 1)]
W = rows[0].width; sheet = Image.new('RGBA', (W, 230 * len(rows)), (70, 120, 60, 255))
for k, r in enumerate(rows): sheet.alpha_composite(r, (0, 230 * k))
sheet.resize((W // 2, 115 * len(rows))).save('outils/couleurs/apercu-capuche.png')
