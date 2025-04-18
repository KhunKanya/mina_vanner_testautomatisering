from behave import when, then, given
from playwright.sync_api import expect
from pages.base_page import add_friend


@given(u'användaren är på kontaktsidan')
def step_given_start_page(context):
    context.page.goto(context.base_url)

@when(u'användaren lägger till Kanya Suwannajan med epost')
def step_when_enter_name(context):
    add_friend(context.page, 'Kanya suwannajan', "kanya.beyon@gmail.com")

@then(u'användaren kan ser "Kanya suwannajan" i kontaklistan')
def step_then_verify_contact(context):
    context.page.get_by_role('link', name='Vänlista').click()
    element = context.page.locator('section.friends').get_by_text('Kanya suwannajan')
    expect(element).to_be_visible(timeout=100)

@then(u'användaren kan ser "kanya.beyon@gmail.com" i kontaklistan')
def step_then_verify_email(context):
    element = context.page.locator('section.friends').get_by_text('kanya.beyon@gmail.com')
    expect(element).to_be_visible(timeout=100)


#  """ -----  Försök att lägga till kontakt med saknade fält ----"""

@given(u'användaren är på kontaktsidan2')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)
    friend_button = context.page.get_by_role("link", name='Ny vän')
    friend_button.click()


@given(u'användaren lämnar "Namn" och "E-post" tomma')
def step_given_not_do_anything(context):
    pass


@when(u'användaren klickar på "Spara"2')
def step_when_click_save(context):
    context.result = context.page.get_by_role('button', name='Spara')


@then(u'användaren kunde inte klickar på "Spara"')
def step_then_button_disabled(context):
    expect(context.result).to_be_disabled()
