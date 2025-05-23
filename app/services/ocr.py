import json

from openai import OpenAI

from app import config
from app.models.receipt import Receipt, Article

client = OpenAI(
    api_key=config.OpenaiSettings().OPENAI_API_KEY,
)

def get_prompt():
    return """
        The text is in French, correction should be done in French.
        Extract structured information from the following receipt text using this JSON format, return only the JSON:
        {
            "name": "",
            "date": "",
            "articles": [
                {
                    "name": "",
                    "quantity": 0,
                    "unit_price": 0.0,
                    "total_price": 0.0,
                }
            ],
            "total_price": 0.0
        }

        **Instructions:**
        
        - `name`: Store name if present. Skip otherwise.
        - `date`: Extract the purchase date and time in ISO 8601 format (e.g.,
        "2022-01-17T16:55:00").
        - Under `articles`, extract all purchased items with:
        
          - `name`: the item name. It may be incorrect, so correct it if necessary.
          - `quantity`: default to `1` if not specified.
          - `unit_price`: equal to `total_price` if not specified.
          - `total_price`: as shown.
        - `total_price`: total sum of all articles, as shown on the receipt. Make sure to fetch the total price, not the total
        of food, hygiene, etc. There may be multiple total prices, so choose the one that seems most relevant.
        - Convert all numeric fields to appropriate types: `quantity` as integer, prices as float.
        - Leave out any unrelated or non-item text (like totals, messages, VAT breakdowns, etc.).
        """

def extract_data_from_receipt(base64_image) -> Receipt:
    prompt = get_prompt()
    try:
        completion = client.responses.create(
            model="gpt-4.1",
            temperature=0.2,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": prompt
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpg;base64,{base64_image}"
                        }
                    ]
                },
            ]
        )
    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
    result = completion.output[0].content[0].text
    parsed_result = json.loads(result)
    articles = [Article(**article) for article in parsed_result["articles"]]
    receipt = Receipt(
        name=parsed_result["name"],
        date=parsed_result["date"],
        articles=articles,
        total_price=parsed_result["total_price"]
    )
    return receipt
