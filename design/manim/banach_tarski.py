"""
Banach–Tarski (free-group paradox), a ~54.5 s silent looping animation.
Moves are named by direction, as in Vsauce's telling: up, down, left, right.

Two color versions from one file:
    manim -ql --media_dir media banach_tarski.py BanachTarskiNight BanachTarskiDay
    manim -qh --fps 30 --media_dir media banach_tarski.py BanachTarskiNight BanachTarskiDay

Beats (start times in seconds, for the HTML captions): see BEATS below.

Math notes
* Chocolate: a 5x4 bar is cut by the line y = 1.5 + x/5, a vertical cut
  x = 1 above it, and a horizontal cut y = 3 for 0 <= x <= 1. The upper
  piece slides one column left along the cut (so it drops 1/5), the thin
  left column moves to the right end, and the top-left square is spare.
  The rebuilt bar is 5 x (4 - 1/5): it lost exactly one square's area as a
  sliver along the top. Checked numerically below (areas + tiling).
* Tree / ball: the free group F2 on a = right, b = up (a^-1 = left,
  b^-1 = down). S(x) = reduced words starting with x, and
  a·S(a^-1) = S(a^-1) ∪ S(b) ∪ S(b^-1) ∪ {e}.
* The point cloud is a picture of "every point colored by its piece"
  (the real pieces cannot be drawn). When a piece turns, each point of the
  three pieces it becomes grows out of the nearest turned point.
"""

from manim import *
import itertools
import numpy as np

# ---------- frame: 4:3 ----------
config.frame_height = 8.0
config.frame_width = 8.0 * 4 / 3
config.pixel_width = int(round(config.pixel_height * 4 / 3))

# keys: a = right, A = left, b = up, B = down
PALETTES = {
    "night": dict(
        bg="#151a21", ink="#F2EFE8", muted="#A19E96", hi="#F2EFE8",
        b="#C9ACDE",   # up    : lilac (accent)
        a="#EE9CA7",   # right : warm rose
        B="#E2CF9E",   # down  : pale sand
        A="#8FB4E8",   # left  : sky periwinkle
        choc="#8C6F54", choc_gap="#56443A", shade=0.022,
        # slightly richer variants, used only for the point cloud
        cloud=dict(b="#B78CE6", a="#F2879C", B="#E6C77E", A="#7EA8EC"),
    ),
    "day": dict(
        bg="#F3EBDD", ink="#1f1a14", muted="#5c5348", hi="#FCF5EA",
        b="#6C4487",   # up    : plum (accent)
        a="#A13F5E",   # right : deep rose
        B="#7A6230",   # down  : dark sand
        A="#3E6597",   # left  : dusk blue
        choc="#94734F", choc_gap="#5E4733", shade=0.05,
        cloud=dict(b="#6C4487", a="#A13F5E", B="#7A6230", A="#3E6597"),
    ),
}

BEATS = [
    (0.0, "chocolate bar is cut, rearranged, one square spare"),
    (6.2, "reveal: the rebuilt bar is a sliver shorter"),
    (11.0, "one solid ball"),
    (14.5, "four turns: up, down, left, right; tree of move sequences grows"),
    (22.5, "tree splits by first move into four pieces + the point e"),
    (28.0, "left piece turned right covers left+up+down: with right = whole"),
    (36.0, "every point of the ball colored by its piece"),
    (41.5, "split into two pairs; in each, one piece turns and fills its ball"),
    (48.8, "two solid balls (same size as the first) + the spare point e"),
]

R = 2.1          # ball radius (every ball has this radius)
L = 1.1          # first edge length; tree reaches 1.875 L < R
SIDE = 2.4       # x-offset of the two final balls
MAXD = 4         # tree depth (legible at ~600 px wide)

DIRS = {"a": RIGHT, "A": LEFT, "b": UP, "B": DOWN}
INV = {"a": "A", "A": "a", "b": "B", "B": "b"}
EDGE_W = {1: 7.0, 2: 5.4, 3: 4.0, 4: 3.0}
DOT_R = {0: 0.10, 1: 0.07, 2: 0.053, 3: 0.04, 4: 0.031}


# ======================= chocolate geometry ========================
CM, CN, CC = 5, 4, 1.5             # columns, rows, cut-line height at x=0
CS = 0.95                          # square size (frame units)
CX0, CY0 = -1.15, -2.4             # bar's bottom-left corner on screen
CHOC = {
    "P1": [(0, 0), (CM, 0), (CM, CC + 1), (0, CC)],
    "P2": [(1, CC + 1 / CM), (CM, CC + 1), (CM, CN), (1, CN)],
    "P3": [(0, CC), (1, CC + 1 / CM), (1, CN - 1), (0, CN - 1)],
    "P4": [(0, CN - 1), (1, CN - 1), (1, CN), (0, CN)],
}
CHOC_MOVE = {                      # final translation of each piece (units)
    "P1": (0, 0),
    "P2": (-1, -1 / CM),
    "P3": (CM - 1, 1 - 1 / CM),
    "P4": (-2.6, -(CN - 1)),          # spare square, left of the bar
}


def shoelace(P):
    return 0.5 * abs(sum(P[i][0] * P[(i + 1) % len(P)][1]
                         - P[(i + 1) % len(P)][0] * P[i][1] for i in range(len(P))))


def inside_convex(P, x, y):
    s = [np.sign((P[(i + 1) % len(P)][0] - P[i][0]) * (y - P[i][1])
                 - (P[(i + 1) % len(P)][1] - P[i][1]) * (x - P[i][0]))
         for i in range(len(P))]
    return all(v > 0 for v in s) or all(v < 0 for v in s)


def check_chocolate():
    areas = {k: shoelace(P) for k, P in CHOC.items()}
    assert abs(sum(areas.values()) - CM * CN) < 1e-9, areas
    assert abs(areas["P4"] - 1) < 1e-9
    moved = {k: [(x + CHOC_MOVE[k][0], y + CHOC_MOVE[k][1]) for x, y in P]
             for k, P in CHOC.items()}
    rebuilt = ["P1", "P2", "P3"]
    assert abs(sum(areas[k] for k in rebuilt) - CM * (CN - 1 / CM)) < 1e-9
    # tiling check on a fine grid (offsets avoid every boundary)
    H = CN - 1 / CM
    for x in np.linspace(0.0137, CM - 0.0113, 181):
        for y in np.linspace(0.0071, CN - 0.0059, 151):
            k = sum(inside_convex(moved[p], x, y) for p in rebuilt)
            assert k == (1 if y < H - 1e-6 else 0) or abs(y - H) < 0.02, (x, y, k)
    # spare square sits clear of the bar
    assert max(x for x, _ in moved["P4"]) < -0.3


check_chocolate()


def clip_convex(subject, clip):
    """Sutherland–Hodgman: polygon `subject` clipped to convex `clip` (ccw)."""
    out = list(subject)
    n = len(clip)
    for i in range(n):
        a, b = np.array(clip[i]), np.array(clip[(i + 1) % n])
        inp, out = out, []
        if not inp:
            break

        def inside(p):
            return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) >= -1e-12

        def inter(p, q):
            p, q = np.array(p), np.array(q)
            d = q - p
            e = b - a
            t = ((a[0] - p[0]) * e[1] - (a[1] - p[1]) * e[0]) / (d[0] * e[1] - d[1] * e[0])
            return tuple(p + t * d)

        for j in range(len(inp)):
            cur, prev = inp[j], inp[j - 1]
            if inside(cur):
                if not inside(prev):
                    out.append(inter(prev, cur))
                out.append(cur)
            elif inside(prev):
                out.append(inter(prev, cur))
    return out


# ======================= tree helpers ========================
def reduced_words(maxd, first=None, exclude_first=None):
    out = []
    frontier = [(c,) for c in "aAbB"
                if (first is None or c == first) and c != exclude_first]
    for _ in range(maxd):
        out.extend(frontier)
        frontier = [w + (c,) for w in frontier for c in "aAbB" if c != INV[w[-1]]]
    return out


def pos(word):
    p = np.zeros(3)
    for i, c in enumerate(word):
        p = p + DIRS[c] * L / 2 ** i
    return p


# ======================= point-cloud helpers ========================
def cube_rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3))
            for i, (p, s) in enumerate(zip(perm, signs)):
                M[i, p] = s
            if np.isclose(np.linalg.det(M), 1):
                mats.append(M)
    assert len(mats) == 24
    return mats


ROT_RIGHT = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]], float)   # front -> right
ROT_UP = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], float)      # front -> up


def rot_y(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])


def rot_x_up(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[1, 0, 0], [0, c, s], [0, -s, c]])


assert np.allclose(rot_y(PI / 2), ROT_RIGHT) and np.allclose(rot_x_up(PI / 2), ROT_UP)


class BanachTarskiBase(Scene):
    MODE = "night"

    # ---------- small builders ----------
    def first_col(self, word):
        return self.P["ink"] if len(word) == 0 else self.P[word[0]]

    def step_col(self, word):
        return self.P["ink"] if len(word) == 0 else self.P[word[-1]]

    def edge(self, word, center, color):
        return Line(center + pos(word[:-1]), center + pos(word),
                    stroke_width=EDGE_W[len(word)], color=color,
                    cap_style=CapStyleType.ROUND)

    def dot(self, word, center, color):
        return Dot(center + pos(word), radius=DOT_R[len(word)], color=color)

    def ball(self, center, dim=False):
        """Flat layers only: base disk, stepped highlight toward upper left,
        equator and meridian (front solid, back dashed)."""
        P = self.P
        k = 0.35 if dim else 1.0
        disk = Circle(radius=R, stroke_color=P["ink"], stroke_width=3,
                      stroke_opacity=0.9 * k, fill_color=P["ink"],
                      fill_opacity=0.09 * k).move_to(center)
        layers = VGroup()
        for i in range(1, 9):
            r = R * (1 - 0.095 * i)
            off = (R - r) * 0.62 * normalize(UL)
            layers.add(Circle(radius=r, stroke_width=0, fill_color=P["hi"],
                              fill_opacity=P["shade"] * k).move_to(center + off))

        def ellipse(rx, ry, t0, t1):
            return ParametricFunction(
                lambda t: center + np.array([rx * np.cos(t), ry * np.sin(t), 0]),
                t_range=[t0, t1], stroke_width=1.6, color=P["muted"])

        eq_front = ellipse(R, 0.26 * R, PI, TAU).set_stroke(opacity=0.7 * k)
        eq_back = DashedVMobject(ellipse(R, 0.26 * R, 0, PI), num_dashes=22)
        eq_back.set_stroke(opacity=0.35 * k)
        me_front = ellipse(0.3 * R, R, -PI / 2, PI / 2).set_stroke(opacity=0.7 * k)
        me_back = DashedVMobject(ellipse(0.3 * R, R, PI / 2, 3 * PI / 2), num_dashes=22)
        me_back.set_stroke(opacity=0.35 * k)
        return VGroup(disk, layers, eq_back, me_back, eq_front, me_front)

    def piece(self, first, center):
        words = reduced_words(MAXD, first=first)
        stem = self.edge((first,), center, self.step_col((first,)))
        edges = VGroup(*[self.edge(w, center, self.step_col(w))
                         for w in words if len(w) >= 2])
        dots = VGroup(*[self.dot(w, center, self.step_col(w)) for w in words])
        return dict(words=words, stem=stem, edges=edges, dots=dots,
                    body=VGroup(edges, dots), all=VGroup(stem, edges, dots))

    def moved_target(self, pc, center):
        words = pc["words"]
        edges = VGroup(*[self.edge(w[1:], center, self.first_col(w[1:]))
                         for w in words if len(w) >= 2])
        dots = VGroup(*[self.dot(w[1:], center, self.first_col(w[1:])) for w in words])
        return VGroup(edges, dots)

    def missing_level(self, exclude_first, center):
        words = [w for w in reduced_words(MAXD, exclude_first=exclude_first)
                 if len(w) == MAXD]
        edges = VGroup(*[self.edge(w, center, self.first_col(w)) for w in words])
        dots = VGroup(*[self.dot(w, center, self.first_col(w)) for w in words])
        return edges, dots

    def until(self, t):
        dt = t - self.renderer.time
        if dt > 1e-3:
            self.wait(dt)

    # ---------- chocolate ----------
    def scr(self, x, y):
        return np.array([CX0 + x * CS, CY0 + y * CS, 0])

    def choc_piece(self, key):
        P = self.P
        poly = CHOC[key]
        base = Polygon(*[self.scr(x, y) for x, y in poly], stroke_width=0,
                       fill_color=P["choc_gap"], fill_opacity=1)
        g = 0.075
        tiles = VGroup()
        for i in range(CM):
            for j in range(CN):
                sq = [(i + g, j + g), (i + 1 - g, j + g), (i + 1 - g, j + 1 - g), (i + g, j + 1 - g)]
                cl = clip_convex(sq, poly)
                if len(cl) >= 3 and shoelace(cl) > 1e-4:
                    tiles.add(Polygon(*[self.scr(x, y) for x, y in cl], stroke_width=0,
                                      fill_color=P["choc"], fill_opacity=1))
        return VGroup(base, tiles)

    def chocolate(self):
        P = self.P
        pcs = {k: self.choc_piece(k) for k in CHOC}
        bar = VGroup(*pcs.values())
        self.play(FadeIn(bar, shift=0.15 * UP), run_time=0.9)
        cut_kw = dict(stroke_width=3, color=P["ink"], dash_length=0.1)
        cuts = VGroup(
            DashedLine(self.scr(-0.15, CC - 0.15 / CM), self.scr(CM + 0.15, CC + 1 + 0.15 / CM), **cut_kw),
            DashedLine(self.scr(1, CC + 1 / CM), self.scr(1, CN + 0.15), **cut_kw),
            DashedLine(self.scr(-0.15, CN - 1), self.scr(1, CN - 1), **cut_kw),
        )
        self.play(LaggedStart(*[Create(c) for c in cuts], lag_ratio=0.35), run_time=1.0)
        # 1) thin left column + corner square step out to the left
        self.play(VGroup(pcs["P3"], pcs["P4"]).animate.shift(LEFT * 1.4 * CS),
                  FadeOut(cuts), run_time=0.6)
        # 2) the big upper piece slides one column along the cut, while the
        #    corner square moves further left (clear of everything)
        dx, dy = CHOC_MOVE["P2"]
        self.play(pcs["P2"].animate.shift(np.array([dx, dy, 0]) * CS),
                  pcs["P4"].animate.shift(LEFT * (-CHOC_MOVE["P4"][0] - 1.4) * CS),
                  run_time=0.8, rate_func=smooth)
        # 3) corner square drops to its spare spot; the column lifts above
        #    the bar, crosses over it, and drops into the empty right end
        lift = CN + 0.15 - CC
        self.play(pcs["P4"].animate.shift(DOWN * (CN - 1) * CS),
                  pcs["P3"].animate.shift(UP * lift * CS), run_time=0.7)
        self.play(pcs["P3"].animate.shift(RIGHT * (CHOC_MOVE["P3"][0] + 1.4) * CS),
                  run_time=0.8)
        self.play(pcs["P3"].animate.shift(DOWN * (lift - CHOC_MOVE["P3"][1]) * CS),
                  run_time=0.5, rate_func=rush_into)
        # the rebuilt bar, drawn clean (rows are 1/20 shorter: 3.8/4 each)
        H = CN - 1 / CM
        hr = H / CN
        g = 0.075
        clean = VGroup(Rectangle(width=CM * CS, height=H * CS, stroke_width=0,
                                 fill_color=P["choc_gap"], fill_opacity=1)
                       .move_to(self.scr(CM / 2, H / 2)))
        for i in range(CM):
            for j in range(CN):
                clean.add(Rectangle(width=(1 - 2 * g) * CS, height=(1 - 2 * g) * hr * CS,
                                    stroke_width=0, fill_color=P["choc"], fill_opacity=1)
                          .move_to(self.scr(i + 0.5, (j + 0.5) * hr)))
        self.play(FadeIn(clean), run_time=0.4)
        self.remove(pcs["P1"], pcs["P2"], pcs["P3"])
        bar = VGroup(clean, pcs["P4"])
        self.until(6.2)
        # reveal: outline of the original bar; the sliver it lost
        outline = DashedVMobject(
            Rectangle(width=CM * CS, height=CN * CS, stroke_width=2.5, color=P["ink"])
            .move_to(self.scr(CM / 2, CN / 2)), num_dashes=60)
        sliver = Rectangle(width=CM * CS, height=CS / CM, stroke_width=0,
                           fill_color=P["b"], fill_opacity=0.55
                           ).move_to(self.scr(CM / 2, CN - 1 / (2 * CM)))
        self.play(Create(outline), FadeIn(sliver), run_time=0.7)
        self.until(10.3)
        self.play(FadeOut(VGroup(bar, outline, sliver)), run_time=0.7)

    # ---------- point cloud ----------
    def build_cloud(self):
        """Random points filling the ball, each colored by its piece
        (balanced). Hidden 'spawn' dots are the three quarters a turned
        piece sweeps into."""
        rng = np.random.default_rng(11)
        n = 640
        v = rng.normal(size=(n, 3))
        v = v / np.linalg.norm(v, axis=1, keepdims=True)
        pts = v * (0.93 * R) * rng.random((n, 1)) ** (1 / 3)
        cols = np.array(list("aAbB" * (n // 4)))
        rng.shuffle(cols)
        self.pts, self.cols = pts, cols
        CP = self.P["cloud"]

        def mk(c, p3, cen, vis, sc):
            dt = Dot(radius=0.05, color=CP[c])
            dt.p3, dt.cen, dt.vis, dt.sc = p3.copy(), cen.copy(), vis, sc
            return dt

        allg = VGroup()
        self.base = {}
        for j in np.argsort(pts[:, 2]):
            dt = mk(cols[j], pts[j], ORIGIN, 0.0, 1.0)
            self.base[j] = dt
            allg.add(dt)
        self.spawn = {}
        for tag, keys, cen in (("L", "AbB", LEFT * SIDE), ("R", "BaA", RIGHT * SIDE)):
            lst = []
            for k in np.argsort(pts[:, 2]):
                if cols[k] in keys:
                    dt = mk(cols[k], pts[k], cen, 0.0, 1.0)
                    dt.target = pts[k].copy()
                    lst.append(dt)
                    allg.add(dt)
            self.spawn[tag] = lst
        for dt in allg:
            self.refresh(dt)
        self.cloud = allg
        return allg

    def refresh(self, dt):
        t = (dt.p3[2] / R + 1) / 2
        r = (0.045 + 0.03 * t) * max(dt.sc, 1e-3)
        dt.set_width(2 * r)
        dt.move_to(dt.cen + np.array([dt.p3[0], dt.p3[1], 0]))
        dt.set_fill(opacity=(0.5 + 0.5 * t) * dt.vis)

    def cloud_anim(self, items, run_time, rate_func=smooth):
        """items: list of (dot, f) where f(dot, alpha) updates its state."""
        def upd(mob, alpha):
            a = rate_func(alpha)
            for dt, f in items:
                f(dt, a)
                self.refresh(dt)
        return UpdateFromAlphaFunc(self.cloud, upd, run_time=run_time,
                                   rate_func=linear)

    def rot_arrow(self, center, radius, a0, a1, color):
        """Curved arrow concentric with a ball, from angle a0 to a1 (deg)."""
        arc = Arc(radius=radius, start_angle=a0 * DEGREES, angle=(a1 - a0) * DEGREES,
                  arc_center=center, stroke_width=5, color=color)
        arc.add_tip(tip_length=0.24, tip_width=0.24)
        return arc

    def turn_and_fill(self, piece_key, rot, tag, arrow):
        self.play(Create(arrow), run_time=0.4)
        movers = [dt for j, dt in self.base.items() if self.cols[j] == piece_key]
        for dt in movers:
            dt.p0 = dt.p3.copy()
        # the piece turns a quarter turn, in the arrow's direction ...
        self.play(self.cloud_anim(
            [(dt, lambda d, a: setattr(d, "p3", rot(PI / 2 * a) @ d.p0)) for dt in movers],
            run_time=1.3))
        # ... and keeps sweeping the same way, fanning out over the three
        # quarters it becomes (its own color + the two others)
        items = []
        for dt in movers:
            dt.p1 = dt.p3.copy()

            def go_on(d, a):
                d.p3 = rot(PI / 3 * a) @ d.p1
                d.vis = 1 - a
            items.append((dt, go_on))

        def sweep(d, a):
            d.p3 = rot(-PI / 2 * (1 - a)) @ d.target
            d.vis = min(1.0, 1.6 * a)
        items += [(dt, sweep) for dt in self.spawn[tag]]
        self.play(self.cloud_anim(items, run_time=1.0), FadeOut(arrow), run_time=1.0)

    # ---------- the film ----------
    def construct(self):
        P = dict(PALETTES[self.MODE])
        self.P = P
        self.camera.background_color = P["bg"]
        O = ORIGIN

        # ===== chocolate (0 s) =====
        self.chocolate()
        self.until(11.0)

        # ===== the ball (8 s) =====
        ball = self.ball(O)
        self.play(FadeIn(ball, scale=0.96), run_time=1.2, rate_func=smooth)
        self.until(14.5)

        # ===== four turns, tree grows on the ball (10 s) =====
        keys = VGroup(*[
            Arrow(DIRS[c] * (R + 0.2), DIRS[c] * (R + 0.95), buff=0,
                  stroke_width=6, max_tip_length_to_length_ratio=0.38, color=P[c])
            for c in "baBA"])
        self.play(LaggedStart(*[GrowArrow(k) for k in keys], lag_ratio=0.25), run_time=1.8)
        self.wait(0.4)
        self.play(Transform(ball, self.ball(O, dim=True)), run_time=0.5)
        e_dot = Dot(O, radius=DOT_R[0], color=P["ink"])
        self.play(GrowFromCenter(e_dot), run_time=0.3)

        pieces = {c: self.piece(c, O) for c in "aAbB"}

        def by_depth(d):
            es, ds = [], []
            for c in "aAbB":
                pc = pieces[c]
                if d == 1:
                    es.append(pc["stem"])
                ds += [m for w, m in zip(pc["words"], pc["dots"]) if len(w) == d]
                es += [m for w, m in zip([w for w in pc["words"] if len(w) >= 2],
                                         pc["edges"]) if len(w) == d]
            return es, ds

        level_times = {1: 1.1, 2: 1.0, 3: 0.9, 4: 0.9}
        for d in range(1, MAXD + 1):
            es, ds = by_depth(d)
            anims = [Create(m) for m in es] + [GrowFromCenter(m) for m in ds]
            if d == 3:
                anims.append(FadeOut(keys))
            self.play(*anims, run_time=level_times[d], rate_func=smooth)
            self.bring_to_front(*ds)
        for c in "aAbB":
            self.remove(*pieces[c]["all"].family_members_with_points())
            self.add(pieces[c]["all"])
        self.add(e_dot)
        self.until(22.5)

        # ===== four pieces by first move (15.5 s) =====
        for c in "bAaB":
            self.play(pieces[c]["all"].animate.set_color(P[c]), run_time=0.9)
            self.wait(0.25)
        self.bring_to_front(e_dot)
        self.play(e_dot.animate.scale(1.8), run_time=0.4)
        self.play(e_dot.animate.scale(1 / 1.8), run_time=0.4)
        self.until(28.0)

        # ===== key move, on the ball (20 s) =====
        pa = pieces["A"]
        others = VGroup(pieces["a"]["all"], pieces["b"]["all"], pieces["B"]["all"])
        arrow_tree = self.rot_arrow(O, R + 0.22, 128, 52, P["a"])
        self.play(others.animate.set_opacity(0.22), run_time=0.6)
        self.play(Create(arrow_tree), FadeOut(pa["stem"]), run_time=0.6)
        self.play(Transform(pa["body"], self.moved_target(pa, O)),
                  run_time=2.6, rate_func=smooth)
        new_e, new_d = self.missing_level(exclude_first="a", center=O)
        self.play(*[Create(m) for m in new_e], *[GrowFromCenter(m) for m in new_d],
                  run_time=0.6)
        self.wait(0.8)
        self.play(pieces["a"]["all"].animate.set_opacity(1), FadeOut(arrow_tree),
                  run_time=0.8)
        self.bring_to_front(e_dot)
        self.until(36.0)

        # ===== the ball as a cloud of colored points (24.5 s) =====
        cloud = self.build_cloud()
        self.add(cloud)
        self.bring_to_front(e_dot)
        outline = Circle(radius=R, stroke_color=P["ink"], stroke_width=3, stroke_opacity=0.9)
        tree_all = VGroup(others, pa["body"], new_e, new_d)
        base = list(self.base.values())

        def fade_in(d, a):
            d.vis = a
        self.play(self.cloud_anim([(dt, fade_in) for dt in base], run_time=2.0),
                  FadeOut(tree_all), FadeOut(ball), FadeIn(outline),
                  run_time=2.0)
        self.until(41.5)

        # ===== split into two pairs (26.5 s) =====
        CL, CR = LEFT * SIDE, RIGHT * SIDE
        out_L, out_R = outline, outline.copy()
        self.add(out_R)
        items = []
        for j, dt in self.base.items():
            target = CL if self.cols[j] in "aA" else CR

            def mv(d, a, t=target):
                d.cen = t * a
            items.append((dt, mv))
        self.play(self.cloud_anim(items, run_time=1.8),
                  out_L.animate.move_to(CL), out_R.animate.move_to(CR),
                  run_time=1.8, rate_func=smooth)
        # e stays behind between the balls: neither copy needs it, since each
        # turned piece already covers its own e (spare, like the chocolate square)
        self.bring_to_front(e_dot)
        self.until(43.3)

        # ===== each pair: one piece turns and fills in (28.3 s) =====
        arrow_r = self.rot_arrow(CL, R + 0.22, 128, 52, P["a"])
        arrow_u = self.rot_arrow(CR, R + 0.07, -38, 38, P["b"])
        self.turn_and_fill("A", rot_y, "L", arrow_r)
        self.turn_and_fill("B", rot_x_up, "R", arrow_u)
        self.until(48.8)

        # ===== two solid balls (33.8 s) =====
        ball_L, ball_R = self.ball(CL), self.ball(CR)

        vis_dots = [dt for dt in self.cloud if dt.vis > 0 and dt.sc > 0]
        for dt in vis_dots:
            dt.v0 = dt.vis

        def fo(d, a):
            d.vis = d.v0 * (1 - a)
        self.play(FadeIn(ball_L), FadeIn(ball_R),
                  self.cloud_anim([(dt, fo) for dt in vis_dots], run_time=1.4),
                  FadeOut(out_L), FadeOut(out_R), run_time=1.4)
        self.remove(self.cloud)
        self.until(53.5)
        self.play(FadeOut(ball_L), FadeOut(ball_R), FadeOut(e_dot), run_time=1.0)
        self.until(54.5)


class BanachTarskiNight(BanachTarskiBase):
    MODE = "night"


class BanachTarskiDay(BanachTarskiBase):
    MODE = "day"
