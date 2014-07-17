Udacity-dl
==========

A python package for archiving content from udacity.org (videos,
lecture notes, quizzes, …) for offline reference.


Installation
------------

Make sure you have installed [Python 2.7](http://www.python.org/download)

With the help of python pip installation is as simple:  
`sudo pip install udacity-dl`

If you prefer manual installation:
- Clone [this repo]() locally
  `git clone https://github.com/ashishnitinpatil/udacity-dl.git <local_dir_path>`
- Then simply run:  
  `python setup.py install`  
  This will create a udacity-dl script in `/usr/local/bin` (linux) or `c:\\Python27\\Scripts` (windows)


Usage 
-----

For Usage help, run:  
`udacity-dl -h`

Example usage:  
`udacity-dl -d /my/destination/path/ course_name(s)`


Notes
-----

For the link https://www.udacity.com/wiki/ST095/downloads *ST095* is the course_name.

Usage:  
`udacity-dl -d /my/destination/path/ ST095 cs222`

A few courses and their respective course names have been listed under  
[udacity_courses](/udacity_courses.md)


Features
--------

- Now downloads all available resources in wiki
- Skips already downloaded resources
- Proper naming of course and class contents
- No need of Udacity username and password
