# -*- coding: utf-8 -*-
"""Snippets: Importing libraries

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb

# Importing a library that is not in Colaboratory

To import a library that's not in Colaboratory by default, you can use `!pip install` or `!apt-get install`.
"""

!pip install langchain openai langchain-community

# news_summarizer_langchain.py

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI()

prompt = PromptTemplate(
    input_variables=["article"],
    template="Summarize this news article:\n\n{article}\n\nSummary:"
)

summarizer_chain = LLMChain(llm=llm, prompt=prompt)

article = """
India's space agency ISRO launched a new weather satellite that is expected to improve forecasting. The launch was successful and marks another milestone...
"""

summary = summarizer_chain.run(article)
print("Summary:", summary)



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