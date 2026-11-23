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
 # ---- lot 3
 'dryade': T('Vert', 0.16, 0.38, 0.26, [('Orange', 0.07, 1, 1.05), ('Rouge', 0.0, 0.95, 0.95), ('Bleu', 0.56, 0.9, 1), ('Violet', 0.78, 0.8, 1), ('Rose', 0.92, 0.6, 1.1), ('Doré', 0.12, 1, 1.1)], smin=0.3, vmin=0.12, squeeze=0.5),
 'sac': T('Bleu', 0.5, 0.67, 0.56, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Jaune', JAUNE, 1, 1.1), ('Noir', 0.6, 0.12, 0.45), ('Rose', ROSE, 0.7, 1.1)], smin=0.25),
 'lutin': T('Vert', 0.15, 0.47, 0.27, [('Bleu', 0.6, 0.9, 1), ('Rouge', 0.0, 0.9, 0.95), ('Violet', 0.78, 0.8, 0.95), ('Orange', 0.07, 1, 1.05), ('Turquoise', 0.47, 0.9, 1), ('Rose', 0.9, 0.6, 1.1)], smin=0.3, vmin=0.12, squeeze=0.5),
 'golem': T('Bleu', 0.46, 0.66, 0.54, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 1, 1), ('Violet', VIOLET, 1, 1), ('Jaune', 0.13, 1, 1.05), ('Rose', ROSE, 0.8, 1.05), ('Orange', ORANGE, 1, 1.05)], smin=0.25, vmin=0.2, squeeze=0.6),
 'mecha': G('Blanc', [('Rouge', ROUGE, 0.5, 0.95), ('Bleu', BLEU, 0.5, 0.95), ('Noir', 0.6, 0.12, 0.38), ('Jaune', 0.13, 0.5, 1), ('Vert', VERT, 0.45, 0.9), ('Rose', ROSE, 0.35, 1)], smax=0.2, vmin=0.4, min_area=120, skip=[(0, 0, 1, 0.38), (0.2, 0.3, 0.8, 0.5, ('down',)), (0.3, 0.38, 0.7, 0.5, ('big',)), (0.4, 0.3, 0.95, 0.5, ('right',))]),
 'rockeuse': T('Auburn', 0.94, 0.05, 0.0, [('Blond', 0.11, 0.8, 1.35), ('Noir', 0.0, 0.3, 0.45), ('Bleu', BLEU, 0.9, 1.2), ('Rose', 0.92, 0.7, 1.35), ('Violet', VIOLET, 0.8, 1.2), ('Vert', VERT, 0.8, 1.15)], smin=0.42, vmin=0.12, skip=[(0.25, 0.3, 0.75, 0.68, ('big', 'down')), (0.4, 0.3, 0.95, 0.65, ('right',))]),
 'robotte': T('Rose', 0.8, 0.98, 0.9, [('Bleu', BLEU, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Rouge', ROUGE, 1, 0.95), ('Orange', ORANGE, 1, 1.05), ('Cyan', CYAN, 1, 1)], smin=0.25, vmin=0.2, squeeze=0.5),
 'hacker': T('Cyan', 0.44, 0.72, 0.56, [('Rouge', ROUGE, 1, 1), ('Vert', 0.33, 1, 1), ('Violet', VIOLET, 1, 1), ('Orange', ORANGE, 1, 1), ('Rose', ROSE, 0.85, 1), ('Jaune', 0.14, 1, 1)], smin=0.25, vmin=0.06, squeeze=0.5),
 'arcaniste': T('Violet', 0.62, 0.85, 0.71, [('Rouge', ROUGE, 1, 1), ('Bleu', 0.6, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Noir', 0.71, 0.12, 0.5), ('Orange', ORANGE, 1, 1.1), ('Cyan', CYAN, 1, 1)], smin=0.25, vmin=0.08, squeeze=0.5),
 'olympien': G('Blanc', [('Rouge', ROUGE, 0.55, 0.9), ('Bleu', BLEU, 0.55, 0.9), ('Vert', VERT, 0.45, 0.85), ('Violet', VIOLET, 0.45, 0.9), ('Noir', 0.6, 0.1, 0.35), ('Doré', 0.12, 0.6, 1)], smax=0.2, vmin=0.55, min_area=150, skip=[(0, 0, 1, 0.4)]),
 # ---- lot 4
 'legionnaire': T('Rouge', 0.93, 0.025, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.12, 0.5), ('Jaune', JAUNE, 1, 1.2), ('Rose', ROSE, 0.8, 1.15)], smin=0.5, vmin=0.1),
 'parrain': G('Noir', [('Bleu marine', 0.62, 0.6, 1.0, 0.08), ('Bordeaux', 0.98, 0.6, 1.0, 0.08), ('Blanc', 0.1, 0.06, 1.3, 0.45), ('Marron', 0.07, 0.5, 1.1, 0.1), ('Vert', 0.38, 0.5, 1.0, 0.07), ('Violet', 0.77, 0.55, 1.0, 0.08)], smax=0.22, vmin=0.03, vmax=0.62, min_area=200, skip=[(0.25, 0.22, 0.75, 0.5, ('big', 'down')), (0.4, 0.2, 0.95, 0.5, ('right',))]),
 'sable': T('Or', 0.05, 0.18, 0.11, [('Argent', 0.6, 0.12, 1.05), ('Rose', 0.94, 0.55, 1.05), ('Bleu', 0.57, 0.6, 1), ('Vert', 0.33, 0.6, 0.95), ('Violet', 0.78, 0.55, 1), ('Rouge', 0.01, 0.9, 0.95)], smin=0.25, vmin=0.15, squeeze=0.5),
 'elfe': T('Rouge', 0.93, 0.03, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.12, 0.5), ('Jaune', JAUNE, 1, 1.2), ('Rose', ROSE, 0.8, 1.15)], smin=0.5, vmin=0.1),
 'mandarin': T('Rouge', 0.93, 0.025, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.12, 0.5), ('Jade', 0.44, 0.9, 1.05), ('Rose', ROSE, 0.8, 1.15)], smin=0.55, vmin=0.1),
 'marie': G('Noir', [('Bleu marine', 0.62, 0.6, 1.0, 0.1), ('Bordeaux', 0.98, 0.6, 1.0, 0.1), ('Blanc', 0.1, 0.05, 1.3, 0.55), ('Gris', 0.6, 0.06, 1.2, 0.3), ('Vert', 0.38, 0.5, 1.0, 0.09), ('Violet', 0.77, 0.55, 1.0, 0.1)], smax=0.42, vmin=0.0, vmax=0.42, min_area=200, skip=[(0.2, 0.25, 0.8, 0.55, ('big', 'down')), (0.3, 0.25, 0.95, 0.52, ('right',)), (0, 0.22, 1, 0.5, ('up',))]),
 'mariee': G('Blanc', [('Rose', ROSE, 0.3, 1.0), ('Bleu', 0.58, 0.3, 0.97), ('Or', 0.12, 0.45, 1.0), ('Lilas', 0.76, 0.3, 0.97), ('Rouge', ROUGE, 0.55, 0.9), ('Noir', 0.7, 0.1, 0.32)], smax=0.14, vmin=0.6, min_area=200, skip=[(0.25, 0.15, 0.75, 0.48, ('big', 'down')), (0.4, 0.15, 0.95, 0.48, ('right',))]),
 'bricolo': T('Bleu', 0.5, 0.7, 0.6, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Jaune', JAUNE, 1, 1.1), ('Noir', 0.6, 0.12, 0.45), ('Rose', ROSE, 0.7, 1.1)], smin=0.3, vmin=0.1, squeeze=0.6),
 'momie': G('Lin', [('Vert', 0.3, 0.35, 1.0), ('Bleu', 0.58, 0.35, 1.0), ('Rose', ROSE, 0.3, 1.05), ('Noir', 0.08, 0.1, 0.45), ('Doré', 0.12, 0.5, 1.0), ('Violet', 0.77, 0.3, 1.0)], smax=0.3, vmin=0.35, min_area=150),
 'fee': T('Vert', 0.15, 0.5, 0.3, [('Bleu', 0.58, 0.9, 1), ('Rose', 0.92, 0.7, 1.1), ('Violet', 0.77, 0.8, 1), ('Orange', 0.07, 1, 1.05), ('Rouge', 0.0, 0.9, 0.95), ('Doré', 0.13, 1, 1.05)], smin=0.25, vmin=0.12, squeeze=0.5),
 'orc': T('Vert', 0.12, 0.30, 0.19, [('Bleu', 0.58, 0.9, 1), ('Rouge', 0.0, 0.9, 0.95), ('Violet', 0.78, 0.8, 0.95), ('Gris', 0.19, 0.15, 0.9), ('Orange', 0.07, 1, 1.05), ('Turquoise', 0.46, 0.9, 1)], smin=0.3, vmin=0.12, squeeze=0.7),
 'ondine': T('Bleu', 0.46, 0.7, 0.55, [('Rose', 0.92, 0.7, 1.05), ('Vert', 0.36, 0.9, 1), ('Violet', 0.77, 0.8, 1), ('Orange', 0.07, 1, 1.05), ('Rouge', 0.0, 0.9, 0.95), ('Doré', 0.13, 1, 1.05)], smin=0.2, vmin=0.12, squeeze=0.5),
 'papy': T('Bleu', 0.5, 0.67, 0.56, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Jaune', JAUNE, 1, 1.1), ('Noir', 0.6, 0.12, 0.45), ('Rose', ROSE, 0.7, 1.1)], smin=0.25),
 'peintre': T('Rouge', 0.93, 0.03, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.12, 0.5), ('Jaune', JAUNE, 1, 1.2), ('Rose', ROSE, 0.8, 1.15)], smin=0.55, vmin=0.12),
 'pompiere': T('Rouge', 0.93, 0.045, 0.99, [('Bleu', BLEU, 1, 1.1), ('Vert', VERT, 0.95, 1), ('Violet', VIOLET, 1, 1.05), ('Noir', 0, 0.12, 0.5), ('Jaune', JAUNE, 1, 1.2), ('Rose', ROSE, 0.8, 1.15)], smin=0.55, vmin=0.15, skip=[(0, 0.33, 1, 1)]),
 'sylve': T('Vert', 0.15, 0.4, 0.26, [('Orange', 0.07, 1, 1.05), ('Rouge', 0.0, 0.95, 0.95), ('Bleu', 0.56, 0.9, 1), ('Violet', 0.78, 0.8, 1), ('Rose', 0.92, 0.6, 1.1), ('Doré', 0.12, 1, 1.1)], smin=0.3, vmin=0.12, squeeze=0.5),
 'prospecteur': T('Bleu', 0.52, 0.7, 0.6, [('Rouge', ROUGE, 1, 1), ('Vert', VERT, 0.95, 0.95), ('Violet', VIOLET, 1, 1), ('Jaune', JAUNE, 1, 1.1), ('Noir', 0.6, 0.12, 0.45), ('Rose', ROSE, 0.7, 1.1)], smin=0.25, vmin=0.1),
}
