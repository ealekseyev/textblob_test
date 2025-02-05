from textblob import TextBlob
import csv

# Define a function to read the CSV file and print each row
def read_csv(file_path):
    with open(file_path, newline='', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = []
        # Loop through each row in the CSV and print it
        for row in reader:
            rows.append(row)
        return rows

# Replace 'your_file.csv' with your actual CSV file path

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
correct = 0
wrong=0
for row in read_csv('data.csv'):
    if(row[1] == row[2]): # skip all empty lines at end
        continue
    if(get_sentiment(row[1]).lower() == row[2]):
        correct += 1
    else:
        print(row[1].lower(), " ", row[2])
        wrong += 1
print("Correct: ", correct, " Wrong: ", wrong)
# Get and print the sentiment of the input
