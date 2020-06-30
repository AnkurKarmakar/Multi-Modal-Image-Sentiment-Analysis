# Multi-Modal-Image-Sentiment-Analysis
Final Year Project

Python version used : 3.6.0

# To perform Sentiment Analysis of Text present in Image.
> python3 OCRSentiment.py
# Face classification and detection.
Real-time face detection and emotion/gender classification using fer2013/IMDB datasets with a keras CNN model and openCV.
* IMDB gender classification test accuracy: 96%.
* fer2013 emotion classification test accuracy: 66%.


### Run real-time emotion demo:
> python3 video_emotion_color_demo.py

### Make inference on single images:
> python3 image_emotion_gender_demo.py <image_path>

e.g.

> python3 image_emotion_gender_demo.py ../images/test_image.jpg

### Steps to run the final application UI.exe
Steps to run project:-
Step 1:- Download project from https://github.com/AnkurKarmakar/Multi-Modal-Image-Sentiment-Analysis
Extract the zip folder and place the entire project folder in any drive except C drive.


Step 2:- Install Python 3.6.0 64 bit from https://www.python.org/downloads/release/python-360/(Note:- Other versions will cause problems with the tensorflow version used)


Step 3:- Download site-packages.rar from https://drive.google.com/file/d/1yBVfiMuq6DI8gIF4z__E_gCmwSwEL4uu/view?usp=sharing and extract it into C:\Users\<UserName>\AppData\Local\Programs\Python\Python36\Lib\


Step 4:- Go to project folder where requirements.txt is present.Then open cmd there and type pip install -r requirements.txt


Step 5:- Download Tesseract from https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download  and then install it


Step 6:- Go to project folder. Inside src folder there is UI.exe. Run it and program will run. After the UI pops up click on Browse to select image and then click on Analyze.


### To train previous/new models for emotion classification:


* Download the fer2013.tar.gz file from [here](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

* Move the downloaded file to the datasets directory inside this repository.

* Untar the file:
> tar -xzf fer2013.tar

* Run the train_emotion_classification.py file
> python3 train_emotion_classifier.py

### To train previous/new models for gender classification:

* Download the imdb_crop.tar file from [here](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) (It's the 7GB button with the tittle Download faces only).

* Move the downloaded file to the datasets directory inside this repository.

* Untar the file:
> tar -xfv imdb_crop.tar

* Run the train_gender_classification.py file
> python3 train_gender_classifier.py
