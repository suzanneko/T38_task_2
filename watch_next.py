# To run this program, SpaCy must be installed. Type 'pip3 install spacy' into command line to install.
# Install the required language model by typing 'python -m spacy download en_core_web_md' into your command line

# The program below takes the given description for Planet Hulk as specified
# in the task and compares it with descriptions in the 'movies.txt' document using SpaCy.
# It finds the most similar movie to Planet Hulk and prints it.

import spacy

    

def compare(compare_film):
    '''
    Finds and returns the most similar film.

    Returns
    -------
    max_sim_movie: str
        Movie with the highest similarity score when compared to given movie.
    '''
    nlp = spacy.load('en_core_web_md') 

    # The section below reads the 'movies.txt' document and creates a dictionary of the 
    # data, using the title of the movie as the key, and the description as the value.

    f=open("movies.txt","r")
    movie_dict={}
    descriptions=f.read()

    descriptions=descriptions.split("\n")

    while '' in descriptions:
        descriptions.remove('')

    for line in descriptions:
        movie=line.split(":")
        key=movie[0]
        value=movie[1]
        movie_dict[key]=value

    # Looping through the dictionary, the descriptions are tokenised 
    # and compared to the description of Planet Hulk using the similarity method.
    # The maximum similarity level is found and the most similar film is returned.

    max_sim=0
    max_sim_movie=""
    token2=nlp(compare_film)
    for movie in movie_dict:
        token=nlp(movie_dict[movie])
        sim=token.similarity(token2)
        if sim>max_sim:
            max_sim=sim
            max_sim_movie=movie
        else: 
             continue
    return max_sim_movie
            
def main():
    compare_film="Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    print("The most similar film is:")
    print(compare(compare_film))

main()