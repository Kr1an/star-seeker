import React from 'react'

export default class Images extends React.Component {
  render() {
    const photoBlue = `url(${this.props.photoBlue})`;
    const photoYellow = `url(${this.props.photoYellow})`;
    const blueStyles = {backgroundImage: photoBlue}
    const yellowStyles = {backgroundImage: photoYellow}
    const elem = (
      <div className="images">
        <div style={blueStyles} className="images__image"></div>
        <div style={yellowStyles} className="images__image images__image--right"></div>
      </div>
    )
    return elem
  }
}
