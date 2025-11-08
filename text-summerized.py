from transformers import pipeline
summarizer = pipeline("summarization")

text = """Your long paragraph text goes here..."""
print(summarizer(text, max_length=60, min_length=30, do_sample=False)[0]['summary_text'])

