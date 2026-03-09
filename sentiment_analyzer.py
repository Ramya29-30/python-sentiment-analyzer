from textblob import TextBlob

text = input("Enter a sentence: ").lower()

analysis = TextBlob(text)

score = analysis.sentiment.polarity

print("Polarity Score:", score)

if score > 0.2:
    print("Positive Sentiment 😊")
elif score < -0.2:
    print("Negative Sentiment 😞")
else:
    print("Neutral Sentiment 😐")