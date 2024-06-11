import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re

# Function to read the document and clean the text
def read_and_clean_text(file_path):
    # Read the document
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Clean the text
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\W+', ' ', text)  # Remove punctuation and non-word characters
    
    return text

# Function to generate and display the word cloud
def generate_word_cloud(text):
    # Define stopwords
    stopwords = set(STOPWORDS)
    
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(text)
    
    # Display the word cloud
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    
    plt.show()

# Main function to execute the process
def main():
    # Path to your document
    file_path = 'testdata.txt'
    
    # Read and clean the text
    text = read_and_clean_text(file_path)
    
    # Generate and display the word cloud
    generate_word_cloud(text)

if __name__ == "__main__":
    main()
