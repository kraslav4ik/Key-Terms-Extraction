# Key-Terms-Extraction
Completed HyperSkill Project "Key-Terms-Extraction"

![Example](https://github.com/kraslav4ik/Key-Terms-Extraction/blob/main/examples/cloud_example_3.png) ![Example2](https://github.com/kraslav4ik/Key-Terms-Extraction/blob/main/examples/cloud_example.png)

Programm allows you to extract the most important words from text. It reads text or xml-files from "texts" directory, (in XML files program takes text from tags "head" (to headers) and "text" (for text), in text files - takes name as header and text as text resp.), then lemmatize words in them, removes punctuation and stop-words, then takes only nouns and returns the most important words for each text (to define, which words are the most important programm uses the tf-idf criteria as a weighting factor of the word). The most frequent words are shown in word-clouds (font-size depends on word importance)

Text/xml files should be placed in ./Key Terms Extraction/texts directory

Python 3.8

Launch src and tests from "./Key Terms Extraction"

Test is working with "news.xml" which is already in texts dir

Test-files "news.xml", "news.py" and "tests.py" are made by HyperSkill. 
