from pyspark.sql import SparkSession
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
import pandas as pd
from pyspark.sql import SQLContext
from pyspark.sql.functions import col
from pyspark.ml.linalg import Vectors
from pyspark.sql.types import DoubleType
from pyspark.sql.functions import substring, length, col, expr
from pyspark.ml.regression import LinearRegression

df=pd.read_csv('word_rating.csv')
print(df)

spark = SparkSession \
.builder \
.appName("Project") \
.getOrCreate()

sqlContext = SQLContext(spark)
sparkDF=spark.createDataFrame(df.astype(str)) 
sparkDF.printSchema()
sparkDF.select('word rating').show()
sparkDF.select('Rating').show()




ML_df=sparkDF.select('Rating','word rating')
ML_df.show()
ML_df = ML_df.select(col("Rating").alias("label"), col("word rating").alias("features"))


ML_df = ML_df.withColumn("features",expr("substring(features, 2, length(features)-2)"))

feat_array = [[row.features] for row in ML_df.collect()]
rating_array = [row.label for row in ML_df.collect()]

val_tot=[]
for group in feat_array:
    val_lst=group[0].split(', ')
    val_sec=[]
    for item in val_lst:
        try:
            int_val=int(item)
        except Exception as e:
            print(e)
            print("here")
            int_val=0
            
        val_sec.append(int_val)
    val_tot.append(Vectors.dense(val_sec))

print(len(rating_array),len(val_tot))    
    
final_df=sqlContext.createDataFrame(zip(rating_array, val_tot), schema=['label', 'features'])
final_df = final_df.withColumn("label", final_df["label"].cast(DoubleType()))
final_df.show()

splData=final_df.randomSplit([0.1,0.9], 100)
trainingData=splData[0]
testData=splData[1]

#===============================
print("Total Data Set count:")
print(ML_df.count())

print("Training Data:")
print(trainingData.count())
print("Test Data:")
print(testData.count())

if (trainingData.count()+testData.count())==ML_df.count():
    print("Data count verified:")
    print("total data=",str(trainingData.count()+testData.count()))
else:
    print("Data totals do not match")

trainingData.show()

lr = LinearRegression(featuresCol = 'features', labelCol='label', maxIter=2, regParam=0.3, elasticNetParam=0.8)
lr_model = lr.fit(trainingData)
print("Coefficients: " + str(lr_model.coefficients))
print("Intercept: " + str(lr_model.intercept))