# Class 10 - Classification

Classification is something that happens everyday all around us. Your key cards are classified so that some people can open doors that others cannot. When you try to find something on Netflix, algorithms classify movies into fun categories such as "20th Century Period Pieces for Hopeless Romantics" or "Suspenseful Scandinavian Movies based on Booked". And those movies use a classification system to determine whether they are suitable for children, teenagers, or adults. But classification has it downfalls. When you apply to get a credit card, a company classifies you as an applicant to determine your credit limit. But letting an algorithm decide who is worthy, or not worthy, of receiving credit, has negative consequences that disproportionality impacts women and people of color. The homework contains videos and readings that dive further into the dark side of classification.

But to fight to negative effects, we must first understand how it works.

## NLTK & Bayes Theorum

There are a vast set of options to classify something, but a fairly easy way to jump in is with NLTK (Natural Language Toolkit). NLTK has a classifier based on the Naive Bayes algorithm, which is a probabilistic machine learning algorithm based on the Bayes Theorem.  We could spend a lot of time on Bayes' Theorem, but to simplify, we want to calculate the possibility of something happening (A) based on something else already occurring (B). If we observe Lucy misses the bus (B), we can say there's a greater chance of her being late (A). A more detailed explanation can be found [here](https://www.kdnuggets.com/2020/06/naive-bayes-algorithm-everything.html).

## Naive Bayes

Two important components of this algorithm are **features** and **labels**. Labels are our possible classifiers. For example, maybe we are trying to classify whether a piece of text is positive or negative, our labels would be *positive* and *negative*. Regardless of what data we try to classify, our algorithm will only respond with one of our pre-determined labels. So you may think the text you entered should be classified as neutral, but if the only labels are *positive* and *negative*, you'll only get one of those two as a response.

**Features** are information we have about the entity we are trying to classify. Looking at the positive/negative text example, maybe we look at the emojis as a feature, or the keywords as a feature, or even the punctuation as a feature. With the Naive Bayes algorithm, there are two rules with features:

1. They are independent
2. They are equal

So no one feature is more important than other, and one feature has nothing to do with another. 

Let's break down an example. Let's try and classify 

LABELS: 'positive', 'negative'

For features, let's say we decided verbs are the best way to determine where the general tone is positive or negative.



