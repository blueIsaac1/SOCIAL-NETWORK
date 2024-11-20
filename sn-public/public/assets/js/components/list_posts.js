import { Fecther } from "../fetcher.js"
import { Post } from "./post.js"

export const ListPosts = async () => {
    
    const response = await Fecther({
        url: '/posts/get-posts/',
        method: 'GET'
    })
    console.log(await response)

    const ListPromisesPosts = response.map(async (post) => await Post(post))
    const ListPosts = await Promise.all(ListPromisesPosts)

    return `
        <section class="list-post">${
            ListPosts.join('')
        }</section>
    `
}