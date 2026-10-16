# Python Text Classifier
# A beginner project that classifies text sentiment
# using simple keyword-based rules.

def classify_sentiment(text):
"""Classify a sentence as positive, negative, or neutral."""

positive_words = [
"good", "great", "happy", "excellent",
"love", "wonderful", "amazing", "helpful",
"success", "best"
]

negative_words = [
"bad", "sad", "angry", "terrible",
"hate", "awful", "poor", "worst",
"disappointed", "failure"
]

# Convert text to lowercase so matching is case-insensitive.
words = text.lower().split()

# Count positive and negative keyword matches.
positive_score = sum(
1 for word in words
if word.strip(".,!?;:") in positive_words
)

negative_score = sum(
1 for word in words
if word.strip(".,!?;:") in negative_words
)

# Decide the sentiment based on the scores.
if positive_score > negative_score:
sentiment = "Positive"
elif negative_score > positive_score:
sentiment = "Negative"
else:
sentiment = "Neutral"

return sentiment, positive_score, negative_score


def main():
print("=== Python Text Classifier ===")
print("Enter a sentence to analyse its sentiment.")
print("Type 'quit' to exit.\n")

while True:
user_text = input("Enter text: ").strip()

if user_text.lower() == "quit":
print("Thank you for using the Text Classifier!")
break

if not user_text:
print("Please enter a sentence.\n")
continue

sentiment, positive_score, negative_score = (
classify_sentiment(user_text)
)

print("\n--- Classification Result ---")
print("Text:", user_text)
print("Sentiment:", sentiment)
print("Positive keyword matches:", positive_score)
print("Negative keyword matches:", negative_score)
print("-----------------------------\n")


if __name__ == "__main__":
main()
