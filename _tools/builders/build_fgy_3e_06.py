# -*- coding: utf-8 -*-
"""3e/06 — feladatgyujtemeny: sorozatok (A1, A2, B1, B2). Az indukciohoz (C) NINCS feladat.
Horgony-terv: narrativa_06-indukcio-sorozatok.md · feladat-terkep: terkep_fgy_06-indukcio-sorozatok.md.
Forras: 7_Sorozatok/0_Feladatok - Sorozatok (szamtani, mertani).pdf (PDF n), A MERTANI SOROZAT.docx (MS n),
a foiskolai jegyzet FELADATOK-blokkjai (JZ), Kamatos kamat.pdf (KK) es sajat feladatok."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal
from tananyag_common import svg_fuggvenyek

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Rational as Q, symbols, solve, simplify, Eq, sympify, log, N
E = []


def _eq(g, w):
    if isinstance(g, (list, tuple)):
        return len(g) == len(w) and all(_eq(a, b) for a, b in zip(g, w))
    k = simplify(sympify(g) - sympify(w))
    try:
        return abs(float(k)) < 1e-9
    except TypeError:
        return k == 0


def chk(nev, g, w):
    if not _eq(g, w):
        E.append((nev, g, w))


n, x, q = symbols("n x q", positive=True)
u, v = symbols("u v", real=True)   # ismeretlen a_1, d (elojel-korlat nelkul)
SZ = lambda a1, d, k: a1 + (k - 1)*d                      # szamtani n-edik tag
SS = lambda a1, d, k: sympify(k)/2*(2*a1 + (k - 1)*d)     # szamtani osszeg
MB = lambda b1, qq, k: b1*qq**(k - 1)                     # mertani n-edik tag
MS = lambda b1, qq, k: b1*(qq**k - 1)/(qq - 1)            # mertani osszeg

# --- alap
chk("a1a", [Q(3*i + 1, i + 2) for i in range(1, 6)], [Q(4, 3), Q(7, 4), 2, Q(13, 6), Q(16, 7)])
chk("a1b", [Q(6*i, 2*i - 1) for i in range(1, 6)], [6, 4, Q(18, 5), Q(24, 7), Q(10, 3)])
chk("a1c", [Q((-1)**i, i*i + 1) for i in range(1, 6)], [-Q(1, 2), Q(1, 5), -Q(1, 10), Q(1, 17), -Q(1, 26)])
chk("a1d", [Q(i*i, 2**i) for i in range(1, 6)], [Q(1, 2), 1, Q(9, 8), 1, Q(25, 32)])
r1 = [3]
for i in range(1, 5):
    r1.append(r1[-1] + 2*i)
r2 = [1]
for _ in range(4):
    r2.append(2*r2[-1] + 1)
chk("a2a", r1, [3, 5, 9, 15, 23]); chk("a2b", r2, [1, 3, 7, 15, 31])
chk("a3a", solve(Eq(2**(n - 3), 16), n), [7])
chk("a3b", solve(Eq(Q(1, 2)**(1 - n), 16), n), [5])
chk("a3c", sorted(solve(Eq(u*u - 17*u + 16, 16), u)), [0, 17])
chk("a4", [2*i - 5 for i in range(1, 7)], [-3, -1, 1, 3, 5, 7])
chk("a5a", [7*i - 5 for i in range(5, 7)], [30, 37])
chk("a5b", [2*3**(i - 1) for i in range(5, 7)], [162, 486])
chk("a5c", [i*i for i in range(5, 7)], [25, 36])
chk("a6", [solve(Eq(n*(n + 1)/2, 55), n), [k for k in range(1, 20) if k*(k + 1)//2 == 60]], [[10], []])
chk("a7c", [(-1)**i*i for i in range(1, 5)], [-1, 2, -3, 4])
chk("a8a", simplify((n + 1)/(n + 6) - n/(n + 5)), 5/((n + 5)*(n + 6)))
chk("a8a", [[i*i - i for i in range(1, 5)], simplify(((n + 1)**2 - (n + 1)) - (n*n - n))],
    [[0, 2, 6, 12], 2*n])
chk("a8b", [Q(2*i + 3, i) for i in range(1, 5)], [5, Q(7, 2), 3, Q(11, 4)])
chk("a9a", [3 + Q(1, i) for i in range(1, 4)], [4, Q(7, 2), Q(10, 3)])
chk("a11a", [2 - i for i in range(1, 4)], [1, 0, -1])
chk("a11b", [Q(3*i - 1, i) for i in range(1, 4)], [2, Q(5, 2), Q(8, 3)])
chk("a12", [Q((-1)**i, i) for i in range(1, 5)], [-1, Q(1, 2), -Q(1, 3), Q(1, 4)])
chk("a13", [[SZ(a, d, k) for k in range(1, 5)] for a, d in [(3, 2), (-2, 5), (7, -3), (-5, -2)]],
    [[3, 5, 7, 9], [-2, 3, 8, 13], [7, 4, 1, -2], [-5, -7, -9, -11]])
chk("a14", [SZ(3, 4, 8), SZ(-5, 2, 12), SZ(4, -Q(1, 4), 13), SZ(-5, -2, 16)], [31, 17, 1, -35])
chk("a15", [SS(1, 3, 12), SS(-8, 5, 36)], [210, 2862])
chk("a16", [SZ(2, 6, 15), SS(2, 6, 27)], [86, 2160])
chk("a17", [SZ(12, -3, 12), SS(12, -3, 36)], [-21, -1458])
for nev, (a1, d, an, nn, sn) in zip("abcd", [(-5, 3, 13, 7, 28), (-1, -3, -13, 5, -35),
                                             (4, 7, 81, 12, 510), (3, -5, -72, 16, -552)]):
    chk("a18" + nev, [solve(Eq(SZ(a1, d, n), an), n)[0], SS(a1, d, nn)], [nn, sn])
chk("a19", [[SZ(a, d, k), SS(a, d, k)] for a, d, k in [(7, 3, 20), (3, 6, 28), (-6, -3, 27), (-1, 2, 16)]],
    [[64, 710], [165, 2352], [-84, -1215], [29, 224]])
chk("a20", [Q(3 + 11, 2), 12 + (12 - 5)], [7, 19])
chk("a21", [[MB(b, qq, k) for k in range(1, 5)] for b, qq in [(2, 3), (3, -Q(1, 3)), (1, -2), (-4, 2)]],
    [[2, 6, 18, 54], [3, -1, Q(1, 3), -Q(1, 9)], [1, -2, 4, -8], [-4, -8, -16, -32]])
chk("a22", [[Q(5*3**(k - 1)) for k in range(1, 6)], [3*(-3)**(k - 1) for k in range(1, 6)],
            [Q(2, 3)*Q(3, 4)**(k - 1) for k in range(1, 6)], [-6*(-2)**(k - 1) for k in range(1, 6)]],
    [[5, 15, 45, 135, 405], [3, -9, 27, -81, 243],
     [Q(2, 3), Q(1, 2), Q(3, 8), Q(9, 32), Q(27, 128)], [-6, 12, -24, 48, -96]])
chk("a23", [MB(-1, 3, 8), MB(-5, -2, 6), MB(-Q(3, 2), -4, 4), MB(2, 4, 5)], [-2187, 160, 96, 512])
chk("a24", MS(2, -2, 9), 342)
chk("a25a", [solve(Eq(MB(3, 4, n), 3072), n)[0], MS(3, 4, 6)], [6, 4095])
chk("a25b", [solve(Eq(MB(27, Q(2, 3), n), 8), n)[0], MS(27, Q(2, 3), 4)], [4, 65])
chk("a26", [[MB(b, qq, k), MS(b, qq, k)] for b, qq, k in
            [(2, -4, 4), (1, 3, 6), (-1, 5, 5), (3, Q(1, 3), 4)]],
    [[-128, -102], [243, 364], [-625, -781], [Q(1, 9), Q(40, 9)]])
chk("a27", [sorted(solve(Eq(x*x, 100), x)), sorted(solve(Eq(x*x, 36), x))], [[10], [6]])
chk("a28", [80000*(1 + Q(5, 100)*3), round(float(80000*Q(105, 100)**3), 2)], [92000, 92610.00])
# --- közép
chk("k1", [[SZ(2, 3, k) for k in range(1, 6)], SZ(2, 3, n)], [[2, 5, 8, 11, 14], 3*n - 1])
chk("k2", solve(Eq(log(n + 1, 2), 16), n), [65535])
chk("k3", sorted(solve(n*n - 7*n + 12, n)), [3, 4])
chk("k4", [(i - 1)*(i - 2)*(i - 3) + 2*i - 1 for i in range(1, 5)], [1, 3, 5, 13])
chk("k5", [simplify((2*(n + 1) - 1)/(n + 2) - (2*n - 1)/(n + 1)), Q(1, 2)], [3/((n + 1)*(n + 2)), Q(1, 2)])
chk("k6", [simplify((n + 3)/(2*n + 3) - (n + 2)/(2*n + 1)), 1], [-3/((2*n + 1)*(2*n + 3)), 1])
chk("k7", [Q(3*i, i + 1) for i in range(1, 4)], [Q(3, 2), 2, Q(9, 4)])
chk("k8", [i*i - 12*i + 40 for i in range(1, 9)], [29, 20, 13, 8, 5, 4, 5, 8])
d9 = Q(103 - 38, 13); a9 = 38 - 7*d9
chk("k9a", [d9, a9, [SZ(a9, d9, k) for k in range(1, 5)]], [5, 3, [3, 8, 13, 18]])
d9b = Q(-16 - 2, 9); a9b = 2 - 5*d9b
chk("k9b", [d9b, a9b, [SZ(a9b, d9b, k) for k in range(1, 5)]], [-2, 12, [12, 10, 8, 6]])
s = solve([Eq(SZ(u, v, 5), 6), Eq(SZ(u, v, 12), -15)], [u, v], dict=True)[0]
chk("k10", [s[u], s[v], SS(s[u], s[v], 18)], [18, -3, -135])
s = solve([Eq(SZ(u, v, 2) + SZ(u, v, 4), 16), Eq(SZ(u, v, 5) - u, 28)], [u, v], dict=True)[0]
chk("k11", [s[u], s[v], [SZ(s[u], s[v], k) for k in range(1, 6)]], [-6, 7, [-6, 1, 8, 15, 22]])
for nev, (e1, e2, var) in zip("abc", [
        (lambda a, d: SZ(a, d, 3) + SZ(a, d, 6) - 20, lambda a, d: SZ(a, d, 9) - SZ(a, d, 2) - 14, (3, 2)),
        (lambda a, d: 5*a + 10*SZ(a, d, 5) - 0, lambda a, d: SS(a, d, 4) - 14, (8, -3)),
        (lambda a, d: 2*SZ(a, d, 4) + SZ(a, d, 6) - 48, lambda a, d: 5*SZ(a, d, 5) - 7*SZ(a, d, 2) - 29, (5, 3))]):
    s = solve([Eq(e1(u, v), 0), Eq(e2(u, v), 0)], [u, v], dict=True)[0]
    chk("k12" + nev, [s[u], s[v]], list(var))
chk("k12b-atirt", SZ(8, -3, 1) + 2*SZ(8, -3, 5), 0)   # 5a1+10a5=0  <=>  a1+2a5=0
chk("k13", [SZ(5, 3, solve(Eq(SS(5, 3, n), 124), n)[0]), SZ(4, 5, solve(Eq(SS(4, 5, n), 172), n)[0]),
            SZ(-3, 4, solve(Eq(SS(-3, 4, n), 150), n)[0])], [26, 39, 33])
chk("k14a", [solve(Eq(SS(3, 1, n), 250), n)[0], SZ(3, 1, 20)], [20, 22])
chk("k14b", [sorted(solve(Eq(SS(18, -3, n), 54), n)), SZ(18, -3, 4), SZ(18, -3, 9)], [[4, 9], 9, -6])
chk("k14c", [solve(Eq(SS(2, 5, n), 245), n)[0], SZ(2, 5, 10)], [10, 47])
chk("k14d", [solve(Eq(SS(-2, -5, n), -555), n)[0], SZ(-2, -5, 15)], [15, -72])
chk("k15a", [solve(Eq(MS(2, Q(1, 2), n), Q(31, 8)), n)[0], MB(2, Q(1, 2), 5)], [5, Q(1, 8)])
chk("k15b", [[k for k in range(1, 9) if MS(2, -3, k) == -40][0], MB(2, -3, 4)], [4, -54])
chk("k16", [[MB(b, qq, k) for k in range(1, 5)] for b, qq in
            [(4, 2), (-5, -2), (-3, -3), (Q(2, 3), 3)]],
    [[4, 8, 16, 32], [-5, 10, -20, 40], [-3, 9, -27, 81], [Q(2, 3), 2, 6, 18]])
chk("k16-ell", [MB(4, 2, 4), MB(4, 2, 9), MB(-5, -2, 2), MB(-5, -2, 7), MB(-3, -3, 3), MB(-3, -3, 6),
                MB(Q(2, 3), 3, 4), MB(Q(2, 3), 3, 6)], [32, 1024, 10, -320, -27, 729, 18, 162])
chk("k16d-masodik", [MB(-Q(2, 3), -3, 4), MB(-Q(2, 3), -3, 6),
                     [MB(-Q(2, 3), -3, k) for k in range(1, 5)]],
    [18, 162, [-Q(2, 3), 2, -6, 18]])
chk("k17a", [MB(-4, 2, 1) + MB(-4, 2, 3), MB(-4, 2, 2) + MB(-4, 2, 4)], [-20, -40])
chk("k17b", [MB(1, 3, 5) - 1, MB(1, 3, 3) + 1, MB(1, -3, 5) - 1, MB(1, -3, 3) + 1], [80, 10, 80, 10])
chk("k17c", [MB(1, 3, 6) - MB(1, 3, 4), MB(1, 3, 3) - 1], [216, 8])
chk("k18", [MB(3, 2, solve(Eq(MS(3, 2, n), 189), n)[0]), MB(2, 3, solve(Eq(MS(2, 3, n), 728), n)[0]),
            MB(4, 2, solve(Eq(MS(4, 2, n), 2044), n)[0])], [96, 486, 1024])
chk("k19", [MB(3, 3, 2) + MB(3, 3, 4), MB(3, 3, 1) + MB(3, 3, 3)], [90, 30])
chk("k20a", round(float(100000/Q(104, 100)**6), 2), 79031.45)
chk("k20b", round(float(100000*Q(101, 100)**24), 2), 126973.46)
# --- nehéz
chk("n1", [simplify((3*(n + 1) + 2)/(n + 5) - (3*n + 2)/(n + 4)), Q(3*1 + 2, 1 + 4)],
    [10/((n + 4)*(n + 5)), 1])
chk("n1-felso", [3*Q(10) + 2 - 3*(10 + 4), 3*Q(100) + 2 - 3*(100 + 4)], [-10, -10])  # 3n+2 < 3n+12
s = solve([Eq(SS(u, v, 10), 145), Eq(SS(u, v, 20), 590)], [u, v], dict=True)[0]
chk("n2", [s[u], s[v]], [1, 3])
chk("n3", [105, 994, (994 - 105)//7 + 1, SS(105, 7, 128)], [105, 994, 128, 70336])
chk("n4", [MB(2, 3, 3), MB(2, 3, 6), [k for k in range(1, 12) if MB(2, 3, k) > 1000][0], MB(2, 3, 7)],
    [18, 486, 7, 1458])
megold = solve([Eq(MB(u, v, 3) - u, 12), Eq(u*MB(u, v, 3), 64)], [u, v])
chk("n5", sorted([(float(a), float(b)) for a, b in megold]),
    sorted([(4.0, 2.0), (4.0, -2.0), (-16.0, 0.5), (-16.0, -0.5)]))
chk("n6", [[k for k in range(1, 15) if 50*3**k > 100000][0], 50*3**7, 50*3**6], [7, 109350, 36450])
chk("n6b", [[k for k in range(1, 15) if 50*3**k > 10**6][0], 50*3**10, 50*3**9],
    [10, 2952450, 984150])
chk("n7", [2 + 6 + 18, 2*(6 + 6) - (2 + 1 + 18 + 3)], [26, 0])
chk("n8", simplify(SS(3, 2, n) - n*(n + 2)), 0)
chk("n8b", [k for k in range(1, 30) if k*k + 2*k == 195], [13])
chk("joker", [[k for k in range(1, 60) if Q(1, 10000)*2**k > 384000000][0]], [42])
chk("joker-km", [round(float(Q(1, 10000)*2**42/1000)), round(float(Q(1, 10000)*2**41/1000)),
                 float(Q(1, 10000)*2**10*1000)], [439805, 219902, 102.4])
assert not E, E
print("sympy önteszt: OK")

# ============================== ÁBRA (A10) ==============================
ZOLD, KEK, BORO, PIROS = "#047857", "#3b82f6", "#f59e0b", "#ef4444"
_p = lambda f, szin: [(k, f(k), "", szin) for k in range(1, 9)]
def _abra(f, yr, leiras, szin, felirat, egyseg=("1", "1")):
    return (svg_fuggvenyek([], xr=(0, 9), yr=yr, w=290, h=185, jelmagyarazat=False,
                           tengely=("n", "aₙ"), leiras=leiras, egyseg=egyseg,
                           pontok=[(k, f(k), "", szin) for k in range(1, 9)])
            + f'<p class="cap">{felirat}</p>')


A10_ABRA = ('<div class="svgwrap">'
            + _abra(lambda k: 2*k/(k + 3), (0, 2.2), "Az első sorozat pontjai emelkednek, és 2 alatt "
                    "maradnak", ZOLD, "a)")
            + _abra(lambda k: 1 + 5/k, (0, 7), "A második sorozat pontjai süllyednek, és 1 fölött "
                    "maradnak", KEK, "b)")
            + _abra(lambda k: (-1)**(k + 1)*3/k, (-2.2, 3.4), "A harmadik sorozat pontjai felváltva "
                    "a tengely fölött és alatt vannak, egyre közelebb a tengelyhez", BORO, "c)")
            + _abra(lambda k: (k*k + 1)/20, (0, 3.6), "A negyedik sorozat pontjai egyre meredekebben "
                    "emelkednek", PIROS, "d) — egy osztás = 5 egység", ("1", "5"))
            + '</div>')

# ============================== ALAP (28) ==============================
ALAP = [
 # --- A1: a sorozat fogalma és megadása
 (r"Írd fel az alábbi sorozatok első öt tagját!",
  [r"$a_n=\frac{3n+1}{n+2}$", r"$a_n=\frac{6n}{2n-1}$", r"$a_n=\frac{(-1)^n}{n^2+1}$",
   r"$a_n=\frac{n^2}{2^n}$"],
  [r"$\frac{4}{3};\ \frac{7}{4};\ 2;\ \frac{13}{6};\ \frac{16}{7}$",
   r"$6;\ 4;\ \frac{18}{5};\ \frac{24}{7};\ \frac{10}{3}$",
   r"$-\frac{1}{2};\ \frac{1}{5};\ -\frac{1}{10};\ \frac{1}{17};\ -\frac{1}{26}$",
   r"$\frac{1}{2};\ 1;\ \frac{9}{8};\ 1;\ \frac{25}{32}$"]),

 (r"Írd fel a rekurzívan megadott sorozat első öt tagját!",
  [r"$a_1=3$ és $a_{n+1}=a_n+2n$", r"$a_1=1$ és $a_{n+1}=2a_n+1$"],
  [r"$3;\ 5;\ 9;\ 15;\ 23$", r"$1;\ 3;\ 7;\ 15;\ 31$"]),

 (r"Hányadik tagja a $16$ az alábbi sorozatoknak?",
  [r"$a_n=(-2)^{n-3}$", r"$a_n=\left(\frac{1}{2}\right)^{1-n}$", r"$a_n=n^2-17n+16$"],
  [r"a $7.$", r"az $5.$", r"a $17.$ (a másodfokú egyenlet másik gyöke $0$, az viszont nem sorszám)"]),

 (r"Ábrázold az $a_n=2n-5$ sorozat első hat tagját a koordináta-rendszerben! "
  r"Hányadik tagtól pozitív a sorozat?", None,
  r"a tagok: $-3;\ -1;\ 1;\ 3;\ 5;\ 7$ — a $3.$ tagtól pozitív"),

 (r"Folytasd a sorozatot két taggal, és írd fel az általános tagját!",
  [r"$2,\ 9,\ 16,\ 23,\ \dots$", r"$2,\ 6,\ 18,\ 54,\ \dots$", r"$1,\ 4,\ 9,\ 16,\ \dots$"],
  [r"$30$ és $37$; $a_n=7n-5$", r"$162$ és $486$; $b_n=2\cdot 3^{n-1}$", r"$25$ és $36$; $a_n=n^2$"], True),

 (r"A háromszögszámok sorozata $a_n=\frac{n(n+1)}{2}$. Tagja-e ennek a sorozatnak az $55$, illetve a "
  r"$60$? Ha igen, hányadik?", None,
  r"az $55$ a $10.$ tag; a $60$ nem tagja a sorozatnak"),

 # --- A2: monotonitás és korlátosság
 (r"Monoton-e a sorozat? Ha igen, növekvő vagy csökkenő?",
  [r"$a_n=5n-3$", r"$a_n=7-2n$", r"$a_n=(-1)^n\cdot n$"],
  [r"szigorúan növekvő ($a_{n+1}-a_n=5$)", r"szigorúan csökkenő ($a_{n+1}-a_n=-2$)",
   r"nem monoton: $-1;\ 2;\ -3;\ 4;\ \dots$"], True),

 (r"Döntsd el a szomszédos tagok különbségéből, monoton-e a sorozat!",
  [r"$a_n=n^2-n$", r"$a_n=\frac{2n+3}{n}$"],
  [r"a tagok $0;\ 2;\ 6;\ 12;\ \dots$, és $a_{n+1}-a_n=2n\gt 0$, tehát szigorúan növekvő",
   r"$5;\ \frac{7}{2};\ 3;\ \frac{11}{4};\ \dots$ — szigorúan csökkenő"]),

 (r"Adj meg egy alsó és egy felső korlátot, ha van!",
  [r"$a_n=3+\frac{1}{n}$", r"$a_n=(-1)^n$", r"$a_n=n^2$"],
  [r"alsó korlát $3$, felső korlát $4$ (az első tag)", r"alsó korlát $-1$, felső korlát $1$",
   r"alsó korlát $1$; felülről nem korlátos"], True),

 (A10_ABRA + r"Az ábrán négy sorozat első nyolc tagja látható. Mondd meg mindegyikről, hogy "
  r"monoton-e, és hogy korlátos-e!", None,
  [r"szigorúan növekvő és korlátos (minden tagja $0$ és $2$ között van)",
   r"szigorúan csökkenő és korlátos (minden tagja $1$ fölött van, és egyik sem nagyobb $6$-nál)",
   r"nem monoton (váltakozó előjelű), de korlátos",
   r"szigorúan növekvő és felülről nem korlátos"]),

 (r"Vizsgáld meg a sorozatot monotonitás és korlátosság szempontjából!",
  [r"$a_n=2-n$", r"$a_n=\frac{3n-1}{n}$"],
  [r"$1;\ 0;\ -1;\ -2;\ \dots$ — szigorúan csökkenő, felülről korlátos ($1$), alulról nem korlátos",
   r"$2;\ \frac{5}{2};\ \frac{8}{3};\ \dots$ — szigorúan növekvő és korlátos: $2\le a_n\lt 3$"]),

 (r"<b>Maxi trükkje.</b> Maxi szerint az $a_n=\frac{(-1)^n}{n}$ sorozat csökkenő, „mert a nevező "
  r"egyre nagyobb”. Írd fel az első négy tagot, és cáfold meg!", None,
  r"$-1;\ \frac{1}{2};\ -\frac{1}{3};\ \frac{1}{4}$ — a tagok felváltva nőnek és csökkennek, "
  r"tehát a sorozat nem monoton"),

 # --- B1: számtani sorozat
 (r"Írd fel a számtani sorozat első négy tagját!",
  [r"$a_1=3$, $d=2$", r"$a_1=-2$, $d=5$", r"$a_1=7$, $d=-3$", r"$a_1=-5$, $d=-2$"],
  [r"$3;\ 5;\ 7;\ 9$", r"$-2;\ 3;\ 8;\ 13$", r"$7;\ 4;\ 1;\ -2$", r"$-5;\ -7;\ -9;\ -11$"], True),

 (r"Számítsd ki $a_n$ értékét!",
  [r"$a_1=3$, $d=4$, $n=8$", r"$a_1=-5$, $d=2$, $n=12$", r"$a_1=4$, $d=-\frac{1}{4}$, $n=13$",
   r"$a_1=-5$, $d=-2$, $n=16$"],
  [r"$a_8=31$", r"$a_{12}=17$", r"$a_{13}=1$", r"$a_{16}=-35$"], True),

 (r"Számítsd ki az összeget!",
  [r"az $1,\ 4,\ 7,\ \dots$ sorozat első $12$ tagjának összegét",
   r"a $-8,\ -3,\ 2,\ \dots$ sorozat első $36$ tagjának összegét"],
  [r"$S_{12}=210$", r"$S_{36}=2862$"], True),

 (r"A $2,\ 8,\ 14,\ \dots$ számtani sorozatban határozd meg $a_{15}$ és $S_{27}$ értékét!", None,
  r"$a_{15}=86$ és $S_{27}=2160$"),

 (r"A $12,\ 9,\ 6,\ \dots$ számtani sorozatban határozd meg $a_{12}$ és $S_{36}$ értékét!", None,
  r"$a_{12}=-21$ és $S_{36}=-1458$"),

 (r"Határozd meg $n$ és $S_n$ értékét, ha adott az első tag, a különbség és az $n$-edik tag!",
  [r"$a_1=-5$, $d=3$, $a_n=13$", r"$a_1=-1$, $d=-3$, $a_n=-13$", r"$a_1=4$, $d=7$, $a_n=81$",
   r"$a_1=3$, $d=-5$, $a_n=-72$"],
  [r"$n=7$, $S_7=28$", r"$n=5$, $S_5=-35$", r"$n=12$, $S_{12}=510$", r"$n=16$, $S_{16}=-552$"], True),

 (r"Számítsd ki $a_n$ és $S_n$ értékét!",
  [r"$a_1=7$, $d=3$, $n=20$", r"$a_1=3$, $d=6$, $n=28$", r"$a_1=-6$, $d=-3$, $n=27$",
   r"$a_1=-1$, $d=2$, $n=16$"],
  [r"$a_{20}=64$, $S_{20}=710$", r"$a_{28}=165$, $S_{28}=2352$", r"$a_{27}=-84$, $S_{27}=-1215$",
   r"$a_{16}=29$, $S_{16}=224$"], True),

 (r"Milyen $x$ esetén alkot a három szám számtani sorozatot?",
  [r"$3,\ x,\ 11$", r"$5,\ 12,\ x$"], [r"$x=7$", r"$x=19$"], True),

 # --- B2: mértani sorozat és kamat
 (r"Írd fel a mértani sorozat első négy tagját!",
  [r"$b_1=2$, $q=3$", r"$b_1=3$, $q=-\frac{1}{3}$", r"$b_1=1$, $q=-2$", r"$b_1=-4$, $q=2$"],
  [r"$2;\ 6;\ 18;\ 54$", r"$3;\ -1;\ \frac{1}{3};\ -\frac{1}{9}$", r"$1;\ -2;\ 4;\ -8$",
   r"$-4;\ -8;\ -16;\ -32$"], True),

 (r"Határozd meg a hányadost, és írd fel az első öt tagot!",
  [r"$b_1=5$, $b_2=15$", r"$b_1=3$, $b_2=-9$", r"$b_1=\frac{2}{3}$, $b_2=\frac{1}{2}$",
   r"$b_1=-6$, $b_2=12$"],
  [r"$q=3$: $5;\ 15;\ 45;\ 135;\ 405$", r"$q=-3$: $3;\ -9;\ 27;\ -81;\ 243$",
   r"$q=\frac{3}{4}$: $\frac{2}{3};\ \frac{1}{2};\ \frac{3}{8};\ \frac{9}{32};\ \frac{27}{128}$",
   r"$q=-2$: $-6;\ 12;\ -24;\ 48;\ -96$"]),

 (r"Számítsd ki $b_n$ értékét!",
  [r"$b_1=-1$, $q=3$, $n=8$", r"$b_1=-5$, $q=-2$, $n=6$", r"$b_1=-\frac{3}{2}$, $q=-4$, $n=4$",
   r"$b_1=2$, $q=4$, $n=5$"],
  [r"$b_8=-2187$", r"$b_6=160$", r"$b_4=96$", r"$b_5=512$"], True),

 (r"Mennyi a $2,\ -4,\ 8,\ -16,\ \dots$ mértani sorozat első kilenc tagjának összege?", None,
  r"$S_9=342$"),

 (r"Határozd meg $n$ és $S_n$ értékét!",
  [r"$b_1=3$, $q=4$, $b_n=3072$", r"$b_1=27$, $q=\frac{2}{3}$, $b_n=8$"],
  [r"$n=6$, $S_6=4095$", r"$n=4$, $S_4=65$"], True),

 (r"Számítsd ki $b_n$ és $S_n$ értékét!",
  [r"$b_1=2$, $q=-4$, $n=4$", r"$b_1=1$, $q=3$, $n=6$", r"$b_1=-1$, $q=5$, $n=5$",
   r"$b_1=3$, $q=\frac{1}{3}$, $n=4$"],
  [r"$b_4=-128$, $S_4=-102$", r"$b_6=243$, $S_6=364$", r"$b_5=-625$, $S_5=-781$",
   r"$b_4=\frac{1}{9}$, $S_4=\frac{40}{9}$"], True),

 (r"Milyen pozitív $x$ esetén alkot a három szám mértani sorozatot?",
  [r"$4,\ x,\ 25$", r"$2,\ x,\ 18$"],
  [r"$x=10$ (a $-10$ is megoldás, ha nem kötjük ki a pozitív előjelet)",
   r"$x=6$ (a $-6$ is megoldás, ha nem kötjük ki a pozitív előjelet)"], True),

 (r"💰 $80\,000$ dinárt helyezel el $3$ évre, évi $5\%$-os kamatláb mellett. Mennyi lesz a számlán "
  r"a futamidő végén, ha a kamat",
  [r"egyszerű kamatként jár (mindig a kezdő tőkére)?",
   r"kamatos kamatként, évente egyszer jóváírva jár? (Kerekíts két tizedesjegyre!)"],
  [r"$80\,000\cdot 1{,}15=92\,000$ dinár", r"$80\,000\cdot 1{,}05^{3}=92\,610{,}00$ dinár"]),
]

# ============================== KÖZÉP (20) ==============================
KOZEP = [
 (r"Az $a_1=2$, $a_{n+1}=a_n+3$ rekurzív sorozatnál írd fel az első öt tagot, majd az általános "
  r"tagot is!", None, r"$2;\ 5;\ 8;\ 11;\ 14$, az általános tag $a_n=3n-1$"),

 (r"Hányadik tagja a $16$ az $a_n=\log_2(n+1)$ sorozatnak?", None,
  r"a $65\,535.$ tag, mert $n+1=2^{16}=65\,536$"),

 (r"Van-e olyan tagja az $a_n=n^2-7n+12$ sorozatnak, amelyik $0$? Ha igen, melyik — és "
  r"vigyázz, hány ilyen tag van!", None,
  r"két ilyen tag is van: a $3.$ és a $4.$"),

 (r"Egy sorozat általános tagja $a_n=(n-1)(n-2)(n-3)+2n-1$. Az első három tagja $1$, $3$, $5$, "
  r"ezért egy kadét azt mondja, a negyedik tag $7$. Számítsd ki a negyedik tagot!", None,
  r"$a_4=3\cdot 2\cdot 1+7=13$ — a felsorolás nem határozza meg a sorozatot"),

 (r"Vizsgáld meg az $a_n=\frac{2n-1}{n+1}$ sorozatot monotonitás és korlátosság szempontjából!", None,
  r"$a_{n+1}-a_n=\frac{3}{(n+1)(n+2)}\gt 0$, tehát szigorúan növekvő; korlátos: "
  r"$\frac{1}{2}\le a_n\lt 2$"),

 (r"Vizsgáld meg az $a_n=\frac{n+2}{2n+1}$ sorozatot monotonitás és korlátosság szempontjából!", None,
  r"$a_{n+1}-a_n=-\frac{3}{(2n+1)(2n+3)}\lt 0$, tehát szigorúan csökkenő; korlátos: "
  r"$\frac{1}{2}\lt a_n\le 1$"),

 (r"Mi a legkisebb egész felső korlátja az $a_n=\frac{3n}{n+1}$ sorozatnak?", None,
  r"$3$ — a tagok ($\frac{3}{2};\ 2;\ \frac{9}{4};\ \dots$) egyre nagyobbak, de $3$ alatt maradnak"),

 (r"<b>Maxi trükkje.</b> Maxi szerint az $a_n=n^2-12n+40$ sorozat növekvő, „mert a négyzetes tag "
  r"együtthatója pozitív”. Írd fel az első nyolc tagot, és döntsd el, igaza van-e!", None,
  r"$29;\ 20;\ 13;\ 8;\ 5;\ 4;\ 5;\ 8$ — a $6.$ tagig csökken, utána nő, tehát nem monoton"),

 (r"Írd fel a számtani sorozat első négy tagját!",
  [r"$a_8=38$ és $a_{21}=103$", r"$a_6=2$ és $a_{15}=-16$"],
  [r"$d=5$, $a_1=3$: $3;\ 8;\ 13;\ 18$", r"$d=-2$, $a_1=12$: $12;\ 10;\ 8;\ 6$"]),

 (r"Egy számtani sorozat ötödik tagja $a_5=6$, tizenkettedik tagja $a_{12}=-15$. Számítsd ki az "
  r"első $18$ tag összegét!", None, r"$d=-3$, $a_1=18$, $S_{18}=-135$"),

 (r"Egy számtani sorozat második és negyedik tagjának összege $16$, ötödik és első tagjának "
  r"különbsége $28$. Határozd meg a sorozat első öt tagját!", None,
  r"a különbség $7$, az első tag $-6$: $-6;\ 1;\ 8;\ 15;\ 22$"),

 (r"Határozd meg a számtani sorozat első tagját és különbségét!",
  [r"$a_3+a_6=20$ és $a_9-a_2=14$", r"$a_1+2a_5=0$ és $S_4=14$",
   r"$2a_4+a_6=48$ és $5a_5-7a_2=29$"],
  [r"$a_1=3$, $d=2$", r"$a_1=8$, $d=-3$", r"$a_1=5$, $d=3$"], True),

 (r"Oldd meg az egyenleteket!",
  [r"$5+8+11+\dots+x=124$", r"$4+9+14+\dots+x=172$", r"$-3+1+5+\dots+x=150$"],
  [r"$x=26$", r"$x=39$", r"$x=33$"], True),

 (r"Határozd meg $n$ és $a_n$ értékét!",
  [r"$a_1=3$, $d=1$, $S_n=250$", r"$a_1=18$, $d=-3$, $S_n=54$", r"$a_1=2$, $d=5$, $S_n=245$",
   r"$a_1=-2$, $d=-5$, $S_n=-555$"],
  [r"$n=20$, $a_{20}=22$", r"<b>két megoldás:</b> $n=4$, $a_4=9$ vagy $n=9$, $a_9=-6$",
   r"$n=10$, $a_{10}=47$", r"$n=15$, $a_{15}=-72$"]),

 (r"Határozd meg $n$ és $b_n$ értékét!",
  [r"$b_1=2$, $q=\frac{1}{2}$, $S_n=\frac{31}{8}$", r"$b_1=2$, $q=-3$, $S_n=-40$"],
  [r"$n=5$, $b_5=\frac{1}{8}$", r"$n=4$, $b_4=-54$"], True),

 (r"Írd fel a mértani sorozat első négy tagját!",
  [r"$b_4=32$ és $b_9=1024$", r"$b_2=10$ és $b_7=-320$", r"$b_3=-27$ és $b_6=729$",
   r"$b_4=18$ és $b_6=162$"],
  [r"$4;\ 8;\ 16;\ 32$", r"$-5;\ 10;\ -20;\ 40$", r"$-3;\ 9;\ -27;\ 81$",
   r"<b>két megoldás</b> ($q^2=9$): $\frac{2}{3};\ 2;\ 6;\ 18$ vagy "
   r"$-\frac{2}{3};\ 2;\ -6;\ 18$"]),

 (r"Határozd meg a mértani sorozat első négy tagját!",
  [r"$b_1+b_3=-20$ és $b_2+b_4=-40$", r"$b_5-b_1=80$ és $b_3+b_1=10$",
   r"$b_6-b_4=216$ és $b_3-b_1=8$"],
  [r"$-4;\ -8;\ -16;\ -32$", r"<b>két megoldás:</b> $1;\ 3;\ 9;\ 27$ vagy $1;\ -3;\ 9;\ -27$",
   r"$1;\ 3;\ 9;\ 27$"]),

 (r"Oldd meg az egyenleteket!",
  [r"$3+6+12+\dots+x=189$", r"$2+6+18+\dots+x=728$", r"$4+8+16+\dots+x=2044$"],
  [r"$x=96$", r"$x=486$", r"$x=1024$"], True),

 (r"Egy mértani sorozatban a második és a negyedik tag összege $90$, az első és a harmadik tagé "
  r"$30$. Írd fel a sorozat első négy tagját!", None, r"$q=3$, $b_1=3$: $3;\ 9;\ 27;\ 81$"),

 (r"💰 A bank évi $4\%$-os kamatot fizet. Kerekíts mindkét részfeladatban két tizedesjegyre!",
  [r"Mekkora összeget kell ma elhelyezned ahhoz, hogy $6$ év múlva $100\,000$ dinárod legyen, ha a "
   r"kamatot évente egyszer írják jóvá?",
   r"Mennyi lenne $100\,000$ dinárból $6$ év múlva, ha a kamatot <b>negyedévente</b> írnák jóvá?"],
  [r"$K_0=\frac{100\,000}{1{,}04^{6}}=79\,031{,}45$ dinár",
   r"negyedévente $1\%$, összesen $24$ jóváírás: $100\,000\cdot 1{,}01^{24}=126\,973{,}46$ dinár"]),
]

# ============================== NEHÉZ (8) ==============================
NEHEZ = [
 (r"Igazold, hogy az $a_n=\frac{3n+2}{n+4}$ sorozat szigorúan monoton növekvő, és hogy minden "
  r"tagja $1$ és $3$ közé esik!", None,
  r"$a_{n+1}-a_n=\frac{10}{(n+4)(n+5)}\gt 0$, tehát növekvő; így a legkisebb tag $a_1=1$, felülről "
  r"pedig $3$ korlátozza, mert $\frac{3n+2}{n+4}\lt 3$ minden $n$-re ($3n+2\lt 3n+12$)"),

 (r"Egy számtani sorozat első tíz tagjának összege $145$, az első húsz tagé $590$. Írd fel a "
  r"sorozat első négy tagját!", None, r"$a_1=1$, $d=3$: $1;\ 4;\ 7;\ 10$"),

 (r"Hány olyan háromjegyű szám van, amely osztható $7$-tel, és mennyi ezek összege?", None,
  r"az első $105$, az utolsó $994$, tehát $128$ ilyen szám van, az összegük $70\,336$"),

 (r"Egy mértani sorozat harmadik tagja $18$, hatodik tagja $486$. Hányadik tagtól haladja meg a "
  r"sorozat az $1000$-et?", None, r"$q=3$, $b_1=2$; $b_6=486$, $b_7=1458$, tehát a $7.$ tagtól"),

 (r"Egy mértani sorozatban a harmadik és az első tag különbsége $12$, az első és a harmadik tag "
  r"szorzata $64$. Határozd meg a sorozatot! <i>(Több megoldás is van — keresd meg mindet!)</i>", None,
  r"<b>négy megoldás:</b> $b_1=4$, $q=2$ · $b_1=4$, $q=-2$ · $b_1=-16$, $q=\frac{1}{2}$ · "
  r"$b_1=-16$, $q=-\frac{1}{2}$"),

 (r"Egy baktériumtelep óránként a háromszorosára nő. Kezdetben $50$ baktérium van a telepben.",
  [r"Hányadik óra végén haladja meg a telep a $100\,000$ baktériumot?",
   r"És hányadik óra végén az egymilliót?"],
  [r"$50\cdot 3^{7}=109\,350$, tehát a $7.$ óra végén (a $6.$ óra végén még csak $36\,450$)",
   r"$50\cdot 3^{10}=2\,952\,450$, tehát a $10.$ óra végén (a $9.$ óra végén még csak $984\,150$)"]),

 (r"Három szám összege $26$, és mértani sorozatot alkot. Ha rendre $1$-gyel, $6$-tal és $3$-mal "
  r"növeljük őket, számtani sorozatot kapunk. Melyik ez a három szám?", None,
  r"$2;\ 6;\ 18$ (a megnövelt számok: $3;\ 12;\ 21$ — valóban számtani sorozat, $d=9$). "
  r"A másodfokú egyenlet másik gyöke, $q=\frac{1}{3}$, ugyanezt a három számot adja fordított "
  r"sorrendben"),

 (r"Egy számtani sorozat $n$-edik tagja $a_n=2n+1$.",
  [r"Fejezd ki az első $n$ tag összegét $n$ segítségével!",
   r"Hány tagot kell összeadni ahhoz, hogy az összeg $195$ legyen?"],
  [r"$S_n=n^2+2n$", r"$n=13$"]),
]

JOKER = (r"Egy papírlap vastagsága $0{,}1$ mm. Képzeld el, hogy félbe tudod hajtani akárhányszor — "
         r"minden hajtásnál kétszereződik a vastagság.",
         [r"$0{,}1\ \text{mm}\cdot 2^{10}=102{,}4$ mm, azaz nagyjából $10$ cm",
          r"$42$ hajtás kell: $0{,}1\ \text{mm}\cdot 2^{42}\approx 439\,800$ km, ami már több, "
          r"mint $384\,000$ km (a $41.$ hajtásnál még csak $219\,900$ km)"],
         [r"Milyen vastag a köteg $10$ hajtás után?",
          r"Hányadik hajtás után haladja meg a vastagság a Hold távolságát, $384\,000$ km-t?"])

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1], JOKER[2]),
]
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (28, 20, 8), (len(ALAP), len(KOZEP), len(NEHEZ))

ut = oldal(tagozat="3e", mappa="06-indukcio-sorozatok", fajl="feladatok-sorozatok.html",
           cim="Sorozatok", temakor="Matematikai indukció. Sorozatok",
           alcim="A sorozat fogalma és megadása, monotonitás és korlátosság, számtani és mértani "
                 "sorozat, összegképletek, kamatszámítás. Számológép használható: a nem egész "
                 "eredményeket két tizedesjegyre kerekítsd. A végeredmény minden feladatnál "
                 "lenyitható — előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-mertani-sorozat.html", prevc="A mértani sorozat és a kamatos kamat",
           nxt="feladatok-hazi.html", nxtc="Kristály-kamra — Vészterem")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP), "Nehéz", len(NEHEZ), "+ Joker")
