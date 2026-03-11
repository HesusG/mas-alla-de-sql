<script setup>
defineProps({
  question: { type: String, required: true },
  options: { type: Array, required: true },
})
</script>

<template>
  <div class="border-2 border-black max-w-2xl mx-auto bg-white shadow-[2px_2px_0px_#000]">
    <div class="mac-titlebar">
      <div class="mac-close-box" />
      <span class="mac-titlebar-title">Pop Quiz</span>
    </div>
    <div class="p-3">
      <p class="text-sm font-bold mb-2" style="font-family: 'Space Grotesk'">
        <span class="i-pixelarticons-alert inline-block w-4 h-4 text-[#2DD4BF] align-middle mr-1" />
        {{ question }}
      </p>
      <div class="grid grid-cols-2 gap-1.5">
        <div v-for="opt in options" :key="opt.letter"
          class="border border-black p-1.5 flex items-center gap-1.5 bg-[#C0C0C0]/20 text-xs">
          <span class="bg-[#C0C0C0] w-5 h-5 flex items-center justify-center font-bold text-xs flex-shrink-0 border border-black">
            {{ opt.letter }}
          </span>
          <span>{{ opt.text }}</span>
        </div>
      </div>
      <slot />
    </div>
  </div>
</template>
