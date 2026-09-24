# Generated asset builder. Run from the repository root: python3 tools/build_stack.py
import json, os

ICONS = json.load(open("tools/icons.json"))
os.makedirs("assets", exist_ok=True)

FONT = "system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"

DARK = dict(
    bg="#0D1117", panel="#FFFFFF", panel_op="0.045", border="#30363D",
    title="#E6EDF3", text="#C9D1D9", muted="#8B949E",
)
LIGHT = dict(
    bg="#FFFFFF", panel="#F6F8FA", panel_op="1", border="#D8DEE4",
    title="#1F2328", text="#1F2328", muted="#59636E",
)

GROUPS = [
    ("Mobile", [
        ("kotlin", "Kotlin", "#7F52FF"), ("openjdk", "Java", "#E76F00"),
        ("jetpackcompose", "Jetpack Compose", "#4285F4"), ("android", "Android", "#3DDC84"),
        ("react", "React Native", "#61DAFB"), ("expo", "Expo", "#6C7A89"),
        ("flutter", "Flutter", "#40A3DB"), ("capacitor", "Capacitor", "#119EFF"),
    ]),
    ("Web and backend", [
        ("typescript", "TypeScript", "#3178C6"), ("nextdotjs", "Next.js", "#7D8590"),
        ("nodedotjs", "Node.js", "#5FA04E"), ("postgresql", "PostgreSQL", "#4169E1"),
        ("payloadcms", "Payload CMS", "#8A93A5"), ("tailwindcss", "Tailwind", "#06B6D4"),
    ]),
    ("Delivery and platform", [
        ("cloudflare", "Cloudflare", "#F38020"), ("vercel", "Vercel", "#8A93A5"),
        ("firebase", "Firebase", "#FFA000"), ("githubactions", "CI/CD", "#2F81F7"),
        ("sentry", "Sentry", "#9E86FF"), ("claude", "AI-assisted delivery", "#D97757"),
    ]),
    ("Devices and payments", [
        ("bluetooth", "BLE and USB", "#3B9EFF"), ("mqtt", "MQTT", "#A45BA4"),
        ("googleplay", "QRIS, EMV, NFC", "#3DDC84"),
    ]),
]

CHAR_W = 8.05   # approx advance width at 14px for the fallback chain
PAD_X, ICON, GAP, PILL_H, ROW_GAP, COL_GAP = 13, 17, 9, 34, 12, 9
WIDTH, MARGIN = 880, 22


def pill_w(label):
    return PAD_X * 2 + ICON + GAP + len(label) * CHAR_W


def icon_glyph(slug, color, x, y, size=ICON):
    d = ICONS.get(slug)
    if not d:
        return f'<circle cx="{x + size/2:.1f}" cy="{y + size/2:.1f}" r="{size/2.4:.1f}" fill="{color}"/>'
    s = size / 24.0
    return (f'<g transform="translate({x:.1f},{y:.1f}) scale({s:.4f})">'
            f'<path d="{d}" fill="{color}"/></g>')


def build_stack(theme, name):
    t = theme
    rows, y = [], 26
    for title, items in GROUPS:
        rows.append(f'<text x="{MARGIN}" y="{y}" fill="{t["muted"]}" font-size="12.5" '
                    f'font-weight="700" letter-spacing="1.3">{title.upper()}</text>')
        y += 16
        x = MARGIN
        for slug, label, color in items:
            w = pill_w(label)
            if x + w > WIDTH - MARGIN:
                x = MARGIN
                y += PILL_H + 8
            rows.append(
                f'<g><rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{PILL_H}" rx="{PILL_H/2}" '
                f'fill="{t["panel"]}" fill-opacity="{t["panel_op"]}" stroke="{t["border"]}"/>'
                + icon_glyph(slug, color, x + PAD_X, y + (PILL_H - ICON) / 2)
                + f'<text x="{x + PAD_X + ICON + GAP:.1f}" y="{y + PILL_H/2 + 4.8:.1f}" '
                f'fill="{t["text"]}" font-size="14" font-weight="500">{label}</text></g>')
            x += w + COL_GAP
        y += PILL_H + ROW_GAP + 10
    h = y - 6
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {h}" width="{WIDTH}" '
           f'height="{h}" role="img" aria-label="Technology stack">'
           f'<rect width="{WIDTH}" height="{h}" fill="{t["bg"]}"/>'
           f'<g font-family="{FONT}">' + "".join(rows) + '</g></svg>')
    open(f"assets/{name}", "w").write(svg)
    return h


for theme, name in ((DARK, "stack-dark.svg"), (LIGHT, "stack-light.svg")):
    print(name, build_stack(theme, name))
