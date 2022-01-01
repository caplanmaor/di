class Creature{
  constructor(name, legCount, headCount) {
    
  }
}

////////////////////

// TV
class Tv {
  constructor(tvBrand, tvChannel = 1, tvVolume = 50) {
    this.tvBrand = tvBrand;
    this.tvChannel = tvChannel;
    this.tvVolume = tvVolume;
  }

  increaseVolume() {
    this.tvVolume += 1;
  }
}

let lgTv = new Tv("LG");
lgTv.increaseVolume();
console.log(lgTv);

// Smart TV

class SmartTv extends Tv {
  constructor(tvBrand) {
    super();
    this.tvBrand = tvBrand;
  }

  increaseVolume() {
    this.tvVolume < 100 && this.tvVolume > 0 ? (this.tvVolume += 10) : null;
  }

  setChannel(targetChannel) {
    let previousChannel = this.tvChannel;
    this.tvChannel = targetChannel;
    this.tvChannel < 0 || this.tvChannel > 50
      ? (this.tvChannel = previousChannel)
      : null;
  }
}

let smartLgTv = new SmartTv("Smart-LG");
smartLgTv.increaseVolume();
smartLgTv.increaseVolume();
smartLgTv.increaseVolume();
smartLgTv.increaseVolume();
smartLgTv.setChannel(5);
smartLgTv.setChannel(-3);
console.log(smartLgTv);
