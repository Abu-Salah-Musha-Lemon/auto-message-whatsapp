from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ✅ কন্টাক্ট তালিকা
contacts = [
    "Shahidul", "Rana", "Abdullah", "Shanto", "Parvez", "Shohag",
    "Rafiqul", "Engr Alhaz", "Raju", "Ashraful", "Azadul", "Shaon",
    "Bappy", "Atik", "Foysal", "Engr Bulbul", "Mizan", "Elias",
    "Pronoy", "Kamrul"
]

# ✅ মেসেজ কনটেন্ট (মাল্টিলাইন)
message = "আসসালামু আলাইকুম\nকাজের কী খবর?"

# ✅ Chrome ব্রাউজার চালু করে WhatsApp Web খুলবে
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("📷 QR কোড স্ক্যান করুন WhatsApp-এ লগইন করতে, তারপর Enter চাপুন...")

for name in contacts:
    try:
        # ✅ কন্টাক্ট সার্চ
        search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
        search_box.clear()
        search_box.send_keys(name)
        time.sleep(2)

        contact = driver.find_element(By.XPATH, f'//span[@title="{name}"]')
        contact.click()
        time.sleep(1)

        # ✅ মেসেজ টাইপ ও সেন্ড
        msg_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
        msg_box.send_keys(message)
        msg_box.send_keys(Keys.ENTER)
        time.sleep(1)

        print(f"✅ মেসেজ পাঠানো হয়েছে: {name}")
    except Exception as e:
        print(f"❌ সমস্যা হয়েছে {name}-এর জন্য: {e}")

driver.quit()
