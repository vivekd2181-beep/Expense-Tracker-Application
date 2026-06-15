# scraper.py
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config import USER_AGENTS

def get_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1280,800")
    options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # ⚠️ No headless this time — Amazon blocks headless easily
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def scrape_amazon_price(url):
    driver = get_driver()
    price = None
    try:
        driver.get(url)

        # Wait longer — let page fully load
        time.sleep(random.uniform(5, 8))

        # Scroll like a human
        driver.execute_script("window.scrollBy(0, 300)")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 300)")
        time.sleep(1)

        # Print page title for debugging
        print(f"   📄 Page title: {driver.title}")

        # Try all known Amazon price selectors
        selectors = [
            "span.a-price-whole",
            "#priceblock_ourprice",
            "#priceblock_dealprice",
            "#corePrice_feature_div span.a-price-whole",
            "div.a-section.a-spacing-none span.a-price-whole",
            ".apexPriceToPay span.a-price-whole",
            "#apex_offerDisplay_desktop span.a-price-whole",
            "span.priceToPay span.a-price-whole",
        ]

        for selector in selectors:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    raw = element.text.replace(",", "").replace("₹", "").strip()
                    if raw and raw.replace(".", "").isdigit():
                        price = float(raw.split(".")[0])
                        print(f"   ✅ Found via selector: {selector}")
                        break
                if price:
                    break
            except:
                continue

        # If still no price, print page source snippet for debugging
        if not price:
            print("   ⚠️  No price found. Checking page...")
            if "captcha" in driver.page_source.lower():
                print("   🤖 CAPTCHA detected! Amazon is blocking us.")
            elif "sign in" in driver.title.lower():
                print("   🔒 Amazon is asking to sign in.")
            else:
                print("   ❓ Page loaded but price not found.")

    except Exception as e:
        print(f"   [ERROR] {e}")
    finally:
        driver.quit()

    return price