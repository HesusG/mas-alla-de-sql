<script setup>
defineProps({
  time: { type: String, required: true },
})
</script>

<template>
  <span class="inline-flex items-center gap-1 bg-[#C0C0C0] border-2 text-sm font-mono px-3 py-1 shadow-[1px_1px_0px_#000]" style="border-color: #FFF #000 #000 #FFF;">
    <div class="i-pixelarticons-clock inline-block w-4 h-4" />
    {{ time }}
  </span>
</template>
