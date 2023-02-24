# Creating Wordcloud on Japan using Python!

⚠️For today's project we are going to make Wordcloud on some text data based on Japan using libraries from Python!

What is wordcloud?
According to betterevaluation.org, Word clouds or tag clouds are graphical representations of word frequency that give greater prominence to words that appear more frequently in a source text. The larger the word in the visual the more common the word was in the document(s).

Wordclouds give you very visual representation of words and their frequency in a particular text.
For today we are going to create a wordcloud for the keyword subject ☀️Japan☀️

It is a very simple program but it is fun to see the insights!

For this example we are going to data scrape (mine) text data from Wikipedia about Japan and use it to create a wordcloud! 

The steps for this project are as follows:
1. Download data from wikipedia
2. Read the data and remove stopwords
3. Visualise the data in a wordcloud

So lets get started!

Let's install some libraries for the project

For this project run this command

"pip install wordcloud wikipedia pillow"

This will install the packages for this project.

For me I only needed to install Pillows
![image](https://user-images.githubusercontent.com/110551323/221180850-b20b0863-0f4c-43ab-9948-99edd8c058c4.png)
(It was already installed)

Next step is to import and setup all the libraries for the project
![image](https://user-images.githubusercontent.com/110551323/221181376-3804b2dd-e3a2-4f98-aedc-9801a7767e59.png)



Now we scrape our data from Wikipedia.
We will extract summary for a particular keyword. In this case, 'Japan'

We will also define stopwords for the project to not detect words such as 'is' 'as' 'was' to appear in the wordcloud
![image](https://user-images.githubusercontent.com/110551323/221181501-f672e1de-0f77-44ec-8a03-8183a32b3a8a.png)

The data looks good to me!
Now, let's make the wordcloud, while weeding out the stopwords

![image](https://user-images.githubusercontent.com/110551323/221182031-fccbc99f-a80e-4fc0-b5db-efe4ae36c42b.png)

The final output will look like this:
![image](https://user-images.githubusercontent.com/110551323/221182128-58dc40c7-b482-4abc-99d3-9e976293fddf.png)

This concludes our wordcloud for the above summary (string data) on Japan~

Thank you for reading!
Feedback is always appreciated!

