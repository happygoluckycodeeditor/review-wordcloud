#import libraries
from matplotlib.colors import Colormap
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import Wordcloud, STOPWORDS

#import dataset
df = pd.read_csv("Book1.csv", sep="  ")

#Create the text variable
text = " ".join(cat for cat in df.customer_review)

#Generate wordcloud
word_cloud = Wordcloud(
    width= 3000,
    height= 2000,
    random_state= 1,
    background_color="antique white",
    Colormap="Pastel1",
    collocations=False,
    stopwords=STOPWORDS,
).generate(text)

#Display the cloud
plt.imshow(word_cloud)
plt.axis("off")
plt.show()