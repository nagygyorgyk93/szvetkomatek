# -*- coding: utf-8 -*-
"""4e/06 — valós nyílt adatok a valószínűség- és statisztika-oldalakhoz (letöltve 2026-09-28).

Kizárólag nyilvános, összesített adat; a nyers letöltések a repón kívül: projektek/szvetkomatek/4e/adatok_06/.
Minden oldalon, ahol az adat megjelenik, a FORRAS megfelelő sorát fel kell tüntetni."""

FORRAS = {
    "popis": ("Republički zavod za statistiku (RZS): Popis stanovništva, domaćinstava i stanova 2022, Excel-táblák",
              "https://popis2022.stat.gov.rs/sr-latn/popisni-podaci-eksel-tabele/"),
    "eurostat": ("Eurostat: Live births by mother's age and newborn's sex (demo_fasec)",
                 "https://ec.europa.eu/eurostat/databrowser/view/demo_fasec/default/table"),
    "openmeteo": ("Open-Meteo Historical Weather API (ERA5-reanalízis, Copernicus), CC BY 4.0",
                  "https://open-meteo.com/en/docs/historical-weather-api"),
    "titanic": ("Vanderbilt University, Department of Biostatistics: titanic3 (F. E. Harrell)",
                "https://hbiostat.org/data/"),
    "jokic": ("Nikola Jokić NBA-alapszakasz statisztikái (Wikipedia, az NBA hivatalos adatai alapján)",
              "https://en.wikipedia.org/wiki/Nikola_Joki%C4%87"),
    "penz": ("Történeti pénzfeldobás-kísérletek: G.-L. L. de Buffon (18. sz.), K. Pearson (1900 körül), J. E. Kerrich "
             "(1946; közli D. Freedman, R. Pisani, R. Purves: Statistics)", ""),
}

# Népesség a népszámlálások szerint (fő). szabadka_varos = Szabadka város (grad), szabadka_telepules = a település. Forrás: FORRAS['popis']
NEPESSEG = {'evek': [1948, 1953, 1961, 1971, 1981, 1991, 2002, 2011, 2022],
 'szerbia': [6527583, 6978119, 7641962, 8446726, 9313686, 7822795, 7498001, 7186862, 6647003],
 'szabadka_varos': [123688, 126559, 136782, 146770, 154611, 150534, 148401, 141554, 123952],
 'szabadka_telepules': [62715, 65718, 74604, 88302, 99840, 99515, 99283, 97910, 88752]}

# Népesség 2022-ben, 5 éves korcsoportok szerint (az utolsó: 85 és több); atlagkor = átlagéletkor. Forrás: FORRAS['popis']
KOR = {'csoportok': ['0–4', '5–9', '10–14', '15–19', '20–24', '25–29', '30–34', '35–39', '40–44', '45–49', '50–54', '55–59',
               '60–64', '65–69', '70–74', '75–79', '80–84', '85 и више'],
 'szerbia': {'osszes': {'ossz': 6647003,
                        'csoport': [310928, 321202, 323322, 337351, 337105, 373087, 401653, 451556, 472169, 475882,
                                    453104, 448883, 471906, 502140, 434378, 239194, 175492, 117651],
                        'atlagkor': 43.85},
             'ferfi': {'ossz': 3231978,
                       'csoport': [160197, 165302, 166740, 172986, 172013, 190414, 203800, 228321, 238432, 237906,
                                   223511, 216635, 222891, 230917, 191641, 99381, 68610, 42281],
                       'atlagkor': 42.43},
             'no': {'ossz': 3415025,
                    'csoport': [150731, 155900, 156582, 164365, 165092, 182673, 197853, 223235, 233737, 237976,
                                229593, 232248, 249015, 271223, 242737, 139813, 106882, 75370],
                    'atlagkor': 45.19}},
 'szabadka': {'osszes': {'ossz': 123952,
                         'csoport': [6090, 6032, 5957, 6286, 6039, 6548, 7108, 8473, 9153, 8974, 8122, 8794, 9060,
                                     9355, 7781, 4881, 3256, 2043],
                         'atlagkor': 43.92},
              'ferfi': {'ossz': 59602,
                        'csoport': [3148, 3080, 3094, 3136, 3170, 3355, 3600, 4240, 4649, 4575, 4045, 4178, 4265,
                                    4120, 3319, 1907, 1126, 595],
                        'atlagkor': 42.09},
              'no': {'ossz': 64350,
                     'csoport': [2942, 2952, 2863, 3150, 2869, 3193, 3508, 4233, 4504, 4399, 4077, 4616, 4795, 5235,
                                 4462, 2974, 2130, 1448],
                     'atlagkor': 45.62}}}

# Háztartások 2022-ben taglétszám szerint: 1, 2, 3, 4, 5, 6 vagy több tag; atlag = átlagos taglétszám. Forrás: FORRAS['popis']
HAZTARTAS = {'szerbia': {'ossz': 2589344, 'tag_1_5_6plusz': [773945, 711946, 459926, 375565, 156050, 111912], 'atlag': 2.55},
 'szabadka': {'ossz': 52491, 'tag_1_5_6plusz': [17702, 15440, 9110, 6817, 2257, 1165], 'atlag': 2.33}}

# A 15 éves és idősebb népesség számítógépes ismerete 2022-ben. Forrás: FORRAS['popis']
SZAMITOGEP = {'oszlopok': ['összes', 'ismeri', 'részben ismeri', 'nem ismeri', 'ismeretlen'],
 'szerbia': {'osszes': [5691551, 2602550, 1685824, 1376725, 26452],
             'ferfi': [2739739, 1227972, 889986, 608298, 13483],
             'no': [2951812, 1374578, 795838, 768427, 12969]},
 'szabadka': {'osszes': [105873, 45792, 34820, 24667, 594],
              'ferfi': [50280, 21006, 18177, 10790, 307],
              'no': [55593, 24786, 16643, 13877, 287]}}

# Élveszületések: RS = Szerbia, HU = Magyarország; M = fiú, F = lány, T = összes. Forrás: FORRAS['eurostat']
SZULETES = {'HU_F': {2019: 45116, 2020: 45534, 2021: 45520, 2022: 43592, 2023: 42590, 2024: 38028},
 'RS_F': {2019: 31262, 2020: 29909, 2021: 30209, 2022: 30434, 2023: 29711, 2024: 29449},
 'HU_M': {2019: 47984, 2020: 48273, 2021: 48483, 2022: 46077, 2023: 45081, 2024: 40840},
 'RS_M': {2019: 33137, 2020: 31783, 2021: 31971, 2022: 32266, 2023: 31341, 2024: 31396},
 'HU_T': {2019: 93100, 2020: 93807, 2021: 94003, 2022: 89669, 2023: 87671, 2024: 78868},
 'RS_T': {2019: 64399, 2020: 61692, 2021: 62180, 2022: 62700, 2023: 61052, 2024: 60845}}

# 2024 napi adataiból: havi középhőmérséklet (°C), esős nap (≥ 1 mm csapadék) havonta. Forrás: FORRAS['openmeteo']
IDOJARAS_2024 = {'szabadka': {'havi_kozep': [2.5, 8.9, 10.3, 14.6, 18.7, 23.1, 26.4, 26.7, 19.1, 12.9, 4.6, 2.5],
              'esos_nap_havonta': [11, 5, 7, 6, 8, 10, 3, 3, 9, 6, 4, 7],
              'havi_csapadek_mm': [42.2, 21.6, 20.8, 33.7, 50.1, 80.7, 13.7, 8.7, 79.3, 44.2, 40.4, 52.7],
              'napok': 366,
              'eves_kozep': 14.2},
 'split': {'havi_kozep': [8.0, 11.0, 12.3, 15.7, 18.9, 23.8, 28.4, 28.6, 21.4, 18.4, 11.7, 8.1],
           'esos_nap_havonta': [12, 8, 16, 6, 15, 9, 1, 5, 10, 10, 7, 9],
           'napok': 366,
           'eves_kozep': 17.22},
 'lisszabon': {'havi_kozep': [13.1, 14.2, 13.8, 16.6, 17.6, 19.6, 22.4, 22.8, 20.5, 18.6, 16.3, 12.2],
               'esos_nap_havonta': [11, 9, 14, 6, 2, 8, 2, 0, 4, 12, 11, 3],
               'napok': 366,
               'eves_kozep': 17.31}}

# A Titanic 1309 utasa: [túlélt, nem élte túl]. Forrás: FORRAS['titanic']
TITANIC = {'utas': 1309,
 'nem': {'no': [339, 127], 'ferfi': [161, 682]},
 'osztaly': {'1': [200, 123], '2': [119, 158], '3': [181, 528]},
 'jelentes': '[túlélt, nem élte túl]'}

# Alapszakasz szezononként: lejátszott meccs, büntető-arány, pont/meccs. Forrás: FORRAS['jokic']
JOKIC = [{'szezon': '2015–16', 'meccs': 80, 'bunteto': 0.811, 'pont': 10.0},
 {'szezon': '2016–17', 'meccs': 73, 'bunteto': 0.825, 'pont': 16.7},
 {'szezon': '2017–18', 'meccs': 75, 'bunteto': 0.85, 'pont': 18.5},
 {'szezon': '2018–19', 'meccs': 80, 'bunteto': 0.821, 'pont': 20.1},
 {'szezon': '2019–20', 'meccs': 73, 'bunteto': 0.817, 'pont': 19.9},
 {'szezon': '2020–21', 'meccs': 72, 'bunteto': 0.868, 'pont': 26.4},
 {'szezon': '2021–22', 'meccs': 74, 'bunteto': 0.81, 'pont': 27.1},
 {'szezon': '2022–23', 'meccs': 69, 'bunteto': 0.822, 'pont': 24.5},
 {'szezon': '2023–24', 'meccs': 79, 'bunteto': 0.817, 'pont': 26.4},
 {'szezon': '2024–25', 'meccs': 70, 'bunteto': 0.8, 'pont': 29.6},
 {'szezon': '2025–26', 'meccs': 65, 'bunteto': 0.831, 'pont': 27.7}]

# Történeti pénzfeldobás-sorozatok. Forrás: FORRAS['penz']
PENZFELDOBAS = [{'ki': 'Buffon', 'dobas': 4040, 'fej': 2048}, {'ki': 'Kerrich', 'dobas': 10000, 'fej': 5067},
 {'ki': 'Pearson', 'dobas': 24000, 'fej': 12012}]

