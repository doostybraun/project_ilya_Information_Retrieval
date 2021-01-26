import nltk
import helper


#txt2="Я и три маленьких и два больших гнома зашли вчера ко мне в дом, смеясь от радости, и , бац!, уселись на пол,чтобы сообщить мне неожиданную новость."

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\PublicisticStyle\ShagiDalesa.txt').read()


counter=0



def Beta(text):
        next_token = None
        counter_for_NN=0
        counter_for_VB=0
        counter_A_f=0
        counter_ADV=0
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

                if(helper.helper_for_A_f(tagged_token[1]) and helper.helper_for_NN(next_token[1])):
                        counter_A_f+=1

                if(helper.helper_for_VB(tagged_token[1]) and helper.helper_for_ADV(next_token[1])):
                        counter_ADV+=1
        return [(counter_for_VB + counter_ADV)/(counter_for_NN + counter_A_f)]
              


def NN_same_neighbors(text):
        next_token = None
        counter_for_NN=0
        txt_tokenized = nltk.tokenize.word_tokenize(text, language="russian")
        txt_tagged = nltk.tag.pos_tag(txt_tokenized, lang='rus')
        for index,tagged_token in enumerate(txt_tagged):
                if(index<len(txt_tagged)-1):
                        next_token = txt_tagged[index+1]
               # print(index, next_token, tagged_token)
                if(helper.helper_for_NN(next_token[1]) and helper.helper_for_NN(tagged_token[1])):
                        counter_for_NN+=1
               #        print("OK")
        return counter_for_NN
        
#a = NN_same_neighbors(text1)
#print(a)

