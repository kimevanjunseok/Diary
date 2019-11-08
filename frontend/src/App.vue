<template>
    <div id="app">
        <NavigationBar/>
        <div class="container">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import NavigationBar from './components/navbar/NavigationBar'

export default {
    name: 'app',
    components: {
        NavigationBar,
    }
}
</script>

<style scoped>
.container {
    margin-top: 70px;
}
</style>
