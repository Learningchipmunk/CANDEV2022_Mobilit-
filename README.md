# CANDEV 2022 Challenge: Retention and mobilization of talent among employment equity groups

Data analysis conducted for the [CANDEV Data Challenge 2022](https://candev.statcan.gc.ca/home) using the data they provided for the [2020 Public Service Employee Survey](https://open.canada.ca/data/en/dataset/4301f4bb-1daa-4b50-afab-d1193b5d2284/resource/25076d6a-84c0-48d0-97a9-f9d20ec2a10d).

### Description of the Project

We **identified** reasons behind the **mobility of minority groups** within the **Canadian government** through **Machine Learning** and **Statistics**. We used **Python** with a static website to generate and showcase our results. You can have access to our website through this link [here](http://candev.mobility.ca.s3-website-us-east-1.amazonaws.com/?fbclid=IwAR2vqHPWC0hd5koFO_n6JsdlQ8VepDJU5N-jzZkIVRQe3N2iX9FLYdKafJE). 

We approached the data from multiple perspectives. First, we **plotted** the **answers** to the survey **by demographic categories**. This helped us <u>identify</u> which minority wanted to leave the most and why. Then, we ran many **experiments** on the data with different methods, such as `k-means`, `PCA`, `Logistic Regression` and `Gradient Boosting`. Only `PCA` and `Logistic Regression` gave us meaningful results.  Subsequently, we **extracted** the **discriminant features** and **identified groups** of population which where **more susceptible to mobility**. 

These scripts are **flask-ready** and can easily be put in a dynamic server, processing the data live. However, we lacked a server on which to deploy it.

### Prerequisites

1. **python 3.7**
1. **Jupyter Notebook**
2. **ubuntu** or **WSL**

*Our code was tested on Ubuntu 20.0*

### File Tree

* **src/** : scripts to generate the graphs for the [visualization website](http://candev.mobility.ca.s3-website-us-east-1.amazonaws.com/)
* **Data/** : subset 3 from the [2020 Public Service Employee Survey](https://open.canada.ca/data/en/dataset/4301f4bb-1daa-4b50-afab-d1193b5d2284/resource/25076d6a-84c0-48d0-97a9-f9d20ec2a10d)
* **www/** : script for the website

### Scripts

- `LogReg_for_Mobility_Pred`: Notebook that contains the code for the **Logistic Regression** experiment.
- `data_preproc`: Notebook that contains the code for our **data preprocessing** scheme.
- `Ponderation-Normalization-PCA`: Notebook that contains the code for our **PCA** experiment.

### Authors

@Learningchipmunk

@Alexis-BX

@AlyZei

@KatiaJDL
