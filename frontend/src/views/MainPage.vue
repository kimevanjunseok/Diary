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
            <button type="button" class="btn btn-success" @click="test">저장</button>
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
    methods: {
        test() {
            this.$http.get('http://127.0.0.1:8000/api/post')
            .then(res => {
                console.log(res)
            })
        }
    }
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