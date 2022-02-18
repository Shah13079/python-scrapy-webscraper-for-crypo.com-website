# python-scrapy-webscraper-for-crypo.com-website
The Web Scraper is purely build in python Scrapy and appended data into MongoDb non relational database 

**About**:<br/>
This project is made with python scrapy framework, the spider "stocks" scrape crypto.com website stocks markets, it directly sends request to the server for html pages and fetching the data and parsing them.

Instead of editing the code, the spider structured to accept arguments start=<> and end=<> argument from CMD, So the spider will start and end crawling  on specific pages  provided by user.

In pipelines.py the pipelines the is written to upload data directly into non-relational database MongoDb,As websites start crawling, automatically it sends data into MongoDb database which is also called NoSQL DB.


**Some features**:<br/>
1) MongoDb database integration [NoSQL db]
2) Passing arguments with CMD
3) Parsing Response data

**Tools and packages used in this project:**<br/>
Python<br />
Scrapy framework<br />
MongoDB: which is source-available cross-platform document-oriented database program. Classified as a NoSQL database program.
Visual studio as tool

**Setup:**<br/>
Donwload python from official website: https://www.python.org/downloads/ <br/>
Scrapy requires Python 3.6+<br />
Make sure pip package-management system is installed

**Prerequisites:** <br />
Open CMD and change working directory into project directory and give command:<br/>
pip install -r requirements.txt <br/>
this will install all required dependencies and packges.

**Database Connection** <br />
If you want to connect to Your MongoDb database change the following attribute in setting.py to yours cloud MONGO_URI Url:

```
MONGO_URI=""
```


**Enable/disable pipelines:** <br />
Note:
If you don't want to use Database Simply comment out bellow piplines in settings.py:

```
ITEM_PIPELINES = {
   'crypto_web.pipelines.MongoPipeline': 300,
}

```

**Run:** <br />
1) Run for default Url from start to end:<br />```scrapy crawl stocks -o <filename>.csv```  (-o filename.csv will generate data csv file ) <br/>
2) Run for specific Range of pages :<br/>```scrapy crawl stocks -a start=integer_pagenumber -a end=integer_pagenumber -o OUTPUT_FILE.csv``` <br/>


**Cancel Process:** <br />
CTRL+C to cancel.


**Licence** <br />
Feel free to contribute to code and use in your personal & commercial projects. Happy coding


-----------------------------------------------------------------------------------------
