<script setup>
defineProps({
  question: { type: String, required: true },
  options: { type: Array, required: true },
})
</script>

<template>
  <div class="mac-window max-w-2xl mx-auto">
    <div class="mac-titlebar">
      <div class="mac-close-box" />
      <span class="mac-titlebar-title">Pop Quiz</span>
    </div>
    <div class="mac-window-content !p-4">
      <div class="flex items-start gap-3 mb-3">
        <div class="i-pixelarticons-alert inline-block w-6 h-6 flex-shrink-0 text-[#2DD4BF]" />
        <p class="text-base font-bold" style="font-family: 'Space Grotesk'">{{ question }}</p>
      </div>
      <div class="space-y-2">
        <div v-for="opt in options" :key="opt.letter"
          class="border-2 border-black p-2 flex items-center gap-2 bg-white">
          <span class="mac-bevel-raised w-7 h-7 flex items-center justify-center bg-[#C0C0C0] font-bold text-xs flex-shrink-0">
            {{ opt.letter }}
          </span>
          <span class="text-sm">{{ opt.text }}</span>
        </div>
      </div>
      <slot />
    </div>
  </div>
</template>
