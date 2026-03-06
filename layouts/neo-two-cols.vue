<template>
  <div class="slidev-layout neo-two-cols h-full flex flex-col bg-white relative overflow-hidden">
    <div class="flex-1 flex flex-col px-10 py-8">
      <div class="mb-6">
        <slot name="title" />
      </div>
      <div class="flex-1 grid grid-cols-2 gap-6">
        <div class="border-r border-black/10 pr-6">
          <slot name="left" />
        </div>
        <div class="pl-6">
          <slot name="right" />
        </div>
      </div>
    </div>
  </div>
</template>
