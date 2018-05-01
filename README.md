# Sentiment-Analysis-
Used Python to do sentiment analysis from social media posts and wrote python scripts mapper and reducer to calculate final index score
“Does the media reflect public mood or form it? What about social media?”
To fully answer the above question is complex, however, we can use python to perform sentiment analysis (SA) to understand the whether stories have a positive or negative spin.
a)Proposed an “index” or measure of sentiment expressed in articles. 
b)Downloaded and examined the xml file available at http://www.cbc.ca/cmlink/rss-topstories
c)Wrote a python script named getStories.py that performs the following:
- query the xml resource from the web-service endpoint;
- extract the headline or summary for each story;
- print the headline/summaries to standard output (STDOUT), one per line.
d)Wrote a python script named mapper.py that performs the following:
- reads lines of text from standard input (STDIN);
- for each "positive" or "negative" term (ignore neutral terms) that appears in the input text,print to standard output (STDOUT) the term followed by a comma, followed by the aggregate score of that term, based on whether the term is positive or negative and how many times it occurs in the input. 
e)Wrote a python script named reducer.py that performs the following:
- reads from standard input (STDIN) terms and their aggregate scores appearing one per line (separated by a comma as printed to STDOUT by mapper.py);
- computes the aggregate sentiment score across all terms;
- outputs the final index score to standard output (one number, which can be positive or negative depending on the terms encountered).
