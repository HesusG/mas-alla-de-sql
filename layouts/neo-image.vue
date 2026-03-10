<script setup>
const base = (import.meta.env.BASE_URL || '/').replace(/\/$/, '')
</script>

<template>
  <div class="slidev-layout neo-image h-full flex flex-col bg-[#C0C0C0] relative overflow-hidden">
    <MacMenuBar />
    <!-- Mac Window with full-bleed image -->
    <div class="flex-1 flex flex-col mx-2 mb-1 mt-0">
      <div class="mac-window flex-1 flex flex-col">
        <div class="mac-titlebar">
          <div class="mac-close-box" />
          <span class="mac-titlebar-title">{{ $slidev.frontmatter.title || 'image.png' }}</span>
        </div>
        <div
          class="flex-1 relative overflow-hidden"
          :style="{
            backgroundImage: `url(${base}${$slidev.frontmatter.image || ''})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }"
        >
          <div class="absolute bottom-0 left-0 right-0 bg-black/70 px-6 py-4 text-white">
            <slot />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
