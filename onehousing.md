# Data Engineer
## Projects
### Teko:
- ETL: 
  - What is ETL? ETL is stand for Extract, Transform and Load process of big data. In Teko, I have been doing ETL for big data which is about dozens of TB data and growing about hundreds of data per day.
    - Extraction - Ingestion: Getting data into the data warehouse: I have been doing ingestion from multiple sourcees such as sequential DBs like postgres, mysql, sqlServer, ... etc or non-sequential DBs like MongoDB. I contributed in developing a Scala library to simply the ingestion process from DBs. I am also contributing in developing streaming ingestion and ingestion from Elastic Search. 
    - Transformation: I have been doing designing, cleaning, standardization, de-duplication, verification by exploring data, visualization, examining business and technical documentations.
      - How exploring data? Using Spark to load data intergrated with reading documentations we can know number of records, data types, primary keys, business keys. Know what data look like (scale of number, upper-bound, lower-bound of values, decoder of string columns, enum values). The step helps a lot in designing data
      - How visualize work? In this step, I usually use Pandas, Matplotlib to visualize data to understand trend, noise, outlier of data. Combined with reading documentation, we can get rid of abnormal data, error data inputed by user. For example, with data of POS365, user can manually input price for goods so sometimes we can get the price up to billion VND for a bamboo stick which lead to mistakes when calculating revenue or benefit in report. Which chart? mostly Histogram
      - How we design data?
        - SSOT: Single source of truth. It means that data of a instance is only stored in place. It helps to eliminate duplicate data and reduce time spent of identifying which recored data is more precision, sufficient.
        - SnowFlake design
        - Modeling data base Ralph Kimball's theory
          - Dimensions table:
            - Type 1: 
              - definition
              - I developed a scd Type 1 processor to add auto increment id (new id for new record, maintain id for record which have the same pk but the other information/columns is updated)
            - Type 2:
              - definition
        - Design tables in google sheets for other non code-based teams con contribute
        - Centralized schemas in Hive, I also do contribute in this project. Centralized schema in Hive helps schema in Presto and Data Warehouse are synchonized.
  - Load: The final step of ETL process. This step is to load the newly transformed data into new destination. We have been using S3-like-object-storage systems such as Minio, Ceph to store fact, dim, cube tables. We store data in both mode full loading for some type 1 dim tables, and incremental for fact, cube and dim tables.
- Appendix:
  - What is dim, fact, cube tables in our systems?
    - Dim: Dimension table 
