import os
import docx
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv

#pip install wordcloud
#pip install nltk
#pip intall python-docx
#pip install csv
#python -m nltk.downloader all

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to read and clean text from Word documents
def read_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    text = re.sub(r'[\r\n\t]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\W+', ' ', text)  # Remove punctuation and non-word characters

    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and len(word) > 1]
    return ' '.join(tokens)
    

# Function to generate and display word cloud
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=STOPWORDS, min_font_size=10).generate(text)
    print(wordcloud.words_)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

# Main function
def main():
    folder_path = "docs"
    all_text = ""

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Read text from Word documents
        if filename.endswith(".docx"):
            text = read_docx(file_path)
            all_text += text + " "

    # Preprocess the combined text
    processed_text = preprocess_text(all_text)

    # Generate and display the word cloud
    generate_word_cloud(processed_text)

if __name__ == "__main__":
    main()
