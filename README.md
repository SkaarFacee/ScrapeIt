# ScrapeIt :bomb:
This is basically a webscraper that is capable of scraping a mobile websites for all details about mobile phones listed on their website. <br> The code has 3 parts :
- [ ] script
- [ ] spider 
- [ ] convert
## Script file :rocket:
This is the main file that processes the list of phones and get their respective links. As the site is dymanic, the script checks if a specific row number is loaded, if not it then it waits untillt the row number is loaded and then it scrapes the page for all links that lead to the phones specification page. Finally saves the data as a json file.
## Spider :spider:
This uses the saved json file. It is of the format `phone_name:phone_relative_link`. The spider uses this data to crawl into the various websites and saves the data as a dictionary. Finally, the dicts of all the phones is made into a list and saved it into a file
## Convert :open_file_folder:
This converts the saved file into a csv so that it can be used with more ease

> Note the URL used is a public website, but is saved as a variable in the `secret.py` file
# How to use: :cloud:
1.  Run `script.py`
2.  Run `spider.py`
3.  Run `convert.py`

# Contributing Help :boom:

If you are really interested in contributing to the please follow the below steps and rules.
1. Fork the project :fork_and_knife: (Star :star: the repo before that :stuck_out_tongue:)
2. Clone it.
```
https://github.com/<username>/ScrapeIt.git
```
3. Look for any issues clicking the issues tab. Go through it and assign take one. Make sure you get assigned or atleast say that you are gonna work on it.
5. Always create a new branch and work on the feature or bug. Check this if you are not that familiar with branching, [Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
6. If you are using any other module for implementing any new features, please install the modules in the virtual environment and update it in the `requirements.txt` by using the below command.
```
pip freeze > requirements.txt
```

If you have any doubts or issues, let the maintainers know about it. They would be ready to help.
