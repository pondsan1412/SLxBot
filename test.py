from googletrans import Translator
words_to_translate = "สวัสดีครับผมชื่อบ่อน้ำ และผมชอบเล่นเกมจากนินเทนโด้ เป็นเกมที่มีชื่อว่า มาริโอ้คาร์ท ซึ่งเป็นเกมแนวแข่งรถ style casual"
translator = Translator()
translated_text = translator.translate(words_to_translate,dest = "en")


print(translated_text.text)