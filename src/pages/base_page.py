from playwright.sync_api import Page, expect

class FriendListPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, base_url):
        self.page.goto(f"{base_url}#/friends")

    def get_all_friends(self):
        return self.page.locator("li.list-group-item")

    def expect_friends_visible(self):
        friends = self.get_all_friends()
        expect(friends).to_have_count_above(0)

def add_friend(page, name, email, go_to_baseurl=False, base_url=None):
    if go_to_baseurl:
        page.goto(base_url)
    friend_button = page.get_by_role("link", name='Ny vän')
    friend_button.click()
    page.locator('section.form input[type="text"]').nth(0).fill(name)
    page.locator('section.form input[type="text"]').nth(1).fill(email)
    page.get_by_role('button', name='Spara').click()

