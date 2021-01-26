import tags_counter
import math
import ImaginationDetectionFuncs
import MoneyDetectionFuncs
import PublicisticDetectionFuncs
import ScienceDetectionFuncs
import os

#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\pression_recall_materials\fantasy\elerando_1_Akselerando.WCI3Fw.605185.txt', encoding="utf-8").read()
#text1 = open(r'C:\Users\lisin\OneDrive\Рабочий стол\Third semester Sami Shimoon\InformationSearch\project_content\DocumentsToRead\fantasy\cat-yashchikov-Pandory.NMzHKw.606645utf.txt', encoding="utf-8").read()
root_path = "DocumentsToRead/"
list_of_dirs = os.listdir(root_path)

itr = 0


stable_style_mutex_matrix = [
        ["D","None","Бизнес проэкт с научной компонентой","None"],
        ["None","D","Фэнтези","Очерк, фельетон, роман фельетон"],
        ["Бизнес проэкт с научной компонентой","Фэнтези","D","Научно-популярная литература"],
        ["None","Очерк, фельетон, роман фельетон","Научно-популярная литература","D"]
        ]

def takeSecond(elem):
    return elem[1]

def main(txt):
    #Definding
    answer = ""
    flag=False
    art_grade = 0.0
    bus_grade = 0.0
    pub_grade = 0.0
    sci_grade = 0.0
    style_names = [["художественный стиль", 0.0],["деловой стиль", 0.0],["публицистический стиль", 0.0],["научный стиль", 0.0]]
    style_mutex_matrix = stable_style_mutex_matrix
    index1=None
    index2=None
    artf = 0.0
    busf = 0.0
    pubf = 0.0
    scif = 0.0
    root, art, business, publicistic, science = range(5)
    new_vector = tags_counter.counter(txt)
    final_vector = [0,0,0,0]
    artf_vector = [0,0,0,0,0,0,0]
    businessf_vector = [0,0,0,0,0,0,0]
    publicisticf_vector = [0,0,0,0,0,0,0]
    sciencef_vector = [0,0,0,0,0,0,0]

    style_graph = [
                    {art:[0.023760263981509343, 0.35371707875325975, 0.2040443210131834, 0.0963055779346601, 0.0011647325330115476, 0.21527548961053436, 0.04854175587512543],
                     business:[0.056069806798929506, 0.49945164580233187, 0.07646007421162238, 0.0059741687047524935, 5.907447269189139e-06, 0.18718383438799607, 0.00990992596953209],
                     publicistic:[0.026284184790169217, 0.37295947971220544, 0.14745773166597215, 0.05849909233891134, 0.00045761114282080815, 0.19410465682222114, 0.03433783420906395],
                     science:[0.029249357068169668, 0.38194513081644055, 0.12577647720357518, 0.035155040976619326, 0.0001995401875289625, 0.1838662824442813, 0.029586040776505534]}
            ]
    #Text preanalyzis
    
    art_grade += ImaginationDetectionFuncs.verb_noun_counter(txt)
    art_grade += ImaginationDetectionFuncs.beta_for_imgntn(txt)
    bus_grade += MoneyDetectionFuncs.sent_money_Detection(txt)
    bus_grade += MoneyDetectionFuncs.beta_money_Detection(txt)
    pub_grade += PublicisticDetectionFuncs.publicisticDetection(txt)
    pub_grade += PublicisticDetectionFuncs.betaPublicisticDetection(txt)
    sci_grade += ScienceDetectionFuncs.prefixCheck(txt)
    sci_grade += ScienceDetectionFuncs.scienceParamDetection(txt)

    grade_vector = [bus_grade, art_grade, sci_grade, pub_grade]
    
    if(art_grade < 5 and sci_grade < 5):
        style_mutex_matrix[1][2] = "Fantasy(Low connectivity)"
        style_mutex_matrix[2][1] = "Fantasy(Low connectivity)"
    if(art_grade < 5 and pub_grade < 5):
        style_mutex_matrix[1][3] = "Feuilletons(Low connectivity)"
        style_mutex_matrix[3][1] = "Feuilletons(Low connectivity)"

    if(bus_grade < 5 and sci_grade < 5):
        style_mutex_matrix[0][2] = "Bussiness project(Low connectivity)"
        style_mutex_matrix[2][0] = "Bussiness project(Low connectivity)"
    if(sci_grade < 5 and pub_grade < 5):
        style_mutex_matrix[2][3] = "Sciefie(Low connectivity)"
        style_mutex_matrix[3][2] = "Sciefie(Low connectivity)"
    #Vector-distance computation
    itr=0
    for parametre in style_graph[root][art]:
        art_inner_list = [0,0,0,0,0,0,0]
        business_inner_list = [0,0,0,0,0,0,0]
        public_inner_list = [0,0,0,0,0,0,0]
        science_inner_list = [0,0,0,0,0,0,0]
    
        artf_vector[itr] = (new_vector[itr] - style_graph[root][art][itr])**2
        businessf_vector[itr] = (new_vector[itr] - style_graph[root][business][itr])**2
        publicisticf_vector[itr] = (new_vector[itr] - style_graph[root][publicistic][itr])**2
        sciencef_vector[itr] = (new_vector[itr] - style_graph[root][science][itr])**2
        itr+=1
        
    itr2=0
    for i in artf_vector:
        artf += artf_vector[itr2]
        busf += businessf_vector[itr2]
        pubf += publicisticf_vector[itr2]
        scif += sciencef_vector[itr2]
        itr2 += 1

    final_vector = [math.sqrt(artf), math.sqrt(busf), math.sqrt(pubf), math.sqrt(scif)]
    itr3 = 0
    for i in final_vector:
        style_names[itr3][1] = final_vector[itr3]
        itr3 += 1
        
    #print(style_names)
    style_names.sort(key=takeSecond)
    
    if(style_names[0][0]=="деловой стиль"):
        index1 = 0
    elif(style_names[0][0]=="художественный стиль"):
        index1 = 1
    elif(style_names[0][0]=="научный стиль"):
        index1 = 2
    elif(style_names[0][0]=="публицистический стиль"):
        index1 = 3

    if(style_names[1][0]=="деловой стиль"):
        index2 = 0
    elif(style_names[1][0]=="художественный стиль"):
        index2 = 1
    elif(style_names[1][0]=="научный стиль"):
        index2 = 2
    elif(style_names[1][0]=="публицистический стиль"):
        index2 = 3
    #ANSWER
    answer = style_mutex_matrix[index1][index2]

    #Special action
    grade_vector = list(enumerate(grade_vector))
    print("Not normalized grade vector")
    print(grade_vector)
    grade_vector.sort(key=takeSecond, reverse=True)
    print("Normalized grade vector")
    print(grade_vector)
    dis_point = None
    indx2_gr = style_names[1][0]
    if(indx2_gr == "деловой стиль"):
        dis_point = 0
    elif(indx2_gr == "художественный стиль"):
        dis_point = 1
    elif(indx2_gr == "научный стиль"):
        dis_point = 2
    elif(indx2_gr == "публицистический стиль"):
        dis_point = 3
    point2_gr = grade_vector[1][1]
    dis_point2 = grade_vector[dis_point][1]
    #point2_gr = grade_vector[2][1]
    print("second point result ", point2_gr, "second vector result", indx2_gr )    
    if(point2_gr == dis_point2):
        answer = answer + " " + style_mutex_matrix[grade_vector[1][0]][grade_vector[0][0]]
        print("We have 2 results")
        print("Distance index's: ",index1, index2," Point index's: ", grade_vector[1][0], grade_vector[0][0])
    elif(point2_gr > dis_point2):
        current_ans = answer
        print("We prefered point result")
        print("Distance index's: ", index1, index2," Point index's: " ,grade_vector[1][0], grade_vector[0][0])
        answer = style_mutex_matrix[grade_vector[1][0]][grade_vector[0][0]]
        answer = answer + " OR LESS POSIBLE " + current_ans
    else:
        print("Without special action")
        print("Distance index's: ",index1, index2)

    print("Points")
    print(bus_grade, art_grade, sci_grade, pub_grade)
    print("Normalized posibility vector")
    print(style_names)
    print("Final style matrix")
    print(style_mutex_matrix[0],"\n",style_mutex_matrix[1],"\n", style_mutex_matrix[2],"\n", style_mutex_matrix[3])
    print("Answer")
    print(answer)
    print("#####################################################")


#main(text1)
for directory in list_of_dirs:
    folder = root_path + directory
    iner_list_of_dirs = os.listdir(folder)
    for file in iner_list_of_dirs:
        if(file.endswith("utf.txt")):
            with open(folder+"/"+file, "r", encoding="utf-8") as currfile:
                text = currfile.read()
                main(text)
        else:
            with open(folder+"/"+file, "r") as currfile:
                text = currfile.read()
                main(text)
    print("#####################################################")
    print("####################END OF CORPUS####################")
    print("#####################################################")

