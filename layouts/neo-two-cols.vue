<template>
  <div class="slidev-layout neo-two-cols h-full flex flex-col bg-paper relative overflow-hidden">
    <div class="neo-dotgrid" />
    <div class="relative z-10 flex-1 flex flex-col px-10 py-8">
      <div class="mb-6">
        <slot name="title" />
      </div>
      <div class="flex-1 grid grid-cols-2 gap-6">
        <div class="neo-card bg-white p-5">
          <slot name="left" />
        </div>
        <div class="neo-card bg-white p-5">
          <slot name="right" />
        </div>
      </div>
    </div>
  </div>
</template>
