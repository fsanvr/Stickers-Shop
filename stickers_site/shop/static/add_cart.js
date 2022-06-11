document.onsubmit = event => {

    if (event.target.name == 'add_cart'){
    event.preventDefault();

    var XHR = new XMLHttpRequest();
    XHR.open('POST', '/add_cart/');

    var formData = new FormData(event.target);
    XHR.send(formData);
    }
}