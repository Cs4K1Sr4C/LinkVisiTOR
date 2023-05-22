# 🌐 VisiTOR .:. Simple TOR Circuit Renewal and Web Scraping 🕷️

### A Python script to perform web scraping through TOR network by renewing TOR circuits. This script allows you to change your IP address and scrape websites anonymously using TOR.

## ⚙️ Usage

1. Make sure you have TOR installed on your machine.
2. Install the required Python packages by running pip install requests stem.
3. Copy the code provided into a Python file (e.g., tor_scraping.py).
4. Replace the "PLACE_URLs_HERE" and "HERE_TOO" placeholders with the desired URLs you want to scrape.
5. Run the script using python tor_scraping.py.

## 🔄 TOR Circuit Renewal

The script includes a function called renew_tor_circuit() that attempts to renew the TOR circuit. It authenticates with the TOR control port and signals TOR to establish a new circuit, resulting in a new IP address.

## 🌍 Random User Agent and URL

The script provides two functions:

- `get_random_user_agent()`: Returns a random User-Agent string from a predefined list. This helps mimic different web browsers.
- `get_random_url()`: Returns a random URL from the provided list of URLs. You can customize this list to suit your scraping needs.

## 🔄 Main Function

The `main()` function is responsible for the main execution flow of the script. It launches a TOR process with specified configuration, and then continuously renews the TOR circuit, opens random URLs, and scrapes their content using the specified User-Agent. The script includes a status bar that displays the time left for each scraping cycle.

## 🚀 Running the Script

1. Ensure you have TOR installed and running.
2. Execute the script by running python tor_scraping.py.

***🔒 Note: This script is meant for educational purposes and to demonstrate the usage of TOR for web scraping. Make sure to comply with the terms of service of the websites you scrape and respect their policies regarding scraping.***

Feel free to customize the code according to your requirements and happy scraping! 🕸️
