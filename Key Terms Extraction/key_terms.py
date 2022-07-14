import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from lxml import etree
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class KeyTerm:

    def __init__(self, dir_name):
        self.dir = dir_name
        self.texts = {}
        self.stop_words = set(stopwords.words('english')) | set(punctuation)
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer()

    def find_texts(self) -> None:
        files = [f for f in os.listdir(self.dir) if os.path.isfile(os.path.join(self.dir, f))]
        for file in files:
            if file.endswith(".xml"):
                with open(os.path.join(self.dir, file)) as xml:
                    root = etree.parse(xml).getroot()
                    for tag in root.iter():
                        if tag.get('name') == 'head':
                            head = f'{tag.text}:'
                            continue
                        if tag.get('name') == 'text':
                            text = tag.text
                            self.texts[head] = text
                continue
            with open(os.path.join(self.dir, file)) as txt:
                self.texts[file] = txt.read()
        return

    def find_normal_words(self) -> None:
        for key in self.texts:
            tokens = word_tokenize(self.texts[key].lower())
            lemmatized_words = [self.lemmatizer.lemmatize(word) for word in tokens]
            pos_speech = [nltk.pos_tag([word]) for word in lemmatized_words]
            nouns = [word[0][0] for word in pos_speech if word[0][1] == 'NN']
            normalized_words = [word for word in nouns if word not in self.stop_words]
            self.texts[key] = ' '.join(normalized_words)
        return

    def find_frequent_words(self) -> None:
        matrix = self.vectorizer.fit_transform(self.texts.values()).toarray()
        terms = self.vectorizer.get_feature_names_out()
        for i, key in enumerate(self.texts):
            self.texts[key] = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0.0:
                    continue
                self.texts[key].append((matrix[i][j], terms[j]))
            print(key)
            sorted_words = [k[1] for k in sorted(self.texts[key], reverse=True)[:5]]
            words_to_cloud = [k[1] for k in sorted(self.texts[key], reverse=True)[:20]]
            answer = ' '.join(sorted_words)
            print(answer)
            self.cloud(words_to_cloud, key)
        return

    def cloud(self, word_list, title):
        words = ' '.join(word_list)
        wordcloud = WordCloud(width=680, height=680, max_words=100).generate(words)
        fig = plt.figure()
        fig.suptitle(title, fontsize=12, fontweight='bold')
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.margins(x=0, y=0)
        plt.show()

    #
    # def __del__(self):
    #     self.xml_file.close()


if __name__ == '__main__':
    dir_name = "texts"
    extractor = KeyTerm(dir_name)
    extractor.find_texts()
    extractor.find_normal_words()
    extractor.find_frequent_words()
