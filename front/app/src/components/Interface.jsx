import React from 'react'
import ImageButtons from './ImageButtons.jsx'
import Images from './Images.jsx'
import Separator from './Separator.jsx'
import Data from './Data.jsx'


export default class Interface extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      yellowFilterFilePath: null,
      blueFilterFilePath: null,
      statistic: [
        {
          header: 'statistic1',
          content: 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        },
        {
          header: 'statistic2',
          content: 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        },
        {
          header: 'statistic3',
          content: 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        }
      ]
    }
    this.yellowButtonHandler = this.yellowButtonHandler.bind(this);
    this.blueButtonHandler = this.blueButtonHandler.bind(this);

  }
  yellowButtonHandler(e) {
    this.setState({yellowFilterFilePath: e.target.files[0].path})
    this.props.onContentChange(false)
  }
  blueButtonHandler(e) {
    this.setState({blueFilterFilePath: e.target.files[0].path})
    this.props.onContentChange(false)
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
