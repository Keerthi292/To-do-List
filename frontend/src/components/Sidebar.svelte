<script lang="ts">
  let {
    total = 0,
    completedCount = 0,
    importantCount = 0,
    activeCount = 0
  } = $props<{
    total: number;
    completedCount: number;
    importantCount: number;
    activeCount: number;
  }>();
</script>

<div class="sidebar-wrap d-flex flex-column justify-content-between h-100">
  <div>
    <div class="brand-box text-white p-4">
      <h2 class="mb-0 d-flex align-items-center gap-2">
        <i class="bi bi-clipboard-check" ></i>
        Todo App
      </h2>
    </div>

    <div>
      <div class="menu-item active d-flex justify-content-between align-items-center mb-3">
        <div class="d-flex align-items-center gap-2">
          <i class="bi bi-grid"></i>
          <span>All Tasks</span>
        </div>
        <span class="badge-count">{total}</span>
      </div>

      <div class="menu-item d-flex justify-content-between align-items-center mb-3">
        <div class="d-flex align-items-center gap-2">
          <i class="bi bi-hourglass-split"></i>
          <span>Active</span>
        </div>
        <span class="badge-count">{activeCount}</span>
      </div>

      <div class="menu-item d-flex justify-content-between align-items-center mb-3">
        <div class="d-flex align-items-center gap-2">
          <i class="bi bi-check-circle"></i>
          <span>Completed</span>
        </div>
        <span class="badge-count">{completedCount}</span>
      </div>

      <div class="menu-item d-flex justify-content-between align-items-center mb-4">
        <div class="d-flex align-items-center gap-2">
          <i class="bi bi-star"></i>
          <span>Important</span>
        </div>
        <span class="badge-count">{importantCount}</span>
      </div>

      <hr />

      
    </div>
  </div>

  <div class="p-4 text-center">
    <div class="illustration-box mx-auto d-flex align-items-center justify-content-center">
      <i class="bi bi-card-checklist display-3 text-primary"></i>
    </div>
  </div>
</div>