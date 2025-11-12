# 🎨 **Terminal Text Styler**

A **Python-based terminal color and style customizer** that lets you create vibrant, styled text directly in your terminal using **ANSI escape sequences**.  
Easily choose **foreground**, **background**, and **font styles** interactively — and watch your text transform in real time! ⚡  

---

## 🌟 **Features**

✅ **Interactive Menus** — Step-by-step selection for color and font style.  
✅ **Live Preview** — Instantly see your text update with new styles.  
✅ **7 Foreground & Background Colors** — 🎨  
✅ **Font Styles:** Bold, Italic, Underline.  
✅ **Loop Until You’re Happy** — Adjust endlessly until your design is perfect.  

---


---

## 🎨 **Supported Colors**

| 🎨 Color Name | 🔢 Code | ANSI Example | Preview |
|:--------------|:---------:|:--------------|:----------:|
| 🔵 **Blue** | `34` | `\033[34m` | 🟦 |
| 🔴 **Red** | `31` | `\033[31m` | 🟥 |
| 🟢 **Green** | `32` | `\033[32m` | 🟩 |
| 🟡 **Yellow** | `33` | `\033[33m` | 🟨 |
| 🟣 **Magenta** | `35` | `\033[35m` | 🟪 |
| 🩵 **Cyan** | `36` | `\033[36m` | 🩵 |
| ⚪ **White** | `37` | `\033[37m` | ⬜ |

---

## ✍️ **Font Styles**

| ✨ Style | Code | Example |
|:----------|:------:|:------------|
| **Bold** | `\033[1m` | **Bold Text** |
| *Italic* | `\033[3m` | *Italic Text* |
| <u>Underline</u> | `\033[4m` | Underlined Text |

---

## ⚙️ **How It Works**

1️⃣ The program greets you with an ASCII banner.  
2️⃣ You enter the text you want to style.  
3️⃣ Then you:  
   - Choose a **foreground color (FG)**  
   - Choose a **background color (BG)**  
   - Pick a **font style** (bold/italic/etc.)  
4️⃣ The text is displayed with your selected combination.  
5️⃣ You can repeat until you finalize your perfect style.

---

## 🚀 **Usage Instructions**

### 🧩 Step 1: Clone or Download
```bash
git clone https://github.com/yourusername/terminal-text-styler.git
cd terminal-text-styler
