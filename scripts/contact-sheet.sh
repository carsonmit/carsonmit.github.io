#!/usr/bin/env bash
# Contact sheet for a mockup: one image with Night and Day, at desktop (1280×900) and phone (375×812) width,
# plus a report of console errors and sideways scrolling on phones.
#
# Usage:   scripts/contact-sheet.sh design/mockups/home-doors-3d-r2.html [wait-ms]
# Needs:   the local server running (the "site" entry in .claude/launch.json), and playwright-cli (see README "Tools").
# Output:  design/mockups/shots/<page>-sheet.png and four single shots beside it (not committed; see .gitignore).
set -euo pipefail

PAGE="${1:?Give the mockup path, e.g. design/mockups/home-doors-3d-r2.html}"
WAIT="${2:-3000}"                      # how long to let each view settle (3D scenes rise in and fonts load)
BASE="${BASE:-http://127.0.0.1:8770}"  # the port in .claude/launch.json
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/design/mockups/shots"
NAME="$(basename "$PAGE" .html)"
mkdir -p "$OUT"

if ! curl -s -o /dev/null "$BASE/$PAGE"; then
  echo "The local server isn't answering at $BASE. Start it first (preview \"site\", or: python3 -m http.server 8770 --bind 127.0.0.1)." >&2
  exit 1
fi

S="sheet-$$"
playwright-cli -s="$S" open "about:blank" >/dev/null
trap 'playwright-cli -s="$S" close >/dev/null 2>&1 || true' EXIT

playwright-cli -s="$S" run-code "async page => {
  const url = '$BASE/$PAGE', out = '$OUT', name = '$NAME', wait = $WAIT;
  const errors = [], overflow = [], shots = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push(String(e)));
  for (const theme of ['night', 'day']) {
    for (const [label, w, h] of [['desktop', 1280, 900], ['phone', 375, 812]]) {
      await page.setViewportSize({ width: w, height: h });
      await page.goto(url);
      await page.evaluate(t => localStorage.setItem('theme', t), theme);
      await page.reload();
      await page.waitForTimeout(wait);
      const sideways = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      if (sideways > 0) overflow.push(theme + ' ' + label + ': ' + sideways + 'px too wide');
      const file = out + '/' + name + '-' + theme + '-' + label + '.png';
      const png = await page.screenshot({ path: file, fullPage: true });
      shots.push({ data: png.toString('base64'), caption: theme + ' · ' + label });
    }
  }
  // Lay the four shots out on one sheet: desktop pair on top, phone pair under it
  const img = s => 'data:image/png;base64,' + s.data;
  const cell = s => '<figure><img src=\"' + img(s) + '\"><figcaption>' + s.caption + '</figcaption></figure>';
  await page.setViewportSize({ width: 2600, height: 900 });
  await page.setContent('<style>body{margin:0;padding:24px;background:#888;font:600 22px system-ui;display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}figure{margin:0}img{width:100%;display:block}.p{display:flex;gap:24px;justify-content:center}.p img{width:375px}</style>'
    + cell(shots[0]) + cell(shots[2]) + '<div class=p>' + cell(shots[1]) + '</div><div class=p>' + cell(shots[3]) + '</div>');
  await page.screenshot({ path: out + '/' + name + '-sheet.png', fullPage: true });
  return { sheet: out + '/' + name + '-sheet.png', consoleErrors: [...new Set(errors)], sidewaysScroll: overflow };
}" | awk '/^### Result/ { getline; print; done = 1 } /^### Error/ { err = 1 } err && !/^### Ran/ { print } /^### Ran/ { err = 0 }'   # print only the result (or the error)
