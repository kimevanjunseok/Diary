<template>
    <div>
        <div class="file-design">
            <div class="input-group mb-3">
                <div class="input-group-prepend" style="margin-top:100px">
                    <span class="input-group-text" id="inputGroupFileAddon01">Photo</span>
                </div>
                <div class="custom-file" style="margin-top:100px">
                    <input type="file" ref="image" @change="onFileSelected" class="custom-file-input" id="inputGroupFile01" aria-describedby="inputGroupFileAddon01" accept=".jpg, .png, .gif">
                    <label class="custom-file-label" for="inputGroupFile01">{{ filename }}</label>
                </div>
            </div>
        </div>
        <img v-show="selectedFile" class="fileimg" :src="selectedFile" alt="">
        <textarea style="resize: none; width:100%;" v-model="content" rows="10"></textarea>

        <button class="btn" id="show-btn" @click="$bvModal.show('bv-modal-map')">Open Map</button>

        <b-modal id="bv-modal-map" hide-footer>
            <template v-slot:modal-title>
                위치 저장
            </template>
            <div class="d-block text-center">
                <div id="map" style="width:100%;height:32vw;"></div>
                <button type="button" class="btn" @click="mapCreate">저장</button>  
            </div>
            <button class="mt-3 btn" block @click="$bvModal.hide('bv-modal-map')">Save</button>
        </b-modal>
      
        <button type="button" class="btn" @click="Write">Save</button>     
    </div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=430d2bc0c6980838704c2c88e382e1f3"></script>

<script>
import api from "@/api/api"

export default {
    name: 'WritePage',
    data() {
        return {
            filename: 'Choose Photo',
            selectedFile: null,
            content: "",
            image: null,
        }
    },
    mounted() {
        
    },
    methods: {
        mapCreate: function() {
            let container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
            let options = { //지도를 생성할 때 필요한 기본 옵션
                center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
                level: 3 //지도의 레벨(확대, 축소 정도)
            };

            let map = new kakao.maps.Map(container, options);
        },
        onFileSelected: function() {
            this.image = event.target
            if (this.image.files && this.image.files[0]) { 
                var reader = new FileReader(); 
                reader.onload = (e) => { 
                    this.selectedFile = e.target.result
                    this.filename = this.image.files[0].name
                } 
                reader.readAsDataURL(this.image.files[0]); 
            }
        },
         Write: async function() {
            const filedata = new FormData()
            filedata.append('content', this.content)
            filedata.append('image', this.image.files[0])
            await api.PostWrite(filedata)
            this.$router.push('/')
        }
    }
}
</script>

<style scoped>
.fileimg {
    width: 100%;
    margin-bottom: 20px; 
}
.btn {
    background-color: #e9ecef;
    border: 1px solid #ced4da;
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>