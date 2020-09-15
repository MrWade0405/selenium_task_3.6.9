link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# import time

def test_language(browser):
    browser.get(link)
    # to check the correctness of work
    # time.sleep(30)
    button = None
	
    try:
        button = browser.find_element_by_css_selector(".btn-add-to-basket")
    except ZeroDivisionError:
        # don't need to be processed here, 'assert' is called below
        pass

    assert button != None, "The button for adding an item to the shopping cart doesn't exist"