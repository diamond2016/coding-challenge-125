<template>
  <div class="task-manager-layout">
    <AppHeader />
    <div class="main-content-area">
      <div class="left-column">
        <Text1View
          v-model="text1Value"
          :label="text1Label"
        />
        <Text2View
          v-model="text2Value"
          :label="text2Label"
        />
      </div>
      <div class="right-column">
        <DiffView v-model="textDiffValue" :label=textDiffLabel @update:modelValue="handleDiffUpdate" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import AppHeader from '@/components/AppHeader.vue';
  import Text1View from '@/components/TextView.vue';
  import Text2View from '@/components/TextView.vue';
  import DiffView from '@/components/TextView.vue';

  // all for api dif-prettyp
  import { DefaultApi } from '@/api/client/api'
  import type { DiffPrettypRequest, DiffPrettypResponse } from '@/api/client';
  import { Configuration } from '@/api/client/configuration'
  const apiConfig = new Configuration({
  basePath: 'http://localhost:8000/api', // Base URL of the diff API
  });


  const postDiff = async () => {
  try {
    const request: DiffPrettypRequest = {"string_a": text1Value.value, "string_b": text2Value.value }
    const response: DiffPrettypResponse = await (new DefaultApi(apiConfig)).apiDiffPrettypPost(request)
    textDiffValue.value = response.diff
  } catch (error) {
    console.error('Error from post diff-prettyp:', error)
  }
}
  // Reactive state for text inputs
  const text1Value = ref<string>('');
  const text2Value = ref<string>('');

  // Labels for the text areas
  const text1Label = ref<string>('Original Text');
  const text2Label = ref<string>('Modified Text');

   // Reactive state to hold the diff result
  const textDiffLabel = ref<string>('Diff');
  const textDiffValue = ref<string>('');

  // Helper function to handle update:modelValue event from DiffView
  const handleDiffUpdate = (value: string) => {
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
    textDiffValue.value = value;
    console.log('=== DiffManager: State updated ===');
  };

  // Initialize text values and labels on mount
  onMounted(() => {
    console.log('=== DiffManager: Component mounted ===');

    // Set initial text values
    text1Value.value = 'Hello World!';
    text2Value.value = 'Hello Vue!';

    // Set initial labels
    text1Label.value = 'Original Text';
    text2Label.value = 'Modified Text';

    console.log('Initial text1Value:', text1Value.value);
    console.log('Initial text2Value:', text2Value.value);
    console.log('Initial text1Label:', text1Label.value);
    console.log('Initial text2Label:', text2Label.value);
  });
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