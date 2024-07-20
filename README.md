# Quotes X Bot

This Python script tweets a random inspirational quote from a CSV file using the Tweepy library. It reads quotes from a CSV file, randomly selects a quote, tweets it, and removes it from the CSV to ensure no duplicates.

## Features

- Reads quotes from a CSV file
- Randomly selects a quote and removes it from the CSV
- Tweets the selected quote using the Twitter API/X API
- The code is hosted on https://www.pythonanywhere.com to run everyday at a specified time.

## Requirements

- Python 3.x
- `tweepy` library
- X/Twitter Account

## Configuration

Update the following variables in the script with your Twitter API credentials:

```python
api_key = 'your_api_key'
api_secret_key = 'your_api_secret_key'
bearer_token = 'your_bearer_token'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
```

Define the path to your CSV file containing the quotes:
```python
csv_file = r'path\to\your\quotes.csv'
```

## CSV Format
Ensure your CSV file is formatted as follows:
```csv
quote,author
"The only way to achieve the impossible is to believe it is possible.",Charles Kingsleigh
"Success is not final, failure is not fatal: It is the courage to continue that counts.",Winston Churchill
```

## Link and Screenshots
It would be helpful if you could follow the account.<br>
https://x.com/Quotessence_ <br><br>
![screenshot1](screenshot1.png)<br>
![screenshot2](screenshot2.png)


##### Worked on this as part of a module project from Dr. Angela Yu's course on Udemy titled: 100 Days of Code: The Complete Python Pro Bootcamp

