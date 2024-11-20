import { Fecther } from "../fetcher.js"

export const MiniPostUser = async (post) => {

    const response = await Fecther({
        url: `/users/get-mini-user/${post.user_id}`,
        method: 'GET'
    })
    console.log(response.user_pic)
    return `
        <a class="mini-user" href="#">
            <div class="avatar">
                <img src="${response.image_pic}">
            </div>
            <div class="info">
                <div>${response.name}</div>
                <div class="time">${new Date(post.created_at).toLocaleString()}</div>
            </div>
        </a>
    `
}