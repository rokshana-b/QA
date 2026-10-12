from playwright.sync_api import Page, expect

from pages.homepage import Homepage


def test_user_can_start_a_new_submission(page: Page) -> None:
    homepage = Homepage(page)

    # Replace with the URL from this project's config.
    homepage.open("https://sample-project1.example.test")
    homepage.expect_loaded()
    homepage.start_new_submission()

    # Replace with the expected heading or page content.
    expect(
        page.get_by_role("heading", name="New submission")
    ).to_be_visible()