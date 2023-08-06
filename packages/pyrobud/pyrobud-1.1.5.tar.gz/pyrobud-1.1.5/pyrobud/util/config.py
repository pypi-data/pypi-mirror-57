import logging
import os

import plyvel
import toml

from .db import AsyncDB
from .time import sec as now_sec

log = logging.getLogger("migrate")


def save(config, path):
    tmp_path = path + ".tmp"

    try:
        with open(tmp_path, "w+") as f:
            toml.dump(config, f)
            f.flush()
            os.fsync(f.fileno())

        os.rename(tmp_path, path)
    except:
        os.remove(tmp_path)
        raise


def upgrade_v2(config, path):
    tg_config = config["telegram"]

    if "session_name" not in tg_config:
        log.info("Adding default session name 'main' to Telegram config section")
        tg_config["session_name"] = "main"

        if os.path.exists("anon.session"):
            log.info("Renaming 'anon' session to 'main'")
            os.rename("anon.session", "main.session")
        if os.path.exists("anon.session-journal"):
            os.rename("anon.session-journal", "main.session-journal")


def upgrade_v3(config, path):
    def migrate_antibot(config, db):
        if "antibot" in config:
            log.info("Migrating antibot settings to database")
            mcfg = config["antibot"]
            mdb = db.prefixed_db("antibot.")

            if mcfg["threshold_time"] != 30:
                mdb.put_sync("threshold_time", mcfg["threshold_time"])

            group_db = mdb.prefixed_db("groups.")
            for gid in mcfg["group_ids"]:
                group_db.put_sync(f"{gid}.enabled", True)
                group_db.put_sync(f"{gid}.enable_time", now_sec())

            del config["antibot"]

    def migrate_snippets(config, db):
        if "snippets" in config:
            log.info("Migrating snippets to database")
            mdb = db.prefixed_db("snippets.")

            for snip, repl in config["snippets"].items():
                mdb.put_sync(snip, repl)

            del config["snippets"]

    def migrate_stats(config, db):
        if "stats" in config:
            log.info("Migrating stats to database")
            mdb = db.prefixed_db("stats.")

            for stat, value in config["stats"].items():
                mdb.put_sync(stat, value)

            del config["stats"]

    def migrate_stickers(config, db):
        if "stickers" in config:
            log.info("Migrating stickers to database")
            mdb = db.prefixed_db("stickers.")

            for sticker, value in config["stickers"].items():
                mdb.put_sync(sticker, value)

            del config["stickers"]

        if "user" in config:
            log.info("Migrating sticker settings to database")
            mcfg = config["user"]
            mdb = db.prefixed_db("sticker_settings.")

            if "kang_pack" in mcfg:
                mdb.put_sync("kang_pack", mcfg["kang_pack"])

            del config["user"]

    bot_config = config["bot"]

    if "default_prefix" not in bot_config:
        log.info("Renaming 'prefix' key to 'default_prefix' in bot config section")
        bot_config["default_prefix"] = bot_config["prefix"]
        del bot_config["prefix"]

    if "db_path" not in bot_config:
        log.info("Adding default database path 'main.db' to bot config section")
        bot_config["db_path"] = "main.db"

    with AsyncDB(plyvel.DB(config["bot"]["db_path"], create_if_missing=True)) as db:
        migrate_antibot(config, db)
        migrate_snippets(config, db)
        migrate_stats(config, db)
        migrate_stickers(config, db)


def upgrade_v4(config, path):
    bot_config = config["bot"]

    if "report_errors" not in bot_config:
        log.info("Enabling error reporting by default without usernames")
        log.info("Please consider enabling report_username if you're comfortable with it!")
        bot_config["report_errors"] = True
        bot_config["report_username"] = False


def upgrade_v5(config, path):
    bot_config = config["bot"]

    if "sentry_dsn" not in bot_config:
        log.info("Adding default Sentry DSN to bot config section")
        bot_config["sentry_dsn"] = ""


def upgrade_v6(config, path):
    bot_config = config["bot"]

    if "response_mode" not in bot_config:
        log.info("Setting response mode to default 'edit'")
        bot_config["response_mode"] = "edit"


# Old version -> function to perform migration to new version
upgrade_funcs = [
    upgrade_v2,  # 1 -> 2
    upgrade_v3,  # 2 -> 3
    upgrade_v4,  # 3 -> 4
    upgrade_v5,  # 4 -> 5
    upgrade_v6,  # 5 -> 6
]

# Master upgrade function
def upgrade(config, path):
    # Get current version
    if "version" in config:
        cur_version = config["version"]
    else:
        cur_version = 1

    # Already at latest version; nothing to do
    if cur_version == len(upgrade_funcs) - 1:
        return

    # Upgrade each version sequentially
    for upgrader in upgrade_funcs[cur_version - 1 :]:
        target_version = cur_version + 1
        log.info(f"Upgrading config to version {target_version}")
        upgrader(config, path)
        config["version"] = target_version

        # Save config ASAP to prevent an inconsistent state if the next upgrade fails
        save(config, path)
