# BACKEND - API

## Tools
 - Python
 - FastAPI
 - SQLAlchemy (PostgreSQL)
    - Follows ORM as described by SQLAlchemy documentation: https://docs.sqlalchemy.org/en/14/orm/quickstart.html

## Terminology
 - Source
    - A Source refers to an item in a given category. For example, a 'source' in the 'Income' category would be money being made from a job, counting towards income.
- Category
    - A category refers to one of the incoming or outgoing money options from: Income, Expenses, Savings, or Recreational

## Requirements
 - User specific data for...
    - Summary graph
    - Income
    - Expenses
    - Savings
    - Recreational 
 - Functionalities
    - Add / Remove a source
    - Update existing data
    - Account management (*out of current scope*)

## ENDPOINTS
 - Namespace: `/api/v1`
 - Common:
    - Headers:
        ```json
            {
                "Authorization": "Bearer q1w2e3r4t5y6u7i8o9p0" // Users auth token (*Out of current scope*)
            }
        ```
 - Paths:
    - `/budget`
        - `GET`
            - Gets the budget data for the specified category in the specified month and year
            - Request: `/budget?category={category}&month={month}&year={year}`
                - Query Parameters:
                    - Required
                        - `category`: ie: `"income"`
                        - `month`:    ie: `1` (1=january)
                        - `year`:     ie: `2023`
            - Response:
                - Headers:
                    ```json
                        {
                            "Content-Type": "application/json"
                        }
                    ```
                - Body
                    ```json
                        {
                            "category": "string",
                            "month": "integer",
                            "year": "integer",
                            "monthlyValue": "float",
                            "yearlyValue": "float",
                            "sources": [
                                {
                                    "string": "float",
                                },
                            ],
                            "taxRate": "float", // Optional, used for 'Income'
                            "emgFund": "float", // Optional, used for 'Savings'
                        }
                    ```
    - `/source`
        - `POST`
            - Creates a new source for the given category and month (if applicable)
            - Request: `/source`
                - Headers:
                    ```json
                        {
                            "Content-Type": "application/json"
                        }
                    ```
                - Body:
                    ```json
                        {
                            "category": "string",
                            "month": "integer",
                            "year": "integer",
                            "source": "string",
                            "value": "float"
                        }
                    ```
            - Response:
                - Success: `200`
        - `PUT`
            - Updates a source for the given category and month (if applicable)
            - Request: `/source`
                - Headers:
                    ```json
                        {
                            "Content-Type": "application/json"
                        }
                    ```
                - Body:
                    ```json
                        {
                            "category": "string",
                            "month": "string",
                            "year": "string",
                            "source": "string",
                            "value": "string"
                        }
                    ```
            - Response:
                - Success: `200`
        - `DELETE`
            - Deletes a source for the given category and month (if applicable)
            - Request: `/source?category={category}&month={month}&source={source}`
            - Response:
                - Success: `200`
    - `/aggregated`
        - `GET`
            - Gets the aggregated budget data for graph display
            - Request: `/aggregated?year={year}`
            - Response:
                - Headers:
                    ```json
                        {
                            "Content-Type": "application/json"
                        }
                    ```
                - Body:
                    - **TBD**

## Steps Taken
 - Setup file structure
   - /ui
      - Init ReactJS project with Vite
   - /backend
      - Setup poetry
      - /api
      - /db
 - Setup docker containers
    - DB connection and running Python
 - Setup database models
    - Make sure this works with database initialization
    - Resource: https://fastapi.tiangolo.com/tutorial/sql-databases/
 - Setup API
   - Defined API models
   - Setup first API route
      - Verify functionality
   - Setup the rest of the API routes
      - defined paths and functions
      - added query parameters
 - Setup DB
   - Create DB accessor functions
      - Create `get` functions for each table
      - Create `add` functions for each table
 - Continue API functions
   - Setup `get_budget` function for accessing database
 - Configure Docker and test host communication
      
