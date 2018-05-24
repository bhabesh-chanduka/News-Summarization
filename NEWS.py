from bottle import route, run , template
import os
import pandas as pd
from text_summarizer import FrequencySummarizer


@route('/news')
def news():
	
	command = "scrapy runspider news_spider.py -o news.csv"
   	os.system(command)
	df = pd.read_csv("news.csv")
	news=""
        dic={}
        for i in xrange(len (df)):
            if df['text'][i] in dic:
                continue
            dic[df['text'][i]]=1
            news=news+" "+(df['text'][i])

        
        fs = FrequencySummarizer()
        final_summary = fs.summarize(news, 10)
	s="<marquee behavior='scroll' bgcolor='yellow' style='border:solid;'> <h1> Today's Breaking News! <br/> </h1></marquee>"
	for i in final_summary:
		s=s+'<p style="color:red; font-family:garamond"><b>'+i+"</b><br/></p>"
	print s
	return  s

run(host='localhost', port=8080, debug=True)


