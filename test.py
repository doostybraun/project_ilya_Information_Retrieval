import nltk



#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\Money\prikaz3utf.txt', encoding="utf-8").read()


#txt="ультракек перебор максикод гиперзвук"
def prefixCheck(txt):
    prefix=["ультра", "анти", "био", "микро", "макро", "экстра", "мини", "макси", "нео", "нано", "гипер", "суб", "гипо", "экс"]
    txt_tknzd = nltk.tokenize.word_tokenize(txt)
    counter=0
    for token in txt_tknzd:
        currt = token
        for pref in prefix:
            if(currt.startswith(pref)):
                counter+=1
    return counter    
    
#print(counter)
