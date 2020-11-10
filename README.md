# Fake News Classification with a Flask Front End
----
#### by Ben Inoyatov

### Introduction
---
- Fake news has become a buzzword in the days of the Digital Revolution. With the power of the internet, *anyone* can have their voice heard. While this idea has led to the exponential growth of real, trustworthy data it has also led to the rise of 'fake' data. Take for example 70News - a fake news website hosted on WordPress. After the 2016 election, they claimed Donald Trump won the popular vote. The story became so popular that it was one of the top results when googling "final election results." [Source](https://www.cbsnews.com/news/googles-top-search-result-for-final-election-numbers-leads-to-fake-news-site/) 

- It is more important now than ever before that we maintain a ground-truth of what the internet can be. This project focuses on analyzing twenty thousand+ articles [Kaggle Source](https://www.kaggle.com/c/fake-news/overview) that were deemed 'fake' or not. In addition to tuning a model, there is also a front end Flask application where a user can enter a URL link to an article and the application will output whether it deems the article fake. 
- Libraries used: ```pandas | numpy | matplotlib | scikitlearn | NLTK | Flask```

Notebooks to refer to:
- For EDA and csv compilation refer to: ```eda_and_cleaning.ipynb```
- For the model process along with visualizations refer to: ```modeling_visualizations.ipynb```

#### Model Process
---
- Class Balance: very balanced to start 

![image](https://user-images.githubusercontent.com/44031998/98706497-e74cf880-234c-11eb-87dc-701a061d4934.png)


- Accuracy was used to balance both false positives and negatives. 


![confusion matrix ](https://user-images.githubusercontent.com/44031998/98706514-eae07f80-234c-11eb-8113-b3f5c485a2b2.png)

#### Word count bar graphs 
- Fake news and Real news have similiar word usage however some differences are shown e.g., true news' most used word was 'said' which can imply that those news outlets use direct quotes of the people they report about. In constrast fake news cannot rely on direct quotes often times and instead paraphrase or use other inflammatory words to distract the reader like 'war'. 
![word counts bar graph](https://user-images.githubusercontent.com/44031998/98706525-ee740680-234c-11eb-8f89-3013c87ca86a.png)


- Real news wordcloud

![real worldcloud](https://user-images.githubusercontent.com/44031998/98706520-ecaa4300-234c-11eb-9c28-3331b222f5cf.png)

- Fake news wordcloud

![fake wordcloud](https://user-images.githubusercontent.com/44031998/98706503-e87e2580-234c-11eb-840e-60f9570ccc64.png)



## Links 
---
[Kaggle Source](https://www.kaggle.com/c/fake-news/overview)

[Google Slides](https://docs.google.com/presentation/d/1J8PWzQ1aH5EcLo3egiD1mbHyhR61dhtSv_kgYRAXsVE/edit?usp=sharing)
