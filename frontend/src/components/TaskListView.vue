<template>
  <div class="task-list-view">
    <div class="controls-bar">
      <input type="text" placeholder="Search tasks..." class="search-input" />
      <select class="sort-select">
        <option value="date">Sort by Due Date</option>
        <option value="priority">Sort by Priority</option>
        <option value="creation">Sort by Creation Date</option>
      </select>
      <button class="add-filter-button">+ Add Filter</button>
      <button class="debug-button" @click="debugShowTasks">Debug Tasks</button>
    </div>

    <div class="task-list-container">
      <div class="task-list-header">
        <div>Title</div>
        <div>Desc.</div>
        <div>Priority</div>
        <div>DueDate</div>
        <div>Compl.</div>
      </div>
      <!-- Task items will be rendered here -->
      <div v-if="sortedTasks.length === 0" class="empty-state">
        No tasks found matching your criteria.
      </div>
      <div v-else>
        <div>Total: {{ sortedTasks.length }}</div>
        <div v-for="task in sortedTasks" :key="task.id">
          <TaskItem :task="task" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import TaskItem from '@/components/TaskItem.vue';
import { useTaskManager } from '@/composables/useTaskManager';
import { computed } from 'vue';

const { filteredTasks } = useTaskManager();

// Sort filtered tasks by due date in ascending order
const sortedTasks = computed(() => {
  // Safely handle undefined/null filteredTasks
  if (!filteredTasks.value || !Array.isArray(filteredTasks.value)) {
    return [];
  }
  return [...filteredTasks.value].sort((a, b) => {
    // Handle undefined/null due dates by treating them as far in the future
    const parseDate = (dateStr: string): number => {
      if (!dateStr) return Infinity;
      // Dates are in dd/mm/yyyy format
      const [day, month, year] = dateStr.split('/').map(Number);
      return new Date(year, month - 1, day).getTime();
    };
    const dateA = parseDate(a.dueDate);
    const dateB = parseDate(b.dueDate);
    return dateA - dateB;
  });
});

// Debug function to display all task data in a dialog
const debugShowTasks = () => {
  const tasks = sortedTasks.value;
  let output = '=== TASK LIST DEBUG ===\n\n';
  tasks.forEach((task, index) => {
    output += `Task ${index + 1}:\n`;
    output += `  ID: ${task.id}\n`;
    output += `  Title: ${task.title}\n`;
    output += `  Description: ${task.description}\n`;
    output += `  Priority: ${task.priority}\n`;
    output += `  Due Date: ${task.dueDate}\n`;
    output += `  Is Completed: ${task.isCompleted}\n`;
    output += `  Created At: ${task.createdAt}\n`;
    output += '------------------------\n';
  });
  output += `Total tasks: ${tasks.length}\n`;
  alert(output);
};
</script>

<style scoped>
.task-list-view {
  /* Styles inherited from TaskManager.vue, but defining internal structure */
  display: flex;
  flex-direction: column;
  height: 100%; /* Ensure the view takes full height */
}

.controls-bar {
  display: flex;
  gap: 15px;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
  align-items: center;
}

.search-input, .sort-select {
  padding: 10px 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1em;
}

.search-input {
  flex-grow: 1;
}

.add-filter-button {
  padding: 10px 20px;
  background-color: #2ecc71; /* Green accent */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.add-filter-button:hover {
  background-color: #27ae60;
}

.debug-button {
  padding: 10px 20px;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.debug-button:hover {
  background-color: #c0392b;
}

.task-list-container {
  flex-grow: 1; /* Allows the container to fill remaining space */
  display: flex;
  flex-direction: column; /* Stack header and tasks vertically */
  overflow-y: auto; /* Enables scrolling if tasks exceed height */
  padding: 0;
}

.task-list-header {
  display: flex;
  padding: 10px 15px;
  font-weight: bold;
  border-bottom: 1px solid #ccc;
  background-color: #f9f9f9;
}

.task-list-header div {
  flex: 1; /* Distribute space equally */
}

.empty-state {
  text-align: center;
  padding: 50px;
  color: #7f8c8d;
  font-size: 1.2em;
}
</style>