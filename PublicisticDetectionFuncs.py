import betafunc
import ScienceDetectionFuncs
import tags_counter
import same_neighbors_counter
import average_length_of_word

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\PublicisticStyle\public8.txt').read()


def publicisticDetection(text):
    grade = 0.0
    #vector = tags_counter.counter(text)
    beta = betafunc.Beta(text)
    prefix = ScienceDetectionFuncs.numPrefixCheck(text)
    NN_value = same_neighbors_counter.NN_same_neighbors(text)
    if(beta > 0.22 and prefix < 90):
        """Сейчас этот текст скорее всего не имеет признаки делового или научного стилей"""
        grade = 2.5
        #print(NN_value)
        if(NN_value >= 400):
            """Сейчас этот текст имеет признаки публицистического текста"""
            grade = 5.0
            #print(grade)
            return grade
        else:
            #print(grade)
            return grade
    else:
        #print(grade)
        return grade



def betaPublicisticDetection(text):
    grade = 0.0
    beta = betafunc.Beta(text)
    sent_len = average_length_of_word.average_sent_length(text)
    prefix = ScienceDetectionFuncs.numPrefixCheck(text)
    text_vector = tags_counter.counter(text)
    if(text_vector[0] < 0.025 and beta < 0.5):
        grade = 2.5
        if(prefix < 70):
            grade = 5.0
            return grade
        else:
            return grade
    else:
        return grade
    


    
#a = publicisticDetection(text1)
#print(a)

