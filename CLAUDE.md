# Mas alla de SQL - Workshop Repository

## Overview
A 2-hour workshop for ITESM Business Intelligence students covering Elasticsearch and ChromaDB as tools beyond SQL. Neobrutalist design with Slidev.

## Commands
- `npm run dev` - Start Slidev dev server (localhost:3030)
- `npm run build` - Build static site
- `npm run export` - Export PDF
- `cd demo && pip install -r requirements.txt && python career_coach_rag.py` - Run RAG demo

## Tech Stack
- **Slides**: Slidev + UnoCSS + Vue 3
- **Design**: Neobrutalist (thick borders, offset shadows, flat colors)
- **Demo**: Python + ChromaDB + together.ai + Gradio
- **Icons**: pixelarticons via @iconify-json/pixelarticons

## Design System

### Neobrutalist Rules
1. **Borders**: `border-3 border-black` (3px solid black)
2. **Shadows**: Offset only: `shadow-[4px_4px_0px_#000]`
3. **Colors**: Flat fills, NO gradients
4. **Border-radius**: `rounded-none` or `rounded-sm` (max 4px)
5. **Typography**: Space Grotesk bold headings, Inter body, JetBrains Mono code
6. **Hover**: `hover:shadow-[2px_2px_0px_#000] hover:translate-x-[2px]`
7. **Backgrounds**: Solid color blocks, subtle dot-grid patterns

### Color Palette
| Name   | Hex       | Usage                      |
|--------|-----------|----------------------------|
| Banana | `#FFE156` | Primary accent, highlights |
| Coral  | `#FF6B6B` | Warnings, Elasticsearch    |
| Sky    | `#4ECDC4` | Links, ChromaDB            |
| Grape  | `#6C5CE7` | Code blocks, emphasis      |
| Ink    | `#2D3436` | Text, borders              |
| Paper  | `#FAFAFA` | Backgrounds                |
| Cream  | `#FFF8E7` | Alt backgrounds            |

### Code Theme
Dracula

## Slide Conventions
- **Layouts**: neo-cover, neo-section, neo-two-cols, neo-demo
- **Components**: NeoCard, PixelDivider, TimerBadge, ComparisonTable, RefFootnote
- **Snippets**: Load via `<<< @/snippets/filename.ext`
- **References**: Use `<RefFootnote>` for APA 7 inline citations

## Content Language
- Slides: Spanish
- Code: English
- Tech terms: Keep English form (Elasticsearch, ChromaDB, etc.)

## APA 7 Rules
- Every slide with a claim needs a `<RefFootnote>` citation
- Per-section reference slides (slides 28, 42, 49)
- Complete list in `references/apa7.md`
- Authoritative sources only (official docs, peer-reviewed papers, industry reports)

## Quality Checklist
- [ ] Fonts: Space Grotesk headings, Inter body, JetBrains Mono code
- [ ] Icons: pixelarticons render via `<div i-pixelarticons-search />`
- [ ] Code theme: Dracula
- [ ] Timing: ~120 minutes total
- [ ] References: APA 7 on every claim slide
- [ ] SQL-to-ES comparison on every ES concept slide
