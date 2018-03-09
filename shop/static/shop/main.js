const SERVER_URL = 'http://localhost:8000/'
const POST_DETAIL_ENDPOINT = 'cart/add/'
const DELETE_DETAIL_ENDPOINT = 'cart/detail/delete/'
const UPDATE_DETAIL_ENDPOINT = 'cart/detail/update/'
const GET_CART_ENDPOINT = 'cart/get/'
const UPDATE_CART_ENDPOINT = 'cart/update/'

const HTTP_METHODS = {
    GET: 'GET',
    POST: 'POST',
    PUT: 'PUT',
    DELETE: 'DELETE'
};

window.onload = function () {
    const xhr = new XMLHttpRequest();
    const CSRF_TOKEN = document.getElementById('token').innerHTML;

    var cart = document.getElementById('cart');

    function attachListeners() {
        var productButtons = document.querySelectorAll('.product-btn');

        if (productButtons.length > 0) {
            productButtons.forEach(btn => {
                btn.onclick = function () {//ONCLICK WORKS EVENTHOU btn IS OF TYPE Element
                    //let data = new FormData();
                    //ata.append('product_id', parseInt(btn.dataset.id));

                    xhr.open(HTTP_METHODS.POST, `${SERVER_URL}${POST_DETAIL_ENDPOINT}`);
                    xhr.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
                    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                    xhr.responseType = 'json';
                    xhr.onload = function () {
                        console.log(xhr.response);
                        if (xhr.response.error) {
                            alert(xhr.response.error);
                        }
                        else {
                            reloadCart();
                        }
                    };
                    xhr.send(JSON.stringify({ product_id: parseInt(btn.dataset.id) }));
                    //ITEM ALREADY IN CART
                };
            });
        }

        var cartFavoriteButtons = document.querySelectorAll('.cart-item-action.favorite');

        if (cartFavoriteButtons.length > 0) {

            cartFavoriteButtons.forEach(heart => {
                heart.onclick = function () {
                    heart.classList.toggle('active');
                };
            });
        }

        var cartDeleteButtons = document.querySelectorAll('.cart-item-action.cross');

        if (cartDeleteButtons.length > 0) {
            cartDeleteButtons.forEach(cross => {
                cross.onclick = function () {

                    if (confirm('Are you sure you want to delete this item?')) {
                        let data = { detail_id: parseInt(cross.parentElement.parentElement.parentElement.dataset.id) };

                        xhr.open(HTTP_METHODS.POST, SERVER_URL + DELETE_DETAIL_ENDPOINT);
                        xhr.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
                        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                        xhr.onload = function () {
                            console.log(xhr.response);
                            reloadCart();
                        };
                        xhr.send(JSON.stringify(data));
                    }
                };
            });
        }

        var minusButtons = document.querySelectorAll('.minus');

        if (minusButtons.length > 0) {
            minusButtons.forEach(minus => {
                minus.onclick = function () {
                    let currentQuantity = parseInt(minus.nextElementSibling.innerHTML);
                    if (currentQuantity <= 1) {
                        alert('Quantity cannot be less than 1');
                    }
                    else {
                        let data = {
                            detail_id: parseInt(minus.parentElement.parentElement.parentElement.dataset.id),
                            quantity: --currentQuantity
                        };

                        xhr.open(HTTP_METHODS.POST, SERVER_URL + UPDATE_DETAIL_ENDPOINT);
                        xhr.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
                        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                        xhr.onload = function () {
                            console.log(xhr.response);
                            reloadCart();
                        };
                        xhr.send(JSON.stringify(data));
                    }
                };
            });
        }

        var plusButtons = document.querySelectorAll('.plus');

        if (plusButtons.length > 0) {
            plusButtons.forEach(plus => {
                plus.onclick = function () {
                    let currentQuantity = parseInt(plus.previousElementSibling.innerHTML);
                    let detail_id = plus.parentElement.parentElement.parentElement.dataset.id;
                    let data = { detail_id: detail_id, quantity: ++currentQuantity };//prepend the ++ so that it works for assignation
                    xhr.open(HTTP_METHODS.POST, SERVER_URL + UPDATE_DETAIL_ENDPOINT);
                    xhr.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
                    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                    xhr.onload = function () {
                        console.log(xhr.response);
                        reloadCart();
                    };
                    xhr.send(JSON.stringify(data));
                }
            });
        }

        var orderButton = document.getElementById('order-button');

        if (orderButton) {
            orderButton.onclick = function () {
                let orderId = document.getElementById('order').dataset.id;
                if (orderId) {
                    let data = { order_id: orderId, order_state: false };
                    xhr.open(HTTP_METHODS.POST, SERVER_URL + UPDATE_CART_ENDPOINT);
                    xhr.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
                    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                    xhr.onload = function () {
                        console.log(xhr.response);
                        reloadCart();
                    };
                    xhr.send(JSON.stringify(data));
                }
            }
        }
    }

    /*let cross = cartActions.item(0);
        let heart = cartActions.item(1);

        cross.addEventListener('click', function(){
            alert('Cart is full');
        });*/

    /*(cross as HTMLElement).onclick = function(){
        alert('es6 working')
    }*/

    function reloadCart() {//THE RELOAD METHOD USES ITS OWN XHR, IT SEEMS USING THE CONST ONE CAUSES ISSUES
        let xhr = new XMLHttpRequest();
        xhr.open(HTTP_METHODS.POST, SERVER_URL + GET_CART_ENDPOINT);
        xhr.setRequestHeader('X-CSRFToken', CSRF_TOKEN);
        xhr.onload = function () {
            console.log(xhr.response);
            cart.innerHTML = xhr.response;
            attachListeners();
        };
        xhr.send();
    }

    attachListeners();
};