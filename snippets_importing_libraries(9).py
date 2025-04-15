# -*- coding: utf-8 -*-
"""Snippets: Importing libraries

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb

# Importing a library that is not in Colaboratory

To import a library that's not in Colaboratory by default, you can use `!pip install` or `!apt-get install`.
"""

!pip install langchain openai langchain-community



# housing_logistic.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset (replace with actual file)
# Ensure your CSV has columns like 'price', 'sqft', 'bedrooms'
df = pd.read_csv("housing.csv")

# Create a binary target column: expensive or not
df['expensive'] = (df['price'] > 500000).astype(int)

# Features and labels
X = df[['sqft', 'bedrooms']]
y = df['expensive']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))



!pip install matplotlib-venn

!apt-get -qq install -y libfluidsynth1

"""# Install 7zip reader [libarchive](https://pypi.python.org/pypi/libarchive)"""

# https://pypi.python.org/pypi/libarchive
!apt-get -qq install -y libarchive-dev && pip install -U libarchive
import libarchive

"""# Install GraphViz & [PyDot](https://pypi.python.org/pypi/pydot)"""

# https://pypi.python.org/pypi/pydot
!apt-get -qq install -y graphviz && pip install pydot
import pydot

"""# Install [cartopy](http://scitools.org.uk/cartopy/docs/latest/)"""

!pip install cartopy
import cartopy