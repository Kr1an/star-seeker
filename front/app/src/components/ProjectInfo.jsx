import React from 'react'
import {shell} from 'electron'
import Link from './Link.jsx'

export default class ProjectInfo extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      paragraphs:[
        (<p>If you are trying to estimate how old the star cluster is
            this app is exactly what you need. Provide two photo of same
            sky area in blue and yellow filters and get different
            characteristics of the cluster easily.</p>),
        (<p>Pay attention to some importent rules: photo should be done
            very close to each other, and the same star cluster. Algo
            overview Algo overwiew Algo overwiew Algo overwiew
            Algo overwiew Algo overwiew Algo overwiew.</p>),
        (<p>Check out the docs and source code on&nbsp;
            <Link to='https://github.com/Kr1an/star-seaker'>github</Link>.<br />
            Feel free to leave comments,&nbsp;
            <Link to='https://github.com/Kr1an/star-seaker/issues'>issues, bugs, ideas</Link>.<br />
            Contact us via email:&nbsp;
            <Link to='kr1an@hotmail.com'>kr1an@hotmail.com</Link>.</p>)
      ]
    };
  }
  render() {
    let paragraphs = this.state.paragraphs;
    return (
      <div>
        <div className="logo">
            <h1>Star-Seeker</h1>
        </div>
        {paragraphs}
      </div>
    );
  }
}
