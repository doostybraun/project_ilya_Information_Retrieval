import nltk
import string
 

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Деловой стиль\Заявления.txt', encoding="utf-8").read()


def remove_chars_from_text(text):
    spec_chars = '.,!#$%&""()*+-/:;<=>?[\]^_`{|}\n\xa0«»\t—…@№№'
    return "".join([ch for ch in text if ch not in spec_chars])

def remove_spcfk_chars(text):
    spec_chars = '!#$%&""()*+-/:;<=>?[\]^_`{|}\n\xa0«»\t—…@№№'
    return "".join([ch for ch in text if ch not in spec_chars])

#print(string.punctuation)
#txt_tokenized = nltk.tokenize.word_tokenize(text1, language="russian")
#print(len(txt_tokenized))
#txt_clean = remove_chars_from_text(text1)
#txt_tokenized1 = nltk.tokenize.word_tokenize(txt_clean, language="russian")
#print(len(txt_tokenized1))
