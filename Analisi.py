df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", 
                 names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

esplorazione_iniziale(df)
analisi_approfondita(df)
visualizzazione(df)
