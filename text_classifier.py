# Python Text Classifier
# A beginner project that classifies text sentiment
# using keyword-based rules.

import re


POSITIVE_WORDS = {
"good", "great", "happy", "excellent",
"love", "wonderful", "amazing", "helpful",
"success", "best", "fantastic", "enjoy",
"beautiful", "kind", "excited", "perfect"
}

NEGATIVE_WORDS = {
"bad", "sad", "angry", "terrible",
"hate", "awful", "poor", "worst",
"disappointed", "failure", "horrible",
"annoyed", "unhappy", "ugly", "boring"
}

NEGATION_WORDS = {
"not", "never", "no", "neither", "nor",
"hardly", "isn't", "wasn't", "weren't",
"don't", "doesn't", "didn't", "can't",
"couldn't", "won't", "wouldn't", "shouldn't"
}


def classify_sentiment(text):
"""Classify text as positive, negative, or neutral."""

if not isinstance(text, str):
raise TypeError("Input must be a string.")

if not text.strip():
raise ValueError("Input cannot be empty.")

# Extract words and punctuation marks.
tokens = re.findall(
r"[a-z]+(?:'[a-z]+)?|[.!?,;:]",
text.lower()
)

positive_score = 0
negative_score = 0
negation_window = 0

for token in tokens:

# Punctuation ends the current negation scope.
if token in {".", "!", "?", ",", ";", ":"}:
negation_window = 0
continue

if token in NEGATION_WORDS:
negation_window = 3
continue

is_negated = negation_window > 0

if token in POSITIVE_WORDS:
if is_negated:
negative_score += 1
else:
positive_score += 1

elif token in NEGATIVE_WORDS:
if is_negated:
positive_score += 1
else:
negative_score += 1

if negation_window > 0:
negation_window -= 1

if positive_score > negative_score:
sentiment = "Positive"
elif negative_score > positive_score:
sentiment = "Negative"
else:
sentiment = "Neutral"

return sentiment, positive_score, negative_score


def main():
print("=== Python Text Classifier ===")
print("Analyse the sentiment of a sentence.")
print("Type 'quit' to exit.\n")

while True:
user_text = input("Enter text: ").strip()

if user_text.lower() == "quit":
print("Thank you for using the Text Classifier!")
break

if not user_text:
print("Please enter a sentence.\n")
continue

try:
sentiment, positive_score, negative_score = (
classify_sentiment(user_text)
)

print("\n--- Classification Result ---")
print("Text:", user_text)
print("Sentiment:", sentiment)
print("Positive score:", positive_score)
print("Negative score:", negative_score)
print("-----------------------------\n")

except (TypeError, ValueError) as error:
print("Error:", error, "\n")


if __name__ == "__main__":
main()
