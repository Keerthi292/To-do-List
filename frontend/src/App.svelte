<script lang="ts">
  import Sidebar from './components/Sidebar.svelte';
  import Header from './components/Header.svelte';
  import TaskInput from './components/TaskInput.svelte';
  import FilterTabs from './components/FilterTabs.svelte';
  import TaskList from './components/TaskList.svelte';
  import type { FilterType } from './types/todo';
  import { getTodos, createTodo, updateTodo, deleteTodo, clearAllTodos, type Todo } from './lib/api';
  import { onMount } from 'svelte';
  
  export let total: number = 0;

  let tasks: Todo[] = [];
  let filter: FilterType = 'all';
  let loading = false;
  let error: string | null = null;


  async function loadTasks() {
    try {
      loading = true;
      error = null;
      tasks = await getTodos();
    } catch (err) {
      error = 'Failed to load tasks';
      console.error('Error loading tasks:', err);
    } finally {
      loading = false;
    }
  }

  onMount(() => {
    loadTasks();
  });

  async function addTask(text: string) {
    try {
      error = null;
      const newTodo = await createTodo(text);
      tasks = [newTodo, ...tasks];
    } catch (err) {
      error = 'Failed to add task';
      console.error('Error adding task:', err);
    }
  }

  async function toggleTask(id: string) {
    try {
      error = null;
      const task = tasks.find(t => t.id === id);
      if (task) {
        const updatedTask = await updateTodo({ ...task, completed: !task.completed });
        tasks = tasks.map(t => t.id === id ? updatedTask : t);
      }
    } catch (err) {
      error = 'Failed to update task';
      console.error('Error toggling task:', err);
    }
  }

  async function deleteTask(id: string) {
    try {
      error = null;
      await deleteTodo(id);
      tasks = tasks.filter(task => task.id !== id);
    } catch (err) {
      error = 'Failed to delete task';
      console.error('Error deleting task:', err);
    }
  }

  async function toggleImportant(id: string) {
    try {
      error = null;
      const task = tasks.find(t => t.id === id);
      if (task) {
        const updatedTask = await updateTodo({ ...task, important: !task.important });
        tasks = tasks.map(t => t.id === id ? updatedTask : t);
      }
    } catch (err) {
      error = 'Failed to update task';
      console.error('Error toggling important:', err);
    }
  }

  async function editTask(id: string, text: string) {
    try {
      error = null;
      const task = tasks.find(t => t.id === id);
      if (task) {
        const updatedTask = await updateTodo({ ...task, text });
        tasks = tasks.map(t => t.id === id ? updatedTask : t);
      }
    } catch (err) {
      error = 'Failed to update task';
      console.error('Error editing task:', err);
    }
  }

  async function clearCompleted() {
    try {
      error = null;
      const completedTasks = tasks.filter(task => task.completed);
      await Promise.all(completedTasks.map(task => deleteTodo(task.id)));
      await loadTasks(); // Reload to get fresh data
    } catch (err) {
      error = 'Failed to clear completed tasks';
      console.error('Error clearing completed:', err);
    }
  }

  async function clearAll() {
    try {
      error = null;
      await clearAllTodos();
      await loadTasks(); // Reload to get fresh data
    } catch (err) {
      error = 'Failed to clear all tasks';
      console.error('Error clearing all:', err);
    }
  }

  $: filteredTasks =
    filter === 'all'
      ? tasks
      : filter === 'active'
        ? tasks.filter((task) => !task.completed)
        : tasks.filter((task) => task.completed);

  $: total = tasks.length;
  $: completedCount = tasks.filter((task) => task.completed).length;
  $: importantCount = tasks.filter((task) => task.important).length;
  $: activeCount = tasks.filter((task) => !task.completed).length;
</script>

<div class="app-shell container-fluid py-4">
  <div class="todo-wrapper mx-auto">
    <div class="row g-0 h-100">
      <div class="col-lg-3 border-end sidebar-panel">
        <Sidebar
          {total}
          {completedCount}
          {importantCount}
          {activeCount}
        />
      </div>

      <div class="col-lg-9 content-panel">
        <div class="p-4 p-lg-5">
          <Header total/>

          {#if error}
            <div class="alert alert-danger" role="alert">
              {error}
              <button 
                type="button" 
                class="btn-close float-end" 
                on:click={() => error = null}
                aria-label="Close"
              ></button>
            </div>
          {/if}

          {#if loading}
            <div class="text-center py-4">
              <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
              <p class="mt-2">Loading tasks...</p>
            </div>
          {:else}
            <TaskInput onAdd={addTask} />

            <FilterTabs
              activeFilter={filter}
              onChange={(value) => (filter = value)}
              onClearCompleted={clearCompleted}
            />

            <TaskList
              tasks={filteredTasks}
              onToggle={toggleTask}
              onDelete={deleteTask}
              onStar={toggleImportant}
              onEdit={editTask}
              onClearAll={clearAll}
            />
          {/if}
        </div>
      </div>
    </div>
  </div>
</div>