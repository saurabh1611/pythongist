# GitHub Gist Monitor

This Python script helps in monitoring public gists on GitHub associated with a specific user. It retrieves information about gists, identifies new gists published since the last check, and displays all publicly available gists if it's the first run or if the last run date isn't available.

## Prerequisites

To use this script, ensure you have the following installed:

- Python 3.x
- Necessary Python libraries (install using `pip install -r requirements.txt`)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/gist-monitor.git
   cd gist-monitor
   ```
2. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Update the configuration:**
   Open the Python script and set the GITHUB_USERNAME variable to the GitHub username whose gists you want to monitor.

## Usage

Run the Python script using the following command:
```bash
python gist_monitor.py
```

## Functionality

`get_public_gists()`: Fetches the public gists from the specified GitHub user's account using the GitHub API.
`load_last_run_date()`: Loads the last run date from the "last_run_date.txt" file. If the file doesn't exist, it returns an empty string.
`save_last_run_date()`: Saves the last run date to the "last_run_date.txt" file.
`main()`: The main function that orchestrates the checking of new gists since the last run and displays the available gists accordingly.

## Example Output

Upon running the script, you can expect to see:

- New gists published since the last run, with their IDs, descriptions, and creation dates.
- All publicly available gists in case of the initial run or if the last run date isn't available.
