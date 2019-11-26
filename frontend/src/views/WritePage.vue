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
        <button type="button" class="btn" @click="Write">저장</button>
    </div>
</template>

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