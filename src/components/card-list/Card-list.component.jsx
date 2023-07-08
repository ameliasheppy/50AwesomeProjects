// import { Component } from "react";
import './card-list.css'
import Card from '../cardyb/Card'

const CardList = ({monsters}) => {
    return (
    <div className="card-list">
        {monsters.map((monster) =>{
        return <Card monster={monster}/>
        })}
    </div>
    )
}

// class CardList extends Component{
//     render() {
//         const { monsters } = this.props
//         // console.log(this.props)

//         // console.log('Render from CardList');
//         return (
//         <div className="card-list">
//             {monsters.map((monster) =>{
//                 return (
//                     <Card monster={monster}/>
//             )})}
//         </div>
//         )
//     }
// }

export default CardList

//why does React render things twice? 
//It loads the initial page, runs back through and re-renders

//setState will trigger render. But they also re-render when props change
//how do the props change in the CardList? 
//at first, CardList gets an empty array passed to it, but then the fetch comes back from componentDidMount. So, R re-renders
//R is saying, we have new props, let's re-render!

//R renders top down
//App   ------->          CardList     ----------->       CardList2

//It works down the tree into the children and it's subsequent children

//REACT RENDERS ON MOUNT AND THEN IT RE-RENDERS WHENEVER PROPS CHANGE AND SET STATE GETS CALLED.

