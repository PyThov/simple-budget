# FRONTEND

## PAGES
 - Single Page App

## Component Requirements
 - Summary Graph
    - Shows percent spread of income across different spending categories
 - Summary Card
    - Receives optional fields
        - ie: yearly, monthly, rent
    - Lists number of sources
    - Has an edit button, triggers popup modal
        - Should take dynamic fields
        - Sends payload to backend on close
        - Has an add button to add a source
            - Add source will contain a label matching the card name, for example the 'Income' card would request an 'Income' name
            - Will also contain the amount for the source
            - Sources should be editable on click of text

## Accessible API Routes
 - `/budget`
 - `/source`
 - `/aggregated`
