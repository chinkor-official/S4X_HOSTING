"""
╔═══════════════════════════════════════════════════════════╗
║  🌟 APON HOSTING PANEL — Premium Edition v6.0 🌟         ║
║  Developer: @developer_apon                               ║
║  Config File — All Settings Here (No .env needed)         ║
╚═══════════════════════════════════════════════════════════╝
"""

import os

# ═══════════════════════════════════════════════════
#  BOT TOKENS
# ═══════════════════════════════════════════════════
TOKEN            = '8567624910:AAEHCu1KJnU1RdEQB36vBG_Cu4DYvxW-tv0'          # ← এখানে তোমার BOT_TOKEN দাও
ERROR_BOT_TOKEN  = ''          # ← Error bot token (optional)

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN is not set! TOKEN ভেরিয়েবলে টোকেন দাও।")

# ═══════════════════════════════════════════════════
#  MONGODB — PRIMARY + SECONDARY FALLBACK
# ═══════════════════════════════════════════════════
MONGO_URL         = ''         # ← Primary MongoDB URL
MONGO_URL_BACKUP  = ''         # ← Backup MongoDB URL (optional)
DB_NAME           = 'CHINKORHOSTINGROBOT'

DB_STORAGE_WARN_MB  = 400
DB_STORAGE_LIMIT_MB = 490

# ═══════════════════════════════════════════════════
#  OWNER & ADMIN
# ═══════════════════════════════════════════════════
OWNER_ID       = 7112632356             # ← তোমার Telegram User ID দাও
ADMIN_ID       = 7112632356
BOT_USERNAME   = 'CHINKORHOSTINGROBOT'
YOUR_USERNAME  = '@chinkor'
UPDATE_CHANNEL = 'https://t.me/ChinkorTCP'

# ═══════════════════════════════════════════════════
#  DIRECTORIES
# ═══════════════════════════════════════════════════
BASE_DIR   = os.path.abspath(os.path.dirname(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'upload_bots')
DATA_DIR   = os.path.join(BASE_DIR, 'apon_data')
LOGS_DIR   = os.path.join(BASE_DIR, 'logs')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

for _d in [UPLOAD_DIR, DATA_DIR, LOGS_DIR, BACKUP_DIR]:
    os.makedirs(_d, exist_ok=True)

# ═══════════════════════════════════════════════════
#  BRANDING
# ═══════════════════════════════════════════════════
BRAND        = "🌟CHINKOR HOSTING PANEL"
BRAND_SHORT  = "SBHP"
BRAND_VER    = "v6.0"
BRAND_TAG    = f"{BRAND} {BRAND_VER}"
BRAND_FOOTER = f"\n━━━━━━━━━━━━━━━━━━━━\n{BRAND_TAG}"

# ═══════════════════════════════════════════════════
#  FORCE SUBSCRIBE
# ═══════════════════════════════════════════════════
DEFAULT_FORCE_CHANNELS = {'ChinkorTCP': 'bot Updates'}

# ═══════════════════════════════════════════════════
#  PLAN LIMITS
# ═══════════════════════════════════════════════════
PLAN_LIMITS = {
    'free':       {'name': '🆓 Free',        'max_bots': 1,  'ram': 128,  'auto_restart': False, 'price': 0},
    'starter':    {'name': '🟢 Starter',     'max_bots': 2,  'ram': 256,  'auto_restart': True,  'price': 99},
    'basic':      {'name': '⭐ Basic',        'max_bots': 5,  'ram': 512,  'auto_restart': True,  'price': 199},
    'pro':        {'name': '💎 Pro',          'max_bots': 15, 'ram': 2048, 'auto_restart': True,  'price': 499},
    'enterprise': {'name': '🏢 Enterprise',   'max_bots': 50, 'ram': 4096, 'auto_restart': True,  'price': 999},
    'lifetime':   {'name': '👑 Lifetime',     'max_bots': -1, 'ram': 8192, 'auto_restart': True,  'price': 1999},
}

# ═══════════════════════════════════════════════════
#  PAYMENT METHODS
# ═══════════════════════════════════════════════════
PAYMENT_METHODS = {
    'bkash':   {'name': 'bKash',       'number': '01833221665',            'type': 'Send Money',       'icon': '🟪'},
    'nagad':   {'name': 'Nagad',       'number': '01833221665',            'type': 'Send Money',       'icon': '🟧'},
    'binance': {'name': 'Binance Pay', 'number': 'Binance ID: 936118119', 'type': 'Binance Pay/USDT', 'icon': '🟡'},
}

# ═══════════════════════════════════════════════════
#  REFERRAL SETTINGS
# ═══════════════════════════════════════════════════
REF_BONUS_DAYS = 3
REF_COMMISSION = 20

# ═══════════════════════════════════════════════════
#  MODULE MAP (for auto-install)
# ═══════════════════════════════════════════════════
MODULES_MAP = {
    'telebot': 'pytelegrambotapi', 'telegram': 'python-telegram-bot',
    'pyrogram': 'pyrogram', 'telethon': 'telethon', 'aiogram': 'aiogram',
    'PIL': 'Pillow', 'cv2': 'opencv-python', 'sklearn': 'scikit-learn',
    'bs4': 'beautifulsoup4', 'dotenv': 'python-dotenv', 'yaml': 'pyyaml',
    'aiohttp': 'aiohttp', 'numpy': 'numpy', 'pandas': 'pandas',
    'requests': 'requests', 'flask': 'flask', 'fastapi': 'fastapi',
    'motor': 'motor', 'pymongo': 'pymongo', 'httpx': 'httpx',
    'cryptography': 'cryptography',
}

# ═══════════════════════════════════════════════════
#  FLASK PORT
# ═══════════════════════════════════════════════════
FLASK_PORT = 5000

# ═══════════════════════════════════════════════════
#  DAILY REPORT
# ═══════════════════════════════════════════════════
DAILY_REPORT_HOUR   = 0
DAILY_REPORT_MINUTE = 0

# ═══════════════════════════════════════════════════
#  FREE PLAN BOT LIMIT
# ═══════════════════════════════════════════════════
FREE_BOT_MAX_HOURS  = 24

#
