import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Akhil Chandra Shanivendra 
# MS Business Analytics, UTD.
##### *Resume* 
''')

image = Image.open("DP.jpg")
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I am an experienced analyst with a demonstrated history of working in the Analytics space in the development, automation, and software integration for four years. 
- I developed cutting-edge analytical tools and techniques and worked with clients across various domains, including Insurance, financial services, and risk management sectors. 
- Skilled in Python, R, Machine Learning, SQL, NoSQL, C#, VBA, Microsoft Excel, Cloud Computing(AWS), Data Visualization.
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
- Relevant Courses: Advanced Statistics for Data Science, Business Analytics with R, Cloud Computing, Database Management, Applied Machine Learning, Big Data, Programming for Data Science, Predictive Analytics with SAS. 
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

txt('**Analyst II, Verisk Analytics**, Hyderabad, India',
'Apr 2020 - Jul 2021')
st.markdown('''
- Collaborated on a recommendation system project utilizing a state-of-the-art language model for NLP(BERT), integrated it into the work environment, and reduced the manual processing time by almost 50%.
- Automated the Geocoding and Address cleansing process using Python, VBA, and Geocoding APIs, which increased the revenue of the data services division by almost $350,000
- Designed a custom application using Python and SQL, allowing users to execute three complex processes with a single click, thus eliminating manual intervention and reducing the processing time by 40%.
- Developed a single click automation solution for a complex data application process using Python, VBA, SQL, XML, which reduced the data application time by 60%.
- Written Hive and Impala queries for data analysis and ETL, loaded the data into tables to meet the business requirements.
''')

txt('**Analyst I, Verisk Analytics**, Hyderabad, India',
'Dec 2020 - Mar 2020')
st.markdown('''
- Improved and streamlined the process by automating the existing workflow applying Python, VBA, SQL, and C#, which increased the team's efficiency and reduced the manual work time by 50%.
- Performed data modeling and prepared data in databases for various downstream analytical tools.
- Worked on an internal tool to build a data linage to enable the team to trace the issues in case of inquiries.
- Developed ETL processes using a combination of SQL, Python, Spark, and Hive
- Built data visualizations using Tableau, Excel, SQL for business KPIs that reduced manual reporting by 8 hours.
- Developed efficient SQL queries to create tables extract data for uploading, reporting, and visualizations.
''')


#####################


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `SQL`, `NoSQL`, `SAS`, `VBA`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`Tableau`, `PowerBI` ,`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`Linear/Logistic Regression`, `Classification and Regression Trees`, `Neural Networks`, `Clustering`, `Association Rules`, `KNN`, `Ensemble Techniques`, `Statistical Analysis.`')
txt3('Databases', '`MySQL`, `SQL-Server`, `MongoDB`')
txt3('Big Data Technologies', '`Spark`, `Hadoop`, `Kafka`, `MapReduce`, `Sqoop`, `Hive`, `Impala`')
txt3('Certifications', '`AWS Cloud Practitioner`, `Lean Six Sigma Yellow Belt`, `Certified Extreme Event Modeller (CEEM), AIR`, `Oracle Certified SQL Developer`.')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'www.linkedin.com/in/akhil-chandra-shanivendra')
txt2('GitHub', 'https://github.com/akhil-chandra-s')
