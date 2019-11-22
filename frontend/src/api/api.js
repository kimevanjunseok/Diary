import axios from 'axios'

const apiUrl= "http://localhost:8000"

export default {
    ApiUrl() {
        return apiUrl
    },
    PostAll() {
        return axios.get(`${apiUrl}/api/post/`)
    },
    PostWrite(params) {
        return axios.post(`${apiUrl}/api/post/create/`, params)
    }
}