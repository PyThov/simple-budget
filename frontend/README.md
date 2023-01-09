# FRONTEND

## PAGES
 - Single Page App

## Components
 - Summary Graph
 - Summary Card
    - Receives optional fields
        - ie: yearly, monthly, rent
    - Lists number of sources
    - Has an edit button, triggers popup modal
        - Should take dynamic fields
        - Sends payload to backend for updating DB on close
        - Has an add button to add a source
            - Add source will contain a label mactching the card name, for example the 'Income' card would request an 'Income' name
            - Will also contain the amount for the source
            - Sources should be editable on click of text
