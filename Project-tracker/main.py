# main.py
import json
import schedule
import time
from database import init_db, save_price
from scraper import scrape_amazon_price
from alert import send_alert
from visualizer import plot_all_products

def load_products():
    with open("products.json", "r") as f:
        return json.load(f)

def check_prices():
    print("\n🔍 Checking prices...")
    products = load_products()

    for product in products:
        name = product["name"]
        url = product["url"]
        threshold = product["threshold"]

        print(f"\n➡️  Scraping: {name}")
        price = scrape_amazon_price(url)

        if price:
            print(f"   💰 Price found: ₹{price}")
            save_price(name, price)

            if price <= threshold:
                print(f"   🚨 Below threshold! Sending alert...")
                send_alert(name, price, threshold, url)
        else:
            print(f"   ❌ Could not fetch price for {name}")

    # Generate graphs after each run
    product_names = [p["name"] for p in products]
    plot_all_products(product_names)

if __name__ == "__main__":
    init_db()
    print("✅ Database initialized")
    print("🤖 Price Tracker Started!\n")

    # Run immediately once
    check_prices()

    # Then run every 6 hours
    schedule.every(6).hours.do(check_prices)

    print("\n⏰ Scheduler running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(60)