import streamlit as st
import pandas as pd
import requests
import urllib.parse
from pytz import timezone
import pytz
import pandas as pd
import time
from datetime import datetime

def get_product_info(url_key):
  headers = {
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'x-operation-name': 'GetProduct',
    'accept-language': 'en-US',
    'App-Platform': 'Iron',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjVjMGZlMGZkLWMwNTEtMTFlNy1iZmIxLTEyODg3OGViYjhiNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImh0dHBzOi8vc3RvY2t4LmNvbS9lbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5zdG9ja3guY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3MDQ4MjgyNDA5OTg0ODIzMjAyIiwiYXVkIjpbImdhdGV3YXkuc3RvY2t4LmNvbSIsImh0dHBzOi8vc3RvY2t4LXByb2Quc3RvY2t4LXByb2QuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMzI4OTk0NCwiZXhwIjoxNzEzMzMzMTQ0LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIiwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQifQ.axOMkt3C3Vd2tFDAQfqnxiKC-ecWc1sENEHQIUpvDCqlx5P8-HbH0mQvATYBIaHVafZw8DGhlIPvHAPjjwk9pEzbxbWXC-0ILS5SQbT8IISkjSb1clyLjZIovZfrtkVPPn3OaINI4zr4TWcQhpeAk8xfeYkL9egmF1H9_etO8QBus0tGFIB_6kZPW6Koy9_AFMKWN_hAnRuXG0yZjbfnMUytBpZGCvM3CgL-4epGCXIHsgta8uMo44Hfv3BT58LM9x7Y7dQ6IPZpKLVxZ7bkTfYBORlV5xfVXxtyycKc5az84kZiZ5pGsp5wfpw4qXVCkJ0CMX8y9znZnfk5beJdrA',
    'selected-country': 'US',
    'x-stockx-session-id': '8588b3ed-d944-4d24-a16a-92a7af3ba93b',
    'sec-ch-ua-platform': '"macOS"',
    'apollographql-client-name': 'Iron',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Referer': 'https://stockx.com/air-jordan-1-retro-low-golf-chicago?size=11.5',
    'x-stockx-device-id': '908b36ce-4320-48a8-bfc9-384c6846a26d',
    'apollographql-client-version': '2024.04.07.01',
    'App-Version': '2024.04.07.01',
}

  json_data = {
      'query': 'query GetProduct($id: String!, $currencyCode: CurrencyCode, $countryCode: String!, $marketName: String, $skipMerchandising: Boolean!) {\n  product(id: $id) {\n    id\n    listingType\n    deleted\n    gender\n    browseVerticals\n    ...ProductMerchandisingFragment\n    ...BreadcrumbsFragment\n    ...BreadcrumbSchemaFragment\n    ...HazmatWarningFragment\n    ...HeaderFragment\n    ...NFTHeaderFragment\n    ...MarketActivityFragment\n    ...MediaFragment\n    ...MyPositionFragment\n    ...ProductDetailsFragment\n    ...ProductMetaTagsFragment\n    ...ProductSchemaFragment\n    ...ScreenTrackerFragment\n    ...SizeSelectorWrapperFragment\n    ...StatsForNerdsFragment\n    ...ThreeSixtyImageFragment\n    ...TrackingFragment\n    ...UtilityGroupFragment\n    ...FavoriteProductFragment\n  }\n}\n\nfragment ProductMerchandisingFragment on Product {\n  id\n  merchandising @skip(if: $skipMerchandising) {\n    title\n    subtitle\n    image {\n      alt\n      url\n    }\n    body\n    trackingEvent\n    link {\n      title\n      url\n      urlType\n    }\n  }\n}\n\nfragment BreadcrumbsFragment on Product {\n  breadcrumbs {\n    name\n    url\n    level\n  }\n}\n\nfragment BreadcrumbSchemaFragment on Product {\n  breadcrumbs {\n    name\n    url\n  }\n}\n\nfragment HazmatWarningFragment on Product {\n  id\n  hazardousMaterial {\n    lithiumIonBucket\n  }\n}\n\nfragment HeaderFragment on Product {\n  primaryTitle\n  secondaryTitle\n  condition\n  productCategory\n}\n\nfragment NFTHeaderFragment on Product {\n  primaryTitle\n  secondaryTitle\n  productCategory\n  editionType\n}\n\nfragment MarketActivityFragment on Product {\n  id\n  title\n  productCategory\n  primaryTitle\n  secondaryTitle\n  media {\n    smallImageUrl\n  }\n}\n\nfragment MediaFragment on Product {\n  id\n  productCategory\n  title\n  brand\n  urlKey\n  variants {\n    id\n    hidden\n    traits {\n      size\n    }\n  }\n  media {\n    gallery\n    imageUrl\n    videos {\n      video {\n        url\n        alt\n      }\n      thumbnail {\n        url\n        alt\n      }\n    }\n  }\n}\n\nfragment MyPositionFragment on Product {\n  id\n  urlKey\n}\n\nfragment ProductDetailsFragment on Product {\n  id\n  title\n  productCategory\n  contentGroup\n  browseVerticals\n  description\n  gender\n  traits {\n    name\n    value\n    visible\n    format\n  }\n}\n\nfragment ProductMetaTagsFragment on Product {\n  id\n  urlKey\n  productCategory\n  brand\n  model\n  title\n  description\n  condition\n  styleId\n  breadcrumbs {\n    name\n    url\n  }\n  traits {\n    name\n    value\n  }\n  media {\n    thumbUrl\n    imageUrl\n  }\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      lowestAsk {\n        amount\n      }\n      numberOfAsks\n    }\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n    }\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        lowestAsk {\n          amount\n        }\n      }\n    }\n  }\n  seo {\n    meta {\n      name\n      value\n    }\n  }\n}\n\nfragment ProductSchemaFragment on Product {\n  id\n  urlKey\n  productCategory\n  brand\n  model\n  title\n  description\n  condition\n  styleId\n  traits {\n    name\n    value\n  }\n  media {\n    thumbUrl\n    imageUrl\n  }\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      lowestAsk {\n        amount\n      }\n      numberOfAsks\n    }\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n    }\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        lowestAsk {\n          amount\n        }\n      }\n    }\n    gtins {\n      type\n      identifier\n    }\n  }\n}\n\nfragment ScreenTrackerFragment on Product {\n  id\n  brand\n  productCategory\n  primaryCategory\n  title\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      highestBid {\n        amount\n      }\n      lowestAsk {\n        amount\n      }\n      numberOfAsks\n      numberOfBids\n    }\n    salesInformation {\n      lastSale\n    }\n  }\n  media {\n    imageUrl\n  }\n  traits {\n    name\n    value\n  }\n  variants {\n    id\n    traits {\n      size\n    }\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        highestBid {\n          amount\n        }\n        lowestAsk {\n          amount\n        }\n        numberOfAsks\n        numberOfBids\n      }\n      salesInformation {\n        lastSale\n      }\n    }\n  }\n  tags\n}\n\nfragment SizeSelectorWrapperFragment on Product {\n  id\n  ...SizeSelectorFragment\n  ...SizeSelectorHeaderFragment\n  ...SizesFragment\n  ...SizesOptionsFragment\n  ...SizeChartFragment\n  ...SizeChartContentFragment\n  ...SizeConversionFragment\n  ...SizesAllButtonFragment\n}\n\nfragment SizeSelectorFragment on Product {\n  id\n  title\n  productCategory\n  browseVerticals\n  sizeDescriptor\n  availableSizeConversions {\n    name\n    type\n  }\n  defaultSizeConversion {\n    name\n    type\n  }\n  variants {\n    id\n    hidden\n    traits {\n      size\n    }\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n      }\n    }\n  }\n}\n\nfragment SizeSelectorHeaderFragment on Product {\n  sizeDescriptor\n  productCategory\n  availableSizeConversions {\n    name\n    type\n  }\n}\n\nfragment SizesFragment on Product {\n  id\n  productCategory\n  listingType\n  title\n}\n\nfragment SizesOptionsFragment on Product {\n  id\n  listingType\n  variants {\n    id\n    hidden\n    group {\n      shortCode\n    }\n    traits {\n      size\n    }\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n      }\n    }\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        numberOfCustodialAsks\n        lowestCustodialAsk {\n          amount\n        }\n        lowestAsk {\n          amount\n        }\n      }\n    }\n  }\n}\n\nfragment SizeChartFragment on Product {\n  availableSizeConversions {\n    name\n    type\n  }\n  defaultSizeConversion {\n    name\n    type\n  }\n}\n\nfragment SizeChartContentFragment on Product {\n  availableSizeConversions {\n    name\n    type\n  }\n  defaultSizeConversion {\n    name\n    type\n  }\n  variants {\n    id\n    sizeChart {\n      baseSize\n      baseType\n      displayOptions {\n        size\n        type\n      }\n    }\n  }\n}\n\nfragment SizeConversionFragment on Product {\n  productCategory\n  browseVerticals\n  sizeDescriptor\n  availableSizeConversions {\n    name\n    type\n  }\n  defaultSizeConversion {\n    name\n    type\n  }\n}\n\nfragment SizesAllButtonFragment on Product {\n  id\n  sizeAllDescriptor\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      lowestAsk {\n        amount\n      }\n      numberOfCustodialAsks\n      lowestCustodialAsk {\n        amount\n      }\n    }\n  }\n}\n\nfragment StatsForNerdsFragment on Product {\n  id\n  title\n  productCategory\n  sizeDescriptor\n  urlKey\n}\n\nfragment ThreeSixtyImageFragment on Product {\n  id\n  title\n  variants {\n    id\n  }\n  productCategory\n  media {\n    all360Images\n  }\n}\n\nfragment TrackingFragment on Product {\n  id\n  productCategory\n  primaryCategory\n  brand\n  title\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      highestBid {\n        amount\n      }\n      lowestAsk {\n        amount\n      }\n    }\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        highestBid {\n          amount\n        }\n        lowestAsk {\n          amount\n        }\n      }\n    }\n  }\n}\n\nfragment UtilityGroupFragment on Product {\n  id\n  ...PortfolioFragment\n  ...PortfolioContentFragment\n  ...ShareFragment\n}\n\nfragment PortfolioFragment on Product {\n  id\n  title\n  productCategory\n  variants {\n    id\n  }\n  traits {\n    name\n    value\n  }\n}\n\nfragment PortfolioContentFragment on Product {\n  id\n  productCategory\n  sizeDescriptor\n  variants {\n    id\n    traits {\n      size\n    }\n  }\n}\n\nfragment ShareFragment on Product {\n  id\n  productCategory\n  title\n  media {\n    imageUrl\n  }\n}\n\nfragment FavoriteProductFragment on Product {\n  favorite\n}',
      'variables': {
          'id': url_key,
          'currencyCode': 'USD',
          'countryCode': 'US',
          'marketName': 'US',
          'skipMerchandising': False,
      },
      'operationName': 'GetProduct',
  }

  product_variant = []

  response = requests.post('https://stockx.com/api/p/e', headers=headers, json=json_data).json()
  st.write(response)
  title = response['data']['product']['title']
  image_url = response['data']['product']['media']['imageUrl']
  brand = response['data']['product']['brand']
  retail_price = 0

  for i in response['data']['product']['traits']:
    if i['name'] == 'Retail Price':
      retail_price = i['value']


  for variant in response['data']['product']['variants']:
    # only include variants that are not hidden
    if variant['hidden'] == False:
      product_variant.append({
          'url_key': url_key,
          'brand': brand,
          'title': title,
          'msrp': retail_price,
          'variant_id': variant['id'],
          'size': variant['traits']['size'],
          'department': variant['sizeChart']['baseType'],
          'img_url': image_url
          })

  product_variant_df = pd.DataFrame(product_variant, columns = ['title', 'msrp', 'img_url', 'brand', 'variant_id', 'department', 'size'])

  return product_variant_df

def get_search_results(variant):
  headers = {
    'accept': 'application/json',
    'accept-language': 'en-US',
    'apollographql-client-name': 'Iron',
    'apollographql-client-version': '2024.04.07.01',
    'app-platform': 'Iron',
    'app-version': '2024.04.07.01',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjVjMGZlMGZkLWMwNTEtMTFlNy1iZmIxLTEyODg3OGViYjhiNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImh0dHBzOi8vc3RvY2t4LmNvbS9lbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5zdG9ja3guY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3MDQ4MjgyNDA5OTg0ODIzMjAyIiwiYXVkIjpbImdhdGV3YXkuc3RvY2t4LmNvbSIsImh0dHBzOi8vc3RvY2t4LXByb2Quc3RvY2t4LXByb2QuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMzI4OTk0NCwiZXhwIjoxNzEzMzMzMTQ0LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIiwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQifQ.axOMkt3C3Vd2tFDAQfqnxiKC-ecWc1sENEHQIUpvDCqlx5P8-HbH0mQvATYBIaHVafZw8DGhlIPvHAPjjwk9pEzbxbWXC-0ILS5SQbT8IISkjSb1clyLjZIovZfrtkVPPn3OaINI4zr4TWcQhpeAk8xfeYkL9egmF1H9_etO8QBus0tGFIB_6kZPW6Koy9_AFMKWN_hAnRuXG0yZjbfnMUytBpZGCvM3CgL-4epGCXIHsgta8uMo44Hfv3BT58LM9x7Y7dQ6IPZpKLVxZ7bkTfYBORlV5xfVXxtyycKc5az84kZiZ5pGsp5wfpw4qXVCkJ0CMX8y9znZnfk5beJdrA',
    'content-type': 'application/json',
    # 'cookie': 'stockx_device_id=908b36ce-4320-48a8-bfc9-384c6846a26d; language_code=en; _pxvid=8b02e142-f6bf-11ee-bf69-ca6d3c3f6c15; chakra-ui-color-mode=light; __pxvid=8b12e6e2-f6bf-11ee-844a-0242ac120002; _gcl_au=1.1.1649690169.1712701303; ajs_anonymous_id=52397773-6c6a-4e79-8eaf-20d78921e78c; _fbp=fb.1.1712701303384.1444115676; rbuid=rbos-2bf778d6-492b-41d7-ae81-c88f5990dc7b; __ssid=40fb064f7f301822f23fd1adc49e2e7; rskxRunCookie=0; rCookie=64cfg7l50mt0ho8ewpnb4crlusy4w41; QuantumMetricUserID=7d8c619f24607b997acc4721ebb8f89b; __pdst=c919d3d576b047b19b9f5ecf0afaef56; ftr_ncd=6; ajs_user_id=5c0fe0fd-c051-11e7-bfb1-128878ebb8b6; forterToken=3383a42e990c4e2292436a87926dffbe_1712957690154_161_UDF43-m4_13ck; _gid=GA1.2.1895683782.1713202804; stockx_session_id=8588b3ed-d944-4d24-a16a-92a7af3ba93b; stockx_session=60124767-c215-4a69-bde0-dd679eef944e; stockx_selected_region=US; display_location_selector=false; cf_clearance=H5dryMyTfBpK02inovMC6HmVnZqqzCzrFA8m7YbW1sQ-1713289073-1.0.1.1-B4.uRWdjfITaXwr4a_oDFEaE3mr.yFJtBHO2lAPGYrH5UqKg6BM_sLf2KAjLRAGzrXz0u8Mro9cJrqf0Wq83Uw; pxcts=126d3ae2-fc18-11ee-b919-6a9724a4bb00; stockx_message_last_seen_inbox=2024-04-12T14%3A24%3A16.223Z; QuantumMetricSessionID=e307327d0e8613e8470b4c9837f876c6; token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjVjMGZlMGZkLWMwNTEtMTFlNy1iZmIxLTEyODg3OGViYjhiNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImh0dHBzOi8vc3RvY2t4LmNvbS9lbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5zdG9ja3guY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3MDQ4MjgyNDA5OTg0ODIzMjAyIiwiYXVkIjpbImdhdGV3YXkuc3RvY2t4LmNvbSIsImh0dHBzOi8vc3RvY2t4LXByb2Quc3RvY2t4LXByb2QuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMzI4OTk0NCwiZXhwIjoxNzEzMzMzMTQ0LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIiwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQifQ.axOMkt3C3Vd2tFDAQfqnxiKC-ecWc1sENEHQIUpvDCqlx5P8-HbH0mQvATYBIaHVafZw8DGhlIPvHAPjjwk9pEzbxbWXC-0ILS5SQbT8IISkjSb1clyLjZIovZfrtkVPPn3OaINI4zr4TWcQhpeAk8xfeYkL9egmF1H9_etO8QBus0tGFIB_6kZPW6Koy9_AFMKWN_hAnRuXG0yZjbfnMUytBpZGCvM3CgL-4epGCXIHsgta8uMo44Hfv3BT58LM9x7Y7dQ6IPZpKLVxZ7bkTfYBORlV5xfVXxtyycKc5az84kZiZ5pGsp5wfpw4qXVCkJ0CMX8y9znZnfk5beJdrA; stockx_preferred_market_activity=sales; maId={"cid":"f869bcf54e34be13645cd09938ea446a","sid":"6f55a6c9-2e18-4c8a-9326-d8b9cd9cfe44","isSidSaved":true,"sessionStart":"2024-04-16T17:52:30.000Z"}; loggedIn=5c0fe0fd-c051-11e7-bfb1-128878ebb8b6; stockx_selected_currency=USD; is_gdpr=false; stockx_ip_region=US; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Apr+16+2024+11%3A04%3A02+GMT-0700+(Pacific+Daylight+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=7da7631c-94df-437a-b7b0-af261a03ff49&interactionCount=1&landingPath=NotLandingPage&groups=BG84%3A1%2CC0004%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false; _ga=GA1.1.711997752.1712701303; lastRskxRun=1713290737939; stockx_product_visits=60; stockx_homepage=sneakers; _tq_id.TV-5490813681-1.1a3e=4120c17ef0c9e2aa.1712701308.0.1713290742..; _uetsid=31adf160fb4f11ee948113a1e3434e7c|1f54bn1|2|fkz|0|1566; _uetvid=8b701c60f6bf11ee8f29d3c3cf72be57|bkew2g|1713292184837|23|1|bat.bing.com/p/insights/c/f; _gat=1; _ga_TYYSNQDG4W=GS1.1.1713289081.15.1.1713292187.0.0.0; __cf_bm=9BCDNyRYWJ0e2iqpzIY9eEgAnjqhV6Vlu1GR2yXWiGY-1713292187-1.0.1.1-fbpKZBilcO.uU5gFwwpLEC97RmHXCnGR4w4.Z56r6GIbHM3grcS3q3XH5g7tHsVYK1SJ7kGtsJsPc258Ls6NXQ; _dd_s=rum=0&expire=1713293104561&logs=1&id=f2b24e6d-b775-4124-bd2e-5f24a4c550d7&created=1713289073484',
    'origin': 'https://stockx.com',
    'referer': 'https://stockx.com/air-jordan-1-mid-true-blue-cement-gs?size=5.5Y',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'selected-country': 'US',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-operation-name': 'GetSearchResults',
    'x-stockx-device-id': '908b36ce-4320-48a8-bfc9-384c6846a26d',
    'x-stockx-session-id': '8588b3ed-d944-4d24-a16a-92a7af3ba93b',
    }

  json_data = {
      'query': 'query GetSearchResults($countryCode: String!, $currencyCode: CurrencyCode!, $filtersVersion: Int, $page: BrowsePageInput, $query: String!, $sort: BrowseSortInput, $staticRanking: BrowseExperimentStaticRankingInput, $list: String, $skipVariants: Boolean!, $marketName: String) {\n  browse(\n    query: $query\n    page: $page\n    sort: $sort\n    filtersVersion: $filtersVersion\n    experiments: {staticRanking: $staticRanking}\n  ) {\n    categories {\n      id\n      name\n      count\n    }\n    results {\n      edges {\n        objectId\n        node {\n          ... on Product {\n            id\n            listingType\n            urlKey\n            primaryTitle\n            secondaryTitle\n            media {\n              thumbUrl\n            }\n            brand\n            productCategory\n            market(currencyCode: $currencyCode) {\n              state(country: $countryCode, market: $marketName) {\n                numberOfCustodialAsks\n                lowestCustodialAsk {\n                  amount\n                }\n              }\n            }\n            favorite(list: $list)\n            variants @skip(if: $skipVariants) {\n              id\n            }\n          }\n          ... on Variant {\n            id\n            product {\n              id\n              listingType\n              urlKey\n              primaryTitle\n              secondaryTitle\n              media {\n                thumbUrl\n              }\n              brand\n              productCategory\n            }\n            market(currencyCode: $currencyCode) {\n              state(country: $countryCode, market: $marketName) {\n                numberOfCustodialAsks\n                lowestCustodialAsk {\n                  amount\n                }\n              }\n            }\n          }\n        }\n      }\n      pageInfo {\n        limit\n        page\n        pageCount\n        queryId\n        queryIndex\n        total\n      }\n    }\n    sort {\n      id\n      order\n    }\n  }\n}',
      'variables': {
          'countryCode': 'US',
          'currencyCode': 'USD',
          'filtersVersion': 4,
          'query': urllib.parse.quote(variant),
          'sort': {
              'id': 'featured',
              'order': 'DESC',
          },
          'staticRanking': {
              'enabled': True,
          },
          'skipVariants': True,
          'marketName': None,
          'page': {
              'index': 1,
              'limit': 10,
          },
      },
      'operationName': 'GetSearchResults',
  }

  response = requests.post('https://stockx.com/api/p/e', headers=headers, json=json_data)
  st.write(response)
  url_key = response.json()['data']['browse']['results']['edges'][0]['node']['urlKey']
  return url_key


def get_market_data(url_key):
  headers = {
    'accept': 'application/json',
    'accept-language': 'en-US',
    'apollographql-client-name': 'Iron',
    'apollographql-client-version': '2024.04.07.01',
    'app-platform': 'Iron',
    'app-version': '2024.04.07.01',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjVjMGZlMGZkLWMwNTEtMTFlNy1iZmIxLTEyODg3OGViYjhiNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImh0dHBzOi8vc3RvY2t4LmNvbS9lbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5zdG9ja3guY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3MDQ4MjgyNDA5OTg0ODIzMjAyIiwiYXVkIjpbImdhdGV3YXkuc3RvY2t4LmNvbSIsImh0dHBzOi8vc3RvY2t4LXByb2Quc3RvY2t4LXByb2QuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMzI4OTk0NCwiZXhwIjoxNzEzMzMzMTQ0LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIiwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQifQ.axOMkt3C3Vd2tFDAQfqnxiKC-ecWc1sENEHQIUpvDCqlx5P8-HbH0mQvATYBIaHVafZw8DGhlIPvHAPjjwk9pEzbxbWXC-0ILS5SQbT8IISkjSb1clyLjZIovZfrtkVPPn3OaINI4zr4TWcQhpeAk8xfeYkL9egmF1H9_etO8QBus0tGFIB_6kZPW6Koy9_AFMKWN_hAnRuXG0yZjbfnMUytBpZGCvM3CgL-4epGCXIHsgta8uMo44Hfv3BT58LM9x7Y7dQ6IPZpKLVxZ7bkTfYBORlV5xfVXxtyycKc5az84kZiZ5pGsp5wfpw4qXVCkJ0CMX8y9znZnfk5beJdrA',
    'content-type': 'application/json',
    # 'cookie': 'stockx_device_id=908b36ce-4320-48a8-bfc9-384c6846a26d; language_code=en; _pxvid=8b02e142-f6bf-11ee-bf69-ca6d3c3f6c15; chakra-ui-color-mode=light; __pxvid=8b12e6e2-f6bf-11ee-844a-0242ac120002; _gcl_au=1.1.1649690169.1712701303; ajs_anonymous_id=52397773-6c6a-4e79-8eaf-20d78921e78c; _fbp=fb.1.1712701303384.1444115676; rbuid=rbos-2bf778d6-492b-41d7-ae81-c88f5990dc7b; __ssid=40fb064f7f301822f23fd1adc49e2e7; rskxRunCookie=0; rCookie=64cfg7l50mt0ho8ewpnb4crlusy4w41; QuantumMetricUserID=7d8c619f24607b997acc4721ebb8f89b; __pdst=c919d3d576b047b19b9f5ecf0afaef56; ftr_ncd=6; ajs_user_id=5c0fe0fd-c051-11e7-bfb1-128878ebb8b6; forterToken=3383a42e990c4e2292436a87926dffbe_1712957690154_161_UDF43-m4_13ck; _gid=GA1.2.1895683782.1713202804; stockx_homepage=sneakers; _tq_id.TV-5490813681-1.1a3e=4120c17ef0c9e2aa.1712701308.0.1713246688..; stockx_session_id=8588b3ed-d944-4d24-a16a-92a7af3ba93b; stockx_session=60124767-c215-4a69-bde0-dd679eef944e; stockx_selected_region=US; __cf_bm=J0EYofDGp7urO_zGFTj7YclMfS04HWLgNDg1xE7GMLg-1713289073-1.0.1.1-S1C8ha7NZ2Ukgts3WQHLtTY2VaJ8Lxqj0LOBu8s6c5Jf28.3ngHFsEzqujZ17Y_CoU0378xCwJkiZSkuhTB63A; display_location_selector=false; cf_clearance=H5dryMyTfBpK02inovMC6HmVnZqqzCzrFA8m7YbW1sQ-1713289073-1.0.1.1-B4.uRWdjfITaXwr4a_oDFEaE3mr.yFJtBHO2lAPGYrH5UqKg6BM_sLf2KAjLRAGzrXz0u8Mro9cJrqf0Wq83Uw; pxcts=126d3ae2-fc18-11ee-b919-6a9724a4bb00; stockx_message_last_seen_inbox=2024-04-12T14%3A24%3A16.223Z; _gat=1; _com.auth0.auth.%7B%7D_compat={%22nonce%22:null%2C%22state%22:%22{}%22%2C%22lastUsedConnection%22:%22%22}; com.auth0.auth.%7B%7D={%22nonce%22:null%2C%22state%22:%22{}%22%2C%22lastUsedConnection%22:%22%22}; QuantumMetricSessionID=e307327d0e8613e8470b4c9837f876c6; token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjVjMGZlMGZkLWMwNTEtMTFlNy1iZmIxLTEyODg3OGViYjhiNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImh0dHBzOi8vc3RvY2t4LmNvbS9lbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5zdG9ja3guY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3MDQ4MjgyNDA5OTg0ODIzMjAyIiwiYXVkIjpbImdhdGV3YXkuc3RvY2t4LmNvbSIsImh0dHBzOi8vc3RvY2t4LXByb2Quc3RvY2t4LXByb2QuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMzI4OTk0NCwiZXhwIjoxNzEzMzMzMTQ0LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIiwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQifQ.axOMkt3C3Vd2tFDAQfqnxiKC-ecWc1sENEHQIUpvDCqlx5P8-HbH0mQvATYBIaHVafZw8DGhlIPvHAPjjwk9pEzbxbWXC-0ILS5SQbT8IISkjSb1clyLjZIovZfrtkVPPn3OaINI4zr4TWcQhpeAk8xfeYkL9egmF1H9_etO8QBus0tGFIB_6kZPW6Koy9_AFMKWN_hAnRuXG0yZjbfnMUytBpZGCvM3CgL-4epGCXIHsgta8uMo44Hfv3BT58LM9x7Y7dQ6IPZpKLVxZ7bkTfYBORlV5xfVXxtyycKc5az84kZiZ5pGsp5wfpw4qXVCkJ0CMX8y9znZnfk5beJdrA; _ga_TYYSNQDG4W=GS1.1.1713289081.15.1.1713289945.0.0.0; lastRskxRun=1713289945660; _px3=4b867c91f419d1f7b32e03823dddc03cfa70189ec73ae02cbfa8cfcd29f33dea:8nqjj2ew3sSzH7OPnBS2x9Ckb8TN4ZLPA5JiLkJ9pVbkppa86lcRgl7/7zaHIGf94OwiHVXzKo0hIEVEDLJFpw==:1000:dyZbi+vP3IJNIeUyC+E2X8xMszdGIcbBSQOUMVZkEhFJy195eBtA3GUwkN8HJCekyCsi8WZRoDq87gadt8iUGqZkwIH70kwkibxZTyDnv1dyBZ5/zFAydgGi/6vXwIfXH6TmTeoald9P0CqekQtmGSfzIiRBLG0gvht8muPmv2xh9OfC9/yTqevk5LHeRBR/QwU0/ESMqZIOv3wn512T7EFkDtnY9yfQfIP1U1ow69E=; _uetsid=31adf160fb4f11ee948113a1e3434e7c|1f54bn1|2|fkz|0|1566; _uetvid=8b701c60f6bf11ee8f29d3c3cf72be57|bkew2g|1713289945865|4|1|bat.bing.com/p/insights/c/f; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Apr+16+2024+10%3A52%3A27+GMT-0700+(Pacific+Daylight+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=7da7631c-94df-437a-b7b0-af261a03ff49&interactionCount=1&landingPath=NotLandingPage&groups=BG84%3A1%2CC0004%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false; stockx_preferred_market_activity=sales; stockx_product_visits=52; loggedIn=5c0fe0fd-c051-11e7-bfb1-128878ebb8b6; stockx_selected_currency=USD; is_gdpr=false; stockx_ip_region=US; _dd_s=rum=0&expire=1713290847691&logs=1&id=f2b24e6d-b775-4124-bd2e-5f24a4c550d7&created=1713289073484; _ga=GA1.2.711997752.1712701303; _pxde=83b043ffbe003e0ad06b69075b0fcf5617648012646863c92d4ee55919b86478:eyJ0aW1lc3RhbXAiOjE3MTMyODk5NDc5MDcsImZfa2IiOjB9',
    'origin': 'https://stockx.com',
    'referer': 'https://stockx.com/air-jordan-4-retro-military-blue-2024',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'selected-country': 'US',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-operation-name': 'GetMarketData',
    'x-stockx-device-id': '908b36ce-4320-48a8-bfc9-384c6846a26d',
    'x-stockx-session-id': '8588b3ed-d944-4d24-a16a-92a7af3ba93b',
  }

  json_data = {
      'query': 'query GetMarketData($id: String!, $currencyCode: CurrencyCode, $countryCode: String!, $marketName: String) {\n  product(id: $id) {\n    id\n    urlKey\n    listingType\n    title\n    uuid\n    contentGroup\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        lowestAsk {\n          amount\n        }\n        highestBid {\n          amount\n        }\n        numberOfCustodialAsks\n        numberOfAsks\n        numberOfBids\n        lowestCustodialAsk {\n          amount\n        }\n      }\n      salesInformation {\n        lastSale\n        salesLast72Hours\n      }\n    }\n    variants {\n      id\n      market(currencyCode: $currencyCode) {\n        state(country: $countryCode, market: $marketName) {\n          lowestAsk {\n            amount\n          }\n          highestBid {\n            amount\n          }\n          numberOfCustodialAsks\n          numberOfAsks\n          numberOfBids\n          lowestCustodialAsk {\n            amount\n          }\n        }\n        salesInformation {\n          lastSale\n          salesLast72Hours\n        }\n      }\n    }\n    ...BidButtonFragment\n    ...BidButtonContentFragment\n    ...BuySellFragment\n    ...BuySellContentFragment\n    ...XpressAskPDPFragment\n    ...LastSaleFragment\n  }\n}\n\nfragment BidButtonFragment on Product {\n  id\n  title\n  urlKey\n  sizeDescriptor\n  productCategory\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      highestBid {\n        amount\n      }\n      lowestAsk {\n        amount\n      }\n    }\n  }\n  media {\n    imageUrl\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        highestBid {\n          amount\n        }\n        lowestAsk {\n          amount\n        }\n      }\n    }\n  }\n}\n\nfragment BidButtonContentFragment on Product {\n  id\n  urlKey\n  sizeDescriptor\n  productCategory\n  lockBuying\n  lockSelling\n  minimumBid(currencyCode: $currencyCode)\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      highestBid {\n        amount\n      }\n      lowestAsk {\n        amount\n      }\n      numberOfAsks\n    }\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        highestBid {\n          amount\n        }\n        lowestAsk {\n          amount\n        }\n        numberOfAsks\n      }\n    }\n  }\n}\n\nfragment BuySellFragment on Product {\n  id\n  title\n  urlKey\n  sizeDescriptor\n  productCategory\n  lockBuying\n  lockSelling\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      highestBid {\n        amount\n      }\n      lowestAsk {\n        amount\n      }\n    }\n  }\n  media {\n    imageUrl\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        highestBid {\n          amount\n        }\n        lowestAsk {\n          amount\n        }\n      }\n    }\n  }\n}\n\nfragment BuySellContentFragment on Product {\n  id\n  urlKey\n  sizeDescriptor\n  productCategory\n  lockBuying\n  lockSelling\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      highestBid {\n        amount\n      }\n      lowestAsk {\n        amount\n      }\n    }\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        highestBid {\n          amount\n        }\n        lowestAsk {\n          amount\n        }\n      }\n    }\n  }\n}\n\nfragment XpressAskPDPFragment on Product {\n  market(currencyCode: $currencyCode) {\n    state(country: $countryCode, market: $marketName) {\n      numberOfAsks\n      numberOfBids\n      numberOfCustodialAsks\n      lowestCustodialAsk {\n        amount\n      }\n    }\n  }\n  variants {\n    market(currencyCode: $currencyCode) {\n      state(country: $countryCode, market: $marketName) {\n        numberOfAsks\n        numberOfBids\n        numberOfCustodialAsks\n        lowestCustodialAsk {\n          amount\n        }\n      }\n    }\n  }\n}\n\nfragment LastSaleFragment on Product {\n  id\n  market(currencyCode: $currencyCode) {\n    statistics(market: $marketName) {\n      ...LastSaleMarketStatistics\n    }\n  }\n  variants {\n    id\n    market(currencyCode: $currencyCode) {\n      statistics(market: $marketName) {\n        ...LastSaleMarketStatistics\n      }\n    }\n  }\n}\n\nfragment LastSaleMarketStatistics on MarketStatistics {\n  lastSale {\n    amount\n    changePercentage\n    changeValue\n    sameFees\n  }\n}',
      'variables': {
          'id': url_key,
          'currencyCode': 'USD',
          'countryCode': 'US',
          'marketName': None,
      },
      'operationName': 'GetMarketData',
  }

  # get sales data
  response = requests.post('https://stockx.com/api/p/e', headers=headers, json=json_data).json()
  st.write(response)
  market_sales = []
  # parse variants for item
  for variant in response['data']['product']['variants']:
    lowest_ask = ''
    highest_bid = ''

    if variant['market']['state']['lowestAsk'] is not None:
      lowest_ask = variant['market']['state']['lowestAsk']['amount']

    if variant['market']['state']['highestBid'] is not None:
      highest_bid = variant['market']['state']['highestBid']['amount']

    market_sales.append({
        'url': f'https://stockx.com/{url_key}',
        'variant_id': variant['id'],
        'lowest_ask': lowest_ask,
        'highest_bid': highest_bid,
        'number_of_asks': variant['market']['state']['numberOfAsks'],
        'number_of_bids': variant['market']['state']['numberOfBids'],
        'last_sales': variant['market']['salesInformation']['lastSale'],
        'last_sales_72_hrs': variant['market']['salesInformation']['salesLast72Hours']
    })

  market_sales_df = pd.DataFrame(
              market_sales,
              columns = ['url', 'variant_id', 'lowest_ask', 'highest_bid',
                         'number_of_asks', 'number_of_bids', 'last_sales',
                         'last_sales_72_hrs'])
  return market_sales_df



def get_stockx_data(variant):
  # get scraped time
  date = datetime.now(tz=pytz.utc)
  date = date.astimezone(timezone('US/Pacific'))
  # get the search URL term for the variant
  url_key = get_search_results(variant)
  #sleep for 1.5 seconds before making another request
  time.sleep(1.5)
  # get the sales info
  sales_df = get_market_data(url_key)
  #sleep for 2 seconds before making another request
  time.sleep(2)
  # # get product variant mapping
  product_df = get_product_info(url_key)

  output_df = sales_df.merge(product_df, how='inner', on='variant_id').fillna(0)
  output_df['sku'] = variant
  output_df['scraped_timestamp'] = date
  output_df = output_df[['sku', 'img_url', 'title', 'url',  'brand',
                         'size', 'department', 'lowest_ask', 'highest_bid',
                         'last_sales', 'last_sales_72_hrs', 'number_of_asks',
                         'highest_bid', 'scraped_timestamp']]
  return output_df


st.title('🔌⚡️👻')

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
    # get_stockx_data('AQ9129-170')
sku = st.text_input('SKU to search! 🔍')
if sku is not None or sku != '':
  get_stockx_data('AQ9129-170')