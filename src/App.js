  import './App.css';
  import { Component } from 'react';

class App extends Component {
  //state is info that only this component is aware of and can modify
  //super is called on the constructor method and any of the other classes you are extending from.
  constructor(){
    //call the constructor method on the comp with super()!!!!
    super();

    //instantiate the state:
    this.state = {
      //this.state is alwats a JSON obj
      name: {firstName: "Jesse", lastName: "Stanley"},
      company: "ZTM"
    }
  }
  //render is specifically telling the Component what to render
  render() {
    return (
      <div className="App">
       <h1>Hey there, {this.state.name.firstName} {this.state.name.lastName}. Do you like {this.state.company}</h1>
       <button onClick={() => {
        this.setState((state, props) => {
          return {
            name: { firstName: "Amy", lastName: "Stanley"}
          }
        }, () => {
          console.log(this.state)
        })
       }}>Change Name</button>
      </div>
    )
  }
}

export default App;
