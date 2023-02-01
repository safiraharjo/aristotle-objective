# Is Aristotle's Natural Philosophy objective?

### Code dev/lib Folder

The lib directory contains various files with function and computation codes. Files contained in the folder are:

 - **nlp_cleaning.py**
	 - Tokenizes text
	 - Removes adverb, pronoun, coordinating conjunction, punctuation, particle, determiner, adposition, space, number, symbol
	 - Lemmatizes text
 - **coherence_modelling.py**
	 - Creates corpus and dictionary
	 - Removes words in the corpus that less than 5 times or in over half of the corpus
	 - Runs LDA modelling, looping through a range of number of topics
	 - Displays plot of selected coherence scoring method for that range of topics
 - **subjectivity_modelling.py**
	 - Runs subjectivity analysis using Textblob for the selected dataframe column