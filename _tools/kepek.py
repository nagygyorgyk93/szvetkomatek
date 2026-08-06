# -*- coding: utf-8 -*-
"""Karakterképek beszúrása a .brief dobozokba.

  - az s0 (Küldetés-eligazítás) brief, ha a szereplőnek van fekvő képe → banner
  - minden más brief → kerek avatar (a SZVETI-minta szerint)
Használat: python kepek.py <web-gyoker> [--apply]
"""
import os, re, sys, collections

# név → (avatar-törzs, van-e fekvő változat)
KAR = {
    'SZVETI': ('svetozar', False),
    'Ikol': ('ikol', True),
    'Dr. Bizarr': ('dr_bizarr', True),
    'Petar Pauk': ('pauk_petar', True),
    'Barton Kálmán': ('barton_kalman', True),
    'Iruhs': ('iruhs', False),
    'Banner Brúnó': ('banner_bruno', True),
    'Banner': ('banner_bruno', True),
    'Brúnó': ('banner_bruno', True),
    'Hangya Henrik': ('hangya_henrik', False),
    'Darázs Dorka': ('darazs_dorka', False),
    'Vanda': ('vanda', False),
    'Fürge Pjotr': ('furge_pjotr', True),
    'Krats Ynot': ('krats_ynot', True),
    'Denveri Karolina': ('denveri_karolina', False),
    'Nikola Furić parancsnok': ('furic_nikola', False),
    'Nikola Furić': ('furic_nikola', False),
    'X. Károly professzor': ('x_karoly', True),
    'X. Károly': ('x_karoly', True),
    'Nagol hadnagy': ('nagol', True),
    'Nagol': ('nagol', True),
    'Vihar Vera': ('vihar_vera', False),
    'Dr. Bestia': ('dr_bestia', False),
    'Küklopsz': ('kuklopsz', False),
    'Magnetron': ('magnetron', True),
    'Szürke Janka': ('szurke_janka', False),
    'Crni Grom': ('crni_grom', False),
    'Medúza': ('meduza', False),
    'Kanrak': ('kanrak', False),
    'Prizma': ('prisma', False),
    'Tér-eb': ('ter_eb', False),
    'Véd Vilmos': ('ved_vilmos', True),
    'Véd-eb': ('ved_eb', False),
    'Mini-Vili': ('baby_vili', False),
}

ALT = {
    'SZVETI': 'a Szvetkó-kampusz mesterséges intelligenciája',
    'Ikol': 'az igaz és a hamis mestere',
    'Dr. Bizarr': 'a multiverzum térképésze',
    'Petar Pauk': 'a hálók és a függvények mestere',
    'Barton Kálmán': 'a kampusz célzó-oktatója',
    'Iruhs': 'a kampusz fejlesztőmérnöke',
    'Banner Brúnó': 'a mérés és a hibabecslés tudósa',
    'Banner': 'a mérés és a hibabecslés tudósa',
    'Brúnó': 'a mérés és a hibabecslés tudósa',
    'Hangya Henrik': 'a méretarányok szakértője',
    'Darázs Dorka': 'a Zsugor-protokoll pilótája',
    'Vanda': 'a valóságformálás mestere',
    'Fürge Pjotr': 'a kampusz leggyorsabb kadétja',
    'Krats Ynot': 'a kampusz fővezető mérnöke',
    'Denveri Karolina': 'kiképzőtiszt',
    'Nikola Furić parancsnok': 'az Akadémia igazgatója',
    'Nikola Furić': 'az Akadémia igazgatója',
    'X. Károly professzor': 'a Mutáns Osztag alapítója',
    'X. Károly': 'a Mutáns Osztag alapítója',
    'Nagol hadnagy': 'a morcos kiképzőtiszt',
    'Nagol': 'a morcos kiképzőtiszt',
    'Vihar Vera': 'az időjárás úrnője',
    'Dr. Bestia': 'a kampusz fővezető tudósa',
    'Küklopsz': 'az optikai sugarak mestere',
    'Magnetron': 'a mágneses mezők ura',
    'Szürke Janka': 'a telepata bemérő-specialista',
    'Crni Grom': 'a Néma Király',
    'Medúza': 'a Királyi Család hangja',
    'Kanrak': 'a rendszerek és töréspontok mestere',
    'Prizma': 'a térgeometria oktatótisztje',
    'Tér-eb': 'a teleportáló kutya',
    'Véd Vilmos': 'a negyedik falat áttörő zsoldos',
    'Véd-eb': 'a nyomravezető kutya',
    'Mini-Vili': 'a legkisebb variáns',
}

# <div class="brief"...><p>IKON <b>NÉV:</b>
BRIEF = re.compile(
    r'<div class="brief"(?P<attr>[^>]*)>\s*<p>(?P<elo>[^<]*)<b>(?P<nev>[^<]{1,70}):</b>')

# a névből az ELSŐ szereplőt vesszük ("Iruhs &amp; Krats Ynot" → Iruhs)
def elso_nev(s):
    s = re.split(r'\s*(?:&amp;|&|,)\s*', s)[0].strip()
    return s


def gyoker(p, web):
    mely = os.path.relpath(web, os.path.dirname(p)).replace('\\', '/')
    return mely + '/' if mely != '.' else ''


def main():
    web = os.path.abspath(sys.argv[1])
    ir = '--apply' in sys.argv
    stat = collections.Counter()
    kihagy = collections.Counter()
    fajlszam = 0

    for r, ds, fs in os.walk(web):
        ds[:] = [d for d in ds if d not in ('.git', '_tools', 'assets')]
        for f in fs:
            if not f.endswith('.html'):
                continue
            p = os.path.join(r, f)
            t = open(p, encoding='utf-8', newline='').read()
            elotag = gyoker(p, web)
            elso_brief = [True]     # az első brief kaphat banner-t

            def csere(m):
                nyers = m.group('nev')
                nev = elso_nev(nyers)
                if nev not in KAR:
                    kihagy[nev] += 1
                    return m.group(0)
                torzs, van_fekvo = KAR[nev]
                alt = f'{nev} — {ALT.get(nev, "a Szvetkó-kampusz szereplője")}'
                attr = m.group('attr')
                banner = elso_brief[0] and van_fekvo and 'data-outro' not in attr
                elso_brief[0] = False
                if banner:
                    stat['banner'] += 1
                    img = (f'<img class="portre" src="{elotag}assets/img/kar/{torzs}_w.webp" '
                           f'alt="{alt}" width="1200" height="670" decoding="async">')
                    return (f'<div class="brief karakter-nagy"{attr}>{img}'
                            f'<p>{m.group("elo")}<b>{nyers}:</b>')
                stat['avatar'] += 1
                img = (f'<img class="avatar" src="{elotag}assets/img/kar/{torzs}.webp" '
                       f'alt="{alt}" width="320" height="320" loading="lazy" decoding="async">')
                return (f'<div class="brief karakter"{attr}>{img}'
                        f'<p>{m.group("elo")}<b>{nyers}:</b>')

            uj = BRIEF.sub(csere, t)
            if uj != t:
                fajlszam += 1
                if ir:
                    open(p, 'w', encoding='utf-8', newline='').write(uj)

    print(f"{'ÍRVA' if ir else 'SZÁRAZ'}: {fajlszam} fájl · "
          f"{stat['banner']} banner + {stat['avatar']} avatar")
    if kihagy:
        print("\nkihagyva (nincs hozzá kép):")
        for n, c in kihagy.most_common():
            print(f"  {c:3d}  {n}")


if __name__ == '__main__':
    main()
