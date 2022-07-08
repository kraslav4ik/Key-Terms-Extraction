# Key-Terms-Extraction
Completed HyperSkill Project "Key-Terms-Extraction"

Programm allows you to extract the most important words from text. It reads an xml-file, takes text from tags "head" (to headers) and "text" (for text), then lemmatize words in it, removes punctuation and stop-words, then takes only nouns and returns the most important words for each text (to define, which words are the most important programm uses the tf-idf criteria as a weighting factor of the word)

Current programm works with xml file "news.html" which is attached.

Python 3.8

Launch src and tests from "./Key Terms Extraction"

Test-files "news.xml", "news.py" and "tests.py" are made by HyperSkill. 
