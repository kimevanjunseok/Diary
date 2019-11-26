<template>
    <div>
        <div class="profile">
            <img class="profile-img rounded-circle" src="https://news.korean.go.kr/wp-content/uploads/2015/11/secret_CG_visual_151117.jpg" alt="">
        </div>
        <hr>
        <div class="row">
            <div v-for="(value, key) in postdata" v-bind:key="key" class="col-4" style="padding: 0;">
                <div class="array">
                    <img class="postimg" :src="imgUrl + value.imgfile" alt="">
                </div>
                    <div class="darkness"></div>
            </div>
        </div>
        <div id="map" style="width:500px;height:400px;"></div>
    </div>
</template>
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=430d2bc0c6980838704c2c88e382e1f3"></script>
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
        let container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
        let options = { //지도를 생성할 때 필요한 기본 옵션
            center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
            level: 3 //지도의 레벨(확대, 축소 정도)
        };

        let map = new kakao.maps.Map(container, options);
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
    text-align: center;
}
.profile-img {
    width: 12vw;
    height: 12vw;
    margin-top: 120px;
    margin-bottom: 20px;
}

.array {
    position: relative;
    width: 90%;
    padding-bottom: 90%;
    margin: 15px;
    cursor: pointer;
}
.postimg {
    position: absolute;
    width: 100%;
    height: 100%;
}

.postimg:hover {
    opacity: 0.7;
}
</style>