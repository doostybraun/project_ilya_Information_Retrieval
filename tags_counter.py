import nltk
import remove_chars_from_text
import unique_words_counter
#nltk.help.upenn_tagset()

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\ocherk\Эдик Штейнберг.txt').read()

def counter(text, part_of_speech="default"):
    #Counters
    A_f_and_A_p1_counter=0 #прилагательное
    S_counter=0 #существительное
    V_counter=0 #глагол
    S_PRO_counter=0 #местоимение
    INTJ_counter=0 #междометие
    PR_and_CONJ_counter=0 #частица
    ADV_counter=0
    
    #Cleaning
    txt_clean = remove_chars_from_text.remove_chars_from_text(text)
    txt_clean_tokenized = nltk.tokenize.word_tokenize(txt_clean, language="russian")
    #Tokenization
    txt_tokenized = nltk.tokenize.word_tokenize(text, language="russian")
    txt_tagged = nltk.tag.pos_tag(txt_tokenized, lang='rus')
    #Check Phase
    for token_with_tag in txt_tagged:
            tag = token_with_tag[1]
            if(tag == "A=f" ):
                A_f_and_A_p1_counter+=1
            elif(tag == "S"):
                S_counter+=1
            elif(tag == "V"):
                V_counter+=1
            elif(tag == "S-PRO"):
                S_PRO_counter+=1
            elif(tag == "INTJ"):
                INTJ_counter+=1
            elif(tag == "PR" or tag == "CONJ"):
                PR_and_CONJ_counter+=1
            elif(tag == "ADV"):
                ADV_counter+=1
                
    return [A_f_and_A_p1_counter/len(txt_clean_tokenized), S_counter/len(txt_clean_tokenized), V_counter/len(txt_clean_tokenized), S_PRO_counter/len(txt_clean_tokenized), INTJ_counter/len(txt_clean_tokenized), PR_and_CONJ_counter/len(txt_clean_tokenized), ADV_counter/len(txt_clean_tokenized)]

#print(counter(text1))



