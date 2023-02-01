
### [Project Description](doc/)

+ Project title: Is Aristotle's Natural Philosophy objective?
+ This project is conducted by Safira Raharjo

+ Project summary: Natural philosophy is well known as the predecessor to the scientific method. Most people will also agree that a well written scientific article in a journal will be more objective than an article in a magazine. Can we use methods of machine learning in natural language processing to see if natural philosophy is similarly objective compared to other schools of thought? The analysis finds that texts classified under natural philosophy is written in language no more objective than texts in other schools of thout, and even modern scientific articles. It can be concluded that just just because the methods of analysis used in the texts are more objective, it doesn't mean that the language used is, regardless of topic.

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz), this folder is organized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.

# Is Aristotle's Natural Philosophy objective?

## Introduction
The scientific method is one of mankind's greatest creation. It allowed us to make observations about the world around us and discern what is fact and what is fiction, making way to great advancements in humanity's quality of life. Natural philosophy is well known as the predecessor to the scientific method. In fact, what we know as science today was simply called natural philosophy in the past. There didn't used to be a distinction.

Science is considered to be pretty objective in method. We have frameworks put in place like double-blind experimentation to reduce the number of errors due to human error or bias. Most people will also agree that a well written scientific article in a journal will be more objective than an article in a magazine. Can we use methods of machine learning in natural language processing to see if natural philosophy is similarly objective compared to other schools of thought?

The [History of Philosophy dataset](https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy) will be used to make the analysis, focusing specifically on Aristotle's body of work, since he has written texts on natural philosophy and also other topics such as logic and politics with which we can make a comparison on objectivity. The subset of works will be put into a topic modelling algorithm to try and discern which sentences are part of his works on natural philosophy, and then put through a sentiment analysis algorithm measuring the subjectivity of the sentences.

## Topic Modelling
Topic Modelling is the task of using unsupervised learning to extract the main topics (represented as a set of words) that occur in a collection of documents. In this case, the collection of documents are sentences in philosophical texts and we are identifying which texts are likely to fall into the category of natural philosophy based on their topics. Latent Dirichlet Allocation (LDA) will be used to conduct this analysis, which is a statistical model that explains a set of observations (sentences) through unobserved groups (topics), and each group explains why some parts of the data are similar using a set of words. Before the LDA can be run, the dataset first needs to be pre-processed.

### Data Pre-processing
Texts need to go through a series of processes before they can be input into the LDA model. Some of these processes include tokenization and lemmatization. Tokenization is used in natural language processing to split paragraphs and sentences into smaller units that can be more easily assigned meaning. Lemmatization is a text normalization technique that switches any kind of a word to its base root mode. In addition to that, certain parts of text such as pronouns are removed, as they do not affect output topics.

The result of the processed texts of Aristotle can be visualized in a word cloud. Words such as 'the' and 'a' are no longer in the text, and words like 'things' and 'thing'only appear in one form.

![Word cloud of Aristotle's texts](https://github.com/TZstatsADS/ads-spring2023-project1-safiraharjo/blob/main/figs/aristotle_wc.png?raw=true)

### Modelling
The first step to the modelling is removing words that appear in most of the text or appear very infrequently. Words that appear in most of the texts will make it difficult to cluster the text into topics, and words that appear very infrequently are likely to be irrelevant.

The number of topics also needs to be determined. If there is previous knowledge of the texts, the number of topics can often be determined without further analysis (e.g. if the texts are composed of articles from 5 different magazines, it can be expected that there are 5 topics). In this case however, the number of topics will be determined using an analysis of coherence scores.

There are two major types of coherence scores which will be used in this analysis. One of the most popular coherence metrics is called CV which measures the distance between words. The other, UMass coherence, measure how often two words are seen together.

![Plot of CV coherence scores as a result of LDA models with 1-10 topics](https://github.com/TZstatsADS/ads-spring2023-project1-safiraharjo/blob/main/figs/c_v_score_fig.png?raw=true)

![Plot of UMass coherence scores as a result of LDA models with 1-10 topics](https://github.com/TZstatsADS/ads-spring2023-project1-safiraharjo/blob/main/figs/u_mass_score_fig.png?raw=true)

### Results
With CV scores, there is a dramatic increase in coherence score at 4 topics. With UMass scores, there is a dramatic decrease in coherence between 2 and 4 topics. Given that 2 topics seem to be too general, 4 seems right. However, a look at Aristotle's body of work spanning natural philosophy, theoretical philosophy (logic and metaphysics), as well as practical philosophy (politics and economics), 5 topics were chosen as there was not a large decrease in coherence scores.

![Word cloud of Aristotle's texts by topics](https://github.com/TZstatsADS/ads-spring2023-project1-safiraharjo/blob/main/figs/topic_wc.png?raw=true)

The word cloud by topic shows words like air in topic 1, genus in topic 2, and animal in topic 3. It is still difficult to determine which ones fall under natural philosophy, as they seem to have many words in common.

|  |  |
|--|--|
| ![Plot of intertopic distance](https://github.com/TZstatsADS/ads-spring2023-project1-safiraharjo/blob/main/figs/pyLDAvis1.png?raw=true) | ![Most relevant terms for topic 2](https://github.com/TZstatsADS/ads-spring2023-project1-safiraharjo/blob/main/figs/pyLDAvis2.png?raw=true) |


Finally, looking at the intertopic distance, topic 2 is very far away from all the other topics, and the relevant topical keywords very much suggest it is talking about something scientific. Words like animal, bird, water, and heat appear. Sentences which have the highest probability of being in topic 2 will therefore be the subject of the next part of the analysis.

## Subjectivity Modelling
Subjectivity analysis investigates attitudes, feelings, and expressed opinions in a text. As a basic task, it classifies a text as subjective (opinion) or objective (fact). The Textblob module used in this analysis will measure subjectivity on a scale of 0 to 1, 0 being the most objective and 1 being the most subjective.

### Natural Philosophy and the Works of Aristotle
| Topics | Mean Subjectivity |
|--|--|
| 0 | 0.315566 |
| 1 | 0.325995 |
| 2 | 0.327974 |
| 3 | 0.315465 |
| 4 | 0.335072 |

The average level of subjectivity in all topic groups don't differ very much. Topic 2, which seems to be closest to natural philosophy, is about average in terms of subjectivity compared to other topic groups.

### Comparison to Other Texts

| School | Mean Subjectivity |
|--|--|
| analytic | 0.286684 |
| aristotle | 0.341157 |
| capitalism | 0.367580 |
| communism | 0.290665 |
| continental | 0.314276 |
| empiricism | 0.357706 |
| feminism | 0.361778 |
| german_idealism | 0.312720 |
| nietzsche | 0.333113 |
| phenomenology | 0.283388 |
| plato | 0.319806 |
| rationalism | 0.366719 |
| stoicism | 0.329450 |

Running the analysis on the overall dataset shows that the subjectivity of Aristotle's works is about average compared to other schools of thoughts. Some of the ones that are notably more objective are tha analytic and phenomenology schools of philosophy.

As a fun exercise, the same subjectivity analysis methods are applied on a dataset of [10,000 Abstracts of Covid Research Papers](https://www.kaggle.com/datasets/anandhuh/covid-abstracts) to see whether modern research papers are any more objective than philosophical texts. Surprisingly, the abstracts of modern research papers are more subjective with a score of 0.42.

## Conclusion

Looking further into the abstracts dataset, a sentence like "The impact of the coronavirus disease 2019 (COVID-19) pandemic on well-being has the potential for serious negative consequences on work, home life, and patient care" found in one of the abstracts, is a very subjective sentence. While most people can agree the sentence is factual, serious consequences are subjective, as what one considers serious may not be considered serious by others. Conversely, a sentence by Aristotle like "Thus, for example, both a man and an ox are animals" is both factually correct but also doesn't use any subjective language. Oftentimes, modern research is geared towards getting people to take action, such as wear a mask, and using emotionally charged subjective language is effective in addition to providing factual evidence.

It can be concluded that just just because the methods of analysis used in the texts are more objective, it doesn't mean that the language used is, regardless of what the topic is.
