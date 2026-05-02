import sqlite3

from hero.hero import Hero


def init_db():
    conn = sqlite3.connect('game_save.db')
    cur = conn.cursor()

    #TABLE FOR WEAPONS
    cur.execute('CREATE TABLE IF NOT EXISTS weapons (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,damage INTEGER)')

    #TABLE FOR HERO STATS
    cur.execute("CREATE TABLE IF NOT EXISTS player(id INTEGER PRIMARY KEY,pl_level INTEGER,pl_hp INTEGER,pl_name TEXT,pl_base_damage INTEGER,pl_xp INTEGER)")

    conn.commit()
    conn.close()


def save_game(hero: Hero):
    conn = sqlite3.connect('game_save.db')
    cur = conn.cursor()

    # cur.execute('''
    #     INSERT OR REPLACE INTO weapons (name, damage) VALUES (?,?)
    # ''')

    # Using 'REPLACE' makes it overwrite the old save for 'Player 1'
    cur.execute('''
        INSERT OR REPLACE INTO player (id, pl_level, pl_hp, pl_name, pl_base_damage, pl_xp)
        VALUES (1, ?, ?, ?, ?, ?)
    ''', (hero.level, hero.hp, hero.name, hero.base_dmg, hero.xp ))

    conn.commit()
    conn.close()
    print("Game saved successfully!")


def load_game():
    conn = sqlite3.connect('game_save.db')
    cursor = conn.cursor()

    cursor.execute('SELECT  pl_level, pl_hp, pl_name, pl_base_damage, pl_xp FROM player WHERE id = 1')
    data = cursor.fetchone()

    conn.close()
    return data