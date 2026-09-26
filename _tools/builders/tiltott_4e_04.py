# -*- coding: utf-8 -*-
"""4e/04 — tiltott adatok a weboldal számára: a 25/26-os és a 26/27-es integrál-felmérők (3. ellenőrző, 4. dolgozat)
integrandusai és területfüggvényei, valamint a két görbe közötti területek görbepárjai (párként és különbségként).
Forrás: projektek/4e/munkafajlok/build_felmero_4e_04.py (2026-09-26). A felmérők nem kerülnek a webre, és a web
anyagai nem használhatják az adataikat — a 04-es builderek ezzel a modullal ellenőrzik magukat."""
import sympy

x = sympy.symbols("x", positive=True)
_LD = {"x": x, "R": sympy.Rational, "sqrt": sympy.sqrt, "log": sympy.log, "exp": sympy.exp, "sin": sympy.sin,
       "cos": sympy.cos, "tan": sympy.tan, "pi": sympy.pi}

TILTOTT = [
    '(-2*x+7)/(-x**2+7*x)',
    '(10*x-3)/(5*x**2-3*x+4)',
    '(2*x**3+4)/x**2',
    '(2*x**4+5*x-3)/x',
    '(2*x**4-3)/x**2',
    '(2*x+3)/(x**2+3*x-1)',
    '(2*x+5)**5',
    '(2*x+6)**3',
    '(2*x-3)**4',
    '(2*x-7)**6',
    '(3*x**2-12*x)/(x**3-6*x**2)',
    '(3*x**3-2)/x',
    '(3*x**3-5)/x**2',
    '(3*x-2)**4',
    '(3*x-4)**6',
    '(4*x**3+3)/x**2',
    '(4*x+1)**5',
    '(4*x-5)/(2*x**2-5*x+1)',
    '(4*x-6)/(x**2-3*x+1)',
    '(5*x-2)**4',
    '(6*x+4)/(3*x**2+4*x-2)',
    '(6*x-1)**3',
    '(6*x-2)/(3*x**2-2*x+5)',
    '(9*x-1)**3',
    '(x**3+2*x**2-3)/x',
    '(x**3+2*x**2-3)/x**2',
    '(x**3-4*x+2)/x',
    '(x**4-3*x**2+5)/x',
    '(x+2)*(x-3)',
    '(x+5)*(x-1)',
    '(x-1)*(x+4)',
    '-2/sin(x)**2',
    '-3*sin(x)',
    '-3/(x*log(x))',
    '-5*x**R(3,7)+3/x**R(3,4)',
    '1/(2*x-5)',
    '1/(3*x+2)',
    '1/(4*x+3)',
    '1/x**7',
    '10/x**6',
    '11*x**R(5,6)-4/x**R(1,3)',
    '11/sin(x)**2',
    '12*x**3+2*x',
    '12/x**5',
    '18*x**R(4,5)+1/x**R(1,3)',
    '2*exp(2*x)',
    '2*x*(x**2-3)**5',
    '2*x**3-3*x**2+4*x+5',
    '2*x**R(3,4)-3/sqrt(x)',
    '2/x',
    '28*x**3+6*x',
    '3*cos(x)+4/cos(x)**2',
    '3*exp(3*x)',
    '3*sin(3*x)',
    '3*sqrt(x)',
    '3*x**2*(x**3+2)**4',
    '3*x**2+2',
    '3*x**2+4*x',
    '3*x**2+8*x',
    '3*x**5',
    '3*x**R(2,3)-4/x**R(1,4)',
    '3*x**R(3,5)-8/x**R(2,7)',
    '3/x',
    '4*exp(2*x)',
    '4*exp(4*x)',
    '4*sin(x)+3/sin(x)**2',
    '4*x**11',
    '4*x**3*(x**4-1)**3',
    '4*x**3-3',
    '4*x**3-6*x**2+5',
    '4*x**3-9*x**2+2*x-7',
    '4*x**R(2,5)-2/x**R(1,3)',
    '4*x**R(3,5)-2/x**R(2,3)',
    '4/x',
    '5*cos(5*x)',
    '5*cos(x)-2/cos(x)**2',
    '5*sin(x)/cos(x)**5',
    '5*x**4-12*x**3-3',
    '5*x**4-8*x**3+3*x**2-1',
    '5*x**9',
    '5*x**R(1,4)-4/x**R(2,5)',
    '5/cos(x)**2',
    '5/sin(x)**2',
    '5/x',
    '50*x**49',
    '6*exp(3*x)',
    '6*sqrt(x)',
    '6*x**2+2*x',
    '6*x**2-2*x',
    '6*x**2-4*x',
    '6*x**5+4*x**3-7',
    '6*x**7',
    '6*x**R(1,5)-3/x**R(3,4)',
    '6/cos(x)**2',
    '6/x**4',
    '7*x**8',
    '7/cos(x)**2',
    '8*x**3+3*x**2',
    '8*x**3+6*x**2-4*x+3',
    '8*x**3-9*x**2+2',
    '8/cos(x)**2',
    '9*cos(x)',
    'cos(4*x)',
    'cos(x)',
    'exp(-2*x)',
    'exp(-3*x)',
    'exp(-x/2)',
    'exp(7*x)',
    'log(x)**2/x',
    'log(x)**3/x',
    'log(x)**5/x',
    'sin(3*x)',
    'sin(5*x)',
    'sin(x)',
    'sqrt(x)',
    'x**100',
    'x**2+1',
    'x**2+2',
    'x**2+3',
    'x**2+5',
    'x**2/(x**3+8)',
    'x**3+2*x+2',
    'x**3-2*x+1',
    'x**3-4*x',
    'x**3-9*x',
    'x**3-x',
    'x**5+2*x**3-x+7',
    'x*sqrt(x**2+3)',
    'x*sqrt(x**2+5)',
    'x*sqrt(x**2+7)',
    'x-3*x**2']

TILTOTT_PAR = [
    ('x**2', '2*x+3'),
    ('x**2-4', '-x**2+14'),
    ('x**2', 'x+6'),
    ('x**2-2*x', '4*x-x**2'),
    ('x**2', '3*x+4'),
    ('x**2-2*x-3', '-x**2+2*x+3'),
    ('x**2', '6*x'),
    ('x**2-3', '-x**2+5'),
    ('x**2+2*x', '6*x-3'),
    ('2*x**2-1', '-x**2+11')]

_P = (0.37, 1.91, 2.63, 3.3)


def _e(s):
    return s if isinstance(s, sympy.Basic) else sympy.sympify(s, locals=_LD)


def azonos(u, v):
    try:
        a, b = _e(u), _e(v)
        return all(abs(complex(a.subs(x, t)) - complex(b.subs(x, t))) < 1e-9 for t in _P)
    except (TypeError, ZeroDivisionError, ValueError):
        return False


def ellenoriz(kifejezesek=(), parok=()):
    """[(ok, kifejezés, tiltott)] — üres lista: minden rendben."""
    hibak = []
    for u in kifejezesek:
        for r in TILTOTT:
            if azonos(u, r):
                hibak.append(("tiltott", u, r))
    for f, g in parok:
        for a, b in TILTOTT_PAR:
            if (azonos(f, a) and azonos(g, b)) or (azonos(f, b) and azonos(g, a)) \
               or azonos(f"({g})-({f})", f"({b})-({a})") or azonos(f"({f})-({g})", f"({b})-({a})"):
                hibak.append(("tiltott görbepár", (f, g), (a, b)))
    return hibak
