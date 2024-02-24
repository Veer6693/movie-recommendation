# Movie Recommendation System

This project aims to recommend movies based on user input, using the TMDB dataset. The recommendation is based on movie overview, genres,keywords, actor names, and director names.

## Overview

The project includes the following steps:

1. **Data Processing:** First, we select only the useful columns. Then, we format some column values to ensure they are well-structured. We extract values in list format from 'genres' and 'keywords', and obtain actors' names from 'cast' and directors' names from 'crew'.
2. **Text Normalization:** Using PorterStemmer to get words in their root form.
3. **Text Vectorization:** Using CountVectorizer to convert text into a matrix of token counts.
4. **Recommendation:** Using cosine_similarity to check the angle between vectors and recommend movies.
5. **Deployment:** Using Streamlit to deploy the project locally.

The main goal of this project is to provide users with personalized movie recommendations based on their current preferences and viewing habits. By analyzing movie descriptions, genres, keywords, and the involvement of specific actors and directors, the system can suggest movies that are likely to be of interest to the user.

## Usage

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git

2. Install the required packages:

   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app:

   ```bash
   streamlit run app.py

4. Open your browser and navigate to http://localhost:8501 to access the web interface for movie recommendations.

![Screenshot 2024-02-24 123957](https://github.com/Veer6693/movie-recommendation/assets/102231617/fbfaa95c-84ed-4c9c-ab5d-242ce83c24a3)


![Screenshot 2024-02-24 123957](https://github.com/Veer6693/movie-recommendation/assets/102231617/872cae06-bd5b-4bf4-982f-c3b5bf780386)


## Future Improvements

- Implement collaborative filtering to enhance the recommendation engine.
- Enhance the user interface for a more engaging experience.
