# telegram_bot.py

import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- IMPORT YOUR GATEWAY FUNCTIONS ---
# This script assumes your functions are in a file named gates.py
try:
    import gates
except ImportError:
    print("ERROR: Could not import 'gates.py'. Make sure it's in the same directory.")
    exit()

# --- CONFIGURATION ---
BOT_TOKEN = '7879139068:AAFOhOXb3fW4GVY05-denGDreUMrsjjdEow'

# --- LOGGING SETUP ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# --- GENERIC HANDLER LOGIC (UPDATED) ---
async def handle_command(gate_function: callable, update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Generic handler that first sends a "Processing" message, runs the gate
    function, and then edits the original message with the result.
    """
    if not context.args:
        command_name = update.message.text.split(' ')[0]
        await update.message.reply_text(
            f"⚠️ Please provide an input for the `{command_name}` command.\n\n"
            f"*Example:* `{command_name} 4242...|12|25|123`",
            parse_mode='MarkdownV2'
        )
        return

    # 1. Send an initial "Processing" message and store it
    processing_message = await update.message.reply_text("⏳ Processing your request... please wait.")

    user_input = " ".join(context.args)
    
    try:
        # 2. Run the synchronous (blocking) gateway function in a separate thread
        result = await asyncio.to_thread(gate_function, user_input)
        response_message = str(result)
        
        # 3. Edit the original message with the success result
        await processing_message.edit_text(
            f"✅ **Success!**\n\n**Result:**\n`{response_message}`", 
            parse_mode='Markdown'
        )

    except Exception as e:
        logger.error(f"Error executing {gate_function.__name__}: {e}", exc_info=True)
        # 3. Edit the original message with the error details
        await processing_message.edit_text(
            f"❌ **Error!**\n\n**Details:**\n`{e}`", 
            parse_mode='Markdown'
        )


# --- COMMAND HANDLERS (Generated from gates.py) ---
# Each function below is a specific handler for a command.

async def vip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.vip, update, context)

async def stc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.stc, update, context)
    
async def pay_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.pay, update, context)

async def sa_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.sa, update, context)

async def xc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.xc, update, context)

async def sf_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.sf, update, context)

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.info, update, context)

async def sd_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.sd, update, context)

async def scc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.scc, update, context)

async def sh_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.sh, update, context)

async def pv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.pv, update, context)

async def vbv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.vbv, update, context)

async def br_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.br, update, context)
    
async def brr_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.brr, update, context)

async def be_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.be, update, context)

async def sff_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.sff, update, context)

async def b3_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.b3, update, context)

async def cvv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.cvv, update, context)

async def auth_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.auth, update, context)
    
async def gg_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.gg, update, context)
    
async def sq_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.sq, update, context)

async def au_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.au, update, context)
    
async def cn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.cn, update, context)

async def sv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.sv, update, context)

async def pro_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.pro, update, context)
    
async def x_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_command(gates.x, update, context)

async def generate_fake_address_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Special handler for the address generator which takes no arguments."""
    processing_message = await update.message.reply_text("⏳ Generating fake address...")
    try:
        result = await asyncio.to_thread(gates.generate_fake_address)
        response_message = "\n".join([f"{key}: {value}" for key, value in result.items()])
        await processing_message.edit_text(f"✅ Generated Address:\n\n`{response_message}`", parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Error executing generate_fake_address: {e}", exc_info=True)
        await processing_message.edit_text(f"❌ An error occurred: {e}")
        
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message with a list of available commands."""
    await update.message.reply_text(
        "Welcome! The following commands are available:\n\n"
        "/vip, /stc, /pay, /sa, /xc, /sf, /info, /sd, /scc, "
        "/sh, /pv, /vbv, /br, /brr, /be, /sff, /b3, /cvv, "
        "/auth, /gg, /sq, /au, /cn, /sv, /pro, /x, /generate_fake_address"
    )

def main() -> None:
    """Starts the bot and registers all the command handlers."""
    application = Application.builder().token(BOT_TOKEN).build()
    
    logger.info("Registering commands...")
    
    # Add all command handlers
    handlers = [
        CommandHandler("start", start),
        CommandHandler("vip", vip_command),
        CommandHandler("stc", stc_command),
        CommandHandler("pay", pay_command),
        CommandHandler("sa", sa_command),
        CommandHandler("xc", xc_command),
        CommandHandler("sf", sf_command),
        CommandHandler("info", info_command),
        CommandHandler("sd", sd_command),
        CommandHandler("scc", scc_command),
        CommandHandler("sh", sh_command),
        CommandHandler("pv", pv_command),
        CommandHandler("vbv", vbv_command),
        CommandHandler("br", br_command),
        CommandHandler("brr", brr_command),
        CommandHandler("be", be_command),
        CommandHandler("sff", sff_command),
        CommandHandler("b3", b3_command),
        CommandHandler("cvv", cvv_command),
        CommandHandler("auth", auth_command),
        CommandHandler("gg", gg_command),
        CommandHandler("sq", sq_command),
        CommandHandler("au", au_command),
        CommandHandler("cn", cn_command),
        CommandHandler("sv", sv_command),
        CommandHandler("pro", pro_command),
        CommandHandler("x", x_command),
        CommandHandler("generate_fake_address", generate_fake_address_command)
    ]
    application.add_handlers(handlers)
    
    logger.info("All commands registered. Starting bot...")
    application.run_polling()

if __name__ == "__main__":
    main()
