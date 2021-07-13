# An example use of New York Times API
- New York Times APIs > https://developer.nytimes.com/

# API limit
- 4,000 requests per day and 10 requests per minute
- https://developer.nytimes.com/faq#a11
> 11. Is there an API call limit? --- 
> Yes, there are two rate limits per API: 4,000 requests per day and 10 requests per minute.
> You should sleep 6 seconds between calls to avoid hitting the per minute rate limit. 

# Sample code
- article_crawler.py : getting all articles through Article API
  - Need API key
- config.txt : apikey information
```
apikey=xxxx
```
