# Generated asset builder. Run from the repository root: python3 tools/build_buttons.py
import json
ICONS = json.load(open("tools/icons.json"))
FONT = "system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"

BUTTONS = [
    ("portfolio", "googlechrome", "astu.app", "#61DAFB"),
    ("play", "googleplay", "Google Play", "#3DDC84"),
    ("printama", "github", "Printama", "#F5A623"),
    ("community", "googlechrome", "mobiledev.id", "#A78BFA"),
    ("linkedin", "linkedin", "LinkedIn", "#2F81F7"),
]

THEMES = {
    "dark": dict(bg="#161B22", border="#30363D", text="#E6EDF3"),
    "light": dict(bg="#F6F8FA", border="#D8DEE4", text="#1F2328"),
}

H, ICON, PAD, GAP, CHAR = 38, 16, 16, 9, 7.9

for name, slug, label, color in BUTTONS:
    w = PAD * 2 + ICON + GAP + len(label) * CHAR
    for mode, t in THEMES.items():
        s = ICON / 24.0
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {H}" width="{w:.0f}" '
               f'height="{H}" role="img" aria-label="{label}">'
               f'<rect x="0.5" y="0.5" width="{w-1:.0f}" height="{H-1}" rx="{(H-1)/2}" '
               f'fill="{t["bg"]}" stroke="{t["border"]}"/>'
               f'<g transform="translate({PAD},{(H-ICON)/2:.0f}) scale({s:.4f})">'
               f'<path d="{ICONS[slug]}" fill="{color}"/></g>'
               f'<text x="{PAD+ICON+GAP:.0f}" y="{H/2+4.8:.0f}" font-family="{FONT}" font-size="13.5" '
               f'font-weight="600" fill="{t["text"]}">{label}</text></svg>')
        open(f"assets/btn-{name}-{mode}.svg", "w").write(svg)
print("buttons written")
