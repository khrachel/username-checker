import requests  # lets script talk to the internet
import time  # helps space out timing so we dont get blocked by websites
import sys  # lets us exit the script cleanly if something goes wrong

def check_user(username):
    platforms = {
        "GitHub":    "https://github.com/{}",
        "Reddit":    "https://www.reddit.com/user/{}",
        "TikTok":    "https://www.tiktok.com/@{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Twitch":    "https://www.twitch.tv/{}",
        "YouTube":   "https://www.youtube.com/@{}",
        "Instagram": "https://instagram.com/{}",
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }  # avoiding suspicion for being a bot

    print(f"\nChecking username: {username}\n")
    results = []

    for platform, url_template in platforms.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, headers=headers, timeout=10)
            print(f" {platform} status code: {response.status_code}")
            if response.status_code == 200:
                status = "OK;FOUND"
            elif response.status_code == 403:
                status = "FORBIDDEN"
            elif response.status_code == 404:
                status = "NOT FOUND"
            else:
                status = "NOT FOUND"
        except:
            status = "ERROR"

        print(f"{platform:<12} {status:<12} {url}")
        results.append((platform, status, url))
        time.sleep(1)

def main():
    print("Welcome to the simple username checker. Please enter a username!")
    while True:
        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            username = input("Enter a username: ")
        check_user(username)
        repeat = input("\nWould you like to search another username? (yes/no): ")
        if repeat.lower() == "no":
            print("Thanks for using this! This was created as part of my journey of learning code. Anthropic's Claude assisted in creating this script. :)")
            break
main()
