<template>
  <div class="diff-container">
    <div class="diff-header">
      <span class="diff-label">{{ label }}</span>
    </div>
    <div class="diff-content" ref="diffContentRef">
      <pre class="diff-text">{{ modelValue }}</pre>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';

const props = withDefaults(defineProps<{
  modelValue?: string;
  label?: string;
}>(), {
  modelValue: '',
  label: 'Diff',
});

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void;
}>();

const diffContentRef = ref<HTMLElement | null>(null);

// Parse and apply ANSI color codes
const parseAndApplyColors = (text: string) => {
  if (!text) return '';
  
  let result = '';
  let i = 0;
  
  while (i < text.length) {
    const escapeSequence = text.substring(i);
    const ansiCodeMatch = escapeSequence.match(/^\\033\[(\d+)m/);
    
    if (ansiCodeMatch) {
      const code = parseInt(ansiCodeMatch[1], 10);
      result += `<span class="ansi-code ansi-${code}" data-code="${code}">${text[i + ansiCodeMatch[0].length]}</span>`;
      i += ansiCodeMatch[0].length;
    } else {
      result += text[i];
      i++;
    }
  }
  
  return result;
};

// Watch for modelValue changes and update display
watch(() => props.modelValue, (newValue) => {
  if (newValue !== null) {
    emit('update:modelValue', newValue);
  }
}, { deep: true });

// Apply color codes on mount and when content changes
onMounted(() => {
  if (diffContentRef.value && props.modelValue) {
    diffContentRef.value.innerHTML = parseAndApplyColors(props.modelValue);
  }
});

watch(() => props.modelValue, (newValue) => {
  if (diffContentRef.value && newValue) {
    diffContentRef.value.innerHTML = parseAndApplyColors(newValue);
  }
});
</script>

<style scoped>
.diff-container {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-width: 0;
  border-radius: 6px;
  overflow: hidden;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1), 0 2px 6px rgba(0, 0, 0, 0.06);
  transition: box-shadow 0.3s ease, transform 0.2s ease;
}

.diff-container:hover {
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15), 0 3px 8px rgba(0, 0, 0, 0.08);
}

.diff-container:focus-within {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(44, 62, 80, 0.15), 0 4px 10px rgba(0, 0, 0, 0.1);
}

.diff-header {
  padding: 14px 18px;
  background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
  border-bottom: 3px solid #9b59b6;
  display: flex;
  align-items: center;
  gap: 10px;
}

.diff-label {
  font-weight: 600;
  color: #ecf0f1;
  font-size: 12px;
  letter-spacing: 0.5px;
}

.diff-label::before {
  content: '';
  display: inline-block;
  width: 8px;
  height: 8px;
  background-color: #9b59b6;
  border-radius: 50%;
  margin-right: 8px;
}

.diff-content {
  flex: 1;
  padding: 18px 20px;
  overflow: auto;
  background-color: transparent;
  color: #2c3e50;
}

.diff-text {
  margin: 0;
  font-family: 'Fira Code', 'Courier New', 'Consolas', monospace;
  font-size: 14px;
  line-height: 1.6;
  white-space: pre-wrap;
  word-wrap: break-word;
}

/* ANSI Color Codes */
.ansi-code {
  font-weight: normal;
}

.ansi-31 {
  color: #e74c3c;
  background-color: #fadbd8;
}

.ansi-32 {
  color: #27ae60;
  background-color: #d5f5e3;
}

.ansi-36 {
  color: #3498db;
  background-color: #d6eaf8;
}

.ansi-37 {
  color: #7f8c8d;
  background-color: #f2f6f4;
}

.diff-content::-webkit-scrollbar {
  width: 8px;
}

.diff-content::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.diff-content::-webkit-scrollbar-thumb {
  background: #9b59b6;
  border-radius: 4px;
}

.diff-content::-webkit-scrollbar-thumb:hover {
  background: #8e44ad;
}
</style>
