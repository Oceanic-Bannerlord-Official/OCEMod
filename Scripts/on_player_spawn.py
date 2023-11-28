#this here tells server to spawn in dem colors G 
def on_player_spawn(player):
    faction_colors = get_faction_colors(player.clan.tag)
    player.faction.set_colors(faction_colors)
