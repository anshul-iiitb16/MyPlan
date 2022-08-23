
# MY PLAN

Nowadays, Telecom Companies are keen on reaching out to customers and tailoring custom plans unique to the user as per their requirements. Telecom Companies have a lot of plans to offer to their customers. Filtering the most suitable plan for each customer, and recommending that plan to that customer can be really profitable for telecom businesses. 

We have built a **Phone Plan Recommender System** by collecting the customers’ Data Usage Records and Call Detail Records for the past 1 month and suggesting the best possible plan according to their usage patterns. We have our own created dataset of plans offered by a telecom company.



## Acknowledgements

 - [CDR Dataset](https://www.kaggle.com/datasets/anshulmehtakaggl/cdrcall-details-record-predict-telco-churn)
 - [Phone Plans](https://www.airtel.in/recharge-online)
 - [Top 1 Million Websites](https://www.kaggle.com/datasets/cheedcheed/top1m)


## Approach
- Initial Phase was getting the required data. We looked up various websites for the UDR and CDR datasets. We got the CDR dataset from Kaggle but couldn’t find the UDR dataset anywhere. Hence we decided to generate a UDR dataset of our own.
- Then we prepared an initial database which will contain a list of phone numbers and websites that will be used for data generation.
- Then we prepared the catalog of calls and data plans.
- Finally we coded the data_generation_module and recommender module implementing the required algorithms. 
- We used 2 different approaches, first by catogorising all the user collected data, and then applying K means to it, but as the the data was too big, the visualisation appeared to be a problem. Therefore we recompiled the data for each day, and wrote a K means algorithm to ensure that the data runs everyday, and the centroids are updated on each iteration of the program run.

## Implementation

- All the code has been written in **Python Programming Language**. 
- We have following files:
    - **Calling_Plans.csv**: This file is a catalog of Talktime plans being offered by the company. Initially, there are 12 plans offered each having a unique Plan ID. It has the following columns:
        -   **PLAN ID**: It is a unique ID given to each data plan.
        -   **PLAN TYPE**: Indicates which type of data plan it is.
        -   **VALIDITY(days)**: It indicates the validity of a particular plan in days.
        -   **TALKTIME-DOM**: It mentions the Talktime for domestic calls included in each data plan.
        -   **TALKTIME-INT**: It mentions the Talktime for International calls included in each data plan.

    - **CategoryID.csv**: All categories are assigned a unique ID called CategoryID. It is basically a map with key as CategoryID and value as Category Name. It has the following columns:
        - **Category ID**: It mentions the unique ID given to any category.
        - **Category Name**: It mentions the name of the categories which have been identified. 

    - **CDR_Sample.csv**: Just a sample CDR Data file. CDR data will be generated in a similar format. It has the following column:
        - **Phone Number**: It mentions the list of phone numbers whose data has been generated.
        - **Day Mins**: It mentions the Domestic call time for a customer.
        - **Intl Mins**: It mentions the International call time for a customer.
        - **CustServ Calls**: It mentions the number of calls a customer has made to customer service.

    - **Database.csv**: This file contains a list of all phone numbers and a list of all the sites that will be used for data generation. It has the following columns:
        - **Phone Number**: Mentions list of all the phone numbers to be used in data generation.
        - **List of Websites**: Mentions list of all the websites that are to be used in data generation.

    - **Sites_Categories.csv**: This contains the names of sites listed under the category each of them belongs to.
    - **UDR_Sample.csv**: Just a sample UDR Data file. UDR data will be generated in a similar format. It has the following columns:
        - **Phone Number**: Mentions the list of phone numbers whose data has been generated.
        - **Date**: Mentions date for a particular month.
        - **Domain Name**: Mentions the names of the sites visited by the customer.
        - **Domain Category ID**: Mentions the Category ID of the corresponding Domain name.
        - **Bytes Uploaded**: Mentions the bytes uploaded by the user from that corresponding domain.
        - **Bytes Downloaded**: Mentions the bytes downloaded by the user from that corresponding domain. 

    - **CDR_Recommender.py**: 
        - Generates **Recommendation.csv** which lists the recommended plan for each customer.
        - Read files **Calling_Plans.csv** to get the information about all the data plans being offered.
        - Data Points are marked for customer records and plan records. For each customer record, distance is calculated between all plan records, and that plan is offered to the customer who is nearest to the customer record.
        - **Recommendation Plot** is also made for each iteration of recommendations and is appended in a pdf for each month/iteration.

    - **Data_Generation_Module.py**:
        - Generates CDR and UDR data. In each iteration, new data is generated.
        - Reads files **Database.csv, Sites_Categories.csv, and CategoryID.csv** which helps in data generation involving specific patterns.
        - **UDR_Assist.csv** file is also generated which just mentions names, bytes uploaded and downloaded for all the sites visited by the user in a month.
        - This internally calls **CDR_Recommender.py** to recommend suitable plans to the customers.

    - **KMeans.ipynb**:
        - Uses the generated module from **Data_Generation_Module.py**  to calculate the centeroid of data using K means. 
        - Uses the initiate centroid method to select k datapoints as centroid.
        - After calculating the centroids and errors to change the centroids every iteration, for our purpose we use K = 3 to iterate only 3 times throughout the data.
        - After using Kmeans function, an initial cluster can be formed which helps us create blobs for data formation.

## Libraries Used

- **CSV**: This library was used to create and read from or write into .csv files.
- **Matplolib**: This library was used to draw the recommender plots.
- **PyPDF2**: This library was used to create and merge pdf files. The recommender plots are stored in pdf form.
- **Scikit-learn**: This library was used to create confusion matrix and other elements in our k means algorithm. We also developed an initial model to test this libraries functionality.
- Other common libraries such as **NumPy, time, os, etc**. are also used.

## Flowchart
<img src="https://user-images.githubusercontent.com/77500664/186198940-ada92d68-e547-4fb3-9485-0692dc0238d0.jpg" width="700">

## Algorithms Used and Inferences

Throughout the project duration, we analyzed and implemented multiple algorithms for each task and figured out the best suitable algorithm. The algorithm which fulfilled our requirement, was efficient and faster was finally considered.

  The following Algorithms were considered:
- **Nearest Neighbor Algorithm**: To get the most suitable calling plan for a customer, the Nearest Neighbor Algorithm is used. Customers' records and Dataset of plans have been plotted as **scatter points** on a 2D graph. The plan which is nearest (as inferred by **Euclidian Distance**) to the customer record is recommended to that customer.
     
     For the same purpose, we also tried implementing the cosine similarly algorithm but later dropped the idea because cosine similarly captured the orientation of the points rather than the magnitude. But in our case, magnitude had a great role in deciding the plan for a customer and not only the orientation.
- **K Means Algorithm**:  We looked at various algorithms, to find a median/ usage for multiple data selection of plans for the users. After looking at various algorithms, we chose between **KNN and K-Means**. But as we had to cluster the data instead of creating a regression trend, we ended up using **K Means.**

## Steps To Run The Code

- Keep all the files mentioned above in the same directory.
- Run the file **Data_Generation_Module.py**.
- **INPUTS**: 
    - Once you run the code, it will ask for an **Integer Input** which is the time period for data generation. It is basically the time interval between two data sets generated.
- **NO** need to separately run the **CDR_Recommender.py** file. 
- Data_Generation_Module.py will internally call CDR_Recommender.py

## Output And Results

Following result files will be generated:
- **CDR(iteration_number).csv** - CDR dataset for a particular month in a format similar to that of the CDR_Sample.csv file.
- **UDR(iteration_number).csv** - UDR dataset for a particular month in a format similar to that of the UDR_Sample.csv file.
- **UDR_Assist(iteration_number).csv** - It is a slight modification of the UDR.csv file. It mentions all the sites visited by the customer in a month and the total bytes uploaded and downloaded for that whole month. We don’t mention each site visited day-wise here.
- **Recent_Data.pdf** - It is the recommendation plot for the **recent iteration** that marks the points for customer records and Data-plan records and shows which data-plan point is nearest to each customer record point. That specific plan is recommended to that customer.


- **Results(iteration_number).pdf** - It contains all the recommendation plots for all the iterations. During each iteration, the newly generated plot for that iteration is appended to this pdf file.
- **Recommendation.csv** - It contains the list of phone numbers and the Plan ID of the data plan recommended for each month. 

After the data is generated, we use the KMeans.ipynb and KMeansWebsite.ipynb to create centroids for data and figure various clusters formed between different websites used. We can make **New Categories** or update the existing categories of the websites based on the clustering plot. This task has to be done manually by updating **Sites_Categories.csv** and **Category ID.csv.**

## Screenshots
### Application Screenshots
<!-- ![Screenshot-20220213174103-882x569](https://user-images.githubusercontent.com/77500664/184311798-4a6cf118-0c9a-492a-a861-936dac544ee4.jpg)
![Screenshot-20220213234840-882x569](https://user-images.githubusercontent.com/77500664/184326309-fcbaeb93-622e-41b3-8053-f1009a28b284.png) -->
<img src="https://user-images.githubusercontent.com/77500664/184311798-4a6cf118-0c9a-492a-a861-936dac544ee4.jpg" width="700">
<img src="https://user-images.githubusercontent.com/77500664/184326309-fcbaeb93-622e-41b3-8053-f1009a28b284.png" width="700">

## Assumptions

In the real world, the information that some telecom companies can collect is the websites visited by the users and the bytes uploaded and downloaded from each  website. The data will also contain domestic and international call information for a customer. 

Hence, keeping this in mind, we have used created a Data_Generation Module which is processed as per the following assumptions:

- Initially we will be starting with only 10 users.
- 80 percent of the users are biased toward one of the categories of sites and the rest 20 percent are random users.
- Bytes uploaded and downloaded are higher for the sites towards which the user is biased.
- 3-10 users are added in every next iteration.

## Code Review
- The code written can be much more optimised using advanced concepts of Object Oriented Programming.
- Varibles used throughout the code can be declared in a separate python file instead of declaring them in the main code file.
- One single pattern should be followed when naming the files.

## Future Scope

- We can collect churn data for a customer or identify the customers who gonna churn out and make changes to our data plans by including offers for these customers.
- We can extend our recommender system to be able to make a plan for a customer which is the combination of various other plans assigning a suitable weight to each plan to be included in that. Examples of such plans can be Educational Plans, Social Media Plans, etc.

## Authors

- [Anshul Jindal](https://github.com/anshul-iiitb16)
- [Aryan Singh](https://github.com/RyanWolf11)
