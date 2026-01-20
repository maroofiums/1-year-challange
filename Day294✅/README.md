# Day294

## 🧠 Git kya hai? (Simple words)

**Git = Version Control System**

Matlab:

* Tumhara **code ka history** rakhta hai
* Galti ho jaye → **wapis ja sakte ho**
* Team ke sath kaam → **conflict ke baghair**

💡 Socho Git ek **Time Machine for code** hai ⏪⏩

---

## 🔥 Git vs GitHub (Important confusion clear)

| Git                     | GitHub                   |
| ----------------------- | ------------------------ |
| Tool / software         | Website                  |
| Local machine pe chalta | Online code store        |
| History track karta     | Code share & collaborate |

👉 **Git seekhna = must**
👉 **GitHub = Git ka playground**

---

## 🛠️ Step 1: Git install karo

Check karo:

```bash
git --version
```

Agar version aa jaye → ✅ ready
Nahi aaye → git-scm.com se install

---

## 🧩 Step 2: Git ko apna naam batao (one-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
```

🧠 Git commits pe ye naam/email lagata hai (history ke liye)

---

## 📁 Step 3: Project ko Git repo banao

```bash
git init
```

📌 Iska matlab:

> “Is folder ka history track karo”

Hidden `.git` folder ban jata hai (kabhi delete mat karna ❌)

---

## 📊 Step 4: Git status (MOST USED command)

```bash
git status
```

Ye batata hai:

* Kaun si files new hain
* Kaun si modified hain
* Kaun si commit ke liye ready hain

🧠 **Rule:** Har kaam se pehle `git status`

---

## ➕ Step 5: Files ko stage karo

```bash
git add file.py
```

Ya sab:

```bash
git add .
```

🎯 Staging = “Git, is change ko yaad rakhna”

---

## 🧱 Step 6: Commit (Snapshot lo)

```bash
git commit -m "Added login logic"
```

📸 Commit = **photo of your code at that moment**

💡 Best practice:

* Short
* Clear
* Verb se start (“Add”, “Fix”, “Update”)

---

## 🕰️ Step 7: History dekho

```bash
git log
```

Tum dekh sakte ho:

* Kis ne kya change kiya
* Kab kiya
* Commit message

---

## 🔄 Daily Git Workflow (Yaad rakhna)

```text
Code likho
↓
git status
↓
git add .
↓
git commit -m "message"
```

---

## 🌿 Step 8: Branch kya hoti hai?

Branch = **parallel universe 🌍**

Example:

* `main` → stable code
* `feature-login` → new feature testing

Commands:

```bash
git branch
git branch feature-login
git checkout feature-login
```

Shortcut:

```bash
git checkout -b feature-login
```

💡 **Golden rule:** New feature = new branch

---

## 🔀 Step 9: Merge (branch ko main mein lao)

```bash
git checkout main
git merge feature-login
```

🧠 Git automatically changes combine karta hai
Conflict aaye → manually fix karna hota hai

---

## 🌍 Step 10: GitHub se connect (real world)

```bash
git remote add origin https://github.com/user/repo.git
git push -u origin main
```

Ab tumhara code:

* Online safe
* Shareable
* Portfolio ready 💼

---

## ⚠️ Common mistakes (avoid these)

❌ Commit without message
❌ Big commits (100 changes ek sath)
❌ `.git` folder delete karna
❌ Direct `main` pe kaam (team mein)

---

## ✅ Best Practices (Pro tips)

✔ Small commits
✔ Clear messages
✔ Branch per feature
✔ `git status` habit
✔ `.gitignore` use karo (next topic)

---

## 🧠 Quick Summary

* Git = code history manager
* Commit = snapshot
* Branch = safe experimentation
* GitHub = online storage
