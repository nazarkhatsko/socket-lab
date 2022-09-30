const SERVER = getServer()
getPosts()

function getServer() {
    const host = prompt("Enter the server host", ["localhost"])
    const port = prompt("Enter the server port", [3000])
    return `http://${host}:${port}`
}

function createPostList(posts) {
    const list = document.querySelector(".blog-list")
    while (list.lastChild) {
        list.removeChild(list.lastChild)
    }

    if (posts.length == 0) {
        const title = document.createElement("label")
        title.setAttribute("class", "blog-title")
        title.innerHTML = "There aren't any posts"
        list.appendChild(title)
    }

    for (let i = 0; i < posts.length; i++) {
        const box = document.createElement("div")
        box.setAttribute("class", "blog-box")

        const content = document.createElement("label")
        content.setAttribute("class", "blog-content")
        content.innerHTML = posts[i].data
        box.appendChild(content)

        const remove = document.createElement("button")
        remove.setAttribute("class", "blog-remove")
        remove.innerHTML = "Remove"
        remove.addEventListener("click", () => {
            removePost(posts[i].id)
        })
        box.appendChild(remove)

        list.appendChild(box)
    }
}

function addNewPost() {
    const newBlogInput = document.querySelector(".new-blog-input")
    if (newBlogInput.value != "") {
        newPost(newBlogInput.value)
        newBlogInput.value = ""
    }
}

function getPosts() {
    fetch(`${SERVER}/api/get/posts/`)
    .then(res => {
        return res.json()
    })
    .then(list => {
        return createPostList(list)
    })
    .catch(err => {
        console.log("Error: " + error)
    })
}

function newPost(postData) {
    fetch(`${SERVER}/api/new/post/`, {
        method: "POST",
        body: JSON.stringify({
            post_data: postData
        })
    })
    .then(res => {
        return res.json()
    })
    .then(list => {
        return createPostList(list)
    })
    .catch(err => {
        console.log("Error: " + error)
    })
}

function removePost(postId) {
    fetch(`${SERVER}/api/remove/post/`, {
        method: "POST",
        body: JSON.stringify({
            post_id: postId
        })
    })
    .then(res => {
        return res.json()
    })
    .then(list => {
        return createPostList(list)
    })
    .catch(err => {
        console.log("Error: " + error)
    })
}
