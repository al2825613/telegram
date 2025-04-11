
import requests
import time

def load_cookies(file_path):
    cookies = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if '=' in line and 'c_user' in line and 'xs' in line:
                cookie = {}
                for part in line.split(';'):
                    if '=' in part:
                        k, v = part.strip().split('=', 1)
                        cookie[k.strip()] = v.strip()
                cookies.append(cookie)
    return cookies

def report_account(cookie, target_id):
    session = requests.Session()
    session.cookies.update(cookie)
    try:
        report_url = f"https://mbasic.facebook.com/help/contact/295309487309948"
        response = session.get(report_url)
        if "الإبلاغ" in response.text or "report" in response.text:
            print(f"[+] تم فتح صفحة البلاغ بـ: {cookie.get('c_user')}")
            return True
        else:
            print(f"[-] فشل فتح النموذج بـ: {cookie.get('c_user')}")
            return False
    except Exception as e:
        print(f"[!] خطأ: {e}")
        return False

def main():
    target_id = input("ادخل ID الحساب المستهدف: ").strip()
    cookies = load_cookies("facebook_cookies.txt")
    print(f"تم تحميل {len(cookies)} كوكيز.
")

    for i, cookie in enumerate(cookies):
        print(f"[*] بلاغ رقم {i+1}")
        report_account(cookie, target_id)
        time.sleep(2)

if __name__ == "__main__":
    main()
