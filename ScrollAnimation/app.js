const boxes = document.querySelectorAll('.box')
//the above puts them in an arr/node list

window.addEventListener('scroll', checkBoxes)

checkBoxes()

function checkBoxes(){
    const triggerBottom = window.innerHeight / 5 * 4

    // the below method returns the DOM rect obj and describes what to do with a rect, where it will be shown in the viewport. we want the top of the rect
    boxes.forEach(box =>{
        const boxTop = box.getBoundingClientRect().top
        // see if the top of the box is less than the trigger bottom, if it is, we want to add the class of show, if not, remove the class of show

        if(boxTop < triggerBottom){
            box.classList.add('show')
        }else{
            box.classList.remove('show')
        }
    })

}