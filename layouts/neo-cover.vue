<template>
  <div class="slidev-layout neo-cover h-full flex flex-col bg-[#C0C0C0] relative overflow-hidden">
    <!-- Decorative Mac Menu Bar -->
    <div class="mac-menu-bar">
      <span>&#9632; File</span>
      <span>Edit</span>
      <span>View</span>
      <span>Special</span>
    </div>
    <!-- Centered Mac Window -->
    <div class="flex-1 flex items-center justify-center p-8">
      <div class="mac-window max-w-3xl w-full">
        <div class="mac-titlebar">
          <div class="mac-close-box" />
          <span class="mac-titlebar-title">Mas alla de SQL</span>
        </div>
        <div class="mac-window-content text-center px-12 py-10">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>
