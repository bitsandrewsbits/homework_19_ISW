#homework__19
#Information System - Workers(ISWorkers)

import functions_19_ISW as f19

worker_id = 0
file = input("Enter name of file for ISWorkers: ")
#creating tmp file for checking that file is exist or not
check_file = open(file + ".txt", "at")
check_file.close()

tmp_storage = f19.reading_file(file)[0]
worker_id = f19.reading_file(file)[1] + 1  #reading last ID in file of ISWorkers

while True:
    user_command = input("Enter your command [or press finish to exit from programm]: ")

    if user_command == "helpme":
        f19.helpme()
    elif user_command == "add":
        worker_id = f19.add(tmp_storage, worker_id)

    elif user_command == "del":
        f19.deleting(tmp_storage)
        
    elif user_command == "show all":
        f19.show_all(tmp_storage)

    elif user_command == "find":
        f19.find_worker(tmp_storage)

    elif user_command == "change one":
        f19.update_info(tmp_storage)

    elif user_command == "save":
        f19.write_to_file(tmp_storage, file)

    elif user_command == "find by letter":
        f19.find_FL_workers(tmp_storage)
        
    elif user_command == "find by age":
        f19.age_workers(tmp_storage)
        
    elif user_command == "finish":
        f19.write_to_file(tmp_storage, file)
        print("All information was saving successfully!")
        print("Bye")
        break
    
