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
      'accept': 'application/json',
      'accept-language': 'en-US',
      'apollographql-client-name': 'Iron',
      'apollographql-client-version': '2024.04.07.01',
      'app-platform': 'Iron',
      'app-version': '2024.04.07.01',
      'content-type': 'application/json',
      'cookie': "stockx_device_id=3aeca24a-cd31-4247-aefa-9a8f7def424a; language_code=en; stockx_selected_region=US; display_location_selector=false; pxcts=9fc19cbe-9492-11ee-9877-7bb915045ef5; _pxvid=9fc18fc3-9492-11ee-9877-cc96b6d9de68; __pxvid=9fdde741-9492-11ee-a11a-0242ac120004; _gcl_au=1.1.634647357.1701906797; ajs_user_id=9446d072-0baf-11ee-8a06-12f12be0eb51; ajs_anonymous_id=5610aa88-956b-4707-b2ff-a0d045d1ef7a; rbuid=rbos-02a7aa0f-e9f7-4546-9ed9-06eca955d094; _pin_unauth=dWlkPU9XWXhZVEptTURZdE5ETmtOUzAwTmpCaUxXRmpOMkl0WldOak5USXlNell4TldKaQ; __ssid=b4adf9676cb3a9430bbdaf107592c73; rskxRunCookie=0; rCookie=m6kbnu8qhrpuueq1tfxnyglpufd5nr; QuantumMetricUserID=7f2983365431254d6545c9d9520935b7; stockx_preferred_market_activity=sales; stockx_homepage=sneakers; __pdst=477420963548418494053e0795445794; IR_gbd=stockx.com; _ga=GA1.1.1523747110.1701906797; _gid=GA1.2.1166477341.1701996675; QuantumMetricSessionID=18218a876bf99107edf75a69decaa4ee; stockx_product_visits=1; stockx_session_id=40478d32-2c5f-489f-8a5b-8b6d00baba46; stockx_session=13520fed-2074-4261-bfc2-9209904da39d; ftr_blst_1h=1702062927260; inbox_reminder_tooltip_count=V1-6; is_gdpr=false; stockx_ip_region=US; cf_clearance=79brHNovNjdZaxVoOVmNTU9FybNZcA7if9sQQLKSHic-1702063038-0-1-4d9666e0.bb49bb15.9a7eb21f-0.2.1702063038; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+08+2023+11%3A17%3A18+GMT-0800+(Pacific+Standard+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=4311af09-4a1b-4f7f-aef0-e9695a0e947c&interactionCount=1&landingPath=NotLandingPage&groups=BG84%3A1%2CC0004%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false; _gat=1; _px3=149f754348995e06d7bc346e2c076859d3a702c5521be3c7a86698ea93874b79:wRgz61qro2slI+JpenVjub55+iTYLxiX2SNH+mrxImht2eiVM1WMGgbBiU1Q0CCt4JvYGpPe2daugxcw6E/Drg==:1000:3B81cxaNXNZQlSn0ZOaNH+x8G048s81p4qz8SwVKOlmT7MKSDZaz4XRYUj9vwIl7wGkFLuTxDCO8EfVilI7zyMiwo7xgfs4epz5hcnM7vK4Ci5ufWnAwlQNluj/sRT+M5M6zagnKX/Ot+bPuQ9FFU63O772DNw/H9AOkphhyc8wXqejle3x5pdNTQeaN0YqqwMK6+F4mEj3FF0CSThb8b51JcfrnbSQS18phDlXzW04=; _ga=GA1.1.1523747110.1701906797; lastRskxRun=1702063039075; __cf_bm=nQGA4lJtFhQyWCOJNibz5S7h9XG1Vq2dXEMHv17fFrU-1702063039-0-Aayr2HSHGZFGk6up4E+SUiRNLc43nGqG6GHKrJyat8V51wmq3H0CvVmks5eWUjnsST/bZkf51eVAqrVXwuKH9fg=; forterToken=7634462a2a614382bf18ec90746c558d_1702063038724__UDF43-m4_13ck; _pxde=9aeb95b007777bdc15d4d64af79a6d989b2fe4f3bae7c89e841b858bb555b00f:eyJ0aW1lc3RhbXAiOjE3MDIwNjMwNDA5NDgsImZfa2IiOjB9; IR_9060=1702063042769%7C4294847%7C1702063042769%7C%7C; IR_PI=a2b4387f-9492-11ee-a0d6-b939e1749955%7C1702149442769; _tq_id.TV-6345811836-1.1a3e=6994ec2c459f3972.1701906801.0.1702063043..; _ga_TYYSNQDG4W=GS1.1.1702062926.5.1.1702063044.0.0.0; _uetsid=4ea307f0955f11ee90efa56aa728dee8; _uetvid=d1b008c0a1a511ed8fbc5120d7b11837; _dd_s=rum=0&expire=1702063944327&logs=1&id=c1ee7000-e149-450b-9fb2-27b21811127d&created=1702062925734",      'origin': 'https://stockx.com',
      'referer': f'https://stockx.com/{url_key}',
      'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'selected-country': 'US',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
      'x-operation-name': 'GetProduct',
      'x-stockx-device-id': '9035ff45-2262-4085-9a86-65e00c5f06a7',
      'x-stockx-session-id': '1df5ef7a-07d3-4433-96d2-45bc6e1c70c6',
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
    # 'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjVjMGZlMGZkLWMwNTEtMTFlNy1iZmIxLTEyODg3OGViYjhiNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImh0dHBzOi8vc3RvY2t4LmNvbS9lbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5zdG9ja3guY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3MDQ4MjgyNDA5OTg0ODIzMjAyIiwiYXVkIjpbImdhdGV3YXkuc3RvY2t4LmNvbSIsImh0dHBzOi8vc3RvY2t4LXByb2Quc3RvY2t4LXByb2QuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMzI4OTk0NCwiZXhwIjoxNzEzMzMzMTQ0LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIiwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQifQ.axOMkt3C3Vd2tFDAQfqnxiKC-ecWc1sENEHQIUpvDCqlx5P8-HbH0mQvATYBIaHVafZw8DGhlIPvHAPjjwk9pEzbxbWXC-0ILS5SQbT8IISkjSb1clyLjZIovZfrtkVPPn3OaINI4zr4TWcQhpeAk8xfeYkL9egmF1H9_etO8QBus0tGFIB_6kZPW6Koy9_AFMKWN_hAnRuXG0yZjbfnMUytBpZGCvM3CgL-4epGCXIHsgta8uMo44Hfv3BT58LM9x7Y7dQ6IPZpKLVxZ7bkTfYBORlV5xfVXxtyycKc5az84kZiZ5pGsp5wfpw4qXVCkJ0CMX8y9znZnfk5beJdrA',
    'content-type': 'application/json',
    "cookie": "stockx_device_id=3aeca24a-cd31-4247-aefa-9a8f7def424a; language_code=en; stockx_selected_region=US; display_location_selector=false; pxcts=9fc19cbe-9492-11ee-9877-7bb915045ef5; _pxvid=9fc18fc3-9492-11ee-9877-cc96b6d9de68; __pxvid=9fdde741-9492-11ee-a11a-0242ac120004; _gcl_au=1.1.634647357.1701906797; ajs_user_id=9446d072-0baf-11ee-8a06-12f12be0eb51; ajs_anonymous_id=5610aa88-956b-4707-b2ff-a0d045d1ef7a; rbuid=rbos-02a7aa0f-e9f7-4546-9ed9-06eca955d094; _pin_unauth=dWlkPU9XWXhZVEptTURZdE5ETmtOUzAwTmpCaUxXRmpOMkl0WldOak5USXlNell4TldKaQ; __ssid=b4adf9676cb3a9430bbdaf107592c73; rskxRunCookie=0; rCookie=m6kbnu8qhrpuueq1tfxnyglpufd5nr; QuantumMetricUserID=7f2983365431254d6545c9d9520935b7; stockx_preferred_market_activity=sales; stockx_homepage=sneakers; __pdst=477420963548418494053e0795445794; IR_gbd=stockx.com; _ga=GA1.1.1523747110.1701906797; _gid=GA1.2.1166477341.1701996675; QuantumMetricSessionID=18218a876bf99107edf75a69decaa4ee; stockx_product_visits=1; stockx_session_id=40478d32-2c5f-489f-8a5b-8b6d00baba46; stockx_session=13520fed-2074-4261-bfc2-9209904da39d; ftr_blst_1h=1702062927260; inbox_reminder_tooltip_count=V1-6; is_gdpr=false; stockx_ip_region=US; cf_clearance=79brHNovNjdZaxVoOVmNTU9FybNZcA7if9sQQLKSHic-1702063038-0-1-4d9666e0.bb49bb15.9a7eb21f-0.2.1702063038; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+08+2023+11%3A17%3A18+GMT-0800+(Pacific+Standard+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=4311af09-4a1b-4f7f-aef0-e9695a0e947c&interactionCount=1&landingPath=NotLandingPage&groups=BG84%3A1%2CC0004%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false; _gat=1; _px3=149f754348995e06d7bc346e2c076859d3a702c5521be3c7a86698ea93874b79:wRgz61qro2slI+JpenVjub55+iTYLxiX2SNH+mrxImht2eiVM1WMGgbBiU1Q0CCt4JvYGpPe2daugxcw6E/Drg==:1000:3B81cxaNXNZQlSn0ZOaNH+x8G048s81p4qz8SwVKOlmT7MKSDZaz4XRYUj9vwIl7wGkFLuTxDCO8EfVilI7zyMiwo7xgfs4epz5hcnM7vK4Ci5ufWnAwlQNluj/sRT+M5M6zagnKX/Ot+bPuQ9FFU63O772DNw/H9AOkphhyc8wXqejle3x5pdNTQeaN0YqqwMK6+F4mEj3FF0CSThb8b51JcfrnbSQS18phDlXzW04=; _ga=GA1.1.1523747110.1701906797; lastRskxRun=1702063039075; __cf_bm=nQGA4lJtFhQyWCOJNibz5S7h9XG1Vq2dXEMHv17fFrU-1702063039-0-Aayr2HSHGZFGk6up4E+SUiRNLc43nGqG6GHKrJyat8V51wmq3H0CvVmks5eWUjnsST/bZkf51eVAqrVXwuKH9fg=; forterToken=7634462a2a614382bf18ec90746c558d_1702063038724__UDF43-m4_13ck; _pxde=9aeb95b007777bdc15d4d64af79a6d989b2fe4f3bae7c89e841b858bb555b00f:eyJ0aW1lc3RhbXAiOjE3MDIwNjMwNDA5NDgsImZfa2IiOjB9; IR_9060=1702063042769%7C4294847%7C1702063042769%7C%7C; IR_PI=a2b4387f-9492-11ee-a0d6-b939e1749955%7C1702149442769; _tq_id.TV-6345811836-1.1a3e=6994ec2c459f3972.1701906801.0.1702063043..; _ga_TYYSNQDG4W=GS1.1.1702062926.5.1.1702063044.0.0.0; _uetsid=4ea307f0955f11ee90efa56aa728dee8; _uetvid=d1b008c0a1a511ed8fbc5120d7b11837; _dd_s=rum=0&expire=1702063944327&logs=1&id=c1ee7000-e149-450b-9fb2-27b21811127d&created=1702062925734",    'origin': 'https://stockx.com',
    'referer': 'https://stockx.com/',
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
  print(response)
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
    # 'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjVjMGZlMGZkLWMwNTEtMTFlNy1iZmIxLTEyODg3OGViYjhiNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImh0dHBzOi8vc3RvY2t4LmNvbS9lbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5zdG9ja3guY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3MDQ4MjgyNDA5OTg0ODIzMjAyIiwiYXVkIjpbImdhdGV3YXkuc3RvY2t4LmNvbSIsImh0dHBzOi8vc3RvY2t4LXByb2Quc3RvY2t4LXByb2QuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcxMzI4OTk0NCwiZXhwIjoxNzEzMzMzMTQ0LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIiwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQifQ.axOMkt3C3Vd2tFDAQfqnxiKC-ecWc1sENEHQIUpvDCqlx5P8-HbH0mQvATYBIaHVafZw8DGhlIPvHAPjjwk9pEzbxbWXC-0ILS5SQbT8IISkjSb1clyLjZIovZfrtkVPPn3OaINI4zr4TWcQhpeAk8xfeYkL9egmF1H9_etO8QBus0tGFIB_6kZPW6Koy9_AFMKWN_hAnRuXG0yZjbfnMUytBpZGCvM3CgL-4epGCXIHsgta8uMo44Hfv3BT58LM9x7Y7dQ6IPZpKLVxZ7bkTfYBORlV5xfVXxtyycKc5az84kZiZ5pGsp5wfpw4qXVCkJ0CMX8y9znZnfk5beJdrA',
    'content-type': 'application/json',
    "cookie": "stockx_device_id=3aeca24a-cd31-4247-aefa-9a8f7def424a; language_code=en; stockx_selected_region=US; display_location_selector=false; pxcts=9fc19cbe-9492-11ee-9877-7bb915045ef5; _pxvid=9fc18fc3-9492-11ee-9877-cc96b6d9de68; __pxvid=9fdde741-9492-11ee-a11a-0242ac120004; _gcl_au=1.1.634647357.1701906797; ajs_user_id=9446d072-0baf-11ee-8a06-12f12be0eb51; ajs_anonymous_id=5610aa88-956b-4707-b2ff-a0d045d1ef7a; rbuid=rbos-02a7aa0f-e9f7-4546-9ed9-06eca955d094; _pin_unauth=dWlkPU9XWXhZVEptTURZdE5ETmtOUzAwTmpCaUxXRmpOMkl0WldOak5USXlNell4TldKaQ; __ssid=b4adf9676cb3a9430bbdaf107592c73; rskxRunCookie=0; rCookie=m6kbnu8qhrpuueq1tfxnyglpufd5nr; QuantumMetricUserID=7f2983365431254d6545c9d9520935b7; stockx_preferred_market_activity=sales; stockx_homepage=sneakers; __pdst=477420963548418494053e0795445794; IR_gbd=stockx.com; _ga=GA1.1.1523747110.1701906797; _gid=GA1.2.1166477341.1701996675; QuantumMetricSessionID=18218a876bf99107edf75a69decaa4ee; stockx_product_visits=1; stockx_session_id=40478d32-2c5f-489f-8a5b-8b6d00baba46; stockx_session=13520fed-2074-4261-bfc2-9209904da39d; ftr_blst_1h=1702062927260; inbox_reminder_tooltip_count=V1-6; is_gdpr=false; stockx_ip_region=US; cf_clearance=79brHNovNjdZaxVoOVmNTU9FybNZcA7if9sQQLKSHic-1702063038-0-1-4d9666e0.bb49bb15.9a7eb21f-0.2.1702063038; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+08+2023+11%3A17%3A18+GMT-0800+(Pacific+Standard+Time)&version=202309.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=4311af09-4a1b-4f7f-aef0-e9695a0e947c&interactionCount=1&landingPath=NotLandingPage&groups=BG84%3A1%2CC0004%3A1%2CC0005%3A1%2CC0002%3A1%2CC0003%3A1%2CC0001%3A1&AwaitingReconsent=false; _gat=1; _px3=149f754348995e06d7bc346e2c076859d3a702c5521be3c7a86698ea93874b79:wRgz61qro2slI+JpenVjub55+iTYLxiX2SNH+mrxImht2eiVM1WMGgbBiU1Q0CCt4JvYGpPe2daugxcw6E/Drg==:1000:3B81cxaNXNZQlSn0ZOaNH+x8G048s81p4qz8SwVKOlmT7MKSDZaz4XRYUj9vwIl7wGkFLuTxDCO8EfVilI7zyMiwo7xgfs4epz5hcnM7vK4Ci5ufWnAwlQNluj/sRT+M5M6zagnKX/Ot+bPuQ9FFU63O772DNw/H9AOkphhyc8wXqejle3x5pdNTQeaN0YqqwMK6+F4mEj3FF0CSThb8b51JcfrnbSQS18phDlXzW04=; _ga=GA1.1.1523747110.1701906797; lastRskxRun=1702063039075; __cf_bm=nQGA4lJtFhQyWCOJNibz5S7h9XG1Vq2dXEMHv17fFrU-1702063039-0-Aayr2HSHGZFGk6up4E+SUiRNLc43nGqG6GHKrJyat8V51wmq3H0CvVmks5eWUjnsST/bZkf51eVAqrVXwuKH9fg=; forterToken=7634462a2a614382bf18ec90746c558d_1702063038724__UDF43-m4_13ck; _pxde=9aeb95b007777bdc15d4d64af79a6d989b2fe4f3bae7c89e841b858bb555b00f:eyJ0aW1lc3RhbXAiOjE3MDIwNjMwNDA5NDgsImZfa2IiOjB9; IR_9060=1702063042769%7C4294847%7C1702063042769%7C%7C; IR_PI=a2b4387f-9492-11ee-a0d6-b939e1749955%7C1702149442769; _tq_id.TV-6345811836-1.1a3e=6994ec2c459f3972.1701906801.0.1702063043..; _ga_TYYSNQDG4W=GS1.1.1702062926.5.1.1702063044.0.0.0; _uetsid=4ea307f0955f11ee90efa56aa728dee8; _uetvid=d1b008c0a1a511ed8fbc5120d7b11837; _dd_s=rum=0&expire=1702063944327&logs=1&id=c1ee7000-e149-450b-9fb2-27b21811127d&created=1702062925734",    'origin': 'https://stockx.com',
    'origin': 'https://stockx.com',
    'referer': f'https://stockx.com/{url_key}',
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
  # output_df = output_df[['sku', 'img_url', 'title', 'url',  'brand',
  #                        'size', 'department', 'lowest_ask', 'highest_bid',
  #                        'last_sales', 'last_sales_72_hrs', 'number_of_asks',
  #                        'highest_bid', 'scraped_timestamp']]
  # return output_df
  
  df = pd.dataframe(output_df.values, columns = ['sku', 'img_url', 'title', 'url',  'brand',
                         'size', 'department', 'lowest_ask', 'highest_bid',
                         'last_sales', 'last_sales_72_hrs', 'number_of_asks',
                         'highest_bid', 'scraped_timestamp'])
  return st.dataframe(df, hide_index=True)


st.title('🔌⚡️👻')

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
    # get_stockx_data('AQ9129-170')
sku = st.text_input('SKU to search! 🔍')
if sku is not None or sku != '':
  get_stockx_data(sku)