# Emotion Recognition App  

A Streamlit-based application for recognizing emotions in social media texts, specifically tweets. The app leverages a fine-tuned **IndoBERT** model to classify emotions into eight categories:  
- Anger  
- Anticipation  
- Disgust  
- Fear  
- Joy  
- Sadness  
- Surprise  
- Trust  

This project also includes an API powered by **Uvicorn** for efficient backend handling.  

## 🛠 Project Structure  
The repository is organized into two main folders:  
1. **finetune**: Contains the following resources for training the emotion recognition model:  
   - A Jupyter Notebook for fine-tuning IndoBERT  
   - The dataset used for training and testing  
   - Utility scripts for preprocessing and model training  

2. **deploy**: Contains the files necessary to deploy the app, including the Streamlit frontend and Uvicorn API backend.  

## 🚀 Features  
- Predicts emotions from user-provided text  
- Built-in fine-tuning resources for IndoBERT  
- Lightweight deployment setup

## 📚 Dataset
The dataset used for fine-tuning IndoBERT is included in the finetune folder. Details about the dataset and preprocessing steps can be found in the provided Jupyter Notebook.

## 🛠 Tech Stack  
- **Streamlit**: For building the web app  
- **Uvicorn**: For running the API backend  

## 🔧 Installation Instructions  
To run the app locally:  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/farrelsp/emotion-recognition-app.git
   cd emotion-recognition-app
   
2. **Install Dependencies**
   Ensure you have Python installed, then install the required libraries:
   ```bash
   cd deploy
   pip install -r requirements.txt

3. **Run the API**
   Start the API server using Uvicorn:
   ```bash
   uvicorn main:app

4. **Run the App**
   Launch the app locally using:
   ```bash
   Launch the app locally using:
   streamlit run streamlit.py
   
## App Preview 
<img width="605" alt="image" src="https://github.com/user-attachments/assets/86ad26fb-b365-4daf-ba1d-dcdeb6758d74">
