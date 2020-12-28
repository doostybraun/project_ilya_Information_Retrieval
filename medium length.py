import nltk
import remove_chars_from_text
text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Деловой стиль\Заявления.txt', encoding="utf-8").read()

def average_word_length(text):
    txt_clean = remove_chars_from_text.remove_chars_from_text(text)
    txt_tokenized = nltk.tokenize.word_tokenize(txt_clean, language="russian")
    sum_words=0
    flag=0
    while flag<len(txt_tokenized):
        sum_words+=len(txt_tokenized[flag])
        flag+=1
        if(flag == len(txt_tokenized)):
            sum_words=sum_words/len(txt_tokenized)
    return sum_words



print(average_word_length(text1))
