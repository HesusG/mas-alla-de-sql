<template>
  <div class="slidev-layout neo-demo h-full flex flex-col bg-[#2D3436] text-white relative overflow-hidden">
    <div class="relative z-10 flex-1 flex flex-col px-10 py-6">
      <div class="mb-4">
        <slot name="title" />
      </div>
      <div class="flex-1 overflow-auto">
        <slot />
      </div>
    </div>
    <div class="absolute top-4 right-6 bg-coral text-white text-xs font-bold px-3 py-1 border-2 border-white rounded-sm">
      LIVE DEMO
    </div>
  </div>
</template>
