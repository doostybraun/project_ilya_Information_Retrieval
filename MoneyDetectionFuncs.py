import average_length_of_word
import betafunc

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Imagination\imagi1utf.txt', encoding="utf-8").read()

def sent_money_Detection(txt):
    mean_value = 45.0
    std = 15.0
    sent_value = average_length_of_word.average_sent_length(txt)
    if(sent_value - std*2.5 >= mean_value):
        return 5.0
    elif(sent_value - std >= mean_value or sent_value >= mean_value or sent_value):
        return 2.5
    else:
        return 0.0


def beta_money_Detection(txt):
    beta_value = betafunc.Beta(txt)
    print(beta_value)
    upper_limit = 0.18
    lower_limit = 0.024
    std = 0.19
    if(beta_value + std*2.5 < upper_limit):
        return 5.0
    elif(beta_value + std <= upper_limit and beta_value - std >= lower_limit):
        return 2.5
    else:
        return 0.0





#a = beta_money_Detection(text1) 
#print(a)
