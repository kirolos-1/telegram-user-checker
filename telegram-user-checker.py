import requests
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor

# ==================================================================
#                   بوت تخمين حسابات تيليجرام
#             Telegram Username Guessing Bot
# ==================================================================

# كودات ANSI لتلوين النص
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # لإعادة اللون إلى الوضع الطبيعي

# ==================================================================
# اسم الأداة مع تلوين وجعلها أكبر ويشمل كلمة "Telegram"
# ==================================================================
def print_tool_name():
    print(f"{MAGENTA}══════════════════════════════════════════════{RESET}")
    print(f"{CYAN}       بوت تخمين حسابات تيليجرام {YELLOW}- Telegram Username Guessing Bot{RESET}")
    print(f"{MAGENTA}══════════════════════════════════════════════{RESET}")

def generate_username():
    # Generates a random username with three characters
    gg = random.choice('qwertyuiopasdfghjklzxcvbnm')
    ag = random.choice('qwertyuiopasdfghjklzxcvbnm')
    eg = random.choice('qwertyuiopasdfghjklzxcvbnm')
    return f"{gg}_{ag}_{eg}"

def chk_user(user):
    try:
        # Send a GET request to the fragment website
        response = requests.get(f"https://fragment.com/username/{user[1:]}")
        
        # Check for different user availability statuses
        if '<span class="tm-section-header-status tm-status-taken">Taken</span>' in response.text:
            return f"{user} : مستخدم"
        elif '<span class="tm-section-header-status tm-status-unavail">Sold</span>' in response.text:
            return f"{user} : معروض للبيع"
        elif '<div class="table-cell-status-thin thin-only tm-status-unavail">Unavailable</div>' in response.text:
            return f"{user} : متاح ✅"
        return f"{user} : غير متاح ❌"
    except requests.RequestException:
        return f"{user} : خطأ في الفحص"

def check_multiple_users():
    while True:
        # Generate one username at a time
        user = generate_username()
        
        # Use ThreadPoolExecutor to check the user status
        with ThreadPoolExecutor(max_workers=1) as executor:
            results = list(executor.map(chk_user, [user]))  # Wrap user in a list to pass to executor
        
        # Print the results of the check
        for result in results:
            print(result)

# Add your nickname to be printed when the script runs
if __name__ == "__main__":
    print("جاري فحص اليوزرات...")
    print("تم تطوير هذا السكربت بواسطة: @iro86")  # Your nickname
    print_tool_name()  # Call the function to print the tool name
    check_multiple_users()
