"""
Genera imagenes decorativas para slides del workshop "Mas alla de SQL".
Usa Imagen 4.0 para breathers (16:9) y Gemini 3 Pro para content slides (1:1).

Uso:
    python generate_slide_images.py                  # Genera todas
    python generate_slide_images.py slide_04_reto    # Genera una especifica
    python generate_slide_images.py --breathers      # Solo breathers (16:9)
    python generate_slide_images.py --content        # Solo content slides (1:1)
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

# ── Models ──────────────────────────────────────────────────
IMAGEN_MODEL = "imagen-4.0-generate-001"
GEMINI_MODEL = "gemini-3-pro-image-preview"

# ── Style suffixes ──────────────────────────────────────────

# For breather slides: dark background, 16:9, used inside neo-image layout
BREATHER_STYLE = (
    " STYLE: Clean pixel art illustration on a DARK background (#1a1a2e). "
    "16-bit / 32-bit pixel art aesthetic with visible pixel edges. "
    "Use accent colors: teal (#2DD4BF), coral (#FF6B6B), purple (#6C5CE7), "
    "platinum gray (#C0C0C0). Subtle grid pattern in background. "
    "Think retro Mac OS 7 aesthetic meets sci-fi. "
    "NO text, NO letters, NO watermarks, NO words. High resolution."
)

# For content slides: white background, 1:1, float inside slide content
PIXEL_SUFFIX = (
    " STYLE: Clean pixel art illustration on a PURE WHITE (#FFFFFF) background. "
    "16-bit / 32-bit pixel art aesthetic with visible pixel edges and limited color palette. "
    "Use only these accent colors: teal (#2DD4BF), coral (#FF6B6B), purple (#6C5CE7), "
    "black (#000000), and gray (#C0C0C0). NO gradients, NO photorealism — flat pixel art only. "
    "The subject should float on the white background with NO border, NO frame, NO shadow. "
    "Think retro Mac OS 7 icon art or classic pixel game sprites scaled up. "
    "Crisp, sharp pixel edges. NO text, NO watermarks. High resolution."
)

# ── Breather slide prompts (16:9, dark bg, used in neo-image layout) ──

BREATHER_PROMPTS = {
    "slide_17b_breather": (
        "Pixel art scene: a character in a long black trench coat and dark sunglasses "
        "standing in a dark room. One hand holds a glowing teal pill, the other a glowing "
        "coral pill. Green falling code streams in background. Dramatic choice moment."
    ),
    "slide_23b_breather": (
        "Pixel art scene: two agents (man in suit, woman with red hair) shining flashlights "
        "into a dark office full of filing cabinets and scattered documents. A teal-glowing "
        "magnifying glass hovers over highlighted files. A purple UFO silhouette visible "
        "through the window. Mysterious moody atmosphere."
    ),
    "slide_31c_breather": (
        "Pixel art scene: a character in a red cap and overalls jumping upward to hit a "
        "glowing teal question-mark block. Coral mushroom power-ups and purple star items "
        "float around. Brick platforms, green pipes, gold coins. Classic platformer game "
        "level with celebration energy."
    ),
    "slide_36b_breather": (
        "Pixel art scene: a large robot mid-transformation — the left half is a flat gray "
        "document/text page, the right half is a glowing teal-and-purple mechanical robot "
        "form. Purple energy sparks surround the transformation seam. Coral accents on "
        "robot joints. Text becoming something powerful."
    ),
    "slide_46b_breather": (
        "Pixel art scene: a spaceship bridge with a large viewport showing deep space. "
        "On the viewport, clusters of glowing dots — teal, coral, and purple groups "
        "connected by thin white lines, resembling a semantic embedding map. A pixel art "
        "captain in a uniform pointing at the star map. Final frontier exploration feel."
    ),
    "slide_50b_breather": (
        "Pixel art scene: a student in a white gi performing the iconic crane kick pose "
        "on a beach pier at sunset. A wise sensei in a dark robe watches nearby. Teal and "
        "coral sunset gradient sky. Purple ocean waves. The student glows with teal energy "
        "aura. Dramatic training-complete moment."
    ),
}

# ── Content slide prompts (1:1, white bg, used inline in slides) ──

CONTENT_PROMPTS = {
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
}


def generate_breather(name: str, prompt: str) -> Path:
    """Generate a 16:9 breather image using Imagen 4.0."""
    full_prompt = prompt + BREATHER_STYLE
    print(f"  [Imagen 4.0] Generating: {name}...")

    try:
        response = client.models.generate_images(
            model=IMAGEN_MODEL,
            prompt=full_prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
                output_mime_type="image/png",
            ),
        )
    except Exception as e:
        print(f"  ERROR in {name}: {e}")
        return None

    if response.generated_images:
        img = response.generated_images[0]
        out_path = OUTPUT_DIR / f"{name}.png"
        img.image.save(str(out_path))
        size_kb = out_path.stat().st_size // 1024
        print(f"  OK: {out_path} ({size_kb} KB)")

        # Also save as JPG for slide references
        from PIL import Image as PILImage
        pil_img = PILImage.open(str(out_path))
        jpg_path = out_path.with_suffix(".jpg")
        pil_img.convert("RGB").save(str(jpg_path), format="JPEG", quality=90)
        jpg_kb = jpg_path.stat().st_size // 1024
        print(f"  JPG: {jpg_path} ({jpg_kb} KB)")

        return out_path
    else:
        print(f"  WARNING: No image returned for {name}")
        return None


def generate_content(name: str, prompt: str) -> Path:
    """Generate a 1:1 content image using Gemini 3 Pro Image."""
    full_prompt = prompt + PIXEL_SUFFIX
    print(f"  [Gemini 3 Pro] Generating: {name}...")

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(
                    aspect_ratio="1:1",
                ),
            ),
        )
    except Exception as e:
        print(f"  ERROR in {name}: {e}")
        return None

    if not response.candidates or not response.candidates[0].content.parts:
        print(f"  FILTERED: {name} -- No image generated")
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
            size_kb = out_path.stat().st_size // 1024
            print(f"  OK: {out_path} ({size_kb} KB)")
            return out_path

    print(f"  ERROR: {name} -- Response had no image")
    return None


def main():
    print("=" * 60)
    print("Image Generator — Mas alla de SQL")
    print(f"Imagen 4.0 (breathers) + Gemini 3 Pro (content)")
    print("=" * 60)
    print(f"Output: {OUTPUT_DIR}\n")

    # Parse arguments
    args = sys.argv[1:]
    do_breathers = "--breathers" in args or not any(a.startswith("--") or a.startswith("slide_") for a in args)
    do_content = "--content" in args or not any(a.startswith("--") or a.startswith("slide_") for a in args)
    specific = [a for a in args if a.startswith("slide_")]

    results = {"ok": [], "error": []}

    # Generate breather images (16:9)
    if specific:
        breathers = {k: v for k, v in BREATHER_PROMPTS.items() if k in specific}
        contents = {k: v for k, v in CONTENT_PROMPTS.items() if k in specific}
    else:
        breathers = BREATHER_PROMPTS if do_breathers else {}
        contents = CONTENT_PROMPTS if do_content else {}

    if breathers:
        print(f"\n--- Breather images (16:9, Imagen 4.0) ---\n")
        for name, prompt in breathers.items():
            path = generate_breather(name, prompt)
            results["ok" if path else "error"].append(name)

    if contents:
        print(f"\n--- Content images (1:1, Gemini 3 Pro) ---\n")
        for name, prompt in contents.items():
            path = generate_content(name, prompt)
            results["ok" if path else "error"].append(name)

    total = len(breathers) + len(contents)
    print("\n" + "=" * 60)
    print(f"Generated: {len(results['ok'])}/{total}")
    if results["error"]:
        print(f"Errors: {results['error']}")
    print("=" * 60)

    if breathers and results["ok"]:
        print("\nREMINDER: Update slides.md image paths from .svg to .png:")
        print("  image: /images/slides/slide_XXX.svg  →  .png")


if __name__ == "__main__":
    main()
