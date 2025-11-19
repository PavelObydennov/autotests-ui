import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    # Проверка наличия заголовка "Create course"
    create_course_page.create_course_toolbar_view.check_visible()
    # Проверка, что кнопка создания курса недоступна для нажатия
    create_course_page.create_course_toolbar_view.check_visible()
    # Проверка, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.create_course_form_component.check_visible_create_course_form(title='',estimated_time='',description='',max_score='0',min_score='0')
    # Проверка наличие заголовка "Exercises" и кнопки
    create_course_page.create_course_exercise_toolbar_view.check_visible()
    # Загрузка изображение для превью курса
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    # Проверка, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    # Заполнение формы создания курса
    create_course_page.create_course_form_component.fill_create_course_form(title = "Playwright",estimated_time = "2 weeks",description = "Playwright",max_score = "100",min_score = "10")
    # Нажатие на кнопку создания курса
    create_course_page.create_course_toolbar_view.click_create_course_button()
    # Проверка наличия заголовка "Courses"
    courses_list_page.toolbar_view.check_visible()
    # Проверка корректность отображаемых данных на карточке курса
    courses_list_page.course_view.check_visible(index=0,title='Playwright',estimated_time = "2 weeks",max_score = "100",min_score = "10")



@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar_view.check_visible()









