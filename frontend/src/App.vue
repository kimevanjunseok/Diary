<template>
    <div id="app" class="container">
        <NavigationBar/>
        <div>
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
    },
    mounted() {
        document.getElementById("app").style.minHeight = window.innerHeight + 'px'
    }
}
</script>

<style scoped>
.container {
    background-color: #FFFFF0;
    padding-right: 12vw; 
    padding-left: 12vw;
}
</style>
