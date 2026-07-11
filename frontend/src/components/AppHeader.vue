<template>
    <header class="app-header">
        <div class="logo">
            <router-link to="/"><img src="@/assets/logo.svg" alt="Diff Manager Logo"></router-link>
        </div>
        <nav class="header-nav">
            <router-link to="/diff-prettyp" class="router-button">
                Diff
            </router-link>
            <button v-if="onDiffClick" class="diff-button" @click="onDiffClick">
                Run Diff
            </button>
        </nav>
    </header>
</template>

<script setup lang="ts">
  // Props to allow parent component to provide a callback
  defineProps<{
    onDiffClick?: () => void
  }>();
</script>
