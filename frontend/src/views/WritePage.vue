<template>
    <div>
        <div class="file-design"> 
            <label for="fileupload">사진 업로드</label>
            <input type="file" id="fileupload" @change="onFileSelected">
        </div>
        <textarea style="resize: none; width:100%;" name="" id="" rows="10"></textarea>
    </div>
</template>

<script>
export default {
    name: 'WritePage',
    data() {
        return {
            selectedFile: null,
        }
    },
    methods:{
        onFileSelected(event) {
            this.selectedFile = event.target.files[0]
            console.log(this.selectedFile, 1)
        }
    }
}
</script>

<style scoped>
.file-design label { 
    display: inline-block; 
    padding: .5em .75em; 
    color: #999; 
    font-size: inherit; 
    line-height: normal; 
    vertical-align: middle; 
    background-color: #fdfdfd; 
    cursor: pointer; 
    border: 1px solid #ebebeb; 
    border-bottom-color: #e2e2e2; 
    border-radius: .25em; 
} 
.file-design input[type="file"] { /* 파일 필드 숨기기 */ 
    position: absolute; 
    width: 1px; 
    height: 1px; 
    padding: 0; 
    margin: -1px; 
    overflow: hidden; 
    clip:rect(0,0,0,0); 
    border: 0; 
}
</style>