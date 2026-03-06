<template>
  <div class="slidev-layout neo-demo h-full flex flex-col bg-[#0d1117] text-[#e6edf3] relative overflow-hidden">
    <div class="term-scanlines" />
    <div class="relative z-10 flex-1 flex flex-col px-10 py-6">
      <div class="mb-4">
        <slot name="title" />
      </div>
      <div class="flex-1 overflow-auto">
        <slot />
      </div>
    </div>
    <div class="absolute top-4 right-6 text-[#00ff41] text-xs font-mono font-bold px-3 py-1 border border-[#00ff41] rounded-sm">
      LIVE
    </div>
  </div>
</template>
