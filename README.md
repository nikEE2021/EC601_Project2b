# EC601_Project2b

The file "google_API_sentiment.py" uses the Google Cloud NLP API for sentiment analysis to compare the score and magnitude of synonyms of the words "good" and "bad". The synomyns were composed of the first nine results from https://www.thesaurus.com and their respective search term. The purpose was to look at how the API evaluates words' scores and magnitudes when given basic words with sentiment which is obvious to an English speaking human reader.

This code was executed in Google Cloud Shell using interactive python in the command line. The function, imports and variables were executed in one instance and the function calls in two separate instances. The positvely and negatively sentimented words showed a relatively similar distribution of magnitudes and the scores were all non-negative for the positively sentimented words and vice versa. Almost all magnitudes were above 0.8, which makes sense since the entire text consisted of one polarizing word. The outliers, like the word "cheap", appeared to simply be poor synonyms.

References
- https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3#0
- https://www.thesaurus.com/
