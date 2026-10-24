"""Re-encode a Manim render to a small web MP4 (H.264, no audio, faststart)
and save a poster PNG.  Uses PyAV (bundled with Manim), no ffmpeg CLI needed.

    ~/.venvs/manim/bin/python encode.py SRC.mp4 OUT.mp4 POSTER.png [crf] [width] [poster_t]
"""
import sys, av
from fractions import Fraction

src, out, poster = sys.argv[1:4]
crf = sys.argv[4] if len(sys.argv) > 4 else "30"
width = int(sys.argv[5]) if len(sys.argv) > 5 else 1200
poster_t = float(sys.argv[6]) if len(sys.argv) > 6 else 15.0
# Optional "r,g,b" nudge added to every pixel before encoding. Dark colors round slightly
# during compression, so the night video needs a tiny correction to land exactly on the
# page's background color (measured in the browser; see README "Tools").
nudge = [int(v) for v in sys.argv[7].split(",")] if len(sys.argv) > 7 else None
height = width * 3 // 4

inp = av.open(src)
vin = inp.streams.video[0]
fps = Fraction(30, 1)
outc = av.open(out, "w", options={"movflags": "+faststart"})
vs = outc.add_stream("libx264", rate=fps)
vs.width, vs.height, vs.pix_fmt = width, height, "yuv420p"
vs.options = {"crf": crf, "preset": "slow", "tune": "animation", "profile:v": "high",
              "x264-params": "colorprim=bt709:transfer=iec61966-2-1:colormatrix=bt709:range=tv"}
best = None
for i, frame in enumerate(inp.decode(vin)):
    t = float(frame.time)
    # Convert with the BT.709 matrix and label the file as sRGB (below), so browsers show
    # exactly the colors Manim drew; unlabeled video gets color-shifted and its background
    # no longer matches the page.
    rgb = frame.reformat(width=width, height=height, format="rgb24", src_colorspace="ITU601",
                         interpolation="LANCZOS")
    if nudge:
        import numpy as np
        arr = np.clip(rgb.to_ndarray().astype(np.int16) + np.array(nudge, np.int16), 0, 255).astype(np.uint8)
        rgb = av.VideoFrame.from_ndarray(arr, format="rgb24")
    img = rgb.reformat(format="yuv420p", dst_colorspace="ITU709")
    img.pts = i
    img.time_base = 1 / fps
    for pkt in vs.encode(img):
        outc.mux(pkt)
    if best is None or abs(t - poster_t) < abs(best[0] - poster_t):
        best = (t, frame.to_image())
for pkt in vs.encode():
    outc.mux(pkt)
outc.close()
best[1].resize((width, height)).save(poster, optimize=True)
print("frames", i + 1, "poster at", round(best[0], 2))
