
### Ollama Commands
## Links
  - Build a Private GPT with simple UI
  https://www.youtube.com/watch?v=F0lO8d15_GY


  - What is RAG
  https://www.youtube.com/watch?v=u47GtXwePms

#### Links
 - https://www.youtube.com/watch?v=fnvZJU5Fj3Q&list=PL4041kTesIWby5zznE5UySIsGPrGuEqdB&index=3
Ollama
```sh
  ollama
  ollama list
  ollama run phi3 # to pull and run phi3 model
  ollama show phi3 --modelfile
  # Test ollama
  curl http://localhost:11434/api/generate -d '{
    "model": "phi3",
    "prompt": "How old is Indian history?",
    "stream": false
  }' | jq .
```
### Create own model 'aura-phi' from another model 'phi3'
```sh
ollama show phi3 --modelfile >  arr-modelfile
ollama create aura-phi --file aura-modelfile
ollama list
ollama run aura-phi:latest
```

### Running local LLMs and exposing to internet world
 - https://www.youtube.com/watch?v=syR0fT0rkgY&list=PL4041kTesIWby5zznE5UySIsGPrGuEqdB&index=2
```sh
 docker run -d --network=host \
 -v open-webui:/app/backend/data \
 -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```
From Browser
- http://127.0.0.1:8080

```sh
 snap install ngrok
 ngrok config add-authtoken <auth-token-from ngrok.com> 
 ngrok http http://localhost:8080
```

### Scrap
https://github.com/iongpt/LLM-for-Whatsapp

### MS SQL Server Management Studio Installation
  - Insallation steps [link](https://www.nobledesktop.com/how-to-install-sql-server-management-studio)
  - Details to provide while running 
  ```json
    Server Type: Database Engine
    Server Name: 127.0.0.1, 1433
    Authentication: SQL Server Authentication
    Login: sa
    Password: Mssql!Passw0rd
    Tick "Trust Server certificate"
  ```
  ## SQL
  ### Data Definition Language
  ```SQL
    CREATE DATABASE happy;
    USE happy;
    DROP DATABASE happy;
  ```
  ### Data Types
  #### Numerical Data Type
  ```
    bigint   (long int 8 bytes)
    int      (int 4 bytes)
    smallint (short 2 bytes)
    tinyint  (unsigned char)
    decimal  (s, d)
  ```
  #### Char Data Type
  ```
    char(s)   (255)
    varchar   (255)
    text      (65535)
  ```
  #### Date & Time Data Type
  ```
    date(s)       (YYYY-MM-DD)
    varchartime   (HH:MM:SS)
    Year          (YYYY)
  ```
  ### Constrints
  ```
    Not Null
    Default
    Unique
    Primary Key
    Not Null + Unique
  ```

  ```SQL
    CREATE TABLE EMPLOYEE(
    e_id int not null,
    e_name varchar(20),
    e_salary int,
    e_age int,
    e_gender varchar(20),
    e_dept varchar(20),
    primary key(e_id)
  );

  INSERT INTO EMPLOYEE VALUES (
    1,'sam', 95000, 45, 'Male', 'Operations' 
  );

  INSERT INTO EMPLOYEE VALUES (
    2,'bob', 80000, 21, 'Male', 'Spport' 
  );

  INSERT INTO EMPLOYEE VALUES (
    3,'Anne', 125000, 25, 'Female', 'Analytics' 
  );

  INSERT INTO EMPLOYEE VALUES (
    4,'BAnne', 12500, 25, 'Female', 'Programming' 
  );

  INSERT INTO EMPLOYEE VALUES (
    5,'Bhagavan', 12456, 28, 'Male', 'Management' 
  );

  INSERT INTO EMPLOYEE VALUES (
    6,'Saketh', 123432, 20, 'Male', 'Student' 
  );

  SELECT * FROM EMPLOYEE;

  SELECT e_id, e_name from EMPLOYEE;
  SELECT e_id, e_name, e_age from EMPLOYEE;

  SELECT DISTINCT  e_gender from EMPLOYEE;
  SELECT e_gender from EMPLOYEE;

  SELECT e_name, e_gender from EMPLOYEE WHERE e_gender='Female';
  SELECT e_name, e_gender from EMPLOYEE WHERE e_gender='male';
  SELECT * from EMPLOYEE WHERE e_age<30 AND e_salary > 90000;
  SELECT * from EMPLOYEE WHERE e_name LIKE 'B%';
  SELECT * from EMPLOYEE WHERE e_age LIKE '_5';
  SELECT * from EMPLOYEE WHERE e_age BETWEEN 25 and 50;

  A INNER JOIN B -->  A INTERSECTION B
  A LEFT JOIN  B -->  A + A INTERSECTION B
  A RIGHT JOIN B -->  B + B INTERSECTION A
  A FULL JOIN  B -->  A UNION B
```

# LLMs
## Ollama
### Installation 
```Shell
```
```Shell
    https://python.langchain.com/docs/get_started/quickstart/
    curl -fsSL https://ollama.com/install.sh > install.sh
    sudo sh install.sh
    ollama pull llama2
    sudo pip3 install langchain
```
### Pulling new models
```Shell
   ollama pull nomic-embed-text
```
### Test ollama locally with curl
```Shell
    curl http://localhost:11434/api/generate -d '{
      "model": "llama2",
      "prompt":"Why is the sky blue?"
    }'
```

### Test script
```Python
    from langchain_community.llms import Ollama
    from langchain.callbacks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

    llm = Ollama(
        model="llama2", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    )
    # llm.invoke("The first man on the summit of Mount Everest, the highest peak on Earth, was ...")
    llm.invoke("What is Prabhas caste")
    print()
```










