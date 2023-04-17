import requests
import stem.process
import stem.control
import random
import time
import sys

TOR_CONTROL_PORT = 9051
TOR_SOCKS_PORT = 9050
MAX_RENEW_ATTEMPTS = 3

MAX_TIME_INTERVAL = 60

urls = [
    "PLACE_URLs_HERE",
    "HERE_TOO",
]

def renew_tor_circuit():
    renew_attempts = 0
    while renew_attempts < MAX_RENEW_ATTEMPTS:
        try:
            with stem.control.Controller.from_port(port=TOR_CONTROL_PORT) as controller:
                controller.authenticate()
                controller.signal(stem.Signal.NEWNYM)
                print("Tor IP has been changed.")
            break
        except stem.connection.AuthenticationFailure:
            print("Authentication with Tor failed. Please check your Tor authentication settings.")
            exit(1)
        except stem.connection.SocketError as exc:
            print("Error communicating with Tor: %s" % exc)
            renew_attempts += 1
            if renew_attempts >= MAX_RENEW_ATTEMPTS:
                print("Max attempts reached while renewing Tor circuit. Exiting...")
                exit(1)

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    ]
    return random.choice(user_agents)

def get_random_url():
    return random.choice(urls)

def main():
    with stem.process.launch_tor_with_config(config = {'ControlPort': str(TOR_CONTROL_PORT), 'SocksPort': str(TOR_SOCKS_PORT)}) as tor_process:
        while True:
            renew_tor_circuit()
            url = get_random_url()
            headers = {
                "User-Agent": get_random_user_agent()
            }
            try:
                response = requests.get(url, headers=headers, proxies={'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'})
                print(f"Successfully opened {url}")
            except:
                print(f"Error opening {url}")

            # Status bar
            sleep_time = random.randint(1, MAX_TIME_INTERVAL)
            for i in range(sleep_time, 0, -1):
                time_left = f"{i}s left"
                sys.stdout.write('\r' + time_left)
                sys.stdout.flush()
                time.sleep(1)

            # Clear the status bar
            sys.stdout.write('\033[2K\033[1G')

if __name__ == "__main__":
    main()
