from behave import when, then, given
from playwright.sync_api import expect
from pages.base_page import add_friend

@given(u'änvandaren är i websidan på vänsidan')
def step_given_go_to_homepage(context):
    context.page.goto(context.base_url)


@given(u'Är vän med Tom Bombadil')
def step_given_friends_with_tom(context):
    add_friend(context.page, "Tom Bombadil", "tom@middle-earth.com")


@when(u'Användaren tar bort Tom')
def step_when_remove_tom(context):
    context.page.get_by_role('link', name='Vänlista').click()
    section = context.page.locator('.friend', has_text="Tom Bombadil")
    section.get_by_role("button", name="Ta bort").click()


@then(u'Tom är inte längre kompis')
def step_verify_result(context):
    element = context.page.locator('section.friends').get_by_text('Tom Bombadil')
    expect(element).to_have_count(0, timeout=100)
