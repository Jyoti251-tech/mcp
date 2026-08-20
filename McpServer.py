from mcp.server.fastmcp import FastMCP
import dotenv
import os
import requests
dotenv.load_dotenv()
mcp=FastMCP("currencty_tool")

@mcp.tool()
def convert_currency(
    from_currency:str,
    to_currency:str,
    amount:float
)-> str:
    """convert an amount between two currency, from INR to USD"""


    key = os.getenv("EXCHANGE_RATE_API_KEY")
    if not key:
        raise RuntimeError
    ("EXCHANE_RATE_API_KEY is not set .. create a "" env file thee to set a key ")

    url = ""
    data = requests.get(url).json()
    rate = data ["conversion_rate"].get(to_currency)

    if not rate :
       return f"Unkwon currency:{to_currency}"
    return f"{amount} {from_currency} = {amount*rate:.2f}{to_currency}"

if __name__=="__main__":
   mcp.run(transport="sse")
   