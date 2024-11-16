import { Fecther } from "../fetcher.js"

export const ListPosts = async () => {
    
    const r = await Fecther({
        url: 'http://localhost:8000/posts/get-posts/',
        method: 'GET'
    })
    console.log(await r.json())
    return `
        <section class="list-post"></section>
    `
}