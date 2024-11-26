from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.udemy.com/courses/development/data-science/")

# Wait for the content to load
driver.implicitly_wait(10)

# Get the page source and search for data
page_source = driver.page_source

# To retrieve all the courses via a parent element
parent = driver.find_element(By.CLASS_NAME, 'course-list_container__yXli8')

# to retrieve all child elements
children = parent.find_elements(By.CLASS_NAME, 'course-list_card-layout-container__F2SfZ')

with open("data.txt", "w", encoding="utf-8") as file:
    for child in children:
        element = child.find_element(By.CLASS_NAME, "popper_popper__jZgEv").text
        file.write(element)
        file.write('\n')
        file.write("================================")
        file.write('\n')
    
driver.quit()