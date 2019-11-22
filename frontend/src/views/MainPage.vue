<template>
    <div>
        <div class="profile">
            <img class="profile-img rounded-circle" src="https://news.korean.go.kr/wp-content/uploads/2015/11/secret_CG_visual_151117.jpg" alt="">
        </div>
        게시물 : {{ postdata.length }}
        <hr>
        <div class="row">
            <div v-for="(value, key) in postdata" v-bind:key="key" class="col-4" style="padding: 0;">
                <div class="array">
                    <img class="postimg" :src="imgUrl + value.imgfile" alt="">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import api from "@/api/api"

export default {
    name: "MainPage",
    data() {
        return {
            postdata: [],
            imgUrl: api.ApiUrl(),
        }
    },
    mounted() {
        this.UserPost()
    },
    methods: {
        UserPost: async function() {
            await api.PostAll()
                .then(res => {
                    this.postdata = res.data
                })
        }
    },
}
</script>

<style scoped>
.profile {
    position: relative;
    width: 20%;
    padding-bottom: 20%;
    margin-left: 100px; 
    margin-bottom: 20px; 
}
.profile-img {
    position: absolute;
    width: 100%;
    height: 100%;
    right: 0;
}

.array {
    position: relative;
    width: 90%;
    padding-bottom: 90%;
    margin: 15px;
}
.postimg {
    position: absolute;
    width: 100%;
    height: 100%;
}
</style>