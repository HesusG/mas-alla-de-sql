"""
Genera imagenes decorativas para slides text-heavy del workshop "Mas alla de SQL".
Estilo: Pixel art con fondo blanco, retro Mac OS 7 / terminal aesthetic.
Usa Gemini 3 Pro Image.

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

# Pixel art style on WHITE background — blends with slide bg
PIXEL_SUFFIX = (
    " STYLE: Clean pixel art illustration on a PURE WHITE (#FFFFFF) background. "
    "16-bit / 32-bit pixel art aesthetic with visible pixel edges and limited color palette. "
    "Use only these accent colors: teal (#2DD4BF), coral (#FF6B6B), purple (#6C5CE7), "
    "black (#000000), and gray (#C0C0C0). NO gradients, NO photorealism — flat pixel art only. "
    "The subject should float on the white background with NO border, NO frame, NO shadow. "
    "Think retro Mac OS 7 icon art or classic pixel game sprites scaled up. "
    "Crisp, sharp pixel edges. NO text, NO watermarks. High resolution."
)

PROMPTS = {
    "slide_04_reto": (
        "A pixel art retro CRT monitor showing a red X error icon on its screen. "
        "A small keyboard in front of it. A coffee mug next to it. "
        "Two small paper documents with red question marks scattered nearby. "
        "Simple, iconic, minimal objects floating on white background."
    ),
    "slide_12_normalizar": (
        "Pixel art illustration of a data pipeline: on the left, a messy pile of colorful "
        "document icons (CSV files, spreadsheets, emails) in disarray. An arrow points right "
        "to a set of gears/cogs processing the data. Another arrow points to neat, organized "
        "database table icons on the right, perfectly stacked. The gears are teal colored. "
        "Simple flat pixel art on white background."
    ),
    "slide_13_codd": (
        "Pixel art portrait of a middle-aged man in a suit and tie from the 1970s era, "
        "resembling a classic computer scientist. He has short hair, glasses, and a friendly "
        "expression. The portrait is in a pixel art style like a retro video game character "
        "portrait — 32-bit quality with visible pixels. Muted professional colors. "
        "Floating on pure white background, no frame."
    ),
    "slide_16_costo": (
        "Pixel art split illustration: on the left, a small magnifying glass finding only "
        "3 tiny dots (few results). On the right, a large radar/sonar circle with many "
        "bright teal and coral dots scattered across it (many missed results). "
        "A dashed line divides the two halves. Simple flat pixel art on white background."
    ),
    "slide_42_semantica": (
        "Pixel art of two side-by-side browser windows. Left window has a simple search bar "
        "with a few scattered gray dots below (keyword search). Right window has a glowing "
        "network of interconnected nodes in purple and teal (semantic search), with lines "
        "connecting related concepts. The right side is vibrant, the left side is dull. "
        "Flat pixel art on white background."
    ),
    "slide_44_peliculas": (
        "Pixel art bird's-eye view of index cards being sorted into four colored groups on "
        "a surface: teal group, coral group, purple group, and gray group. Each card is a "
        "tiny rectangle with a small icon. Dotted lines connect cards within groups. "
        "A pixel art hand or cursor is moving one card. "
        "Flat pixel art on white background."
    ),
    "slide_46_rey_reina": (
        "Pixel art chess pieces on a coordinate grid: a king piece, a queen piece, a pawn, "
        "and a knight. Teal vector arrows connect them showing mathematical relationships. "
        "Plus, minus, and equals signs float between pieces in pixel font. "
        "The grid is subtle gray lines. Flat pixel art on white background."
    ),
}


def generate_image(name: str, prompt: str) -> Path:
    """Genera una imagen con Gemini 3 Pro Image."""
    full_prompt = prompt + PIXEL_SUFFIX
    print(f"  Generando: {name}...")

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(
                    aspect_ratio="1:1",
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
            if pil_img.mode == "P":
                pil_img = pil_img.convert("RGBA")
            pil_img.save(str(out_path), format="PNG", optimize=True)
            print(f"  OK: {out_path}")
            return out_path

    print(f"  ERROR: {name} -- Respuesta sin imagen")
    return None


def main():
    print("=" * 60)
    print("Generador de imagenes pixel art -- Mas alla de SQL")
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
