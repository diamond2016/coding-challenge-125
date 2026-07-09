<template>
  <div class="text-area-container">
    <div class="text-area-header">
      <span class="text-area-label">{{ label }}</span>
    </div>
    <textarea
      class="text-area"
      v-model="text"
      :placeholder="placeholder"
    ></textarea>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';

const props = withDefaults(defineProps<{
  modelValue?: string;
  label?: string;
  placeholder?: string;
}>(), {
  modelValue: '',
  label: 'Text',
  placeholder: 'Enter or paste text here...',
});

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void;
}>();

const text = ref(props.modelValue || '');

watch(text, (newValue) => {
  emit('update:modelValue', newValue);
});

// Sync with external changes
watch(
  () => props.modelValue,
  (newValue) => {
    if (newValue !== text.value) {
      text.value = newValue;
    }
  }
);
</script>

<style scoped>
.text-area-container {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 0;
  border-radius: 12px;
  overflow: hidden;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1), 0 2px 6px rgba(0, 0, 0, 0.06);
  transition: box-shadow 0.3s ease, transform 0.2s ease;
}

.text-area-container:hover {
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15), 0 3px 8px rgba(0, 0, 0, 0.08);
}

.text-area-container:focus-within {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(44, 62, 80, 0.15), 0 4px 10px rgba(0, 0, 0, 0.1);
}

.text-area-header {
  padding: 14px 18px;
  background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
  border-bottom: 3px solid #3498db;
  display: flex;
  align-items: center;
  gap: 10px;
}

.text-area-label {
  font-weight: 600;
  color: #ecf0f1;
  font-size: 15px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.text-area-label::before {
  content: '';
  display: inline-block;
  width: 8px;
  height: 8px;
  background-color: #3498db;
  border-radius: 50%;
  margin-right: 8px;
}

.text-area {
  flex: 1;
  width: 100%;
  padding: 18px 20px;
  border: none;
  resize: none;
  font-family: 'Fira Code', 'Courier New', 'Consolas', monospace;
  font-size: 15px;
  line-height: 1.6;
  outline: none;
  background-color: transparent;
  color: #2c3e50;
  transition: background-color 0.2s ease;
}

.text-area:focus {
  background-color: #fafafa;
}

.text-area::placeholder {
  color: #bdc3c7;
  font-style: italic;
}

.text-area:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Scrollbar styling */
.text-area::-webkit-scrollbar {
  width: 8px;
}

.text-area::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.text-area::-webkit-scrollbar-thumb {
  background: #3498db;
  border-radius: 4px;
}

.text-area::-webkit-scrollbar-thumb:hover {
  background: #2980b9;
}

/* Selection styling */
.text-area ::selection {
  background-color: #3498db;
  color: #ffffff;
}
</style>