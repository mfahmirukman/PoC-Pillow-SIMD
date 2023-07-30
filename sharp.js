var sharp = require("sharp");

var startTime = new Date();
sharp.cache(false);

sharp("Membeli-Properti.jpg")
  .resize(618, 412, {
    kernel: sharp.kernel.lanczos3,
    fit: 'contain',
    // position: 'right top',
    // background: { r: 255, g: 255, b: 255, alpha: 0.5 }
  })
  .toFile("sharp-output.jpg")
  .then((data) => {
    var endTime = new Date();
    var dif = endTime.getTime() - startTime.getTime();
    console.log(dif);
    console.log(startTime);
    console.log(endTime);
  });
