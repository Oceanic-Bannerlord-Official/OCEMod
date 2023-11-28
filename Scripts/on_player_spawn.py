#this here tells server to spawn in dem colors G 
def on_player_spawn(player):
    # Get the player's clan tag
    clan_tag = player.clan.tag

    # Determine the faction colors based on the clan tag
    faction_colors = get_faction_colors(clan_tag)

    # Set the player's faction colors
    player.faction.set_colors(faction_colors)
