import React from 'react'

export default class ImageButtons extends React.Component {
  render() {
    return (
      <div className="image-buttons">
          <div className="button">
            <label className="input-container">
              <input onChange={this.props.blueButtonHandler} type="file" className="image-buttons__input" />
              <span>Blue Filter</span>
            </label>
          </div>
          <div className="button button--right">
            <label className="input-container">
              <input onChange={this.props.yellowButtonHandler} type="file" className="image-buttons__input image-buttons__input--right" />
              <span>Yellow Filter</span>
            </label>
          </div>
        </div>
    )
  }
}
