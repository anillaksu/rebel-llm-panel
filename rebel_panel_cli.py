from core.task_runner import run_task_by_id
from core.test_runner import run_basic_tests

def main_menu():
    while True:
        print("\n[REBEL PANEL]")
        print("1 - Görev çalıştır (örnek)")
        print("2 - Testleri çalıştır")
        print("q - Çıkış")

        choice = input("> Seçiminizi yapın: ").strip()

        if choice == "1":
            run_task_by_id("example_task_id")
        elif choice == "2":
            run_basic_tests()
        elif choice.lower() == "q":
            print("[REBEL] Çıkılıyor...")
            break
        else:
            print("[REBEL] Geçersiz seçim.")

if __name__ == "__main__":
    main_menu()
