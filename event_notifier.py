import os
import datetime
from plyer import notification
import pandas as pd

if __name__ == "__main__":
    today= datetime.datetime.now().strftime("%d-%m")
    print(today)
    os.chdir("F:\python project github\Event_notifier") # add path of your excel file "calender.xlsx"
    df = pd.read_excel("calender.xlsx", index_col = 0)
    # print(df)
    for index, item in df.iterrows():
        event = item['Event_list'].strftime("%d-%m")
        if event == today:
            title = "Today is "+' '+ item["Event_name"]
            message = "Wish you a happy "+ item["Event_name"]
            notification.notify(title= title, message= message, timeout= 5) # this line of code will show notification on windows
        