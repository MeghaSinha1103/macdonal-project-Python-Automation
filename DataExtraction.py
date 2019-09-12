def main():

    import csv
    import json
    import pandas as pd
    import re
    #Open the csv file for reading
    data = list(csv.reader(open("D:\\Uc Arts\\\export sample data\\identify-a-person-classifications.csv", "rt"), dialect="excel"))
    list_n = []
    records = {"name":"","birth_year":"","death_year":"","gender":"","previous_name":""} #records 
    big_list = []
    print("StART")
    for i, row in enumerate(data):
        #print("Done")
        if i != 0:
            currentCard = row[11]
            subject_id = row[13]
            jsonCard = json.loads(currentCard)
            #print(jsonCard)
            womenOnThisCard = 0
            previous_name_of_person =""
            name_of_person=""
            gender_of_person=""
            year_of_birth =""
            year_of_death=""
            previous_name_of_person=""
            for j, currentTask in enumerate(jsonCard):
                #print(currentTask)
                taskNumber = currentTask.get("task")
                #print("new row")
                if taskNumber == "T5":
                    #print("Entered T5")
                    name_of_person = currentTask.get("value")
                    #print(name_of_person)
                if taskNumber == "T6":
                    #print("Entered T6")
                    name_of_person = currentTask.get("value")
                    #print(name_of_person)
                if taskNumber == "T7":
                    #print("Entered T7")
                    previous_name_of_person = currentTask.get("value")
                    #print(previous_name_of_person)
                if taskNumber == "T3":
                    #print("Entered T3")
                    gender_of_person = currentTask.get("value")
                    #$print(gender_of_person)
                if taskNumber == "T1":
                    #print("Entered T1")
                    year_of_birth = currentTask.get("value")
                    #print(year_of_birth)
                if taskNumber == "T4":
                    #print("Entered T4")
                    year_of_death = currentTask.get("value")
                    #print(year_of_death)
                if taskNumber == "T2":
                    #print("Entered T2")
                    #records.insert(name = name_of_person,gender = gender_of_person,birth_year = year_of_birth,death_year = year_of_death, previous_name = previous_name_of_person )
                    names = name_of_person.strip().split(" ")
                    firstname= ""
                    lastname=""
                    if len(names) > 1:
                        lastname = names[-1]
                        firstname = ', '.join(names[:-1])
                    else:
                        firstname = ', '.join(names[:])
                    list_n = ["",lastname,firstname,"",previous_name_of_person, gender_of_person,year_of_birth,year_of_death,"","","",subject_id,"",""]
                    #print(list_n)
                    name_of_person=""
                    gender_of_person=""
                    year_of_birth =""
                    year_of_death=""
                    previous_name_of_person=""
                    big_list.append(list_n)
       
    info_df = pd.DataFrame(big_list, columns =['Record type','Family Name','First Name','Title','Known as','Person Type','Birth','Death','Life date notes','Occupation/Notes','Omnibus ref','subject_id',"Path","URL"])
    info_df = info_df.astype({'subject_id':str})
    

    subject_df =   pd.read_csv("D:\\Uc Arts\\\export sample data\\macdonald-dictionary-subjects.csv", usecols=['metadata','subject_id'])
    def split_it(body):
        st= re.findall(r'\"i(.+?.jpg)\"', body)
        img_list = []
        for s in st:
            img_list.append(s.split(":")[1].replace('"',''))
        rt_str = ', '.join(img_list)
        return rt_str
    subject_df['FileName'] = subject_df['metadata'].apply(split_it)
    subject_df = subject_df.astype({'subject_id':str})
    subject_df.drop(columns=['metadata'])
    #subject_df = subject_df['image_names','subject_id']
    print(subject_df.head())
    cols = ['Record type','Family Name','First Name','Title','Known as','Person Type','Birth','Death','Life date notes','Occupation/Notes','Omnibus ref','subject_id',"Path",'FileName',"URL"]
    df_merge_col = pd.DataFrame(pd.merge(info_df, subject_df, on='subject_id',how = "left"), columns=cols)
    df_merge_col= df_merge_col.rename(columns={'subject_id':'No'})
    print(df_merge_col.head())
    df_merge_col.to_csv(r'D:\\Uc Arts\\export sample data\\import_to_museum.csv',index = False)
    


if __name__ == "__main__":
  main()
