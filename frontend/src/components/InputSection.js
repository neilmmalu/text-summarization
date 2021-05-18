import React from "react";
import "../css/InputSection.css";
import axios from "axios";

import { Dropdown } from "semantic-ui-react";
import "semantic-ui-css/semantic.min.css";

class InputSection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      text: "",
      file: null,
      error: true,
      allOptions: [
        {
          key: "similarityMatrix",
          text: "Extractive: Similarity Matrix",
          value: "Extractive: Similarity Matrix",
        },
        {
          key: "nltkSummarizer",
          text: "Extractive: NLTK",
          value: "Extractive: NLTK",
        },
        {
          key: "lsaSummarizer",
          text: "Extractive: LSA",
          value: "Extractive: LSA",
        },
        {
          key: "klSummarizer",
          text: "Extractive: KLSum",
          value: "Extractive: KLSum",
        },
        {
          key: "luhnSummarizer",
          text: "Extractive: Luhn",
          value: "Extractive: Luhn",
        },
        {
          key: "lexRankSummarizer",
          text: "Extractive: Lex Rank",
          value: "Extractive: Lex Rank",
        },
      ],
      option: "",
    };
  }

  onProcess = () => {
    this.setState({ error: false });
    let formData = new FormData();
    if (this.state.text !== "") {
      formData.append("inputText", this.state.text);
    }

    if (this.state.file !== null) {
      formData.append("upload", this.state.file, this.state.file?.name);
    }

    axios.post("http://localhost:8000/api/texts/", formData).then((res) => {
      this.props.update(res.data.transactionID);
    });
  };

  onFileChange = (e) => {
    this.setState({ file: e.target.files[0] }, () => {
      if (this.state.file === null && this.state.text === "") {
        this.setState({ error: true });
      } else if (this.state.file !== null && this.state.text !== "") {
        this.setState({ error: true });
      } else {
        this.setState({ error: false });
      }
    });
  };

  handleTextChange = (e) => {
    this.setState({ text: e.target.value }, () => {
      if (this.state.file === null && this.state.text === "") {
        this.setState({ error: true });
      } else if (this.state.file !== null && this.state.text !== "") {
        this.setState({ error: true });
      } else {
        this.setState({ error: false });
      }
    });
  };

  summarizeOps = (e, data) => {
    console.log(data.value);
    console.log(data.key);
    this.setState({ option: data.value });
  };

  render() {
    return (
      <div className="ui container">
        <div className="ui one column grid">
          <div className="row">
            <Dropdown
              placeholder="Select Type of Summarizer"
              selection
              options={this.state.allOptions}
              value={this.state.option}
              onChange={this.summarizeOps}
            />
          </div>
          <div className="row">
            <h3>Enter Text Here</h3>
          </div>
          <div className="row">
            <textarea
              onChange={this.handleTextChange}
              className="textarea"
              value={this.state.text}
            ></textarea>
          </div>

          <div className="row">
            <button
              className="fluid ui teal button"
              onClick={this.onProcess}
              disabled={this.state.error}
            >
              Process
            </button>
          </div>
        </div>
        <div className="row">
          <div className="ui horizontal divider">Or</div>
        </div>
        <div className="row">
          <div className="ui action input">
            <input type="file" onChange={this.onFileChange} />
            <button
              className="ui button"
              onClick={this.onProcess}
              disabled={this.state.error}
            >
              Process
            </button>
          </div>
        </div>
        {this.state.error && (
          <div className="row">Either add text or file, not both.</div>
        )}
      </div>
    );
  }
}

export default InputSection;
