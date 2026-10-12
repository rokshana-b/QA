from playwright.sync_api import Page, expect


class Homepage:
    def __init__(self, page: Page) -> None:
        self.page = page

        # Replace these example selectors with ones from your demo application.
        self.new_submission_button = page.get_by_role(
            "button",
            name="New submission",
        )

    def open(self, base_url: str) -> None:
        self.page.goto(base_url)

    def start_new_submission(self) -> None:
        self.new_submission_button.click()

    def expect_loaded(self) -> None:
        expect(self.page).to_have_title("Sample Project 1")