<template>
    <div>
        <div v-if="!error">
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
        
            <button type="button" class="btn" @click="Write">Save</button>     
        </div>
        <div v-else>
            <div style="height:100px;">
            </div>
                <h1>잘못된 접근 입니다.</h1>
                <h1>{{ error }}</h1>
        </div>
    </div>
</template>

<script>
import api from "@/api/api"

export default {
    name: 'UpdatePage', 
    data() {
        return {
            postid: this.$route.params.id,
            filename: 'Change',
            selectedFile: null,
            content: "",
            image: null,
            error: null,
        }
    },
    mounted() {
        this.GetUserData(this.postid)
    },
    methods: {
        GetUserData: async function(id) {
            await api.UpdatePage(id)
            .then(res => {
                this.content = res.data.content
                this.selectedFile = api.ApiUrl() + res.data.imgfile
            })
            .catch(error => {
                this.error = error
            })
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
            if (this.image) {
                filedata.append('image', this.image.files[0])
            } else {
                filedata.append('image', null)
            }
            await api.UpdatePost(this.postid, filedata)
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