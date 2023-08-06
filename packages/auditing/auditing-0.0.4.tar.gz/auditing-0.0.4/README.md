The purpose of this library is to provide a simple mechanism for auditing of user actions in Flask-based web applications. 

### Example

To setup auditing, simply import the package and run the setup method with the appropriate arguments. As an example, let's consider a postgres database. First, spin in up via docker

    docker run --name my-postgres -p 5432:5432 -d postgres

Next, setup the connection to the database,

    import auditing

    args_to_postgres = dict(database="mydb", user="postgres", password="", host="127.0.0.1", port="5432")
    auditing.setup("postgres_auto", args_to_postgres)

The special "postgres_auto" driver creates the database and any needed tables automatically. Furthermore, it extends tables when new properties are added. If this is not needed, simply use the "postgres" driver instead. Subsequently, auditing can be performed as

    from auditing import audit
    
    audit("mytag", a="1", b="2", username="me")


where "mytag" identifies the audit collection (in postgres sql it will map to the table name) while the following keyword arguments denotes the data (in the above example, the value "1" will be inserted in column "a" and the value "2" in column "b"). Hence the result in postgres is,

     username |          datetime          | a | b 
    ----------+----------------------------+---+---
     me       | 2019-12-05 13:18:00.785871 | 1 | 2

If the username is not provided, an attempt is made to extract it from the session context. If the user cannot be identifies, the audit is cancelled. If the audit is made within a request context, the following data is appended, 

* ip (from "X-Forwarded-For" header)
* host (from Flask request)
* path (from Flask request)
* username (from Flask session)  

The current datetime is always appended unless overwritten via the "dt" argument.

[*] In addition to postgres, elastic search is supported. Other databases can be used, simply inject a driver via the "inject_driver" method. 


