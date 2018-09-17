# News-Summarization

This repository contains the implementation of a news summarizer.
The four-stage pipeline involved in its design is:
1) Designing a web scraper to scrap off the news from multiple websites(built using Scrapy for Python)
2) Saving the scraped news to a CSV
3) Processing this CSV to generate the summary (using NLP)
4) Displaying the output on a webpage using Bottle framework (for Python)
