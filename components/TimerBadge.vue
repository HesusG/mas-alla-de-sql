<script setup>
defineProps({
  time: { type: String, required: true },
})
</script>

<template>
  <span class="inline-flex items-center gap-1 border-2 border-black bg-banana text-ink text-sm font-bold px-3 py-1 rounded-sm shadow-[2px_2px_0px_#000]">
    <div class="i-pixelarticons-clock inline-block w-4 h-4" />
    {{ time }}
  </span>
</template>
