<template>
  <div class="slidev-layout neo-section h-full flex flex-col items-center justify-center bg-[#A0A0A0] relative overflow-hidden">
    <!-- CRT Monitor Frame -->
    <div class="crt-bezel w-[85%] max-w-4xl">
      <div class="crt-screen px-8 py-10 text-center relative">
        <div class="crt-scanlines" />
        <div class="relative z-10">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>
