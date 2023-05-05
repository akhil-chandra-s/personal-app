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
-As an Analytics professional with 4 years of experience, I am highly skilled in statistical analysis, machine learning, and data visualization. My expertise lies in using data to uncover insights and drive business decisions. I have worked in diverse industries, including Insurance, Finance, and risk management clients.

-I have a strong command over programming languages such as Python, R, and SQL and experience in working with big data technologies such as Hadoop and Spark. I have also worked extensively with visualization tools like Tableau and Power BI to create intuitive dashboards and communicate complex information effectively.

-In my previous roles, I have applied statistical modeling techniques to solve complex business problems, develop predictive models, and identify patterns and insights from large datasets. I have experience in developing and deploying machine learning models, including deep learning models, and have worked on natural language processing projects.

-I am an analytical problem-solver with a keen attention to detail and a strong focus on delivering high-quality work. I possess excellent communication skills and have the ability to work effectively in a team-oriented environment.

-Overall, I am an analytical professional with a passion for finding innovative solutions using data-driven approaches. I am committed to leveraging my skills to help organizations drive growth and achieve their business objectives.
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

txt('**Data Science Intern, Cerebral Technologies**, Dallas, TX, USA',
'Jan 2023 - May 2023')
st.markdown('''
- Analyzed health claims data to detect and prevent fraudulent activity, resulting in a 20% reduction in fraudulent claims.
- Conducted data analysis and identify patterns in healthcare utilization, leading to the identification of cost-saving opportunities and the development of new coverage policies that saved clients $2 million annually.
- Developed predictive models to identify high-risk patients, predict health outcomes, and streamline the claims 
adjudication process, resulting in a 15% reduction in claim processing time.

''')

txt('**Data Science Intern, Varunavi Consultants Inc**, Dallas(Remote), USA',
'May 2022 - Aug 2022')
st.markdown('''
- Gathered and evaluated the data on credit risk and developed and deployed a model to identify fraudulent transactions at a rate 15% higher than before.
- Developed an end-to-end MLOps pipeline using AWS Sagemaker to enhance the deployed model continually.
- Created dashboards using Tableau, presented the data and reported conclusions to senior management.

''')

txt('**Analyst II, Verisk Analytics**, Hyderabad, India',
'Apr 2020 - Jul 2021')
st.markdown('''
- Deployed a recommendation system into production to recommend occupancy and construction codes based on a property occupancy and construction description, reducing human processing time by over 50%.
- Coordinated with the business development team to define client interaction that maximized service alternatives, improving conversions by 30%.
- Facilitated end-to-end development, testing, and monitoring of analytical models for 6 insurance clients.
- Automated the geocoding and address cleansing process, cutting data cleansing and data analysis time by 40% while increasing the data service's annual revenue by $350K.
- Led a team of 3 analysts, Improved data quality and performance by 45% by analyzing and modifying python scripts.
- Developed a one-click automation solution combining Python, VBA, SQL, and XML to streamline a tedious data application process and cut processing time by 60%.
''')

txt('**Analyst I, Verisk Analytics**, Hyderabad, India',
'Dec 2020 - Mar 2020')
st.markdown('''
- Applied analytical, statistical, and programming skills to collect, analyze, and interpret 1500+ large data sets.
- Received, cleansed, and prepared client data for risk analysis using catastrophe models and delivered loss statistics within 48 hours.
- Identified potential areas for improvement in the data cleansing, analysis, and reporting process and improved it by automating, increasing team efficiency, and reducing manual labor by 50%.
- Built a dashboard for company KPIs using Tableau, Excel, and SQL to minimize manual reporting by 8 hours.
- Reduced 40% of manual effort by writing efficient SQL queries to extract data for reports and visualizations.

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

txt3('Auto_Claim_Fraud_Detection', 'https://github.com/akhil-chandra-s/AutoClaimFraudDetection')
st.markdown('''
- predict whether auto insurance claim is fradulent or not based on previous data.
- Made use of libraries like Numpy, Pandas, Scikit-Learn, Matplotlib, Seaborn.
- Developed an end to end machine learning pipeline using Amazon Sagemaker.
''')

txt3('Customer_Personality_Analysis', 'https://github.com/akhil-chandra-s/Customer_Personality_Analysis---Marketing_Campaign')
st.markdown('''
- Provide analysis on customer segmentation based on marketing campaign data.
- Made use of libraries like Numpy, Pandas, Scikit-Learn, Matplotlib, Seaborn.
- Used machine leraning models such as K-Means to segment the data.
''')

#####################



st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'www.linkedin.com/in/akhil-chandra-shanivendra')
txt2('GitHub', 'https://github.com/akhil-chandra-s')
