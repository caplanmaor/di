class Dog {
  constructor(name) {
    this.name = name;
  }
}

class Labrador extends Dog {
  constructor(name, size) {
    super(name);
    this.size = size;
  }
}

let rex = new Labrador("rex", "big");
console.log(rex);

/////////////////////////////////

class Animal {
  constructor(color, type, name) {
    this.animalColor = color;
    this.animalType = type;
    this.animalName = name;
  }
  present() {
    return (
      "The " + this.animalColor + " " + this.animalType + " " + this.animalName
    );
  }
}

class Mamal extends Animal {
  constructor(color, type, name, voice) {
    super(color, type, name);
    this.sound = voice;
  }
  show() {
    return this.present() + " sounds like this: " + this.sound;
  }
}

let myanimal = new Mamal("Brown", "Cow", "Elizabeth", "Mooo");
document.body.innerHTML = myanimal.show();

// class Animal {
//   constructor(name, type, color) {
//     this.name = name;
//     this.type = type;
//     this.color = color;
//   }
// }

// class Mamal extends Animal {
//   constructor(name, type, color, voice) {
//     super(name, type, color);
//     this.voice = voice;
//     this.name = name;
//   }
//   sound(voice) {
//     return name` the ` + this.color + this.type + ` sound like this : ` + voice;
//   }
// }

// let myCow = new Mamal("jasmine", "cow", "brown");
// console.log(myCow.sound("moooo"));
