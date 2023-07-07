import { Component } from "react";

import './searchBox.css'
class SearchBar extends Component{
    render(){
        return <div>
                <input className={`search-box ${this.props.className}`}
                type='search' 
                placeholder={this.props.placeholder} 
                onChange={this.props.onChangeHandler}/>
        </div>
    }
}

export default SearchBar

//we need this search bar to run in App
//why? We are sorting down through our monsters based on this search field.

//So App utilizes the search field val. We need the str stored in state in App.
//onSearchChange updates the state in App.js searchField.