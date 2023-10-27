import requests
import os
import json

# Define your GitHub username and the API endpoint
GITHUB_USERNAME = "your_username"
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/gists"

LAST_RUN_FILE = "last_run_date.txt"

def get_public_gists():
    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch gists - {e}")
        return None

def load_last_run_date():
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, "r") as file:
            return file.read().strip()
    else:
        return ""

def save_last_run_date(last_date):
    with open(LAST_RUN_FILE, "w") as file:
        file.write(last_date)

def main():
    last_run_date = load_last_run_date()
    gists = get_public_gists()

    if gists is not None:
        if last_run_date:
            print("New gists published since the last run:")
            for gist in gists:
                created_at = gist["created_at"]
                if created_at > last_run_date:
                    print(f"- {gist['id']}: {gist['description']} ({created_at})")
        else:
            print("All publicly available gists:")
            for gist in gists:
                print(f"- {gist['id']}: {gist['description']} ({gist['created_at']})")

        if gists:
            last_created_at = gists[0]["created_at"]
            save_last_run_date(last_created_at)

if __name__ == "__main__":
    main()
