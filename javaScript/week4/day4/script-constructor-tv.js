function Tv(tvBrand, tvChannel = 1, tvVolume = 50) {
  this.brand = tvBrand;
  this.channel = tvChannel;
  this.volume = tvVolume;

  this.increaseVolume = function () {
    this.volume += 1;
  };
  this.decreaseVolume = function () {
    this.volume -= 1;
  };
}

let lgTv = new Tv("LG");
console.log(lgTv);

lgTv.increaseVolume();

console.log(lgTv);
