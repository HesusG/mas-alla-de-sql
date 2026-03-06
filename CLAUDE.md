# Mas alla de SQL - Workshop Repository

## Overview
A 2-hour workshop for ITESM Business Intelligence students covering Elasticsearch and ChromaDB as tools beyond SQL. Terminal pixel art design with Slidev.

## Commands
- `npm run dev` - Start Slidev dev server (localhost:3030)
- `npm run build` - Build static site
- `npm run export` - Export PDF
- `cd demo && pip install -r requirements.txt && python career_coach_rag.py` - Run RAG demo

## Tech Stack
- **Slides**: Slidev + UnoCSS + Vue 3
- **Design**: Terminal Pixel Art (white bg, 1px borders, green-on-black code, selective color)
- **Demo**: Python + ChromaDB + together.ai + Gradio
- **Icons**: pixelarticons via @iconify-json/pixelarticons

## Design System

### Terminal Pixel Art Rules
1. **Borders**: `border border-black` (1px solid black)
2. **Shadows**: None (clean, minimal)
3. **Colors**: White backgrounds, color only as selective highlight (bg-[#color]/10 or /20)
4. **Border-radius**: `rounded-sm` max
5. **Typography**: Space Grotesk bold headings, Inter body, JetBrains Mono code
6. **Code blocks**: Dark terminal bg (#0d1117), green text (#00ff41) for terminal feel
7. **Backgrounds**: Clean white, dark terminal (#0d1117) for section/demo slides
8. **Section slides**: bg-[#0d1117] with scanline effect, green mono text

### Color Palette (used sparingly as accents)
| Name      | Hex       | Usage                           |
|-----------|-----------|---------------------------------|
| Banana    | `#FFE156` | Highlights (bg-[#ffe156]/20)    |
| Coral     | `#FF6B6B` | Elasticsearch, warnings         |
| Sky       | `#4ECDC4` | ChromaDB, links                 |
| Grape     | `#6C5CE7` | Emphasis, vector DB             |
| Term BG   | `#0d1117` | Terminal/code backgrounds       |
| Term Text | `#00ff41` | Terminal green text             |
| White     | `#FFFFFF` | Default slide background        |

### Code Theme
Dracula (Shiki)

## Slide Conventions
- **Layouts**: neo-cover, neo-section, neo-two-cols, neo-demo (names kept for compat)
- **Components**: NeoCard, PixelDivider, TimerBadge, ComparisonTable, RefFootnote
- **Snippets**: Load via `<<< @/snippets/filename.ext`
- **References**: Use `<RefFootnote>` for APA 7 inline citations
- **Cards**: Use `border border-black bg-white p-4` (or via neo-card shortcut)
- **Colored accents**: Use `bg-[#color]/10` for subtle tints, not solid fills

## Content Language
- Slides: Spanish
- Code: English
- Tech terms: Keep English form (Elasticsearch, ChromaDB, etc.)

## APA 7 Rules
- Every slide with a claim needs a `<RefFootnote>` citation
- Per-section reference slides (slides 39, 52, 58)
- Complete list in `references/apa7.md`
- Authoritative sources only (official docs, peer-reviewed papers, industry reports)

## Quality Checklist
- [ ] Fonts: Space Grotesk headings, Inter body, JetBrains Mono code
- [ ] Icons: pixelarticons render via `<div i-pixelarticons-search />`
- [ ] Code theme: Dracula
- [ ] Timing: ~120 minutes total
- [ ] References: APA 7 on every claim slide
- [ ] SQL-to-ES comparison on every ES concept slide
- [ ] White backgrounds on content slides
- [ ] Dark terminal backgrounds on section/demo slides
