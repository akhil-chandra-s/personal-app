import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Akhil Chandra Shanivendra 
# MS Business Analytics, UTD.
''')

image = Image.open("DP.jpg")
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I am an experienced analyst with a demonstrated history of working in the Analytics space in the development, automation, and software integration for four years. 
- I developed cutting-edge analytical tools and techniques and worked with clients across various domains, including Insurance, financial services, and risk management sectors. 
- Skilled in Python, R, Machine Learning, SQL, C#, VBA, Microsoft Excel, Cloud Computing(AWS), Data Visualization.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" target="_blank">Akhil Chandra</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master of Science** (Business Analytics), *University of Texas at Dallas*, Texas, USA',
'2021-2023')
st.markdown('''
- Deans Excellence Scholarship
- GPA: `3.5`
- Relevant Courses: Advanced Statistics for Data Science, Business Analytics with R, Cloud Computing, Database Management, Applied Machine Learning, Big Data, Programming for Data Science, Predictive Analytics with SAS, Prescriptive Analytics, Organizing for Business Analytics Uisng AWS. 
''')

txt('**Bachelors of Technology** (Information Technology), *Jawaharlal Nehru Technological University*, Hyderabad',
'2013-2017')
st.markdown('''
- GPA: `7.5`
- Graduated with First Class with Distinction.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Science Intern, Varunavi Consultants Inc**, Dallas(Remote), USA',
'May 2022 - Aug 2022')
st.markdown('''
- Worked on credit risk data; presented analysis and made recommendations to assist in reducing losses.
- Utilized Machine Learning methods like Random Forest, Logistic Regression, Classification and Regression Trees.
- Pre-processed and analyzed the data using Python library Pandas and built data visualizations in Tableau.
''')

txt('**Analyst II, Verisk Analytics**, Hyderabad, India',
'Apr 2020 - Jul 2021')
st.markdown('''
- Utilized a state-of-the-art NLP model (BERT) on a recommendation system project, embedded it into the workflow, and reduced the need for human processing time by over 50%.
- Automated geocoding and address cleansing with Python, VBA, and Geocoding APIs, cutting data cleansing time by 40% while increasing data services income by $350,000.
- Created a tool using Python and SQL that streamlines the execution of three complex tasks into a single mouse click, cutting user input by 40%.
- Developed a one-click automation solution combining Python, VBA, SQL, and XML to streamline a tedious data application process and cut processing time by 60%.
''')

txt('**Analyst I, Verisk Analytics**, Hyderabad, India',
'Dec 2020 - Mar 2020')
st.markdown('''
- Improved the existing procedure by automating it using Python, VBA, SQL, and C#, significantly boosting the team's productivity and cutting down on manual labor by 50%.
- Received, cleansed, and prepared client data using Python, SQL, and Excel to do risk analysis using catastrophe models and deliver loss statistics within 48 hours.
- Built a dashboard for company KPIs using Tableau, Excel, and SQL to minimize manual reporting by 8 hours.
- Developed efficient SQL queries to extract data for reports and visualizations, saving 40% manual effort.
- Created a tool that plots address information on a map using Maps API to find invalid addresses 50% faster



''')


#####################


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `SQL`, `SAS`, `VBA`, `C#` ')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`Tableau`, `PowerBI` ,`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`Linear/Logistic Regression`, `Classification and Regression Trees`, `Neural Networks`, `Clustering`, `Association Rules`, `KNN`, `Ensemble Techniques`, `Statistical Analysis.`')
txt3('Databases', '`MySQL`, `SQL-Server`')
txt3('Big Data Technologies', '`Spark`, `Hadoop`, `Kafka`, `MapReduce`, `Sqoop`, `Hive`, `Impala`')
txt3('Others', '`Jupyter Notebook`, `A/B Testing`, `GitHub`, `Agile`, `Git`, `Excel`')
txt3('Certifications', '`AWS Cloud Practitioner`, `Lean Six Sigma Yellow Belt`, `Certified Extreme Event Modeller (CEEM), AIR`, `Oracle Certified SQL Developer`.')

#####################

#####################
st.markdown('''
## Projects
''')
txt3('Credit_Card_Fraud_Detection', 'https://github.com/akhil-chandra-s/Credit_Card_Fraud_Detection')
st.markdown('''
- Predict fraudulent credit card transactions so that the customers of credit card companies are not charged for items that they did not purchase.
- Used libraries like Numpy, Pandas, Scikit-Learn, Matplotlib, pycaret for comparing all models with target model.
- Random Forest was the first model used to predict the outcome, then I compared it with all the models using the pycaret library.
''')
txt3('Customer_Churn_Telecom', 'https://github.com/akhil-chandra-s/Loan_Prediction')
st.markdown('''
- Predict behavior of the telecom customers and analyze all relevant customer data and developed models for customer retention.
- Made use of libraries like Numpy, Pandas, Scikit-Learn, Matplotlib, Seaborn.
- Used machine leraning models such as Logistic regression, KNN, Random Forest, Decision Trees, Gradient Boost.
''')
txt3('Insurance_Claim_Prediction', 'https://github.com/akhil-chandra-s/Insurance_Claim_Prediction')
st.markdown('''
- A simple yet challenging project, to anticipate whether the insurance will be claimed or not.
- Made use of libraries like Numpy, Pandas, Scikit-Learn, Matplotlib, Seaborn.
- Built classification model to predict weather the insurance will be claimed or not and also fine-tune the hyperparameters & compare the evaluation metrics of vaious classification algorithms.
- Used machine leraning models such as Logistic regression, Random Forest, Decision Trees, Gradient Boost, Extreme dradient boosting, Support vector machines.
''')
txt3('Loan_Prediction', 'https://github.com/akhil-chandra-s/Loan_Prediction')
st.markdown('''
- predict whether a loan will be approved for an applicant based on previous data.
- Made use of libraries like Numpy, Pandas, Scikit-Learn, Matplotlib, Seaborn.
- Used machine leraning models such as Logistic regression to predict the outcome.
''')

#####################



st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'www.linkedin.com/in/akhil-chandra-shanivendra')
txt2('GitHub', 'https://github.com/akhil-chandra-s')
