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
    <div class="mac-window-content">
      <div class="flex items-start gap-4 mb-5">
        <div class="i-pixelarticons-alert inline-block w-8 h-8 flex-shrink-0 text-[#2DD4BF]" />
        <p class="text-lg font-bold" style="font-family: 'Space Grotesk'">{{ question }}</p>
      </div>
      <div class="space-y-3">
        <div v-for="opt in options" :key="opt.letter"
          class="border-2 border-black p-3 flex items-center gap-3 bg-white">
          <span class="mac-bevel-raised w-8 h-8 flex items-center justify-center bg-[#C0C0C0] font-bold text-sm flex-shrink-0">
            {{ opt.letter }}
          </span>
          <span class="text-sm">{{ opt.text }}</span>
        </div>
      </div>
      <slot />
    </div>
  </div>
</template>
