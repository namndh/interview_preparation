# Interview Preparation
## CS Fundamental

### Database
1. Compare relational DB and NoSQL.
    - Relational DB or SQL databases have a table-based data structure, with a strict predefined schema required. Relational databases are vertically scalable, but usually more expensive
    - NoSQL databases or non-relational databases can be document based, graph databases, key-value pairs or wide-column stores. NoSQL databases don't require any predefined schema. NoSQL databases are horizontal scaling with morer cost-efficient
    1.1 How these thing scale up?
        - Relational DBs are vertically scalable but typically expensive. Since they require a single server to host the entire database, in order to scale, we need to buy a more powerful server
        - NoSQL DBs scaling is much cheaper, because you can add capacity by scaling horizontally over cheap, comodity servers.
    1.2 How Transactions is handled?
        - Transactions are often composed of multiple statements
        - To handle transactions while remain scalability and performance, NoSQL databases relies upon a model know BASE model
        - SQL databases handle transactions according to ACID models
    1.3: ACID of SQL and BASE of NoSQL? Why NoSQl is eventual consistency?
        - ACID:
            - Atomicty: guarantees that each transaction is treated as a single "unit". which either succeeds completely or fails completely: if any and statements constituting a transactions fails to complete, the entire transactions failes and the database left unchanged
            - Consistency: ensures that a tracsaction can only bring the database from one valid state to another, maintaining database invariants. The prevents database corruption by an illegal transaction, but does not guarantee that a transaction is correct.
            - Isolation: Transactions are often executed concurrently. Isolation ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially
            - Durability: guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure. This usually means that completed transactions are recorded in non-volatile memory
        - BASE: 
            - Basically Available: basic reading and writing operations are available as much as possible (using all nodes of database clusters), but without of any consistency guarantees
            - Soft state: without consistency guarantees, after some amount of time, we only have some probability of knowing the state, since it may not yet have converges
            - Eventually consistent: if the system is functioning and we wait long enough after any given set of inputs
        - Eventual consistency is a reasonable trade-off of durability risk versus availability. Mostly NoSQL dbs try to achieve high availability for the application which help increase the perfomance of the system when an application execute a write operation to the db node
        , it may reponse a success response and application is able to execute another operation while data may not be persisted into the disk
    1.4. CAP theorem in the case.
        - Because NoSQL DBs is horizontal scalable it means that NoSQL DBs contains replicas and it's also horizontal partitions so we can use CAP theorem to describe a NoSQL DMBS
        - CAP Theorem:
            - Consistency: It is not same as consistency in ACID. It means all clients see the same data at the same time, no matter which node they connect to.
            - Availability: means that any client making a request for data gets a response, even if one or more nodes are down. Or all working nodes in the distributed system return a valid response for any request, without exception
            - Partition Tolerance: means that the cluster must continue to work despite any number of communication breakdowns between nodes in the system
        - CP database: A CP database delivers consistency and partition tolerance at the expense of availability. When a partition occurs between any nodes, the system has to shut down the non-consistent node until the partition is resolved
        - AP database: An Ap database delivers availability and partition tolerance at the expense of consistency. When a patitions occurs, all nodes remain available but those at the wrong end of a parition might return an older version of data.
        when the partition is resolved, the AP databases will typically resync the nodes to repair all inconsistency in the system.
        - CP database: A CA database delivers consistency and availability across all nodes. It can't do this if there is a partiton between any two nodes in the system.
2. What is parameterized statement or prepared statement?
    - Prepard statement is feature used to execute the same or similar databate statements repeatedly with high effiency. Typically used with SQL statements such as querries or updates, the prepared statement takes the form of a template into which certain constant values are substitued during each execution.
    - Workflow:
        - Prepare: at first, the application creates the statement template and send it to the DBMS. Certain values are left unspecified, called parameters
        - Then, the DBMS compiles the statement template and stores the result without executing
        - Execute: when the application supplies values for the parameters, the DBMS execute the statement.
    - Advantages:
        - The compiling the statement if incurred only once. However not all optimization can be performed. Optimaztion based on specific parameters values.
        - Avoid SQL Injection because values which are transmitted later using a different protocol from compiling the statement template. If the statement template is not derived from external input, SQL Injection cannot occur.
    2.1 What is SQL Injection? How to avoid?
    - SQL Injection is a code injection technique, used to attack data-driven applications, in which malicious SQL statments are inserted into an entry field for execution.
    - To prevent SQL Injection, We can use parameterized statement, santitizing inputs, escaping input or use object relational mapping
    2.2. In java/scala, after using resultSet we should close connection from resultSet to DB. So we can not reuse a compiled query

3. How indexing work internally?
    - Database index fasten speed of a query is executed by DMBS. Index is a data structure which is created on one or more columns of a table in DBMS. When index is created on a column or a set of columns in the table, it actually creates a lookup table with columns and pointer to the memory address where a row with these columns is actually stored
    - When we query a table with columns in `where` clause, the parser first checks if these columns are a part of index, and if there is a index look up table for them, then it checks for the memory address where the record is stored. It then directly jumps to that memory address and returns the result to user
    - Indexes speed up searching in the table, but executing UPDATE, INSERT, or DELETE statments require updating data in the index. When we change the data which get the index update, typical index tree in DBMS is not self-balancing, that requires us to rebuilt the index tree
    3.1 What algorithm and data structure indexing used? and why?
    - B-Tree data structure is used to store the indexs. This is the B-Tree data are traversed, searched, inserted, deleted, and updated in logarithmic time, moreover, B-Tree data ware always sorted and stored. The data values stored in B-Tree are balanced.
    - Howerver, we can configure which data structure used for the index.
    3.2 How composition indexing works?
    - Assume we make the index in a composition of three columns (a,b,c), there columns will be concatenated together, and those concatenatd keys are stored in sorted order using B Tree. When we perform a search, concatenation of search keys is matched against those of the composited index.
    - We defined the index on three columns (a,b,c), we have search capabilty using index on col a, col a and col b
    3.2 How to know your query is using index?
    - To know a query is using index or not, we can using `explain` operation to check the query. For example in MySQL, we can look up into the output of explain operation, the column key represent which index is used
    3.3 How index work in this case: `WHERE age = 5` and `WHERE age > 5`?
    - If we use B-Tree for the index column age, age = 5, search to node in the B-Tree where is value equal to 5. with age > 5 we can get all the nodes in the B-Tree that value larger than 5
    - The complexity if O(log(n))
    3.4 Indexing with char?
    - CHAR indexing or FULLTEXT indexes in MySQL are created on text-based columns to help speed up queries and DML operations
    - FULLTEXT indexes find keywords in the text instead of camparing values to the values in the index
    - FULLTEXT searching if performed using MATCH() ___ AGAINST syntax
    - FULLTEXT in MySQL using inverted index. That store a list of words, and for each word, a list of documents that the work appears in and the position information of each word as a byte offset.
4. The complexity of SQL query? How to measure it? How SQL optimize a query?
    - The complexity of SQL query depends on how SQL engine process the query
    - To optimize a SQL query, we can use explain statement. With help of explain statement, we can see where we should add indexes to tables, we can also use explain statement to check where the optimizer joins the tables in optimal orders.
    4.1 Complexity of this query `SELECT * FROM abc ORDER BY name LIMIT 10 OFFSET 1000000`. Because the ORDER BY statement will execute first, so without indexing, the complexity to going to o(N). To optimzing it, we can index the column `name`.
    4.2 The complexity of COUNT(*) depends on DB, if the DB engine store the values of how many records in the table, the complexity is O(1) otherwise, O(N)
    4.3 Depend on the use case, add indexes to make query faster using indexes instead of scanning full table.
    4.4 JOIN and INNER JOIN has complexity O(MxN), OUTERJOIN has complexity O(M+N)
5. What is Database Replicating? When we need it?
 - Database Replicating is the process of copying data from a central database to one or more databases. The cental databases is called the publication databases because it provides the data for users at other sites. The data in the publication database is copied or replicated to subscription databases at other locations.
 All users whether connected to the slave or master see the same data and work on the same records optionally.
 - Recovery purpose, backup plan, business rules, privacy rules 
 5.2
 - The binary log is a set of log files that contain information about data modifications made to a DBMS instance. It contains all statements that update data. Statements are stored in the form of "events" that describe the modifications.
 The binary log events describe actions that can be used to reprocedure the same changes of global state which has happened on the server
 - The binary has two types: statement-based and row-based
 - There are two protocols to sync bin log from master to slave : push to slave and Sync from master
 5.3
 - Yes, MySQL provides a model that called replication relay allow a slaveDB can be a slave of other slaveDB
6. What is Database Sharding?
 - Sharding is a database architecture pattern related to horizontal partitioning - the practice of seperating on table's rows into multiple different tables, known as partitions. Each partition has the same schema and columns, but different rows. In other words, the data held in each is unique and independent of the data held in other partitions.
 - Usage: to scale up the system when the vertical scale up is more expensive. Sharding can ensure high availability and speed up processing
 6.1 To remains unique ID accross sharded DB:
    - GUID - Globally unique ID
    - Give each shard it's own ID and set ranges for each shard
 6.2 To query a sharding databases, we can union these tables then query.

7. 
 - when DBMS start execute a transaction, DBMS to roolback by preserving the original data by storing it in an area of database called the rollback segment. So when the trasaction failed, DBMS just re-copies those pages of data to recover current legal state of the DBMS
 - Dirty Read occurs when a transaction is allowed to read data from a row that has been modified by another running transaction or not commited yet.
 - To prevent race condition in database when concurrent transactions occurs, we should lock the database when a transaction occurs ultil succeed or fail completely then we unlock it for other transactoin

### Spark/Hadoop
1. What is Hadoop/Spark?
 1.1 Hadoop: is a software framework which is used to store and process big data. It breaks down large datasets into smaller pieces and processes them parallely which saves times. It is a disk-based storage and processing system.
 It can scales to many nodes, in Hadoop, multiple nodes connected to each other work collectively as a single system. There are two components of Hadoop: HDFS and MapReduce
 1.1.1 HDFS: It is the storage system of Hadoop. It has master-slave architecture, which consists of a single master call "NameNode" and multiple slaves called "DataNodes". A NameNode and its DataNode form a cluster. There can be multiple clusters in HDFS.
   - A file is split into one or more blocks and these blocks are stored in a set of DataNodes.
   - NameNode maintains metadata and also executes operations like the renaming the files (configure metadata)
   - DataNodes store actual data and also perform tasks like replication, deletion of data as instruted by NameNode, DataNodes communicates with each other 
1.1.2 MapReduce: is a programming framework that used to process BigData. It splits dataset into smaller chunks which the map task processes parallely and produces key-value pairs as output.
   - MapReduce architecture: It has as master-slave architecture which consists a single master server called "Job Tracker" ans a "Task Tracker" per slave node that runs along DataNode.
   - JobTracker is responsible for scheduling the tasks on slaves, monitoring them and re-execute the failed tasks
   - TaskTracker executes the tasks as directed by master and return the status of the tasks to job tracker.
   The DataNode in HDFS and TaskTracker in MapReduce periodically send heartbeat messages to their masters indicating that it is alive.
1.2 Spark: is a cluster compute engine for processing BigData. It uses in-memory processing for processing BigData which makes it highly fasters. It is also a distributed data processing engine. It does not have its own storage system like Hadoop havs, so it requires a storage system platform like HDFS. It can be run on local mode or cluster mode.
1.2.1 Architeture: Spark also follows master-slave architecture. Apart from the master node and slave node, it has a cluster manager that acquires and allocates resources required to run a task
    - In master node, there is driver program that is responsible for creating Spark Context. Spark Context acts as a gateway for the execution of Spark application.
    - The Spark context breaks a job into multiple tasks and distributes them to slave node called Worker Nodes.
    - Inside the worker nodes, there are executors who execute the tasks
    - The driver program and cluter manager communicate with each other for the allocation of resources. The cluster manager launches the executors. Then the drivers send the tasks to executors and monitors their end-to-end execution.
1.2.2 Data Presentation:
    - RDD: is an immutable distributed collection of distributed data that can be process parallely with a low-level API that offers transformation and actions. We use RDD when data in unstructed or imposing a schema, such as columnar format, while processing or accessing data attributes by name or column
    - Dataframe: is similar to a table in a relational database. Dataframe is immutable. It has particular schema. We can perform SQL like queries on a dataframe. It is used only for structured and semi-structured data.
    - Dataset: Dataset is a collection of strongly-typed JVM object that can help us to expose syntax errors and analysis errors at compile time instead or run time. Dataset with typed object JVM can provide a optimal performance for data processing.
1.2.3 Spark Ecosystem
    - Spark Core: it contains the basic functionality of Spark. All other libraries in Spark are build on top of it. It supports RDD as its data represenations. Its responsibilities include task scheduling, fault recovery, memory manangement and distribution of jobs across worker nodes.
    - Spark Streaming: it is used to process data which streams in realtime
    - Spark SQL: it supports using SQL queries. It supports data to be represented in the form of DataFrame and DataSet.
2. Spark and Hadoop comparision:
2.1 Speed:
    - In Hadoop, all the data is stored in the Hard disks of DataNodes, whenever the data is required for processing, it is read from the disk and save into the hard disk, moreover, the data is read sequantially form the begining, so the entire dataset would be read from the disk, not just the portion that is required.
    - While in Spark, the data is stored in RAM which makes reading and writing data highly faster
    - Suppose there is a task that requires a chain of jobs, where the output of the first is input of the second and so on. 
        - In MapReduce, the data is fetched from disk and output is stored to disk, then the second job, fetched the output from the first from disk and process then save the output to the disk and so on
        - In Spark, the data is saved into the RAM
2.2 Data Processing:
    - Hadoop is suitable for batch processing
    - Spark can be used for both batch processing and streaming processing
2.3 Cost:
    - Both Hadoop and Spark are open source Apache products, so they are free. But they have hardware cost associated with them. According to data saving strategy, Spark requires more RAM which is more expensive in than disk required from Hadoop.
2.4 Simplicity:
    - Both are easy to use
2.5 Fault Tolerance:
    - In Hadoop, the data is divided into blocks which are stored in DataNodes. Those blocks have duplicate copied stored in other nodes in other nodes with the default replication factor. If a node go down, the data can be retrieved from other nodes.

### Datawarehouse
1. Datawarehouse is a subject/object oriented, integrated, time-variant, and novolatile collection of data that supports managerment's decision-making process
2. Subject oriented datawarehouse mean that data in the datawarehouse stores the information around a pariticular subject such as product, customer, sales, etc.
3. OLAP is Online Analytical Process, OLTP Online Transactional Process
4. A datawarehouse contains historical databases information that is made available for analysis of the business whereas an operational database contains currrent information that is required to run the business
5. Datamart contains the subset of organization-wide data. The subset of data is valuable to specific groups of an organization or application. In other words, we can say that datamart contains data specific to a particular group.
6. Dim table: is a table in a star schema of a datawarehouse. Dim table used to describe dimensions, they contain dimension keys, values, and attributes.
    - SCD type 0: dimension attributes never change or in other words, the attributes have durable values. Such as: Date dimension attributes.
    - SCD type 1: this method overwrite old data with new ones. and therefore does not track historical data
    - SCD type 2: this method tracks historical data by creating mutiple row of the records which have update with different surrogate keys and/or different version numbers.
        - We can use different types of attribute to indicate version: version number, effective date, current_flag, etc
    - SCD type 3: this method tracks changes using seperate columns and preserves limited history as it is limited to the number of columns designated for storing historical data.
    - SCD type 4: this track the history by create history tables and current tables
  