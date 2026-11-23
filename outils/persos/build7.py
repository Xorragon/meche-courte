# 20 planches du joueur (2026-11-23) : découpe, détourage, puis bande perso-<clé>.png + rectangles
# Haut et bas : 1er pas, pose immobile (grande pose du haut, réduite), 2e pas (le 3e pas n'est pas utilisé)
import numpy as np, json, sys, pickle
from PIL import Image
from scipy import ndimage as ndi
import os
U = os.environ.get('PLANCHES', '/mnt/user-data/uploads/')
CH = [('bricolo','4d2c05d7'),('momie','0ddb21e0'),('fee','a47ea16d'),('orc','b10552a9'),('ondine','16b4090b'),
      ('papy','77e8f210'),('cocorico','37bfc94c'),('peintre','519ab8c9'),('phenix','4cd834c2'),('pompiere','af152df5')]
only = sys.argv[1:] or [k for k, _ in CH]
def matte_hard(im):
    mx, mn = im.max(2), im.min(2)
    light = (mn > 172) & (mx - mn < 24)
    lab, n = ndi.label(light)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(border))
    for _ in range(2):
        edge = ~bg & ndi.binary_dilation(bg) & (mn > 200); bg = bg | edge
    fg = ~bg
    rgba = np.zeros(im.shape[:2] + (4,), np.uint8); rgba[..., :3] = im
    a = fg.astype(np.uint8) * 255
    a = (ndi.uniform_filter(a.astype(float), 2) * (a > 0)).clip(0, 255).astype(np.uint8)
    rgba[..., 3] = a
    return rgba, fg
def matte_soft(im):   # perso lumineux : on garde le halo
    imf = im.astype(float); mx, mn = imf.max(2), imf.min(2)
    light = (mn > 236) & (mx - mn < 14)
    lab, n = ndi.label(light)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(border))
    a = np.clip((255 - mn) / 255, 0, 1); a = np.clip((a - 0.07) / 0.93, 0, 1) ** 0.85
    a[~bg] = np.maximum(a[~bg], 1.0); a[bg & (mn > 247)] = 0
    col = np.where(a[..., None] > 1e-3, (imf - (1 - a[..., None]) * 255) / np.maximum(a[..., None], 1e-3), 0)
    rgba = np.dstack([np.clip(col, 0, 255), a * 255]).astype(np.uint8)
    return rgba, a > 0.06
def crop(rgba, fg, x0, x1, y0, y1, feather=0):
    sub = fg[y0:y1, x0:x1]; ys, xs = np.nonzero(sub)
    # on ne garde que les gros morceaux (pas les miettes du texte voisin)
    lab, n = ndi.label(sub)
    if n > 1:
        sz = ndi.sum(sub, lab, range(1, n + 1)); keep = np.isin(lab, [i + 1 for i, s in enumerate(sz) if s >= 40])
        sub = keep; ys, xs = np.nonzero(sub)
    A, B, C, D = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    out = rgba[y0 + A:y0 + B, x0 + C:x0 + D].copy(); out[..., 3] = np.where(sub[A:B, C:D], out[..., 3], 0)
    if feather:
        w = out.shape[1]; ramp = np.minimum(1, np.minimum(np.arange(w) + 1, w - np.arange(w)) / feather)
        out[..., 3] = (out[..., 3] * ramp[None, :]).astype(np.uint8)
    return Image.fromarray(out, 'RGBA')
meta = {}
for key, f in CH:
    if key not in only: continue
    im = np.array(Image.open(U + f + '-image.png').convert('RGB'))
    soft = key == 'astral'
    rgba, fg = (matte_soft if soft else matte_hard)(im)
    big = [crop(rgba, fg, q * 256, (q + 1) * 256, 40, 380) for q in range(4)]
    walk = []; Y0, Y1 = 400, 595; band = fg[Y0:Y1]
    for q in range(4):
        cols = band[:, q * 256:(q + 1) * 256].sum(0).astype(float)
        nz = np.nonzero(cols > 2)[0]; A, B = nz.min(), nz.max()
        cuts = []
        for t in (1 / 3, 2 / 3):
            c0 = int(A + (B - A) * t); lo, hi = max(A, c0 - 18), min(B, c0 + 18)
            cuts.append(lo + int(np.argmin(cols[lo:hi])))
        xs = [A, cuts[0], cuts[1], B + 1]
        walk.append([crop(rgba, fg, q * 256 + xs[i], q * 256 + xs[i + 1], Y0, Y1, 6 if soft else 0) for i in range(3)])
    # bombe : le dernier objet en bas à droite
    reg = fg[730:915, 620:800].copy(); lab, n = ndi.label(reg)
    sz = ndi.sum(reg, lab, range(1, n + 1)); main = int(np.argmax(sz)) + 1
    ys, xs = np.nonzero(lab == main); y0, y1, x0, x1 = ys.min() - 40, ys.max() + 30, xs.min() - 30, xs.max() + 40
    keep = np.zeros_like(reg)
    for i, sl in enumerate(ndi.find_objects(lab)):
        if sl[0].start >= y0 and sl[0].stop <= y1 and sl[1].start >= x0 and sl[1].stop <= x1: keep |= lab == i + 1
    fg2 = fg.copy(); fg2[730:915, 620:800] = keep
    bomb = crop(rgba, fg2, 620, 800, 730, 915)
    meta[key] = {'big': big, 'walk': walk, 'bomb': bomb}
    print(key, [b.size for b in big], [[x.size for x in g] for g in walk], bomb.size, flush=True)
pickle.dump(meta, open('outils/persos/v7/meta7.pkl', 'wb'))
