![banner-md-data-analyst](https://github.com/cistelsa/Predictive-Sentiment-Analysis-of-Twitter-for-BTC/assets/17438992/c3a80d3a-a0f5-4766-8ed3-7868e36fb9aa)
# Roadmap: Data Analyst - Bitcoin Analysis
This roadmap outlines the key steps involved in the sentiment analysis of Bitcoin, using a PostgreSQL database in the cloud as the data source. The objective is to analyze the sentiment of tweets related to Bitcoin and correlate it with the price of BTC over time. Additional tasks include creating a dimensional model, installing necessary libraries, performing visualizations with Tableau, practicing storytelling for data visualization, and presenting the findings to Data Engineers and Data Scientists/ML teams. The roadmap is as follows:

- [ ] **Data Extraction from Cloud Database**
  - [ ] Configure a secure connection and proper authentication to access the PostgreSQL database in the cloud.
  - [ ] Write SQL queries to extract relevant Bitcoin-related data, including tweets and BTC prices over time.
  - [ ] Import the extracted data into a local development environment for processing and analysis.

- [ ] **Sentiment Analysis**
  - [ ] Identify and select the appropriate library for sentiment analysis in text, such as NLTK, TextBlob, or VADER.
  - [ ] Preprocess the extracted tweets, including text cleaning, tokenization, and stopword removal.
  - [ ] Apply sentiment analysis techniques to assign sentiment scores to each tweet.
  - [ ] Calculate aggregated sentiment metrics, such as average, standard deviation, or percentage of positive, negative, and neutral sentiments.

- [ ] **Bitcoin Price Analysis**
  - [ ] Utilize suitable libraries like Pandas and NumPy to load and process BTC price data over time.
  - [ ] Perform exploratory analysis on price data, including temporal visualizations and descriptive statistics.
  - [ ] Identify trends, seasonal patterns, or significant events in BTC price.
  - [ ] Calculate additional metrics, such as percentage returns, volatility, or correlation with other Bitcoin-related variables.

- [ ] **Dimensional Model Creation**
  - [ ] Design and create a dimensional model to structure the data optimally for analysis.
  - [ ] Identify key dimensions, such as time, sentiment, price, and establish relationships between them.
  - [ ] Define measures or metrics to be used for analysis, such as average sentiment score, average BTC price, etc.
  - [ ] Load the processed data into the dimensional model and verify data integrity.

- [ ] **Installation of Additional Libraries**
  - [ ] Research and select necessary libraries for sentiment analysis and Tableau visualizations.
  - [ ] Install the selected libraries in the local development environment and ensure compatibility and correct dependencies.

- [ ] **Tableau Visualizations**
  - [ ] Prepare the data from the dimensional model for visualization in Tableau.
  - [ ] Create interactive visualizations that showcase the evolution of tweet sentiment and BTC price over time.
  - [ ] Explore different chart types and tables to highlight patterns and trends.
  - [ ] Configure filters and parameters to enable data exploration by users.

- [ ] **Storytelling and Results Presentation**
  - [ ] Prepare a presentation or report that tells a coherent story based on the results of sentiment analysis and BTC price.
  - [ ] Utilize impactful visualizations to support findings and conclusions.
  - [ ] Explain the insights to Data Engineers, emphasizing the relationship between tweet sentiment and BTC price and its relevance for decision-making.
  - [ ] Communicate the results and implications to Data Scientists/ML teams, providing valuable information for future models and strategies related to Bitcoin.



