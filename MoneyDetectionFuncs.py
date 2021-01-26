import average_length_of_word
import betafunc

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Imagination\imagi1utf.txt', encoding="utf-8").read()

def sent_money_Detection(txt):
    mean_value = 49.0
    std = 11.0
    sent_value = average_length_of_word.average_sent_length(txt)
    if(sent_value - std*2 >= mean_value):
        return 5.0
    elif(sent_value - std >= mean_value or sent_value >= mean_value):
        return 2.5
    else:
        return 0.0



def beta_money_Detection(txt):
    beta_value = betafunc.Beta(txt)
    #print(beta_value)
    upper_limit = 0.19
    lower_limit = 0.057
    std = 0.025
    if(beta_value + std*2.5 < upper_limit):
        return 5.0
    elif(beta_value + std <= upper_limit or beta_value - std >= lower_limit):
        return 2.5
    else:
        return 0.0


def anti_mutex_prefix_Detection(txt):
    prefix=["закон","стать","юри","адвокат","стандарт","служб","Федераци","граждан","Стать","гос"]
    txt_tokenized = average_length_of_word.nltk.word_tokenize(txt, language="russian")
    counter = 0
    for token in txt_tokenized:
        curr = token
        for pref in prefix:
            if(curr.startswith(pref)):
                counter += 1
    return counter


#a = beta_money_Detection(text1) 
#print(a)
