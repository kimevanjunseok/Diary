import axios from 'axios'

const apiUrl= "http://127.0.0.1:8000/api"

export default {
    PostWrite(params) {
        return axios.post(`${apiUrl}/post/create/`, params)
    }
}