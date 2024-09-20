# Question 1: Parse and Summarise Log Files

### Problem:
Write a script that reads a server log file, extracts errors, and outputs a summary of errors grouped by error type and how many times each error occurred. 


### Execution
```shell
docker build -t error-log-parser .
docker run --rm -v $(pwd):/app error-log-parser
```

### Output Can also be viewed in GitHubActions
* Navigate GitHub Actions
* Click on `Python Syntax Check and Docker Build` in the leftside panel.
* Select most recent successful run
* Expand `Run Docker Container`