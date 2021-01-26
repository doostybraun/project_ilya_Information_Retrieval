import nltk
import remove_chars_from_text

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\ArtStyle\jukovskyutf.txt', encoding="utf-8").read()

def average_word_length(text):
    txt_clean = remove_chars_from_text.remove_chars_from_text(text)
    txt_tokenized = nltk.tokenize.word_tokenize(txt_clean, language="russian")
    sum_words=0.0
    flag=0
    while flag<len(txt_tokenized):
        sum_words += len(txt_tokenized[flag])
        flag += 1
        if(flag == len(txt_tokenized)):
            sum_words=sum_words/len(txt_tokenized)
    return sum_words


def average_sent_length(text):
    txt_clean = remove_chars_from_text.remove_spcfk_chars(text)
    txt_sents_tokenized = nltk.tokenize.sent_tokenize(txt_clean, language="russian")
    sum_words_sent=0.0
    flag=0
    #print(len(txt_sents_tokenized))
    while flag < len(txt_sents_tokenized):
        sent_token = txt_sents_tokenized[flag]
        flag += 1
        clean_tokenized_sent_token = remove_chars_from_text.remove_chars_from_text(sent_token)
        tokenized_sent_token = nltk.tokenize.word_tokenize(clean_tokenized_sent_token, language="russian")
        sum_words_sent += len(tokenized_sent_token)
        final = 0
        #print(sum_words_sent)
        if(flag+1 > len(txt_sents_tokenized)):
            #средняя длина предложения
            #print(len(txt_sents_tokenized), sum_words_sent, sum_words_sent/len(txt_sents_tokenized))
            #print(sum_words_sent, len(txt_sents_tokenized), sum_words_sent/len(txt_sents_tokenized))
            sum_words_sent = sum_words_sent/len(txt_sents_tokenized)    
            return sum_words_sent
        



#a=average_sent_length(text1)
#print(a)
