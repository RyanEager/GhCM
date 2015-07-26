# GhCM

**G**it**H**ub **C**ontributions **M**essage is a small ultility used to write a message in your Contributions graph.

Inspired by https://github.com/avinassh/rockstar

#Alphabet
![a-h](images/sample1.jpg)
![i-p](images/sample2.jpg)
![q-x](images/sample3.jpg)
![yz](images/sample4.jpg)

# Usage
Requires: ~~[GitPython 1.0.2](https://github.com/gitpython-developers/GitPython)~~ **Pull from GitHub until 1.0.2 is out**

    GhCm.py <message>

The message should be less than 8 characters(letters only), or else it won't fit. GhCM will create a folder called "GhCM - \<Message\>", simply push this folder to a repo on your github and the message will appear. If you want to remove a message simply delete the repo from GitHub.

# Issues
 * Waiting on GitPython 1.0.2 to be released for [Feature #317](https://github.com/gitpython-developers/GitPython/pull/317), though the current version on GitHub works.

# To Do:
  * Test if possible to commit in future
  * Add punctuation
  * Add lower case letters
  * Add option for different colors
  * Add option for background color
