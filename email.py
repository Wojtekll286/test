import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage to scrape
url = "https://www.example.com"

# Send a GET request to fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Use regex to find all email addresses in the text
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, soup.get_text())

# Print found emails
print("Extracted Email Addresses:")
print(emails)
