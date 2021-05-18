import axios from "axios";
import React from "react";
import "../css/OutputSection.css";

class OutputSection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      summarizedText: "",
      transactionID: "",
      jaccard: null,
      cosine: null,
      gensim: null,
      rogue: null,
    };
  }

  componentDidUpdate(prevProps) {
    if (this.props.tID !== prevProps.tID) {
      this.setState({ transactionID: this.props.tID }, () => {
        // console.log(this.state.transactionID);

        if (window.location.origin === "http://localhost:3000") {
          axios.defaults.baseURL = "http://localhost:8000";
        } else {
          axios.defaults.baseURL = window.location.origin + ":8000";
        }
        axios.defaults.baseURL = "http://retr0-su-nlp.duckdns.org:8000";
        axios.get("/api/texts/" + this.state.transactionID).then((res) => {
          let obj = JSON.parse(res.data.scores);
          // console.log(obj);
          this.setState({
            summarizedText: res.data.summarizedText,
            jaccard: obj.Jaccard,
            cosine: obj.Cosine,
            gensim: obj.Gensim,
            rogue: obj.Rogue,
          });
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
          <div className="row">
            {this.state.jaccard && (
              <span>Jaccard Score: {this.state.jaccard}</span>
            )}
          </div>
          <div className="row">
            {this.state.cosine && (
              <span>Cosine Score: {this.state.cosine}</span>
            )}
          </div>
          <div className="row">
            {this.state.gensim && (
              <span>Gensim Score: {this.state.gensim}</span>
            )}
          </div>
          <div className="row">
            {this.state.rogue && <span>Rogue Score: {this.state.rogue}</span>}
          </div>
        </div>
      </div>
    );
  }
}

export default OutputSection;
