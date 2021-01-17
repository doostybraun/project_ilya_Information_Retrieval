import nltk
import helper
import betafunc

№text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Imagination\imagi4utf.txt', encoding="utf-8").read()

txt2="бегал крот, бежит трамвай"

def verb_noun_counter(txt):
    upper_limit = 640
    lower_limit = 310
    std = 77
    next_token = None
    counter_verb_noun=0
    txt_tokenized = nltk.tokenize.word_tokenize(txt, language="russian")
    txt_tagged = nltk.tag.pos_tag(txt_tokenized, lang="rus")
    for index, tagged_token in enumerate(txt_tagged):
        if(index < len(txt_tagged)-1):
            next_token = txt_tagged[index+1]
        if(helper.helper_for_VB(tagged_token[1]) and helper.helper_for_NN(next_token[1])):
            counter_verb_noun+=1
    if(counter_verb_noun+std > lower_limit or counter_verb_noun-std < upper_limit):
        print(counter_verb_noun)
        return 5.0
    else:
        print(counter_verb_noun)
        return 0.0
    
#a=verb_noun_counter(text1)            
#print(a)


def beta_for_imgntn(text):
    beta_value = betafunc.Beta(text)
    lower_limit = 0.48
    upper_limit = 1.25
    std = 0.17
    if(beta_value+std > lower_limit or beta_value-std < upper_limit):
        print(beta_value)
        return 5.0
    else:
        return 0.0
    
#a = beta_for_imgntn(text1)
#print(a)
