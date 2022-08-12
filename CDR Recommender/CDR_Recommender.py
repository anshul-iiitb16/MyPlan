import csv
import matplotlib.pyplot as plt
import sys
import math
from PyPDF2 import PdfFileMerger
import os

# Function which reads the Data Plans Info offered by the telecom company
def Plan_Info():
    Plan_Info = []

    # opening the CSV file
    with open('Calling_Plans.csv', mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # Iterating the contents of the CSV file and updating our lists

        for lines in csvFile:
            break

        for lines in csvFile:
            Plan_Info.append([])
            for i in lines:
                Plan_Info[len(Plan_Info) - 1].append(i)

        file.close()
    # ---------------------------------------------------------

        return Plan_Info


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


# Function which recommends the plan to the users
def Recommend(Plan_Info, iteration_count, Start_Date, Header_for_Recommender, Latest_CDR_file_name):

    # Reading the latest created CDR file for Call Data information of the customers
    Call_Data_Info = []

    # opening the CSV file
    with open(Latest_CDR_file_name, mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # Iterating the contents of the CSV file and updating our lists

        for lines in csvFile:
            break

        for lines in csvFile:
            Call_Data_Info.append([])
            for i in lines:
                Call_Data_Info[len(Call_Data_Info) - 1].append(i)


        file.close()

    # ------------------------------------------------------------------------------------------

    # First read all the data from the previously created Recommendation file. And we will append new data.
    Data_Read = []
    with open("Recommendation.csv", mode='r') as f:
        # reading the CSV file
        csvFile = csv.reader(f)

        # Iterating the contents of the CSV file and updating our lists

        for lines in csvFile:
            break

        for lines in csvFile:
            Data_Read.append([])
            for i in lines:
                Data_Read[len(Data_Read) - 1].append(i)

        file.close()

    # This is the list of phn numbers which were present in the previous iteration also
    old_phn_numbers = []
    for i in range(len(Data_Read)):
       old_phn_numbers.append(Data_Read[i][0])

    # This is the list of all the phone numbers included in the CDR file
    # From this list and old phone numbers lise, we will get the list of newly added phone numbers in this iteration
    All_phn_numbers = []
    for i in range(len(Call_Data_Info)):
        All_phn_numbers.append(Call_Data_Info[i][0])

    # Mappping = Phone Number -> Recommended Plan ID
    Phn_number__Recommended_Plan_Map = {}

    # List of new phone numbers added in this iteration
    New_phn_Numbers = []
    for i in All_phn_numbers:
        if i not in old_phn_numbers:
            New_phn_Numbers.append(i)


    # To calculate the best plan for a customer, we will take a set (DOM calls, INT Calls) for each customer
    # We will take similar set of values for the data plans being offered by the telecom
    # Then for each customer record/set, we will calculate distance of that set from every set/point of Data plans and whichever is nearest, that plan will be offered
    for i in range(len(Call_Data_Info)):
        min = sys.maxsize
        Plan_ID_Recommended = -1

        # A list will contain Customer Data
        A = []
        A.append(float(Call_Data_Info[i][2]))
        A.append(float(Call_Data_Info[i][3]))

        for j in range(len(Plan_Info)):

            # B list will contain Plan record
            B = []
            B.append(float(Plan_Info[j][3]))
            B.append(float(Plan_Info[j][4]))

            # Calculating the Distance between the 2 data points/records
            Distance = abs(math.dist(A, B))

            if Distance < min:
                min = Distance
                Plan_ID_Recommended = j + 1

                # That plan will be recommended
                Phn_number__Recommended_Plan_Map[Call_Data_Info[i][0]] = Plan_ID_Recommended


    # Now we shall finalise the data which has to be written in Recommendation file
    # This data will be the combination of the old data that we read and the new recommendations
    Data_to_be_written = []
    for i in range(len(Call_Data_Info)):
        Data_to_be_written.append([])

        # If this is a new phone number added in this iteration, then we have to leave blank some spaces for the previous months when this customer was not there
        if Call_Data_Info[i][0] in New_phn_Numbers:
            Data_to_be_written[i].append(Call_Data_Info[i][0])

            # Hence we append blank string for the months data for the new customer
            for j in range(iteration_count):
                Data_to_be_written[i].append('')

            Data_to_be_written[i].append(Phn_number__Recommended_Plan_Map[Call_Data_Info[i][0]])

        # If the phone number is old, then we first write its previous records and then the new one
        else:
            for j in range(len(Data_Read)):
                if(Call_Data_Info[i][0] == Data_Read[j][0]):
                    for k in range(len(Data_Read[j])):
                        Data_to_be_written[i].append(Data_Read[j][k])

                    Data_to_be_written[i].append(Phn_number__Recommended_Plan_Map[Call_Data_Info[i][0]])
                    break


    # Now we write this data
    with open("Recommendation.csv", 'w', encoding='UTF8') as f:

        writer = csv.writer(f)

        # write the header
        writer.writerow(Header_for_Recommender)

        writer.writerows(Data_to_be_written)

    return Call_Data_Info, Phn_number__Recommended_Plan_Map


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# Drawing some graphs
# Plan Records are marked as Stars
# Customer Records as dots
def visualise(Plan_Info, Call_Data_Info, Start_Date, Phn_number__Recommended_Plan_Map, iteration):

    x1 = []
    y1 = []
    x2 = []
    y2 = []

    z1 = []
    z2 = []

    markers = []
    for i in range(len(Plan_Info)):
        x1.append((int(Plan_Info[i][3])))
        y1.append(int(Plan_Info[i][4]))
        markers.append("*")
        z1.append(i+1)

    for i in range(len(Call_Data_Info)):
        x2.append(int(float(Call_Data_Info[i][2])))
        y2.append(int(float(Call_Data_Info[i][3])))
        markers.append(".")
        z2.append(Call_Data_Info[i][0])

        # Marking the arrow
        plt.arrow(x2[i], y2[i], int(Plan_Info[Phn_number__Recommended_Plan_Map[Call_Data_Info[i][0]] - 1][3]) - x2[i], int(Plan_Info[Phn_number__Recommended_Plan_Map[Call_Data_Info[i][0]] - 1][4]) - y2[i], head_width = 0.5, length_includes_head = True)

    # plotting points as a scatter plot
    plt.scatter(x1, y1, label="Plans", color="green", marker="*", s=30)
    plt.scatter(x2, y2, label="Customer_Record", color="Blue", marker=".", s=60)

    # Writing the text
    for i, txt in enumerate(z1):
        plt.annotate(txt, (x1[i] - 4, y1[i] - 8))

    for i, txt in enumerate(z2):
        plt.annotate(txt, (x2[i] - 4, y2[i] - 8))


    # x-axis label
    plt.xlabel('DOM calls')
    # frequency label
    plt.ylabel('INT Calls')
    # plot title
    plt.title('Recommendation Plot: ' + str(Start_Date))
    # showing legend
    plt.legend()

    # Saving the graphs as pdf
    # Pdf's for each month CDR Recommendation will be combines as one pdf
    old_pdf_name = "Results" + str(iteration) + ".pdf"
    new_pdf_name = "Results" + str(iteration + 1) + ".pdf"

    if iteration == 0:
        plt.savefig(new_pdf_name, format="pdf", bbox_inches="tight")

    if iteration > 0:
        Recent_pdf_name = 'Recent_Data.pdf'

        plt.savefig(Recent_pdf_name, format="pdf", bbox_inches="tight")

        # Merger
        merger = PdfFileMerger()
        # Create a list with file names
        pdf_files = [old_pdf_name, Recent_pdf_name]

        # Iterate over the list of file names
        for pdf_file in pdf_files:
            # Append PDF files
            merger.append(pdf_file)


        # Write out the merged PDF
        merger.write(new_pdf_name)
        merger.close()

        os.remove(old_pdf_name)

    # function to show the plot
    print("--------------- RECOMMENDATION PROCESS COMPLETED - SHOWING THE DATA PLOT ---------------")

    print("--------------- ITERATION NO. " + str(iteration + 1), "COMPLETED ---------------\n")


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

def begin(Start_Date, Header_for_Recommender, Latest_CDR_file_name, iteration):

    # In very first iteration, we create a Recommendation csv file
    # In later Iterations we will be appending to this file only
    if iteration == 0:
        with open("Recommendation.csv", 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(Header_for_Recommender)


    Plan_info = Plan_Info()

    Call_Data_Info, Phn_number__Recommended_Plan_Map = Recommend(Plan_info, iteration, Start_Date, Header_for_Recommender, Latest_CDR_file_name)

    visualise(Plan_info, Call_Data_Info, Start_Date, Phn_number__Recommended_Plan_Map, iteration)