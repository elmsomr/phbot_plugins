#  phBot Plugins Collection

A personal collection of useful and lightweight plugins for **phBot** — the powerful Silkroad Online botting tool. These plugins enhance automation, notifications, inventory management and more.

>  Compatible with **phBot Testing** (v31+) and Python 3.9–3.10.

---

##  Included Plugins

### [`telegram_notify.py`](./telegram_notify.py)
>  **Send Telegram notifications when your bot connects, disconnects, joins the game or updates party status.**

- Real-time alerts from your bot to your phone
- Easy setup using [@BotFather](https://t.me/BotFather) and [@userinfobot](https://t.me/userinfobot)
- Works on Windows Server or desktop phBot setups
- Integrated with phBot Plugins tab

 [Read Setup Guide →](./telegram_notify.md)

---

##  How to Use

1. Download or clone this repository:
```bash
git clone https://github.com/elmsomr/phbot_plugins.git
```

2. Copy the `.py` files into your phBot `Plugins/` directory.

3. Launch **phBot**, go to the **Plugins** tab, and enable the plugin(s) you want.

4. Configure each plugin as needed (usually by editing the `.py` file directly).

---

##  Requirements

- Python **3.9.x or 3.10.x** (⚠️ Newer versions like 3.13 may break compatibility)
- Windows 10 or Server 2019+ recommended
- phBot Testing or Stable version
- `requests` Python module (used by `telegram_notify`)

```bash
pip install requests
```

---

##  Suggestions & Contributions
Have an idea for a new plugin? Found a bug? Feel free to open an issue or submit a pull request and if you found this project helpful, don't forget to give it a star rating.

---
