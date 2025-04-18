from behave import when, then, given
from playwright.sync_api import expect
#from pages.base.page import Page

""" Visa lista med alla mina vänner """
@given(u'användaren är på Vänlista sidan " https://forverkliga.se/JavaScript/my-contacts/#/friends "')
def step_given_start_page(context):
    # Navigera till startsidan (Vänlista)
    context.page.goto(f"{context.base_url}#/friends")


@then(u'användare kan se alla vänner på Vänlista sidan')
def step_user_can_see_page(context):
   expect(context.page).to_have_title("Mina vänner")



""" ---------- Ändra uppgifter för en vän ----------- """""" Lyckad ändring """

@given(u'användaren ser vänlista som vill ändra information')
def step_view_friend_list_for_editing(context):
    context.page.goto(f"{context.base_url}#/friends")
    #expect(context.page.locator("h1")).to_have_text("Mina vänner"))

@when(u'jag klickar på "Ändra"-knappen för den kontakten')
def step_click_edit_button(context):
    edit_button = context.page.locator('a[role="button"][href="#/edit/1"]')
    edit_button.click(timeout=500)

@when(u'jag ändra namn eller e-post och klicka på "Spara"')
def step_edit_info_and_save(context):
     context.page.locator('section.form input[type="text"]').nth(0).fill("kanya")
     context.page.locator('section.form input[type="text"]').nth(1).fill("Kanya@gmail.com")
    # Klicka på spara-knappen
     context.page.click('button:has-text("Spara")')

@then(u'användaren ska se kontaktens uppdateras i listan.')
def step_verify_updated_contact_in_list(context):
    context.page.get_by_role('link', name='Vänlista').click()
    element = context.page.locator('section.friends').get_by_text("kanya")
    expect(element).to_have_count(2,timeout=100)


 #""" ------- Felmeddelande vid tomma fält ----------- """

@given(u'användaren ser vänlista som vill ändra information2')
def step_view_friend_list(context):
    context.page.goto(f"{context.base_url}#/friends")


@when(u'jag klickar på "Ändra"-knappen för den kontakten2')
def step_click_edit(context):
    edit_button = context.page.locator('a[role="button"][href="#/edit/1"]')
    edit_button.click(timeout=500)


@when(u'jag rederar namn eller e-post')
def step_delete_name(context):
    context.page.locator('section.form input[type="text"]').nth(0).fill("")

@then(u'kan inte klicka spara')
def step_click_save_button2(context):
    context.result = context.page.get_by_role('button', name='Spara')
    expect(context.result).to_be_disabled()

