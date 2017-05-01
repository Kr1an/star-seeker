import React      from 'react'
import {render}   from 'react-dom'
import {}         from './styles/global.css'
import Interface    from './components/Interface.jsx'
import ProjectInfo from './components/ProjectInfo.jsx'

export default class App extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        isContentEmpty: true
      }
      this.onContentChange = this.onContentChange.bind(this)
    }

    onContentChange(value){
      if(typeof value === undefined)
        return
      console.log("isContentEmpty: <" + this.state.isContentEmpty + ">")
      this.setState({isContentEmpty: value})
    }

    render() {
      let isInfoActive = this.state.isContentEmpty;
      return (
        <div className="body-placer">
          {isInfoActive && <ProjectInfo />}
          <Interface onContentChange={this.onContentChange} />

        </div>

      );
    }
}
