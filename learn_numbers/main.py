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
    number_range = [int(num) for num in input("Give the number range: ").split(" ")]
    if len(number_range) == 1:
        number_range.insert(0, 1)
    use_sound = {"y": True}.get(input("Use sound? (y/n)"), False)

    while True:
        number = int(random.randint(*number_range[:2]))
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
            while True:
                ret = input()
                if ret == "r":
                    playsound("temp.mp3")
                else:
                    break
            print(f"\nNumber: {number_text} ({number})")
        else:
            print(f"\nNumber: {number_text} ({number})")
            input()

        print(f"Correct answer: {resp.text}")

        answer = input("\nDo you want to continue? (y/n)")
        if answer == "n":
            break


if __name__ == "__main__":
    main()
