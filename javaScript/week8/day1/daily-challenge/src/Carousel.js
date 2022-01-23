import React, { Component } from "react";
import ReactDOM from "react-dom";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from "react-responsive-carousel";

class DemoCarousel extends Component {
  render() {
    return (
      <Carousel>
        <div>
          <img src="https://e3.365dm.com/21/07/2048x1152/skynews-grizzly-bear-file_5439223.jpg" />
          <p className="legend">Bear 1</p>
        </div>
        <div>
          <img src="http://cdn.cnn.com/cnnnext/dam/assets/211007211315-01-bear-encounters-restricted.jpg" />
          <p className="legend">Bear 2</p>
        </div>
        <div>
          <img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Image-w-cred-cap_-1200w-_-Brown-Bear-page_-brown-bear-in-fog_2_1.jpg" />
          <p className="legend">Bear 3</p>
        </div>
        <div>
          <img src="https://cdn.cnn.com/cnnnext/dam/assets/211125112643-bart-the-bear-ii-super-tease.jpg" />
          <p className="legend">Bear 4</p>
        </div>
      </Carousel>
    );
  }
}

export default DemoCarousel;

// Don't forget to include the css in your page

// Using webpack or parcel with a style loader
// import styles from 'react-responsive-carousel/lib/styles/carousel.min.css';

// Using html tag:
// <link rel="stylesheet" href="<NODE_MODULES_FOLDER>/react-responsive-carousel/lib/styles/carousel.min.css"/>
