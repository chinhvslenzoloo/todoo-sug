import json
import os

FILE = "todos.json"

# JSON файл унших
def load_todos():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# JSON файлд хадгалах
def save_todos(todos):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2, ensure_ascii=False)

# Таск нэмэх (category-тай)
def add_todo(title, category):
    todos = load_todos()
    todos.append({
        "title": title,
        "category": category,
        "done": False
    })
    save_todos(todos)
    print(f"📝 Таск нэмэгдлээ: {title} [{category}]")

# Таскуудыг жагсаах
def list_todos():
    todos = load_todos()
    if not todos:
        print("⛔ Одоогоор ямар ч таск байхгүй байна.")
        return
    print("\n📋 Таны таскууд:")
    for i, t in enumerate(todos, 1):
        status = "✅" if t["done"] else "🔲"
        print(f"{i}. {t['title']} ({t['category']}) {status}")

# Таск бөглөх (done болгож тэмдэглэх)
def complete_task(index):
    todos = load_todos()
    if 0 < index <= len(todos):
        if todos[index - 1]["done"]:
            print(f"⚠️ '{todos[index - 1]['title']}' аль хэдийн дууссан байна.")
        else:
            todos[index - 1]["done"] = True
            save_todos(todos)
            print(f"🎯 Таск бөглөгдлөө: {todos[index - 1]['title']}")
    else:
        print("⚠️ Ийм дугаар байхгүй байна!")

# Category-р шүүх
def list_by_category(category):
    todos = load_todos()
    filtered = [t for t in todos if t["category"].lower() == category.lower()]
    if not filtered:
        print(f"⛔ '{category}' ангилалд таск байхгүй байна.")
        return
    print(f"\n📚 '{category}' ангиллын таскууд:")
    for i, t in enumerate(filtered, 1):
        status = "✅" if t["done"] else "🔲"
        print(f"{i}. {t['title']} {status}")

# CLI
def main():
    print("🚀 TASK TRACKER (JSON хадгалалттай, CATEGORY-тэй)\n")
    while True:
        cmd = input(">>> Команд (add/list/done/filter/exit): ").strip().lower()

        if cmd == "add":
            title = input("  → Таскны нэр: ").strip()
            category = input("  → Ангилал (жишээ нь: ажил, сургалт, хувийн): ").strip()
            if title:
                add_todo(title, category or "Ерөнхий")
            else:
                print("⚠️ Нэр оруулна уу.")
        elif cmd == "list":
            list_todos()
        elif cmd == "done":
            try:
                n = int(input("  → Дугаар: "))
                complete_task(n)
            except ValueError:
                print("⚠️ Зөв дугаар оруул.")
        elif cmd == "filter":
            category = input("  → Аль ангиллыг харах вэ?: ").strip()
            list_by_category(category)
        elif cmd == "exit":
            print("👋 Гарлаа!")
            break
        else:
            print("⚙️ Командууд: add, list, done, filter, exit")

if __name__ == "__main__":
    main()
