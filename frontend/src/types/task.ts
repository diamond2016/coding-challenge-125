export type Priority = 'low' | 'medium' | 'high';

export interface Task {
  id: string
  title: string
  description?: string
  priority: 'low' | 'medium' | 'high'
  isCompleted: boolean
  dueDate: string
  createdAt: string
}

export interface TaskFormData {
  title: string
  description?: string
  priority: 'low' | 'medium' | 'high'
  dueDate: string
}