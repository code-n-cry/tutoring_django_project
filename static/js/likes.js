function getCookie(name) {
    let pattern = RegExp(name + "=.[^;]*")
    let matched = document.cookie.match(pattern)
    if (matched) {
        let cookie = matched[0].split("=")
        return cookie[1]
    }
    return false
}

document.addEventListener("click", function (btn) {
    let target = btn.target;
    if (target.id.includes("LikedBtn")) {
        let target_id = target.id.split("_")[1]
        fetch("/likes/like/" + target_id, {
            method: "POST",
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                "X-CSRFToken": getCookie("csrftoken")
            }
        }).then(r => {
            if (r.status === 200) {
                document.getElementById("Like_" + target_id).classList.remove("bi-heart")
                document.getElementById("Like_" + target_id).classList.add("bi-heart-fill")
                document.getElementById("Like_" + target_id).innerHTML = `<path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>`
                document.getElementById("Likes_" + target_id).innerText = `${Number(document.getElementById("Likes_" + target_id).innerText) + 1}`
            }
        })
        target.id = "DislikedBtn_" + target_id
    } else if (target.id.includes("DislikedBtn")) {
        let target_id = target.id.split("_")[1]
        fetch("/likes/dislike/" + target_id, {
            method: "POST",
            headers: {
                "Content-type": "application/json; charset=UTF-8",
                "X-CSRFToken": getCookie("csrftoken")
            }
        }).then(r => {
            if (r.status === 200) {
                document.getElementById("Like_" + target_id).classList.remove("bi-heart-fill")
                document.getElementById("Like_" + target_id).classList.add("bi-heart")
                document.getElementById("Like_" + target_id).innerHTML = `<path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143q.09.083.176.171a3 3 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>`
                document.getElementById("Likes_" + target_id).innerText = `${Number(document.getElementById("Likes_" + target_id).innerText) - 1}`
            }
        })
        target.id = "LikedBtn_" + target_id
    }
});