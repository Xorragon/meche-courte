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
}
