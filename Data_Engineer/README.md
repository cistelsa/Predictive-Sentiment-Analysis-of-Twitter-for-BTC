![banner-md-data-engineer](https://github.com/cistelsa/Predictive-Sentiment-Analysis-of-Twitter-for-BTC/assets/17438992/2f6f6c36-7a01-4e1e-96cf-f89c182cb1ba)
# Roadmap: Data Engineering - Twitter Data Extraction and Preparation for Bitcoin Analysis

This roadmap outlines the key steps involved in the data engineering process for extracting and preparing Twitter data related to Bitcoin using the Tweepy library. It also includes the constant extraction of Bitcoin prices through the Coingecko API to find correlations between Twitter sentiment and BTC price. The roadmap is presented in a checklist format within a code environment (.md file) for easy tracking of tasks. The roadmap is as follows:

- [x] **Twitter Data Extraction**
  - [x] Set up a Twitter Developer account and obtain API credentials.
  - [x] Install and configure the Tweepy library for accessing the Twitter API.
  - [x] Implement code to extract tweets related to Bitcoin based on relevant keywords, accounts, or other criteria using Tweepy.

- [ ] **Deep Data Cleaning**
  - [ ] Perform thorough data cleaning processes to ensure data quality and consistency.
  - [x] Remove duplicate tweets, irrelevant information, and noisy data.
  - [ ] Handle missing values and incorrect data formats.
  - [ ] Apply text preprocessing techniques to clean and normalize the textual content of the tweets.

- [ ] **Database Table Normalization**
  - [ ] Analyze the extracted tweet data to identify key entities and relationships.
  - [ ] Design a normalized database schema that represents the data structure efficiently.
  - [ ] Create separate tables for entities such as tweets, users, hashtags, and mentions.
  - [ ] Establish appropriate primary and foreign key relationships between the tables.

- [ ] **Local Database Architecture**
  - [x] Choose a suitable relational database management system (e.g., MySQL, PostgreSQL) for local data storage.
  - [ ] Set up the database system locally and configure the necessary credentials.
  - [ ] Create the required database tables based on the normalized schema design.
  - [ ] Establish connections between the application and the local database for data insertion and retrieval.

- [ ] **Cloud Deployment on Alibaba Cloud**
  - [x] Evaluate cloud service providers and determine Alibaba Cloud as the preferred option.
  - [x] Create an Alibaba Cloud account and set up the necessary credentials.
  - [ ] Deploy the database system on Alibaba Cloud, ensuring proper security measures and scalability options.
  - [ ] Migrate the local database schema and data to the cloud environment.
  - [ ] Test the connectivity and functionality of the cloud-based database.

- [ ] **ETL Automation**
  - [ ] Develop an ETL (Extract, Transform, Load) process using Python.
  - [ ] Automate the data extraction, cleaning, and loading tasks to ensure regular updates.
  - [ ] Schedule the ETL process to run at specific intervals or trigger it based on specific events.
  - [ ] Implement error handling and logging mechanisms to monitor the ETL process and handle exceptions gracefully.

- [ ] **Documentation Delivery**
  - [ ] Prepare comprehensive documentation detailing the data extraction and preparation process.
  - [ ] Include information about the Twitter API setup, Tweepy library usage, data cleaning procedures, database schema design, and ETL automation.
  - [ ] Share the documentation with the Data Analysts, Machine Learning Engineers, and Data Scientists for their reference and use.
  - [ ] Collaborate with other teams to understand their specific requirements, such as API endpoints, cloud systems, applications, or automation needs.
  - [ ] Provide support and address any questions or requests related to accessing and utilizing the data effectively.

> Note: This roadmap focuses on the Data Engineering tasks related to Twitter data extraction, cleaning, database setup, cloud deployment, ETL automation, and documentation delivery.
