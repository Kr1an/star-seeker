import React from 'react'

export default class Data extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    const headers = this.props.statistic.map((x, i)=>(<th key={i}>{x.header}</th>))
    const contents = this.props.statistic.map((x, i)=>(<td key={i} >{x.content}</td>))
    return (
      <div className="data">
        <div className="data-element">
          <table>
            <tbody>
              <tr>
                {headers}
              </tr>
              <tr>
                {contents}
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    )
  }
}
