import nltk
import average_length_of_word
import betafunc
import tags_counter

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\ArtStyle\i-1-4-pratchett-terri-NemaloKnig.net.txt', encoding="utf-8").read()

def numPrefixCheck(txt):
    prefix=["противо","внутри","интра","квази","интер","гига","тера","ультра", "анти", "био", "микро", "макро", "экстра", "мини", "макси", "нео", "нано", "гипер", "суб", "гипо", "экс"]
    txt_tknzd = nltk.tokenize.word_tokenize(txt)
    counter=0
    for token in txt_tknzd:
        currt = token
        for pref in prefix:
            if(currt.startswith(pref)):
                counter += 1
    return counter


def prefixCheck(txt):
    prefix=["противо","внутри","интра","квази","интер","гига","тера","ультра", "анти", "био", "микро", "макро", "экстра", "мини", "макси", "нео", "нано", "гипер", "суб", "гипо", "экс"]
    txt_tknzd = nltk.tokenize.word_tokenize(txt)
    counter=0
    for token in txt_tknzd:
        currt = token
        for pref in prefix:
            if(currt.startswith(pref)):
                counter+=1
    if(counter > 120):
        return 2.5
    elif(counter > 230):
        return 5.0
    else:
        return 0



def scienceParamDetection(txt):
    grade = 0
    prefix = numPrefixCheck(txt)
    tags_vector = tags_counter.counter(txt)
    #sent_len = average_length_of_word.average_sent_length(txt)
    beta = betafunc.Beta(txt)
    #print(prefix, beta)
    if(prefix > 100 and beta > 0.22):
        grade = 2.5
        #print("Данный текст почти невозможно переделать в текст делового или публицистического стиля \n")
        if(tags_vector[5] < 1936908127739503/4611686018427387904 or tags_vector[4] < 5404319552844595/72057594037927936):
            grade = 5
            #print("Есть признаки схожести с научным текстом")
            return grade
        else:
            #print("Возможно схоже с художестным текстом")
            return grade
        
        return grade
    else:
        #print("There is nothing about science here")
        return 0

#a = scienceParamDetection(text1)   
#print(a)
