<div id="top"></div>

# Sinemate - Movie Recommender Web App

[![GitHub last commit](https://img.shields.io/github/last-commit/FirdausJawed/engage-project?style=for-the-badge&logo=git)](https://github.com/FirdausJawed/) 
[![GitHub stars](https://img.shields.io/github/stars/FirdausJawed/engage-project?style=for-the-badge)](https://github.com/FirdausJawed/engage-project/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/FirdausJawed/engage-project?style=for-the-badge&logo=git)](https://github.com/FirdausJawed/engage-project/network)
[![GitHub issues](https://img.shields.io/github/issues/FirdausJawed/engage-project?style=for-the-badge)](https://github.com/FirdausJawed/engage-project/issues)
[![GitHub stars](https://img.shields.io/github/stars/FirdausJawed/engage-project?style=for-the-badge)](https://github.com/FirdausJawed/engage-project/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/FirdausJawed/engage-project?color=%230000ff&style=for-the-badge)](https://github.com/FirdausJawed/engage-project/network)
[![GitHub license](https://img.shields.io/github/license/FirdausJawed/engage-project?style=for-the-badge)](https://github.com/FirdausJawed/engage-project)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FirdausJawed/engage-project">
    <img src="images/81986-movie.gif" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center"><b>Submission for Microsoft Engage 2022 🌟</b></h3>

</div>


## **_Index_**
- [About](#About)
- [UI/UX](#UI/UX)
- [Link of the website](#Complete-website-link)
- [Instructions](#Instruction)
  * [How to commit in CLI](#Instruction)
  * [How to sync your forked repository](#Instruction)

- [Overview of the codebase](#overview-of-the-codebase)

- [Implementation](#implementation)
  * [Libraries/modules Used](#Libraries/modules-used)
  * [Concept used](#Concept-used)
  * [Frequently used terms](#Frequently-used-terms)
  * [Data-set used](#Data-set-used)
- [Demo & Screenshots](#Demo)
- [Project References](#project-references)
- [License](#license)
- [Connect with me](#connect-with-me)


## About

Cinemate is a Movie Recommendation application with a rich integrated UI which helps you to find best movies of your choice .
Developed during my menteeship at [Microsoft Engage 2022](https://acehacker.com/microsoft/engage2022/),
it implements the following features : 
 * Content-Based-Filtering :

    In this system, keywords are used to describe the items and a user profile is built to indicate the type of item this user likes. In other words, these algorithms try to recommend items that are similar to those that a user liked in the past, or is examining in the present. It does not rely on a user sign-in mechanism to generate this often temporary profile. In particular, various candidate items are compared with items previously rated by the user and the best-matching items are recommended. This approach has its roots in information retrieval and information filtering research.


  * Genre-based filtering :

    In this kind of filtering, user can select the genere and then click on the button, recommandation based on the tags will appear.


## **UI / UX**
* Dark theme
* Light theme
* Fully Responsive UI
* Minimalist UI

## **Complete website link**
[Here](http://share.streamlit.io/firdausjawed/engage-project/main/main.py)

## **Instructions**
-----------------------

### How to commit in CLI

```sh
$ git clone https://github.com/FirdausJawed/engage-project.git
$ git checkout -b Branch_Name
$ git add .
$ git commit -m 'message'
$ git push -u origin Branch_Name

```

### How to sync your forked repository

```sh
$ git fetch --all --prune
$ git checkout master
$ git reset --hard upstream/master
$ git push origin master

```


### Overview of the codebase
<a href="#"><p align="center"> <img src="images/1.jpg"/></p></a>

<a href="#"><p align="center"> <img src="images/2.jpg"/></p></a>

  * For more please refer to my [Jupyter notebook file](https://drive.google.com/file/d/1C-QFOuYaa3Om97RTVNgqQg-U73CweNpy/view?usp=sharing) for detailed explanation.


## **Implementation**

### Libraries/Modules used 

- Numpy
- Pandas
- Scikit-learn
- NLTK
- Streamlit

### Data-set used
[here](https://drive.google.com/drive/folders/1AnDwQU0ATlM-I8xR5XSK4Lwe9ToEBu-_?usp=sharing)

### Concepts used
- Bag of words
- Count vectorizer
- Cosine Similarity

## Frequently used terms

- **Bags of word model :**
Bag of words model helps convert the text into numerical representation (numerical feature vectors) such that the same can be used to train models using machine learning algorithms. 

- **Scikit Learn :**
Scikit-learn provides a range of supervised and unsupervised learning algorithms via a consistent interface in Python.The library is focused on modeling data. It is not focused on loading, manipulating and summarizing data.

- **CountVectorizer :**
The CountVectorizer provides a simple way to both tokenize a collection of text documents and build a vocabulary of known words, but also to encode new documents using that vocabulary.

- **Cosine Similarity :**
Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. The cosine of 0° is 1, and it is less than 1 for any angle in the interval (0, π] radians

## Demo
Click to play


**- [Screenshots](https://drive.google.com/file/d/1UGLThYkWczC3nnebU1L99Ai1Ll77iZZu/view?usp=sharing)**


## Project References
- [Streamlit Docs](https://docs.streamlit.io)
- [Rapid APIs](https://www.rapitapi.com/)
- [CampusX YouTube numpy playlist](https://www.youtube.com/playlist?list=PLKnIA16_Rmvb-ToL3RQ_bwxG4_ND-0-DT)
- [CampusX YouTube pandas playlist](https://youtube.com/playlist?list=PLfP3JxW-T70Gf4iJXPb0Yw5_-tDRCD6LB)
- [Python basics Datacamp](https://www.datacamp.com/courses/intro-to-python-for-data-science)
- [Stanford course by Andrew ng](https://www.coursera.org/learn/machine-learning)


## License

Sinemate is released under the [MIT License](https://github.com/FirdausJawed/engage-project/blob/main/LICENSE).

## Connect with me
Drop by and say hello!

[<img height="30" src="https://img.shields.io/badge/linkedin-0077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />][LinkedIn]
[<img height="30" src="https://img.shields.io/badge/twitter-1DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />][twitter]

[linkedIn]:https://www.linkedin.com/in/firdaus-jawed/

[twitter]: https://twitter.com/jawedfirdaus01
