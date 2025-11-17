
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    # Проверка наличия заголовка "Create course"
    create_course_page.check_visible_create_course_title()
    # Проверка, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()
    # Проверка, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()
    # Проверка, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.check_visible_image_upload_view()
    # Проверка, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(title='',estimated_time='',description='',max_score='0',min_score='0')
    # Проверка наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()
    # Проверка наличия кнопки создания задания
    create_course_page.check_visible_create_exercise_button()
    # Проверка, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()
    # Загрузка изображение для превью курса
    create_course_page.upload_preview_image('./testdata/files/image.png')
    # Проверка, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view()
    # Заполнение формы создания курса
    create_course_page.fill_create_course_form(title = "Playwright",estimated_time = "2 weeks",description = "Playwright",max_score = "100",min_score = "10")
    # Нажатие на кнопку создания курса
    create_course_page.click_create_course_button()
    # Проверка наличия заголовка "Courses"
    courses_list_page.check_visible_courses_title()
    # Проверка наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    # Проверка корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(index=0,title='Playwright',estimated_time = "2 weeks",max_score = "100",min_score = "10")
