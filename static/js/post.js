let inpt = document.querySelector("#post")
let preview = document.querySelector(".preview")
let imgdiv = document.querySelector("#imgdiv")

inpt.addEventListener("change", ()=>{
    console.log("changed")
    let imgurl = URL.createObjectURL(inpt.files[0])
    console.log(imgurl)
    imgdiv.src = imgurl
})