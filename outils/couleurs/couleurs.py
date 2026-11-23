# Réglages des couleurs de perso pour recolor3.py (voir son en-tête)
# Teintes cibles
ROUGE, ORANGE, JAUNE, VERT, CYAN, BLEU, VIOLET, ROSE = 0.995, 0.07, 0.14, 0.36, 0.5, 0.61, 0.77, 0.92

def T(name0, h0, h1, center, variants, **kw):
    return dict(mode='teinte', name0=name0, h0=h0, h1=h1, center=center, variants=variants, **kw)

def G(name0, variants, **kw):
    return dict(mode='gris', name0=name0, variants=variants, **kw)

CFG = {
 # ---- lot 1
 'robot': T('Bleu', 0.50, 0.70, 0.59, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Orange', ORANGE, 1, 1.05), ('Rose', ROSE, 0.8, 1.1), ('Noir', 0.62, 0.2, 0.45)], vmin=0.3, skip=[(0.28, 0.28, 0.72, 0.62, ('big', 'down')), (0.45, 0.15, 1.0, 0.5, ('right',))]),
 'ours': T('Rouge', 0.95, 0.025, 0.99, [('Bleu', BLEU, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Jaune', JAUNE, 1, 1.15), ('Noir', 0, 0.15, 0.45), ('Cyan', CYAN, 1, 1.05)], smin=0.55),
 'chevalier': T('Bleu', 0.54, 0.70, 0.61, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Noir', 0.62, 0.2, 0.45), ('Orange', ORANGE, 1, 1.05), ('Rose', ROSE, 0.8, 1.1)], smin=0.4),
 'sorciere': T('Violet', 0.64, 0.92, 0.75, [('Rouge', ROUGE, 1, 1), ('Bleu', BLEU, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Noir', 0.75, 0.2, 0.5), ('Orange', ORANGE, 1.1, 1.2), ('Rose', ROSE, 0.8, 1.1)], squeeze=0.5),
 'aigle': T('Bleu', 0.50, 0.68, 0.57, [('Rouge', ROUGE, 1, 0.95), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Jaune', JAUNE, 1, 1.1), ('Noir', 0.6, 0.15, 0.45), ('Blanc', 0.6, 0.1, 1.4)]),
 'ninja': T('Rouge', 0.93, 0.04, 0.99, [('Bleu', BLEU, 1, 1.05), ('Vert', VERT, 0.95, 0.95), ('Jaune', JAUNE, 1, 1.15), ('Violet', VIOLET, 1, 1), ('Blanc', 0, 0.1, 1.4), ('Cyan', CYAN, 1, 1.05)], smin=0.5),
 'rodeur': T('Violet', 0.70, 0.95, 0.82, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Bleu', BLEU, 1, 1), ('Orange', ORANGE, 1, 1.05), ('Noir', 0.8, 0.15, 0.5), ('Cyan', CYAN, 1, 1.05)], squeeze=0.5),
 'amazone': T('Rouge', 0.94, 0.03, 0.985, [('Bleu', BLEU, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Noir', 0, 0.15, 0.45), ('Blanc', 0, 0.1, 1.45), ('Rose', ROSE, 0.8, 1.1)], smin=0.55, vmin=0.08),
 'matou': T('Bleu', 0.58, 0.82, 0.69, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', 0.8, 1, 1), ('Noir', 0.68, 0.2, 0.5), ('Orange', ORANGE, 1, 1.05), ('Rose', ROSE, 0.8, 1.1)], squeeze=0.6),
 'petardier': T('Rouge', 0.94, 0.03, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Jaune', JAUNE, 1, 1.2), ('Noir', 0, 0.15, 0.5), ('Rose', ROSE, 0.8, 1.15)], smin=0.5, vmin=0.08),
 # ---- lot 2
 'renard': T('Vert', 0.16, 0.38, 0.24, [('Bleu', 0.57, 1, 1), ('Rouge', 0.0, 1, 1), ('Violet', 0.78, 0.9, 1), ('Orange', 0.07, 1, 1), ('Cyan', 0.49, 1, 1), ('Rose', 0.9, 0.7, 1.05)], smin=0.4, vmin=0.25, min_area=60, squeeze=0.6),
 'salpetre': T('Rouge', 0.93, 0.025, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.15, 0.5), ('Cyan', CYAN, 1, 1.15), ('Rose', ROSE, 0.8, 1.15)], smin=0.5, vmin=0.1),
 'barde': T('Bordeaux', 0.86, 0.01, 0.95, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Rouge', ROUGE, 1, 1.05), ('Noir', 0.95, 0.15, 0.5), ('Orange', ORANGE, 1, 1.2), ('Violet', VIOLET, 1, 1.1)], smin=0.4, vmin=0.1, squeeze=0.6),
 'chatbotte': T('Rouge', 0.94, 0.025, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.15, 0.5), ('Jaune', JAUNE, 1, 1.2), ('Rose', ROSE, 0.8, 1.15)], smin=0.55, vmin=0.1),
 'gobelin': T('Vert', 0.12, 0.30, 0.2, [('Bleu', 0.58, 0.9, 1), ('Rouge', 0.0, 0.9, 0.95), ('Violet', 0.78, 0.8, 0.95), ('Gris', 0.2, 0.15, 0.9), ('Orange', 0.07, 1, 1.05), ('Turquoise', 0.46, 0.9, 1)], smin=0.3, vmin=0.15, squeeze=0.7),
 'cramoisi': T('Rouge', 0.9, 0.03, 0.98, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.12, 0.5), ('Orange', ORANGE, 1, 1.2), ('Cyan', CYAN, 1, 1.1)], smin=0.45, vmin=0.08),
 'karateka': G('Blanc', [('Bleu', BLEU, 0.55, 0.85), ('Noir', 0.6, 0.1, 0.3), ('Rouge', ROUGE, 0.55, 0.85), ('Jaune', 0.13, 0.5, 0.95), ('Vert', VERT, 0.45, 0.8), ('Rose', ROSE, 0.35, 0.95)], smax=0.18, vmin=0.55, min_area=300),
 'pilote': T('Bleu marine', 0.56, 0.72, 0.64, [('Bordeaux', ROUGE, 1, 1.5), ('Vert', VERT, 0.95, 1.4), ('Noir', 0.64, 0.12, 0.6), ('Violet', VIOLET, 1, 1.4), ('Blanc', 0.6, 0.08, 2.6), ('Bleu ciel', 0.57, 0.8, 1.9)], smin=0.25, vmin=0.06),
 'commando': G('Noir', [('Kaki', 0.2, 0.45, 1.0, 0.06), ('Sable', 0.1, 0.4, 1.2, 0.12), ('Marine', 0.6, 0.5, 1.0, 0.04), ('Rouge', ROUGE, 0.55, 1.0, 0.04), ('Blanc', 0.6, 0.05, 1.3, 0.3), ('Rose', ROSE, 0.4, 1.1, 0.1)], smax=0.2, vmin=0.04, vmax=0.8, min_area=200),
 'mineur': T('Rouge', 0.93, 0.03, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.12, 0.5), ('Blanc', 0, 0.08, 1.5), ('Rose', ROSE, 0.8, 1.15)], smin=0.5, vmin=0.1),
 'cowboy': T('Rouge', 0.93, 0.03, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.12, 0.5), ('Jaune', JAUNE, 1, 1.2), ('Rose', ROSE, 0.8, 1.15)], smin=0.6, vmin=0.25, skip=[(0, 0, 1, 0.34)]),
}
