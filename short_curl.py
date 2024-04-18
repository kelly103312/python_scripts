import pyshorteners

# Create a Shortener object
shortener = pyshorteners.Shortener()

# Shorten a URL
short_url = shortener.tinyurl.short('https://programacionpython80889555.wordpress.com/2021/11/11/acortando-url-en-python-con-pyshorteners/')

# Print the shortened URL
print("Shortened URL:", short_url)
