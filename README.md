# EECS-731-Project-1
## EECS 731 Homework 1  

#### Project 1 - Jimmy Wrangler, Data Explorer
Traveling the world on a mission to discover new data
1. Set up a data science project structure in a new git repository in your GitHub account
2. Install Jupyter notebook prerequisites (Anaconda, Python, etc.)
3. Select an industry
4. Select two to three public data sets from that industry
5. Load the data sets into panda data frames following the 10 minutes to pandas guide
6. Formulate one or two ideas on how the data sets could be combined to establish additional value using exploratory data analysis
7. Transform the data sets into a single data set while following data preparation processes to clean and transform features (use pandas documentation for help)
8. Document your process and results

#### Dataset 1 Columns
1. Age         | Age of the test subject
2. Height      | Height of the test subject
3. Weight      | Weight of the test subject
4. Gender      | Gender of the test subject
5. Systolic blood pressure   | Blood pressure of the test subject
6. Diastolic blood pressure  | Blood pressure of the test subject
7. Cholesterol | Cholesterol levels of the test subject
8. Glucose     | Glucose levels of the test subject
9. Smoking     | Smoking habit gravity measurement of the test subject
10. Alcohol intake    | Alcohol intake gravity measurement of the test subject
11. Physical activity | Fitness levelts of the test subject
12. Target | Presense of cardiovascular disease. 0 - yes; 1 - No

#### Dataset 2 Columns
1. age
2. sex
3. chest pain type (4 values)
4. resting blood pressure
5. serum cholestoral in mg/dl
6. fasting blood sugar > 120 mg/dl
7. resting electrocardiographic results (values 0,1,2)
8. maximum heart rate achieved
9. exercise induced angina
10. oldpeak = ST depression induced by exercise relative to rest
11. the slope of the peak exercise ST segment
12. number of major vessels (0-3) colored by flourosopy
13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

#### Dataset 3 Columns
1. survival -- the number of months patient survived (has survived, if patient is still alive). Because all the patients had their heart attacks at different times, it is possible that some patients have survived less than one year but they are still alive. Check the second variable to confirm this. Such patients cannot be used for the prediction task mentioned above.
2. still-alive -- a binary variable. 0=dead at end of survival period, 1 means still alive
3. age-at-heart-attack -- age in years when heart attack occurred
4. pericardial-effusion -- binary. Pericardial effusion is fluid around the heart. 0=no fluid, 1=fluid
5. fractional-shortening -- a measure of contracility around the heart lower numbers are increasingly abnormal
6. epss -- E-point septal separation, another measure of contractility. Larger numbers are increasingly abnormal.
7. lvdd -- left ventricular end-diastolic dimension. This is a measure of the size of the heart at end-diastole. Large hearts tend to be sick hearts.
8. wall-motion-score -- a measure of how the segments of the left ventricle are moving
9. wall-motion-index -- equals wall-motion-score divided by number of segments seen. Usually 12-13 segments are seen in an echocardiogram. Use this variable INSTEAD of the wall motion score.
10. mult -- a derivate var which can be ignored
11. name -- the name of the patient (I have replaced them with "name")
12. group -- meaningless, ignore it
13. alive-at-1 -- Boolean-valued. Derived from the first two attributes. 0 means patient was either dead after 1 year or had been followed for less than 1 year. 1 means patient was alive at 1 year.



References:
https://www.kaggle.com/sulianova/cardiovascular-disease-dataset 
https://www.kaggle.com/ronitf/heart-disease-uci
https://www.kaggle.com/loganalive/echocardiogram-uci
