def get_faction_colors(clan_tag):
#add clan colours here
    if clan_tag == "WGWM":
        return (0, 255, 0) 
    elif clan_tag == "Jims":
        return (0, 0, 255)
    else:
        return (255, 255, 255)

#this here tells server to spawn in dem colors G 
def on_player_spawn(player):
    faction_colors = get_faction_colors(player.clan.tag)
    player.faction.set_colors(faction_colors)
