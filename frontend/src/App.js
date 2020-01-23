import React from 'react';
import { Route } from 'react-router-dom';
import { Home, Detail, Write } from './pages';

class App extends React.Component{
  render(){
    return(
      <div>
        <Route exact path="/" component={Home}/>
        <Route exact path="/Detail/:id" component={Detail}/>
        <Route exact path="/Write" component={Write}/>
      </div>
    )
  }
}

export default App;
