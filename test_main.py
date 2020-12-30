import os
import nltk
import tags_counter


print(os.getcwd())
os.chdir("DocumentsToRead")
f_path = os.getcwd()
print(f_path)
full_comp=[[],[],[],[]]
complete_data = []
data=None
list_of_names = os.listdir()
itr=0
itr2=0
num_of_file=0
print(list_of_names)
while itr<len(list_of_names):
    #Start being in Delovoy
    os.chdir(list_of_names[itr])
    print(os.getcwd())
    new_list = os.listdir()
    print(new_list)
    current_path = os.getcwd()+"/"
    while itr2<len(new_list):
        data = open(current_path+new_list[itr2], encoding="utf-8")
        data = data.read()
        complete_data = tags_counter.counter(data)
        full_comp[itr] = complete_data
        print(full_comp,complete_data)
        itr2+=1
        print(os.getcwd())
       
        #tokenized_data = nltk.tokenize.word_tokenize(data)
        #print(len(tokenized_data))
    os.chdir(f_path)
    itr+=1


