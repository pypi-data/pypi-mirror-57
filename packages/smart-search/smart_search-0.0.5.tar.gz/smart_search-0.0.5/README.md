# Concept-Search

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/ItsSiddharth/context_search/blob/master/LICENSE)   [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

## For source code 
This the my <a href="https://github.com/ItsSiddharth/context_search">Github repo. </a>
Contact me for support and PRs are welcome.

## Usage 
1. Pip install the package.
```
$ pip3 install smart-search
```
* **NOTE** : Please have the pickle file in the same folder as the python script in which you will use our pip package.

> Here i use the <a href="http://nlp.stanford.edu/data/wordvecs/glove.6B.zip">glove.6B.zip</a> file from Standfords Github repository from the hyperlink.

## Syntax 
1. Import the library.
```
>> import smart_search
```
2. Create an object of the class, smart_search.model(). Say, `functioncaller`.
```
>> functioncaller = smart_search.model()
```
3. Now to convert a pdf to a list of lists containing page.no and words after stop word removal, we use the built in function `getting_list_of_words()`. This accepts 1 argument, i.e the path to the pdf and returns the required list to be fed to the model.
```
>> pdf_list = functioncaller.getting_list_of_words('path to your pdf')
```
4. Pass this list to the model along with the word you want to get the search result of using the `perform_skip()` function. This accepts 2 variables, i.e the list produced by the previous function and the word you want to search for and retuns the top 5 relevant search locations of the word you searched for.
```
>> location[0:5] = perform_skip(pdf_list, input_word)
```
5. You can use subprocesses library of python to navigate to the page if you want to.

## LICENSE
<a href="https://github.com/ItsSiddharth/context_search/blob/master/LICENSE">MIT</a>


