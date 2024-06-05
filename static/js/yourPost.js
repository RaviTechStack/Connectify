let editBtn = document.querySelectorAll(".edit")
let editMenu = document.querySelectorAll(".edit-menu")
let menuItem = document.querySelectorAll(".editItem")
let postUser = document.querySelectorAll(".postUser")


editBtn.forEach((btn , index)=>{
    btn.addEventListener("mouseenter", ()=>{
        btn.style.backgroundColor = "white"
        editMenu[index].style.display = "block"
    })
})
postUser.forEach((btn , index)=>{
    btn.addEventListener("mouseleave", ()=>{
        editBtn[index].style.backgroundColor = "initial"
        editMenu[index].style.display = "none"
    })
})
editMenu.forEach((btn , index)=>{
    btn.addEventListener("mouseenter", ()=>{
        btn.style.display = "block"
        editBtn[index].style.backgroundColor = "rgb(210, 210, 210)"
        menuItem.forEach(item =>{
            item.addEventListener("mouseenter",()=>{
                item.style.backgroundColor = "rgb(230, 230, 230)"
            })
        })
        menuItem.forEach(item =>{
            item.addEventListener("mouseleave",()=>{
                item.style.backgroundColor = "white"
            })
        })
        
    })
})


