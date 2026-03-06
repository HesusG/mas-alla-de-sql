import { defineConfig } from 'unocss'

export default defineConfig({
  shortcuts: {
    // Terminal design system
    'neo-card': 'border border-black p-6 bg-white',
    'neo-border': 'border border-black',
    'neo-shadow': '',
    'neo-shadow-sm': '',
    'neo-tag': 'border border-black px-2 py-1 text-sm font-mono font-bold',
    'neo-btn': 'border border-black px-4 py-2 font-bold hover:bg-black hover:text-white transition-all',
    'term-card': 'border border-black p-6 bg-white',
    'term-code': 'bg-[#0d1117] text-[#00ff41] font-mono p-4 rounded-sm',
    'term-highlight': 'bg-[#ffe156]/30 px-1',
    'term-accent': 'text-[#ff6b6b] font-bold',
    'term-section-bg': 'bg-[#0d1117] text-white',
    // Color shortcuts (kept for backward compat in slides.md)
    'bg-banana': 'bg-[#FFE156]',
    'bg-coral': 'bg-[#FF6B6B]',
    'bg-sky': 'bg-[#4ECDC4]',
    'bg-grape': 'bg-[#6C5CE7]',
    'bg-ink': 'bg-[#2D3436]',
    'bg-paper': 'bg-[#FAFAFA]',
    'bg-cream': 'bg-[#FFF8E7]',
    'text-banana': 'text-[#FFE156]',
    'text-coral': 'text-[#FF6B6B]',
    'text-sky': 'text-[#4ECDC4]',
    'text-grape': 'text-[#6C5CE7]',
    'text-ink': 'text-[#2D3436]',
  },
  theme: {
    fontFamily: {
      heading: 'Space Grotesk, sans-serif',
      body: 'Inter, sans-serif',
      mono: 'JetBrains Mono, monospace',
    },
  },
})
