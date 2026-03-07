<script setup>
defineProps({
  headers: { type: Array, required: true },
  rows: { type: Array, required: true },
})
</script>

<template>
  <div class="mac-window">
    <div class="mac-titlebar">
      <div class="mac-close-box" />
    </div>
    <div class="mac-window-content !p-0">
      <table class="w-full text-sm mac-table">
        <thead>
          <tr>
            <th v-for="h in headers" :key="h" class="px-4 py-3">
              {{ h }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, i) in rows" :key="i">
            <td v-for="(cell, j) in row" :key="j" class="px-4 py-2">
              {{ cell }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
