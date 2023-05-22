const tagsEl = document.getElementById('tags')
const textarea = document.getElementById('textarea')

textarea.focus()

textarea.addEventListener('keyup', (e) =>{
    createTags(e.target.value)

    if(e.key === 'Enter'){
        setTimeout(() =>{
            e.target.value = ''
        }, 10)
        randomSelect()
    }

})

function createTags(input){ 
    //want to split on a comma and make an arr of whatever is on either side  of the comma
    //filter lets us return things based on a cond
    const tags = input.split(',').filter(tag => tag.trim() !== '').map(tag =>tag.trim())

    tagsEl.innerHTML = ''

    tags.forEach(tag =>{
        const tagEl = document.createElement('span')
        tagEl.classList.add('tag')
        tagEl.innerText = tag
        tagsEl.appendChild(tagEl)
    })
}

function randomSelect(){
    //the num of times to highlight each
    const times = 30
    const interval = setInterval(() => {
        const randomTag = pickRandomTag()
        highlightTag(randomTag)

        if(randomTag !== undefined){
            highlightTag(randomTag)

            setTimeout(() => {
                unHighlightTag(randomTag)
            }, 100)
        }
        }, 100);
        setInterval(() => {
            unHighlightTag(randomTag)
        }, 100);

        setTimeout(() => {
            clearInterval(interval)
    
            setTimeout(() => {
                const randomTag = pickRandomTag()
    
                highlightTag(randomTag)
            }, 100)
    
        }, times * 100)
    }


function pickRandomTag(){
    const tags = document.querySelectorAll('.tag')
    //all are now in an arr/node list
    return tags[Math.floor(Math.random() * tags.length)]
}

function highlightTag(tag){
    tag.classList.add('highlight')
}

function unHighlightTag(tag){
    tag.classList.remove('highlight')
}

