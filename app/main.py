from fastapi import FastAPI, Query
from typing import List
from typing import Optional

app = FastAPI()


@app.get("/ranking")
def read_root(advertiser_campaigns: List[int], advertiser_campaigns_bids: List[int], maximum: Optional[int] = 10):
    
    return {"Hello": "World"}



