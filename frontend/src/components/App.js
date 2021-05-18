import React from "react";
import "../css/App.css";

import InputSection from "./InputSection";
import OutputSection from "./OutputSection";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      transactionID: "",
    };
  }

  updateTransactionID = (id) => {
    this.setState({ transactionID: id });
  };

  render() {
    return (
      <div
        className="ui fluid center aligned container"
        style={{
          backgroundColor: "cadetblue",
          height: "1000px",
          padding: "50px",
        }}
      >
        <h1 style={{ color: "white", fontSize: "50px", padding: "50px" }}>
          Text Summarization
        </h1>

        <div className="ui segment">
          <div className="ui two column very relaxed grid">
            <div className="column">
              <InputSection update={this.updateTransactionID} />
            </div>
            <div className="column">
              <OutputSection tID={this.state.transactionID} />
            </div>
          </div>
          <div className="ui vertical divider">
            <i className="massive sync alternate icon"></i>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
