import sys, numpy as np, re
sys.argv = ['x', 'none']
src = open('outils/persos/build8.py').read().split('meta = {}')[0]
exec(src)
from PIL import Image, ImageDraw, ImageFilter
import sys; sys.path.insert(0, 'outils/persos'); from shoptiers import TIERS
files = {}
for b in ('build5.py', 'build6.py', 'build7.py'):
    for k, f in re.findall(r"\('([a-z]+)','([0-9a-f]{8})'\)", open('outils/persos/' + b).read()): files[k] = f
COL = {1: ((96, 112, 128), (22, 28, 36)), 2: ((52, 108, 180), (12, 24, 48)), 3: ((128, 70, 170), (30, 14, 44)), 4: ((196, 150, 48), (52, 32, 8))}
only = sys.argv[2:] if False else None
for t, keys in TIERS.items():
    c1, c2 = COL[t]
    for key in keys:
        im = np.array(Image.open(U + files[key] + '-image.png').convert('RGB'))
        rgba, fg = matte_hard(im)
        pose = crop(rgba, fg, 420, 620, 690, 915)
        W, H = 400, 500
        yy, xx = np.mgrid[0:H, 0:W]; d = np.clip(np.sqrt((xx - W / 2) ** 2 + ((yy - H * .45) * .9) ** 2) / 320, 0, 1)[..., None]
        bgI = Image.fromarray((np.array(c1) * (1 - d) + np.array(c2) * d).astype(np.uint8), 'RGB').convert('RGBA')
        rays = Image.new('RGBA', (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(rays)
        for k in range(14):
            a = k * np.pi / 7
            dr.polygon([(W / 2, H * .45), (W / 2 + 600 * np.cos(a - .09), H * .45 + 600 * np.sin(a - .09)), (W / 2 + 600 * np.cos(a + .09), H * .45 + 600 * np.sin(a + .09))], fill=(255, 240, 190, 34))
        bgI.alpha_composite(rays.filter(ImageFilter.GaussianBlur(3)))
        s = min(370 / pose.height, 350 / pose.width); p = pose.resize((round(pose.width * s), round(pose.height * s)), Image.LANCZOS)
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse((W / 2 - 120, H - 70, W / 2 + 120, H - 30), fill=(0, 0, 0, 90))
        bgI.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
        bgI.alpha_composite(p, ((W - p.width) // 2, H - 40 - p.height))
        bgI.convert('RGB').save(f'./assets/unlock-{key}.jpg', quality=84)
        print(key, pose.size, flush=True)
