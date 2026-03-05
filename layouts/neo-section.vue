<template>
  <div class="slidev-layout neo-section h-full flex flex-col items-center justify-center text-center relative overflow-hidden" :class="$attrs.class || 'bg-grape'">
    <div class="neo-dotgrid" />
    <div class="relative z-10 max-w-3xl px-8">
      <slot />
    </div>
  </div>
</template>
