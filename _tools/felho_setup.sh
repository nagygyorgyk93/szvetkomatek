#!/usr/bin/env bash
# Szvetkó matek — felhős munkamenet (Claude Code on the web) előkészítése.
# A .claude/settings.json SessionStart-hookja hívja. Helyi gépen (Cowork, saját gép)
# azonnal kilép: csak akkor fut, ha CLAUDE_CODE_REMOTE=true. Idempotens, gyors ha minden megvan.
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/..}" 2>/dev/null || exit 0

allapot=()
# 1) Python: sympy + mpmath (builderek, kulcs-öntesztek)
if ! python3 -c "import sympy, mpmath" 2>/dev/null; then
  pip install -q sympy mpmath >/dev/null 2>&1 || pip install -q --break-system-packages sympy mpmath >/dev/null 2>&1
fi
python3 -c "import sympy, mpmath" 2>/dev/null && allapot+=("sympy ✓") || allapot+=("sympy ✗")

# 2) jsdom a verify_web.py render-rétegéhez (a verify_jsdom.mjs a /tmp/vw alatt keresi)
if [ ! -d /tmp/vw/node_modules/jsdom ]; then
  npm install --silent --no-audit --no-fund jsdom --prefix /tmp/vw >/dev/null 2>&1
fi
[ -d /tmp/vw/node_modules/jsdom ] && allapot+=("jsdom ✓") || allapot+=("jsdom ✗ (verify_web csak kánon-réteggel)")

# 3) Playwright a layout_teszt.py-hoz (böngésző-réteg) — ha nincs, megpróbáljuk
if ! python3 -c "import playwright" 2>/dev/null; then
  pip install -q playwright >/dev/null 2>&1 || pip install -q --break-system-packages playwright >/dev/null 2>&1
fi
python3 -c "import playwright" 2>/dev/null && allapot+=("playwright ✓") || allapot+=("playwright ✗")

# A hook kimenete a munkamenet kontextusába kerül — rövid legyen.
echo "Szvetkó matek felhős munkamenet — eszközök: ${allapot[*]}."
echo "Előbb olvasd el: CLAUDE.md, majd _docs/FELHO_FELADATOK.md (feladatlista, zárolt területek)."
echo "A tiltott-listák (felmérő-adat) itt NINCSENEK meg: a builderek figyelmeztetnek — ez várt viselkedés."
exit 0
