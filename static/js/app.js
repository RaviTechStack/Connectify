
let post = document.querySelector("#postBtn")
let menuBtn = document.querySelectorAll(".menuBtn")



const removeBorder = ()=>{
    menuBtn.forEach(elem =>{
        elem.classList.remove("border")
    })
}
post.addEventListener("click", ()=>{
    window.location = "/post"
})
menuBtn.forEach(elem =>{
    elem.addEventListener("click", ()=>{
        removeBorder()
        elem.classList.add("border")
    })
})



