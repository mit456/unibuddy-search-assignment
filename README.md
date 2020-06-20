# unibuddy-search-assignment
search in three sentence summary of a book

### Steps to run the project/server testing.
1. Change directory to `node-api`.
2. Do `npm install` to install npm packages used in project.
3. Create `.env` file in `node-api` directory with following content:-
    ```
    NODE_PROCESS_TYPE="web"

    NODE_ENV="development"
    PORT=3000

    # Logger configuration
    LOGGER_LEVEL="debug"
    LOGGER_ENABLED="true"
    ```
 4. Run node server with following command, `node web/server.js` and check following on terminal:-
    ```
    info: Express listening on port 3000
    ```
 5. Use Postman and make request to `http://localhost:3000/api/search` with following body data:-
    ```
    {
      "queries": ["is your problems", "achieve take book"],
      "responseCount": 3
    }
    ```

 ### Steps to check standalone search utility.
 1. Be at project root dir and can try followings:-<br/>
 1.1. To fetch search result for a query:-<br/>
    `python3 ./utilities/search/core.py --query "is your problems" --response_count 3 --type "summary"`<br/><br/>
 1.2. To fetch search result for queries:-<br/>
    `python3 ./utilities/search/core.py --queries "is your problems, achieve take book" --response_count 3 --type "summary"`
