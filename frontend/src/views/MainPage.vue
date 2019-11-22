<template>
    <div>
        <h1>Home</h1>
        <div class="row">
            <div class="col-4" style="padding: 0;">
                <div class="array">
                    <img src="https://image.chosun.com/sitedata/image/201903/07/2019030701652_0.jpg" alt="">
                </div>
            </div>
            <div class="col-4" style="padding: 0;">
                <div class="array">
                    <img src="https://image.chosun.com/sitedata/image/201903/07/2019030701652_0.jpg" alt="">
                </div>
            </div>
            <div class="col-4" style="padding: 0;">
                <div class="array">
                    <img src="http://www.bloter.net/wp-content/uploads/2017/09/%EA%B5%AC%EA%B8%80-%EC%96%B4%EC%8B%9C%EC%8A%A4%ED%84%B4%ED%8A%B8-%ED%95%9C%EA%B5%AD%EC%96%B4-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%B6%9C%EC%8B%9C4-765x1045.jpg" alt="">
                </div>
            </div>
            <div class="col-4" style="padding: 0;">
                <div class="array">
                    <img src="http://www.bloter.net/wp-content/uploads/2017/09/%EA%B5%AC%EA%B8%80-%EC%96%B4%EC%8B%9C%EC%8A%A4%ED%84%B4%ED%8A%B8-%ED%95%9C%EA%B5%AD%EC%96%B4-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%B6%9C%EC%8B%9C4-765x1045.jpg" alt="">
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
            postdata: []
        }
    },
    methods: {
    }
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