# Spark  
- [The Big Data Problem](#the-big-data-problem)
- [What is Spark](#what-is-spark)
## The Big Data Problem
In the past, computers became faster every year as the speed of processors increased. These processors could run more tasks per second than the previous one's and as a result applications also became faster gradually without any changes needed to their code. This led to a large ecosystem of applications which were mostly run on a single processor.
Over a period of time, the computations have become larger and huge volumes of data was generated and the trends of improved processor could not scale up to the demand and finally in 2005 this trend has stopped due to hard limits in heat dissipation and a major switch took place where developers started adding more parallel CPU cores with all running at the same speed.
The next step was to modify the applications to add paralellism in order to run faster and set a stage for programming models with a unified computing engine such as **Apache Spark**.  
## What is Spark
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
Transformations are used to build up a logical transformation plan and to trigger the computation, an *action* is used. Spark does not read data from the source until an action is called. It instructs Spark to compute a result from the series of transformations and write the output to the data source. For example:  
` divide.count()`  
`Output: 50`  
### Spark's Toolset  
Apache Spark has a vast ecosystem of tools and libraries. Spark's toolkit is composed of Spark's APIs(Low-level & High-level) and a series of Standard Libraries for additional functionality. Spark also has a built in command-line tool i.e *spark-submit* which makes application productiion easy and also lets user send the application code to a cluster and launch it to execute there and the application will run until it completes the task or encounters an error.  

### Spark's APIs  
Spark has two fundamental set of APIs: Unstructured APIs(RDDs, Distributed Variables) & Structured APIs(Dataframes, Datasets,SQL)  
#### Unstructured APIs   
Spark has a number of low-level APIs to allow arbitary java and python object manipulation via Resilient Distributed Datasets (RDDs). Everything in spark is built on RDDs. All high-level operations are also built on top of RDDs and compile down to these low-level tools for an efficient distributed execution. RDDs are lower than Dataframes because they reveal physical execution characteristics to end users. RDDs are mainly used to parallelize raw data that is stored in the memory of the driver machine.  
#### Structured APIs  
The Structures APIs are a tool for manipulating all sorts of data from unstructured log files to semi-structured CSV files to highly structured Parquet files. There are 3 types of structured APIs i.e *Datasets*, *DataFrames* & *SQL tables and views*. The majority of Structured APIs apply to both batch and streaming computation which means that using structured APIs it is easy to migrate from batch to streaming. These are used to write the majority of data flows in Spark.  
#### DataFrames and DataSets  
These are the 2 structured collections of Spark. These are table-like collectionswith rows and columns. Each column must have same number of rows in a collection and *null* can be used in the absence of any value. Each column also stores type informationthat must be consistent for every row in the collection. In Spark, Datasets and Dataframes are immutable , lazily evaluated plans that specify what operations to apply to data residing at a location to generate the output. DataFrames are *untyped* as spark maintains them completely and only checks whether those types line up those specified in the schema ar *runtime*. DatSets are *typed* abd checks whether types conform to the specification at *compile-time*.  
**Columns**:- Columns are a simple datatype like an integer or a string. They are similar to columns in a spreadsheet.  
**Rows**:- A row is similar to a record of data. Each record in a dataframemust be of type *Row*. These rows can be created from SQL, from RDDs and from data sources.  
#### Structured API Execution  
Spark code is executed across a cluster in these following steps:  
1. Write Dataframe/Dataset/SQL code.   

2. If avlid code, Spark converts this to a *Logical Plan*.  

3. Spark transfroms this Logical Plan to a Physical Plan, checking for optimizations along the way.  

4. Spark then executes this Physical Plan on the cluster.  

The user written code is submitted to spark through the console or via a aubmitted job. Then it is passed through a *Catalyst Optimizer* which decides how the code must be executed a lays out a plan, both logical and physical and finally thecode is run and the result is returned to the user.  
#### Logical Plan  
The logical plan represents a set of abstract transformations that do not refer to executors or drivers, it is mainly to convert user's expression to a most optimized version.  
In the first step, user code is converted into an *unresolved logical plan*. This plan is unresolved because although might be valid, the tables or columnsthat it refers to might or might not exist.  
In the next phase of analysis, Spark uses a *Catalog*, a repository of all table and Dataframe information. Spark might reject this unsolved logical plan if the required table or column name does not exist in the catalog. If all the required data is present in the catalog the unresolved logical plan is converted to a *resolved logical plan*.  
In the next step, the resolved logical plan is passed through a *Catalyst optimizer*, a collection of rules that attempt togenerate an *optimized logical plan* by pushing down predicates or selections.  
#### Physical Plan  
In the first step, Spark considers the optimized lpogical plan and begins the physical planning process. The Physical plan is also called as a *Spark Plan* and it specifies how the logical plan will be executed on the cluster by generating different *physical execution strategies*.  
In the next step, all these physical execution strategies are compared through a *cost model*. The cost comparision involves choosing how to perform a given joinby looking at the physical attributes of a given table, no. of partitions etc. This cost model gives out the best physical plan as an output.  
In the final step, upon selecting the best physical plan, Spark runs all the code over RDDs, the low-level APIs of Spark. Spark performs further optimizations at run-time and the generated result is returned to the user.


