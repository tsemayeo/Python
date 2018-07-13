var shakes = ["https://hips.hearstapps.com/del.h-cdn.co/assets/15/24/1433964595-delish-milkshakes-new-mint.jpg", "https://www.awesomeinventions.com/wp-content/uploads/2016/07/milkshake-recipes-oreo.jpg", "https://i.pinimg.com/originals/bb/d4/4a/bbd44ae08d89bc766dd5d921c5c49fd5.jpg", "http://del.h-cdn.co/assets/15/24/480x480/gallery-1433964673-delish-milkshakes-new-peanut.jpg", "https://hips.hearstapps.com/del.h-cdn.co/assets/15/24/1433964636-delish-milkshakes-new-smores.jpg", "https://i.imgur.com/fWduORk.jpg"];

var image = document.getElementsById("shakes");

function rotate (foodType) {
  var i = 0;
  for (i < foodType.length) {
    image.src = foodType[i];
    i++;
    if (i == foodType.length-1) {
      i = 0;
    }
  }
}

function press(foodType) {
    image.addEventListener("click", rotate(foodType));
}
