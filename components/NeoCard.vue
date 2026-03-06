<script setup>
defineProps({
  color: { type: String, default: 'white' },
})
</script>

<template>
  <div class="border border-black p-6" :class="`bg-${color}`">
    <slot />
  </div>
</template>
