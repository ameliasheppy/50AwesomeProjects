import './App.css';
import { useEffect, useState } from 'react';
  // import { Component } from 'react';
import CardList from './components/card-list/Card-list.component';
import SearchBar from './components/search-box/Search';

//      ANY FETCH CALL IS A SIDE EFFECT, SO 
//                FOR ANY FETCH CALL, USE THE USEEFFECT HOOK

//IF A FUNC COMP IS HAVING BUGS, re-rendering continually, check your state vars. 
//Remember that a func comp runs completely, top to bottom on each render. 
//Read carefully to see what is happening in the func!!
//Check your state vars!!
//

//lets see how a func comp is diff from a class comp
//in a class comp, when there were mounting and update cycles, render would get run when props changed or state updated.
//BUT THE ONLY CODE THAT WOULD RUN IS WHAT IS INSIDE THE RENDER METHOD
//Think of your entire func comp as a render method.
//when R decided a comp needs to re-render, it runs the whole thing from top to bottom
//when props change, the whole func runs
//when state changes, it also re-runs the whole comp


const App = () => {
  //useState allows us to encapsulate a val
  //into useState, pass the inital val that we want it to be
  //Here that is an empty str
  //sometimes it is a num
  //sometimes it is an empty arr
  //
  const [searchField, setSearchField] = useState('cat')
  //we need an arr of monsters. It will be empty at first.
  //but if we fetch to an API to get our users/monsters, that is a different arr from mem, so it would keep fetching and rendering forever
  //the equality check fails user === user nope! It's a different arr in mem
  //so it would re render constantly in a continual, circular fetch
  //how do we stop the circular fetch? 
  //a sideEffect! The useEffect hook. 
  //How do we generate side effects from functional components?
  //useEffect!
  //a side effect is some behavior that we trigger from our func that effect something outside the scope of the func
  const [monsters, setMonsters] = useState([])
  //uh oh, the CL runs twice for every keystroke
  //every time the event changes, the state updates bc we are typing new chars or removing chars from a str
  console.log(searchField);
  //or a destructured version. 
  //look at what the CL's give back. one gives str, one gives obj, they give back whatever type you gave them
  console.log({searchField})

  //we are going to get our monsters using a fetch
  //since we are using a fetch, and changing our state, we need to use a useEffect, with an empty dependency arr to make sure that it only renders on page load, not 800+ times
  //useEffect takes two args
  //a CB func
  //an arr of dependencies
  //what is the first arg, the CB func, in the {}?
  //the code of the effect that we want to happen in the func comp
  //the second, empty arr, contains deps, 
  useEffect(() => {}, [])

  //to set the searchField state to what the user types in, we pass 
  // setSearchField(searchFieldString) searchFieldString into our setter func
  const onSearchChange = (event) => {
    const searchFieldString = event.target.value.toLocaleLowerCase()
       setSearchField(searchFieldString)
  }

  const filteredMonsters = monsters.filter((monster) => {
      return monster.name.toLocaleLowerCase().includes(searchField)
  })

  return(
    <div className='App'>
      <h1 className='app-title'>Monsters Crew</h1>
      <SearchBar 
      onChangeHandler={onSearchChange} 
      placeholder="Find a friend"
      className="monsters-search-box"/>
      <CardList monsters={filteredMonsters} />
    </div>
  )
}


export default App;

//here is an impure func. Bc this func changes something that is outside of it's scope
// let c = 3
// const funcB = (a,b) => {
//   c = a + b
//   return a * b
// }                    see! we are editing c, which is outside the scope!


  // class App extends Component {
  //   constructor(){
  //     super()

  //     this.state = {
  //       monsters: [],
  //       searchString: ''
  //     }
  //     // console.log('1----Constructor')
  //   }

  //   componentDidMount(){
  //     //use native fetch
  //     // console.log('3----ComponentDidMount')
  //     fetch('https://jsonplaceholder.typicode.com/users')
  //     //returns a promise, which we then pass right away to users
  //     .then((response) => response.json())
  //     .then((users) => this.setState(() =>{
  //       return {monsters: users}
  //     },
  //     () => {
  //       console.log(this.state)
  //     }))
  //   }

  //   //monsters is an array of obj, let's filter it! Filter will check the return of each CB to see if the bool is true from filter. 
  //   //includes will also return a bool. 
  //   //so filter gives us a bool
  //   //also, includes gives us a bool
  //   //bools everywhere!
  //   //filteredMonsters gives us a new array. Why do we want this? Add or remove from an arr, it's still same in mem
  //   //we want to use non-modifying methods, and create a new arr, not modify the current one that we are on
  //   //keep things immutable!
  //   //if you must modify an arr, make a new one with the mod in it!
  //   //we need to set the monsters to the new filtered versionc

  //   onSearchChange = (event) => {
  //     const searchField = event.target.value.toLocaleLowerCase()
  //     this.setState(() => {
  //     return { searchField}
  //     })
  //   }
  //   render() {
  //     const { monsters, searchField} = this.state
  //     const { onSearchChange} = this
  //     // console.log('2----Render!')
  //     const filteredMonsters = monsters.filter((monster) => {
  //       return monster.name.toLocaleLowerCase().includes(searchField)
  //   })

  //     return(
  //       <div className='App'>
  //         <h1 className='app-title'>Monsters Crew</h1>
  //         <SearchBar onChangeHandler={onSearchChange} placeholder="Find a friend"
  //         className="monsters-search-box"/>
  //         <CardList monsters={filteredMonsters} />
  //       </div>
  //     )
  //   }
  // }



//Here is an old school class based version:
// import { Component } from 'react';
// class App extends Component {
//   //state is info that only this component is aware of and can modify
//   //super is called on the constructor method and any of the other classes you are extending from.
//   constructor(){
//     //call the constructor method on the comp with super()!!!!
//     super();

//     //instantiate the state:
//     this.state = {
//       //this.state is alwats a JSON obj
//       name: {firstName: "Jesse", lastName: "Stanley"},
//       company: "ZTM"
//     }
//   }
//   //render is specifically telling the Component what to render
//   render() {
//     return (
//       <div className="App">
//        <h1>Hey there, {this.state.name.firstName} {this.state.name.lastName}. Do you like {this.state.company}</h1>
//        <button onClick={() => {
//         this.setState((state, props) => {
//           return {
//             name: { firstName: "Amy", lastName: "Stanley"}
//           }
//         }, () => {
//           //the below will auto run ONLY after the state is fully updated. So we don't have to ask if our code will updte
//           console.log(this.state)
//         })
//        }}>Change Name</button>
//       </div>
//     )
//   }
// }


//every time react needs to update the dom, it runs the render method. the onchange in our input is anonymous, it doesn't belong anywhere.
//so JS will create the func for us, then throw it away. 
//so every time render runs, the anony func RUNS then gets thrown away
//thats a problem!
//we are never really updating the func. we are only updating the event val
//js knows that the event is not controlled by the func.
//every time we re-init the func, our app performance takes a hit
//lots of funcs === slow, bad performance
//in class components, put the func up and out in a callback func in the component, not in the render
//that will prevent it from re-running the anony func on all renders. 
//also, to look better, stop using this. all of the time. Do ES6 destructuring


//a component is something that governs the UI
//we can tie together the func'ly of the UI with the actual UI/visual representation
//components tie together the visual pieces of code into something that we can use

//We want for our components to be as reusable as possible. Make them as generic as we can so that they are Lego blocks with a single bit of responsibility that we can snap together
//