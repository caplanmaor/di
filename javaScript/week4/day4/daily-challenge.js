class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }

  watch() {
    return `${this.uploader} watched all ${this.time} of ${this.title}`;
  }
}

let video1 = new Video("The Office", "Maor", "7 weeks");
console.log(video1.watch());
let video2 = new Video("Zombieland", "bibi", "9 seasons");
console.log(video2.watch());
//object
