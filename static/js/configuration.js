

// left menu hidd-show {
var menuAppear = document.body.querySelector('#menu_appear');
function menuClick() {
  $('#menu').toggleClass('grid_left');
  $('#menu').toggleClass('grid_left_show');
  menuAppear.innerHTML = (menuAppear.innerHTML == '&gt;' ? '&lt;':'&gt;');  // change value #menu_appear '>' =|= '<'
  $('#slider').css('display', 'none');
};
// left menu hidd-show }

// eventform {
let orderForm = document.body.querySelector("#orderForm");
let openOrderFormBtn = document.body.querySelector("#openOrderFormBtn");

function openOrderForm() {
  orderForm.style.display = 'block';
  openOrderFormBtn.style.display = 'none';
}
function closeOrderForm() {
  orderForm.style.display = 'none';
  openOrderFormBtn.style.display = 'block';
}
// } eventform

// slider {
var staticPages = ['mainPage', 'ist_podz', 'cave_quest',];
var slider = document.body.querySelector('#slider');
var init = document.body.querySelectorAll('.init');
var slideClose = document.body.querySelector('.modalClose');
var img = document.body.querySelector('#slideIn img');
var sl_left = document.body.querySelector('#sl_left');
var sl_button_left = document.body.querySelector('#sl_button_left');
var sl_right = document.body.querySelector('#sl_right');
var sl_button_right = document.body.querySelector('#sl_button_right');
var pageID = document.body.querySelector('.content').firstElementChild.getAttribute('id');
var photoCount = document.body.querySelectorAll('.content img').length;
var photoNumber;
var photoNumber_nextSimb;
var URL_prefix;

console.log(photoCount)

  // slider start {
for(let fig=0; fig<=init.length-1; fig++) {
  init[fig].onclick = function(event) {
    var target = event.target;
    if (target.tagName == 'IMG') {
      slider.style.display = 'block';

//   static/page_photo/cave_quest/full/full_1.jpg
//   static/page_photo/cave_quest/prev/prev_1.jpg

//   media/article_photos/100_2013/full_1.jpg
//   media/CACHE/images/article_photos/100_2013/full_1/f2c00886a153320ba777e825f2c858af.jpg
      if (staticPages.includes(pageID)){
        URL_prefix = target.getAttribute('src').split('page_photo')[0] + 'page_photo/' +pageID+ '/full/full_';
        photoNumber = target.getAttribute('src').slice(-6,-5);
        photoNumber_nextSimb = target.getAttribute('src').slice(-5,-4);
        console.log('1-й символ: ' + photoNumber);
        console.log('2-й символ: ' + photoNumber_nextSimb);
        if (!isNaN(photoNumber)){
            photoNumber += photoNumber_nextSimb;
        }
        if (isNaN(photoNumber)){
            photoNumber = photoNumber_nextSimb;
        }
      }
      else {
        URL_prefix = target.getAttribute('src').split('CACHE')[0] + 'articles_photo/' + pageID + '/full_';
        photoNumber = target.getAttribute('src').split('/')[6][5];
        photoNumber_nextSimb = target.getAttribute('src').split('/')[6][6];
        console.log('1-й символ: ' + photoNumber);
        console.log('2-й символ: ' + photoNumber_nextSimb);
        if (!isNaN(photoNumber_nextSimb)){
            photoNumber += photoNumber_nextSimb;
        }
      }

      // URL_prefix = target.getAttribute('src').split('page_photo')[0];
      img.src = URL_prefix + photoNumber+ '.jpg';
      console.log('стартовое фото № ' + photoNumber);
      console.log('URL_prefix: ' + URL_prefix);
      console.log('URL_sep: ' + target.getAttribute('src').split('/'));
      console.log(img.src);
    }
  }
};

  // slider start }

function adaptiveSL() {  // sliderBox size = loadedImage size
  slider.style.height = '90%';
  slider.style.width = '90%';
  slider.style.height = img.height + 'px';
  slider.style.width = img.width + 'px';
  console.log('высота картинки: ' + img.height);
  console.log('ширина картинки: ' + img.width);
};

  // flipping slider {

sl_left.onclick = function() {
  photoNumber--;
  console.log('переход на фото: ' + photoNumber);
  if (photoNumber < 1) {
    photoNumber = photoCount;
  }
  img.src = URL_prefix + photoNumber + '.jpg';
}
sl_right.onclick = function() {
  photoNumber++;
  console.log('переход на фото: ' + photoNumber);
  if (photoNumber > photoCount) {
    photoNumber = 1;
  }
  img.src = URL_prefix + photoNumber + '.jpg';
};
  // flipping slider }

slideClose.onclick = function() { // close slider
  slider.style.display = 'none';
};


  // slider decor {
function opacL_over(){
  sl_button_left.style.opacity = '0.6';
}
function opacL_out(){
  sl_button_left.style.opacity = '0.1';
}

function opacR_over(){
  sl_button_right.style.opacity = '0.6';
}
function opacR_out(){
  sl_button_right.style.opacity = '0.1';
}
  // slider decor }
// slider }
