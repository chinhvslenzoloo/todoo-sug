import json
import os

FILE = "todos.json"

def load_todos():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_todos(todos):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)

def add_todo(title):
    todos = load_todos()
    todos.append({"title": title, "done": False})
    save_todos(todos)
    print(f"✅ Нэмэгдлээ: {title}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("⛔ Одоогоор хоосон байна.")
        return
    print("\n📋 TODO жагсаалт:")
    for i, t in enumerate(todos, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['title']} {status}")

#ene hawitsaa delete hiideg vildeliig hii
#def delete_todo(index):



def toggle_todo(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        todos[index - 1]["done"] = not todos[index - 1]["done"]
        save_todos(todos)
        print(f"🔁 Статус солигдлоо: {todos[index - 1]['title']}")
    else:
        print("⚠️ Тийм дугаар байхгүй байна!")

def main():
    print("🧠 TODO App (JSON хадгалалттай)\n")
    while True:
        cmd = input(">>> Команд (add/list/done/del/exit): ").strip().lower()

        if cmd == "add":
            title = input("  → Юу хийх вэ?: ").strip()
            if title:
                add_todo(title)
            else:
                print("⚠️ Нэр оруулна уу.")
        elif cmd == "list":
            list_todos()
        elif cmd == "done":
            try:
                n = int(input("  → Дугаар: "))
                toggle_todo(n)
            except ValueError:
                print("⚠️ Зөв дугаар оруул.")
        #elif cmd == "del": geed hii
        elif cmd == "exit":
            print("👋 Гарлаа!")
            break
        else:
            print("⚙️ Командууд: add, list, done, del, exit")

if __name__ == "__main__":
    main()
