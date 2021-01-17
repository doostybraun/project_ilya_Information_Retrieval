import nltk
import remove_chars_from_text

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Деловой стиль\Заявления.txt', encoding="utf-8").read()

def amount_of_unique_words(text):
    #txt_tokenized1 = nltk.tokenize.word_tokenize(text, language="russian")
    #print(len(txt_tokenized1))
    txt_clear = remove_chars_from_text.remove_chars_from_text(text)
    txt_tokenized = nltk.tokenize.word_tokenize(txt_clear, language="russian")
    #print(len(txt_tokenized))
    dic = {}  # dict with unique words
    for word in txt_tokenized:  
       if word in dic:  
           dic[word] += 1  
       else:  
           dic[word] = 1  

    return len(dic)  # return sorted list.


#print(amount_of_unique_words(text1))
