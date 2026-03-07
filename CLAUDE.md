# Mas alla de SQL - Workshop Repository

## Overview
A 2-hour workshop for ITESM Business Intelligence students covering Elasticsearch and ChromaDB as tools beyond SQL. Retro Mac OS 7 modernized design with Slidev.

## Commands
- `npm run dev` - Start Slidev dev server (localhost:3030)
- `npm run build` - Build static site
- `npm run export` - Export PDF
- `cd demo && pip install -r requirements.txt && python career_coach_rag.py` - Run RAG demo

## Tech Stack
- **Slides**: Slidev + UnoCSS + Vue 3
- **Design**: Retro Mac OS 7 modernized (window chrome, bevels, CRT bezel, teal accent)
- **Demo**: Python + ChromaDB + together.ai + Gradio
- **Icons**: pixelarticons via @iconify-json/pixelarticons

## Design System

### Retro Mac OS 7 Rules
1. **Borders**: `border-2 border-black` (2px solid black)
2. **Shadows**: `shadow-[2px_2px_0px_#000]` (offset drop shadow)
3. **Windows**: Mac window chrome — striped title bar, close box, centered title
4. **Bevels**: Raised (`border-color: #FFF #000 #000 #FFF`) and sunken (inverse)
5. **Typography**: Space Grotesk bold headings, Inter body, JetBrains Mono code
6. **Code blocks**: Dracula bg (#282A36), configured via `setup/shiki.ts`
7. **Backgrounds**: White content, #C0C0C0 platinum desktop, #A0A0A0 CRT surround
8. **Section slides**: CRT bezel frame (thick #D4D0C8 border, rounded) with dark screen + scanlines
9. **Cover slide**: Platinum desktop with Mac menu bar + centered window
10. **Demo slides**: Terminal inside Mac window chrome with LIVE badge

### Color Palette
| Name      | Hex       | Usage                           |
|-----------|-----------|---------------------------------|
| Teal      | `#2DD4BF` | Primary accent, highlights      |
| Coral     | `#FF6B6B` | Elasticsearch, warnings         |
| Purple    | `#6C5CE7` | ChromaDB, vector DB             |
| Platinum  | `#C0C0C0` | Desktop bg, title bars          |
| Bezel     | `#D4D0C8` | CRT bezel frame                 |
| Dark      | `#282A36` | Code/terminal backgrounds (Dracula) |
| White     | `#FFFFFF` | Window content backgrounds      |

### Code Theme
Dracula (Shiki)

## Slide Conventions
- **Layouts**: neo-cover, neo-section, neo-two-cols, neo-demo (names kept for compat)
- **Components**: NeoCard (with `title` and `noChrome` props), PixelDivider, TimerBadge, ComparisonTable, RefFootnote
- **Snippets**: Load via `<<< @/snippets/filename.ext`
- **References**: Use `<RefFootnote>` for APA 7 inline citations
- **Cards**: Use `border-2 border-black bg-white shadow-[2px_2px_0px_#000]` (or via neo-card shortcut)
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
- [ ] Mac window chrome on cards and layouts
- [ ] CRT bezel on section slides
