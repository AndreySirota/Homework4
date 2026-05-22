"""Инструкция по совершению покупки на сайте https://www.saucedemo.com/:

Экран логина:

1. Открыть страницу https://www.saucedemo.com/
2. Ввести имя пользователя
   Поле: <input id="user-name" ...>
   CSS-селектор: #user-name
   XPath: //input[@id="user-name"]
3. Ввести пароль
   Поле: <input id="password" ...>
   CSS-селектор: #password
   XPath: //input[@id="password"]
4. Нажать кнопку "Login"
   Кнопка: <input id="login-button" ...>
   CSS-селектор: #login-button
   XPath: //input[@id="login-button"]

Экран главной страницы:

5. Добавить товар в корзину
   Кнопка "Add to cart": <button id="add-to-cart-sauce-labs-backpack" ...>
   CSS-селектор: #add-to-cart-sauce-labs-backpack
   XPath: //button[@id="add-to-cart-sauce-labs-backpack"]

Переход в корзину:

6. Кликнуть по иконке корзины в шапке сайта
   Ссылка: <a class="shopping_cart_link" ...>
   CSS-селектор: .shopping_cart_link
   XPath: //a[@class="shopping_cart_link"]

Экран корзины:

7. Нажать кнопку "Checkout"
   Кнопка: <button id="checkout" ...>
   CSS-селектор: #checkout
   XPath: //button[@id="checkout"]

Экран ввода данных пользователя:

8. Заполнение полей формы
   First Name: <input id="first-name" ...>
   CSS-селектор: #first-name
   XPath: //input[@id="first-name"]
   Last Name: <input id="last-name" ...>
   CSS-селектор: #last-name
   XPath: //input[@id="last-name"]
   Zip/Postal Code: <input id="postal-code" ...>
   CSS-селектор: #postal-code
   XPath: //input[@id="postal-code"]

9. Нажать кнопку "Continue"
   Кнопка: <input id="continue" ...>
   CSS-селектор: #continue
   XPath: //input[@id="continue"]

Экран подтверждения заказа:

10. Проверить информацию о заказе и нажать кнопку "Finish"
    Кнопка: <button id="finish" ...>
    CSS-селектор: #finish
    XPath: //button[@id="finish"]

Экран успешного завершения:

11. Убедиться в успешном оформлении заказа
    Заголовок: <h2 class="complete-header" ...>Thank you for your order!</h2>
    CSS-селектор: .complete-header
    XPath: //h2[@class="complete-header"]

Возвращение на экран главной страницы:

12. Нажать на кнопку "Back Home"
    Кнопка: <button id="back-to-products" ...>
    CSS-селектор: #back-to-products
    XPath: //button[@id="back-to-products"] """
