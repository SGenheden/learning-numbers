import random
import time

import inflect
from googletrans import Translator
from gtts import gTTS
from playsound import playsound


def translate(translator, text):
    for _ in range(10):
        try:
            resp = translator.translate(text, src="en", dest="fr")
        except:
            time.sleep(0.5)
        else:
            return resp


def main():
    engine = inflect.engine()
    translator = Translator()
    max_int = int(input("Give maximum number: "))
    use_sound = {"y": True}.get(input("Use sound? (y/n)"), False)

    while True:
        number = int(random.randint(1, max_int))
        number_text = engine.number_to_words(number)
        resp = translate(translator, number_text)
        if not resp:
            print("Failed")
            break

        if use_sound:
            myobj = gTTS(text=resp.text, lang="fr", slow=True)
            myobj.save("temp.mp3")
            playsound("temp.mp3")
            print("")
        else:
            print(f"\nNumber: {number_text} ({number})")

        input()

        if use_sound:
            print(f"\nNumber: {number_text} ({number})")
        print(f"Correct answer: {resp.text}")

        answer = input("\nDo you want to continue? (y/n)")
        if answer == "n":
            break


if __name__ == "__main__":
    main()
