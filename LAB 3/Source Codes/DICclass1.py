import sys
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import *
from pyspark.ml.feature import *
from pyspark.ml.classification import *
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


## Constants
APP_NAME = "LogisticRegrestion"

# Configure Spark
conf = SparkConf().setAppName(APP_NAME)
conf = conf.setMaster("local[*]")
sc   = SparkContext(conf=conf)
spark = SparkSession(sc)

sqlContext = SQLContext(sc)
df = spark.read.text('/home/hadoop/Desktop/business/*')
df = df.withColumn("Category",lit("business"))

df1 = spark.read.text('/home/hadoop/Desktop/politics/*')
df1 = df1.withColumn("Category",lit("politics"))

df2 = spark.read.text('/home/hadoop/Desktop/sports/*')
df2 = df2.withColumn("Category",lit("sports"))

df3 = spark.read.text('/home/hadoop/Desktop/technology/*')
df3 = df3.withColumn("Category",lit("technology"))

mergeDF1 = df.union(df1)
mergeDF2 = mergeDF1.union(df2)
mergeDF3 = mergeDF2.union(df3)
mergeDF3.show()

data = mergeDF3.select([column for column in mergeDF3.columns])
data.show(20)

# regular expression tokenizer
regexTokenizer = RegexTokenizer(inputCol="value", outputCol="words", pattern="\\W")
# stop words
removeWords = ["http","https","amp","rt","t","c","the","sections", "SEARCH","Skip","and","am","ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]
stopwordsRemover = StopWordsRemover(inputCol="words", outputCol="filtered").setStopWords(removeWords)
label_stringIdx = StringIndexer(inputCol = "Category", outputCol = "label")

hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures", numFeatures=120)
idf = IDF(inputCol="rawFeatures", outputCol="features", minDocFreq=5) #minDocFreq: remove sparse terms
pipeline = Pipeline(stages=[regexTokenizer, stopwordsRemover, hashingTF, idf, label_stringIdx])
pipelineFit = pipeline.fit(data)
dataset = pipelineFit.transform(data)

dataset.show()

(trainingData, testData) = dataset.randomSplit([0.8, 0.2], seed = 100)
lr = LogisticRegression(maxIter=20, regParam=0.3, elasticNetParam=0)
lrModel = lr.fit(trainingData)
predictions = lrModel.transform(testData)
predictions.filter(predictions['prediction'] == 0) \
    .select("value","Category","words","filtered","rawFeatures","features","label") \
    .orderBy("probability", ascending=False) \
    .show(n = 10, truncate = 30)

evaluator = MulticlassClassificationEvaluator(predictionCol="prediction")
evaluator.evaluate(predictions)

print("----------------------------------The accuracy is : " , evaluator.evaluate(predictions),"--------------------------------------------------------------------")
