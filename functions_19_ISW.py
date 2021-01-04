#functions Information System - Workers

#data structure - [{'ID': numX, 'first_name': "first_nameN", 'last_name': "last_nameN", 'telefone': "telN",
#     'work_email': "work@...", 'position': "positionN", "ageN": numN, 'skype': 'ejrog@skype.com'}, {...}]

#saving FORMAT in FILE
#Worker#N
#ID -> numX
#first_name -> first_nameN
#and so on...

#open and reading user file
def reading_file(user_file):
    last_id = 0
    data_file = open(user_file + ".txt", "rt")
    strs = data_file.readlines()  #amount strings in file
    res_data = []
    
    if len(strs) == 0:  #if file is empty - creating this file. It was creating beforehand in main file
        print("File", user_file, "doesn't exist. Creating new file", user_file + ".txt")
    else:
        num_str = -1             #counter for list of filling workers
        for i in range(len(strs)):
            #как-то нужно прочитать и конвертировать данные о сотруднике в список из файла.
                
            if len(strs[i].split(' ')) == 1:  #indicator new Worker title (in file - Worker#N)
                res_data.append({})          #adding dictionary for one worker
                num_str += 1
            else:
                if strs[i][:-1] == "Last Worker":  #if we seeing the last worker - send programm next ID
                    continue

                elem_str = strs[i].split(' ')     #find string with key ID and split it
                if elem_str[0] == "ID":
                    last_id = int(elem_str[2][:-1])   #pull ID of last worker in file
                
                res_data[num_str][elem_str[0]] = elem_str[2][:-1]  #without last element in string - '\n'
             
    data_file.close()
    
    return [res_data, last_id]

#writting data to file
def write_to_file(data_list, user_file):
    res_file = open(user_file + ".txt", 'wt')

    for i in range(len(data_list)):
        if i == len(data_list) - 1:
            res_file.write("Last Worker\n")
        res_file.write("Worker#" + str(i) + '\n')
        for key in data_list[i]:
            res_file.write(key + " -> " + str(data_list[i][key]) + '\n')
            
    res_file.close()
    

#helpme

def helpme():
    print("press add - to adding worker to storage\n" +
          "press del - to delete one worker from storage\n" +
          "press show all - to show you all data of workers in storage\n" +
          "press find - to find one worker by last name in storage\n" +
          "press change one - to changing some data for one worker in storage\n" +
          "press save - to saving current data to file" +
          "press find by letter - to find all workers that last name start from input letter\n" +
          "press find by age - to find all workers that one age\n")

#add
def add(storage, tmp_id):
    tmp_dict = {}
    
    while True:
        user_first_name = input("Enter first name [or nothing to exit]: ")
        user_last_name = input("Enter surname [or nothing to exit]:")
        
        if user_first_name == "" or user_last_name == "":
            break

        user_telefone = input("Enter your telefone: ")
        user_work_email = input("Enter you work email: ")
        user_position = input("Enter your position in company: ")
        user_age = int(input("Enter age of worker: "))
        user_skype = input("Enter skype: ")
        
        tmp_dict['ID'] = tmp_id
        tmp_dict['first_name'] = user_first_name
        tmp_dict['last_name'] = user_last_name
        tmp_dict['telefone'] = user_telefone
        tmp_dict['position'] = user_position
        tmp_dict['work_email'] = user_work_email
        tmp_dict['age'] = user_age
        tmp_dict['skype'] = user_skype

        storage.append(tmp_dict)
        tmp_dict = {}

        tmp_id += 1

        return tmp_id
    
#del
def deleting(storage):
    while True:
        l_name_ID = input("Enter worker ID or last name [or nothing to exit]: ")
        if l_name_ID == "":
            break
        for i in range(len(storage)):
            if storage[i]['last_name'] == l_name_ID or str(storage[i]['ID']) == l_name_ID:
                storage.remove(storage[i])
                break
    return True

#show
def show_all(storage):
##    print(storage)
    print(" ", "ID\Last Name\t\tFirst Name\t\tTelefone\tWork email\tPosition\tAge\t\tSkype")  #title of output fields
    
    for i in range(len(storage)):
        print(" ", storage[i]['ID'], "\t", storage[i]['last_name'], storage[i]['first_name'],'\t', "\t",
              storage[i]['telefone'], "\t", storage[i]['work_email'], "\t", storage[i]['position'],
              "\t", storage[i]['age'], "\t", storage[i]['skype'])
    return True

#finding
def find_worker(storage):
    while True:
        l_name_ID = input("Enter worker-ID or last name [or nothing to exit]: ")
        if l_name_ID == "":
            break
        for i in range(len(storage)):
            if storage[i]['last_name'] == l_name_ID or str(storage[i]['ID']) == l_name_ID:
##                file_worker = open("worker_" + storage[i]['last_name'] + "_" + storage[i]['first_name'] + '.txt', "wt")

                write_to_file([storage[i]], "worker_" + storage[i]['last_name'] + "_" + storage[i]['first_name'])
                
##                file_worker.close()
                break
    return True

#replace
def update_info(storage):
    while True:
        l_name_ID = input("Enter worker-ID or last name [or nothing to exit]: ")
        if l_name_ID == "":
            break
        for i in range(len(storage)):
            if storage[i]['last_name'] == l_name_ID or str(storage[i]['ID']) == l_name_ID:

                print("Choose fields for changing information in fields [or press nothing to don't changing info]\n")
                user_last_name = input("Enter worker new last name: ")
                user_first_name = input("Enter worker new first name: ")
                user_telefone = input("Enter worker new telefone: ")
                user_work_email = input("Enter worker new work email: ")
                user_position = input("Enter worker new position in company: ")
                user_age = int(input("Enter worker new age: "))
                user_skype = input("Enter your new skype: ")

                if user_last_name != "":
                    storage[i]['last_name'] = user_last_name
                if user_first_name != "":
                    storage[i]['first_name'] = user_first_name
                if user_telefone != "":
                    storage[i]['telefone'] = user_telefone
                if user_work_email != "":
                    storage[i]['work_email'] = user_work_email
                if user_position != "":
                    storage[i]['position'] = user_position
                if user_age != "":
                    storage[i]['age'] = user_age
                if user_skype != "":
                    storage[i]['skype'] = user_skype
                break
    return True

#finding workers by first letter
#(FL - First Letter in the name of function)

def find_FL_workers(storage):
    match_letter = input("Enter first letter of last name worker: ")
    result_file = open("first_letter_workers.txt", "wt")
    result_file.write("Total workers that last name started from letter '" + match_letter + "':\n")
    
    for i in range(len(storage)):
        #for independency of up or lower case inputing!
        if storage[i]['last_name'][0].lower() == match_letter.lower():
            result_file.write("\nWorker: " + storage[i]['last_name'] + " " + storage[i]['first_name'] + "\n")
            for key in storage[i]:
                result_file.write(key + "-->" + str(storage[i][key]) + "\n")

    result_file.close()


#finding workers by age
def age_workers(lst):
    user_age = int(input("Enter age for finding: "))
    res_file = open("OneAge_Workers.txt", "wt")  #now open file for adding information about workers
    res_file.write("Total workers that age = " + str(user_age) + "\n")
##    print(storage)
    for i in range(len(lst)):
##        print(storage[i]['age'])
        if lst[i]['age'] == str(user_age):
##            print(lst[i]['age'])
            res_file.write("\nWorker: " + lst[i]['last_name'] + " " + lst[i]['first_name'] + "\n")
            for key in lst[i]:
                res_file.write(key + "-->" + str(lst[i][key]) + "\n")

    res_file.close()
