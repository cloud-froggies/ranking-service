from fastapi import FastAPI, Query
from typing import List
from typing import Optional
import random

app = FastAPI()


@app.get("/ranking")
def ranking(advertiser_campaigns: str, advertiser_campaigns_bids: str, maximum: Optional[int] = 10):
    # Split multiple values
    campaigns = [int(i) for i in advertiser_campaigns.split(",")]
    bids = [float(i) for i in advertiser_campaigns_bids.split(",")]

    # Shuffle tuples list in case of repeated bids
    shuffled = list(zip(campaigns, bids))
    random.shuffle(shuffled)

    # Sort according to bids
    sorted_advertiser_campaigns = sorted(shuffled, key=lambda x: x[1])
    
    # Keep only ids according to maximum 
    campaign_ids = []
    for index, tuple in enumerate(sorted_advertiser_campaigns):
        if index < maximum-1:
            campaign_ids.append(tuple[0])

    return campaign_ids



