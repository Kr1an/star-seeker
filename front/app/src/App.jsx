import React, {Component} from 'react'
import {render} from 'react-dom'
import {} from './styles/global.css'
import Logo from './components/Logo.jsx'

import ProjectInfo from './components/ProjectInfo.jsx'

export default class App extends Component {
    // constructor(props) {
    //   super(props);
    //   this.state = {
    //     isContentPartEmpty: true
    //   }
    // }
    render() {
      // let isInfoActive = this.state.isContentPartEmpty;
      return (
        <ProjectInfo />
      )
    }
}
