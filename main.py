import random

name = "Anurag Ranjan"
admission_number = "21JE0146"

def main():
    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮" )
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    fortunes = {
        "happy": [
            f"Great things await you, {name}! Keep smiling.",
            "Joy multiplies when shared. Go spread some!",
        ],
        "sad": [
            "Tough times don’t last. Better days are coming.",
            "Even the darkest night ends with a sunrise.",
        ],
        "neutral": [
            "Stay alert—interesting surprises are just around the corner.",
            "Balance is your superpower today.",
        ],
       
    }

    if mood in fortunes:
        print("✨ Your fortune: " + random.choice(fortunes[mood]) + " ✨")
    else:
        print("🤔 I can't read that mood... Try happy, sad, neutral, or stressed.")

if __name__ == "__main__":
    main()
