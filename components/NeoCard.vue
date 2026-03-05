<script setup>
defineProps({
  color: { type: String, default: 'white' },
})
</script>

<template>
  <div class="border-3 border-black shadow-[4px_4px_0px_#000] rounded-sm p-6" :class="`bg-${color}`">
    <slot />
  </div>
</template>
