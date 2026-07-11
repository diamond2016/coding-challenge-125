<template>
  <div class="task-manager-layout">
    <AppHeader />
    <div class="main-content-area">
      <div class="left-column">
        <Text1View />
        <Text2View />
      </div>
      <div class="right-column">
        <DiffView v-model="diffValue" @update:modelValue="handleDiffUpdate" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import AppHeader from '@/components/AppHeader.vue';
  import Text1View from '@/components/TextView.vue';
  import Text2View from '@/components/TextView.vue';
  import DiffView from '@/components/DiffView.vue';

  // Reactive state to hold the diff result
  const diffValue = ref<string | null>(null);

  // Helper function to handle update:modelValue event from DiffView
  const handleDiffUpdate = (value: string | null) => {
    console.log('=== DiffManager: Received update:modelValue event ===');
    console.log('Event type: update:modelValue');
    console.log('Received value:', value);
    console.log('Value type:', typeof value);
    console.log('Value is null:', value === null);

    if (value !== null) {
      console.log('Value length:', value.length);
      console.log('First 100 chars:', value.substring(0, 100));

      // Check for ANSI color codes
      const hasRed = value.includes('\\033[31m');
      const hasGreen = value.includes('\\033[32m');
      const hasCyan = value.includes('\\033[36m');
      const hasWhite = value.includes('\\033[37m');

      console.log('ANSI color codes detected:');
      console.log('  - Red (deleted):', hasRed);
      console.log('  - Green (inserted):', hasGreen);
      console.log('  - Cyan (equal):', hasCyan);
      console.log('  - White (equal):', hasWhite);
    }

    // Update the reactive state
    diffValue.value = value;
    console.log('=== DiffManager: State updated ===');
  };
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