<template>
    <div>
        <div class="file-design"> 
            <div class="input-group mb-3">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="inputGroupFileAddon01">Photo</span>
                </div>
                <div class="custom-file">
                    <input type="file" @change="onFileSelected" class="custom-file-input" id="inputGroupFile01" aria-describedby="inputGroupFileAddon01" accept=".jpg, .png, .gif">
                    <label class="custom-file-label" for="inputGroupFile01">{{ filename }}</label>
                </div>
            </div>
        </div>
        <img class="fileimg" :src="selectedFile" alt="">
        <textarea style="resize: none; width:100%;" v-model="content" rows="10"></textarea>
        <button type="button" class="btn btn-success">저장</button>
    </div>
</template>

<script>
export default {
    name: 'WritePage',
    data() {
        return {
            filename: 'Choose Photo',
            selectedFile: null,
            content: "",
        }
    },
    methods:{
        onFileSelected(event) {
            let inputdata = event.target

            if (inputdata.files && inputdata.files[0]) { 
                var reader = new FileReader(); 
                reader.onload = (e) => { 
                    this.selectedFile = e.target.result
                    this.filename = inputdata.files[0].name
                    } 
                reader.readAsDataURL(inputdata.files[0]); }
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
    margin-top: 5px;
    float: right;
}
</style>