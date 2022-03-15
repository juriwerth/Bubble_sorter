arr = [];
newArray = true;

function draw() {
  createCanvas(windowWidth/2, windowHeight/2);
  if (newArray == true) {
    for (i = 0; i < width; i++) {
      arr.push(random(height));
    }
    newArray = false;
  }
  background(255);
  for (j = 0; j <= width; j++) {
    stroke(255, 0, 255-arr[j]);
    line(j, height, j, height-arr[j]);
  }
  console.log(arr[0], arr[1]);
  for (l = 0; l < width; l++) {
    if (arr[l] > arr[l+1]) {
      temp = arr[l];
      arr[l] = arr[l+1];
      arr[l+1] = temp;
    }
  }
}
