import requests,json,random,os,time,string,re,shutil
base_user_agents = [
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Chrome/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Safari/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Chrome/%.1f.%.1f',
]
def rand_ua():
    return random.choice(base_user_agents) % (random.random() + 5, random.random() + random.randint(1, 8), random.random(), random.randint(2000, 2100), random.randint(92215, 99999), (random.random() + random.randint(3, 9)), random.random())
User = ''.join(random.choice(string.ascii_letters) for _ in range(10))
Numbers = random.randint(10000000, 99999999)
def reg_accounts(mail):
    email=f'{mail}'
    head_main={"Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": rand_ua()
    }
    req_start=requests.post('https://api.fazpass.com/v1/m/auth/register/start',headers=head_main,json={"pic_name":User,"pic_email":f"{email}","pic_phone":"+668"+str(Numbers),"country":"Thailand"})
    start=req_start.json()
    if start['status']:
       _json={"name":User,"source_lead":"Google","job_title":"Moni"+User,"company_size":"Startup","channel_to_use":["email"]}
       req_id=requests.patch
       r=req_id('https://api.fazpass.com/v1/m/auth/register/finish/'+str(start['data']['id']),headers=head_main,json=_json).json()
       if r['status']:
          get_otp=requests.post('https://api.fazpass.com/v1/m/auth/activate/request',headers=head_main,json={"pic_email": f"{email}"})
          g=get_otp.json()
          if g['status']:
             getID = {"id": start['data']['id'],'otpid': g['data']['otp_id']}
             file_name = "Fazpass_id/GetOTP.json"
             with open(file_name, "w") as json_file:
                  json.dump(getID, json_file)
          else:print('[ Register ] Error otp!!')
       else:print('[ Register ] Something is wrong!!')
    else:print('[ Register ] error!!')
import re
import shutil
User = ''.join(random.choice(string.ascii_letters) for _ in range(10))
Numbers = random.randint(10000000, 99999999)
python_cmd = shutil.which('python') or shutil.which('python3')
def generate_fake_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

fake_ip = generate_fake_ip()
session = requests.Session()

def _GenEmail():
    zort = session
    zort.headers.update({
        "name": "X-Forwarded-For","value": f"{fake_ip}"})
    Response_rmail = zort.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
    if Response_rmail.status_code == 200:
        Mail=Response_rmail.json()
        reg_accounts(Mail[0])
        mail=Response_rmail.json()[0]
        mail_domain = "@" + mail.split("@")[-1] if "@" in mail else ""
        mail_name = mail.split("@")[0] if "@" in mail else mail
        name=mail_name
        domain=mail_domain[1:]
        email_data = {"name": name,"domain": domain}
        file_name = "Getmail/Email.json"
        with open(file_name, "w") as json_file:
             json.dump(email_data, json_file)
        time.sleep(1)
        with open('Getmail/Email.json', 'r') as file:
            data = json.load(file)
        user = data['name']
        email = data['domain']
        found_merchant_key = None
        otp_code = None
        pin_code = None
        while True:
            rdomain = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={email}')
            if rdomain.ok:
                ids = [item['id'] for item in rdomain.json()]
                if ids:
                    for MessID in ids:
                         Getmass = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={email}&id='+str(MessID))
                         if Getmass.ok:
                             message_data = Getmass.json()
                             body_text = message_data.get('body', '')

                             if 'Merchant Key' in body_text and found_merchant_key is None:
                                 found_merchant_key = body_text.split('Merchant Key : ')[1].split('\n')[0]

                             if otp_code is None:
                                 match = re.search(r'your otp code is (\d+)', body_text)
                                 if match:
                                     otp_code = match.group(1)

                             if pin_code is None:
                                 match_pin = re.search(r'PIN : (\d+)', body_text)
                                 if match_pin:
                                     pin_code = match_pin.group(1)

                             if found_merchant_key and otp_code:
                                 print(f'|\n|- [ MAIL ] Get -> {Mail[0]}')
                                 time.sleep(2)
                                 print(f'|\n|- [ PIN ] Get -> {pin_code}')
                                 time.sleep(2)
                                 print(f'|\n|- [ OTP ] Get -> {otp_code}')
                                 time.sleep(2)
                                 print(f'|\n|- [ TOKEN ] Get -> {found_merchant_key}')
                                 break

                    if found_merchant_key and otp_code:
                        email_pin = {"email":f"{Mail[0]}" ,"pass":f"{pin_code}", "token":f"{found_merchant_key}"}
                        file_pin = "Fazpass_id/pin.json"
                        with open(file_pin, "w") as json_pin:
                            json.dump(email_pin, json_pin)
                        with open('Fazpass_id/GetOTP.json', 'r') as id_otp:
                            pullid = json.load(id_otp)
                        ID=int(pullid['id'])
                        head_main={"Accept": "application/json, text/plain, */*","Content-Type": "application/json","User-Agent": rand_ua()}
                        activation=requests.post('https://api.fazpass.com/v1/m/auth/activate/validate',headers=head_main,json={"merchant_id":ID,"pic_email":f"{Mail[0]}","otp_id":f"{pullid['otpid']}","otp":f'{otp_code}'})
                        run=activation.json()
                        if run['status']:os.system(f'{python_cmd} main.py')
                        else:print('ERROR: Something is wrong!!')
                        break
            else: print("[RESPONSE]: Something is wrong!!")


