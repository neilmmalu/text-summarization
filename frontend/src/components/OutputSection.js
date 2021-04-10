import axios from "axios";
import React from "react";
import "../css/OutputSection.css";

class OutputSection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      summarizedText: "",
      transactionID: "",
    };
  }

  componentDidUpdate(prevProps) {
    if (this.props.tID !== prevProps.tID) {
      this.setState({ transactionID: this.props.tID }, () => {
        console.log(this.state.transactionID);
        axios
          .get("http://localhost:8000/api/texts/" + this.state.transactionID)
          .then((res) => {
            this.setState({ summarizedText: res.data.summarizedText });
          });
      });
    }
  }

  render() {
    //random comment

    return (
      <div className="ui container">
        <div className="ui one column grid">
          <div className="row">
            <h3>Processed Text</h3>
          </div>
          <div className="row">
            <textarea
              readOnly
              className="textarea"
              value={this.state.summarizedText}
            ></textarea>
          </div>
        </div>
      </div>
    );
  }
}

export default OutputSection;
