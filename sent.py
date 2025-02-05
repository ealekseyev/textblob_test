from textblob import TextBlob

def get_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity of the text
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on the polarity value
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Input from the user
user_input = input("Enter a string to analyze sentiment: ")

# Get and print the sentiment of the input
sentiment = get_sentiment(user_input)
print(f"The sentiment of the input is: {sentiment}")
