import nltk
import remove_chars_from_text
#nltk.help.upenn_tagset()

text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Деловой стиль\Заявления.txt', encoding="utf-8").read()

def counter(text, part_of_speech="default"):
    #Counters
    A_f_and_A_p1_counter=0 #прилагательное
    S_counter=0 #существительное
    V_counter=0 #глагол
    S_PRO_counter=0 #местоимение
    INTJ_counter=0 #междометие
    PR_and_CONJ_counter=0 #частица
    
    #Cleaning
    txt_clean = remove_chars_from_text.remove_chars_from_text(text)
    
    #Tokenization
    txt_tokenized = nltk.tokenize.word_tokenize(txt_clean, language="russian")
    txt_tagged = nltk.tag.pos_tag(txt_tokenized, lang='rus')
    print(len(txt_tokenized))
    #Check Phase
    for token_with_tag in txt_tagged:
            tag = token_with_tag[1]
            if(tag == "A=f" or tag == "A=p1"):
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
                
    return [A_f_and_A_p1_counter, S_counter, V_counter, S_PRO_counter, INTJ_counter, PR_and_CONJ_counter)

print(counter(text1))


