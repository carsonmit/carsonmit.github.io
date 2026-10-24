/* Carson Mitchell's site: shared script for every page (the day/night switch). */
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

/* ── Day/night switch ── */
const root = document.documentElement, modeBtn = document.getElementById('mode');
function label() { modeBtn.setAttribute('aria-checked', root.dataset.theme === 'day' ? 'false' : 'true'); }
function apply(t) { root.dataset.theme = t; label(); try { localStorage.setItem('theme', t); } catch (e) {} document.dispatchEvent(new Event('themechange')); }
label();
modeBtn.addEventListener('click', () => {
  const next = root.dataset.theme === 'day' ? 'night' : 'day';
  if (!document.startViewTransition) {
    // Older browsers: fade every color on the page together for 0.3 s.
    root.classList.add('fade'); apply(next); setTimeout(() => root.classList.remove('fade'), 350); return;
  }
  root.classList.add('vt');
  if (reduce.matches) {
    // Reduced motion: no spreading circle, just one gentle crossfade of the whole page.
    root.classList.add('vt-fade');
    document.startViewTransition(() => apply(next)).finished.finally(() => root.classList.remove('vt', 'vt-fade'));
    return;
  }
  // Spread the new mode as a circle from the button, covering the farthest corner.
  const r = modeBtn.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
  // In percentages, not pixels: some browsers (high-density screens, zoom) size the snapshot
  // differently, and pixel values then put the circle in the wrong place and too small.
  // A circle's % radius is measured against sqrt(w² + h²) / sqrt(2).
  const w = innerWidth, h = innerHeight;
  const end = Math.hypot(Math.max(x, w - x), Math.max(y, h - y)) / (Math.hypot(w, h) / Math.SQRT2) * 100;
  const at = `at ${x / w * 100}% ${y / h * 100}%`;
  const vt = document.startViewTransition(() => apply(next));
  vt.ready.then(() => root.animate(
    { clipPath: [`circle(0% ${at})`, `circle(${end}% ${at})`] },
    { duration: 560, easing: 'cubic-bezier(0.77, 0, 0.175, 1)', pseudoElement: '::view-transition-new(root)' }
  ));
  vt.finished.finally(() => root.classList.remove('vt'));
});

/* ── KaTeX (math typesetting) loads with `defer`; this resolves once it's ready (or failed). ── */
const katexReady = new Promise(r => { const el = document.querySelector('script[src*="katex.min.js"]'); if (window.katex || !el) return r(); el.addEventListener('load', r, { once: true }); el.addEventListener('error', r, { once: true }); });

/* ── Email: the address is never written in the page, so spam bots that read pages can't collect it.
   It shows as "carsonm6719 [at] gmail [dot] com"; clicking it opens a new email, built only at that moment. ── */
document.querySelectorAll('a.email').forEach(a => a.addEventListener('click', e => {
  e.preventDefault(); location.href = 'mailto:' + a.dataset.user + '@' + a.dataset.host;
}));
