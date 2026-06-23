#!/usr/bin/env python3
import requests
import time
import sys
import os
import re
import random
import string
import json
from datetime import datetime

# ==================== প্রিমিয়াম কালার কোড ====================
class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# ==================== ভাষা ====================
LANGUAGES = {
    '1': {'code': 'fr-FR', 'name': 'Français', 'flag': '🇫🇷', 'accept': 'fr-FR,fr;q=0.9,en;q=0.8'},
    '2': {'code': 'es-ES', 'name': 'Español', 'flag': '🇪🇸', 'accept': 'es-ES,es;q=0.9,en;q=0.8'},
    '3': {'code': 'en-US', 'name': 'English', 'flag': '🇺🇸', 'accept': 'en-US,en;q=0.9'},
    '4': {'code': 'bn-BD', 'name': 'বাংলা', 'flag': '🇧🇩', 'accept': 'bn-BD,bn;q=0.9,en;q=0.8'},
    '5': {'code': 'hi-IN', 'name': 'हिन्दी', 'flag': '🇮🇳', 'accept': 'hi-IN,hi;q=0.9,en;q=0.8'},
}

def select_language():
    os.system('clear')
    print(f"{Colors.BRIGHT_YELLOW}╔{'═' * 58}╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}║{Colors.BRIGHT_CYAN}{Colors.BOLD}      🌐 SELECT LANGUAGE              {Colors.BRIGHT_YELLOW}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}╠{'═' * 58}╣{Colors.RESET}")
    for key, lang in LANGUAGES.items():
        print(f"{Colors.BRIGHT_YELLOW}║  {Colors.BRIGHT_GREEN}{key}. {lang['flag']} {lang['name']}{' ' * (38 - len(lang['name']))}{Colors.BRIGHT_YELLOW}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}╚{'═' * 58}╝{Colors.RESET}")
    print()
    while True:
        choice = input(f"{Colors.BRIGHT_CYAN}➜ Enter choice (1-5): {Colors.RESET}").strip()
        if choice in LANGUAGES:
            return choice, LANGUAGES[choice]
        print(f"{Colors.BRIGHT_RED}❌ Invalid!{Colors.RESET}")

# ==================== BANNER ====================
def print_banner(selected_lang=None):
    os.system('clear')
    print(f"{Colors.BRIGHT_RED}╔{'═' * 58}╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_YELLOW}   ██████╗  █████╗ ███╗   ██╗ █████╗     ███████╗██████╗ {Colors.BRIGHT_RED}║")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_YELLOW}   ██╔══██╗██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██╔══██╗{Colors.BRIGHT_RED}║")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_YELLOW}   ██████╔╝███████║██╔██╗ ██║███████║    █████╗  ██████╔╝{Colors.BRIGHT_RED}║")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_YELLOW}   ██╔══██╗██╔══██║██║╚██╗██║██╔══██║    ██╔══╝  ██╔══██╗{Colors.BRIGHT_RED}║")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_YELLOW}   ██║  ██║██║  ██║██║ ╚████║██║  ██║    ██║     ██████╔╝{Colors.BRIGHT_RED}║")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_YELLOW}   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝     ╚═════╝ {Colors.BRIGHT_RED}║")
    print(f"{Colors.BRIGHT_RED}╠{'═' * 58}╣{Colors.RESET}")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_CYAN}{Colors.BOLD}      🔥 FB ACCOUNT GEN v3.5  🔥        {Colors.BRIGHT_RED}║")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_MAGENTA}      📡 TG: @mrranamia                    {Colors.BRIGHT_RED}║")
    if selected_lang:
        print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_GREEN}      🌐 {selected_lang['flag']} {selected_lang['name']}{' ' * (31 - len(selected_lang['name']))}{Colors.BRIGHT_RED}║{Colors.RESET}")
    print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_BLACK}      📱 Phone/Email OTP (Codes Hidden)    {Colors.BRIGHT_RED}║")
    print(f"{Colors.BRIGHT_RED}╚{'═' * 58}╝{Colors.RESET}")
    print()

def print_header(text, color=Colors.BRIGHT_CYAN):
    print(f"{color}╔{'═' * 58}╗{Colors.RESET}")
    print(f"{color}║{Colors.BOLD}{text.center(56)}{Colors.RESET}{color}║{Colors.RESET}")
    print(f"{color}╚{'═' * 58}╝{Colors.RESET}")

def print_divider(color=Colors.BRIGHT_BLACK):
    print(f"{color}{'─' * 58}{Colors.RESET}")

# ==================== iPhone ডিভাইস ====================
DEVICES = [
    {'model': 'iPhone11,8', 'brand': 'Apple', 'device': 'iPhone 11'},
    {'model': 'iPhone12,1', 'brand': 'Apple', 'device': 'iPhone 11 Pro'},
    {'model': 'iPhone12,3', 'brand': 'Apple', 'device': 'iPhone 11 Pro Max'},
    {'model': 'iPhone13,2', 'brand': 'Apple', 'device': 'iPhone 12'},
    {'model': 'iPhone13,3', 'brand': 'Apple', 'device': 'iPhone 12 Pro'},
    {'model': 'iPhone13,4', 'brand': 'Apple', 'device': 'iPhone 12 Pro Max'},
    {'model': 'iPhone14,5', 'brand': 'Apple', 'device': 'iPhone 13'},
    {'model': 'iPhone14,2', 'brand': 'Apple', 'device': 'iPhone 13 Pro'},
    {'model': 'iPhone14,3', 'brand': 'Apple', 'device': 'iPhone 13 Pro Max'},
    {'model': 'iPhone14,7', 'brand': 'Apple', 'device': 'iPhone 14'},
    {'model': 'iPhone15,2', 'brand': 'Apple', 'device': 'iPhone 14 Pro'},
    {'model': 'iPhone15,3', 'brand': 'Apple', 'device': 'iPhone 14 Pro Max'},
    {'model': 'iPhone15,4', 'brand': 'Apple', 'device': 'iPhone 15'},
    {'model': 'iPhone16,1', 'brand': 'Apple', 'device': 'iPhone 15 Pro'},
    {'model': 'iPhone16,2', 'brand': 'Apple', 'device': 'iPhone 15 Pro Max'},
    {'model': 'iPhone17,1', 'brand': 'Apple', 'device': 'iPhone 16'},
    {'model': 'iPhone17,2', 'brand': 'Apple', 'device': 'iPhone 16 Pro'},
    {'model': 'iPhone17,3', 'brand': 'Apple', 'device': 'iPhone 16 Pro Max'},
]

IOS_VERSIONS = ['16.5', '16.8', '17', '18.1', '18']

def get_random_device():
    return random.choice(DEVICES)

def get_device_ua(device, ios_version):
    if '.' in ios_version:
        major, minor = ios_version.split('.')
        ios_ua = f"{major}_{minor}"
        version_ua = ios_version
    else:
        ios_ua = f"{ios_version}_0"
        version_ua = f"{ios_version}.0"
    return f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ua} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version_ua} Mobile/15E148 Safari/604.1'

# ==================== ইউটিলিটি ====================
def random_name():
    first = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn']
    last = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    return random.choice(first), random.choice(last)

def random_birth():
    return random.randint(1, 28), random.randint(1, 12), random.randint(1980, 2005)

def is_email(s):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', s))

def extract_email(s):
    if '|' in s:
        parts = s.split('|')
        first = parts[0].strip()
        if is_email(first):
            return first
        m = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', s)
        return m.group(0) if m else first
    return s.strip()

def extract_uid_from_cookies(cookies_dict):
    return cookies_dict.get('c_user') if cookies_dict.get('c_user', '').isdigit() else None

def format_cookies_big(cookies_dict):
    priority = ['datr', 'c_user', 'xs', 'fr', 'sb']
    parts = []
    for k in priority:
        if k in cookies_dict:
            parts.append(f"{k}={cookies_dict[k]}")
    for k, v in cookies_dict.items():
        if k not in priority:
            parts.append(f"{k}={v}")
    return '; '.join(parts)

def get_fb_dtsg(session, headers):
    try:
        resp = session.get('https://www.facebook.com/', headers=headers, timeout=30)
        m = re.search(r'"fb_dtsg":"([^"]+)"', resp.text)
        if m:
            return m.group(1)
        m = re.search(r'name="fb_dtsg" value="([^"]+)"', resp.text)
        if m:
            return m.group(1)
        return None
    except:
        return None

def send_verification_code(session, account, headers, selected_lang):
    """যাচাইকরণ কোড পাঠান (ফোন ও ইমেইল উভয়ের জন্য)"""
    try:
        fb_dtsg = get_fb_dtsg(session, headers)
        if not fb_dtsg:
            return False
        
        verify_headers = {
            'User-Agent': headers.get('User-Agent', ''),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': selected_lang['accept'],
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://www.facebook.com/',
            'Origin': 'https://www.facebook.com',
        }
        verify_data = {'fb_dtsg': fb_dtsg, 'submit': 'Send Code', 'resend': '1'}
        resend_url = 'https://www.facebook.com/reg/resend_code/'
        resp = session.post(resend_url, headers=verify_headers, data=verify_data, timeout=30)
        return resp.status_code == 200
    except:
        return False

# ==================== অ্যাকাউন্ট তৈরি ====================
def create_account(account_input, index, total, password, selected_lang):
    account = extract_email(account_input)
    print(f"{Colors.BRIGHT_YELLOW}[{index}/{total}] {account}{Colors.RESET}", end='\r')
    
    fname, lname = random_name()
    day, month, year = random_birth()
    device = get_random_device()
    ios_version = random.choice(IOS_VERSIONS)
    ua = get_device_ua(device, ios_version)
    acc_type = 'email' if is_email(account) else 'phone'
    
    accept_language = selected_lang['accept']
    
    headers = {
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': accept_language,
        'sec-ch-ua-platform': '"iOS"',
        'sec-ch-ua': '"Chromium";v="148", "Android WebView";v="148", "Not/A)Brand";v="99"',
        'x-response-format': 'JSONStream',
        'sec-ch-ua-mobile': '?1',
        'x-asbd-id': '359341',
        'x-fb-lsd': 'AdRg5ufqsQVcQXAYMc0sAcuMAYE',
        'x-requested-with': 'XMLHttpRequest',
        'origin': 'https://limited.facebook.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://limited.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk',
        'priority': 'u=1, i'
    }
    
    data = {
        'ccp': '2',
        'reg_instance': '9XYnakzu3MZlEdcKm5l6S7Xh',
        'submission_request': 'true',
        'helper': '',
        'reg_impression_id': '16b59158-6fd5-4197-a940-9a9a29ce1e50',
        'ns': '3',
        'zero_header_af_client': '',
        'app_id': '103',
        'logger_id': '2dd9b1d6-cbeb-4244-ac05-5f7d8c12f13d',
        'field_names[0]': 'firstname',
        'firstname': fname,
        'lastname': lname,
        'field_names[1]': 'birthday_wrapper',
        'birthday_day': str(day),
        'birthday_month': str(month),
        'birthday_year': str(year),
        'age_step_input': '',
        'did_use_age': '',
        'field_names[2]': 'reg_email__',
        'reg_email__': account,
        'field_names[3]': 'sex',
        'sex': '1',
        'preferred_pronoun': '',
        'custom_gender': '',
        'field_names[4]': 'reg_passwd__',
        'reg_passwd__': password,
        'name_suggest_elig': 'false',
        'was_shown_name_suggestions': 'false',
        'did_use_suggested_name': 'false',
        'use_custom_gender': 'false',
        'guid': '',
        'pre_form_step': '',
        'submit': 'Sign up',
        'fb_dtsg': 'NAfx3wG1Lv9JqEl5Xo_k4IgVl9NOIczPI42MHjtMHwUlwIJPkjDwRQw:0:0',
        'jazoest': '24981',
        'lsd': 'AdRg5ufqsQVcQXAYMc0sAcuMAYE',
        '__dyn': '1Z3pawlEnwm8_Bg9ppoW5UdE4a2i5U4e0C86u7E39x60zU3ex608ewk9E4W0pKq0FE6S0x81vohw73wGwcq1GwqU2YwbK0oi0zE1jU1soG0hi0Lo6-0Co1kU1UU3jwea',
        '__csr': '',
        '__hsdp': '',
        '__hblp': '',
        '__sjsp': '',
        '__req': '9',
        '__fmt': '1',
        '__a': 'AYziFkahooYGibmFOiEjTgieqVVZfkpaag_fk7JZ7MuPjmhxkA1_y8Va3uw3j-5R57TlEkPviSDWHWtTFhXBDy8M4ZSYCckmIVU',
        '__user': '0'
    }
    
    url = 'https://limited.facebook.com/reg/submit/?app_id=103&multi_step_form=1&skip_suma=0&shouldForceMTouch=1'
    
    try:
        session = requests.Session()
        response = session.post(url, headers=headers, data=data, timeout=30)
        print(" " * 70, end='\r')
        
        if response.status_code == 200:
            cookies = session.cookies.get_dict()
            uid = extract_uid_from_cookies(cookies)
            
            # ===== যাচাইকরণ কোড পাঠান =====
            send_verification_code(session, account, headers, selected_lang)
            
            # ===== আউটপুট (শুধু UID, Device, Cookies) =====
            print(f"{Colors.BRIGHT_GREEN}✅ {account} ({acc_type}) - Account Created!{Colors.RESET}")
            print_divider(Colors.BRIGHT_CYAN)
            print(f"{Colors.BRIGHT_GREEN}📱 Account: {account}{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}🆔 UID: {uid if uid else 'Not found'}{Colors.RESET}")
            print(f"{Colors.BRIGHT_BLUE}📲 Device: {device['brand']} {device['device']} (iOS {ios_version}){Colors.RESET}")
            
            print(f"{Colors.BRIGHT_MAGENTA}🍪 Cookies:{Colors.RESET}")
            print_divider(Colors.BRIGHT_BLACK)
            if cookies:
                print(f"{Colors.BRIGHT_WHITE}{format_cookies_big(cookies)}{Colors.RESET}")
            else:
                print(f"{Colors.BRIGHT_RED}No cookies{Colors.RESET}")
            print_divider(Colors.BRIGHT_CYAN)
            
            return {
                'account': account,
                'success': True,
                'password': password,
                'uid': uid,
                'cookies': cookies,
                'type': acc_type,
                'device': device,
                'ios': ios_version,
                'language': selected_lang
            }
        else:
            print(f"{Colors.BRIGHT_RED}❌ {account} ({acc_type}) - Status: {response.status_code}{Colors.RESET}")
            return {'account': account, 'success': False}
    except Exception as e:
        print(f"{Colors.BRIGHT_RED}❌ {account} ({acc_type}) - Error: {str(e)[:50]}{Colors.RESET}")
        return {'account': account, 'success': False}

# ==================== প্রধান ====================
def main():
    lang_choice, selected_lang = select_language()
    print_banner(selected_lang)
    print_header("📌 CREATE ACCOUNT", Colors.BRIGHT_CYAN)
    print()
    
    print(f"{Colors.BRIGHT_CYAN}📌 Supported Account Types:{Colors.RESET}")
    print(f"   {Colors.BRIGHT_GREEN}• Phone number (any format){Colors.RESET}")
    print(f"   {Colors.BRIGHT_GREEN}• Email{Colors.RESET}")
    print(f"{Colors.BRIGHT_BLACK}   🌐 Language: {selected_lang['flag']} {selected_lang['name']}{Colors.RESET}")
    print(f"{Colors.BRIGHT_BLACK}   📱 Verification code sent to Phone/Email (Hidden){Colors.RESET}")
    print()
    print_divider(Colors.BRIGHT_BLACK)
    
    password = input(f"{Colors.BRIGHT_YELLOW}🔑 Enter password (min 6): {Colors.RESET}").strip()
    while len(password) < 6:
        print(f"{Colors.BRIGHT_RED}❌ Min 6 characters!{Colors.RESET}")
        password = input(f"{Colors.BRIGHT_YELLOW}🔑 Enter password: {Colors.RESET}").strip()
    
    print(f"{Colors.BRIGHT_GREEN}✅ Password set!{Colors.RESET}")
    print_divider(Colors.BRIGHT_BLACK)
    
    print(f"{Colors.BRIGHT_CYAN}📧 Enter accounts (Press Enter twice to start){Colors.RESET}")
    accounts = []
    while True:
        line = input()
        if line == "":
            if accounts:
                break
            continue
        accounts.append(line.strip())
    
    if not accounts:
        print(f"{Colors.BRIGHT_RED}❌ No accounts!{Colors.RESET}")
        sys.exit(0)
    
    print()
    print_divider(Colors.BRIGHT_BLACK)
    for i, acc in enumerate(accounts, 1):
        extracted = extract_email(acc)
        acc_type = 'email' if is_email(extracted) else 'phone'
        if acc != extracted:
            print(f"   {Colors.BRIGHT_CYAN}{i}. {extracted}{Colors.RESET} ({acc_type}) [extracted]")
        else:
            print(f"   {Colors.BRIGHT_CYAN}{i}. {acc}{Colors.RESET} ({acc_type})")
    
    print()
    print_divider(Colors.BRIGHT_BLACK)
    confirm = input(f"{Colors.BRIGHT_YELLOW}❓ Create accounts? (y/n): {Colors.RESET}").strip().lower()
    if confirm != 'y':
        print(f"{Colors.BRIGHT_RED}❌ Cancelled!{Colors.RESET}")
        sys.exit(0)
    
    print()
    print_header("🚀 PROCESSING ACCOUNTS", Colors.BRIGHT_MAGENTA)
    print()
    
    for i, acc in enumerate(accounts, 1):
        create_account(acc, i, len(accounts), password, selected_lang)
        print()
        if i < len(accounts):
            time.sleep(random.uniform(2, 4))
    
    print()
    print_header("✅ ALL ACCOUNTS PROCESSED!", Colors.BRIGHT_GREEN)
    print(f"{Colors.BRIGHT_YELLOW}🎉 Successfully completed!{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BRIGHT_RED}❌ Stopped by user{Colors.RESET}")
        sys.exit(0)
