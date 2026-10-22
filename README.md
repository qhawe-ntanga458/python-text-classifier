# Python Text Classifier

A beginner-friendly Python project that classifies text sentiment using keyword-based rules.

The program analyses text and assigns a positive, negative, or neutral sentiment based on positive and negative keyword matches.

## Features

- Classifies text as positive, negative, or neutral
- Recognises a range of positive and negative keywords
- Uses case-insensitive word matching
- Includes basic negation handling
- Accepts interactive user input
- Handles empty input
- Displays sentiment scores
- Allows users to exit the program with `quit`

## Technologies

- Python 3
- Python standard library (`re`)

## Getting Started

### Requirements

Install Python 3 on your computer.

### Run the project

Clone the repository:

```bash
git clone https://github.com/qhawe-ntanga458/python-text-classifier.git
```

Enter the project folder:

```bash
cd python-text-classifier
```

Run the program:

```bash
python text_classifier.py
```

Depending on your system, you may need to use `python3` instead of `python`.

## Example

```text
Enter text: I love this amazing product!

--- Classification Result ---
Text: I love this amazing product!
Sentiment: Positive
Positive score: 2
Negative score: 0
```

## Skills Demonstrated

- Python functions
- Sets and string processing
- Loops and conditional statements
- Regular expressions
- Input validation and exception handling
- Basic sentiment analysis

## Limitations

This project uses predefined keywords and simple rules. It is not a trained machine learning model and may misclassify complex sentences, sarcasm, and some forms of negation.

## Future Improvements

- Add automated unit tests
- Improve negation and phrase detection
- Evaluate classification accuracy on sample datasets
- Explore machine learning-based sentiment analysis

## Author

Qhawe Ntanga

GitHub: [qhawe-ntanga458](https://github.com/qhawe-ntanga458)
