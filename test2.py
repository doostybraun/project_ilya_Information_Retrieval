import os
import tags_counter
import ScienceDetectionFuncs
import nltk

freqall=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
style_names = ["художественный стиль","деловой стиль","публицистический стиль","научный стиль"]
path_root = "DocumentsToRead/"
amount_of_words = [0,0,0,0]
list_of_dirs = os.listdir(path_root)


itr=0
for directory in list_of_dirs:
    folder = path_root + directory
    iner_list_of_dir = os.listdir(folder)
    num_of_files = 0
    maximus=[0,0,0,0,0,0]
    maxFilename = ["","","","","",""]
    average_prefix = [0,0,0,0]
    for file in iner_list_of_dir:
        if(file.endswith("utf.txt")):
            with open(folder+"/"+file, "r", encoding="utf-8") as currfile:
                text = currfile.read()
                freq = tags_counter.counter(text)
                average_prefix[itr] += ScienceDetectionFuncs.prefixCheck(text)
                amount_of_words[itr] += len(nltk.tokenize.word_tokenize(text))
                itr2=0
                for feature in maximus:
                    if(maximus[itr2] < freq[itr2]):
                        maximus[itr2] = freq[itr2]
                        maxFilename[itr2] = file
                    itr2+=1
                print(average_prefix[itr])
                print(freq)
                freqall[itr] = [x+y for x, y in zip(freq, freqall[itr])]
        else:
            with open(folder+"/"+file, "r") as currfile:
                text = currfile.read()
                freq = tags_counter.counter(text)
                average_prefix[itr] += ScienceDetectionFuncs.prefixCheck(text)
                amount_of_words[itr] += len(nltk.tokenize.word_tokenize(text))
                itr2=0
                for feature in maximus:
                    if(maximus[itr2] < freq[itr2]):
                        maximus[itr2] = freq[itr2]
                        maxFilename[itr2] = file
                    itr2+=1
                print(average_prefix[itr])
                print(freq)
                freqall[itr] = [x+y for x, y in zip(freq, freqall[itr])]
        num_of_files+=1
    freqall[itr] = [x/num_of_files for x in  freqall[itr]]
    average_prefix[itr] = average_prefix[itr]/num_of_files
    print( "Среднее значение по ",style_names[itr])
    print( freqall[itr])
    print("Максимальное значение статистического профиля по подкорпусу")
    print(maximus)
    print("Имена файлов с максимальными показателями")
    print(maxFilename)
    print("Среднее значение количества научных prefix по подкорпусу")
    print(average_prefix[itr])
    itr+=1
print(amount_of_words)
