export interface Todo {
  id: string;
  text: string;
  completed: boolean;
  important: boolean;
}

const BASE_URL = 'http://localhost:8000';

export async function getTodos(): Promise<Todo[]> {
  try {
    const res = await fetch(`${BASE_URL}/todos`);
    if (!res.ok) throw new Error('Failed to fetch todos');
    return res.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
}

export async function createTodo(text: string): Promise<Todo> {
  const res = await fetch(`${BASE_URL}/todos`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      text,
      completed: false,
      important: false
    })
  });

  if (!res.ok) throw new Error('Failed to create todo');
  return res.json();
}

export async function updateTodo(todo: Todo): Promise<Todo> {
  const res = await fetch(`${BASE_URL}/todos/${todo.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      text: todo.text,
      completed: todo.completed,
      important: todo.important
    })
  });

  if (!res.ok) throw new Error('Failed to update todo');
  return res.json();
}

export async function deleteTodo(id: string): Promise<void> {
  const res = await fetch(`${BASE_URL}/todos/${id}`, {
    method: 'DELETE'
  });

  if (!res.ok) throw new Error('Failed to delete todo');
}

export async function clearAllTodos(): Promise<void> {
  const res = await fetch(`${BASE_URL}/todos`, {
    method: 'DELETE'
  });

  if (!res.ok) throw new Error('Failed to clear todos');
}