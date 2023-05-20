const jokeEl = document.getElementById('joke')
const jokeBtn = document.getElementById('jokeBtn')

//tie our button clicks to the func to get a new joke
//we can check in our network tab to see our reqs
//when we make a fetch, we see the req and res
jokeBtn.addEventListener('click', generateJoke)

generateJoke()

// USING ASYNC/AWAIT
async function generateJoke() {
  const config = {
    headers: {
      Accept: 'application/json',
    },
  }

  const res = await fetch('https://icanhazdadjoke.com', config)

  const data = await res.json()

  //instead of .thens we are setting what we get back into a var and then setting it in our code
  jokeEl.innerHTML = data.joke
}

//we can put our header info a config so that things look nice!
//we will be getting a promise back, so use .then
//.then says when this is finished, then this will happen
// USING .then()
// function generateJoke() {
//   const config = {
//     headers: {
//       Accept: 'application/json',
//     },
//   }

//   fetch('https://icanhazdadjoke.com', config)
//     .then((res) => res.json())
//     .then((data) => {
//       jokeEl.innerHTML = data.joke
//     })
// }