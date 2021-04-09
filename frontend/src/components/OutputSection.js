import React from "react";
import "../css/OutputSection.css";

class OutputSection extends React.Component {
  render() {
    //random comment

    return (
      <div className="ui container">
        <div className="ui one column grid">
          <div className="row">
            <h3>Processed Text</h3>
          </div>
          <div className="row">
            <textarea readOnly className="textarea"></textarea>
          </div>
        </div>
      </div>
    );
  }
}

export default OutputSection;
