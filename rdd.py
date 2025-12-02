from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, min, max
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

schema = StructType([
    StructField("tconst", StringType(), True),
    StructField("actor", StringType(), True),
    StructField("actorName", StringType(), True),
    StructField("director", StringType(), True),
    StructField("directorName", StringType(), True),
    StructField("averageRating", DoubleType(), True),
])

spark = SparkSession.builder.appName("ActorDirectorDF").getOrCreate()

df = spark.read.csv("infoActorsx10.csv", header=True, schema=schema, escape="\\").select("actor", "actorName", "director", "directorName", "averageRating").repartition(200, "actor", "director").cache()

grouped = df.groupBy("actor", "actorName", "director", "directorName") 
    .agg(
        count("*").alias("num_collaborations"),
        avg("averageRating").alias("avg_rating"),
        min("averageRating").alias("min_rating"),
        max("averageRating").alias("max_rating")
    ) 
    .filter(col("num_collaborations") >= 2) 
    .orderBy(col("num_collaborations").desc()) 
    .limit(20)   
    .select("actorName", "directorName", "num_collaborations", "avg_rating", "min_rating", "max_rating")

grouped.show(truncate=False)

spark.stop()