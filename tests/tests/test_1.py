from task3.tests.pages.Alerts_Frame import AlertsPage
from task3.tests.pages.Main import Main


def test_1(conditions):
    main_page = Main()
    assert main_page.is_validate_main_page_open(), "Главная страница не загрузилась"
    main_page.alerts_windows_frame_click()
    alerts = AlertsPage()
    alerts.element_alerts_click()
    assert alerts.is_validate_form_alert(), 'Форма Alerts не появилась'
    alerts.button_to_see_alert_click()
    assert alerts.is_validate_button_to_see(), 'Кнопка "Click Button to see alert" не нажата'
    alerts.click_alert_OK()
    alerts.button_confirm_click()
    assert alerts.is_validate_button_confirm(), 'Кнопка "Confirm box will appear" не нажата'
    alerts.click_alert_OK()
    assert alerts.is_validate_confirm_text(), 'Надпись не появилась "You selected Ok'
    alerts.button_prompt_click()
    assert alerts.is_validate_button_prompt(), 'Кнопка "Prompt box will appear" не нажата'
    alerts.input_text_in_alert()
    alerts.click_alert_OK()
    assert alerts.text in alerts.button_prompt_text(),"Появившийся текст не соответствует введенному в алерт 'Prompt box will appear'"
