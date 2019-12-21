import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


df = pd.read_csv("Formatted_Data_Sentiment.csv")

senti = df["Sentiment"]

df["Date"] = pd.to_datetime(df["Date"], format = "%Y/%m/%d")
date = df['Date']


#Line Graph
def senti_linegraph(date, senti):
      start_date = input("Please input start date: ")
      converted_start_date = datetime.strptime(start_date, "%Y/%m/%d")
      end_date = input("Please input end date: ")
      converted_end_date = datetime.strptime(end_date, "%Y/%m/%d")

      daterange = []
      sentirange = []

      for i in range(len(date)):
            if date[i] >= converted_start_date and date[i] <= converted_end_date:
            #         print(date[i])
                  daterange.append(date[i])
                  sentirange.append(senti[i])


      #Graph to show the relationship between the said date and the sentiments of the articles in the range 

      plt.plot(daterange, sentirange, 'rD-')
      # plt.ylim(-10,80)

      fig_size = plt.rcParams["figure.figsize"]
      fig_size[0] = 25
      fig_size[1] = 10
      plt.rcParams["figure.figsize"] = fig_size

      plt.title("Sentiments vs Date")

      plt.xlabel('Date')
      plt.ylabel('Sentiments In Each Article')


      plt.show()

#Define number of positive, negative and neutral articles

pos_art = 0
neg_art = 0
neu_art = len(senti) - pos_art - neg_art

def senti_info(senti):
      for num in senti:
            if num > 0:
                  pos_art += 1
            elif num < 0:
                  neg_art += 1
            else:
                  pass
      
      print("Out Of {} Articles, {} Are Positive , {} Are Negative And {} Is/Are Neutral"
            .format(len(senti), pos_art, neg_art, neu_art))

#Piechart
def senti_piechart():
      labels = ["Positive", "Negative", "Neutral"]
      size = [pos_art, neg_art, neu_art]
      colors = ['#2CCDBD', '#CD2C7D', '#FFA500']

      fig_size = plt.rcParams["figure.figsize"]
      fig_size[0] = 10
      fig_size[1] = 5
      plt.title("Net Sentiment")
      plt.pie(size, labels = labels, colors = colors, autopct='%1.1f%%', startangle=90)

      plt.show()

