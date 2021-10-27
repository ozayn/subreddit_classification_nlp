
font_path = f'{G.images_path}/Raleway-Regular.ttf'


# Create a word cloud image
import os
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = '\n'.join(G.hashtags_0)


yoga_mask = np.array(Image.open(path.join(d, f"{G.images_path}/Tree-House-icon.png")))


wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=yoga_mask,
               colormap='rainbow',
               contour_width=.01, contour_color='gray')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, f"{G.images_path}/yoga_test.png"))

# show
plt.figure( figsize=(20,10))
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis("off")
plt.figure()


# Create a word cloud image
import os
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = '\n'.join(G.hashtags_1)


meditation_mask = np.array(Image.open(path.join(d, f"{G.images_path}/meditation_icon.jpg")))


wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=meditation_mask,
               colormap='rainbow',
               contour_width=.01, contour_color='gray')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, f"{G.images_path}/meditation_test.png"))

# show
plt.figure( figsize=(20,10))
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis("off")
plt.figure()
