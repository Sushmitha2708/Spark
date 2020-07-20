# Spark  
### The Big Data Problem
In the past, computers became faster every year as the speed of processors increased. These processors could run more tasks per second than the previous one's and as a result applications also became faster gradually without any changes needed to their code. This led to a large ecosystem of applications which were mostly run on a single processor.
Over a period of time, the computations have become larger and huge volumes of data was generated and the trends of improved processor could not scale up to the demand and finally in 2005 this trend has stopped due to hard limits in heat dissipation and a major switch took place where developers started adding more parallel CPU cores with all running at the same speed.
The next step was to modify the applications to add paralellism in order to run faster and set a stage for programming models with a unified computing engine such as **Apache Spark**.  
### What is Spark?
Apache Spark is an open source unified computing engine and a set of libraries for parallel data processing on computer clusters. It runs from a computer to a cluster of thousands of servers which makes it easy to scale-up to big data processing. Sparks consists of Low-level APIs(RDDs, Distributed Variables), Structured APIs(Datasets, Dataframes, SQL) and other required components. Spark's APIs are consistent, composable and are designed to enable high performance by optimizing accross different libraries and functions composed together in a program.  
  
#### Spark Computing Engine  
Unlike Apache Hadoop which includes both a storage system(HDFS) and a computing system(Map Reduce) and cannot run without the other, Spark runs well on storage and can we used broadly in various environments. Spark can be used with a variety of storage systems like Azure storage, Amazom S3, Apache Cassandra and Apache Kafka. Spark performs computations on data that resides in any of the systems in the cluster.    
#### Spark Libraries  
Sparks libraries since its release have grown to provide more and more types of functionality. Spark supports both Standard and External libraries. Spark includes libraries for SQL, Spark SQL, Machine learning(MLlib), Stream processing(Spark Streaming), Graph analytics(GraphX). Apart from these spark has many external open-source librariesfrom connectors from various storage systems to machine learning algorithms.  

Spark supports multiple widely used programming languages like Python, Java, Scala, R. It is designed to support a wide range of data analytics tasks ranging from simple data loading and SQL queries to machine learning and streaming computation over the same computing enginewith a consistent set of Spark APIs.
