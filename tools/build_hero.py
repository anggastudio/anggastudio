# Generated asset builder. Run from the repository root: python3 tools/build_hero.py
FONT = "system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"

CHIPS = [("Shipping since 2016", "#3DDC84"), ("15 apps on Google Play", "#61DAFB"),
         ("34 projects on astu.app", "#A78BFA"), ("400+ payment terminals", "#F5A623")]

THEMES = {
    "dark": dict(bg1="#0D1117", bg2="#111A28", bg3="#16263B", grid="#FFFFFF", grid_op="0.04",
                 name="#F0F6FC", role="#9FB3C8", sub="#7D8590", chip_bg="#FFFFFF",
                 chip_op="0.06", device="#0D1117", device_stroke_op="0.5", halo_op="0.07"),
    "light": dict(bg1="#FFFFFF", bg2="#F6F8FA", bg3="#EAF1F8", grid="#1F2328", grid_op="0.035",
                  name="#0D1117", role="#42505F", sub="#6A7580", chip_bg="#FFFFFF",
                  chip_op="0.85", device="#FFFFFF", device_stroke_op="0.45", halo_op="0.10"),
}

W, H = 1200, 290


def hero(mode):
    t = THEMES[mode]
    chips, x = [], 64
    for label, color in CHIPS:
        w = 26 + len(label) * 7.6
        chips.append(
            f'<g><rect x="{x:.0f}" y="206" width="{w:.0f}" height="34" rx="17" fill="{t["chip_bg"]}" '
            f'fill-opacity="{t["chip_op"]}" stroke="{color}" stroke-opacity="0.45"/>'
            f'<circle cx="{x + 15:.0f}" cy="223" r="3.6" fill="{color}"/>'
            f'<text x="{x + 26:.0f}" y="228" fill="{t["role"]}" font-size="13.5" '
            f'font-weight="600">{label}</text></g>')
        x += w + 10

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Angga Pratama, Senior Mobile Engineer, Android, React Native, Flutter">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{t['bg1']}"/><stop offset="58%" stop-color="{t['bg2']}"/><stop offset="100%" stop-color="{t['bg3']}"/>
  </linearGradient>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#3DDC84"/><stop offset="38%" stop-color="#61DAFB"/>
    <stop offset="72%" stop-color="#7F52FF"/><stop offset="100%" stop-color="#F5A623"/>
  </linearGradient>
  <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
    <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.55"/>
    <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
  </linearGradient>
  <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse">
    <path d="M36 0H0V36" fill="none" stroke="{t['grid']}" stroke-opacity="{t['grid_op']}" stroke-width="1"/>
  </pattern>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="16"/></clipPath>
  <style>
    .sweep {{ animation: slide 7s ease-in-out infinite; }}
    .halo  {{ animation: breathe 9s ease-in-out infinite; transform-origin: 1010px 120px; }}
    .blip  {{ animation: blink 2.6s ease-in-out infinite; }}
    @keyframes slide   {{ 0% {{ transform: translateX(-420px); }} 55%,100% {{ transform: translateX({W}px); }} }}
    @keyframes breathe {{ 0%,100% {{ opacity: .55; }} 50% {{ opacity: 1; }} }}
    @keyframes blink   {{ 0%,100% {{ opacity: .25; }} 50% {{ opacity: .9; }} }}
    @media (prefers-reduced-motion: reduce) {{ .sweep, .halo, .blip {{ animation: none; }} }}
  </style>
</defs>

<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <g class="halo">
    <circle cx="1010" cy="120" r="210" fill="#61DAFB" fill-opacity="{t['halo_op']}"/>
    <circle cx="1140" cy="250" r="150" fill="#3DDC84" fill-opacity="{t['halo_op']}"/>
  </g>

  <g font-family="{FONT}">
    <text x="64" y="68" fill="#3DDC84" font-size="13" font-weight="700" letter-spacing="3.4">SENIOR MOBILE ENGINEER</text>
    <text x="64" y="128" fill="{t['name']}" font-size="56" font-weight="800" letter-spacing="-1.4">Angga Pratama</text>
    <text x="64" y="162" fill="{t['role']}" font-size="20" font-weight="500">Android, React Native, Flutter. Payments, devices, and the release pipeline behind them.</text>
    <text x="64" y="188" fill="{t['sub']}" font-size="15">Mobile software that runs in production without daily support. Bogor, Indonesia (UTC+7).</text>
    {''.join(chips)}
  </g>

  <g opacity="0.95">
    <rect x="936" y="52" width="112" height="190" rx="18" fill="{t['device']}" stroke="#61DAFB" stroke-opacity="{t['device_stroke_op']}" stroke-width="2"/>
    <rect x="950" y="72" width="84" height="132" rx="7" fill="#61DAFB" fill-opacity="0.10"/>
    <rect x="960" y="86" width="64" height="7" rx="3.5" fill="#3DDC84" fill-opacity="0.8"/>
    <rect x="960" y="102" width="44" height="7" rx="3.5" fill="#61DAFB" fill-opacity="0.65"/>
    <rect x="960" y="118" width="56" height="7" rx="3.5" fill="#7F52FF" fill-opacity="0.65"/>
    <rect x="960" y="134" width="34" height="7" rx="3.5" fill="#61DAFB" fill-opacity="0.4"/>
    <rect x="960" y="150" width="60" height="7" rx="3.5" fill="#3DDC84" fill-opacity="0.4"/>
    <rect x="960" y="166" width="46" height="7" rx="3.5" fill="#F5A623" fill-opacity="0.45"/>
    <circle class="blip" cx="992" cy="222" r="7" fill="#61DAFB"/>

    <rect x="1072" y="92" width="80" height="128" rx="14" fill="{t['device']}" stroke="#3DDC84" stroke-opacity="{t['device_stroke_op']}" stroke-width="2"/>
    <rect x="1086" y="110" width="52" height="36" rx="6" fill="#3DDC84" fill-opacity="0.16"/>
    <rect x="1086" y="156" width="52" height="7" rx="3.5" fill="{t['name']}" fill-opacity="0.16"/>
    <rect x="1086" y="170" width="36" height="7" rx="3.5" fill="{t['name']}" fill-opacity="0.12"/>
    <rect x="1086" y="184" width="44" height="7" rx="3.5" fill="{t['name']}" fill-opacity="0.12"/>
  </g>

  <rect x="0" y="{H-7}" width="{W}" height="7" fill="url(#accent)"/>
  <rect class="sweep" x="0" y="{H-7}" width="420" height="7" fill="url(#sweep)"/>
</g>
</svg>'''


for mode in ("dark", "light"):
    open(f"assets/hero-{mode}.svg", "w").write(hero(mode))
    print("assets/hero-%s.svg" % mode)
