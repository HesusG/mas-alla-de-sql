<template>
  <div class="slidev-layout neo-image h-full flex flex-col bg-[#C0C0C0] relative overflow-hidden">
    <div class="mac-menu-bar">
      <span>&#9632; File</span>
      <span>Edit</span>
      <span>View</span>
      <span>Special</span>
    </div>
    <!-- Mac Window with full-bleed image -->
    <div class="flex-1 flex flex-col mx-2 mb-1 mt-0">
      <div class="mac-window flex-1 flex flex-col">
        <div class="mac-titlebar">
          <div class="mac-close-box" />
          <span class="mac-titlebar-title">{{ $slidev.frontmatter.title || 'image.png' }}</span>
        </div>
        <div class="mac-window-content flex-1 relative p-0 overflow-hidden">
          <img
            :src="$slidev.frontmatter.image"
            class="w-full h-full object-cover"
          />
          <div class="absolute bottom-0 left-0 right-0 bg-black/70 px-6 py-4 text-white">
            <slot />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
