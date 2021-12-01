let uploaders = document.getElementsByClassName("img-uploader");

for (let i = 0; i < uploaders.length; i++) {
  let uploader = uploaders[i].getElementsByClassName("img-uploader-input")[0];

  uploader.addEventListener("change", function (event) {
    let inputFile = uploader.files;
    uploaders[i]
      .getElementsByClassName("img-uploader-wrapper")[0]
      .classList.remove("error");

    if (inputFile.length && inputFile[0].name.match(/.(jpg|jpeg|png)$/i)) {
      uploaders[i].getElementsByClassName(
        "img-uploader-preview"
      )[0].src = window.URL.createObjectURL(inputFile[0]);
    } else if (inputFile.length > 0) {
      uploaders[i]
        .getElementsByClassName("img-uploader-wrapper")[0]
        .classList.add("error");
    }
  });
}

var animateButton = function(e) {
  e.preventDefault;
  //reset animation
  e.target.classList.remove('animate');

  e.target.classList.add('animate');
  setTimeout(function(){
    e.target.classList.remove('animate');
  },2000);
};

var bubblyButtons = document.getElementsByClassName("bubbly-button");

for (var i = 0; i < bubblyButtons.length; i++) {
  bubblyButtons[i].addEventListener('click', animateButton, false);
}

