from google.cloud import language


plus = [
    "good",
    "acceptable",
    "excellent",
    "exceptional",
    "favorable",
    "great",
    "marvelous",
    "positive",
    "satisfactory",
    "superb",
]

minus = [
    "bad",
    "atrocious",
    "awful",
    "cheap",
    "crummy",
    "dreadful",
    "lousy",
    "poor",
    "rough",
    "sad"
]


def analyze_text(texts):
    client = language.LanguageServiceClient()

    for text in texts:
        document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
        response = client.analyze_sentiment(document=document)
        sentiment = response.document_sentiment
        print(sentiment.score, sentiment.magnitude)


analyze_text(plus)
analyze_text(minus)
