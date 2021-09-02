from fastapi import FastAPI, Query
from typing import List
from typing import Optional
import random

app = FastAPI()


@app.get("/ranking")
def read_root(advertiser_campaigns: List[int], advertiser_campaigns_bids: List[float], maximum: Optional[int] = 10):
    # Shuffle tuples list in case of repeated bids
    shuffled = list(zip(advertiser_campaigns, advertiser_campaigns_bids))
    random.shuffle(shuffled)

    # Sort according to bids
    sorted_advertiser_campaigns = sorted(shuffled, key=lambda x: x[1])
    
    # Keep only ids according to maximum 
    campaign_ids = []
    for index, tuple in enumerate(sorted_advertiser_campaigns):
        if index < maximum-1:
            campaign_ids.append(tuple[0])

    return campaign_ids



