<template>
    <header class="app-header">
        <div class="logo">
            <router-link to="/"><img src="@/assets/logo.svg" alt="Diff Manager Logo"></router-link>
        </div>
        <nav class="header-nav">
            <router-link to="/load-text1" class="router-button">
                Load text #1
            </router-link>
            <router-link to="/load-text2" class="router-button">
                Load text #2
            </router-link>
            <router-link to="/diff" class="router-button">
                Diff #1 #2
            </router-link>
        </nav>
    </header>
</template>

<script lang="ts">
</script>

<style lang="css" scoped>
.app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    background-color: #2d59aa; /* Dark blue/grey background */
    color: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.logo img {
    height: 40px; /* Adjust logo size */
    width: auto;
}

.header-nav {
    display: flex;
    gap: 20px; /* Space between buttons */
}

.router-button {
    color: white;
    text-decoration: none;
    padding: 8px 15px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    font-weight: 600;
}

.router-button:hover {
    background-color: #34495e; /* Slightly lighter on hover */
}
</style>