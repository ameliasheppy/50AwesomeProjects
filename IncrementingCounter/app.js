const counters = document.querySelectorAll('.counter')
//above gives us a node list which is similar to an array, now let's loop through it with a for each. 
//a forEach takes in a function.
counters.forEach(counter => {
    counter.innerText = "0"

    const updateCounter = () => {
        //we want to change our data-target to a number. Could wrap it in a Number constructor or do the below.
         const target = +counter.getAttribute('data-target') 
         console.log(typeof target)

         const c = +counter.innerText
         const increment = target / 200

         console.log(increment)
         if(c < target){
            counter.innerText = `${Math.ceil(c + increment)}`
            setTimeout(updateCounter, 1)
         }else{
            counter.innerText = target
         }
    }
    updateCounter()
})