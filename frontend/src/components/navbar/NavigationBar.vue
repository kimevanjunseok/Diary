<template>
    <nav class="navbar fixed-top navbar-expand-lg navbar-light">
        <div class="container">
            <a class="navbar-brand" href="/"><i class="far fa-clipboard fa-lg"></i>&nbsp;Diary</a>
            <div class="navbar-nav">
                <a class="nav-item nav-link" href="/WritePage"><i class="far fa-edit fa-lg"></i></a>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavigationBar",
}
</script>

<style scoped>
nav {
    height: 48px;
    background-color: #fafafa;
}
.container {
    padding-right: 12vw;
    padding-left: 12vw;   
}
.navbar-brand {
    font-family: 'Pacifico', cursive;
}
</style>