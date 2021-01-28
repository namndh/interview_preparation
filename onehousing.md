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
              - This method overwrited old data with new data, therefore dim type 1 does not track historical data. Our method is to to conduct dim type 1 but still make them available when want to check historical data is using current/snapshot method
              - I developed a scd Type 1 processor to add auto increment id (new id for new record, maintain id for record which have the same pk but the other information/columns is updated)
            - Type 2:
              - This method track historical by creating multiple records for a given natural key with seperate surrogate keys and different version numbers
              - there are three methods to versioning data:
                - version
                - available date time
                - flag
        - Design tables in google sheets for other non code-based teams con contribute
        - Centralized schemas in Hive, I also do contribute in this project. Centralized schema in Hive helps schema in Presto and Data Warehouse are synchonized.
  - Load: The final step of ETL process. This step is to load the newly transformed data into new destination. We have been using S3-like-object-storage systems such as Minio, Ceph to store fact, dim, cube tables. We store data in both mode full loading for some type 1 dim tables, and incremental for fact, cube and dim tables. To build a data pipelines for ETL process, we have been using Airflow to schedule and CICD.
- Appendix:
  - What is dim, fact, cube tables in our systems?
    - Dim: Dimension table contains dimensions of a fact, acording to Kimball, Dim table is denormalized but in our datawarehouse, where the design is snowflake, the dim table is normalized to remove redundant records.
    - Fact: Fact table contains the numeric measures produced by an opeational measurement event in the real world. Fact table in our data warehouse mainly stored data from transactions of different systems.

### Aimesoft and MoneyLover: 
  - After more than a year not working with computer vision problems I almost forgot about YOLOv3 and other models in machine learning and deep learning. In this two company, I have leant about machine learning engineering. such as data cleaner, data labeling, data augumentation, traing model, optimize model.
  
## Computer Science:
### OS:
  - Thread vs Process:
    - Process means a program in execution, whereas thread means a segment of a process
    - A process is mostly isolated - not sharing memory space, while threads share memory space in a process
  - Parallelism vs Concurency:
    - Concurency: how many process can start at a time
    - Parallelism: how many process can start and run together at a time
### Backend design:
  - What is APIs?
    - An API (Application Programming Interface) is a very generic term - it can be used in all sorts of programming contexts: web app, mobile apps. It's a specification for how a piece of software can be used by other block of codes
  - What programing language do you use? Why? which you prefer?
    - I am recently using Python which has a general purpose that gained extensive popularity. Closely to human read. Interpreter language/ Script language that can run without compiler.
    - why I am using Python?
      - Script language: I can run a block of code fast without compiling. It helps me to explore the data step by step and consumes less time.
      - Closely to human read: Easy to read code and understand the code
### SE questions:
  - Review code: code review is funcdamental to the software development process, even when there's only engineer in a team or doing a project. with review code, you'll can get ideas of the reviewers's knowledge and problem-solving skills, coding conventions. In our case, we dicussed and propose a coding convention checklist that can use to do the code review
  - TDD (test driven development), in our case, we do unit test. we help to get rids of logic erros and coding flaws. In some case, unit tests help us to estimate performance of the code.
  - Agile software development process: this approach based on iterations. It means requirements and solutions are generated throught the collaboration of team's member, other teams and end-users. 
  - OOP: is a type of programming that is based on objects rather than just functions and procedures. Individual object is grouped into classes.
    - Main features of OOP:
      - Inheritance: allows classes inherit common properties from other classes
      - Polymorphsim: refers to the ability to exist in multiple forms. Multiple definitions can be given to a single interface.
        - Example:
          - Overloading: two or more method in one class have the same method name but different paramterss
          ```
          public class BasicCoffeeMachine {
          // ...
            public Coffee brewCoffee(CoffeeSelection selection) throws CoffeeException {
                switch (selection) {
                case FILTER_COFFEE:
                    return brewFilterCoffee();
                default:
                    throw new CoffeeException(
                        "CoffeeSelection ["+selection+"] not supported!");
                }   
            }
          
            public List brewCoffee(CoffeeSelection selection, int number) throws CoffeeException {
                List coffees = new ArrayList(number);
                for (int i=0; i<number; i++) {
                    coffees.add(brewCoffee(selection));
                }
                return coffees;
            }
          // ...
          }
          ``` 
        - Overriding: there are tow methods which have the same method signature (method names, parameters). One in the child class and another in the parent class
      - Encapsulation: refers to hiding data as the data specified in one class is hidden from other classes. Encapsulation helps in isolating implementation details from the behavior exposed to clients of a class.
      - Abstraction: is a mechanism which providing a generalization
      - Encapsulation vs Abstraction: Encapsulation term we use in implementation, implement encapsulation method using access modifiers (protected, public, private)
  - S.O.L.I.D:
    - (here)[https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design]
  - Design Patterns:
    - 