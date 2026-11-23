# Couleurs de perso par rotation de teinte : la zone d'origine (plage de teinte, saturation mini, grandes zones seulement) prend une autre teinte
import numpy as np, json, sys
from PIL import Image
from scipy import ndimage as ndi
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
def make(key, h0, h1, smin, vmin, center, variants, min_area=150, squeeze=1.0):
    im = Image.open(f'./assets/perso-{key}.png').convert('RGBA'); a = np.array(im).astype(float)
    rgb = a[..., :3] / 255; H, S, V = rgb2hsv(rgb)
    inr = (H >= h0) & (H <= h1) if h0 <= h1 else (H >= h0) | (H <= h1)
    m = inr & (S >= smin) & (V >= vmin) & (a[..., 3] > 30)
    lab, n = ndi.label(m); sz = ndi.sum(m, lab, range(1, n + 1)); m = np.isin(lab, [k + 1 for k, z in enumerate(sz) if z >= min_area])
    x, y, w, hh = RECTS[key]['bomb'][0][:4]; m[y:y + hh, x:x + w] = False
    m = ndi.binary_dilation(m, iterations=1) & inr & (a[..., 3] > 30)   # liseré anti-crénelage
    outs = []
    for n, (name, th, sm, vm) in enumerate(variants, 1):
        dh = th - center
        dH = ((H - center + 0.5) % 1) - 0.5; H2 = np.where(m, th + dH * squeeze, H); S2 = np.clip(S * sm, 0, 1); V2 = np.clip(V * vm, 0, 1)
        new = hsv2rgb(H2, S2, V2)
        b = a.copy(); b[..., :3] = np.where(m[..., None], new, rgb) * 255
        r = Image.fromarray(b.clip(0, 255).astype(np.uint8), 'RGBA')
        r.quantize(colors=255, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(f'./assets/perso-{key}-{n}.png', optimize=True)
        outs.append(r)
    # contrôle : grandes poses côte à côte
    sx, sy, w, h = RECTS[key]['big'][0][:4]
    sheet = Image.new('RGBA', ((len(outs) + 1) * w, h + 140), (70, 120, 60, 255))
    for k, r in enumerate([im] + outs):
        sheet.alpha_composite(r.crop((sx, sy, sx + w, sy + h)), (k * w, 0))
        fx, fy, fw, fh = RECTS[key]['down'][0][:4]; sheet.alpha_composite(r.crop((fx, fy, fx + fw, fy + fh)), (k * w + 10, h + 8))
    sheet.save(f'outils/couleurs/apercu-{key}.png'); print(key, 'masque', int(m.sum()), 'px')
CFG = {
 'mage': dict(h0=0.55, h1=0.72, smin=0.28, vmin=0.12, center=0.63, variants=[('Rouge', 0.99, 1.0, 1.0), ('Vert', 0.36, 0.95, 0.95), ('Violet', 0.78, 1.0, 1.0), ('Noir', 0.66, 0.25, 0.55), ('Blanc', 0.6, 0.12, 1.45), ('Orange', 0.07, 1.05, 1.05)]),
 'slime': dict(h0=0.17, h1=0.48, smin=0.25, vmin=0.15, center=0.30, squeeze=0.45, variants=[('Bleu', 0.58, 1.0, 1.0), ('Rose', 0.91, 0.9, 1.0), ('Violet', 0.76, 1.0, 0.95), ('Orange', 0.075, 1.0, 1.05), ('Rouge', 0.995, 1.0, 0.95), ('Cyan', 0.49, 0.95, 1.05)]),
 'gamin': dict(h0=0.955, h1=0.03, smin=0.5, vmin=0.2, center=0.995, variants=[('Bleu', 0.6, 1.0, 1.0), ('Vert', 0.37, 0.95, 0.9), ('Jaune', 0.14, 1.0, 1.15), ('Violet', 0.77, 0.95, 1.0), ('Noir', 0.0, 0.15, 0.4), ('Rose', 0.92, 0.75, 1.15)]),
}
for k in (sys.argv[1:] or CFG): make(k, **CFG[k])
