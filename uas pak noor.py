import random

def play_game():
    # Rentang angka tetap: 1-100, attempts tetap: 10
    min_num, max_num = 1, 100
    attempts = 10
    
    # Generate angka acak
    target = random.randint(min_num, max_num)
    print("Selamat datang di Game Tebak Angka!")
    print(f"Saya telah memilih angka antara {min_num} dan {max_num}. Anda punya {attempts} kesempatan untuk menebak.")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Tebakan ke-{attempt}: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        
        if guess < target:
            print("Terlalu kecil!")
        elif guess > target:
            print("Terlalu besar!")
        else:
            print(f"Selamat! Anda menebak benar dalam {attempt} kali percobaan.")
            return True  # Menang
    
    print(f"Maaf, Anda kehabisan kesempatan. Angka yang benar adalah {target}.")
    return False  # Kalah

def main():
    while True:
        play_game()
        
        play_again = input("Apakah Anda ingin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            print("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    main()