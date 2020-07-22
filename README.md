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

### Architecture of Spark  
Single processor machines do not have enough power and resources to perform computation on huge amounts of data. In spark, a cluster or a group of computers pools the resources of many machines together, giving user the ability to use all th resources as if they were a single computer. Spark provides a framework to manage and coordinate the execution of tasks on data across a cluster of computers. The cluster of machines that executes the tasks is managed by a *cluster manager* which is mainly YARN or Mesos. Spark applications must be submitted to these cluster managers which will grant resources required for the application.  
#### Spark Application  
Spark Application consists of a *driver process* , *set of executors* and a *cluster manager*.  
Driver process is responsible for for maintaining information about the spark application, responding to user input and analyzing, distributing and scheduling work accross the executors. Driver process is the most essential part of a spark application which maintains all the relevant information during the lifetime of the project.  
Executors are responsible for carrying out the work that the driver program assigns them and reporting the state of the computation back to the driver node.  
The cluster Manager controls the physical machines and allocates resources to spark application. There can be mutliple spark applications running on a cluster at the same time. There are 3 major cluster managers that spark uses i.e Spark's cluster manager , YARN & Mesos. It keeps track of the resources available.  
#### Partitions  
For every executor to perform tasks in parallel, Spark breaks up the data into chunks called *partitions*. A partition is a collection of rows that sit on one physical machine in your cluster. It represents how data is pphysicaaly distributed across the cluster of machines during execution. If there's only 1 partition then Spark will have parallelism only for one, even if there are thousands of executors and if there are many partitions but only one executor, Spark will still have a parallelism of only one because there's only one computation resource.  
#### Transformations  
In spark, data structures are immutable i.e they can't be changed once they are created, they can only be modified and spark does this by giving it a set of instructions called *Transformations*. For example:  
` range = spark.range(100).toDF("number")`  
`divide = range.where("number % 2 = 0")`    
The above lines return no output because Spark will not act on Transformations until an *Action* is called. Spark will wait for the very last moment to execute the graph of computation instructions and this is called *Lazy Evaluation*. Instead of modifying the data immediately, when an operation needs to be performed Spark builds up a plan of transformations which are applied on the source data.  
#### Action  
Transformations are used to build up a logical transformation plan and to trigger the computation, an *action* is used. It instructs Spark to compute a result from the series of transformations and write the output to the data source. For example:  
` divide.count()`  
`Output: 50`  

#### Spark's APIs  
Spark has two fundamental set of APIs:  
1. Low-level APIs(RDDs, Distributed Variables)  
2. High-level APIs(Dataframes, Datasets,SQL)  

