<script setup>
defineProps({
  headers: { type: Array, required: true },
  rows: { type: Array, required: true },
})
</script>

<template>
  <div class="border border-black overflow-hidden">
    <table class="w-full text-sm">
      <thead>
        <tr class="bg-[#0d1117] text-[#00ff41]">
          <th v-for="h in headers" :key="h" class="px-4 py-3 text-left font-mono font-bold border-r border-[#30363d] last:border-r-0">
            {{ h }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, i) in rows" :key="i" :class="i % 2 === 0 ? 'bg-white' : 'bg-gray-50'">
          <td v-for="(cell, j) in row" :key="j" class="px-4 py-2 border-r border-t border-gray-200 last:border-r-0">
            {{ cell }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
