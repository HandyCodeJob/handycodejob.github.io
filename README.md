# blog.mikeandzoey

Still a work in progress

Repo for this [blog](http://blog.mikeandzoey.com)

Theme located [here](https://github.com/mikemhenry/materialistic-pelican)

Code is GPLv3

content/* is [CC BY-NC-SA](http://creativecommons.org/licenses/by-nc-sa/4.0/)


# How to use:
## Set up the enviroment 
```
mkvirtualenv --python=/usr/bin/python3 hcjstatic
pip install -r requirements.txt
```

## Get the theme
you can run this command in the root folder of the project and it will be in
the correct location.
```
git clone git@github.com:eswarm/materialistic-pelican.git
```

## Generate site and serve
```
./develop_server.sh start
```
