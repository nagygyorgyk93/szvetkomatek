<!-- TÜKÖR — ne szerkeszd itt! Forrás (a tanár gépén): _JELOLESEK.md · tükrözve: 2026-09-27 · _tools/docs_tukor.py -->

# Jelölés-kánon — geometria (síkidomok és testek)

*Kötelező érvényű a **teljes** korpuszra: weboldal, feladatgyűjtemények, felmérők,
megoldókulcsok, óravázlatok, ábrák. Forrás: a felhasználó saját **Képlettára**
(`Képlettár.docx`), a `Képletek - csonkagúla.pdf` és a `Csonka kúp.jpg`.
Rögzítve: 2026-08-20.*

> **Miért van rá szükség.** A 3e/01 (Poliéderek) először $m$-mel jelölte a testmagasságot,
> $m_o$-val az oldallap magasságát, $b$-vel a gúla oldalélét és $\rho$-val az apotémát.
> A diák viszont a **saját képlettárából** tanul, ahol $H$, $h$, $s$ és $r$ szerepel — két
> jelölésrendszer között kell fordítania, ami fölösleges kognitív teher és hibaforrás.
> **A weboldal a képlettárat követi, nem fordítva.**

## 1. Testek — az általános jelölések

| Jel | Jelentés | Megjegyzés |
|---|---|---|
| $H$ | **testmagasság** | mindig nagy H — ez a test két alaplapja, illetve alaplapja és csúcsa közti távolság |
| $h$ | **oldallap magassága** (gúla, csonkagúla), illetve az **alaplap** valamely magassága | alsó index a hovatartozásról: $h_a$, $h_b$, $h_c$ |
| $s$ | **oldalél** (hasáb, gúla, csonkagúla), illetve **alkotó** (henger, kúp, csonkakúp) | egyenes hasábnál és hengernél $s=H$ |
| $D$ | **testátló** | |
| $d$ | **lapátló** — alaplapé és oldallapoké | alsó index: hasábnál $d$ az alaplap átlója és $d_1$ az oldallapé; téglatestnél $d_1,d_2,d_3$ a három különböző lapátló |
| $r$ | az alaplap **beírt** körének sugara (**apotéma**); a henger/kúp **alapkörének** sugara; a **gömb síkmetszetének** sugara | |
| $R$ | az alaplap **köré írt** körének sugara; a **gömb** sugara; a **csonkakúp nagyobbik** alapkörének sugara | |
| $B$ | **alapterület** | a képlettárban még $A_t$ — a webes kánon $B$ |
| $M$ | a **palást területe** | a képlettárban még $P_t$ — a webes kánon $M$ |
| $F$, $V$ | felszín, térfogat | |
| $a$ | alapél | |

**Kulcsösszefüggések (szabályos gúla):**

$$H^2=h^2-r^2,\qquad H^2=s^2-R^2,\qquad h^2=s^2-\left(\frac a2\right)^2,\qquad R^2=r^2+\left(\frac a2\right)^2$$

## 2. Csonkagúla

| Jel | Jelentés |
|---|---|
| $a_1$, $a_2$ | az **alaplap**, illetve a **fedőlap** éle |
| $B_1$, $B_2$ | az alaplap, illetve a fedőlap **területe** |
| $r_1$, $r_2$ | a két lap **apotémája** (beírt kör sugara) |
| $R_1$, $R_2$ | a két lap **köré írt** körének sugara |
| $H$, $h$, $s$ | testmagasság · oldallap (trapéz) magassága · oldalél |

$$F=B_1+B_2+M,\qquad V=\frac H3\left(B_1+\sqrt{B_1B_2}+B_2\right)$$
$$M=n\cdot\frac{a_1+a_2}{2}\cdot h,\qquad s^2=H^2+(R_1-R_2)^2,\qquad h^2=H^2+(r_1-r_2)^2$$

## 3. Forgástestek

| Test | Jelölések | Képletek |
|---|---|---|
| **henger** | $r$, $H$, $s$ ($=H$) | $B=r^2\pi$, $M=2r\pi H$, $V=r^2\pi H$, $F=2r^2\pi+2r\pi H$ |
| **kúp** | $r$, $H$, $s$ (alkotó) | $B=r^2\pi$, $M=r s\pi$, $V=\dfrac{r^2\pi H}{3}$, $F=r^2\pi+rs\pi$, $s^2=r^2+H^2$ |
| **csonkakúp** | $R$ (alsó), $r$ (felső), $H$, $s$ | $V=\dfrac{H\pi}{3}(R^2+Rr+r^2)$, $F=R^2\pi+r^2\pi+(R+r)s\pi$, $s^2=H^2+(R-r)^2$ |
| **gömb** | $R$ (sugár); a **síkmetszet** sugara $r$ | $F=4R^2\pi$, $V=\dfrac{4R^3\pi}{3}$ |

A csonkakúp tengelymetszete: $K=2R+2r+2s$, $T=(R+r)\cdot H$.

## 4. Síkidomok

| Alakzat | Jelölések |
|---|---|
| **háromszög** | $a$, $b$, $c$ oldalak; $h_a$, $h_b$, $h_c$ magasságok; $r$ beírt, $R$ köré írt kör sugara |
| **szabályos háromszög** | $h=\dfrac{a\sqrt3}{2}$, $r=\dfrac h3=\dfrac{a\sqrt3}{6}$, $R=\dfrac{2h}{3}=\dfrac{a\sqrt3}{3}$ |
| **paralelogramma** | $a$, $b$ oldalak; $h_a$, $h_b$ magasságok |
| **rombusz** | $a$ oldal, $h$ magasság, $d_1$, $d_2$ átlók, $r=\dfrac h2$ |
| **téglalap** | $a$, $b$ oldalak; $d$ átló; $R=\dfrac d2$ |
| **négyzet** | $a$ oldal; $d=a\sqrt2$; $r=\dfrac a2$; $R=\dfrac d2=\dfrac{a\sqrt2}{2}$ |
| **trapéz** | $a$, $b$ **alapok**; $c$, $d$ **szárak**; $h$ magasság; **$m$ a középvonal**: $m=\dfrac{a+b}{2}$, $T=m\cdot h$ |
| **szabályos hatszög** | $a$ oldal; $h=r=\dfrac{a\sqrt3}{2}$; $R=a$; **hosszabb** átló $D=2a$, **rövidebb** átló $d=a\sqrt3$ |

> ⚠️ A trapéznál az $m$ **a középvonal**, nem a magasság. Ez a leggyakoribb ütközés a régi
> anyagokkal — magasság mindenütt $h$ (síkidom) vagy $H$ (test).

## 5. Amit ez felülír (a 2026-08-20 előtti anyagokban)

| Régi | Új |
|---|---|
| $m$ (testmagasság) | **$H$** |
| $m_o$ (oldallap magassága) | **$h$** |
| $b$ (gúla oldaléle), $c$ (csonkagúla oldaléle) | **$s$** |
| $\rho$ (apotéma) | **$r$** |
| $m$ (síkidom magassága), $m_a$ | **$h$**, **$h_a$** |
| csonkagúla $a$, $a_1$ (élek) | **$a_1$, $a_2$** |
| csonkagúla $B$, $b$ (lapterületek) | **$B_1$, $B_2$** |
| gömb $r$ | **$R$** (a síkmetszeté marad $r$) |

## 6. Hol kell betartani

- `web/_tools/builders/*.py` — minden tananyag-, feladatgyűjtemény- és egyéb builder
- `web/_tools/builders/abra_common.py` — az SVG-generátorok **alapértelmezett feliratai**
- `web/_tools/kulcsok/*.py` — a megoldókulcs-öntesztek kommentárjai és segédfüggvényei
- `projektek/*/munkafajlok/` — felmérő-builderek, terepküldetés-kulcsok, narratíva-tervek
- minden új DOCX (feladatlap, dolgozat, megoldókulcs, óravázlat)
