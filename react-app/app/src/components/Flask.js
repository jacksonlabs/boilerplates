
import React, { Component } from 'react';
import axios from 'axios';

class Flask extends Component {

  state = {
    flaskEnv: null,
    mode: null,
    debugMode: null,
  }

  componentDidMount() {
    console.log(process.env.REACT_APP_API_ENDPOINT + '/env');
    axios.get(process.env.REACT_APP_API_ENDPOINT + '/env')
      .then(response => {
        console.log(response);
        console.log(response.data);

        this.setState({ 
          flaskEnv: response.data.FLASK_ENV,
          mode: response.data.MODE,
          debugMode: response.data.DEBUG_MODE,
        });
      })
  }

  render() {
    return (
      <div>
        <small>The REACT_APP_API_ENDPOINT is <code>{process.env.REACT_APP_API_ENDPOINT}</code></small>
        <p><b>Flask Server Info</b></p>
        <table>
          <tr><td><small>FLASK_ENV: <code>{this.state.flaskEnv}</code></small></td></tr>
          <tr><td><small>MODE: <code>{this.state.mode}</code></small></td></tr>
          <tr><td><small>DEBUG_MODE: <code>{this.state.debugMode}</code></small></td></tr>
        </table>
      </div>
    );
  }

}

export default Flask;