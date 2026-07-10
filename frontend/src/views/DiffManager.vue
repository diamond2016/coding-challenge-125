<template>
  <div class="task-manager-layout">
    <AppHeader />
    <div class="main-content-area">
      <div class="left-column">
        <Text1View />
        <Text2View />
      </div>
      <div class="right-column">
        <DiffView />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import AppHeader from '@/components/AppHeader.vue';
  import Text1View from '@/components/TextView.vue';
  import Text2View from '@/components/TextView.vue';
  import DiffView from '@/components/TextView.vue';
</script>

<style scoped>
.task-manager-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content-area {
  display: flex;
  flex: 1;
  padding: 20px;
  gap: 20px;
  min-height: 0; /* Important for flex children to not overflow */
}

.left-column,
.right-column {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 0; /* Prevent overflow */
  gap: 20px;
}

/* Responsive design */
@media (max-width: 768px) {
  .main-content-area {
    flex-direction: column;
  }

  .left-column,
  .right-column {
    flex-direction: row;
    flex: none;
    width: 100%;
  }
}
</style>