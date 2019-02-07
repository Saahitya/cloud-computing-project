const app = document.getElementById('root');

const logo = document.createElement('img');
logo.src = './logo.png';

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(logo);
app.appendChild(container);

var request = new XMLHttpRequest();
request.open('GET', 'http://127.0.0.1:5000/api/category/list', true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);
  if (request.status >= 200 && request.status < 400) {
//    data.forEach(ctgry => {
    for (var key in data) {
      const card = document.createElement('div');
      card.setAttribute('class', 'card');
      uri_loc_on_click = 'category.html?name='+encodeURIComponent(key);
      console.log(uri_loc_on_click);
      console.log("location.href="+uri_loc_on_click);
      card.setAttribute( "location.href",uri_loc_on_click);
      const h1 = document.createElement('h1');
      h1.textContent = key;

      const p = document.createElement('p');
      //movie.description = data[key];
      p.textContent = `${data[key]}...`;

      container.appendChild(card);
      card.appendChild(h1);
      card.appendChild(p);
      card.append(logo.cloneNode(true));
    }
  } else {
    const errorMessage = document.createElement('marquee');
    errorMessage.textContent = `Gah, it's not working!`;
    app.appendChild(errorMessage);
  }
}

request.send();
