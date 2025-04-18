from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)  # eller True om du inte vill se browsern

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = 'https://forverkliga.se/JavaScript/my-contacts'

def after_scenario(context, scenario):
    if hasattr(context, "page"):
        context.page.close()

def after_all(context):
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()
