"""
Genera imagenes decorativas para slides text-heavy del workshop "Mas alla de SQL".
Estilo: Retro Mac OS 7 / terminal hacker / CRT monitor aesthetic.
Usa Gemini 3 Pro Image para crear imagenes con aspecto retro.

Uso:
    python generate_slide_images.py                  # Genera todas
    python generate_slide_images.py slide_04_reto    # Genera una especifica
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key or api_key == "YOUR_API_KEY_HERE":
    print("ERROR: Configura tu API key en el archivo .env")
    print("  1. Ve a https://aistudio.google.com/apikey")
    print("  2. Copia tu clave")
    print("  3. Pegala en .env: GOOGLE_API_KEY=tu_clave_aqui")
    sys.exit(1)

client = genai.Client(api_key=api_key)

OUTPUT_DIR = Path(__file__).parent / "public" / "images" / "slides"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL = "gemini-3-pro-image-preview"

# Retro Mac OS 7 / terminal / CRT aesthetic suffix
RETRO_SUFFIX = (
    " The image MUST have a retro 1990s Macintosh / early computing aesthetic: "
    "CRT monitor glow, pixel-art inspired elements, monochrome or limited color palette "
    "(teal #2DD4BF, coral #FF6B6B, purple #6C5CE7 as accents on dark or platinum gray backgrounds), "
    "visible scanlines, bitmap-style icons, chunky window chrome borders, "
    "old-school terminal green-on-black text where applicable. "
    "Think classic Mac OS 7 System folder meets hacker terminal meets vaporwave. "
    "Clean composition, NO text or watermarks, suitable as a slide illustration. "
    "High resolution, sharp pixel edges, digital art style."
)

PROMPTS = {
    "slide_04_reto": (
        "A retro CRT monitor on a desk displaying a database search query with red 'NO RESULTS FOUND' "
        "blinking on screen. Around the monitor, scattered printed customer review papers with angry "
        "red marks and question marks. The scene conveys frustration with limited search capabilities. "
        "A coffee cup sits beside the keyboard. The monitor has classic Mac OS 7 window chrome. "
        "Moody teal ambient lighting from the screen illuminates the dark desk."
    ),
    "slide_12_normalizar": (
        "A top-down view of a retro Mac OS 7 desktop showing multiple overlapping database table "
        "windows connected by tangled colored lines (representing JOINs). Each window shows a tiny "
        "spreadsheet grid. The lines between them form an increasingly complex web, some lines are "
        "broken or showing error symbols. The desktop background is classic platinum gray with the "
        "old Mac OS diamond pattern. A 'System Error' dialog box floats in the corner."
    ),
    "slide_16_costo": (
        "A split-screen retro terminal display. Left side shows a green-on-black terminal with a "
        "SQL query running, outputting '23 results found' in dim text. Right side shows a glowing "
        "radar/sonar screen with many bright dots (representing missed results) pulsing in teal, "
        "with the number '124 MISSED' in coral red. The aesthetic is military-grade retro computing "
        "meets Mac OS 7 — chunky bezels, phosphor glow, scan lines visible."
    ),
    "slide_42_semantica": (
        "A retro computer screen showing two search bars side by side in Mac OS 7 style windows. "
        "The left window labeled 'WORDS' shows a simple text search with few gray dots scattered below. "
        "The right window labeled 'MEANING' shows a glowing neural network visualization with "
        "interconnected purple and teal nodes, bright connections pulsing between related concepts. "
        "The contrast between the dull keyword search and the vibrant semantic search is clear. "
        "CRT phosphor glow, scanlines, retro Mac window chrome."
    ),
    "slide_44_peliculas": (
        "A bird's-eye view of a retro wooden desk with movie cards/index cards scattered across it, "
        "being organized into clusters by invisible hands. Each card has a tiny pixel-art movie icon. "
        "Cards are grouped by color-coded zones: teal cluster (comedies), coral cluster (thrillers), "
        "purple cluster (sci-fi), gray cluster (dramas). Faint dotted lines connect similar cards. "
        "A classic Mac OS 7 Finder window floats above showing 'Organizing by: MEANING'. "
        "The scene has warm CRT amber lighting and visible pixel texture."
    ),
    "slide_46_rey_reina": (
        "Four pixel-art chess pieces on a retro grid/coordinate plane displayed on a CRT monitor. "
        "A king and queen piece on opposite sides, connected by glowing vector arrows in teal. "
        "Mathematical symbols (+, -, =) float between them in a retro bitmap font. "
        "The coordinate grid has a dark background with teal gridlines, resembling an old-school "
        "oscilloscope or vector graphics display. The chess pieces cast pixel shadows. "
        "Classic Mac OS 7 window frame surrounds the display."
    ),
}


def generate_image(name: str, prompt: str) -> Path:
    """Genera una imagen con Gemini 3 Pro Image."""
    full_prompt = prompt + RETRO_SUFFIX
    print(f"  Generando: {name}...")

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(
                    aspect_ratio="3:4",
                ),
            ),
        )
    except Exception as e:
        print(f"  ERROR en {name}: {e}")
        return None

    if not response.candidates or not response.candidates[0].content.parts:
        print(f"  FILTRADA: {name} -- No se genero imagen")
        return None

    for part in response.candidates[0].content.parts:
        if getattr(part, "thought", False):
            continue
        if part.inline_data is not None:
            out_path = OUTPUT_DIR / f"{name}.png"
            raw_bytes = part.inline_data.data
            from PIL import Image as PILImage
            import io
            pil_img = PILImage.open(io.BytesIO(raw_bytes))
            # Keep RGBA for transparency support
            if pil_img.mode == "P":
                pil_img = pil_img.convert("RGBA")
            pil_img.save(str(out_path), format="PNG", optimize=True)
            print(f"  OK: {out_path}")
            return out_path

    print(f"  ERROR: {name} -- Respuesta sin imagen")
    return None


def main():
    print("=" * 60)
    print("Generador de imagenes retro -- Mas alla de SQL")
    print(f"Modelo: {MODEL}")
    print("=" * 60)
    print(f"Salida: {OUTPUT_DIR}\n")

    if len(sys.argv) > 1:
        targets = sys.argv[1:]
        prompts = {k: v for k, v in PROMPTS.items() if k in targets}
        if not prompts:
            print(f"No se encontraron prompts para: {targets}")
            print(f"Disponibles: {list(PROMPTS.keys())}")
            sys.exit(1)
    else:
        prompts = PROMPTS

    results = {"ok": [], "error": []}

    for name, prompt in prompts.items():
        path = generate_image(name, prompt)
        if path:
            results["ok"].append(name)
        else:
            results["error"].append(name)

    print("\n" + "=" * 60)
    print(f"Generadas: {len(results['ok'])}/{len(prompts)}")
    if results["error"]:
        print(f"Errores: {results['error']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
