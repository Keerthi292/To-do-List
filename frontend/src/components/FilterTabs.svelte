<script lang="ts">
  import type { FilterType } from '../types/todo';

  export let activeFilter: FilterType = 'all';
  export let onChange: (filter: FilterType) => void;
  // export let onClearCompleted: () => void;
</script>

<div class="filter-row">
  <div class="filter-tabs">
    <button
      type="button"
      class:active={activeFilter === 'all'}
      class="filter-pill"
      on:click={() => onChange('all')}
    >
      All
    </button>

    <button
      type="button"
      class:active={activeFilter === 'active'}
      class="filter-pill"
      on:click={() => onChange('active')}
    >
      Active
    </button>

    <button
      type="button"
      class:active={activeFilter === 'completed'}
      class="filter-pill"
      on:click={() => onChange('completed')}
    >
      Completed
    </button>
  </div>


</div>