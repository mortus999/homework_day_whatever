# ========= Question 1 ===================

import mood_responses
import text_utils as caps
def main():
    
    
    while True:
        print("How are we feeling? \n1. Happy \n2. Sad \n3. Anxious \n4. excited \n5. tired")
        choice = input("Choose an option: ")
        if choice == "1":
            return mood_responses.mood_happy()
            
        elif choice == "2":
            return mood_responses.mood_sad()
            
        elif choice == "3":
            return mood_responses.mood_anxious()
            
        elif choice == "4":
            return mood_responses.mood_excited()
            
        elif choice == "5":
            return mood_responses.mood_tired()
            
        else:
            print("Please enter a valid input")
print(caps.capitalize_string("Hello"))
if __name__ == "__main__":
    print(__name__)
    main()

