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
    },
    UpdatePage(id) {
        return axios.get(`${apiUrl}/api/post/update/${id}/`)
    },
    Update(id, params) {
        return axios.patch(`${apiUrl}/api/post/update/${id}/`, params)
    },
}