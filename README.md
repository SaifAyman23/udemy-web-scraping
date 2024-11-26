
# 🌟 **Udemy Course Scraper** 🌟  
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org) [![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)](https://www.selenium.dev/) [![License](https://img.shields.io/badge/License-Apache-red.svg)](LICENSE)

🚀 A Python-based scraper that extracts **Udemy courses** dynamically rendered with JavaScript. It utilizes **Selenium** for scraping and processes the data into a clean, organized DataFrame with **Pandas** for further analysis.

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

## Why not use `BeautifulSoap`?
`BeautifulSoup` is a great tool for parsing HTML and XML documents, but it's not the best choice for this task. Here's why:
*   `BeautifulSoup` is designed for parsing HTML and XML documents, not JSON data.
*   It's not optimized for parsing large JSON data, which can lead to performance issues. 

The courses in **Udemy** are renderd dynamically using `JavaScript`, so we can't use `BeautifulSoap`.

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

## 📝 **Code Overview**

The repository contains two main scripts:

1. **`scraper.py`**: Scrapes Udemy course data using Selenium.
2. **`cleaner.py`**: Cleans the scraped data and stores it in a structured Pandas DataFrame.

You can find these scripts in the repository and run them as follows:

```bash
python scraper.py  # Scrapes Udemy course data
python cleaner.py  # Processes and formats the scraped data
```

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
