

    

    // let cancel = document.querySelector(".cross")
    // cancel.addEventListener("click", () => {
    //     fullImg.style.transform = "scale(0)"
    // })

    // if(btn.innerHTML == "♡"){
    //         btn.innerHTML = "&#10084;"
    //    } 
    //    else{
    //     btn.innerHTML = "&#9825;"
    //     console.log("changed")
    //    }   

    


    let num = document.querySelectorAll(".singleFeed").length
    let feedContainer = document.querySelector(".feed")
    if(window.matchMedia("(max-width: 1150px)").matches){
        if (num > 0 && num < 4) {
            feedContainer.style.height = "25vh"
        }  
    }
    else{
        if(num > 0 && num < 5) {
        feedContainer.style.height = "35vh"
        console.log("hello")
        }
    }




    


    let followbtn = document.querySelector("#followBtn")
    followbtn.addEventListener("click", () => {
        let userId = followbtn.getAttribute("data-user-id")
        addFollow(userId)

    })
    let Followers = document.querySelector("#follower")
    

    const addFollow = (userId) => {
        fetch("/follow", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": csrfToken
            },
            body: `userId=${userId}`

        }).then(res => res.json()).then(val => {
            Followers.innerText = `${val.allfollow}`
            console.log(`here is ${val.follow}`)
            if (val.follow) {
                followbtn.innerText = "Follow"
            }
            else {
                followbtn.innerText = "UnFollow"
            }
        }).catch(err => console.log(err))
    }

