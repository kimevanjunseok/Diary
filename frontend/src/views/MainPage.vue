<template>
    <div>
        <div class="profile">
            <img class="profile-img rounded-circle" src="https://news.korean.go.kr/wp-content/uploads/2015/11/secret_CG_visual_151117.jpg" alt="">
        </div>
        <hr>
        <div class="row">
            <div v-for="(value, key) in postdata" v-bind:key="key" class="col-4" style="padding: 0;">
                <div class="array">
                    <img class="postimg" :src="imgUrl + value.imgfile" alt="" @click="$bvModal.show(value.imgfile)">
                    <b-modal :id="value.imgfile" size="lg" hide-footer>
                        <template v-slot:modal-header="{ close }">
                            <i class="fas fa-ellipsis-v modal-icon" v-b-modal.modal-1></i>

                            <b-modal id="modal-1" title="BootstrapVue" size="sm" hide-header hide-footer>
                                <p class="modal-p" @click="UpdatePage(value.id)">수정</p>
                                <hr>
                                <p class="modal-p" @click="Delete(value.id)">삭제</p>
                            </b-modal>
                        </template>
           
                        <div class="d-block text-center">
                            <img class="modal-img" :src="imgUrl + value.imgfile" alt="">
                            <p>{{ value.content }}</p>
                        </div>
                    </b-modal>
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
        },
        UpdatePage: function(id) {
            this.$router.push({name: 'UpdatePage', params: {id: id}})
        },
        Delete: function(id) {
            const answer = confirm("정말 게시물을 삭제하시겠습니까?")
            if (answer) {
                api.DeletePost(id)
                window.location.href = '/'
            }
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

.modal-icon {
    margin-left: 98%;
    float: right;
    color:rgba(0, 0, 0, 0.5);
    cursor: pointer;
}
.modal-img {
    width: 50%;
}

.modal-p {
    margin: 0px;
    text-align: center;
    cursor: pointer;
}
</style>