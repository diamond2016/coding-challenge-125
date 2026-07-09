import { ref, computed, onMounted } from "vue";
import type { Task, TaskFormData } from "@/types/task";
import { useLocalStorage } from "./useLocalStorage";

const TASK_STORAGE_KEY = "task_manager_tasks";

/**
 * @description Manages all task-related state, logic, and data fetching.
 * @returns {object} An object containing reactive state and methods.
 */
export function useTaskManager() {
  // Instantiate useLocalStorage
  //    - <Task[]>: Specifies the type of data (an array of Task objects)
  //    - TASK_STORAGE_KEY: The string key used in localStorage
  //    - []: The initial value (an empty array of Tasks)
  const tasks = useLocalStorage<Task[]>(TASK_STORAGE_KEY, []);

  // --- STATE ---
  const filter = ref<"all" | "active" | "completed">("all");
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  // --- COMPUTED PROPERTIES ---
  const filteredTasks = computed(() => {
    const tasksToFilter =
      filter.value === "all"
        ? tasks.value
        : filter.value === "active"
          ? tasks.value.filter((task) => !task.isCompleted)
          : tasks.value.filter((task) => task.isCompleted);

    // Map tasks to include formatted dates for display
    return tasksToFilter.map((task) => ({
      ...task,
      createdAt: formatDate(task.createdAt), // Format createdAt date
    }));
  });

  // --- METHODS (CRUD & Logic) ---
  // Helper function to format ISO date string to dd/mm/yyyy
  const formatDate = (isoString: string): string => {
    if (!isoString) return "";
    const date = new Date(isoString);
    const day = String(date.getDate()).padStart(2, "0");
    const month = String(date.getMonth() + 1).padStart(2, "0"); // Months are 0-indexed
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
  };
  /**
   * Fetches initial task data (simulates API call).
   */
  // Simulate data received from a remote API
  const mockTasks: Task[] = [
    {
      id: crypto.randomUUID(),
      title: "Design UI Mockups",
      description: "Create high-fidelity mockups for the task manager.",
      priority: "high",
      dueDate: "10/05/2026",
      isCompleted: true,
      createdAt: new Date(Date.now() - 86400000).toISOString(),
    },
    {
      id: crypto.randomUUID(),
      title: "Implement Task Logic",
      description: "Finish the CRUD operations in useTaskManager.",
      priority: "high",
      dueDate: "12/06/2026",
      isCompleted: false,
      createdAt: new Date().toISOString(),
    },
    {
      id: crypto.randomUUID(),
      title: "Write Documentation",
      description: "Document the composables and API usage.",
      priority: "medium",
      dueDate: "1/06/2026",
      isCompleted: false,
      createdAt: new Date().toISOString(),
    },
  ];

  const fetchTasks = async () => {
    isLoading.value = true;
    try {
      // Simulate API fetch delay
      try {
        await new Promise((resolve) => setTimeout(resolve, 1000));
        tasks.value = [...tasks.value, ...mockTasks];
      } catch (e) {
        error.value = "Failed to fetch tasks from API.";
      }

      // Overwrite local storage data with fresh data from the API
      // Merge mock tasks with existing tasks to preserve user-added data
      tasks.value = mockTasks;
    } catch (e) {
      error.value = "Failed to fetch tasks from API.";
    } finally {
      isLoading.value = false;
    }
  };

  /**
   * Adds a new task to the list.
   * @param formData - The data for the new task.
   */
  const addTask = (formData: TaskFormData) => {
    // When you modify tasks.value, the useLocalStorage watcher automatically saves it!
    const newTask: Task = {
      id: crypto.randomUUID(),
      title: formData.title,
      description: formData.description,
      priority: formData.priority,
      dueDate: formData.dueDate,
      isCompleted: false,
      createdAt: new Date().toISOString(),
    };
    tasks.value = [...tasks.value, newTask];
  };

  /**
   * Updates an existing task.
   * @param id - The ID of the task to update.
   * @param formData - The new data for the task.
   */
  const updateTask = (id: string, formData: TaskFormData) => {
    tasks.value = tasks.value.map((task) =>
      task.id === id
        ? { ...task, ...formData, updatedAt: new Date().toISOString() }
        : task,
    );
  };

  /**
   * Deletes a task by ID.
   * @param id - The ID of the task to delete.
   */
  const deleteTask = (id: string) => {
    // modifying tasks.value triggers the save
    tasks.value = tasks.value.filter((task) => task.id !== id);
  };

  /**
   * Toggles the 'completed' status of a task.
   * @param id - The ID of the task to toggle.
   */
  const toggleTask = (id: string) => {
    tasks.value = tasks.value.map((task) =>
      task.id === id
        ? {
            ...task,
            completed: !task.isCompleted,
            updatedAt: new Date().toISOString(),
          }
        : task,
    );
  };

  // --- LIFECYCLE HOOKS ---
  onMounted(() => {
    fetchTasks();
  });

  // --- RETURN VALUES ---
  return {
    tasks,
    filteredTasks,
    filter,
    isLoading,
    error,
    addTask,
    updateTask,
    deleteTask,
    toggleTask,
  };
}
