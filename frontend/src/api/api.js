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
        return axios.get(`${apiUrl}/api/post/${id}/`)
    },
    UpdatePatch(id, params) {
        return axios.patch(`${apiUrl}/api/post/update/${id}/`, params)
    },
    UpdatePut(id, params) {
        return axios.put(`${apiUrl}/api/post/update/${id}/`, params)
    },
    DeletePost(id) {
        return axios.delete(`${apiUrl}/api/post/delete/${id}/`)
    }
}