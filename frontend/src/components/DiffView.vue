<template>
  <div class="diff-container">
    <div class="diff-header">
      <span class="diff-label">{{ label }}</span>
    </div>
    <div class="diff-content" ref="diffContentRef"></div>
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
  
  console.log('=== parseAndApplyColors called ===');
  console.log('Input text:', text);
  console.log('Input text length:', text.length);
  console.log('First char code:', text.charCodeAt(0));
  console.log('Char at position 0 (hex):', text.charCodeAt(0).toString(16));
  console.log('Char at position 1:', text.charCodeAt(1));
  console.log('Char at position 2:', text.charCodeAt(2));
  console.log('Char at position 3:', text.charCodeAt(3));
  console.log('Char at position 4:', text.charCodeAt(4));
  console.log('Char at position 5:', text.charCodeAt(5));
  console.log('Char at position 6:', text.charCodeAt(6));
  console.log('Char at position 7:', text.charCodeAt(7));
  console.log('Char at position 8:', text.charCodeAt(8));
  console.log('Char at position 9:', text.charCodeAt(9));
  console.log('Char at position 10:', text.charCodeAt(10));
  console.log('Char at position 11:', text.charCodeAt(11));
  console.log('Char at position 12:', text.charCodeAt(12));
  console.log('Char at position 13:', text.charCodeAt(13));
  console.log('Char at position 14:', text.charCodeAt(14));
  console.log('Char at position 15:', text.charCodeAt(15));
  console.log('Char at position 16:', text.charCodeAt(16));

  let result = '';
  let i = 0;
  
  while (i < text.length) {
    // Check for ANSI escape sequence: ESC [ n m (ESC = ASCII 27)
    const isEscape = text.charCodeAt(i) === 27;
    const isBracket = text[i + 1] === '[';

    console.log(`Position ${i}: char='${text[i]}' code=${text.charCodeAt(i)} (${text.charCodeAt(i).toString(16)}) isEscape=${isEscape} isBracket=${isBracket}`);

    if (isEscape && isBracket) {
      // Found ESC [, now extract the code
      let j = i + 2;
      while (j < text.length && text.charCodeAt(j) !== 109) { // 109 = 'm'
        j++;
      }
      if (j < text.length) {
        const code = parseInt(text.substring(i + 2, j), 10);
        // Get the character AFTER the 'm' (not the 'm' itself)
        const charAfterM = text[j + 1] || '';
        console.log(`Found escape sequence: code=${code}, charAfterM='${charAfterM}'`);
        result += `<span class=\"ansi-code ansi-${code}\" data-code=\"${code}\">${charAfterM}</span>`;
        i = j + 2;
      } else {
      result += text[i];
      i++;
    }
    } else {
      result += text[i];
      i++;
  }
  }
  
  console.log('Output HTML:', result);
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

