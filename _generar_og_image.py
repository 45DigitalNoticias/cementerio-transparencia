"""
Genera la tarjeta Open Graph (1200x630 PNG) del Cementerio de la Transparencia.
Salida: CEMENTERIO_MORELOS/og-image.png

Estética coherente con index.html:
  - Fondo nocturno #0c0c0e
  - Cempasúchil (#f5a623) y oro (#c9a449) como acentos
  - Tipografía Cormorant Garamond (serif Georgia como sustituto en Windows)
  - Tres KPIs sincronizados con la auditoría: 29 sitios · 11 funcionan · 18 fallan

Uso: python _generar_og_image.py
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

PROJ = Path(__file__).parent
OUT = PROJ / "og-image.png"

# ---- Paleta Día de Muertos (matches CSS root variables del index.html) ----
BG               = (12, 12, 14)        # --bg #0c0c0e
BG_CARD          = (22, 22, 26)        # --bg-card #16161a
INK              = (232, 227, 214)     # --ink #e8e3d6
INK_DIM          = (154, 147, 132)     # --ink-dim #9a9384
RULE             = (42, 42, 50)        # --rule #2a2a32
GOLD             = (201, 164, 73)      # --gold #c9a449
CEMPASUCHIL      = (245, 166, 35)      # --cempasuchil #f5a623
CEMPASUCHIL_CLR  = (255, 200, 87)      # --cempasuchil-claro #ffc857
SANGRE           = (160, 24, 24)       # --sangre #a01818
FUNCIONA         = (102, 187, 106)     # --funciona #66bb6a
SEPIA            = (184, 153, 104)     # --sepia
CALAVERA         = (245, 230, 211)     # --calavera

# ---- Tipografías ----
F_REG    = "C:/Windows/Fonts/georgia.ttf"
F_BOLD   = "C:/Windows/Fonts/georgiab.ttf"
F_ITALIC = "C:/Windows/Fonts/georgiai.ttf"
F_MONO   = "C:/Windows/Fonts/consola.ttf"
F_MONO_B = "C:/Windows/Fonts/consolab.ttf"

W, H = 1200, 630


def draw_cempasuchil(draw, cx, cy, r):
    """Dibuja una flor de cempasúchil estilizada (capas concéntricas)."""
    # Pétalos exteriores (8 pétalos)
    for i in range(8):
        angle = i * math.pi / 4
        px = cx + math.cos(angle) * r * 0.85
        py = cy + math.sin(angle) * r * 0.85
        draw.ellipse([px - r * 0.4, py - r * 0.4, px + r * 0.4, py + r * 0.4],
                     fill=CEMPASUCHIL)
    # Pétalos medianos (6)
    for i in range(6):
        angle = i * math.pi / 3 + math.pi / 12
        px = cx + math.cos(angle) * r * 0.5
        py = cy + math.sin(angle) * r * 0.5
        draw.ellipse([px - r * 0.32, py - r * 0.32, px + r * 0.32, py + r * 0.32],
                     fill=(255, 140, 0))
    # Centro claro
    draw.ellipse([cx - r * 0.45, cy - r * 0.45, cx + r * 0.45, cy + r * 0.45],
                 fill=CEMPASUCHIL_CLR)
    # Núcleo
    draw.ellipse([cx - r * 0.2, cy - r * 0.2, cx + r * 0.2, cy + r * 0.2],
                 fill=(160, 90, 10))


def draw_papel_picado(draw, y, color):
    """Banda decorativa estilo papel picado en la parte superior."""
    # Barra superior maciza
    draw.rectangle([0, y, W, y + 6], fill=color)
    # Triángulos colgantes
    triangle_w = 36
    for x in range(0, W, triangle_w):
        draw.polygon([
            (x, y + 6),
            (x + triangle_w // 2, y + 28),
            (x + triangle_w, y + 6)
        ], fill=color)
        # Punto al centro de cada triángulo
        draw.ellipse([
            x + triangle_w // 2 - 2, y + 14,
            x + triangle_w // 2 + 2, y + 18
        ], fill=BG)


def draw_kpi_card(draw, x, y, w, h, numero, label, accent_color):
    """Tarjeta KPI estilo marcador-expediente."""
    # Fondo card semi-transparente (simulado con color sólido cercano)
    draw.rectangle([x, y, x + w, y + h], fill=(8, 8, 10))
    # Borde
    draw.rectangle([x, y, x + w, y + h], outline=RULE, width=1)
    # Acento lateral izquierdo
    draw.rectangle([x, y, x + 4, y + h], fill=accent_color)

    # Número grande
    f_num = ImageFont.truetype(F_BOLD, 70)
    bbox = draw.textbbox((0, 0), numero, font=f_num)
    nw = bbox[2] - bbox[0]
    draw.text((x + (w - nw) // 2, y + 14), numero, font=f_num, fill=accent_color)

    # Label monoespaciada
    f_label = ImageFont.truetype(F_MONO_B, 14)
    bbox = draw.textbbox((0, 0), label, font=f_label)
    lw = bbox[2] - bbox[0]
    draw.text((x + (w - lw) // 2, y + h - 28), label, font=f_label, fill=INK_DIM)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # ---- Halo cempasúchil suave en esquina superior izquierda ----
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for r in range(300, 80, -20):
        alpha = int(8 * (1 - (r - 80) / 220))
        odraw.ellipse([-r + 100, -r + 50, r + 100, r + 50],
                      fill=(245, 166, 35, max(alpha, 0)))
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"))

    # ---- Papel picado decorativo arriba ----
    draw = ImageDraw.Draw(img)
    draw_papel_picado(draw, 0, CEMPASUCHIL)

    # ---- Lápida estilizada en esquina superior derecha ----
    lap_x, lap_y, lap_w, lap_h = W - 165, 60, 95, 120
    # Cuerpo de la lápida con arco superior
    draw.rounded_rectangle([lap_x, lap_y + 30, lap_x + lap_w, lap_y + lap_h],
                           radius=4, fill=BG_CARD, outline=GOLD, width=2)
    draw.pieslice([lap_x, lap_y, lap_x + lap_w, lap_y + 90],
                  start=180, end=360, fill=BG_CARD, outline=GOLD, width=2)
    # Cruz grabada (dibujada con rectángulos, no glifo unicode)
    cx = lap_x + lap_w // 2
    cy = lap_y + 50
    draw.rectangle([cx - 3, cy - 14, cx + 3, cy + 22], fill=GOLD)
    draw.rectangle([cx - 13, cy - 4, cx + 13, cy + 2], fill=GOLD)
    # Inscripción RIP debajo
    f_rip = ImageFont.truetype(F_BOLD, 14)
    bbox = draw.textbbox((0, 0), "R.I.P.", font=f_rip)
    rw = bbox[2] - bbox[0]
    draw.text((lap_x + (lap_w - rw) // 2, lap_y + 85),
              "R.I.P.", font=f_rip, fill=SEPIA)

    # ---- Eyebrow ----
    f_eyebrow = ImageFont.truetype(F_MONO_B, 18)
    eyebrow = "45 DIGITAL NOTICIAS  ·  EXPEDIENTE OPACIDAD MORELOS"
    draw.text((70, 80), eyebrow, font=f_eyebrow, fill=CEMPASUCHIL)

    # Línea fina bajo eyebrow
    draw.rectangle([70, 112, 320, 113], fill=CEMPASUCHIL)

    # ---- Título principal ----
    f_title = ImageFont.truetype(F_BOLD, 74)
    draw.text((70, 138), "El Cementerio de la", font=f_title, fill=INK)
    draw.text((70, 220), "Transparencia", font=f_title, fill=CEMPASUCHIL_CLR)

    # ---- Subtítulo ----
    f_sub = ImageFont.truetype(F_ITALIC, 24)
    subtitulo = "Auditoría visual de los sitios oficiales del gobierno de Morelos."
    draw.text((70, 318), subtitulo, font=f_sub, fill=INK_DIM)

    # ---- KPIs (tres tarjetas) ----
    kpi_y = 388
    kpi_h = 130
    gap = 18
    available_w = W - 140  # margen 70 a cada lado
    kpi_w = (available_w - gap * 2) // 3

    draw_kpi_card(draw, 70 + (kpi_w + gap) * 0, kpi_y, kpi_w, kpi_h,
                  "29", "SITIOS REVISADOS", INK)
    draw_kpi_card(draw, 70 + (kpi_w + gap) * 1, kpi_y, kpi_w, kpi_h,
                  "11", "FUNCIONAN  ·  38%", FUNCIONA)
    draw_kpi_card(draw, 70 + (kpi_w + gap) * 2, kpi_y, kpi_w, kpi_h,
                  "18", "CAIDOS O VACIOS  ·  62%", SANGRE)

    # ---- Cempasúchil decorativo (abajo a la izquierda) ----
    draw_cempasuchil(draw, 110, H - 70, 38)
    draw_cempasuchil(draw, 175, H - 55, 26)

    # ---- Footer ----
    f_foot = ImageFont.truetype(F_MONO_B, 15)
    footer = "VERIFICACION TECNICA  ·  19 DE MAYO DE 2026"
    draw.text((240, H - 78), footer, font=f_foot, fill=INK_DIM)

    f_url = ImageFont.truetype(F_ITALIC, 18)
    url = "45digitalnoticias.github.io/cementerio-transparencia"
    bbox = draw.textbbox((0, 0), url, font=f_url)
    uw = bbox[2] - bbox[0]
    draw.text((W - uw - 70, H - 50), url, font=f_url, fill=GOLD)

    # Banda dorada al pie
    draw.rectangle([0, H - 8, W, H], fill=CEMPASUCHIL)
    draw.rectangle([0, H - 12, W, H - 8], fill=SANGRE)

    img.save(OUT, "PNG", optimize=True)
    print(f"OK -> {OUT}")


if __name__ == "__main__":
    main()