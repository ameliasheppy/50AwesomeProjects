// import { Component } from "react";

// class Card extends Component{
//     render(){
//         const {id, name, email} = this.props.monster;
        
//         return (
//         <div className="card-container" key={id}>
//         <img 
//         alt={`a cartoon drawing of ${name}`} 
//         src={`https://robohash.org/${id}?set=set2&size=180x180`}/>
//         <h2>{name}</h2>
//         <p>{email}</p>
//     </div>
//         )
//     }
// }
import React from "react";

const Card = ({monster}) => {
    const {id, name, email} = monster;
    return (
    <div className="card-container" key={id}>
        <img alt={`a cartoon drawing of ${name}`} 
        src={`https://robohash.org/${id}?set=set2&size=180x180`}/>
        <h2>{name}</h2>
        <p>{email}</p>
        </div>
    )
}

export default Card