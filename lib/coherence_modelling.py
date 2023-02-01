def coherence_score_viz(text,coherence_calculation,lower_range,upper_range,corpora,gensim,plt,CoherenceModel,path_def):
    topics = []
    score = []
    id2word = corpora.Dictionary(text)
    id2word.filter_extremes(no_below=5, no_above=0.5, keep_n=1000)
    corpus = [id2word.doc2bow(doc) for doc in text]
    for i in range(lower_range,upper_range,1):
        lda_model = gensim(corpus=corpus,
                           id2word=id2word,
                           num_topics=i,
                           random_state=100,
                           chunksize=100,
                           passes=10)
        coherence_model_lda = CoherenceModel(model=lda_model, texts=text, dictionary=id2word, coherence=coherence_calculation)
        topics.append(i)
        score.append(coherence_model_lda.get_coherence())
        
    fig = plt.figure()
    plt.plot(topics, score)
    plt.xlabel('Topics')
    plt.ylabel('Coherence Score')
    plt.title(coherence_calculation+' Coherence Score')
    fig.savefig(path_def+'figs/'+coherence_calculation+'_score_fig.png')
    return