import csv
import random
import time
import numpy as np
import CDR_Recommender as CDR_Recommender

# Function which reads the Database file
def Read_Database():

    # ----------------- Data to be read from database File. -----------------------------------
    # Database File contains list of all phn numbers and list of all sites that will be used for data generation

    List_of_phone_numbers = []
    List_of_Sites = []

    # opening the CSV file
    with open('Database.csv', mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # Iterating the contents of the CSV file and updating our lists
        for lines in csvFile:
            List_of_phone_numbers.append(lines[0])
            List_of_Sites.append((lines[1]))

        # Remove the Headings
        List_of_phone_numbers.pop(0)
        List_of_Sites.pop(0)

        # Remove Empty strings from phn_number list
        # because list of sites is longer, hence it fills phn_number list with empty strings
        List_of_phone_numbers = [i for i in List_of_phone_numbers if i != '']

        # Shuffling the lists
        random.shuffle(List_of_phone_numbers)
        random.shuffle(List_of_Sites)

        file.close()
    # ---------------------------- Database File Read ----------------------------------------------

    return List_of_phone_numbers, List_of_Sites


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


# Function which will generate Data
def Generate_Data(List_of_Sites, Start_Date, End_Date, Num_of_File, Total_users, iteration):

    # 2 csv files - Category_ID.csv and Sites_Categories.csv will be read in every iteration because they may be changed
    Sites_Categories_List = []  # it's a list which will contain lists of the sites of each category.
    Category_ID_Map = {}  # Mapping = Category_ID -> Domain name

    # ------------------- Reading Category.csv--------------------------------------------------
    with open('Category ID.csv', mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # To omit the titles (i.e. Category ID and Category name)
        for lines in csvFile:
            break

        # Iterating through the file contents and updating our Map
        for lines in csvFile:
            Category_ID_Map[lines[0]] = lines[1]

        file.close()
    # ------------------------------------------------------------------------------------------


    # ------------ reading Sites_Categories.csv ------------------------------------------------
    no_of_categories = 0
    with open('Sites_Categories.csv', mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # Iterating through the contents of the CSV file
        for lines in csvFile:
            no_of_categories = len(lines)
            break

        # That number of empty lists appended as how many sites categories are there.
        # Each list will contain sites of one category
        for i in range(no_of_categories):
            Sites_Categories_List.append([])

        # Iterating through the data
        for lines in csvFile:
            for i in range(no_of_categories):
                Sites_Categories_List[i].append(lines[i])

        # Some Categories contain more number of sites than others
        # Hence we have to remove the empty strings appended to other categories while reading the data
        for i in range(no_of_categories):
            Sites_Categories_List[i] = [j for j in Sites_Categories_List[i] if j != '']

        file.close()
    # ----------------------------------------------------------------------------------------

    # -------------------- Data Creation Started ---------------------------------------------

    # Date Settings ---------------
    print("Start Date = ", Start_Date, "     End Date = ", End_Date)
    date_list = np.arange(Start_Date, End_Date, dtype='datetime64[D]')

    # --------------------------------

    # Users which will give certain pattern i.e. they will be biased towards some category
    No_of_Users_to_be_biased = int((8 * Total_users) / 10)  # 80 percent of the users will be biased
    No_of_Random_users = Total_users - No_of_Users_to_be_biased  # Remaining 20% will be random

    # Users_to_be_Biased contains list of phn numbers which are to be biased
    random.shuffle(Currently_Being_used_phn_nos)
    User_to_be_biased = []
    for i in range(No_of_Users_to_be_biased):
        User_to_be_biased.append(Currently_Being_used_phn_nos[i])

    # Random_users contains list of phn numbers which are not to be biased
    Random_users = Currently_Being_used_phn_nos[:]

    for l in User_to_be_biased[:]:
        if l in Random_users:
            Random_users.remove(l)

    # Column lists of the excel files to be generated
    phn_list = []
    Domain_Name_list = []
    day_list = []
    Domain_Category = []
    Bytes_Upload = []
    Bytes_Download = []

    # Biasing_Map = Phn numer -> Category ID biased to
    Biasing_Map = {}

    # First Biased Users Entries will be created and written
    for i in range(No_of_Users_to_be_biased):

        # A user can be biased towards any Site Category
        Biased_to_ID = random.randint(0, no_of_categories - 1)

        # Biasing map updated
        Biasing_Map[User_to_be_biased[i]] = Biased_to_ID

        # Remaining_sites list contain sites other than the sites to which the user is being biased to
        Remaining_sites = List_of_Sites[:]
        for l in Sites_Categories_List[Biased_to_ID][:]:
            if l in Remaining_sites:
                Remaining_sites.remove(l)

        # For each date in a month
        for j in date_list:

            # user can open these many sites only in one day. Max allowed is 10
            n = random.randint(0, min(len(Sites_Categories_List[Biased_to_ID]) - 1, 10))

            random.shuffle(Sites_Categories_List[Biased_to_ID])

            # Creating random list of numbers which will be used as indexes for listing sites from Remaining_sites list
            random_list = random.sample(range(0, len(Remaining_sites) - 1), n)
            ptr = 0

            # For every site opened by the user
            for k in range(n):
                day_list.append(j)
                phn_list.append(User_to_be_biased[i])

                # Whether the site the user will open will be biased site or random site, will be decided by random
                # number generation
                s = random.randint(1, 3)
                num1 = random.randint(2, s + 5)
                num = random.randint(1, num1)

                # Append some Random Site. Probability is very less to go inside this if
                if num == 1:
                    Domain_Name_list.append(Remaining_sites[random_list[ptr]])

                    # Now this random site may belong to some other domain listed in the Sites_Categories List
                    # Hence checking for that
                    flag = 0
                    for b in range(len(Sites_Categories_List)):
                        for h in range(len(Sites_Categories_List[b])):
                            if Remaining_sites[random_list[ptr]] == Sites_Categories_List[b][h]:
                                Domain_Category.append(b + 1)
                                flag = 1
                                break

                    # If the random site does not belong to any category, the 0 is filled
                    if flag == 0:
                        Domain_Category.append(0)

                    ptr = ptr + 1

                    # Less Bytes Upload and Download for this site
                    Bytes_Upload.append(random.random() * 1000)
                    Bytes_Download.append(random.random() * 1000)


                # Append the Biased Site. probability of greater for this
                else:
                    Domain_Name_list.append(Sites_Categories_List[Biased_to_ID][k])
                    Domain_Category.append(Biased_to_ID + 1)
                    Bytes_Upload.append(random.random() * 10000)
                    Bytes_Download.append(random.random() * 10000)

    # Now Entries for random users will be created and filled
    for i in range(No_of_Random_users):

        # Now some random sites may belong to some already categorised lists of sites
        List_of_categorised_domains = []

        # So, we fill all the sites in the list which belong to some or the other category
        for j in range(len(Sites_Categories_List)):
            for v in range(len(Sites_Categories_List[j])):
                List_of_categorised_domains.append(Sites_Categories_List[j][v])

        # For every day
        for j in date_list:

            # Max 10 sites all allowed to open
            n = random.randint(0, 10)

            random.shuffle(List_of_categorised_domains)

            # Again creating a random list whose entries will be used as indexes
            random_list = random.sample(range(0, len(List_of_Sites) - 1), n)  # Random List of Indexes
            ptr = 0

            # For each site
            for k in range(n):

                # A random user will around 10 percent of sites which are already categorised
                # 90 percent of the sites which the random user will open will not belong to any category
                num = random.randint(1, 10)

                # User will open a categorised site
                if num == 1:
                    day_list.append(j)
                    phn_list.append(Random_users[i])
                    Domain_Name_list.append(List_of_categorised_domains[k])
                    flag = 0
                    for b in range(len(Sites_Categories_List)):
                        for h in range(len(Sites_Categories_List[b])):
                            if List_of_categorised_domains[k] == Sites_Categories_List[b][h]:
                                Domain_Category.append(b + 1)
                                flag = 1
                                break
                    if flag == 0:
                        Domain_Category.append(0)

                # User will open any random site
                else:
                    day_list.append(j)
                    phn_list.append(Random_users[i])
                    Domain_Name_list.append(List_of_Sites[random_list[ptr]])
                    flag = 0
                    for b in range(len(Sites_Categories_List)):
                        for h in range(len(Sites_Categories_List[b])):
                            if List_of_Sites[random_list[ptr]] == Sites_Categories_List[b][h]:
                                Domain_Category.append(b + 1)
                                flag = 1
                                break
                    if flag == 0:
                        Domain_Category.append(0)

                    ptr = ptr + 1

                # Bytes uploaded and downloaded will be equal for both types of sites
                Bytes_Upload.append(random.random() * 10000)
                Bytes_Download.append(random.random() * 10000)

    #  ----------------- Writing the UDR data ------------------------------
    header_for_UDR = ['Phone Number', 'Date', 'Domain Name', 'Domain Category ID', 'Bytes Upload', 'Bytes Download']

    UDR_Data = []

    for i in range(len(phn_list)):
        UDR_Data.append([])

        UDR_Data[i].append(phn_list[i])
        UDR_Data[i].append(day_list[i])
        UDR_Data[i].append(Domain_Name_list[i])
        UDR_Data[i].append(Domain_Category[i])
        UDR_Data[i].append(Bytes_Upload[i])
        UDR_Data[i].append(Bytes_Download[i])


    with open("UDR" + str(Num_of_File) + ".csv", 'w', encoding='UTF8') as f:

        writer = csv.writer(f)

        # write the header
        writer.writerow(header_for_UDR)

        # write the data
        writer.writerows(UDR_Data)

    print("UDR Done")

    UDR_Assist_Header = ['Phone Number', "Domain Name", 'Bytes Upload', 'Bytes Download']
    UDR_Assit_Data = []

    Sites_Data_Upload = {}
    Sites_Data_Download = {}

    current_phn_number = phn_list[0]
    ptr_to_assist = 0

    for i in range(len(phn_list)):
        Sites_Data_Upload[UDR_Data[i][2]] = 0
        Sites_Data_Download[UDR_Data[i][2]] = 0

    for i in range(len(phn_list)):
        if(current_phn_number == phn_list[i]):
            Sites_Data_Upload[UDR_Data[i][2]] = Sites_Data_Upload[UDR_Data[i][2]] + UDR_Data[i][4]
            Sites_Data_Download[UDR_Data[i][2]] = Sites_Data_Download[UDR_Data[i][2]] + UDR_Data[i][5]

        else:
            for j in Sites_Data_Upload:

                if(Sites_Data_Upload[j] != 0):
                    UDR_Assit_Data.append([])

                    UDR_Assit_Data[ptr_to_assist].append(current_phn_number)
                    UDR_Assit_Data[ptr_to_assist].append(j)
                    UDR_Assit_Data[ptr_to_assist].append(Sites_Data_Upload[j])
                    UDR_Assit_Data[ptr_to_assist].append(Sites_Data_Download[j])

                    ptr_to_assist = ptr_to_assist + 1

            Sites_Data_Upload.clear()
            Sites_Data_Download.clear()

            for l in range(len(phn_list)):
                Sites_Data_Upload[UDR_Data[l][2]] = 0
                Sites_Data_Download[UDR_Data[l][2]] = 0

            current_phn_number = phn_list[i]
            Sites_Data_Upload[UDR_Data[i][2]] = Sites_Data_Upload[UDR_Data[i][2]] + UDR_Data[i][4]
            Sites_Data_Download[UDR_Data[i][2]] = Sites_Data_Download[UDR_Data[i][2]] + UDR_Data[i][5]


    with open("UDR_Assist" + str(Num_of_File) + ".csv", 'w', encoding='UTF8') as f:

        writer = csv.writer(f)

        # write the header
        writer.writerow(UDR_Assist_Header)

        # write the data
        writer.writerows(UDR_Assit_Data)

    print("UDR Assist Done")

    # -------------------- UDR Data Written ---------------------------------------------


    random.shuffle(Currently_Being_used_phn_nos)

    #  ----------------- Writing the CDR data ------------------------------
    header_for_CDR = ['Phone Number', 'Year/Month', 'Day Mins', 'Int Mins', 'CustServ Calls']

    CDR_Data = []
    for i in range(len(Currently_Being_used_phn_nos)):
        CDR_Data.append([])

        CDR_Data[i].append(Currently_Being_used_phn_nos[i])
        CDR_Data[i].append(Start_Date)
        CDR_Data[i].append(round(random.uniform(0.0, 400.00), 1))
        CDR_Data[i].append(round(random.uniform(0.0, 400.00), 1))
        CDR_Data[i].append(random.randint(0, 10))


    with open("CDR" + str(Num_of_File) + ".csv", 'w', encoding='UTF8') as f:

        writer = csv.writer(f)

        # write the header
        writer.writerow(header_for_CDR)

        # write the data
        writer.writerows(CDR_Data)

    print("CDR Done")
    # -------------------- CDR Data Written ---------------------------------------------

    print("--------------- DATA GENERATION COMPLETED ---------------\n")

    print("--------------- STARTING CDR RECOMMENDATION PROCESS ---------------")

    Latest_CDR_file_name = "CDR" + str(Num_of_File) + ".csv"

    # Calling begin function to begin the recommendation process for the generated CDR dataset
    CDR_Recommender.begin(Start_Date, Header_for_Recommender, Latest_CDR_file_name, iteration)



# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    # We will keep count of iterations
    iteration = 0

    # Reading the Database files
    List_of_phone_numbers, List_of_Sites = Read_Database()

    # ----------------------------------------------------------------------------------------------
    # This list store the phn_numbers that are currently being used for data generation
    Currently_Being_used_phn_nos = []

    # Let's say initially we have only 10 users
    ptr_to_phn_number_list = 0
    for i in range(10):
        Currently_Being_used_phn_nos.append(List_of_phone_numbers[ptr_to_phn_number_list])
        ptr_to_phn_number_list = ptr_to_phn_number_list + 1

    Total_users = len(Currently_Being_used_phn_nos)

    # ----------------------------------------------------------------------------------------------


    # ------------------ Iterations will start Now -------------------------------------------------
    # Input the Interval Time for data generation
    print("--------------- DATA GENERATION STARTED ---------------\n")
    Time = int(input("Enter Interval Time in seconds: "))

    # Initialising variables
    Start_Date = '2012-01'
    End_Date = '2012-02'
    Num_of_File = 1

    Header_for_Recommender = ['Phone Number']

    while True:
        print("--------------- ITERATION NO. " + str(iteration + 1), "INITIALISED ---------------")

        Header_for_Recommender.append(Start_Date)

        # Calling Generate_Data function which will generate CDR and UDR data files
        Generate_Data(List_of_Sites, Start_Date, End_Date, Num_of_File, Total_users, iteration)
        iteration = iteration + 1

        # --------------- Updating the variables for next iteration -----------------
        Start_Date = End_Date[:]

        if (int(End_Date[5] + End_Date[6]) + 1) < 10:
            End_Date = End_Date[:6] + str(int(End_Date[6]) + 1)
        elif 10 <= (int(End_Date[5] + End_Date[6]) + 1) <= 12:
            End_Date = End_Date[0:5] + '1' + str((int(End_Date[5] + End_Date[6]) + 1) % 10)
        else:
            End_Date = End_Date[0:5] + '01'
            End_Date = str(int(End_Date[0] + End_Date[1] + End_Date[2] + End_Date[3]) + 1) + End_Date[4:]

        Num_of_File = Num_of_File + 1


        # Number of new users to be added in this iteration
        # 3 to 10 users will be added in every iteration
        number_of_new_users = random.randint(3, 10)

        # Updating the Currently being used phn number list
        for i in range(number_of_new_users):
            Currently_Being_used_phn_nos.append(List_of_phone_numbers[ptr_to_phn_number_list])
            ptr_to_phn_number_list = ptr_to_phn_number_list + 1

        # No of Total Users Updated
        Total_users = len(Currently_Being_used_phn_nos)


        # Sleep Time :)
        time.sleep(Time)
