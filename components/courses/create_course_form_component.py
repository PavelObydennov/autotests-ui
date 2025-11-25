from components.base_component import BaseComponent
from playwright.sync_api import Page,expect
from elements.textarea import TextArea
from elements.input import Input
import allure


class CreateCourseFormComponent(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.create_course_title_input = Input(page,'create-course-form-title-input', 'Create course' )
        self.create_course_estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Create course')
        self.create_course_description_textarea = TextArea(page,'create-course-form-description-input', 'Description')

        self.create_course_max_score_input = Input(page,'create-course-form-max-score-input','Min score')
        self.create_course_min_score_input = Input(page,'create-course-form-min-score-input', 'Max_score')

    @allure.step("Fill create course form")
    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_title_input.fill(title)
        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_description_textarea.fill(description)
        self.create_course_max_score_input.fill(max_score)
        self.create_course_min_score_input.fill(min_score)

    @allure.step("Check visible create course form '{title}' ")
    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_have_value(title)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_have_value(estimated_time)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_have_value(description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_have_value(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_have_value(min_score)
