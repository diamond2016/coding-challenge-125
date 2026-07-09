<template>
  <div class="task-item">
    <div class="task-item-attribute long-text">{{ task.title }}</div>
    <div class="task-item-attribute long-text">{{ task.description }}</div>
    <div class="task-item-attribute">{{ task.priority }}</div>
    <div class="task-item-attribute">{{ task.dueDate }}</div>
    <div class="task-item-attribute">{{ String(task.isCompleted) }}</div>
  </div>
</template>
                                                                                                                                                    
<script setup lang="ts">
import { type Task} from "@/types/task.ts";
defineProps<{ task: Task }>();
</script>
                                                                                                                                                    
                                                                                                                                                    
<style scoped lang="css">
.task-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 0;
}

.task-item-attribute {
  font-size: 0.95em;
}

.task-item-attribute.long-text {
  flex: 1 1 auto;
  overflow-wrap: anywhere;
  white-space: normal;
}
</style>

