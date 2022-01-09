## Helpers
import requests
import json

from config.settings import STRIPE_TOKEN


def authorization():
    header = {
        "Authorization": f"Bearer {STRIPE_TOKEN}",
        "Accept": "application/json",
    }

    return header


# Stripe API
def create_product(name, price, currency="usd") -> str:
    # connect to stripe
    endpoint = "https://api.stripe.com/v1/products"
    r = requests.post(
        url=endpoint,
        headers=authorization(),
        data={
            "name": name,
        },
    )
    if r.status_code != 200:
        return "ERROR"

    product_id = r.json()["id"]

    price_endpoint = "https://api.stripe.com/v1/prices"
    r = requests.post(
        url=price_endpoint,
        headers=authorization(),
        data={
            "currency": currency,
            "unit_amount": price,
            "product": product_id,
        },
    )

    if r.status_code != 200:
        # Delete product if creating the price failed
        requests.delete(
            url=f"https://api.stripe.com/v1/products/{product_id}",
            headers=authorization(),
        )
        return "Error creating product. Adding price failed."

    return r.json()
