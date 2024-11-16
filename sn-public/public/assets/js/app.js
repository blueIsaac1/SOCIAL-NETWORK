import { ListPosts } from "./components/list_posts.js"

( async () => {
    const root = document.getElementById('root')
    root.innerHTML = await ListPosts()
})()