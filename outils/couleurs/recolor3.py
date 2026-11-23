# Couleurs de perso, version générale (lots de persos) : réglages par perso dans couleurs.py
#   python3 outils/couleurs/recolor3.py ninja chevalier ...   (sans argument : tous les persos de couleurs.py)
# Deux façons de recolorer une zone :
#   mode 'teinte' : rotation de teinte d'une plage de couleur (comme recolor2.py)
#   mode 'gris'   : zone peu saturée (blanc, gris, noir) teintée d'une couleur (comme recolor.py)
# Variante = (nom, teinte cible 0-1, facteur de saturation, facteur de luminosité[, ajout de luminosité])
#   en mode 'gris', le 2e nombre est la saturation donnée à la zone (et non un facteur).
# Écrit assets/perso-<clé>-<n>.png, un aperçu outils/couleurs/apercu-<clé>.png (à ne pas garder)
# et la ligne CHAR_VARS à coller dans jeu.html (outils/couleurs/char_vars.txt).
import numpy as np, json, sys, os
from PIL import Image
from scipy import ndimage as ndi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from couleurs import CFG

html = open('./jeu.html').read(); i = html.index('const CHAR_RECTS = ') + 19; j = html.index(';\n', i); RECTS = json.loads(html[i:j])

def rgb2hsv(rgb):
    mx = rgb.max(-1); mn = rgb.min(-1); d = mx - mn; s = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]; dd = np.maximum(d, 1e-6)
    h = np.where(mx == r, ((g - b) / dd) % 6, np.where(mx == g, (b - r) / dd + 2, (r - g) / dd + 4)) / 6
    return np.where(d > 0, h, 0), s, mx

def hsv2rgb(h, s, v):
    h = h % 1; i = np.floor(h * 6).astype(int) % 6; f = h * 6 - np.floor(h * 6)
    p = v * (1 - s); q = v * (1 - f * s); t = v * (1 - (1 - f) * s)
    out = np.zeros(h.shape + (3,))
    for k, (r, g, b) in enumerate([(v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q)]):
        sel = i == k; out[sel] = np.stack([r[sel], g[sel], b[sel]], -1)
    return out

def in_hue(H, h0, h1):
    return (H >= h0) & (H <= h1) if h0 <= h1 else (H >= h0) | (H <= h1)

def mask_of(key, a, H, S, V, c):
    alpha = a[..., 3] > 30
    if c.get('mode', 'teinte') == 'gris':
        base = (S <= c.get('smax', 0.2)) & (V >= c.get('vmin', 0.0)) & (V <= c.get('vmax', 1.0))
    else:
        base = in_hue(H, c['h0'], c['h1']) & (S >= c.get('smin', 0.3)) & (V >= c.get('vmin', 0.12)) & (V <= c.get('vmax', 1.0))
    m = base & alpha
    # grandes zones seulement : seuil min_area pour la grande pose (220 px de haut), réduit pour les petits cadres
    keep = np.zeros_like(m)
    for pose, frames in RECTS[key].items():
        for fx, fy, fw, fh, *_ in frames:
            sub = m[fy:fy + fh, fx:fx + fw]; lab, n = ndi.label(sub); sz = ndi.sum(sub, lab, range(1, n + 1))
            lim = c.get('min_area', 150) * (fh / 220) ** 2
            keep[fy:fy + fh, fx:fx + fw] |= np.isin(lab, [k + 1 for k, z in enumerate(sz) if z >= lim])
    m = keep
    # bombe exclue, et zones à exclure données en fractions du cadre (x0, y0, x1, y1[, poses]) pour chaque cadre de la planche
    x, y, w, hh = RECTS[key]['bomb'][0][:4]; m[y:y + hh, x:x + w] = False
    for x0, y0, x1, y1, *poses in c.get('skip', []):
        for pose, frames in RECTS[key].items():
            if poses and pose not in poses[0]: continue
            for fx, fy, fw, fh, *_ in frames:
                m[int(fy + y0 * fh):int(fy + y1 * fh), int(fx + x0 * fw):int(fx + x1 * fw)] = False
    if c.get('dilate', 1):
        m = ndi.binary_dilation(m, iterations=c.get('dilate', 1)) & (base | c.get('dilate_any', False)) & alpha   # liseré anti-crénelage
    return m

def hexof(rgb):
    return '#%02x%02x%02x' % tuple(int(round(x * 255)) for x in rgb)

def swatch(rgb, m, H, S, V):
    # couleur de la pastille : la teinte la plus fréquente de la zone, à saturation et luminosité « typiques »
    px = rgb[m]; hs = rgb2hsv(px[None])
    h, s, v = hs[0][0], hs[1][0], hs[2][0]
    sel = v >= np.percentile(v, 35)
    if s[sel].mean() < 0.12 or (sel & (s > 0.15)).sum() < 20:   # zone grise : moyenne simple
        return hexof(np.median(px[sel], 0))
    hist, edges = np.histogram(h[sel & (s > 0.15)], bins=36, range=(0, 1))
    hh = (edges[hist.argmax()] + edges[hist.argmax() + 1]) / 2
    ss = np.percentile(s[sel], 60); vv = np.percentile(v[sel], 60)
    return hexof(hsv2rgb(np.array([hh]), np.array([ss]), np.array([vv]))[0])

def make(key, c, write=True):
    im = Image.open(f'./assets/perso-{key}.png').convert('RGBA'); a = np.array(im).astype(float)
    rgb = a[..., :3] / 255; H, S, V = rgb2hsv(rgb)
    m = mask_of(key, a, H, S, V, c)
    gris = c.get('mode', 'teinte') == 'gris'
    outs = []; sw = [(c['name0'], c.get('hex0') or swatch(rgb, m, H, S, V))]
    for n, var in enumerate(c['variants'], 1):
        name, th, sm, vm = var[:4]; add = var[4] if len(var) > 4 else 0.0
        if gris:
            H2 = np.full(H.shape, th); S2 = np.clip(np.full(S.shape, sm) * (0.6 + S * 2), 0, 1)
        else:
            dH = ((H - c['center'] + 0.5) % 1) - 0.5; H2 = th + dH * c.get('squeeze', 1.0); S2 = np.clip(S * sm, 0, 1)
        V2 = np.clip(V * vm + add, 0, 1)
        new = hsv2rgb(H2, S2, V2)
        rgb2 = np.where(m[..., None], new, rgb)
        b = a.copy(); b[..., :3] = rgb2 * 255
        r = Image.fromarray(b.clip(0, 255).astype(np.uint8), 'RGBA')
        if write:
            r.quantize(colors=255, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(f'./assets/perso-{key}-{n}.png', optimize=True)
        outs.append(r); sw.append((name, var[5] if len(var) > 5 else swatch(rgb2, m, H, S, V)))
    # aperçu : grandes poses + un pas de face, et la pastille au-dessus
    sx, sy, w, h = RECTS[key]['big'][0][:4]; fx, fy, fw, fh = RECTS[key]['down'][0][:4]
    sheet = Image.new('RGBA', ((len(outs) + 1) * w, h + fh + 40), (70, 120, 60, 255))
    for k, r in enumerate([im] + outs):
        sheet.alpha_composite(r.crop((sx, sy, sx + w, sy + h)), (k * w, 24))
        sheet.alpha_composite(r.crop((fx, fy, fx + fw, fy + fh)), (k * w + 10, h + 32))
        sheet.paste(Image.new('RGBA', (w - 8, 16), sw[k][1]), (k * w + 4, 4))
    sheet.save(f'outils/couleurs/apercu-{key}.png')
    line = f"  {key}: [" + ', '.join(f"['{nm}', '{hx}']" for nm, hx in sw) + '],'
    print(key, 'masque', int(m.sum()), 'px'); print(line)
    return line

if __name__ == '__main__':
    keys = sys.argv[1:] or list(CFG)
    lines = [make(k, CFG[k]) for k in keys]
    with open('outils/couleurs/char_vars.txt', 'a') as f: f.write('\n'.join(lines) + '\n')
