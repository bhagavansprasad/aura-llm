## MySQL commands
```SQL
    sp_who2 --List all processes
```


### RDBMS Basic properties 
- Atomicity
- Consistentcy 
- Isolation
- Durability

### Link to sample dataset provided by Microsoft
- https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms

#### Links

##### Trainers Google drive link
https://drive.google.com/drive/u/0/folders/1L8VKDskffYBnixC4fIODATClEdwdSq7o

### Data types
https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver16

#### tinyint 1 byte
    declare @age tinyint
    SET @age = 10 --> Unsigned char 0 to 255
    select @age

#### smallint 2 bytes
    declare @count smallint
    SET @count = -1 --> Signed short int
    select @count

#### int 4 bytes
    declare @count int
    SET @count = -1 --> Signed int
    select @count
    select @count, datalength(@count)
    select @count as Number, datalength(@count) as DataTypeLen

#### bigint 8 bytes
    declare @count bigint
    SET @count = -1 --> Long Signed int
    select @count as Number, datalength(@count) as DataTypeLen

#### float 15 bytes
    declare @count float
    SET @count = 12345.5678 --> float
    select @count as Number, datalength(@count) as DataTypeLen

#### decimal (max 38 bytes)
```SQL
     -- decimal     Storage bytes
        -- 1-9     5
        -- 10-19   9
        -- 20-28   13
        -- 29-38   17
    declare @count decimal
    SET @count = 12345.5678
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count decimal(30, 2)
    SET @count = 12345.5678
    select @count as Number, datalength(@count) as DataTypeLen
```
#### char  1-8000 bytes
```SQL
    declare @count char
    SET @count = 'a'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count char(10)
    SET @count = 'abcde'
    select @count as Number, datalength(@count) as DataTypeLen
```

#### varchar 1-8000 bytes
```SQL
    declare @count varchar
    SET @count = 'a'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count varchar(10)
    SET @count = 'abcde'
    select @count as Number, datalength(@count) as DataTypeLen
```

#### nchar, nvarchar (unicode) 1-4000 bytes
```SQL
    declare @count nchar(10) --20 bytes
    SET @count = 'a'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count nchar(10) --20 bytes
    SET @count = 'abcd'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count nchar(20) --20 bytes
    SET @count = 'సరే'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count nvarchar(10) --2 bytes
    SET @count = 'a'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count nvarchar(10) --8 bytes
    SET @count = 'abcd'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count nvarchar(20) --6 bytes
    SET @count = 'సరే'
    select @count as Number, datalength(@count) as DataTypeLen
```
#### date 'YYYY-MM-DD' 3 Bytes
```SQL
    declare @count date
    SET @count = '2024-05-20'
    select @count as Number, datalength(@count) as DataTypeLen
```
#### time 'HH:MM:SS:MMMMMMM' 3 Bytes
```SQL
	declare @count time
    SET @count = '10:15:20'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count time
    SET @count = '10:15:20:2'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count time
    SET @count = '10:15:20:23'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count time
    SET @count = '10:15:20:234'
    select @count as Number, datalength(@count) as DataTypeLen

```
#### time smalldatetime, datetime datetime2 'HH:MM:SS:MMMMMMM' 3 Bytes
```SQL
	declare @count1 smalldatetime
	declare @count2 datetime
	declare @count3 datetime2
    select @count1 as Number, datalength(@count1) as DataTypeLen
    select @count2 as Number, datalength(@count2) as DataTypeLen
    select @count3 as Number, datalength(@count3) as DataTypeLen

```
### DDL
```SQL
-- CREATE
-- ALTER
-- DROP
-- USE
-- TRUNCATE
```
### Questions

declare @count char()
