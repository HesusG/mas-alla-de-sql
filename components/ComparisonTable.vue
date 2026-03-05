<script setup>
defineProps({
  headers: { type: Array, required: true },
  rows: { type: Array, required: true },
})
</script>

<template>
  <div class="border-3 border-black rounded-sm overflow-hidden shadow-[4px_4px_0px_#000]">
    <table class="w-full text-sm">
      <thead>
        <tr class="bg-ink text-white">
          <th v-for="h in headers" :key="h" class="px-4 py-3 text-left font-bold border-r-2 border-black last:border-r-0">
            {{ h }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, i) in rows" :key="i" :class="i % 2 === 0 ? 'bg-white' : 'bg-cream'">
          <td v-for="(cell, j) in row" :key="j" class="px-4 py-2 border-r-2 border-t-2 border-black last:border-r-0">
            {{ cell }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
