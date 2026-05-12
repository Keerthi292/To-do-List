<script lang="ts">
  import type { Todo } from '../types/todo';

  export let tasks: Todo[] = [];
  export let onToggle: (id: number) => void;
  export let onDelete: (id: number) => void;
  export let onStar: (id: number) => void;
  export let onEdit: (id: number, text: string) => void;
  export let onClearAll: () => void;

  let editingId: number | null = null;
  let editedText = '';

  function startEdit(task: Todo) {
    editingId = task.id;
    editedText = task.text;
  }

  function saveEdit(id: number) {
    const cleanText = editedText.trim();
    if (!cleanText) return;

    onEdit(id, cleanText);
    editingId = null;
    editedText = '';
  }

  function cancelEdit() {
    editingId = null;
    editedText = '';
  }
</script>

<div class="task-list">
  {#if tasks.length === 0}
    <div class="empty-box">
      <div class="empty-icon">📝</div>
      <h3>No tasks yet</h3>
      <p>Add your first task to start managing your work.</p>
    </div>
  {:else}
    {#each tasks as task (task.id)}
      <div class="task-card">
        <div class="task-left">
          <input
            type="checkbox"
            class="task-checkbox"
            checked={task.completed}
            on:change={() => onToggle(task.id)}
          />

          {#if editingId === task.id}
            <input
              bind:value={editedText}
              class="edit-input"
              on:keydown={(e) => {
                if (e.key === 'Enter') saveEdit(task.id);
                if (e.key === 'Escape') cancelEdit();
              }}
            />
          {:else}
            <span class="task-text" class:completed-text={task.completed}>
              {task.text}
            </span>
          {/if}
        </div>

        <div class="task-actions">
          {#if editingId === task.id}
            <button class="icon-btn save-btn" type="button" on:click={() => saveEdit(task.id)}>
              Save
            </button>
            <button class="icon-btn cancel-btn" type="button" on:click={cancelEdit}>
              Cancel
            </button>
          {:else}
            <button class="icon-btn edit-btn" type="button" on:click={() => startEdit(task)}>
              Edit
            </button>
            <button class="icon-btn star-btn" type="button" on:click={() => onStar(task.id)}>
              {task.important ? '★' : '☆'}
            </button>
            <button class="icon-btn delete-btn" type="button" on:click={() => onDelete(task.id)}>
              Delete
            </button>
          {/if}
        </div>
      </div>
    {/each}
  {/if}
</div>

<div class="task-footer">
  <p>{tasks.filter((task) => !task.completed).length} tasks remaining</p>
  <button class="clear-all-btn" type="button" on:click={onClearAll}>Clear all</button>
</div>