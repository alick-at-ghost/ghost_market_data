from base64 import b64decode
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time
from datetime import datetime
from pytz import timezone    
import streamlit as st

def get_stockx_product_metadata(variant):
  api_response = requests.post(
      "https://api.zyte.com/v1/extract",
      auth=("338d2fb7537b4a599ca73a8dbf431211", ""),
      json={
          "url": f"https://stockx.com/search?s={variant}",
          "httpResponseBody": True,
      },
  )
  http_response_body: bytes = b64decode(
      api_response.json()["httpResponseBody"])

  soup = BeautifulSoup(http_response_body)
  url_key = soup.find("a", {"data-testid": "productTile-ProductSwitcherLink"})['href']
  title = soup.find("p", {"data-testid": "product-tile-title"}).getText()
  return url_key, title


# given a URL key and title, get the relevant stockX data.
def get_stockx_pricing(url_key, title):
  sales_data = requests.post(
      "https://api.zyte.com/v1/extract",
      auth=("338d2fb7537b4a599ca73a8dbf431211", ""),
      json={
          "url": f"https://stockx.com{url_key}",
          "httpResponseBody": True,
      },
  )
  http_response_body: bytes = b64decode(
      sales_data.json()["httpResponseBody"])

  soup = BeautifulSoup(http_response_body)
  output_json = json.loads(soup.find('script', type="application/json").text)
  # get product variants
  # print(output_json)
  product_variants = output_json['props']['pageProps']['req']['appContext']['states']["query"]['value']['queries'][3]['state']['data']['product']['variants']
  image_url = output_json['props']['pageProps']['req']['appContext']['states']['query']['value']['queries'][-1]['state']['data']['product']['media']['imageUrl']
  output = []

  lowest_ask = 0
  highest_bid = 0

  for variant in product_variants:
    size = variant['traits']['size']

    if variant['market']['state']['lowestAsk'] is not None:
      lowest_ask = variant['market']['state']['lowestAsk']['amount']
    if variant['market']['state']['highestBid'] is not None:
      highest_bid = variant['market']['state']['highestBid']['amount']

    num_of_asks = variant['market']['state']['numberOfAsks']
    num_of_bids = variant['market']['state']['numberOfBids']
    last_sales = variant['market']['salesInformation']['lastSale']

    size_options = ''.join(str([i['size'].replace(' ','') for i in variant['sizeChart']['displayOptions']]))

    output.append({
        'size_options': size_options,
        'lowest_ask': lowest_ask,
        'highest_bid': highest_bid,
        'num_of_asks': num_of_asks,
        'num_of_bids': num_of_bids,
        'last_sales': last_sales
    })

  df = pd.DataFrame(output, columns=['size_options','lowest_ask', 'highest_bid', 'num_of_asks', 'num_of_bids', 'last_sales'])
  df['url'] = f'https://stockx.com{url_key}'
  df['title'] = title
  df['image_url'] = image_url
  return df


# Get stockx data from a variatn
def get_stockx_data(variant):
  # get url key + title name
  stockx_metadata = get_stockx_product_metadata(variant)

  # get StockX pricing
  stockx_pricing_df = get_stockx_pricing(url_key=stockx_metadata[0], title=stockx_metadata[1])
  stockx_pricing_df['variant'] = variant

  pacific_tz = timezone('US/Pacific')
  current_datetime = datetime.now(pacific_tz)
  stockx_pricing_df['stockX_data_as_of'] = current_datetime.strftime('%Y-%m-%d %H:%M:%S PST')
  return stockx_pricing_df



st.title('🔌⚡️👻')


st.subheader('Instructions')
st.markdown('''
    1. Upload CSV like format below
    2. Make sure you have SKU and Size column
    ''')


df = pd.DataFrame(
    {
        "SKU": ["AQ9129-170", "FB2213-200", "HQ6638"],
        "Size": ["US5W", "US10.5C", "US5Y"],
    }
)
st.dataframe(
    df,
    hide_index=True,
)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  # sort by SKU to ensure we're grouping same items together.
  input_csv = pd.read_csv(uploaded_file).sort_values('SKU')

  # get unique SKUs from CSV to avoid duplicate scrapes
  unique_skus = list(input_csv['SKU'].value_counts().index)

  num_of_skus = len(unique_skus)

  relevent_dfs = []
  # get sales data for relevant dataframes
  with st.status("Scraping stockX data...", expanded=True) as status:
    for idx,sku in enumerate(unique_skus):
      st.write(f'Scraping {sku}: {idx + 1} of {num_of_skus}')
      #append dataframe for SKUs we care about
      relevent_dfs.append(get_stockx_data(sku))
      time.sleep(0.5)
    status.update(label="Scraping complete!", state="complete", expanded=False)
  # output stockX dataframe
  stockx_df = pd.concat(relevent_dfs).reset_index(drop=True)


  output_final_df = []
  # get relevant rows for dataframe
  for i in input_csv.iloc[:].to_numpy():
    print(i)
    #filter df for variant
    filtered_sku_df = stockx_df[stockx_df['variant'].apply(lambda x: i[0] in x)]
    #filter df for size
    matched_df = filtered_sku_df[filtered_sku_df['size_options'].apply(lambda x: i[1] in x)]
    matched_df['size'] = i[1]
    output_final_df.append(matched_df)

  temp_df = pd.concat(output_final_df).reset_index(drop=True)
  final_ordered_df = temp_df[['variant', 'size', 'title', 'image_url', 'url', 'lowest_ask', 'highest_bid', 'num_of_asks', 'num_of_bids', 'last_sales', 'stockX_data_as_of']]
  final_ordered_df = pd.DataFrame(final_ordered_df, columns=['variant', 'size', 'title', 'image_url', 'url', 'lowest_ask', 'highest_bid', 'num_of_asks', 'num_of_bids', 'last_sales', 'stockX_data_as_of'])
  
  st.title('Matched StockX Data 🖇️')
  st.text('This CSV will contain rows that match the records you inputted.')
  st.dataframe(final_ordered_df, hide_index=True)
  
  all_df = stockx_df[['variant', 'size_options', 'title', 'image_url', 'url', 'lowest_ask', 'highest_bid', 'num_of_asks', 'num_of_bids', 'last_sales', 'stockX_data_as_of']]
  st.title('All StockX Data 📈')
  st.text('This CSV will contain full size run matched product data.')
  st.dataframe(all_df, hide_index=True)
