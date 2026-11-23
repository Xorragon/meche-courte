import sys, numpy as np
sys.argv = ['x', 'none']
exec(open('outils/persos/build8.py').read().split('meta = {}')[0])
from PIL import Image, ImageDraw, ImageFilter
for key, f, c1, c2 in [('sylve', 'a7bd7bb9', (64, 120, 58), (14, 34, 20)), ('prospecteur', '91ff2ba9', (150, 104, 40), (36, 22, 12))]:
    im = np.array(Image.open(U + f + '-image.png').convert('RGB'))
    rgba, fg = matte_hard(im)
    pose = crop(rgba, fg, 420, 620, 690, 915)       # pose avec la bombe à la main
    W, H = 400, 500
    yy, xx = np.mgrid[0:H, 0:W]; d = np.sqrt((xx - W / 2) ** 2 + ((yy - H * .45) * .9) ** 2) / 320
    d = np.clip(d, 0, 1)[..., None]
    bg = (np.array(c1) * (1 - d) + np.array(c2) * d).astype(np.uint8)
    bgI = Image.fromarray(bg, 'RGB').convert('RGBA')
    rays = Image.new('RGBA', (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(rays)
    for k in range(14):
        a = k * np.pi / 7
        dr.polygon([(W / 2, H * .45), (W / 2 + 600 * np.cos(a - .09), H * .45 + 600 * np.sin(a - .09)), (W / 2 + 600 * np.cos(a + .09), H * .45 + 600 * np.sin(a + .09))], fill=(255, 240, 190, 34))
    bgI.alpha_composite(rays.filter(ImageFilter.GaussianBlur(3)))
    s = min(370 / pose.height, 350 / pose.width); p = pose.resize((round(pose.width * s), round(pose.height * s)), Image.LANCZOS)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse((W / 2 - 120, H - 70, W / 2 + 120, H - 30), fill=(0, 0, 0, 90))
    bgI.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
    bgI.alpha_composite(p, ((W - p.width) // 2, H - 40 - p.height))
    bgI.convert('RGB').save(f'./assets/unlock-{key}.jpg', quality=88)
    print(key, pose.size)
