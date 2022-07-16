# News Key Terms Visualizer
Fun project to illustrate most important words in texts. It preprocesses texts, extracts terms and weights according to the TF-IDF criterion, and creates word-clouds with them.

![Example](https://github.com/kraslav4ik/Key-Terms-Extraction/blob/main/examples/cloud_example_3.png) 

Reads text from text or xml-file(example of xml file is in `"./Key Terms Extraction/texts"`).

Preprocessing consists of the following:
* Word Lemmatization
* Removing punctuation and stop-words
* Extracting only nouns

The most frequent words are shown in word-clouds (font-size depends on word importance: the bigger word is, the more important it is)

Works with: Python 3.8

Launch Visualizer:

```bash
News-key-Terms-Visualizer/> python "./Key Terms Extraction/key_terms.py"
```

Launch tests:

```bash
News-key-Terms-Visualizer/> python "./Key Terms Extraction/tests/test.py"
```

Tests are provided by JetBrains Academy

Project made as a part of JetBrains Academy course

https://hyperskill.org/projects/166?track=2 

![Example2](https://github.com/kraslav4ik/Key-Terms-Extraction/blob/main/examples/cloud_example.png)
