from time import sleep

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_goods_has_add_to_basket_button(browser):
    browser.get(link)
    sleep(30)  # sleep для проверки правильности инициализации браузера
    add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_basket, 'Кнопка добавления товара отсутвует'
