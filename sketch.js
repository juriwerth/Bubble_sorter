function setup() {
  createCanvas(windowWidth/2, windowHeight/2);
  arr = [];
  for (i = 0; i < width; i++) {
    arr.push(random(height));
  }
}

function draw() {
  background(255);
  for (j = 0; j < width; j++) {
    stroke(255, 0, arr[j]);
    line(j, windowHeight, j, arr[j]);
  }
  for (l = 0; l < width; l++) {
    if (arr[l] < arr[l+1]) {
      temp = arr[l];
      arr[l] = arr[l+1];
      arr[l+1] = temp;
    }
  }
}
