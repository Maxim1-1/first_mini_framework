from task3.tests.pages.Alerts_Frame import AlertsPage
from task3.tests.pages.Nested_Frame import Nested_frame
from task3.tests.pages.Frames import Frames
from task3.tests.pages.Main import Main

def test_2(conditions):
    main_page = Main()
    assert main_page.is_validate_main_page_open(), "Главная страница не загрузилась"
    main_page.alerts_windows_frame_click()
    alert_page = AlertsPage()
    alert_page.button_nested_frame_click()
    nested_frame = Nested_frame()
    assert nested_frame.is_validate_form_nested_frames(), 'Кнопка Nested Frames не появилась'
    nested_frame.switch_to_parent_frame()
    assert nested_frame.is_validate_parent_frame(), 'Parent Frame отсутствует'
    nested_frame.switch_to_child_frame()
    assert nested_frame.is_validate_child_frame(), 'Child Frame отсутствует'
    nested_frame.exiting_the_frame()
    nested_frame.element_frames_click()
    frames = Frames()
    assert frames.is_validate_form_frames(), 'Кнопка Frames не появилась'
    frames.switch_to_top_frame()
    frames.get_text_top_frame()
    frames.exiting_the_frame()
    frames.switch_to_bottom_frame()
    assert frames.get_text_top_frame() == frames.get_text_bottom_frame(),'Надпись из верхнего фрейма не совпадает с надпись из нижнего фрейма'