
# 🌟 **Udemy Course Scraper** 🌟  
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org) [![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)](https://www.selenium.dev/) [![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

🚀 A Python-based scraper that extracts **Udemy courses** dynamically rendered with JavaScript. It utilizes **Selenium** for scraping and processes the data into a clean, organized DataFrame with **Pandas** for further analysis.

---

## 🖼️ **Preview**  
![Udemy Courses Banner](https://via.placeholder.com/800x200.png?text=Udemy+Course+Scraper)

---

## 📜 **Features**  
- Scrape Udemy courses dynamically using **Selenium**.  
- Extract key details like **Name**, **Description**, **Instructor**, **Rating**, **Price**, and more.  
- Save raw data to a `.txt` file for further processing.  
- Clean and organize data into a neat **Pandas DataFrame**.  

---

## 🛠️ **Tech Stack**  
- **Language**: Python  
- **Libraries**:  
  - `selenium` for web scraping dynamic content.  
  - `pandas` and `numpy` for data manipulation.  
- **Data**: Exported as `.txt` and cleaned to create a DataFrame.  

---

## 🚀 **Setup Instructions**  

### 1. Clone the Repository  
```bash  
git clone https://github.com/yourusername/udemy-course-scraper.git  
cd udemy-course-scraper  
```  

### 2. Install Dependencies  
To install the required libraries, run the following command:  
```bash
pip install selenium pandas numpy
```

### 3. Run the Scraper  
Follow these steps to execute the scraper:

1. **Set up ChromeDriver**:  
   - Download the appropriate [ChromeDriver](https://chromedriver.chromium.org/downloads) version for your Chrome browser.  

2. **Run the Script**:  
   Execute the Python script:  
   ```bash  
   python scraper.py  
   ```

3. **Data Output**:  
   The raw scraped data will be saved in a file named `data.txt`.  

---

## 📝 **Code Explanation**

### **Scraping the Data**  
The following code uses **Selenium** to scrape dynamically rendered content:  

```python
from selenium import webdriver  
from selenium.webdriver.common.by import By  

driver = webdriver.Chrome()  
driver.get("https://www.udemy.com/courses/development/data-science/")  

# Wait for the page to load completely  
driver.implicitly_wait(10)  

# Locate the course list container and extract child elements  
parent = driver.find_element(By.CLASS_NAME, 'course-list_container__yXli8')  
children = parent.find_elements(By.CLASS_NAME, 'course-list_card-layout-container__F2SfZ')  

# Save the extracted data into a text file  
with open("data.txt", "w", encoding="utf-8") as file:  
    for child in children:  
        element = child.find_element(By.CLASS_NAME, "popper_popper__jZgEv").text  
        file.write(element + "/\n================================/\n")  

driver.quit()
```

- **`implicitly_wait(10)`**: Ensures all elements are loaded before proceeding.  
- **Find Elements**: Identifies the container of courses and iterates over child elements to extract data.  
- **Save Data**: Writes the raw scraped text to `data.txt`.  

---

### **Cleaning and Organizing Data**  
The following script processes and cleans the scraped data to produce a structured DataFrame:  

```python
import pandas as pd
import numpy as np

courses_list = []

with open("data.txt") as file:
    courses_list = file.read().split("================================")
    
courses_list = [x.split("\n") for x in courses_list]
del courses_list[-1]

data = []
for course in courses_list:
    element = []
    del course[-1]
    
    if course[-1] == "Bestseller":
            course[-1] = "Yes"
    else:
        course.append(np.nan)
    for piece in course:
        if isinstance(piece,str) and (piece in ("Instructor:", "Instructors:", "Current Price", "Original Price", "Current price", "Original price", "") or "Rating:" in piece):
            continue
        
        element.append(piece)
    data.append([element[0],*element[2:]])
    
columns = ["Name", "Description", "Instructor", "Rating", "Number of Ratings",  
           "Total Hours", "Number of Lectures", "Level", "Current Price",  
           "Original Price", "Bestseller"]

courses = pd.DataFrame(data, columns=columns)
print(courses)
```

- **Raw Data Reading**: Loads the `data.txt` file and splits it by the delimiter `================================`.  
- **Cleaning**: Filters out unnecessary details and fills missing values.  
- **DataFrame Creation**: Converts the cleaned data into a well-organized Pandas DataFrame.  

---

## 📊 **Sample Output**  

| Name                  | Description | Instructor     | Rating | Number of Ratings | Total Hours | Number of Lectures | Level     | Current Price | Original Price | Bestseller |  
|-----------------------|-------------|----------------|--------|-------------------|-------------|--------------------|-----------|---------------|----------------|------------|  
| Python for Data Science | Learn Python | John Doe       | 4.7    | 15,000            | 10          | 80                 | Beginner  | $19.99        | $99.99         | Yes        |  

---

## 🤝 **Contributing**  
Contributions are welcome! Here's how you can help:  
1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m "Add new feature"`).  
4. Push to your branch (`git push origin feature-name`).  
5. Open a pull request.  

---

## 📧 **Contact**  
Have questions or suggestions? Feel free to reach out!  
- **GitHub**: [SaifAyman23](https://github.com/SaifAyman23)  
- **Email**: your.saifayman3021@gmail.com@example.com  

---