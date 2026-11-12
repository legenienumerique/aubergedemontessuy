"""Générateur de la maquette Auberge de Montessuy. Usage : python build.py <dossier-du-projet>
Contenus relevés sur auberge-de-montessuy.fr et la fiche Ain Tourisme (novembre 2026). Rien d'inventé : textes, photos, carte, prix, coordonnées."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 1  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '04 74 45 01 51', 'tel:0474450151'
MAIL = 'info@auberge-de-montessuy.fr'
ADR = ('Route de Marlieux', '01400 Châtillon-sur-Chalaronne')
OUV = 'Ouvert tous les jours sauf dimanche soir et lundi.'
NAV = [('auberge.html', 'L’Auberge'), ('carte.html', 'La carte'), ('evenements.html', 'Événements')]


def pill(t, href, cls='', arrow='↗', ext=False):
    x = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="pill {cls}" href="{href}"{x}><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><img src="{A}logo.png" alt=""><span><span class="wm">Auberge <i>de Montessuy</i></span><small>Dombes · Bresse</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('reserver.html', 'Réserver', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#0d1528">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Philosopher:wght@400;700&family=Open+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Auberge de Montessuy, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg><span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Nichée au cœur de la Dombes, une vraie pause gourmande dans une ambiance chaleureuse. La cuisine de nos terroirs, entre Dombes et Bresse.</p></div>
<div><h4 class="micro">L’Auberge</h4><ul><li><a href="auberge.html">Notre maison</a></li><li><a href="carte.html">La carte et les menus</a></li><li><a href="evenements.html">Séminaires et événements</a></li><li><a href="reserver.html">Réserver une table</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
<div><h4 class="micro">Nous trouver</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li><li>Parking privé</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">MONTESSUY</div>
<div class="fb micro"><span class="pad">© Auberge de Montessuy</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Une table <em>vous attend</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Réservation conseillée · parking privé</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Réserver une table', 'reserver.html', 'blue')}{pill(TEL, TELH, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


# carte automne 2026 (à partir du 10/10), relevée sur le site
CARTE = [
    ('Entrées', [('Encornet farci', 'Rillettes de poissons et crevettes, pickles d’oignons rouges, mayonnaise à la rouille, tuile à l’encre de seiche', '16 €'),
                 ('Foie gras de canard', 'Terrine du Sud-Ouest (80 g), compotée de pomme au safran, mendiant au chocolat 72 % et noisettes', '25 €'),
                 ('Escargots de Bourgogne', 'Poêlés au beurre et cognac, duxelles de champignons, mousse crémeuse de persillade', '19 €'),
                 ('Salade de l’Auberge', 'Croustillant de Cabécou au thym, jambon cru de Savoie, poires rôties, noix du Montessuy', '17 €'),
                 ('Velouté de butternut et foie gras', 'Éclats de châtaignes, mouillette croustillante au foie gras, poivre de Timut', '19 €'),
                 ('Saint-Jacques rôties', 'Fondue de poireau, mousseline de céleri à la vanille de Madagascar, crème de haddock fumé', '26 €')]),
    ('Volailles et viandes', [('Pintade fermière en Chartreuse', 'Choux vert, jus de rôti corsé, moutarde à l’ancienne, crémeux de céleri', '23 €'),
                              ('Poulet fermier Label Rouge aux morilles', 'À la crème, crêpes parmentières aux herbes fraîches et légumes', '28 €'),
                              ('Ris de veau', 'Cœur de ris de veau rôti, tarte fine aux figues, pickles de girolles', '33 €'),
                              ('Filet de faisan', 'Cuisson douce, gratin de chou-fleur coloré, jus court au poivre long de Java', '28 €'),
                              ('Filet de bœuf Rossini', 'Foie gras poêlé, brioche truffée, pomme Anna, jus réduit au vieux porto', '34 €')]),
    ('Poissons et risotto', [('Poisson du moment', 'Tapenade d’olive kalamata, crème safranée, petit épeautre et légumes', '27 €'),
                             ('Grenouilles fraîches persillées', 'Cuisinées au beurre, 300 g, gratin bressan, en 2 services', '33 €'),
                             ('Risotto aux cèpes', 'Arborio monté à la crème de champignons, cèpes poêlés, légumes acidulés', '23 €')]),
    ('Fromages et desserts', [('Desserts maison', 'Notre sélection du moment', 'dès 9,50 €'),
                              ('Faisselle traditionnelle', 'Servie à votre goût', '5 €'),
                              ('Saint-marcellin affiné', '', '8,50 €'),
                              ('Dégustation de fromages affinés', '', '9 €')]),
]
MENUS = [('Menu affaire', '18 €', 'Le midi, du mardi au vendredi (hors jours fériés)', ['Entrée du jour', 'Plat du jour', 'Dessert du jour']),
         ('Menu de l’Auberge', '32 €', 'Du mardi au samedi (hors jours fériés)', ['Encornet farci ou entrée du jour', 'Pintade fermière en Chartreuse', 'Faisselle, glaces ou dessert']),
         ('Menu de la Dombes', '36 €', 'Le grand classique du pays', ['Poulet fermier de la Dombes aux morilles ou grenouilles fraîches persillées (250 g)', 'Faisselle ou dessert à la carte']),
         ('Menu de Montessuy', '41 €', 'Selon votre envie', ['Une entrée au choix', 'Un plat au choix', 'Un dessert à la carte']),
         ('Menu dégustation', '47 €', 'Pour les amateurs', ['Grenouilles fraîches persillées (200 g)', 'Poulet fermier Label Rouge aux morilles', 'Fromage ou dessert'])]


def pages():
    P = {}
    hero_tiles = [('t1', 'm02'), ('t2', 'm08'), ('t3', 'm29'), ('t4', 'm05'), ('t5', 'm22'), ('t6', 'm10'), ('t7', 'm06')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{PH}{f}.webp" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(f'{PH}{f}.webp') for f in ['m22', 'm25', 'm19', 'm29', 'm32', 'm30', 'm33', 'm23'])
    wall_imgs = ['m02', 'm19', 'm29', 'm30', 'm31', 'm32', 'm33', 'm23', 't03', 'm27', 'm10', 'm24']
    wall = ''.join(tile(f'{PH}{wall_imgs[i % len(wall_imgs)]}.webp') for i in range(54))
    items = [('auberge.html', '01', 'Le restaurant', 'Salle et cheminée, véranda lumineuse, terrasse sur le jardin.', 'm08', 'Midi · soir'),
             ('carte.html', '02', 'La carte', 'Cuisine de saison, menus de 18 à 47 €, grenouilles fraîches.', 'm29', 'Automne 2026'),
             ('evenements.html', '03', 'Événements', 'Deux salles modulables de 80 et 40 couverts, séminaires.', 'm20', 'Sur mesure'),
             ('reserver.html', '04', 'Réserver', 'En ligne ou au téléphone. Réservation conseillée.', 't02', TEL)]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>{b}</b></span></a>' for h, n, t, d, _, b in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    track = ''.join(f'<figure class="tile"><img src="{PH}{f}.webp" alt="{l}" loading="lazy"><span class="tag">{l}</span></figure>' for f, l in [
        ('m29', 'Foie gras'), ('m30', 'De saison'), ('m02', 'Poisson'), ('m32', 'Volaille'), ('m25', 'Desserts maison'), ('m27', 'Cave à vin')])
    steps = [('Vous réservez', f'En ligne en 30 secondes, ou au {TEL}.'),
             ('Vous arrivez', 'Route de Marlieux, parking privé.'),
             ('Vous choisissez', 'À la carte ou l’un de nos cinq menus.'),
             ('Vous savourez', 'Le meilleur de la Dombes et de la Bresse.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Grenouilles fraîches', 'Volaille de Bresse', 'Cuisine de saison', 'Cave à vin', 'Produits locaux', 'Fait maison'] * 2)

    P['index.html'] = head('Auberge de Montessuy — Restaurant à Châtillon-sur-Chalaronne, au cœur de la Dombes', 'Auberge de Montessuy, route de Marlieux à Châtillon-sur-Chalaronne : cuisine de saison entre Dombes et Bresse, grenouilles fraîches, menus de 18 à 47 €, salles pour séminaires. 04 74 45 01 51.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Goûtez</b>la différence</div>
<div class="cap micro c2"><b>Dombes et Bresse</b>la cuisine de nos terroirs</div>
<div class="cap micro c3"><b>Depuis des générations</b>à Châtillon</div>
<div class="go">{pill('Réserver une table', 'reserver.html')}</div>
{ht}
<p class="para">Un havre de paix, une vraie pause gourmande.</p>
<h1 class="word">MONTESSUY</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Ambiance feutrée</span><h2 class="sp">Un lieu de charme <em>et de tradition</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Ici, l’art du bien-manger s’accompagne de l’art du bien-recevoir. Tout est mis en œuvre pour vous offrir des moments gourmands, simplement et naturellement.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Cuisine de saison</b>, gourmande et innovante.</span></li><li><span><b>Producteurs locaux</b> choisis avec soin.</span></li><li><span><b>Parking privé</b>, réservation conseillée.</span></li></ul>{pill('Découvrir l’Auberge', 'auberge.html', 'blue')}</div>{tile(PH + 'm08.webp', '', par=8, alt='La salle et sa cheminée')}</div></section>

<section class="story"><span class="micro mute m3">Notre cuisine</span>
<h2><span class="w">Une</span> <span class="w">cuisine</span> <span class="w">de</span> <span class="w">goût</span> <span class="w">et</span> <span class="w">de</span> <span class="w"><em>cœur</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Tradition et modernité. Le maître mot reste la qualité.</p><span class="micro mute m2">Fait maison</span></section>

<section class="wall"><div class="grid">{wall}</div><div class="mid"><span class="micro mute">Automne 2026</span><h2>La carte <em>de saison</em></h2>{pill('Voir la carte', 'carte.html', 'blue')}</div></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Bienvenue</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Que souhaitez-vous <em>découvrir ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="hz"><div class="pin"><div class="wrap top2"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">À table</span><h2>Le meilleur <em>de nos terroirs</em></h2></div>{pill('La carte', 'carte.html')}</div>
<div class="track">{track}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">En chiffres</span><h2 class="sp">Une maison <em>généreuse</em></h2>
<div class="cnt rv"><div><b data-to="5">0</b><span>menus, de 18 € le midi à 47 € en dégustation</span></div><div><b data-to="80">0</b><span>couverts dans notre grande salle modulable</span></div><div><b data-to="300">0</b><span>grammes de grenouilles fraîches persillées, en deux services</span></div></div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Une cave de caractère</span><h2 class="sp">Des vins <em>à l’image de notre cuisine</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Vins de notre terroir et de nos régions, grands classiques, petits producteurs à découvrir, ou évasion vers des terres plus lointaines.</p>{pill('Réserver une table', 'reserver.html', 'blue')}</div>{tile(PH + 'm27.webp', '', par=8, alt='Dégustation de vins au coucher du soleil')}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Votre venue</span><h2 class="sp">Simplement, <em>naturellement</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    P['auberge.html'] = head('L’Auberge — Auberge de Montessuy, Châtillon-sur-Chalaronne', 'Un lieu de charme et de tradition au cœur de la Dombes : salle avec cheminée, véranda, terrasse sur le jardin, cave à vin et produits de producteurs locaux.', 'auberge.html') + pagehead('L’Auberge', 'Un havre <em>de paix</em>', 'Nichée au cœur de la Dombes, l’Auberge est une vraie pause gourmande, dans une ambiance chaleureuse.', PH + 'm05.webp', PH + 'm16.webp') + f'''
<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Notre cuisine</span><h2 class="sp">Entre Dombes <em>et Bresse</em></h2>
<p class="lead rv" style="margin-top:1.4rem">L’Auberge de Montessuy perpétue son excellence depuis des générations. Une cuisine de saison et d’inspiration, gourmande et innovante, généreuse et source de plaisir. Menus ou à la carte.</p></div>{tile(PH + 'm22.webp', '', par=8, alt='Dressage d’une assiette en cuisine')}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nos produits</span><h2 class="sp">Une sélection <em>d’excellence</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Les produits sont le reflet de notre terroir. Nous créons une vraie relation de partenariat et de confiance avec nos producteurs locaux et régionaux, dont nous sélectionnons rigoureusement les produits.</p></div>{tile(PH + 'm24.webp', '', par=8, alt='Une table, une lampe et des bouteilles de vin')}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">En images</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Bienvenue <em>chez nous</em></h2>
<div class="flt" data-t=".gal figure"><button class="on" data-f="*">Tout</button><button data-f="Lieu">Le lieu</button><button data-f="Assiettes">Les assiettes</button></div>
{gal([('m08', 'Lieu', 'La salle et sa cheminée'), ('m29', 'Assiettes', 'Foie gras'), ('m06', 'Lieu', 'La véranda'), ('m02', 'Assiettes', 'Poisson et légumes'), ('m07', 'Lieu', 'La terrasse'), ('m19', 'Assiettes', 'Une assiette de saison'), ('m12', 'Lieu', 'La salle et son lustre'), ('m30', 'Assiettes', 'Cuisine de saison'), ('m21', 'Lieu', 'À la nuit tombée'), ('m33', 'Assiettes', 'Dessert maison'), ('t04', 'Lieu', 'Une table en terrasse'), ('m32', 'Assiettes', 'Volaille en sauce'), ('m18', 'Lieu', 'Lumières de la salle'), ('m31', 'Assiettes', 'Salade gourmande'), ('t00', 'Lieu', 'Les tables dressées')])}</div></section>''' + cta() + foot()

    tabs = ''.join(f'<button{" class=on" if i == 0 else ""} data-f="{c}">{c}</button>' for i, (c, _) in enumerate(CARTE))
    rows = ''.join(f'<div class="dish rv{"" if c == CARTE[0][0] else " hide"}" data-c="{c}"><div><h3>{n}</h3>{f"<p>{d}</p>" if d else ""}</div><b>{p}</b></div>' for c, its in CARTE for n, d, p in its)
    mn = ''.join(f'<div class="menu rv"><span class="micro mute">{s}</span><h3>{n}</h3><b>{p}</b><ul>{"".join(f"<li>{x}</li>" for x in its)}</ul></div>' for n, p, s, its in MENUS)
    P['carte.html'] = head('La carte et les menus — Auberge de Montessuy', 'Carte d’automne 2026 de l’Auberge de Montessuy : foie gras, Saint-Jacques, poulet fermier aux morilles, grenouilles fraîches, menus de 18 à 47 €.', 'carte.html') + pagehead('La carte', 'La carte <em>d’automne</em>', 'À partir du 10 octobre 2026. Une cuisine de saison, entre tradition et modernité.', PH + 'm29.webp', PH + 'm23.webp') + f'''
<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nos menus</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Cinq menus, <em>toutes les envies</em></h2><div class="menus">{mn}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">À la carte</span><h2 class="sp" style="margin-bottom:2rem">Choisissez <em>votre plat</em></h2>
<div class="flt" data-t=".dish">{tabs}</div><div class="dishes">{rows}</div>
<p class="note" style="margin-top:2rem">Jeunes convives : 25 % de remise sur les plats choisis à la carte. Tableau des allergènes et pain sans gluten disponibles. Prix relevés sur le site actuel, à confirmer avec l’Auberge.</p></div></section>''' + cta() + foot()

    P['evenements.html'] = head('Séminaires et événements — Auberge de Montessuy', 'Deux grandes salles modulables de 80 et 40 couverts, des extérieurs aménageables, des menus sur mesure et un service de plateaux-repas pour les entreprises.', 'evenements.html') + pagehead('Événements', 'Un accueil <em>sur mesure</em>', 'Événements d’exception, séminaires, réunions de travail : nous concevons ensemble l’événement qui vous ressemble.', PH + 'm20.webp', PH + 'm07.webp') + f'''
<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Nos espaces</span><h2 class="sp">Deux salles, <em>des extérieurs</em></h2>
<div class="cnt rv"><div><b data-to="80">0</b><span>couverts dans la grande salle modulable</span></div><div><b data-to="40">0</b><span>couverts dans la seconde salle</span></div><div><b data-to="1">0</b><span>jardin et terrasse aménageables</span></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Pour les entreprises</span><h2 class="sp">Le travail, <em>gourmand</em></h2></div>
<ul class="checks rv"><li><span><b>Séminaires et réunions.</b> Salles modulables et accueil personnalisé.</span></li><li><span><b>Menus adaptés</b> à vos besoins et à vos goûts.</span></li><li><span><b>Plateaux-repas</b> pour les entreprises.</span></li><li><span><b>Menu affaire à 18 €</b>, le midi du mardi au vendredi.</span></li></ul></div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Votre projet</span><h2 class="sp">Parlons <em>de votre événement</em></h2><p class="lead rv" style="margin-top:1.4rem">Appelez-nous au {TEL}, ou laissez-nous un message.</p></div>
<form class="f calc rv"><div class="r2"><div class="fld"><label for="n">Nom</label><input id="n" required></div><div class="fld"><label for="t">Téléphone</label><input id="t" type="tel" required></div></div>
<div class="r2"><div class="fld"><label for="ty">Type</label><select id="ty"><option>Séminaire ou réunion</option><option>Repas de famille</option><option>Événement d’exception</option><option>Plateaux-repas</option></select></div><div class="fld"><label for="g">Nombre de personnes</label><input id="g" type="number" min="1" max="120"></div></div>
<div class="fld"><label for="m">Votre message</label><textarea id="m" rows="4"></textarea></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Envoyer</span><span>Envoyer</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucun message n’est envoyé.)</div></form></div></section>''' + cta() + foot()

    cov = ''.join(f'<button type="button"{" class=on" if i == 2 else ""}>{i}</button>' for i in range(1, 9))
    P['reserver.html'] = head('Réserver une table — Auberge de Montessuy', f'Réservez votre table à l’Auberge de Montessuy, Châtillon-sur-Chalaronne. {OUV} {TEL}.', 'reserver.html') + pagehead('Réserver', 'Votre table <em>vous attend</em>', 'Choisissez le jour, le service et le nombre de couverts. Réservation conseillée.', PH + 't02.webp') + f'''
<section class="sec" id="reserver"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réservation en ligne</span><h2 class="sp">En <em>30 secondes</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Vous recevez une confirmation par e-mail. Pour un groupe, appelez-nous au <a href="{TELH}">{TEL}</a>.</p>
<div class="hor rv"><span><b>{OUV}</b></span><span>{ADR[0]}, {ADR[1]}</span><span class="micro">Horaires à confirmer avec l’Auberge</span></div></div>
<form class="f calc rv" id="resa"><div class="seg"><button type="button" class="on" data-m="table">Déjeuner</button><button type="button" data-m="table" data-s="soir">Dîner</button></div>
<div class="r2"><div class="fld"><label for="rd">Date</label><input id="rd" type="date" required></div><div class="fld"><label for="rh">Heure</label><select id="rh"><option>12 h 00</option><option>12 h 30</option><option>13 h 00</option><option>13 h 30</option></select></div></div>
<div class="fld"><label>Couverts</label><div class="cov">{cov}</div></div>
<div class="r2"><div class="fld"><label for="rn">Nom</label><input id="rn" required></div><div class="fld"><label for="rt">Téléphone</label><input id="rt" type="tel" required></div></div>
<div class="fld"><label for="re">E-mail</label><input id="re" type="email"></div>
<div class="fld"><label for="rm">Une occasion particulière ?</label><input id="rm" placeholder="Anniversaire, allergie, chaise bébé…"></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Réserver</span><span>Réserver</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucune réservation n’est envoyée.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
