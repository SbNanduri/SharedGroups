from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # Initializes the chrome browser

driver.get('https://www.messenger.com/')

email = driver.find_element_by_id("email")  # Finds the email field
password = driver.find_element_by_id("pass")    # Finds the password field

email.send_keys('fake_email@fake.com')
password.send_keys('hunter2')

password.send_keys(Keys.ENTER)  # Presses enter so you can be logged in

contact_name = "Contact"    # The contact you want to find

# Initializes the group lengths used to splice the groups list
groups_length = 0
old_groups_length = 0

while True:
	#Renews the groups list so that it will include all of the contacts that are loaded
	groups = driver.find_elements_by_class_name('_1ht6')
	groups_length = len(groups)

	# Makes sure that the list continues from where it left off in the previous loop
	groups = groups[old_groups_length:groups_length+1]

	if groups_length == old_groups_length:
		# If these are the same length then there are no more contacts to search
		# Therefore, the program can be ended
		break

	old_groups_length = groups_length

	for group in groups:
		group.click()   # Causes the current group to be focused on

		# Gets the list of all of the members in this group
		members = driver.find_elements_by_class_name('_364g')

		for member in members:  # Loops through until the given contact is found
			if member.text == contact_name:
				print(group.text)

	time.sleep(2)   # Gives time for more contacts to load

driver.close()  # Closes the program after it is finished