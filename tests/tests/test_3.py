from task3.tests.pages.Main import Main
from task3.tests.pages.Elements import ElementsPage
from task3.tests.pages.Web_Tables import WebTables
from task3.framework.utils import Utils
import pytest

@pytest.mark.parametrize('user',Utils().read_data_json('test_data.json','Users'))
def test_3(conditions,user):
    main_page = Main()
    assert main_page.is_validate_main_page_open(), "Главная страница не загрузилась"
    main_page.elements_click()
    elements_page = ElementsPage()
    elements_page.button_web_tables_click()
    assert elements_page.is_validate_form_web_tables(), "Кнопка 'Web Tables' не нажата "
    web_tables_page = WebTables()
    data = user
    count_user_before = web_tables_page.read_count_users()
    web_tables_page.button_add_click()
    assert web_tables_page.is_validate_form_registragion(), "Форма регистрации нового пользователя не загрузилась"
    web_tables_page.data_entry(data)
    web_tables_page.button_submit_click()
    new_user = web_tables_page.read_value_last_user()
    assert web_tables_page.is_validate_add_user(data,new_user), 'Новый пользователь не добавлен'
    web_tables_page.delete_new_user()
    count_user_after = web_tables_page.read_count_users()
    assert count_user_before == count_user_after, 'Новый пользователь не удален из таблицы'
