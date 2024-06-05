let likeCount = document.querySelector("#likecount")  
let likeOpt = document.querySelector("#like")
let cmt = document.querySelector(".commentSection")
let cmtbtn = document.querySelector(".cmtBtn")
let cross = document.querySelector(".cross")


cross.addEventListener("click", ()=>{
    history.back()
})

//   HANDLING COMMENTS REPLY DISPLAY
let replyBtn = document.querySelectorAll(".replybtn")
  let reply = document.querySelectorAll(".reply")
  replyBtn.forEach((btn, index) => {
      btn.addEventListener("click", () => {
          if (reply[index].style.display == "block") {
              reply[index].style.display = "none"
          }
          else {
              reply[index].style.display = "block"
          }
      })
  })

  if(comment_open === "true"){
    cmt.style.transform = "translateY(0)"
    console.log("here")
  }
  

  cmtbtn.addEventListener("click", ()=>{
      cmt.style.transform = "translateY(0)"

  })

  document.querySelector(".hide").addEventListener("click", ()=>{
      cmt.style.transform = "translateY(65vh)"

  })

likeOpt.addEventListener("click", ()=>{
  id = likeOpt.getAttribute("data-id")
  addLike(id)
})

  const addLike = (postId) => {
      console.log(postId)
      fetch("/addLike", {
          method: "POST",
          headers: {
              "Content-Type": "application/x-www-form-urlencoded",
              "X-CSRFToken": csrftoken
          },
          body: `postId=${postId}`
      }).then(data => data.json()).then((res) => {
          likeCount.innerHTML = res.numberOfLike
          if(res.liked){
              likeOpt.innerHTML = "&#10084;"
          }
          else{
              likeOpt.innerHTML = "&#9825;"
          }
      }).catch(err => console.log(err))
  }