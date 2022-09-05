# Class 6 - APIs

For this class, we will be using the nltk stopwords. This requires a download which you can do with the following line:

```powershell
python -m nltk.downloader stopwords
```

Be sure to do this after your virtual environment has been created and you have pip installed the necessary libraries. 

## APIs

**A**pplication **P**rogram **I**nterface can be used to interact with software applications, such as Facebook, the New York Times, Youtube, Google Maps, etc. With APIs you can retrieve data, send messages to the client (ie Tweet from a Twitterbot), & so much more! APIs are basically a set of rules that govern how one application talks to another (ie how your code asks Twitter for data or how Yelp uses Google maps to show where your favorite restaurant is).

But proceed with caution... Just because a company has an API today, doesn't mean it will be available tomorrow. For example, a major component of my graduate final was based on gathering public data from Facebook's API, however on the morning of my final, Facebook changed their API and you could no longer query public data.

**Not all APIs are created equally**

Some are clearly documented and feature lots of examples, some you are basically on your own.

Some you can start using instantly, and others require a process called authentication (more on this later). Here's here’s a [list](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/) of APIs that's don't require the authentication process.

### Query Strings

Let's look at the following url: https://www.example.com/widgets?color=blue&sort=newest

Look at everything to the right of the ?, those are referred to as query strings. In this case we have two key:value pairs --> color: blue and sort:newest. Query strings are extremely important when talking about APIs.

### Requests

We interact with APIs by using requests. Two types of requests we'll use in this class are

- A **get** request reads information
  - Get the wind speed in Denver, CO
  - Get every tweet mentioning a certain hashtag
  - Get all the buildings in New York City with a recently malfunctioned elevator
- A **post** request creates new information
  - Post a new tweet from your bot account
  - Post a Signal text
