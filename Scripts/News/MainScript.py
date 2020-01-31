from Class import DataExtraction, NLP

# DataExtraction
extraction = DataExtraction.DataExtraction(
    "9c31513f-beb6-4aac-86ee-0b1320f2860b", 
    "https://content.guardianapis.com/search?",
    input("Which Company? "),
    "2018-07-01",
    "2019-11-01")

config = extraction.NewsConfig()
data = extraction.RetrieveData(config) 
extraction.NewsExtraction(data[0])

while data[1] < data[2]:
    print(str(data[1] + 1) + "/" + str(data[2]))
    extraction.AddPages()
    config = extraction.NewsConfig()
    data = extraction.RetrieveData(config) 
    extraction.NewsExtraction(data[0])

concat_csv = input("Do you want to concatenate the csv files into a single csv file? Yes or No? ")
if concat_csv.upper() =="YES":
    files = []
    li = []
    for i in range(1,(data[2] + 1)):
        files.append(str(os.getcwd()) + "/Classes/" + config["q"] +"_" + str(i) + ".csv")

    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    combined = pd.concat(li, axis=0, ignore_index=True)
    combined.to_csv(str(os.getcwd()) + "/Classes/" + config["q"] + ".csv", index=False)

    for filename in files:
        os.remove(filename)


# NLP
News_NLP = NLP.class_NLP()
df = News_NLP.read_file()
content = df['Text']
News_Tokenizing = News_NLP.tokenize(content)
News_RemoveWords = News_NLP.stopwords_removal()
News_Lemmatizing = News_NLP.lemmatization()
News_NLP.export_csv()
News_POStag = News_NLP.nltk_pos_tag()