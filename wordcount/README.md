### Word Count App

#####Key features

- Enable to process large text files
- Allowed extensions: [.txt]
- Not case sensitive: `Hello` and `hello` will be counted as different words 


Pre-requisites:
- Python version >= 3.7
- Create a virtual env (Recommended)
- No need to install other dependencies





#####Usage:

`python main.py --filepath <path_to_file>`


#####Run tests:

`python -m unittest discover wordcount -v`



#####Venv setting:
- Create a virtualenv:

`python3 -m venv venv`

- Activate virtualenv before running any command:

`source venv/bin/activate`