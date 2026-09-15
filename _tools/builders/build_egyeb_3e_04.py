# -*- coding: utf-8 -*-
"""3e/04 — F4 osszefoglalo (Irantyu-terkep), F5p terepkuldetes (A Kiralyi Iranyitotu),
F6h feladatok-hazi (Veszterem), F5 temakor-index. Mentor: Crni Grom (Meduza tolmacsol)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, abra, brief
from abra_common import svg_vektorialis

T = dict(tagozat="3e", mappa="04-vektorok", temakor="Vektorok")
KUL = "A Királyi Irányítótű"

# ---------------------------------------------------------------- önteszt
from sympy import Matrix, sqrt, acos, pi, Rational as Q, symbols, solve, simplify, N
E = []


def _egyenlo(g, w):
    if isinstance(g, (list, tuple)):
        return len(g) == len(w) and all(_egyenlo(a, b) for a, b in zip(g, w))
    if hasattr(g, "shape"):
        return g.shape == w.shape and all(simplify(a - b) == 0 for a, b in zip(g, w))
    return simplify(g - w) == 0


def chk(n, g, w, tur=None):
    ok = abs(float(N(g)) - float(w)) <= tur if tur is not None else _egyenlo(g, w)
    if not ok:
        E.append((n, g, w))


def V(*k):
    return Matrix(k)


def fok(u, w):
    return acos(u.dot(w) / (u.norm() * w.norm())) * 180 / pi


t, p_ = symbols("t p")
# --- F5p terepküldetés
P, Qp, R = V(1, 2, 0), V(3, 3, 2), V(1, 5, 4)
PQ, PR = Qp - P, R - P
S = Qp + R - P
chk("I-a", [PQ, PR, PQ.norm(), PR.norm()], [V(2, 1, 2), V(0, 3, 4), 3, 5])
chk("I-b", [S, S - R, Qp - P], [V(3, 6, 6), PQ, PQ])
chk("I-c", [(P + S) / 2, (Qp + R) / 2], [V(2, 4, 3), V(2, 4, 3)])
chk("I-d", P + Qp - R, V(3, 0, -2))
chk("II-a", [PQ.dot(PR)], [11]); chk("II-a-fok", fok(PQ, PR), 42.8, 0.05)
chk("II-c", solve((V(0, 0, t) - P).dot(PQ), t), [2])
chk("II-d", [V(1, 1, 1).dot(PQ), V(1, 1, 1).dot(PQ) / PQ.norm()], [5, Q(5, 3)])
chk("II-d-fok", fok(V(1, 1, 1), PQ), 15.8, 0.05)
n = PQ.cross(PR)
chk("III-a", [n, n.norm(), n.norm() / 2], [V(-2, -8, 6), 2*sqrt(26), sqrt(26)])
chk("III-a-k", sqrt(26), 5.10, 0.005); chk("III-a-k2", 2*sqrt(26), 10.20, 0.005)
chk("III-b", n / n.norm(), V(-1, -4, 3) / sqrt(26)); chk("III-b-k", 4 / sqrt(26), 0.784, 0.0005)
chk("III-c", 2*sqrt(26) / 3, 3.40, 0.005)
for U in (V(3, 0, -1), V(2, 4, -2)):
    chk("III-d", [(U - P).dot(PQ), (U - P).norm(), PQ.cross(U - P).norm() / 2], [0, 3, Q(9, 2)])
# --- F6h Vészterem
chk("h-a1", [V(-1, 1, 1) - V(2, -3, 1), (V(-1, 1, 1) - V(2, -3, 1)).norm()], [V(-3, 4, 0), 5])
chk("h-a2", 3*V(1, -2, 3) - 2*V(4, 0, -1), V(-5, -6, 11))
chk("h-a3", V(-3, 9, -6), -Q(3, 2) * V(2, -6, 4))
chk("h-a4", V(3, 1, -2).dot(V(2, -4, 1)), 0)
chk("h-a5", fok(V(2, 2, 1), V(1, 0, -1)), 76.4, 0.05)
chk("h-a6", V(1, -1, 2).cross(V(3, 0, 1)), V(-1, 5, 3))
chk("h-a7", [(V(2, 1, 3) - V(0, 1, 1)).cross(V(1, 3, 1) - V(0, 1, 1)), ((V(2, 1, 3) - V(0, 1, 1)).cross(V(1, 3, 1) - V(0, 1, 1))).norm() / 2],
    [V(-4, 2, 4), 3])
chk("h-a8", [V(1, 0, 2) + V(5, 3, 1) - V(4, 1, 0), (V(1, 0, 2) + V(5, 3, 1)) / 2], [V(2, 2, 3), V(3, Q(3, 2), Q(3, 2))])
chk("h-k1", solve(V(2, t, -1).dot(V(t, 4, 6)), t), [1])
chk("h-k2", sqrt(16 + 9 - 2*12*Q(1, 2)), sqrt(13)); chk("h-k2-k", sqrt(13), 3.61, 0.005)
chk("h-k3", fok(V(2, 1, 2), V(1, -2, 1)), 74.2, 0.05); chk("h-k3-sk", V(2, 1, 2).dot(V(1, -2, 1)), 2)
chk("h-k4", [-3*V(1, 0, -2), (3*V(1, 0, -2)).norm()], [V(-3, 0, 6), 3*sqrt(5)]); chk("h-k4-k", 3*sqrt(5), 6.71, 0.005)
a_, b_ = V(2, 1, 0), V(0, 3, 1)                  # altalanos ellenorzes: (2a+b)x(a-b) = -3 a x b
chk("h-k4-gen", (2*a_ + b_).cross(a_ - b_), -3 * a_.cross(b_))
chk("h-k5", [V(1, 1, 0).cross(V(0, 1, 1)), V(1, -1, 1).norm()], [V(1, -1, 1), sqrt(3)])
A, B, C = V(2, 0, 1), V(3, 2, 3), V(4, -2, 2)
chk("h-k6", [(B - A).dot(C - A), (B - A).norm(), (C - A).norm(), (B - A).cross(C - A).norm() / 2], [0, 3, 3, Q(9, 2)])
chk("h-n2", solve((1 - p_)**2 + 8 - ((3 - p_)**2 + 16), p_), [4])
Pn = V(4, 0, 0)
chk("h-n2-T", [(V(1, 2, 2) - Pn).cross(V(3, 0, 4) - Pn), ((V(1, 2, 2) - Pn).cross(V(3, 0, 4) - Pn)).norm() / 2],
    [V(8, 10, 2), sqrt(42)]); chk("h-n2-k", sqrt(42), 6.48, 0.005)
chk("h-n3", [V(1, t, 0).cross(V(0, 1, 2)), sorted(solve(4*t**2 + 5 - 9, t))], [V(2*t, -2, 1), [-1, 1]])
assert not E, E
print("sympy önteszt: OK")


def h(f, azon, sz="→"):
    return '<a href="' + f + '#' + azon + '">' + sz + '</a>'


A1 = "tananyag-vektorok-sikban.html"
A2 = "tananyag-koordinatak-terben.html"
B1 = "tananyag-skalaris-szorzat.html"
B2 = "tananyag-vektorialis-szorzat.html"
C1 = "tananyag-vektorok-alkalmazasa.html"

# ==================================================================== F4
OSSZ = [
 ("A vektor és a műveletek", [
  r'<p>A <b>vektor</b> az egymásba eltolható irányított szakaszok közös jellemzője; három adata '
  r'az <b>iránya</b> (az egyenes állása), az <b>irányítása</b> (merre mutat) és az '
  r'<b>intenzitása</b> — más néven hossza — $|\vec a|$ (' + h(A1, "def-vektor") + r'). Két vektor '
  r'<b>egyenlő</b>, ha eltolással fedésbe hozhatók. A nullvektor $\vec 0$ (intenzitása $0$, iránya és '
  r'irányítása nincs), az ellentett $-\vec a$.</p>'
  r'<table class="tt-table">'
  r'<tr><th>Művelet</th><th>Szabály</th><th>Megjegyzés</th></tr>'
  r'<tr><td>összeadás</td><td>háromszög-szabály: $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$; '
  r'paralelogramma-szabály: közös kezdőpontból az átló</td><td>$|\vec a+\vec b|\le|\vec a|+|\vec b|$, egyenlőség csak azonos irányításnál (vagy nullvektorral)</td></tr>'
  r'<tr><td>kivonás</td><td>$\vec a-\vec b=\vec a+(-\vec b)$; $\overrightarrow{OB}-\overrightarrow{OA}=\overrightarrow{AB}$</td>'
  r'<td>a paralelogramma másik átlója, a $\vec b$ végpontjából az $\vec a$ végpontjába mutat</td></tr>'
  r'<tr><td>skalárral szorzás</td><td>$|\lambda\vec a|=|\lambda|\,|\vec a|$; $\lambda>0$: azonos, $\lambda<0$: ellentétes irányítás; $\lambda=0$ vagy $\vec a=\vec 0$: nullvektor</td>'
  r'<td>ha $\vec a\ne\vec 0$: $\vec b\parallel\vec a\iff\vec b=\lambda\vec a$ (' + h(A1, "def-skalarral-szorzas") + r')</td></tr>'
  r'</table>'
  r'<p>A műveletekkel úgy számolunk, mint a betűs kifejezésekkel (' + h(A1, "tetel-muveletek") + r').</p>'
  r'<p><b>Két nem nullvektor szöge</b>: közös kezdőpontba tolva, $0^\circ\le\varphi\le180^\circ$. A $\vec b$ '
  r'<b>skaláris vetülete</b> az $\vec a$-ra $|\vec b|\cos\varphi$ — hegyesszögnél pozitív, '
  r'derékszögnél $0$, tompaszögnél negatív (' + h(A1, "def-szog-vetulet") + r').</p>',
 ]),

 ("Koordináták a térben", [
  r'<table class="tt-table">'
  r'<tr><th>Mit</th><th>Képlet</th></tr>'
  r'<tr><td>a vektor két alakja (' + h(A2, "def-vektor-koordinatai") + r')</td>'
  r'<td>$\vec a=x\vec i+y\vec j+z\vec k=(x;y;z)$ — hiányzó tag: $0$ koordináta</td></tr>'
  r'<tr><td>két pont közötti vektor, $A(x_1;y_1;z_1)$, $B(x_2;y_2;z_2)$</td><td>$\overrightarrow{AB}=(x_2-x_1;\;y_2-y_1;\;z_2-z_1)$ — végpont mínusz kezdőpont</td></tr>'
  r'<tr><td>műveletek (' + h(A2, "tetel-koordinatas-muveletek") + r')</td>'
  r'<td>koordinátánként: $\vec a\pm\vec b$, $\lambda\vec a$; párhuzamos: arányos koordináták</td></tr>'
  r'<tr><td>intenzitás, távolság (' + h(A2, "tetel-hossz") + r')</td>'
  r'<td>$|\vec a|=\sqrt{x^2+y^2+z^2}$, &nbsp; $d(A,B)=|\overrightarrow{AB}|$</td></tr>'
  r'<tr><td>egységvektor</td><td>ha $\vec a\ne\vec 0$: $\vec a_0=\dfrac{\vec a}{|\vec a|}$</td></tr>'
  r'<tr><td>felezőpont, paralelogramma</td><td>$F=\tfrac12(A+B)$; ha $ABCD$ sorrendben paralelogramma, $D=A+C-B$ (koordinátánként; $B$ a $D$-vel szemközti csúcs)</td></tr>'
  r'</table>',
 ]),

 ("A két szorzat egymás mellett", [
  r'<table class="tt-table">'
  r'<tr><th></th><th>skaláris szorzat $\vec a\cdot\vec b$</th><th>vektoriális szorzat $\vec a\times\vec b$</th></tr>'
  r'<tr><td>eredménye</td><td><b>szám</b></td><td><b>vektor</b>, merőleges mindkét tényezőre</td></tr>'
  r'<tr><td>definíció</td><td>$|\vec a|\,|\vec b|\cos\varphi$ (' + h(B1, "def-skalaris") + r')</td>'
  r'<td>intenzitása $|\vec a|\,|\vec b|\sin\varphi$, irányítása jobbkéz-szabály (' + h(B2, "def-vektorialis") + r')</td></tr>'
  r'<tr><td>koordinátákkal</td><td>$x_1x_2+y_1y_2+z_1z_2$ (' + h(B1, "tetel-skalaris-koordinatak") + r')</td>'
  r'<td>$\begin{vmatrix}\vec i&\vec j&\vec k\\ x_1&y_1&z_1\\ x_2&y_2&z_2\end{vmatrix}$, előjelek $+\,-\,+$ (' + h(B2, "tetel-vektorialis-koordinatak") + r')</td></tr>'
  r'<tr><td>pontosan akkor $0$, illetve $\vec 0$, ha…</td><td>merőlegesek, vagy valamelyik nullvektor (' + h(B1, "tetel-merolegesseg") + r')</td>'
  r'<td>párhuzamosak, vagy valamelyik nullvektor (' + h(B2, "tetel-vektorialis-tulajdonsagok") + r')</td></tr>'
  r'<tr><td>sorrend</td><td>$\vec a\cdot\vec b=\vec b\cdot\vec a$</td><td>$\vec b\times\vec a=-\vec a\times\vec b$</td></tr>'
  r'<tr><td>önmagával</td><td>$\vec a\cdot\vec a=|\vec a|^2$</td><td>$\vec a\times\vec a=\vec 0$</td></tr>'
  r'<tr><td>legfontosabb használat</td><td><b>szög</b> (nem nullvektorokra): $\cos\varphi=\dfrac{\vec a\cdot\vec b}{|\vec a|\,|\vec b|}$</td>'
  r'<td><b>terület</b>: $T_{\text{par}}=|\vec a\times\vec b|$, $T_{\triangle}=\tfrac12|\vec a\times\vec b|$ (' + h(B2, "tetel-terulet") + r')</td></tr>'
  r'<tr><td>további alkalmazás</td><td><b>munka</b>: $W=\vec F\cdot\vec s=|\vec F|\,|\vec s|\cos\varphi$</td>'
  r'<td><b>magasság, pont–egyenes távolság</b>: $m=\dfrac{2T}{\text{alap}}=\dfrac{|\vec a\times\vec b|}{|\vec a|}$</td></tr>'
  r'</table>'
  r'<p>Mindkettő disztributív, és a számszorzó kiemelhető; a vektoriális szorzat tagonkénti kifejtésénél a tényezők sorrendje nem cserélhető fel. Részletes döntési táblázat: '
  r'melyik szorzat mire (' + h(C1, "tetel-melyik-szorzat") + r').</p>'
  r'<p><b>A szög számológéppel</b> (' + h(B1, "pelda-szog") + r'): fok üzemmód (<b>D</b>/<b>DEG</b>); '
  r'előbb a tört értéke, majd <code>SHIFT cos Ans =</code> (más gépeken <code>2nd cos</code> vagy <code>INV cos</code>). '
  r'A skaláris szorzat előjele előre megmondja, hogy $90^\circ$ alatti vagy fölötti szöget kell kapnod ($0$ esetén pontosan $90^\circ$).</p>',
 ]),

 ("Maxi csapdái — a tipikus hibák", [
  r'<ul>'
  r'<li><b>Fej–láb szög:</b> ha a $\vec b$-t az $\vec a$ végpontjához illeszted, a csatlakozásnál látszó szög a mellékszög — a szöget közös kezdőpontból mérjük.</li>'
  r'<li><b>$\overrightarrow{AB}=A-B$:</b> fordítva! Végpont mínusz kezdőpont.</li>'
  r'<li><b>Hiányzó tag:</b> $2\vec i-\vec k=(2;0;-1)$, nem $(2;-1)$.</li>'
  r'<li><b>$|\vec a+\vec b|=|\vec a|+|\vec b|$:</b> csak azonos irányításnál igaz.</li>'
  r'<li><b>A skaláris szorzat nem vektor:</b> nem $(x_1x_2;\,y_1y_2;\,z_1z_2)$, hanem a három szorzat <b>összege</b>, egy szám.</li>'
  r'<li><b>A középső előjel:</b> a vektoriális szorzatban $-\vec j(\dots)$ áll. Ellenőrzés: az eredmény skaláris szorzata mindkét tényezővel $0$.</li>'
  r'<li><b>A háromszög szöge:</b> mindkét vektor abból a csúcsból induljon ($\overrightarrow{AB}$, $\overrightarrow{AC}$) — ha csak az egyiket fordítod meg (pl. $\overrightarrow{AB}$ és $\overrightarrow{CA}$), a mellékszöget kapod (' + h(C1, "pelda-haromszog") + r').</li>'
  r'<li><b>Radián mód:</b> nézd meg a kijelzőn a <b>D</b> / <b>R</b> / <b>G</b> jelet. Gyanús, ha $0$ és $3{,}14$ közötti szám jön ki, pedig a skaláris szorzat alapján nagyobb szögre számítasz.</li>'
  r'</ul>',
  abra(svg_vektorialis(w=340, h=250, leiras="Az a és b vektor paralelogrammája és a rá merőleges a × b"),
       'Egy ábra mindenre: $|\\vec a\\times\\vec b|$ a paralelogramma területe, és $\\vec a\\times\\vec b$ '
       'merőleges a síkjára.'),
 ]),

 ("Mit hol találsz?", [
  '<div class="brief"><p>📚 <b>Tananyag:</b> '
  '<a href="' + A1 + '">vektorok a síkban</a> · '
  '<a href="' + A2 + '">vektorok a térben</a> · '
  '<a href="' + B1 + '">a skaláris szorzat</a> · '
  '<a href="' + B2 + '">a vektoriális szorzat</a> · '
  '<a href="' + C1 + '">vektorok munkában</a>.</p>'
  '<p>🎯 <b>Gyakorlás:</b> '
  '<a href="feladatok-vektorok.html">vektorok</a> · '
  '<a href="feladatok-szorzatok.html">a két szorzat</a> · '
  '<a href="feladatok-hazi.html">Vészterem</a> — majd indulj a '
  '<a href="terepkuldetes.html">Királyi Irányítótű</a> küldetésre!</p></div>',
 ]),
]

lap(**T, fajl="osszefoglalo.html", cim="Iránytű-térkép — a témakör egy lapon",
    cim_tiszta="Iránytű-térkép", itt="Iránytű-térkép",
    alcim="A vektorok definíciói, legfontosabb képletei és tipikus csapdái egy helyen — ismétléshez, "
          "ellenőrző előtti átfutáshoz, nyomtatáshoz.",
    chip=KUL + " · összefoglaló", chip_tipus="összefoglaló",
    szakaszok=[("📇 " + OSSZ[0][0], OSSZ[0][1])] + OSSZ[1:],
    elozo=("feladatok-szorzatok.html", "A két szorzat — feladatok"),
    kovetkezo=("terepkuldetes.html", KUL))
print("✓ osszefoglalo.html")

# ==================================================================== F5p
TEREP = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Medúza:</b> Crni Grom elkészítette a Királyi Irányítótűt, de a Kamrában csak akkor '
         'működik, ha pontosan bemérjük. Három jeladó áll a teremben — $P$, $Q$ és $R$ —, és '
         'a tűnek tudnia kell, <b>hol</b> a középpont, <b>mekkora szöget</b> zár be a hullám a jeladók vonalával, és '
         '<b>mekkora felületet</b> kell hatástalanítania. A Néma Király nem mondja meg a választ. Irányt mutat — '
         'a számolás a tiéd.'),
   r'<p>Három fázis. Minden lépésnél írd le, melyik vektort számolod és miért. Kerekíts a szögeket '
   r'egy, minden más közelítő értéket két tizedesjegyre, és jelöld a kerekítést. A választ fogalmazd meg mondatban is.</p>'
   r'<p><b>A jeladók helyzete:</b> $P(1;2;0)$, $Q(3;3;2)$, $R(1;5;4)$ (egység: méter).</p>'
   r'<p><b>Amire szükséged lesz:</b> koordináták és műveletek, intenzitás, skaláris és vektoriális '
   r'szorzat, számológép fok üzemmódban.</p>',
 ]),

 ("I. fázis — A jeladók", [
   r'<ol class="reszfeladatok">'
   r'<li>Határozd meg a $\overrightarrow{PQ}$ és a $\overrightarrow{PR}$ vektor koordinátáit és intenzitását!</li>'
   r'<li>Egy negyedik jeladót, $S$-et úgy kell elhelyezni, hogy a $PQSR$ négyszög (ebben a '
   r'sorrendben) paralelogramma legyen. Hol legyen $S$?</li>'
   r'<li>Az irányítótű a paralelogramma középpontjába kerül. Határozd meg a koordinátáit, és '
   r'ellenőrizd a <b>másik</b> átló felezőpontjával is!</li>'
   r'<li>Maxi szerint $S=P+Q-R=(3;0;-2)$. Milyen sorrendben alkot paralelogrammát a $P$, a $Q$, az $R$ '
   r'és Maxi pontja? Melyik szakasz lett nála átló oldal helyett?</li>'
   r'</ol>',
 ]),

 ("II. fázis — A hullám iránya", [
   r'<ol class="reszfeladatok">'
   r'<li>Mekkora szöget zár be a $\overrightarrow{PQ}$ és a $\overrightarrow{PR}$ vektor?</li>'
   r'<li>Téglalap-e a $PQSR$ paralelogramma? Rombusz-e? Indokold!</li>'
   r'<li>Crni Grom jelzése a $z$ tengelyen álló torony csúcsából, a $H(0;0;h)$ pontból érkezik. Mekkora $h$ '
   r'esetén merőleges a $\overrightarrow{PH}$ vektor a $\overrightarrow{PQ}$ vektorra?</li>'
   r'<li>A hanghullám a $\vec v=(1;1;1)$ irányban indul. Mekkora szöget zár be a '
   r'$\overrightarrow{PQ}$ vektorral, és mekkora a $\vec v$ skaláris vetülete a $\overrightarrow{PQ}$-ra?</li>'
   r'</ol>',
 ]),

 ("III. fázis — A kristálylap", [
   r'<ol class="reszfeladatok">'
   r'<li>Számítsd ki a $PQR$ háromszög és a $PQSR$ paralelogramma területét!</li>'
   r'<li>Az irányítótű mutatója merőleges a $PQR$ síkra. Adj meg egy ilyen irányú '
   r'<b>egységvektort</b>, és skaláris szorzattal ellenőrizd, hogy a $\overrightarrow{PQ}$-ra és a $\overrightarrow{PR}$-re is merőleges!</li>'
   r'<li>Milyen messze van az $R$ jeladó a $PQ$ egyenestől? (Ez a háromszög $R$-ből induló magassága.)</li>'
   r'<li>Tervezz egy új jeladót, $U$-t úgy, hogy a $PQU$ háromszög a $P$-nél derékszögű legyen, és '
   r'$PU=3$ méter! Add meg $U$ koordinátáit, mutasd meg, hogy megfelel a két feltételnek, és '
   r'számítsd ki a $PQU$ háromszög területét!</li>'
   r'</ol>',
   brief('<b>Medúza:</b> Ha a tű megtalálta a középpontot, az irányt és a lap síkját, a hullám '
         'már nem pusztít — gyógyít. Crni Grom a számításaidra vár: a megoldásokat a tanárod '
         'ellenőrzi — a kulcs nem kerül a hálózatra.', outro=True),
 ]),
]

lap(**T, fajl="terepkuldetes.html", cim=KUL, cim_tiszta=KUL, itt="Terepküldetés",
    alcim="Három fázis: a jeladók koordinátái, a hullám iránya és a kristálylap területe. Beadható "
          "projektfeladat — a megoldásokat a tanárod ellenőrzi.",
    chip=KUL + " · terepküldetés", chip_tipus="terepküldetés",
    szakaszok=TEREP,
    elozo=("osszefoglalo.html", "Iránytű-térkép"),
    kovetkezo=("index.html", "Témakör Főhadiszállása"))
print("✓ terepkuldetes.html")

# ==================================================================== F6h
from fgy_common import cards, oldal, w

DR_A = [
 (r"Adott az $A(2;-3;1)$ és a $B(-1;1;1)$ pont. Határozd meg az $\overrightarrow{AB}$ koordinátáit és "
  r"az $AB$ szakasz hosszát!", None,
  r"$\overrightarrow{AB}=(-3;4;0)$, $AB=\sqrt{9+16+0}=5$."),
 (r"Legyen $\vec a=(1;-2;3)$ és $\vec b=(4;0;-1)$. Számítsd ki a $3\vec a-2\vec b$ vektort!", None,
  r"$(3;-6;9)-(8;0;-2)=(-5;-6;11)$"),
 (r"Párhuzamos-e a $(2;-6;4)$ és a $(-3;9;-6)$ vektor? Ha igen, hányszorosa a második vektor az elsőnek?", None,
  r"Igen: $(-3;9;-6)=-\tfrac32\cdot(2;-6;4)$ (ellentétes irányításúak)."),
 (r"Merőleges-e az $\vec a=(3;1;-2)$ és a $\vec b=(2;-4;1)$ vektor?", None,
  r"Igen: $\vec a\cdot\vec b=6-4-2=0$."),
 (r"Mekkora szöget zár be az $\vec a=(2;2;1)$ és a $\vec b=(1;0;-1)$ vektor? (Számológéppel, egy tizedesre.)",
  None, r"$\vec a\cdot\vec b=1$, $|\vec a|=3$, $|\vec b|=\sqrt2$, $\cos\varphi=\frac{1}{3\sqrt2}\approx0{,}2357$, "
        r"$\varphi\approx76{,}4^\circ$."),
 (r"Számítsd ki az $\vec a=(1;-1;2)$ és a $\vec b=(3;0;1)$ vektor vektoriális szorzatát!", None,
  r"$\vec a\times\vec b=(-1;5;3)$"),
 (r"Mekkora az $A(0;1;1)$, $B(2;1;3)$, $C(1;3;1)$ csúcsú háromszög területe?", None,
  r"$\overrightarrow{AB}=(2;0;2)$, $\overrightarrow{AC}=(1;2;0)$, $\overrightarrow{AB}\times\overrightarrow{AC}=(-4;2;4)$, "
  r"intenzitása $6$, így $T=3$."),
 (r"Az $ABCD$ paralelogramma három egymást követő csúcsa $A(1;0;2)$, $B(4;1;0)$ és $C(5;3;1)$.",
  [r"Határozd meg a $D$ csúcsot!", r"Hol metszik egymást az átlók?"],
  [r"$D=A+C-B=(2;2;3)$", r"az $AC$ felezőpontjában: $\left(3;\tfrac32;\tfrac32\right)$"]),
]

DR_K = [
 (r"Határozd meg a $t$ értékét úgy, hogy a $(2;t;-1)$ és a $(t;4;6)$ vektor merőleges legyen!", None,
  r"$2t+4t-6=0$, tehát $t=1$."),
 (r"Az $\vec a$ intenzitása $4$, a $\vec b$ intenzitása $3$, szögük $60^\circ$. Mekkora $|\vec a-\vec b|$?", None,
  r"$|\vec a-\vec b|^2=16-2\cdot6+9=13$ (mert $\vec a\cdot\vec b=6$), tehát $|\vec a-\vec b|=\sqrt{13}\approx3{,}61$."),
 (r"Az $ABC$ háromszög csúcsai $A(1;1;0)$, $B(3;2;2)$, $C(2;-1;1)$. Mekkora az $A$ csúcsnál lévő szög? (Számológéppel, egy tizedesre.)", None,
  r"$\overrightarrow{AB}=(2;1;2)$, $\overrightarrow{AC}=(1;-2;1)$, skaláris szorzatuk $2$; "
  r"$\cos\alpha=\frac{2}{3\sqrt6}\approx0{,}2722$, $\alpha\approx74{,}2^\circ$."),
 (r"Tudjuk, hogy $\vec a\times\vec b=(1;0;-2)$. Egyszerűsítsd a $(2\vec a+\vec b)\times(\vec a-\vec b)$ kifejezést, "
  r"majd add meg az értékét és az intenzitását!", None,
  r"$-2\,\vec a\times\vec b+\vec b\times\vec a=-3\,\vec a\times\vec b=(-3;0;6)$, intenzitása $3\sqrt5\approx6{,}71$."),
 (r"Adj meg egy egységvektort, amely merőleges az $\vec a=(1;1;0)$ és a $\vec b=(0;1;1)$ vektorra is!", None,
  r"$\vec a\times\vec b=(1;-1;1)$, intenzitása $\sqrt3$; egy megfelelő egységvektor "
  r"$\frac{1}{\sqrt3}(1;-1;1)$ (az ellentettje is jó)."),
 (r"Az $A(2;0;1)$, $B(3;2;3)$, $C(4;-2;2)$ pontok egy háromszög csúcsai.",
  [r"Mutasd meg, hogy a háromszög derékszögű és egyenlő szárú!", r"Mekkora a területe?"],
  [r"$\overrightarrow{AB}=(1;2;2)$, $\overrightarrow{AC}=(2;-2;1)$: skaláris szorzatuk $0$ (a derékszög az $A$-nál van), és mindkettő intenzitása $3$",
   r"$T=\frac{3\cdot3}{2}=4{,}5$"]),
]

DR_N = [
 (r"Bizonyítsd be, hogy ha két nem nullvektorra $|\vec a+\vec b|=|\vec a-\vec b|$, akkor $\vec a$ és "
  r"$\vec b$ merőleges! Mit jelent ez egy paralelogrammára?", None,
  r"Négyzetre emelve: $|\vec a|^2+2\,\vec a\cdot\vec b+|\vec b|^2=|\vec a|^2-2\,\vec a\cdot\vec b+|\vec b|^2$, "
  r"így $4\,\vec a\cdot\vec b=0$, tehát $\vec a\perp\vec b$. Paralelogrammára: ha az átlói egyenlő "
  r"hosszúak, akkor téglalap."),
 (r"Az $x$ tengely melyik $P$ pontja van egyenlő távolságra az $A(1;2;2)$ és a $B(3;0;4)$ ponttól? "
  r"Mekkora ekkor a $PAB$ háromszög területe?", None,
  r"$P(p;0;0)$: $(1-p)^2+8=(3-p)^2+16$, ebből $4p=16$, $P(4;0;0)$. "
  r"$\overrightarrow{PA}\times\overrightarrow{PB}=(-3;2;2)\times(-1;0;4)=(8;10;2)$, "
  r"$T=\frac{\sqrt{168}}{2}=\sqrt{42}\approx6{,}48$."),
 (r"Az $\vec a=(1;t;0)$ és a $\vec b=(0;1;2)$ vektor által kifeszített paralelogramma területe $3$. "
  r"Határozd meg $t$-t!", None,
  r"$\vec a\times\vec b=(2t;-2;1)$, intenzitása $\sqrt{4t^2+5}=3$, így $t^2=1$: $t=1$ vagy $t=-1$."),
]

body_dr = [
 '    <h2 id="alap">🟢 Alapszint</h2>\n' + cards(DR_A, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint</h2>\n' + cards(DR_K, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint</h2>\n' + cards(DR_N, "nehez", "nehez"),
]

oldal(**T, fajl="feladatok-hazi.html", cim="Vészterem", h1="Vészterem — házi feladatok",
      chipek='<span class="chip alap">Alap</span><span class="chip kozep">Közép</span>'
             '<span class="chip nehez">Nehéz</span>',
      alcim="Rövid, vegyes gyakorlósor a vektorokhoz — házi feladatnak és az ellenőrző előtti "
            "bemelegítésnek. A végeredmény minden feladatnál lenyitható!",
      sections_html="\n".join(body_dr),
      prev="index.html", prevc="Témakör Főhadiszállása",
      nxt="osszefoglalo.html", nxtc="Iránytű-térkép")
print("✓ feladatok-hazi.html | Alap", len(DR_A), "Közép", len(DR_K), "Nehéz", len(DR_N))

# ==================================================================== F5
from tananyag_common import GYOKER


def kartya(href, cim, le):
    return ('      <a class="kartya" href="' + href + '">\n        <h3>' + w(cim) + '</h3>\n'
            '        <p class="le">' + w(le) + '</p>\n      </a>')


K = [
 kartya(A1, "Vektorok a síkban",
        "Irány, irányítás, intenzitás; összeadás, kivonás, skalárral szorzás; két vektor szöge és a vetület"),
 kartya(A2, "Vektorok a térben",
        "A térbeli koordináta-rendszer, a vektor koordinátái, műveletek, intenzitás és távolság"),
 kartya(B1, "A skaláris szorzat",
        "Definíció, előjel és merőlegesség, koordinátás képlet — és a szög számológéppel"),
 kartya(B2, "A vektoriális szorzat",
        "Jobbkéz-szabály, a szorzat intenzitása mint terület, determinánsos képlet, tulajdonságok"),
 kartya(C1, "Vektorok munkában",
        "Melyik szorzat mire; egy térbeli háromszög oldalai, szöge és területe; eredő erő és munka"),
 kartya("feladatok-vektorok.html", "🏋️ Vektorok — feladatok",
        "Kiképzési Adattár: Alap · Közép · Nehéz + Joker — műveletek, szög, koordináták, távolság"),
 kartya("feladatok-szorzatok.html", "🏋️ A két szorzat — feladatok",
        "Skaláris és vektoriális szorzat, szög, merőlegesség, terület és alkalmazások"),
 kartya("feladatok-hazi.html", "🕹️ Vészterem — házi feladatok",
        "A témakör fő számolási típusait lefedő rövid házi feladatsor, az ellenőrző előtti bemelegítésnek"),
 kartya("terepkuldetes.html", "🎯 A Királyi Irányítótű",
        "Háromfázisú küldetés — a jeladók koordinátái, a hullám iránya és a kristálylap területe"),
 kartya("osszefoglalo.html", "📇 Iránytű-térkép",
        "A definíciók, a legfontosabb képletek és a tipikus csapdák egy helyen — ellenőrző előtti átfutáshoz"),
]

INDEX = '''<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vektorok | 3e | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="3e">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">&#8730;</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">3e</span></a> ›
  <span class="itt">Vektorok</span>
</nav>
<div class="hero">
  <h1>Vektorok</h1>
  <p class="alcim">Irány, irányítás és nagyság egyetlen jelben: műveletek a síkban és a térben, koordináták —
  és a két szorzat, amellyel szöget és területet számolunk.</p>
  <div class="meta-sor"><span class="chip ora">9 óra</span><span class="statusz kesz">kész</span></div>
  <div class="brief"><p>🧭 <b>Szektor 04 — A Királyi Irányítótű.</b> Kiképző:
  <b>Crni Grom</b>, a Néma Király — szavait <b>Medúza</b> tolmácsolja. A Király hangja romba dönthetné
  a Kristály-kamrát, de ha tudjuk, <b>merre</b> és <b>mekkora erővel</b> indul a hullám, épp ez a hang
  hatástalaníthatja a kristályokat. Ehhez egy szám kevés: irány kell, nyíl kell — vektor.</p></div>
</div>
<main class="lap">
  <div class="tartalom">
    <h2>Tananyag</h2>

    <h3>➡️ A vektor — Crni Grom</h3>
    <div class="racs">
''' + "\n".join(K[0:2]) + '''
    </div>

    <h3>✖️ A két szorzat — Crni Grom</h3>
    <div class="racs">
''' + "\n".join(K[2:4]) + '''
    </div>

    <h3>🧭 Alkalmazás — Crni Grom</h3>
    <div class="racs">
''' + K[4] + '''
    </div>

    <h2>Feladatgyűjtemény</h2>
    <div class="racs">
''' + "\n".join(K[5:8]) + '''
    </div>

    <h2>Terepküldetés</h2>
    <div class="racs">
''' + K[8] + '''
    </div>

    <h2>Összefoglaló</h2>
    <div class="racs">
''' + K[9] + '''
    </div>

    <p class="le halvany"><b>Ajánlott sorrend:</b> az öt tananyag-egység sorban, közben a
    „Gyakorolj!” sávok a két feladatgyűjteménybe visznek; a témakör végén az Iránytű-térkép,
    majd A Királyi Irányítótű küldetés. A Vészterem házi a két szorzat után bármikor jöhet.</p>
  </div>
</main>
<footer class="lablec">
  <div class="lablec-bel">
    <span><b>Szvetkó matek</b> · Nagygyörgy Kristóf — Svetozar Marković Gimnázium, Szabadka</span>
    <span>Legyél szvetkós!</span>
  </div>
</footer>
<script src="../../assets/katex/katex.min.js"></script>
<script src="../../assets/katex/auto-render.min.js"></script>
<script>
  renderMathInElement(document.body, {delimiters:[
    {left:'\\\\(', right:'\\\\)', display:false},
    {left:'\\\\[', right:'\\\\]', display:true}
  ]});
</script>
<script src="../../assets/js/ui.js"></script>
</body>
</html>
'''

ut = os.path.join(GYOKER, T["tagozat"], T["mappa"], "index.html")
open(ut, "w", encoding="utf-8").write(INDEX)
print("✓ index.html")
