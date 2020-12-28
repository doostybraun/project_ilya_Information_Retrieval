import nltk
import helper


txt1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Деловой стиль\Заявления.txt', encoding="utf-8").read()
#txt_ready = read_corpus_to_nltk(txt1)

txt2="Я и три маленьких и два больших гнома зашли вчера ко мне в дом, смеясь от радости, и , бац!, уселись на пол,чтобы сообщить мне неожиданную новость."

counter=0
next_token = None


def count_number_of_same_part_of_speach(text):
        counter_for_NN=0
        counter_for_VB=0
        txt_tokenized = nltk.tokenize.word_tokenize(text, language="russian")
        txt_tagged = nltk.tag.pos_tag(txt_tokenized, lang='rus')
        for index,tagged_token in enumerate(txt_tagged):
                if(index<len(txt_tagged)-1):
                        next_token = txt_tagged[index+1]
               # print(index, next_token, tagged_token)
                if(helper.helper_for_NN(next_token[1]) and helper.helper_for_NN(tagged_token[1])):
                        counter_for_NN+=1
               #        print("OK")
                if(helper.helper_for_VB(tagged_token[1]) and helper.helper_for_NN(next_token[1])):
                        counter_for_VB+=1
        return [counter_for_NN, counter_for_VB]
              

print(count_number_of_same_part_of_speach(txt1))

sents=None
