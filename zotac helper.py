import webbrowser


def open_tab(url):
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab(url)

steps = ["1: Login", "2: ATC", "3: Paypal start", "4: Paypal review"]
urls = ["https://www.zotacstore.com/us/customer/account/login/", "https://www.zotacstore.com/us/graphics-cards/geforce-rtx-30-series?limit=24", "https://store.zotac.com/paypal/express/start/", "https://store.zotac.com/paypal/express/review/"]
amounts = [6, 6, 6, 6]

while True:
    print("\n\n\n")
    print("Select a step")
    for step in steps:
        print(step)
    try:
        stepindex = int(input())
        print("You selected step "+steps[stepindex-1])
        for i in range(amounts[stepindex-1]):
            open_tab(urls[stepindex-1])
    except:
        print("Enter a valid integer that corresponds to a step")
