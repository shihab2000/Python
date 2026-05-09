import demoji

text = "Good morning 😊🔥"
a1 = demoji.replace(text, " ")
print(a1)

text1 = "Happy birthday! 🎂🎈"
a2 = demoji.replace_with_desc(text1)
print(a2)

text3 = "Good morning ☀️😊"
emojis = demoji.findall(text)
print(emojis)