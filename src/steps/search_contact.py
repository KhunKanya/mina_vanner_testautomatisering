from behave import when, then, given
from playwright.sync_api import expect


@given(u'att kontaktlistan är synlig')
def step_contact_list_visible(context):
    context.page.goto(context.base_url)
    context.page.get_by_role('link', name='Vänlista').click()


@when(u'jag skriver "pICARD" i sökfältet')
def step_search_for_contact_by_name(context):
    search_input = context.page.locator('input[type="text"]').nth(0)
    search_input.fill("pICARD")


@then(u'ska kontakten med namnet "Jean-Luc Picard" visas')
def step_verify_name_in_result(context):
    result = context.page.locator('section.friends')
    expect(result).to_have_count(1, timeout=100)

@given(u'att kontaktlistan är synlig2')
def step_contact_list_visible(context):
    context.page.goto(context.base_url)
    context.page.get_by_role('link', name='Vänlista').click()


@when(u'jag skriver "STARFLEET.COM" i sökfältet')
def step_search_for_contact_by_email(context):
    search_input = context.page.locator('input[type="text"]').nth(0)
    search_input.fill("STARFLEET.COM")

@then(u'ska kontakten med e-post "captain.picard@starfleet.com" visas')
def step_verify_email_in_result(context):
    element = context.page.locator('section.friends').get_by_text('Jean-Luc Picard')
    expect(element).to_be_visible(timeout=100)
