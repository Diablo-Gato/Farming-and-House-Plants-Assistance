import google.generativeai as genai
import csv
import os

apiKey = "APi-key"
genai.configure(api_key=apiKey)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_data():
    data = []
    path = r"D:\Programs\Python\Hackathon Project\datasets"
    list_file = os.listdir(path)
    for file in list_file:
        singleData = [f"Part of csv {file}"]
        with open(fr"{path}\{file}",newline="" ) as f:
            singleData = []
            reader = csv.reader(f)
            for row in reader:
                str_ = " "
                singleData.append(str_.join(row))
            data.append({"role": "user", "parts": singleData})

    return data



def chat_bot(message):
    chat = model.start_chat(history=get_data())
    response = chat.send_message(message)
    return response.text
