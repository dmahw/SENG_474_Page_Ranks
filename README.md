SENG 474 Programming Assignment Page Rank
======

## Developers
* David Mah
* Adam Leung

## Requirements
* numpy
* Python 3.6.7

## Description
This repository computes the page ranks of various websites from a dataset. Part 1 of this programming assignment checks for dead ends between every website. Part 2 covers the page ranks of every website. 

* Each question contains 2 parts, one for the 10k file, and one for the 800k file.
* Each part for the question contains the exact same logic except for the file name it outputs to.
* You may need to run the python script with python3 instead of python, depending on your environment setup.
* Reposted repository to hide sensitive information

## Instructions
1. Run the respective commands below.

Question 1 Part A Dead Ends for 10k Dataset:
1. Run `python p3q1_10k.py web-Google_10k.txt`
2. Outputs file to "deadends_10k.tsv"

Question 1 Part B Dead Ends for 800k Dataset:
1. Run `python p3q1_800k.py web-Google.txt`
2. Outputs file to "deadends_800k.tsv"

Question 2 Part A Dead Ends for 10k Dataset:
1. Run `python p3q2_10k.py web-Google_10k.txt`
2. Outputs file to "PR_10k.tsv"

Question 2 Part B Dead Ends for 800k Dataset:
1. Run `python p3q2_800k.py web-Google.txt`
2. Outputs file to "PR_800k.tsv"


## Commands to run
* `python p3q1_10k.py web-Google_10k.txt`
* `python p3q1_800k.py web-Google.txt`
* `python p3q2_10k.py web-Google_10k.txt`
* `python p3q2_800k.py web-Google.txt`
