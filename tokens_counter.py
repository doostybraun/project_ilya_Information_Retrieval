import nltk
import remove_chars_from_text

#SHIT

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Публицистический стиль\Почему властвует Запад… по крайней мере, пока еще..txt').read()

#tokenized_text = nltk.word_tokenize(text)
#print(len(tokenized_text))
#newtxt=remove_chars_from_text.remove_chars_from_text(text, spec_chars)
#newtxt_tokenized = nltk.word_tokenize(newtxt)
#print(len(newtxt_tokenized))

def counter_tokens_wOrwo(text):
    spec_chars = remove_chars_from_text.string.punctuation + '\n\xa0«»\t—…'

    txt_with_punct_tokenized = nltk.word_tokenize(text)
    txt_without_punct_tokenized = nltk.word_tokenize(remove_chars_from_text.remove_chars_from_text(text, spec_chars))
    return [len(txt_with_punct_tokenized), len(txt_without_punct_tokenized)]
   

#SHIT
