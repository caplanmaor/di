import React from "react";
import data from "../data.json";

class PostList extends React.Component {
  render() {
    return (
      <div>
        {data.map((item, i) => {
          return (
            <div>
              <h3 key={item.id}>{item.title}</h3>
              <h5 key={item.id}>{item.content}</h5>
            </div>
          );
        })}
      </div>
    );
  }
}

export default PostList;
