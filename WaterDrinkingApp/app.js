//make a node list of the elements with cup small class
const smallCups = document.querySelectorAll('.cup-small')
const liters = document.getElementById('liters')
const percentage = document.getElementById('percentage')
const remaining = document.getElementById('remained')

updateBigCup()

smallCups.forEach((cup, idx) => {
    console.log(idx)
    cup.addEventListener('click', () => highlightCups(idx))
})

const highlightCups = (idx) => {
    //with the below, we are checking the node list to see which index we are at so we can decrease it if needed
    if(smallCups[idx].classList.contains('full') && !smallCups[idx].nextElementSibling.classList.contains('full')){
        idx--
    }

    smallCups.forEach((cup, indi) => {
        //get the index of each one in this loop
        if(indi <= idx){
            cup.classList.add('full')
        }else{
            cup.classList.remove('full')
        }
    })

    updateBigCup()
}

function updateBigCup(){
    //get the num of full glasses
    const fullCups = document.querySelectorAll('.cup-small.full').length

    const totalCups = smallCups.length
    // console.log(fullCups)

    if(fullCups === 0){
        percentage.style.visibility = 'hidden'
        percentage.style.height = 0
    }else{
        percentage.style.visibility = 'visible'
        percentage.style.height = `${fullCups / totalCups * 330}px`
        percentage.innerText = `${fullCups / totalCups * 100}%`
    }

    if(fullCups === totalCups){
        remained.style.visibility = 'hidden'
        remained.style.height = 0
    }else{
        remained.style.visibility = 'visible'
        liters.innerText = `${2-(250 * fullCups / 1000)}L to go!`
    }
}