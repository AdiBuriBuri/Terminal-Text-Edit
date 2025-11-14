# 🎨 **Terminal Text Styler**

A **Python-based terminal color and style customizer** that lets you create vibrant, styled text directly in your terminal using **ANSI escape sequences**.  
Easily choose **foreground**, **background**, and **font styles** interactively — and watch your text transform in real time! ⚡

---

## 🌟 **Features**

✅ **Interactive Menus** — Step-by-step selection for color and font style  
✅ **Live Preview** — Instantly see your text update with new styles  
✅ **7 Foreground & Background Colors** — Choose from a vibrant palette  
✅ **Font Styles** — Bold, Italic, Underline  
✅ **Loop Until You're Happy** — Adjust endlessly until your design is perfect

---

## 🎨 **Supported Colors**

| 🎨 Color Name | 🔢 Code | ANSI Example | Preview |
|:--------------|:-------:|:-------------|:-------:|
| 🔵 **Blue**   | `34`    | `\033[34m`   | 🟦      |
| 🔴 **Red**    | `31`    | `\033[31m`   | 🟥      |
| 🟢 **Green**  | `32`    | `\033[32m`   | 🟩      |
| 🟡 **Yellow** | `33`    | `\033[33m`   | 🟨      |
| 🟣 **Magenta**| `35`    | `\033[35m`   | 🟪      |
| 🔵 **Cyan**   | `36`    | `\033[36m`   | 🟦      |
| ⚪ **White**  | `37`    | `\033[37m`   | ⬜      |

---

## ✍️ **Font Styles**

| ✨ Style        | Code        | Example           |
|:----------------|:-----------:|:------------------|
| **Bold**        | `\033[1m`   | **Bold Text**     |
| *Italic*        | `\033[3m`   | *Italic Text*     |
| <u>Underline</u>| `\033[4m`   | Underlined Text   |

---

## ⚙️ **How It Works**

1️⃣ The program greets you with an ASCII banner  
2️⃣ You enter the text you want to style  
3️⃣ Then you:  
   - Choose a **foreground color (FG)**  
   - Choose a **background color (BG)**  
   - Pick a **font style** (bold/italic/underline)  
   - The text is displayed with your selected combination  
   - You can repeat until you finalize your perfect style

---

## 🚀 **Usage Instructions**

### 📋 **Prerequisites**

Before running the Terminal Text Styler, ensure you have Python installed on your system.

#### **Check if Python is installed:**
```bash
python --version
```
or
```bash
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

- **Windows**: Download the installer and check "Add Python to PATH" during installation
- **macOS**: Python 3 comes pre-installed, or install via Homebrew: `brew install python3`
- **Linux**: Install via package manager: `sudo apt install python3` (Ubuntu/Debian)

---

### 🧩 **Step 1: Clone or Download**

```bash
git clone https://github.com/AdiBuriBuri/Terminal-Text-Styler.git
cd Terminal-Text-Styler
```

**Alternative**: Download the ZIP file from GitHub and extract it.

---

### 🧩 **Step 2: Navigate to Project Directory**

```bash
cd Terminal-Text-Styler
```

---

### 🧩 **Step 3: Run the Program**

#### **On Windows:**
```bash
python terminal_styler.py
```

#### **On macOS/Linux:**
```bash
python3 terminal_styler.py
```

---

### 🧩 **Step 4: Follow the Interactive Prompts**

1. Enter your text when prompted
2. Select a foreground color (1-7)
3. Select a background color (1-7)
4. Choose a font style (1-3)
5. View your styled text!
6. Type `yes` to try another style or `no` to exit

---

## 📸 **Example Output**

```
╔═══════════════════════════════════════╗
║   🎨 TERMINAL TEXT STYLER 🎨         ║
╚═══════════════════════════════════════╝

Enter text to style: Hello World!

Choose Foreground Color:
1. Blue  2. Red  3. Green  4. Yellow  5. Magenta  6. Cyan  7. White
Enter choice: 1

Choose Background Color:
1. Blue  2. Red  3. Green  4. Yellow  5. Magenta  6. Cyan  7. White
Enter choice: 7

Choose Font Style:
1. Bold  2. Italic  3. Underline
Enter choice: 1

✨ Your Styled Text: [Bold Blue text on White background] Hello World!
```

---

## 🛠️ **Troubleshooting**

### **Colors not displaying properly?**
- Some terminals have limited ANSI support (older Windows CMD)
- Try using Windows Terminal, PowerShell, or Git Bash on Windows
- Most modern terminals on macOS and Linux support full ANSI colors

### **"Python not recognized" error?**
- Ensure Python is added to your system PATH
- Reinstall Python and check "Add to PATH" option

---

## 📝 **License**

This project is open-source and available under the MIT License.

---

## 💡 **Contributing**

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 👨‍💻 **Author**

Created with ❤️ by **AdiBuriBuri**

**GitHub**: [github.com/AdiBuriBuri](https://github.com/AdiBuriBuri)

---

## 🌟 **Star this repo if you found it helpful!**

Give it a ⭐ on GitHub to show your support!
