from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.functions import *
import sys
import requests
import re

# building the spark session
spark = SparkSession.builder.master("local[4]").appName("GoTplot").config(conf=SparkConf()).getOrCreate()

# read csv file
df = spark.read.csv('episode1.csv')

print(df["text"][0])
