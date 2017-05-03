import React from 'react'
import ImageButtons from './ImageButtons.jsx'
import Images from './Images.jsx'
import Separator from './Separator.jsx'
import Data from './Data.jsx'
import path from 'path'
import {} from 'process'


export default class Interface extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      yellowFilterFilePath: null,
      blueFilterFilePath: null,
      statistic: []
    }

    this.controllerPath = path.join(process.cwd(), '..', 'back', 'controller.py')

    this.yellowButtonHandler = this.yellowButtonHandler.bind(this);
    this.blueButtonHandler = this.blueButtonHandler.bind(this);

  }
  calculateStatistic(){
    var spawn = require('child_process').spawn,
        py    = spawn('python', [this.controllerPath]),
        data = {
          blueFilterFilePath: this.state.blueFilterFilePath,
          yellowFilterFilePath: this.state.yellowFilterFilePath
        },
        dataString = '',
        pypath = this.controllerPath,
        path = require('path');

    py.stdout.on('data', function(data){
      dataString = data;

    });
    py.stdout.on('end', function(){
      console.log(dataString.toString())
      console.log(JSON.parse(dataString.toString()))
      if(dataString === '')
        return
      else {
        this.setState({statistic: JSON.parse(dataString.toString())})
        return
      }
    }.bind(this));
    py.stdin.write(JSON.stringify(data));
    py.stdin.end();
  }
  yellowButtonHandler(e) {
    this.state.yellowFilterFilePath = e.target.files[0].path
    this.setState({yellowFilterFilePath: e.target.files[0].path})
    this.props.onContentChange(false)
    this.calculateStatistic()
  }
  blueButtonHandler(e) {
    this.state.blueFilterFilePath = e.target.files[0].path
    this.setState({blueFilterFilePath: e.target.files[0].path})
    this.props.onContentChange(false)
    this.calculateStatistic()
  }

  render() {
    return (
      <div className='container'>
        <ImageButtons
          yellowButtonHandler={this.yellowButtonHandler}
          blueButtonHandler={this.blueButtonHandler}
        />
        <Images
          photoYellow={this.state.yellowFilterFilePath}
          photoBlue={this.state.blueFilterFilePath}
        />
        <Separator />
        <Data
          statistic={this.state.statistic}
        />
      </div>
    )
  }
}
