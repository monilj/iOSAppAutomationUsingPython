from Automation_for_Native_application.iOS_capability import des_cap_calendar_app

ios_driver = des_cap_calendar_app()
ios_driver.find_element_by_id('Compose').click()
message_field = ios_driver.find_element_by_name('messageBodyField')
message_field.click()
message_field.send_keys('hello there')
ios_driver.hide_keyboard()