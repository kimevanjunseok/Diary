<template>
    <div>
        <h1>Home</h1>
        <div class="row">
            <div v-for="data in postdata" v-bind:key="data" class="col-4" style="padding: 0;">
                <div class="array">
                    <img :src="imgUrl + data.imgfile" alt="">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "MainPage",
    data() {
        return {
            postdata: [],
            imgUrl: 'http://localhost:8000',
        }
    },
    mounted() {
        this.UserPost()
    },
    methods: {
        UserPost: async function() {
            await this.$http.get('http://127.0.0.1:8000/api/post/')
                .then(res => {
                    this.postdata = res.data
                })
        }
    },
}
</script>

<style scoped>
.array {
    position: relative;
    width: 90%;
    padding-bottom: 90%;
    margin: 15px;
}
img {
    position: absolute;
    width: 100%;
    height: 100%;
}
</style>