import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os
import argparse


def shorten_url(headers, user_url):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    post_body = {"long_url": user_url}
    response = requests.post(url, headers=headers, json=post_body)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(headers, user_url):
    url_components = urlparse(user_url)
    netloc_path = f"{url_components.netloc}{url_components.path}"
    url = (
        f"https://api-ssl.bitly.com/v4/bitlinks"
        f"/{netloc_path}/clicks/summary"
    )
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitly(headers, user_url):
    url_components = urlparse(user_url)
    netloc_path = f"{url_components.netloc}{url_components.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{netloc_path}"
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    parse = argparse.ArgumentParser(description="Will make url short")
    parse.add_argument("user_url", type=str, help="Enter you URL")
    args = parse.parse_args()
    user_url = args.user_url
    load_dotenv(".env")
    token = os.environ["TOKEN_BITLY"]
    headers = {"Authorization": f"Bearer {token}"}
    try:
        if is_bitly(headers, user_url):
            total_clicks = count_clicks(headers, user_url)
            print(f"Total clicks on you URL - {total_clicks}")
        else:
            short_url = shorten_url(headers, user_url)
            print(f"You short url - {short_url}")
    except requests.exceptions.HTTPError:
        print("You enter wrong url")

if __name__ == "__main__":
    main()
