<script setup>
defineProps({
  time: { type: String, required: true },
})
</script>

<template>
  <span class="inline-flex items-center gap-1 border border-current text-sm font-mono px-3 py-1">
    <div class="i-pixelarticons-clock inline-block w-4 h-4" />
    {{ time }}
  </span>
</template>
