<script setup>
defineProps({
  headers: { type: Array, required: true },
  rows: { type: Array, required: true },
})
</script>

<template>
  <div class="border-2 border-black overflow-hidden shadow-[2px_2px_0px_#000]">
    <table class="w-full text-sm">
      <thead>
        <tr style="background: repeating-linear-gradient(0deg, #C0C0C0 0px, #C0C0C0 2px, #FFF 2px, #FFF 4px);">
          <th v-for="h in headers" :key="h" class="px-4 py-3 text-left font-bold border-r border-black last:border-r-0">
            {{ h }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, i) in rows" :key="i" :class="i % 2 === 0 ? 'bg-white' : 'bg-[#F0F0F0]'">
          <td v-for="(cell, j) in row" :key="j" class="px-4 py-2 border-r border-t border-black/20 last:border-r-0" style="border-color: #FFF #808080 #808080 #FFF; border-width: 1px;">
            {{ cell }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
