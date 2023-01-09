# BACKEND - API

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
            - Gets the budget data for the specified category in the specified month
            - Request: `/budget?category={category}&month={month}`
            - Query Parameters:
                - Required
                    - `category`: ie: `"income"`
                    - `month`:    ie: `1` (1=january)
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
                        "month": "string", // Only required for `Income`
                        "source": "string",
                        "value": "string"
                    }
                ```
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
                        "month": "string", // Only required for `Income`
                        "source": "string",
                        "value": "string"
                    }
                ```
        - `DELETE`
            - Deletes a source for the given category and month (if applicable)
            - Request: `/source?category={category}&month={month}`
    - `/aggregated`
        - `GET`
            - Gets the aggregated budget data for graph display
            - Request: `/aggregated`
