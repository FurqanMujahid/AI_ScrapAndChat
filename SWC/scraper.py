import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


driver_path = "chromedriver.exe"  

def check_static_site(url):
    """Check if the website is static by fetching it with requests and checking for content."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find_all('p')  
            if content and len(content) > 0:
                return soup 
        return None  
    except requests.exceptions.RequestException as e:
        print(f"Requests failed: {e}")
        return None

def scrape_dynamic_site(url):
    """Scrape the website using Selenium if it's dynamic (JavaScript-rendered content)."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--disable-software-rasterizer")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(url)
        time.sleep(5)  

        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
   
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        
        sop = soup.get_text(separator=" ")
        return sop
    finally:
        driver.quit()

def scrape_website(url):
    """Main function to scrape a website. Determines if the website is static or dynamic."""
    print(f"Scraping {url}...")

 
    soup = check_static_site(url)
    
    if soup:
        print("Static website detected. Scraping using requests and BeautifulSoup.")
        scraped_data = soup.get_text(separator=" ")  
    else:
        print("Dynamic website detected. Scraping using Selenium.")
        scraped_data = scrape_dynamic_site(url)

    if scraped_data and isinstance(scraped_data, str):
     
        return " ".join(scraped_data.split())
    else:
        return "Failed to scrape the website."


