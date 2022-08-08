from task3.tests.pages.Alerts_Frame import AlertsPage
from task3.tests.pages.Main import Main
from task3.tests.pages.Browser_windows import BrowserWindows
from task3.tests.pages.Links import Links

def test_4(conditions):
    main_page = Main()
    assert main_page.is_validate_main_page_open(), "Главная страница не загрузилась"
    main_page.alerts_windows_frame_click()
    alert_page = AlertsPage()
    alert_page.button_browser_windows_click()
    assert alert_page.is_validate_browser_windows_form(), "Кнопка 'Browser Menu' не нажата "
    browser_windows_page = BrowserWindows()
    browser_windows_page.button_new_tab_click()
    browser_windows_page.switch_to_window_sample()
    assert browser_windows_page.is_validate_new_window_sample(), "Вкладка  sample не открыта"
    assert browser_windows_page.is_validate_text_on_sample_page(), "Текст на вкладке sample не 'sample page'"
    browser_windows_page.close_sample_window()
    browser_windows_page.switch_to_window_main()
    assert browser_windows_page.is_validate_browser_windows_form(), "Страница Browser Windows не открыта"
    browser_windows_page.button_elements_click()
    browser_windows_page.links_click()
    links_page = Links()
    assert links_page.are_validate_links_form(), "Страница с формой Links не открыта"
    links_page.link_home_click()
    links_page.switch_to_new_window()
    assert main_page.is_validate_main_page_open(), "Главная страница не загрузилась"
    links_page.switch_to_links_window()
    assert links_page.are_validate_links_form(), "Страница с формой Links не открыта"
