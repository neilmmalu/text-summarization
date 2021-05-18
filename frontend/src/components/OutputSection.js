import axios from "axios";
import React from "react";
import "../css/OutputSection.css";

class OutputSection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      summarizedText: "",
      transactionID: "",
      scores: "",
    };
  }

  componentDidUpdate(prevProps) {
    if (this.props.tID !== prevProps.tID) {
      this.setState({ transactionID: this.props.tID }, () => {
        console.log(this.state.transactionID);

        if (window.location.origin === "http://localhost:3000") {
          axios.defaults.baseURL = "http://localhost:8000";
        } else {
          axios.defaults.baseURL = window.location.origin + ":8000";
        }

        axios.get("/api/texts/" + this.state.transactionID).then((res) => {
          this.setState({
            summarizedText: res.data.summarizedText,
            scores: JSON.parse(res.data.scores),
          });
        });
      });
    }
  }

  render() {
    //random comment
    console.log(typeof(this.state.scores))
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
          <div className="row">
            <span>{this.state.scores}</span>
          </div>
        </div>
      </div>
    );
  }
}

export default OutputSection;
