import pandas as pd
import os
from text_summarizer import FrequencySummarizer

class Crawler:
    def __init__(self):
        self.run_crawler = True
        command = "scrapy runspider news_spider.py -o news.csv"
        os.system(command)
        self.df=pd.DataFrame()
    
    def read_data(self):
        self.df=pd.read_csv('news.csv')
    
    def summary(self,num_news):
        news=""
        dic={}
        df=self.df
        for i in xrange(len (df)):
            if df['text'][i] in dic:
                continue
            dic[df['text'][i]]=1
            news=news+" "+(df['text'][i])

        
        fs = FrequencySummarizer()
        final_summary = fs.summarize(news, num_news)

        return final_summary

def main():
        crawler = Crawler()
        crawler.read_data()
        num_news = input("Enter the number of news pieces ")
        print "Summary: "
        print "\n".join(crawler.summary(num_news))
	#return crawler.summary(num_news)
if __name__ == "__main__":
    main()
