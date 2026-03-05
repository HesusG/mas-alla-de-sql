import { defineConfig } from 'unocss'

export default defineConfig({
  shortcuts: {
    'neo-border': 'border-3 border-black',
    'neo-shadow': 'shadow-[4px_4px_0px_#000]',
    'neo-shadow-sm': 'shadow-[2px_2px_0px_#000]',
    'neo-card': 'border-3 border-black shadow-[4px_4px_0px_#000] rounded-sm p-6',
    'neo-btn': 'border-3 border-black shadow-[4px_4px_0px_#000] rounded-sm px-4 py-2 font-bold hover:shadow-[2px_2px_0px_#000] hover:translate-x-[2px] hover:translate-y-[2px] transition-all',
    'neo-tag': 'border-2 border-black rounded-sm px-2 py-1 text-sm font-bold',
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
