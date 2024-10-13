# SMS and Email Spam Detector

A machine learning project that identifies spam messages from SMS and email communications. The model predicts whether a given message is **spam** or **ham (not spam)**. Additionally, this project offers an interactive **Streamlit web app** for real-time classification.

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Dataset](#dataset)  
5. [Installation](#installation)  
6. [Usage](#usage)  
7. [Web App Deployment](#web-app-deployment)  
8. [Jupyter Notebook](#jupyter-notebook)  
9. [Contributing](#contributing)  
10. [License](#license)

---

## Project Overview
This project aims to enhance communication filtering by accurately classifying SMS and email messages as **spam** or **ham**. It leverages machine learning models trained using labeled datasets. An additional **Streamlit web app** allows users to easily input and classify messages in real-time.

## Features
- Preprocessing of text data with NLP techniques.
- Classification of messages using machine learning.
- Interactive Streamlit app for end-users.
- Support for expanding datasets and retraining models.

---

## Technologies Used
- **Python**: Primary language for development.  
- **Jupyter Notebook**: Used for experiments and prototyping.  
- **Pandas, Numpy**: For data handling and numerical operations.  
- **Scikit-learn**: Machine learning algorithms.  
- **Streamlit**: Web app framework for deployment.  
- **NLP Techniques**: Tokenization and TF-IDF vectorization.

---

## Dataset
This project uses a labeled dataset available as `spam.csv` within the repository. The data consists of SMS and email messages marked as **spam** or **ham**. You can find it [here](https://github.com/jayantkathuria7/sms-email-spam-detector/blob/master/spam.csv)【7†source】.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jayantkathuria7/sms-email-spam-detector.git
   cd sms-email-spam-detector
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Open the Jupyter notebook:
   ```bash
   jupyter notebook sms-spam-classification.ipynb
   ```
2. Execute the cells to preprocess data, train the machine learning model, and test the classifier with different inputs.

---

## Web App Deployment
This project features a **Streamlit web app** to classify messages directly via a browser interface.

- **Access the web app on Streamlit Cloud:**  
  [SMS and Email Spam Detector Web App](https://sms-spam-detecting.streamlit.app/)

To run the app locally:
1. Install Streamlit:
   ```bash
   pip install streamlit
   ```
2. Launch the app:
   ```bash
   streamlit run app.py
   ```

---

## Jupyter Notebook
In addition to the Streamlit app, the project includes an exploratory **Jupyter Notebook** for hands-on learning. You can modify and experiment with the code using the notebook provided in this repository:  

[View the Notebook (sms-spam-classification.ipynb)](https://github.com/jayantkathuria7/sms-email-spam-detector/blob/master/sms-spam-classification.ipynb)

---

## Contributing
Contributions are welcome! If you encounter bugs or want to suggest new features, feel free to fork this repository and open a pull request.
