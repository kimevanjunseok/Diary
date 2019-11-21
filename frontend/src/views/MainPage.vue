<template>
    <div class="row">
        <div class="col-4 array">
            test
        </div>
        <div class="col-4 array">
            test
        </div>
        <div class="col-4 array">
            test
        </div>
        <div class="col-4 array">
            test
        </div>
    </div>
</template>

<script>
export default {
    name: "MainPage",
    data() {
        return {
            postdata: []
        }
    },
}
</script>

<style scoped>
.array {
    flex: 31% !important;
    max-width: 31% !important;
    border: 1px black solid;
    margin: 10px;
}
</style>