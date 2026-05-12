<script lang="ts">
  export let onAdd: (text: string) => void;

  let taskText = '';

  function submitTask() {
    const cleanText = taskText.trim();
    if (!cleanText) return;
    onAdd(cleanText);
    taskText = '';
  }
</script>

<div class="task-input-row">
  <input
    bind:value={taskText}
    type="text"
    class="task-input"
    placeholder="What do you want to do?"
    on:keydown={(e) => e.key === 'Enter' && submitTask()}
  />

  <button class="add-btn" type="button" on:click={submitTask}>
    Add Task
  </button>
</div>