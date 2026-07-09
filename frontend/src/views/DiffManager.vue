<template>
  <div class="task-manager-layout">
    <AppHeader />
    <div class="main-content-area">
      <Text1View />
      <Text2View />
      <DiffView />
      <DiffOpView />
    </div>
  </div>
</template>

<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue';
</script>

<style scoped>
.diff-manager-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Ensure it takes full viewport height */
}

.main-content-area {
  display: flex;
  flex: 1; /* Allows this area to take up remaining vertical space */
  padding: 20px;
  gap: 20px;
}

/* Placeholder styles for layout structure */

</style>
