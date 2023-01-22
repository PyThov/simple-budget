from pydantic import BaseModel

# Common fields reused in models
class CommonFields(BaseModel):
    category: str # One of: [income, expenses, savings, recreational]
    month: int
    year: int

class BudgetSource(BaseModel):
    source: float

# /budget - Responses
class Budget(CommonFields):
    monthlyValue: float
    yearlyValue: float
    sources: list[BudgetSource]
    taxRate: float | None = None # Only used for 'Income'
    emgFund: float | None = None # Only used for 'Savings'

    class Config:
        orm_mode = True

class BudgetRequest(CommonFields):
    pass

# /source - Requests
class Source(CommonFields):
    source: str
    value: float

# /aggregated - Response
# TODO: This data structure will be determined base on what is needed
#       for the structure of the chart data
class Aggregated(BaseModel):
    tbd: None
    
    class Config:
        orm_mode = True

class AggregatedRequest(BaseModel):
    year: int