import nltk

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\BusinessStyle\prikaz10utf.txt', encoding="utf-8").read()


def most_common_NN(text):
    txt_tokenized = nltk.tokenize.word_tokenize(text, language="russian")
    txt_tagged = nltk.tag.pos_tag(txt_tokenized, lang="rus")
    only_nn = [x for (x,y) in txt_tagged if y in 'S']
    dist_nn = nltk.FreqDist(only_nn)
    print(dist_nn.most_common(7))

def most_common_V(text):
    txt_tokenized = nltk.tokenize.word_tokenize(text, language="russian")
    txt_tagged = nltk.tag.pos_tag(txt_tokenized, lang="rus")
    only_v = [x for (x,y) in txt_tagged if y in 'V']
    dist_nn = nltk.FreqDist(only_v)
    print(dist_nn.most_common(7))

def most_common_A_f(text):
    txt_tokenized = nltk.tokenize.word_tokenize(text, language="russian")
    txt_tagged = nltk.tag.pos_tag(txt_tokenized, lang="rus")
    only_A_f = [x for (x,y) in txt_tagged if y in 'A=f']
    dist_nn = nltk.FreqDist(only_A_f)
    print(dist_nn.most_common(7))
#most_common_NN(text1)
#most_common_V(text1)
#most_common_A_f(text1)
