var p = [];

function setup() {
  v = new mVector(1, 2);
  createCanvas(1280, 720);
  background(0, 200, 255);
  noStroke();
  fill(255);
  p.push(new Particle(width / 2, height / 2));
}

function draw() {
  background(0, 200, 255);
  for (var i = 0; i < p.length; i++) {
    var n = new mVector(random(-0.1, 0.1), random(-0.1, 0.1));
    p[i].applyForce(n);
    p[i].update();
    p[i].show();
  }
}


// particle class
function Particle(x, y) {
  this.x = x;
  this.y = y;
  this.t = random(10, 100);
  this.c = 0;
  this.loc = new mVector(this.x, this.y);
  this.vel = new mVector(random(-1, 1), random(-1, 1));
  this.acc = new mVector(0, 0);

  this.show = function() {
    fill(255);
    noStroke();
    ellipse(this.loc.x, this.loc.y, 10, 10);
  };

  this.update = function() {
    this.c++;
    this.vel.mAdd(this.acc);
    //this.vel.limit(1);
    this.loc.mAdd(this.vel);
    this.acc.mMult(0);
    if (this.c > this.t) {
      if (p.length < 200) {
        // delete this particle and add two new ones
        index = p.indexOf(this);
        p.splice(index, 1);
        p.push(new Particle(this.loc.x, this.loc.y));
        p.push(new Particle(this.loc.x, this.loc.y));
      }
    }
  };

  this.applyForce = function(f) {
    this.acc.mAdd(f);
  };
}


// tiny vector class (can't use P5's vector class, because this is going to be a Max MSP script)
function mVector(x, y) {
  this.x = x;
  this.y = y;

  this.mAdd = function(v) {
    this.x += v.x;
    this.y += v.y;
  }
  this.mSub = function(v) {
    this.x -= v.x;
    this.y -= v.y;
  }
  this.mMult = function(n) {
    this.x *= n;
    this.y *= n;
  }
  this.mMag = function() {
    a = Math.pow(this.x, 2);
    b = Math.pow(this.y, 2);
    return Math.sqrt(a + b);
  }
  this.mNorm = function() {
    this.tempMag = this.mMag();
    this.x /= this.tempMag;
    this.y /= this.tempMag;
  }
}
