from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def capture_screenshot(driver, filename):
    driver.save_screenshot(filename)

def main():
    # Setup WebDriver
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        # Navigate to the website
        driver.get("https://inc42.com/")
        logging.info("Navigated to inc42.com")

        # Verify and click the "Datalabs" link
        datalabs_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "DATALABS"))
        )
        datalabs_link.click()
        logging.info("Clicked on DATALABS link")

        # Verify and click the "Login" button
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
        )
        login_button.click()
        logging.info("Clicked on Login button")

        # Enter login credentials and submit
        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys("inc@yopmail.com")
        logging.info("Entered email")

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("Vishal@inc42")
        password_field.send_keys(Keys.RETURN)
        logging.info("Entered password and submitted login form")

        # Verify successful login
        dashboard_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "dashboard"))
        )
        capture_screenshot(driver, "login_successful.png")
        logging.info("Login successful, screenshot captured as login_successful.png")

        # Perform a search for the keyword "Fintech"
        search_bar = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        search_bar.send_keys("Fintech")
        search_bar.send_keys(Keys.RETURN)
        logging.info("Performed search for 'Fintech'")

        # Verify search results are displayed
        search_results = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "search-results"))
        )
        capture_screenshot(driver, "search_results.png")
        logging.info("Search results displayed, screenshot captured as search_results.png")

    except (NoSuchElementException, TimeoutException) as e:
        capture_screenshot(driver, "error.png")
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()
        logging.info("Browser closed")

if __name__ == "__main__":
    main()
