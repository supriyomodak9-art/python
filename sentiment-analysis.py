from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

while True:
    text = input("Enter text for sentiment analysis (or 'exit' to stop): ")
    if text.lower() == "exit":
        break
    result = sentiment(text)[0]
    print(f"Label: {result['label']}, Score: {round(result['score'], 2)}")
