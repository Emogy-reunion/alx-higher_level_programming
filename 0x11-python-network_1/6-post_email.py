#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    response = requests.post(url, data=value)
    print(response.text)
