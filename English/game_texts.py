item_descriptions = {'raw meat': 'Restores 1 Ftg or can be cooked.',
                     'cooked meat': 'Restores 2 Ftg.',
                     'well cooked meat': 'Restores 3 Ftg.',
                     'raw fish': 'Restores 1 HP or can be cooked.',
                     'cooked fish': 'Restores 2 HP.',
                     'well cooked fish': 'Restores 3 HP.',
                     'fruit': 'Restores 1 HP and 1 Ftg.',
                     'vegetables': 'Running away from combat fatigue is halved for 2 rounds (rounded down).',
                     'cognifruit': 'A vibrant blue fruit that boosts critical thinking by 1 point for 2 rounds.',
                     'haggleroot': 'A gnarled root that boosts haggling by 1 point for 2 rounds.',
                     'swayleaf': 'A delicate plant that boosts persuasion by 1 point for 2 rounds.',
                     'handiherb': "A versatile herb that boosts crafting by 1 point for 2 rounds.",
                     'blazeberry': "A small, fiery-red berry that boosts heating by 1 point for 2 rounds.",
                     'forgeflower': "A metallic-sheen bloom that boosts smithing by 1 point for 2 rounds.",
                     'cloakmoss': "A dark, velvety moss that boosts stealth by 1 point for 2 rounds.",
                     'vitalvine': "A robust vine that boosts survival by 1 point for 2 rounds.",
                     'pluckpetal': "A bright flower that boosts gathering by 1 point for 2 rounds.",
                     'findersfern': "A lush fern that boosts excavating by 1 point for 2 rounds.",
                     'elixir of feasting': "Any food you gather instantly gets heated into well cooked for 5 rounds.",
                     'elixir of cognition': "Any critical thinking success chance is 100% for 3 rounds.",
                     'elixir of vigor': "No fatigue or HP damage taken for 5 rounds (except combat).",
                     'elixir of shadow': "Stealth success and sneak attack chance is 100% for 5 rounds.",
                     'elixir of forging': "Can smith any ore for 2 rounds.",
                     'elixir of abundancy': "Market sells all items for 3 rounds.",
                     'elixir of merchants': "Can successfully sell any item in your market for 2 rounds.",
                     'elixir of retention': "Retain most valuable item from craft when sold for 2 rounds.",
                     'elixir of certainty': "Can excavate 3 of any item 100% of the time for 2 rounds.",
                     'elixir of harvest': "Can gather 3 of any crop 100% of the time for 2 rounds. Gathering does not deplete tile.",
                     'string': 'Basic crafting material.',
                     'beads': 'Basic crafting material.',
                     'hide': 'Can be heated into leather (Lv 5 Heating).',
                     'sand': 'Can be heated into glass (Lv 9 Heating).',
                     'clay': 'Can be heated into ceramic (Lv 6 Heating).',
                     'scales': 'Shiny craft material, can be used at Tamarania as enchant material.',
                     'leather': 'Tough craft material, can be used at Tamarania as enchant material.',
                     'bark': 'Tough craft material that can be heated into rubber (Lv 12 Heating), or used as enchant material.',
                     'ceramic': 'Fragile craft material, can be used at Tamarania as enchant material.',
                     'glass': 'Fragile craft material, can be used at Tamarania as enchant material.',
                     'rubber': 'Tough craft material, can be used at Tamarania as enchant material.',
                     'gems': 'Valuable trading and craft item, can be used at Tamarania as enchant material.',
                     'napsack': f'Gives you +1 rest on emptied tiles. Can be crafted with leather and string (Lv 3 Crafting). Destroyed after {napsack_life} uses.',
                     'lead': 'Rank 1 ore with elemental properties.',
                     'tin': 'Rank 1 ore with physical properties.',
                     'copper': 'Rank 1 ore with trooper properties.',
                     'iron': 'Rank 1 ore with wizard propterties.',
                     'tantalum': 'Rank 2 ore with elemental properties (Lv 4 Smithing).',
                     'aluminum': 'Rank 2 ore with physical properties (Lv 4 Smithing).',
                     'kevlium': 'Rank 2 ore with trooper properties (Lv 4 Smithing).',
                     'nickel': 'Rank 2 ore with wizard properties (Lv 4 Smithing).',
                     'tungsten': 'Rank 3 ore with elemental properties (Lv 7 Smithing).',
                     'titanium': 'Rank 3 ore with physical properties (Lv 7 Smithing).',
                     'diamond': 'Rank 3 ore with trooper properties (Lv 7 Smithing).',
                     'chromium': 'Rank 3 ore with wizard properties (Lv 7 Smithing).',
                     'shinopsis': 'Rank 4 ore with elemental properties (Lv 10 Smithing).',
                     'ebony': 'Rank 4 ore with physical properties (Lv 10 Smithing).',
                     'astatine': 'Rank 4 ore with trooper properties (Lv 10 Smithing).',
                     'promethium': 'Rank 4 ore with wizard properties (Lv 10 Smithing).',
                     'cooling cubes': 'Used by smithers to control heat.',
                     'lost gold': 'A well trained smith can make something useful with this.',
                     'bedrock': 'A rare ore with properties that enable enchantment.',
                     'meteorite': 'A rare ore with properties that enable enchantment.',
                     'living stone': 'A rare ore with properties that enable enchantment.',
                     'valuable item': 'An item that holds great sentimenal value.',
                     'rare artifact': 'There seems to be ancient magical properties contained within.',
                     'water sword': 'An elegant blade imbued with the essence of water.',
                     'air sword': 'Shimmers and blurs slightly, giving the impression that it’s constantly in motion.',
                     'earth sword': 'Heavy, powerful presence, as if it was carved from the very bedrock of the earth.',
                     'fire sword': 'Enveloped in a faint, fiery aura, making it look as though it’s constantly burning.',
                     'ice sword': 'Emits a cold mist, giving the impression that it’s perpetually covered in frost.',
                     'light sword': 'Glows with an ethereal aura, giving it a powerful and blinding presence.',
                     'blood sword': 'Seems to drip with dark energy, giving it a menacing and fearsome presence.',
                     'death sword': 'Shrouded in a faint, dark mist, giving it an ethereal and otherworldly presence.'}
for book in gameItems['Knowledge Books']:
    item_descriptions[book] = f'Successful reading grants xp to your {" ".join(book.split(" ")[:-1])} skill.'
for book in gameItems['GrandLibrary']:
    item_descriptions[book] = 'Loaned out by the Benfriege Grand Library. There is no return date.'
item_descriptions['learned library book'] = 'Return this book to the Benfriege Grand Library.'
for fragment in gameItems['Fragment']:
    item_descriptions[fragment] = 'By itself, has no useful properties, but Starfex may reward you for donating it and make them more useful later.'
    
clothSpecials = {'benfriege cloth':{'zinzibar','glaser','enfeir','starfex'},
                 'demetry cloth': {'benfriege', 'glaser'},
                 'enfeir cloth':{'benfriege','tutalu','pafiz'},
                 'glaser cloth':{'pafiz','fodker','benfriege','tutalu','scetcher'},
                 'kubani cloth': {'glaser', 'anafola', 'starfex'},
                 'pafiz cloth':{'zinzibar','glaser'},
                 'scetcher cloth':{'glaser'},
                 'starfex cloth':{'benfriege','tutalu','pafiz'},
                 'tamariza cloth':{'zinzibar', 'enfeir'},
                 'tutalu cloth':{'zinzibar','glaser','enfeir'},
                 'zinzibar cloth':{'benfriege', 'pafiz','fodker'},
                 'old fodker cloth':{'zinzibar','glaser'},
                 'old enfeir cloth':{'benfriege','tutalu','pafiz'},
                 'old zinzibar cloth':{'benfriege','pafiz','fodker'},
                 'luxurious cloth':{}}
for cloth in gameItems['Cloth']:
    city = cloth.split(' ')[0].title()
    if cloth == 'luxurious cloth':
        item_descriptions[cloth] = 'A luxurious cloth primarily for trading.'
    item_descriptions[cloth] = f'Good sell value in {", ".join(clothSpecials[cloth])}, or can be used in enchantment.'
for cloth in gameItems['Old Cloth']:
    city = cloth.split(' ')[1].title()
    item_descriptions[cloth] = f'Great sell value in {", ".join(clothSpecials[cloth])}, or can be used in enchantment.'    
    

connectpage_multiplayer_texts = {
                     'username_input': 'Input Username:',
                     'host_title': "Host Game", # Whether they wish to host the server for the game.
                     'connect_title': "Connect to Host", # Whether the player wishes to connect to an existing hosted game.
                     'ip_input': 'Input IP Address:', # If they do wish to connect, then provide the IP address they wish to connect to.
                     'port_input': 'Input Port:', # Also provide the port number.
                     'local_note': "{IP} (Local / Household Connection)",
                     'external_note': "{extIP} (External / Requires Port-Forwarding)",
                     'join': "Connect to Host", # This is the button that they click to then join the IP address and port to attempt connection to host.
                     'playLocally': "Host Game", # This is the button they click to trigger hosting of a game.
                     'local_ip': 'IP Addresses:', # Informational label that will tell them what their IP address is, if they choose to host their game locally, that they can give out to their friends to connect. It will also provide your external IP address.
                     'default_port': 'Default Port:', # The port that is chosen for them by default if they are hosting the game.
                     'connect_help': 'Share the info above to connect with people on your wifi (LAN)!' # Some instructional messaging that tells them what to do with this IP and Port number.
                     }
connectpage_singleplayer_texts = {
                     'username_input': 'Input Username:',
                     'host_title': "Single Player Game", # Prompts the user whether they are ready to continue to the next step in playing the game (choose settings before playing)
                     'playLocally': "Continue", # The button that continues them to the game settings launch page.
                     }
# Please translate the non-nested dictionary values (e.g. the 'message' key would be left alone but the value under message should be translated). Keep aptitude names unchanged (i.e. Combat, Knowledge, Fellowship), brackets that specify colors or text formatting (e.g. [i], [color]), and Parameters that have to be in that english format (e.g. Very Easy, Easy, etc). Keep in mind these will go into Kivy Label widget texts with markup=True. Please refer to comments to help to appropriately translate. Keep it english if the language uses the same english word to describe it. Also, when you translate, please ensure you do not accidently add repeated quotations accidently breaking the string.
launchpage_texts = {
    'readyButton': {
        'message': "Player with the highest total victory points (VP), when Game End is triggered, wins the game! We recommend single player for beginners and strategy testers."
    },
    'submitButton': {
        'message': "By clicking this button you send the modifications in the text box(es) above to the server and the rest of the lobby. You can also press [Enter] to submit changes."
    },
    'end_lbl': {
        'message': "This controls when game-end is triggered. Format is {a}:{vp}, where {a} is [i]minimum aptitudes[/i] and {vp} is [i]minimum VP[/i], e.g. 3:100 means you need at least 100 VP in 3 aptitudes to trigger game-end. {a} can also be an aptitude name. Multiple aptitudes are allowed too, e.g. Combat:30, Reputation:80" # Please clarify in the new language translation that aptitude names must be given in english.
    },
    'save_lbl': {
        'message': "The game is auto-saved at the start of every round under this save name."
    },
    'load_lbl': {
        'message': "If you have a saved file, you can enter its name here. The game will load at the start of the round you left at. All usernames must match with the load file."
    },
    'seed_lbl': {
        'message': "Controls the random placement of the board tiles. Must be an integer."
    },
    'npc_difficulty_lbl': {
        'message': 'Acceptable Parameters:\n[color=43dc00]Very Easy[/color], [color=438700]Easy[/color], [color=ffb700]Moderate[/color], [color=ff0700]Hard[/color], [color=850700]Very Hard[/color]\nControls foe dodge, block, and attack likelihood.'
    },
    'disable_warnings_lbl': {
        'message': 'Sometimes the game may output system warnings, like "low memory". You can toggle whether or not you want to see them.'
    },
    'logging_level_lbl': {
        'message': 'We only suggest changing this if you are a developer.'
    },
    'wide_screen_lbl': {
        'message': 'This game has been optimized to 1920x1080 screen resolution, which we detect your screen is not. If you set to full-screen then the game widget will stretch to fit, though, Wide-screen is safer for text-sizes. You can try manually changing to 1920x1080 to fix screen anomalies with this game.'
    },
    'auto_resize_lbl': {
        'message': 'Game will resize to use entire screen on launch if set to True. Otherwise you can keep it windowed if set to False. Please ensure to play on your primary monitor if auto-resizing.'
    },
    'localsettings': 'Local Settings', # This describes settings that change only your game.
    'extip': 'Cant Find (is this a Mac?)', # Meaning that their external IP could not be detected, most likely because of a certificate issue when calling the internet- this happens more often with a Mac.
    'save_is_same': 'It appears as though you did not change your save file name. Would you like to continue with the default?',
    'continue': 'Yes, Continue',
    'go back': 'No, Go Back',
    'current save': 'Current Save: ',
    'resize': 'Auto Resize',
    'auto_save': 'Auto Save', # Whether auto-save is on/off
    'wide': 'Resize Setting',
    'toggle': 'Toggle',
    'warning': 'Show Warnings',
    'show': 'Show',
    'disable': 'Disable',
    'false': 'False',
    'true': 'True',
    'wide-screen': 'Wide-Screen',
    'full-screen': 'Full-Screen',
    'resize to full-screen': 'Resize to Full-Screen',
    'resize to wide-screen': 'Resize to Wide-Screen',
    'logging_lvl': 'Logging Level',
    'info': 'Info', # Refers to info logging level
    'debug': 'Debug', # Refers to debug logging level
    'change2info': 'Change to Info', # Change to info level logging
    'change2debug': 'Change to Debug', # Change to debug level logging
    'globalsettings': 'Global Settings', # This describes settings that change the game for everyone.
    'multiplayernote': "[color=969696]Want to invite players to join? Give them your IP and ask them to 'Connect to Host'.\n\nNote: To connect to the world, you must enable port-forwarding and give them your external IP.[/color]", # Keep the markup format in original text.
    'ip_info': "(This is only visible to you, the Host)\nLocal IP: {socket_server.IP}\nExternal IP: {game_app.connect_page.formatter['extIP']}\nPORT: {socket_server.PORT}",
    'lobby': "Lobby", # The usernames go under the lobby.
    'ready': 'Ready', # The player is ready to play.
    'notready': 'Not Ready', # The player is not ready to play.
    'notconnected': 'WARNING: Not Connected!', # Something went wrong when attempting to connect to the host.
    'change': 'Request Changes', # Apply global settings changes to the rest of the lobby.
    'single player': 'Play Single Player',
    'combat': 'Combat Difficulty', 
    'seed': 'Seed', # This refers to the random "seed" that numpy uses to generate random numbers.
    'load': 'Load', # Load name of the save-file.
    'save': 'Save', # Save name of the save-file.
    'end': 'Game End', # Describes what settings will trigger the game to end.
    'standby': 'Please Wait While Game Loads',
    'unknown_detail': 'Unrecorded', # Details about the previous save that were not recorded because prior version did not keep track of it.
    'no_records': 'We did not find any records', # In the context of no game saves found in the save directory.
    'delete_record': 'Are you sure you would like to delete this record?', # Record is pretty generic in this context, it could mean save-file, it could mean username, or something else.
    'delete': 'Delete', # Delete the record
    'no': 'No', # Do not delete the record
}
# Do the same for this but keep Magic Sword in english
info_page_texts = {
    'quit': 'Exit Magic Sword',
    'return': 'Return', # Meaning go back or try connection again.
    'launch': 'Launching Game Locally...',
    'join': 'Joining',
    'failed': 'Connection Failed', # Regarding connecting to host IP address.
    'wait': 'Please Standby - Preparing Game',
    'crash': "Oh no! Your game crashed! {'' if save_file is None else 'You can try to reload the file `'+str(save_file)+'`'}.\n{'We have been notified of the error and should fix it soon!' if self.status else 'Please help us solve this issue by emailing magicsword.public@gmail.com with the snippet below (copied to your clipboard).'}", # Please translate this with all subtext in a manner that is linguistically sound, including rearranging embedded code as needed (in curly braces).
    'copy': 'Copy', # Used for copying to clipboard.
    'host_closed': "Game Aborted. Most likely the host closed the server.\nIf this sounds like an error, then please report what happened to magicsword.public@gmail.com\n\nYou can reload the game with the same usernames under the save file: {save_file}\n\n",
    'other_closed': "{username} Disconnected. Game Aborted.\n\nIf you were all in the middle of a game, feel free to pick back up with the same usernames, using the save file: {save_file}",
}
# Do the same translation for this dictionary, using the comments to better help guide you for the best translation.
birthcity_texts = {
    'hover': 'Hover over a city to see their benefits! Click one to choose your character.',
    'standby': 'Please standby for other players.',
    'loading': 'Please standby while the game loads.',
    'claim': 'You have claimed', # Keep in mind that following this statment a city name will be given in english. So the full context may be "You have claimed 'Scetcher'." - so allow the translation to account for that.
    'combat': 'Combat Style',
    'coins': 'Coins',
    'knowledge': 'Knowledges',
    'boosts': 'Combat Boosts',
    'tension': 'Tensions',
    'peacelvl': 'Peace Level',
    'hallmark': 'Hallmark',
    'perk': 'Perk'
}
# Please do the same translation for this dictionary
city_perks = {
    'anafola': 'Summoner contract fulfillments are 2x faster, bond rate is 1.25x faster.',
    'benfriege': '+1 xp when studying checked-out library books.',
    'demetry': 'Length of loans are 2 rounds longer, and maximum loan amount is 2 coins higher.',
    'enfeir': 'Auto-class 1 at the Reaquisition Guild.',
    'fodker': 'Auto-class 1 at the Defenders Guild.',
    'glaser': 'Rest bonus from completing Peace Assignment lasts for 2 extra rounds.',
    'kubani': 'Subtract one skill level requirement, 5 total Knowledge requirement, and 1 coin cost at the Ancestrial Order.',
    'pafiz': 'Combat boosts from meditating are lost at a rate of 4 instead of 5 per round.',
    'scetcher': 'Auto-class 1 Fighting Arena and can always face duelists in training.',
    'starfex': 'The chance of finding magic sword fragments are 8% rather than the standard 5% when excavating.',
    'tamarania': 'Auto-class 1 at the Smithing Guild.',
    'tamariza': 'Memberships at the Wizard Tower cost 1 less coin (which makes Basic membership free).',
    'tutalu': 'Auto-class 1 at the Hunters Guild.',
    'zinzibar': 'Subtract one combat attribute level requirement for learning secret combat arts at the Hidden Lair.'
}
# Please translate the following values as well put keep everything in the curly brances the same, as they will be replaced later.
virtue_texts = {
    'volunteer': "How many major actions would you like to help for?",
    'beggar': "How many coins would you like to give them?",
    'donation_drive': "Which item would you be willing to donate?",
    'escort': "Escort them to {city.title()}? Appears to be {distance} tiles away. Keep in mind, you only have 5 rounds to get there. If this city is locked to you, you can still take them there.",
    'rescue': "They need to be rushed to {city.title()} right away - it is {distance} tiles away. You only have 2 rounds. If this city is locked to you, you can still take them there.",
    'prisoner': "The bandit appears to have a combat level between {lvl_range[0]} and {lvl_range[1]}. Fight the bandit and rescue the prisoner?",
    'ally': "There are {enemies} enemies between combat level {lvl_range[0]} and {lvl_range[1]}. Aide the level {line['level']} {line['character']} in this fight? (Fight together)",
    'vine': "The wild vine monster appears to be between combat level {lvl_range[0]} and {lvl_range[1]}. Aide the level {line['level']} {line['character']} in this fight? (Fight together)"
}
# Please translate these entire list, keeping in mind that HP is short-hand for Hit Points, Major is short-hand for major actions available, Minor is minor actions available, Road is short-hand for road movements available, and Eat is short-hand for eat actions available. Please preserve the short-hand as best as possible, while retaining its meaning. 
frontstat_texts = ['Fatigue','HP','Coins','Items','Major','Minor','Road','Eat']
# Please translate this as best as possible- Also keep paragraphing and important formatting text like \n or \t. Also, please keep VP as it is.
player_track_texts = {
    'combat': ['', 'Attribute','Base','Boost','Total','Primed', ''],
    'knowledge': ['', 'Skill', 'Level', 'Boosts', 'XP', 'Primed', ''],
    'capital': ['City','Home','Market','Bank','Village 1', 'Village 2', 'Village 3', 'Village 4', 'Village 5'],
    'reputation': ['Mission','Stage 1\nCommon Folk', 'Stage 2\nNoblemen', 'Stage 3\nDistrict Leaders', 'Stage 4\nCity Counsel', 'Stage 5\nMayor'],
    'titles': ['Title', 'Category', 'VP', 'Minimum Req', 'Your Record', 'Highest Record'],
    'items': ['', 'Item', 'Quantity', 'Description', 'Sell', 'Use', 'Drop'],
    'quest': {'req': 'Requirement', 'fail': 'Failable', 'reward': 'Reward', 'proc': 'Procedure'},
    'stagger': 'Attack Stagger',
    'cbxp': 'Combat XP',
    'rep_req': "{self.player.fellowships['fodker'].get_asset_req(city)} Reputation\nRequired",
    'req_purchase_home': "You need at least {self.player.fellowships['fodker'].get_asset_req(city)} Reputation to purchase the home!",
    'has_worker': 'Owned and Has Worker (persuasion={self.player.workers[city]["persuasion"]}, haggling={self.player.workers[city]["haggling"]})!', # In the context of owning a market and having a worker there helping you.
    'req_market': "You need at least {self.player.fellowships['fodker'].get_asset_req(city)} Reputation to purchase the market!",
    'total_committed': 'Total Items Committed with Worker',
    'potential_profit': 'Minimum Total Potential Profit of Commited Items',
    'bank_cap': 'Bank Cap: {bank_cap} coins.',
    'title_desc': {
        'explorer': 'Most unique tiles traveled upon.',
        'loyal': 'Most rounds spent in their birth city (all actions per round).',
        'valiant': 'Maximum difference between an opponent stronger than you, that you defeated, and your total combat at the start of battle.',
        'sorcerer': 'Most consecutive Tamariza Wizard Tower platinum membership renewals.',
        'superprime': 'Highest credit score from the Demetry Grand Bank.',
        'traveler': 'Most road tile movement.',
        'apprentice': 'Most cumulative levels gained from trainers.',
        'laborer': 'Most jobs worked.',
        'valuable': 'Most money earned from jobs worked.',
        'entrepreneur': 'Most money received from owned markets.',
        'trader': 'Most trading (buy or sell) with unique traders.',
        'negotiator': 'Most successful persuasions.',
        'steady': 'Most rounds started with zero fatigue.',
        'grinder': 'Most skill XP earned by successfully using the skill or learned from checked-out library books.',
        'merchant': 'Most coin made from selling items to merchants or traders.',
        'brave': 'Sum total level of continuous enemies defeated without restoring HP.',
        'decisive': 'Shortest average round time.',
        'champion': 'Most class V Scetcher Tournament titles won.',
        'honorable': 'Most times successfully protected a village from bandits.',
        'resurrector': 'Strongest magic sword revived with its ability unlocked.'
    },
}
# Please translate these as well, keeping \n if the texts becomes too long, otherwise you can leave it out if the character count is less than 10. Also, please preserve text in curly braces because they will be replaced with python code. But feel free to rearrange those variables to make more grammatical sense after translation.
page_texts = {
    'defeat_req': "Defeated {amt} / {req} Bandit Targets.",
    'defend_req': "Defended {amt} / {req} Villages from Bandit Raids.",
    'increase_by_pct': 'This value goes up by {amt} after each attempt.',
    'complete_requests': 'Completed {done}/{mx} Class {c} Requests',
    'promotion_check_list': 'Class {c} Promotion Check List:',
    'mx_lvl': 'Level Cap: {lvl}', # Cap meaning maximum level this reward applies to.
    'nxt_add_rwd': 'Next Additional Reward for Class {c} Success:',
    'almost_credit': 'In {rounds} more rounds, you can gain {credit_score} credit score when returning your loan.',
    'return_loan': 'Return between now and the end of your loan to gain {credit_score} credit score.',
    'zoomlabel': 'You can zoom into the text with the mouse wheel or scroll by dragging.',
    'jobs_header': ['Available', 'Posting Chance', 'Recruiter', 'Skill', 'Level', 'Payment', 'XP', 'Accept'],
    'market_header': ['Available', 'Image', 'Item', 'Market Price', 'Description', 'Season', 'Quantity', 'Purchase'],
    'personal_market_header': ['Image', 'Item', 'Owned', 'In Demand', 'In Supply', 'Rare Item', 'Base Chance', '+ Persuade\nChance', 'Total\nSell Chance', 'Min Price', 'Max Price', 'Offer', 'Remove'],
    'worker_header': ['Image', 'Item', 'Owned', 'In Demand', 'In Supply', 'Rare Item', 'Base Chance', '+ Persuade\nChance', 'Total\nSell Chance', 'Min Profit', 'Max Profit', 'Offer', 'Remove'],
    'spar_title': 'Sparring Area',
    'spar_header': ['Combat Range', 'Spar Cost', 'Spar'],
    'hire_header': ['Comabt Level', 'Hire Cost', 'Hire'],
    'train_text': 'Train combat with sparring partners, if this is your birth-city then the cost is waived.\nYour health will not go to zero but you receive {xp_multiplier}% the normal combat XP for winning.',
    'hire_sellsword': 'Hire sell-swords to join your party for 10 rounds to fight with you.\nMinor Action',
    'no_sellsword': 'No sell-swords available to hire this round.',
    'weak_spar': 'Spar Lvl 2-5',
    'medi_spar': 'Spar Lvl 5-9',
    'sellsword_lvl': 'Hire Lvl {lvl}',
    'job_title': 'Job Postings',
    'job_descr': 'Jobs take 4 major actions to perform, which will occur automatically if you accept the job.',
    'skirm_header_base': ['City', 'Status', 'Rounds Left', 'Peace Level', 'Skirmish Chance'],
    'skirm_header_add': ['Level Range', 'Coins Dropped', 'Join Fight'],
    'late': 'Too Late\nto Join',
    'join': 'Join Fight',
    'skirm_desc_base': 'When this city is in a skirmish, market activity drops to {market_activity_reduced}% of normal, making trading more difficult. However, the rate at which supply decreases is also slowed. The market activity reduction matches the skirmish win rate, capped at 90%. The minimum is 5% unless adjusted during city development.',
    'skirm_desc_allowed': ['Now that you have completed the Join the Fight quest, you can participate in active skirmishes!', 'If there are 2 rounds left in the skirmish, you can join whenever, but you need at least 3 major actions if only 1 round left.', 'You will participate in 3 fights consecutively (only allowing to eat in-between), whose enemy level range can vary. You gain {xp_boost}x the combat experience each time if victorious!', 'Note: You lose combat XP if you run away from the battlefield!'],
    'skirm_desc_notallowed': ['If you complete the Join the Fight quest, you can participate in active skirmishes.', 'It would involve fighting 3 enemies consecutively, of varying combat level, with {xp_boost}x the combat xp earned.', 'But you will lose combat XP if you run away from the battlefield!'],
    'win_text': "Win{'' if len(winners) > 1 else 's'} the Game!", # When you translate this please convert the dynamic coding logic to make sense for the new language as well. It should by a pythonic statement in the new langauge that allows for a single winner or multiple winners. If the language does not have plurality, feel free to remove the embedded code.
    'game_time': "Total Game Time\n{tm}",
    'tour_citypage_title': "Welcome to Magic Sword!", # Please do not translate Magic Sword, but translate the rest and allow it to make grammatical sense as best as possible.
    'tour_citypage_welcome': "Would you like to take a tour of the city? Get a sense of your surroundings?\n\nIt takes about 5 minutes, but you can skip around or end it early.",
    'tour_boardpage_title': "Board Page Tour",
    'tour_boardpage_welcome': "Would you like to take a tour of the board? Get a sense of your surroundings?\n\nIt takes about 5 minutes, but you can skip around or end it early.",
    'tour_start': 'Start Tour', # Refers to starting a guided tour of the digital board game.
    'tour_exit': 'No Thanks', # Refusing the tour gracefully.
    'tour_dont_show': 'Dont show this tour again for this Username', # Refers to a check-box a user can click to stop this tour message from popping up next time they play.
    'tour_close': 'Close Tour',
    'smith_action': 'Smith', # In context of performing a smithing action yourself.
    'lack_cost': 'Low Coin', # In context of meaning does not have sufficient coin to purchase an item - the translation should remain short yet accurate.
    'rental_cost': 'Rental Cost', # In context of renting out a smithing room to smith your own armor.
    'smithing': "Smithing enables you to buff your attack or your defense. Attack can only be buffed with ore that match your combat style, and only the defense that matches the ore's combat property. Doing this yourself requires you to rent out the facility, the price is on the top-right corner.\nIf you do not possess the required smithing level, the smither may help for a fee, assuming they also have the level (shown on the top right). Cities either have a level 4, 8, or 12 smither in-house.",
    'smithing_header': [None, 'Attack', None, 'Ore', 'Boost', 'Lvl Req', 'Amount', None, 'Chance', 'Smith', None, 'Hire Cost', 'Hire Smith'], # Please dont translate None, also "Lvl Req" is horthand for minimum level requirement - in the translation please keep it short but allow it to be easily interpretable/recognizable.
    'trainer_title': 'Trainers',
    'trainer_descr': 'Trainers teach knowledge- and combat-based abilities for a fee based on their mastery and your skill level. Beginners are advised to wait until the mid-to-late game to use trainers effectively. Adept trainers can train up to level 8, while Masters can train up to level 12 with higher success rates but at a higher cost. Success depends on their mastery, your fatigue, and your critical thinking level, though there’s a small chance to succeed without it. Payment is only required upon successful training.\n\nTrainers may not always be available, leaving you with three options: wait until the next round, persuade them to prioritize you, or pay extra to secure their training services immediately.',
    'trainer_header': ['Available', '', 'Ability', 'Mastery', 'Persuade', 'Buyout', 'Cost', 'Train'], # Please use this context to help you translate the headers: Ability refers to either a knowledge skill or a combat attribute, Mastery refers to whether they are an Adept trainer or Master trainer, buyout is the act of paying the trainer extra money to acquire their training services immediately.
    'invest_header': ['', 'Item', 'Speed', 'Cost', 'Invest'], # Speed means speed of production, Invest means whether you want to invest money and resources into a factory.
    'invest_descr': 'Investing in villages grants one Capital Victory Point and requires the production cost and a loan of one item, returned after the first output. The village produces items at the specified speed, storing them in its warehouse until collected. However, if you delay too long, bandits may attack the village, and you risk losing most of the stored items.',
    'too_many_items_descr': 'Oh no, it seems as though you are carrying too many items. Would you like to drop any to make room for the new items?',
    'too_many_items_new': 'New Items',
    'too_many_items_old': 'Currently Held Items',
    'drop_none': 'Keep Items', # Meaning that you do not wish to drop any items in favor of picking up the new ones on offer.
    'active_quests': 'Active Quests',
    'no_quests': 'No Quests Active',
    'active_boosts': 'Active Boosts',
    'no_boosts': 'No Boosts Active',
    'garden_title': 'Community Garden', # The idea is that the Community Garden is a place where any player can grow vegetables or crops.
    'garden_descr': 'In this community garden you can only plant crops that grow in this city, and not all of them grow at the same rate. Planting crops works by removing one from your bag, after which a minimum of 2 units will be produced after the rounds specified (adjustable by Building the City). Planting gives 1/8 build points. Beware, it is a community garden, which means any player can harvest them or plant in the available spots, as long as they own a home! There is also a small chance that strangers will harvest or plant items. Planting will grant 1 gathering xp until level 3, while harvesting will grant 1 gathering xp until level 1. Both take minor actions.\n\n   - When you stack eat vegetables, only the round counter goes up.\n   - When you stack eat other crops, only the skill level goes up.',
    'garden_grow': 'Crops that grow here:\nHover over them for descriptions.',
    'garden_rounds': 'The numbers in the circles indicate how many rounds it takes for them to grow.',
    'rep_req': "Requires {vp} Reputation.", # Where vp is a score.
    'disconnected': "A player has disconnected from the game. The game does not work unless all expected players are in-game.\nFeel free to either return to the main menu and start a new game, or continue playing together later.\n\nYou can continue your game by returning to Magic Sword under the same exact usernames and entering this name into the load-file: {save_file}",
    'nocthollow': "A mysterious and dark force resides here. It is causing tiles to transform into wilderness, wreaking havoc upon Valdhomir. If {total} tiles succumb to the wilderness, the game will end. There are a few ways to make 1 progress point toward reverting a tile back to normal:\n   1) Get a Rare Find when Excavating.\n   2) Defeating wild vine monsters at location.\n   3) Paying the coins to clear it. Price depends on how close the nearest city is (pay on location).\n   4) Spending build points with cities, nearby cities will require less build points (spend in cities).",
    'player_nocthollow': "The rate at which tiles are transformed into wilderness depends on the number of players:",
    'temp_nocthollow': "Traveling here is not yet implemented and currently has no effect. However, the plan is for traveling here to eventually trigger a boss fight. If you emerge victorious, it will initiate the end-game and reward you with victory points. Stay tuned for updates!",
    # Build City texts
    'new_master': 'Choose an Adept trainer to promote into a Master trainer:',
    'local_source': 'Choose the new item to locally source:',
    'new_cultivation': 'Choose the crop to allow to grow (unnatural):',
    'trade_link_city': 'First, choose the city to establish a trade-route with:',
    'trade_link_item': 'Next, choose the item for the trade link:',
    'cat_req': "Upgrading {category} will require a {asset}{alternate}, {rep} Reputation, and cost {bp} Build Points.", # {category} is one of 'Security', 'Market', 'Agriculture', or 'Artisans', {asset} is 'home' or 'market', {rep} is an integer, and {bp} is an integer. Please use this information to best translate into the new language.
    'hard_support': '(Weakly supported at {city})',
    'base_support': '(Moderately supported at {city})',
    'easy_support': '(Strongly supported at {city})',
    'Roadwatch m': "Make nearby roads {pct}% safer from robbers. Also, any bandit camps within 2 tiles become half that percent safer.",
    'Roadwatch r': "Nearby roads are {pct}% safer from robbers. Also, any bandit camps within 2 tiles are half that percent safer.",
    'Fortify Villages m': "Make neighboring villages {pct}% safer from bandits.",
    'Fortify Villages r': "Neighboring villages are {pct}% safer from bandits.",
    'Keepers of the Peace m': "Make the city {pct}% safer from hooligans and player vs player fights.",
    'Keepers of the Peace r': "The city is {pct}% safer from hooligans and player vs player fights.",
    'Bolster Might m': 'Increase city might by one, improve minimum market activity by {market}%, and boost the XP multiplier for joining skirmishes by {xp}%.', # Where x is used to indicate multiplier, like 1.4x
    'Bolster Might r': 'City might is currently {might}, the minimum market activity possible is {market}%, and the current XP multiplier for joining skirmishes is {xp}x.',
    'Trap Sweepers m': "Make neighboring ruins {pct}% less likely to have traps.",
    'Trap Sweepers r': "Neighboring ruins are {pct}% less likely to have traps.",
    'Supply Boost m': "Boost market item replenish supply by one when the season hits.",
    'Supply Boost r': "Market replenish supply is {lvl} greater than normal, when the season hits.",
    'Trade Link m': "Establish a trade link with another city to bring an item to market. It becomes available 1-2 rounds after the season starts—unless skirmishing occurs both rounds. The supply equals the linked city's amount minus one. Both cities gain build points when purchasing.",
    'Trade Link r': "{amount} trade links have been established. Purchasing trade-linked items gives the linked city the same amount of build points. {items}",
    'Sourcing m': "Introduce a new item to the marketplace directly from local resources (limited selection). The amount that comes online is the normal supply amount minus one (on its season).",
    'Sourcing r': "{amount} items have been introduced to the marketplace from local resources. {items}",
    'Labor Growth m': "Make job openings {pct}% more likely, but with diminishing effect at higher base chances. (percent is applied to complement probability)",
    'Labor Growth r': "Job openings are {pct}% more likely, with diminishing effect at higher base chances. (percent is applied to the complement probability)",
    'Planting Grounds m': "Make an addition planting ground open up at the community garden.",
    'Planting Grounds r': "{lvl} additional planting grounds have been opened up at the community garden.",
    'Enhance Yield m': "Increase the yield for {typ} crops by one.",
    'Enhance Yield r': "Yield for vegetables is {vegetables}, for natural crops is {natural}, and for unnatural crops is {unnatural}.",
    'Stimulate Sprouting m': "Making crop sprouting (ready-time) one round faster for {typ} crops.",
    'Stimulate Sprouting r': "Sprouting (ready-time) for vegetables is {vegetables}, for natural crops is {natural}, and for unnatural crops is {unnatural}.",
    'New Cultivation m': "Cultivate the grounds to allow a new crop to grow unnaturally here.",
    'New Cultivation r': "{amount} new crops can grow here, unnaturally. {items}",
    'Support Apprentices m': "Make training availability for {typ} trainers {pct}% more likely.",
    'Support Apprentices r': "Training availability for Adept trainers is {adept}% more likely, and {master}% more likely for Masters.",
    'Harden Sparring R': "Add a new combat level range option for sparring: {range}",
    'Harden Sparring X': "Boost combat xp awarded by {pct}% when winning a sparring match.",
    'Harden Sparring r': "New combat level ranges: {ranges}.\nCurrent combat xp awarded when sparring is {pct}% of regular combat.",
    'Elevate Sellswords m': "Make the sellsword combat level range between {mn}-{mx}. Also, increase the usual count by {count}.",
    'Elevate Sellswords r': "Sellsword combat level range is {mn}-{mx} and the number of sellswords available are between {min_count} and {max_count}.",
    'Instructor Training M': "Promote an Adept level trainer to a Master level trainer (cannot be for Attack or Technique).",
    'Instructor Training P': "Make both adept and master level trainers {pct}% more successful in training.",
    'Instructor Training r': "Adept and Master trainers are {pct}% more successful in training. {amount} Adept trainers have been promoted to Masters.",
}

# When you translate these following texts, please leave VP as it is, and city names as they are, but feel free to change up order or context to make it grammatically correct and sound. Feel free to translate XP (experience) into something that is more meaningful for that language, otherwise keep it XP if it is commonly understood and well recognized. Also, please allow the voice for the following tour_texts translations to retain a helpful, tutorial type voice for gamers.
tour_texts = {
    # City Page Tour
    'Objective': "Your goal is to optimize each round by strategizing to collect as many Victory Points (VP) as possible.",
    'Aptitudes': "Click on the Player Track to explore five key aptitudes that award VP:\nCombat\nCapital\nKnowledge\nReputation\nFellowships\nTitles can also grant VP — more on that later!",
    'Info and Settings': "Here you'll find helpful guides, your game's auto-save name, options to change your settings, and a button to quit the game.",
    'Action Cards': "The action cards show you nearly all of your available actions. These are cards you can click to interact with the game and make decisions.",
    'Major Actions': "Each round consists of Major Actions. Once you've used them all, the round ends and a new one begins. In multiplayer, wait for all players to complete their rounds before proceeding.",
    'Minor Actions': "Using all your Minor Actions equals one Major Action.",
    'Fatigue': "Every Major Action adds to your fatigue. If it reaches the red zone, your actions become harder. Exceeding your fatigue limit paralyzes you, forcing you to rest for a few rounds.",
    'Rest': "Reduce fatigue by resting. Resting in your city is easier, unless you're at an Inn or have purchased a house outside.",
    'Reputation': "Earn Reputation VP by helping people around the city, indicated by marks above their heads. We recommend starting here to familiarize yourself with the game.",
    'Community Garden': "Grow and harvest crops. Crops in this game either give you boosts to skills or make some game mechanics easier. Community garden is shared by anyone owning a home, so be careful what you intend to grow! Also, sometimes strangers (non-players) may plant or harvest things.", 
    'Sparring Area': "Train Combat in the sparring area. While sparring grants less Combat XP than actual fights, it's safer. Level up when you reach 100 Combat XP, gaining 1 Combat VP.",
    'Job Postings': "Some jobs may appear each round. They’re a great way to earn Knowledge XP and VP early. As you gain skills, you can also earn coins through jobs.",
    'Market': "Each round, markets offer different items for quests, crafting, smithing, or learning. Each city has unique items, so you might need to travel. Early in the game, saving coins and finding items can be wiser.",
    'Inn': "Each city has an inn where you can pay 1 coin to recover fatigue faster. Inns are usually unnecessary when you're in your home city.",
    'Trainers': "Cities host different trainers—some focus on Combat attributes, others on Knowledge skills. They’re expensive and best utilized in the mid-to-late game when you have more coins.",
    'Personal Market': "While you can quick-sell items anytime, purchasing a personal market is a great early asset to earn coins by selling your items at a greater price. Many players travel to Glaser or Benfriege for cheaper markets. Owning one awards Capital VP. Note: purchasing in cities other than your own requires meeting Reputation requirements.",
    'Home': "Homes provide Capital VP, boost fatigue recovery, and increase carrying capacity. Players often start with purchasing their first homes in Benfriege, Glaser, or Zinzibar for more affordability and early carry capacity gains. Note: purchasing in cities other than your own requires meeting Reputation requirements.",
    'Skirmishes': "Tensions exist between each city and most of their neighbors. Depending on their peace level, a skirmish could break out. Skirmishes affect four things:\n1) If you visit a city skirmishes yours, its possible hooligans will attack you\n2) If you own a personal market, selling items will be more difficult in actively skirmishing cities\n3) If you have completed the 'Join the Fight' quest (Stage 3 Mission 6) then you can participate in these skirmishes.\n4) Wins/Draws/Loses will be recorded - which can affect the market activity.",
    'Smithing': "You start with a basic weapon (not displayed) and no armor, but you can upgrade anytime as long as you have the required ore and coins. The settings tab includes a help guide that details which ores to use and the Smithing levels needed to use them.",
    'Hallmarks': "Every city has a unique hallmark, and 11 out of 14 cities award Fellowship VP. You can visit any city Hallmark, but you'll likely use your own the most. Check the 'Fellowship' tab in the Player Track for details on what each hallmark does and how to earn VP through them!",
    'Gates': "Leaving the city can be risky. We recommend reaching Combat level 8-10 or hiring a Sellsword at the Sparring Area if you have enough coins. Some players wait to start the 'Mother Serpent' quest for a temporary companion. Don’t hesitate to explore—you might discover magical surprises!",
    'Good Deeds': "Occasionally, you’ll have opportunities to perform good deeds. These won’t appear on your stats but might help you earn VP faster over time.",
    'End': "Continue playing until you reach the Game End settings. The game auto-saves at the start of each round, so you can pick up right where you left off anytime. Practice your strategies, explore new approaches, challenge yourself, and, if possible, play with a friend!\n\nWe’d love your feedback to make the game even better. Visit us at https://magicsword.games and join the community!",
    # Board Page Tour
    'The Board': "Welcome to the board page, where you can explore tiles, gather resources, or visit cities in the world of Valdhomir. Most tiles, except cities and villages, offer two options: Excavate to search for items using your Excavating skill, or Harvest to gather herbs with your Gathering skill. Herbs provide temporary skill boosts. Successfully Excavating or Harvesting has 90% chance of emptying the tile for a few rounds, while failing has a 20% chance. Choosing not to take a found item costs only a Minor Action, while taking it requires a Major Action.",
    'Your City': "This is your birth-city, the only place where Reputation quests are available. You can click this tile again to return to the city page. The green highlight around this tile will follow you wherever you move, so you can easily identify your location on the board. To move to a different tile, simply click on a neighboring one.",
    'Cities': "Valdhomir has 14 cities, though many are initially locked until you earn the required Reputation VP to enter. Each city offers unique items in their markets, jobs, trainers for Knowledge and Combat, and fellowships to join. To purchase homes or markets in a city, you’ll need the necessary Reputation, shown on the Capital page under Player Track. Central cities generally have higher costs for homes and markets, but their Capital VP and returns are also greater.",
    'Villages': "Villages come in three types: food, crafting, and cloth. Investing resources in villages earns Capital VP and lets you produce those resources at varying rates based on their nearby cities (central cities typically produce faster). Beware—bandits may attack villages, delaying production. If you catch them in time, you can defend the village and reduce future attacks. See the Fodker Hallmark for more details.", 
    'Roads': "Moving between tiles requires Road Actions—using all of them consumes one Major Action. Entering a road or moving from a road to a city also uses a Road Action, but all other movements require a Major Action. Beware of traveling the roads, as you may encounter Highway Robbers, especially farther from cities! On the upside, you might also meet Traders usually offering rare or uncommon items, with all items often at better prices than city markets. Quick selling to traders usually also gets you better prices, especially if you haggle successfully.",
    'Ponds': "Ponds are the safest tiles in Valdhomir. No traps, monsters, or fighters will attack you here. You can Excavate for clay or fishing spots—eating fish restores HP. Sometimes, a Giant Serpent option may appear when Excavating. These creatures are strong but drop valuable scales when defeated. Avoid them if your Combat skill is low. Ponds may also contain mysterious water fragments. These tile locations vary between games.",
    'Plains': "Plains are relatively safe but may contain traps that cause fatigue damage unless you have a moderate Survival skill. Here, you can Excavate to find food sources like fruit bushes or wild herds, which reduce fatigue or restore HP. You might meet Hunting Masters, who can train you in Agility or Gathering. Plains may also hide mysterious air fragments. These tile locations vary between games.",
    'Caves': "Caves are rich in monsters and ores. They have three tiers—descend deeper for rarer ores and stronger foes. Traps and ambushes are common, so tread carefully. Caves are great for Combat training or testing your strength. At the caves, you might find mysterious earth fragments. These tile locations vary between games.",
    'Mountains': "Mountains offer ores and free training from Monks, the only trainers who charge nothing. They specialize in Survival and Excavating skills. While there are no enemies, the terrain is treacherous and best suited for players with high Survival. Ascend higher tiers for rarer ores and a greater chance of finding monks. Mountains may contain mysterious ice fragments. These tile locations vary between games.",
    'Outposts': "Outposts are perfect for crafters, offering excellent resources but guarded by strong bandits. These bandits also collect mysterious fire fragments. Be cautious when venturing here. Outpost locations vary between games.",
    'Old Libraries': "Old Libraries are ideal for Knowledge seekers, with books that increase Knowledge XP in their respective skill. However, Hermits guard these places fiercely—they may attack you, though some can be persuaded to teach Critical Thinking or Cunning. These tiles don’t contain fragments. Library locations vary between games.",
    'Ruins': "Ruins were once villages, now turned to rubble. They are recommended for mid-to-late game. You may find valuable old cloth, old books, or meet ancient wizards who either battle you or train you (if your Persuasion is high enough). They teach Hit Points and Heating. Ruins may also hide mysterious light fragments.",
    'Battle Zones': "Battle Zones are highly dangerous. Ninjas from Zinzibar and Enfeir are constantly at war here, and you may get caught in the crossfire. If you can survive, you may find rare ores or mysterious blood fragments.",
    'Wilderness': "The most dangerous tiles in Valdhomir. Survive the treacherous terrain and wild vine monsters to uncover the rarest items. Tile emptying also occurs much more frequently here regardless of excavating or harvesting success. While there are no fragments here, a strange force seems to linger in these areas.",
    'Inspect': "You can click on any tile to see movement consequences and what can be found in that tile.",
    'Zoom': "You can use the mouse wheel to zoom in or out. You can also press and hold the left-mouse button to pan the board. The highlighted button will center the board to the player. If you pan the board, a new button will appear which will re-center the board if you click it.",
    'Explore': "That’s it! There’s a lot to take in, and we don’t expect you to learn everything right away. Be bold—explore, make mistakes, and discover new things. We’d love to hear your thoughts! Join us at https://magicsword.games and share your journey!",
}
# Please translate these dictionaries, keeping the embeded variables intact (everything in curly-braces) and please make the translation seem as smooth as possible keeping in mind those curly-brace values will be replaced by more meaningful information. FTG is short-hand for fatigue- please keep that in mind when translating.
fight_texts = {
    'caught_off_guard': "You are caught off-guard!\n{self.foename} Lvl. {self.foelvl} using {lmap.m(style)} combat style.\n",
    'potential_xp': "Potential Combat XP rewarded for victory: {self.xp_up_for_grabs}\n",
    'guard_breakup_chance': "There is a {breakup_chance}% chance a Guard will break up this fight.\n",
    'cant_faint': "You can't faint, but leveling up probability is reduced.",
    'fighting_time': "Total Fighting Time: {total_fight_time} seconds.",
    'category': ['Very Weak', 'Weak', 'Match', 'Strong', 'Very Strong'],
    'fight': 'Fight',
    'run': 'Run (+{ftg} FTG)',
    'eat': 'Eat Before Fight',
    'ct_am': "{self.critthink} Critical Thinking\n   > Controls hint box opacity: {int(np.round(self.get_opacity()*100))}%",
    'ex_am': "{self.excavating} Excavating\n    > Controls hint box stay time: {np.round(self.get_hint_time(), 2)} seconds",
    'gt_am': "{self.gathering} Gathering\n   > Controls item click time: {np.round(self.get_gather_time(), 2)} seconds",
    'sv_am': "{self.survival} Survival\n   > Controls trap avoidance chance: {int(np.round(100*self.survival/self.get_rad()['survival']))}%",
    'cl_cm': 'Use mouse or press [C] to click.',
    'awaiting': "Awaiting for {self.foename} to Start Fight",
    'ready': "{self.foename} is Ready to Fight",
    'next_attack': "{self.fightorder[self.order_idx]} is Attacking Next",
    'vanished': "The Foe Vanished for a Moment! Your attack missed.",
    'missed': "You missed.", # In the context of they tried to attack but their attack missed.
    'summoner_msg': 'Your summoner helps you with {atk_increase} attack.\n',
    'attack_old': '{summoner_msg}Strike with {self.curAtk} {lmap.m(self.P.combatstyle).lower() if self.P.magic_sword_wielded is None else lmap.m(self.P.magic_sword_wielded).lower()} attack!\n\nUse [A]/mouse to Attack and [F] for fakes.',
    'attack': "{summoner_msg}Strike with {self.curAtk} attack on opponent's hit-box!\n\nUse [A]/mouse to Attack and [F] for fakes.", # When translating, please allow the grammatical formatting to make sense when the sub-messages are replaced.
    'out_of_time': "You ran out of time! You missed.",
    'foe_out_of_time': "Foe ran out of time - they missed.",
    'awaiting_opp': "Waiting for Opponent to Attack",
    'foe_failed': "Foe failed to submit an attack!",
    'you_failed': "You failed to submit an attack!",
    'npc_defending': "NPC Defending",
    'player_defending': "Player Defending",
    'foe_missed': 'Foe missed!',
    'dodge_defend': 'Dodge Time (Press [D] or mouse on green): {round(self.dodgeTime,2)}\nBlock Time (Press [B] or mouse on blue): {round(self.blockTime,2)}\nStrike Time: {round(self.strikeDelay,2)}', # Please allow grammatical sense to be retained as best as possible when translating and replacing the code.
    'select': "Select Attack\nOr Press [S]",
    'hitbox': "Click in this box to begin placing your attack!\n\n\nPlacing them in corners is generally a better approach.",
    'defbox': "Boxes will begin popping up here!\n\nPress [D]/left-click on Green Boxes to Dodge them, or [B]/left-click on Blue Boxes to Block them.\n\nYou can only Block if you have enough Defense.",
    'slow_mode': "Slow Pace", # Referring to whether you want to play on a slow fighting pace, which is recommended for beginners.
    'auto_fight': 'Auto Fight', # In other words, if the player clicks this button they choose to do auto-fighting (simulated fighting).
    'take_control': 'Take Control', # Meaning that they allowed auto-fight to be on for some time, and now want to stop auto-fighting and take full control.
    'attack_power': 'Attack = ',
    'foe_dodge': 'Foe Dodged ', # Will be filled in with a number after of how many were dodged.
    'you_dodge': 'You Dodged ', # Will be filled in with a number after of how many were dodged.
    'foe_block': 'Foe Blocked ', # Will be filled in with a number after of how many were blocked.
    'you_block': 'You Blocked ', # Will be filled in with a number after of how many were blocked.
    'foe_hit': 'Foe Inflicts ', # Damage inflicted, will be filled in with a number of how much damage after.
    'you_hit': 'You Inflicts ', # Damage inflicted, will be filled in with a number of how much damage after.
}
p2p_texts = {
    'awaiting': "Awaiting {self.O} to accept offer.",
    'no_actions': "You have no actions left! Either wait for the round to start or quit trade!",
    'accepted': "{self.O} has accepted the offer!",
    'An update has been made.': 'An update has been made.',
    'You rejected the offer!': 'You rejected the offer!',
    'receive_reject': '{self.O} rejected the offer!',
    'ins_coins': "You do not have enough coin to make that offer!",
    'max_item': "You cannot offer any more of that item!",
    'max_train': "You cannot train more than one at a time!",
    'remove': "You cannot make anymore offers to the trade! Try removing some!",
    'quit': 'Quit Player Trading',
    'complete': 'Complete Player Trading',
    "Training was unsuccessful.": "Training was unsuccessful.",
}
settings_texts = {
    'quit': 'Quit Game',
    'main': 'Main Menu',
    'info': 'Info',
    'play': 'Play',
    'help': 'Help',
    'coming_soon': 'Coming Soon',
    'savefile': 'Save-file Name',
    'save': 'Save', # Referring to save game
    'settings': 'Settings',
    'round table': 'Round Ranking', # See the highest victory points on the current round
    'round lbl': 'Most victory points earned by this round in all your games',
    'all time table': 'Personal Bests', # Refers to all-time high scores for only a single username.
    'all time lbl': 'Personal best scores across all your games',
    'i': {'save': "Your game is auto-saved at the start of each round as"
         },
    'h': {'more': "More help is coming soon!\nDont forget to check out our Youtube Page in the meantime!",
          'youtube': "Open YouTube Page"
          },
    's': {'more': "More settings options coming soon!"}
}
chat_texts = {
    'chat': 'Chat Box (press enter in the input box below to send message)'
}
# When translating please keep the paragraphs in place. Tiers indicate different tier levels of caves or mountains (i.e. lower down or higher up respectively) - please take that into account when translating it to the best of your ability.
consequence_message = {'road': 'Highway Robber encounter chance: (distance to nearest city)/6. Highway Robber Lvl: 3-30. Reward: 1-3 coins. Highway Robber Avoidance: sneak/12.\n\nTrader Chance: 1/6 if no Highway Robber encounter.',
                       'pond': 'No consequences upon entering this tile.',
                       'plains': '1/4 chance of stepping on a trap - Fatigue Damage: 1. Damage Avoidance: (survival+1)/9.',
                       'cave': 'HP Damage: 1 in tier1, 3 in tier2, 5 in tier3. Avoidance: (survival+1)/3 in tier1, (survival+1)/5 in tier2, (survival+1)/9 in tier3.\n\nMonster Lvls: 3-20 tier1, 15-40 tier2, 35-60 tier3. Reward: raw meat and hide (varying). Monster Avoidance: (sneak+1)/(4*tier).',
                       'outpost': 'Bandit encounter chance: 1/3. Bandit Lvl: 15-40. Reward: 2-5 coins. Bandit Avoidance: stealth/12.',
                       'mountain': 'HP & Fatigue Damage = tier level. Damage Avoidance: (survival+1)/3 in tier1. (surval+1)/5 in tier2, (survival+1)/9 in tier3.',
                       'oldlibrary': 'Hermit encounter chance: 1/4. Hermit Lvl: 55-75. Reward: 5-9 coins. Hermit Avoidance: persuasion/12.',
                       'ruins': 'HP Damage: 2. Damage Avoidance: survival/14.\n\nOld Wizard encounter Lvl 60-85. Reward: 2 old cloth. Old Wizard Avoidance: persuasion/12.',
                       'battle1': 'Ninjas: 1/4 chance 1 Ninja Lvl 70-95, 1/4 chance 1 Ninja Lvl 60-85, 1/4 chance 2 Ninjas Lvls 50-75, 1/4 chance 3 Ninjas Lvls 50-75. Reward: varying coins. Ninja Avoidance: stealth/18.',
                       'wilderness': 'HP Damage: 2, Fatigue Damage: 3. Damage Avoidance: survival/15.\n\nWild Vine Monster Lvl 95-120. Reward: 4 bark. Wild Vine Monster Avoidance: stealth/18.'}
consequence_message['battle2'] = consequence_message['battle1'] # No translation needed for this line.
# Continue translating as before please
hallmark_texts = {
    'sharpness': 'Improves combat critical hit chance through sharpness training.',  
    'invincibility': 'Boosts defense capabilities through invincibility training.',  
    'vanish': 'Enhances dodge skills, allowing the player to vanish from sight.',  
    'shadow': 'Increases dodging ability by mastering shadow techniques.',  
    'vision': 'Heightens battlefield awareness by improving cunning in combat.',  
    'class': 'Displays the current guild class rank of the player.',  
    'active_hunt': 'Details of the active quest or hunt the player is pursuing.',  
    'coins_rewarded': 'Displays the number of coins awarded upon quest completion.',  
    'next_additional_reward': 'Indicates the next potential reward upon success.',  
    'successes_until_promotion': 'Tracks the number of successful quests needed for class promotion.',  
    'next_class_skill_reqs': 'Lists the skills needed to advance to the next class rank.',  
    'membership': 'Current membership level in the wizard tower.',  
    'membership_rounds_remaining': 'Number of rounds remaining before membership expires.',  
    'auto_renewal': 'Indicates if membership auto-renewal is enabled.',  
    'renew_with_market_earnings': 'Displays whether market earnings are used for membership renewal.',  
    'current_consecutive_platinum_renewals': 'Count of consecutive platinum-level renewals achieved.',  
    'best_consecutive_platinum_renewals': 'Records the best streak of platinum renewals.',  
    'active_enchant_quantity': 'Shows the number of active enchantments on items.',  
    'active_enchants': 'Description of the active enchantments on player’s gear.',  
    'active_enchant_timer': 'Rounds left until current enchantments expire.',  
    'ores_gifted': 'Total ores gifted to the smithing guild.',  
    'quest_task': 'Displays the current smithing guild task.',  
    'quest_status': 'Status update on the current quest’s progress.',  
    'tournament_signedup': 'Shows if player is signed up for an arena tournament.',  
    'tournament_start_rounds': 'Rounds remaining until tournament begins.',  
    'consecutive_last_place': 'Count of consecutive last-place finishes in tournaments.',  
    'dueling_hiatus': 'Cooldown period before returning to the battle arena.',  
    'stored_energy': 'Energy stored from meditation for future use.',  
    'combat_boosts': 'Combat boosts gained through meditation (i.e. active energy remaining).',  
    'optimal_successes': 'Total optimal meditation sessions completed.',  
    'loot_class': 'Loot quality improvement through specialized training.',  
    'food_class': 'Increases food benefits through skill development.',  
    'fatigue_class': 'Reduces fatigue after activities through training.',  
    'minor_treading': 'Allows more minor actions per round through training.',  
    'horse_riding': 'Permits horseback riding for faster travel on roads.',  
    'major_treading': 'Enables more major actions per round through skill.',  
    'assignments_completed': 'Tracks the number of guild assignments completed.',  
    'rest_bonus_rounds': 'Rounds left where rest bonus is active.',  
    'current_assignment': 'Displays the current guild assignment.',  
    'counsel_convinced': 'Shows whether the counsel has been convinced of a proposal - required for promotion.',  
    'bandit_target_defeated': 'Tracks if the target bandit for promotion has been defeated.',  
    'villages_protected': 'Count of villages the player has protected.',  
    'protection_request_chance': 'Chance of receiving a protection request from a village.',  
    'coins_rewarded': 'Coins awarded for completing the current guild quest.',  
    'request_active': 'Indicates if the quest request is currently active.',  
    'chain_number': 'Shows the current quest chain number.',  
    'total_successes': 'Total successful completions of quests.',  
    'credit_score': 'Player’s credit score at the bank, affecting loan offers. Based on player Reputation and successful loan returns.',  
    'loan_amount': 'Current loan amount borrowed from the bank.',  
    'original_loan_length': 'Length of the loan agreement when first taken out.',  
    'loan_length_remaining': 'Rounds left until the loan repayment is due.',  
    'strikes': 'Current missed payments on loan.',  
    'total_strikes': 'Total historical missed payments.',  
    'read_fatigue': 'Extra fatigue from reading activities.',  
    'read_action_counter': 'Rounds until reading fatigue resets.',  
    'total_borrowed': 'Total library books borrowed.',  
    'books_learned': 'Total checked-out books learned from, increasing knowledge.',  
    'creature_class': 'Level of training for a summoned creature.',  
    'creature_hp': 'Health points of the summoned creature.',  
    'bond_rate': 'Rate at which bond with the creature increases.',  
    'creature_bond': 'Current bond level with the summoned creature.',  
    'effect_probability': 'Chance that creature assists during combat.',  
    'penalty_rounds': 'Rounds until bond growth can resume after penalty.',
    # Quest descriptions - please do not translate variables in {}, as they will be formatted later.
    'enfeir_progress_0': 'Go to the purple highlighted village to begin searching for the stolen valuable item. Click `Investigate` in the action grid once there.',
    'enfeir_progress_1': 'Your investigation suggests that the item was moved to a different village (highlighted in purple). There may be more than one village to search.',
    'enfeir_progress_2': 'You found the right village. Now its time to attempt its retrieval! Click `Study Environment` in the action grid.',
    'enfeir_progress_3': 'You found the valuable item! Return to Enfeir with it to claim your reward!',
    'glaser_progress_0': 'Go to the two purple highlighted cities and convince their leaders to improve relations. Click `Improve Peace` in the action grid once there.',
    'glaser_progress_1': 'Go to the final remaining city highlighted in purple and convince them to improve relations as well, in the same way as the first.',
    'starfex_quest': 'Finding Rare Artifact',
    'starfex_progress_0': 'Go to the olive green highlighted {area} tile on the board where the rare artifact is located. Use the action grid to start the minigame once there.',
    'starfex_progress_1': 'Return to Starfex with the Rare Artifact and click on the Ancient Magic Museum, then click `Give Rare Artifact` button in the action grid.',
    'tamarania_class_2_quest': 'Go to three different cities, click `Convince Smither` button in the action grid once there. ({amt}/3 done)',
    'tamarania_class_3_quest': 'Go to any plains tile, click `Excavate` button in the action grid once there to find meteorite. ({amt}/3 done)',
    'tamarania_class_4_quest': 'Go to depth 3 of any cave tile, click `Excavate` button in the action grid once there to find bedrock. ({amt}/3 done)',
    'tamarania_class_5_quest': 'Go to any wilderness tile, click `Excavate` button in the action grid once there to find living stone. ({amt}/3 done)',
    'tamarania_complete': 'Return to the Smithing Guild and gift all rare ores to them. You should find a `Gift Ore` option once you click the Smithing Guild.',
    'tutalu_progress_0': 'Go to the purple highlighted {area} tile - It may attack you once there, otherwise click `Excavate` to find the Monster once there. Defeat it.',
    'tutalu_progress_1': 'Go back to the Hunters Guild to claim your reward for defeating the monster!',
}
enchant_texts = {
    "scales": "+1 coin when persuasion successful.",
    "leather": "+1 hit points.",
    "bark": "+1 survival when in caves, mountains, and wilderness.",
    "ceramic": "+1 minor action.",
    "benfriege cloth": "+1 xp when reading books.",
    "demetry cloth": "+2 xp and +2 coins when working jobs.",
    "glaser cloth": "Safely enter cities skirmishing with yours.",
    "kubani cloth": "-1 fatigue when survival is successfully activated.",
    "pafiz cloth": "+1 major action when staying on the same tile (and tier), outside cities, for two rounds.",
    "scetcher cloth": "+30 combat xp when defeating an opponent stronger than you (with combat-related def stats).",
    "starfex cloth": "8% fragment finding chance increase.",
    "tamariza cloth": "75% chance for +1 xp when using a skill.",
    "tutalu cloth": "25% piercing damage chance against non-human foes.",
    "glass": "75% tile emptying chance reduction upon successful excavation.",
    "rubber": "30% chance of automatically defending an attack after defense-time expires.",
    "gems": "+30% better selling price on crafted item.",
    "old fodker cloth": "+2 stability.",
    "old enfeir cloth": "+2 cunning.",
    "old zinzibar cloth": "+2 agility."
}
# Please translate each action option below (only the values in the dictionary) - but You must keep the @ symbol in the beginning of the string if present. Also, when translating, please keep the curly braces and their contents but feel free to rearrange it depending on what fits better with the translation.
common_action_texts = {
    'More Prompts on Click': 'More Prompts on Click',
    'Minor Action': 'Minor Action',
    'Revert Tile': 'Revert Tile',
    'Revert Wilderness Tile': 'Revert Wilderness Tile',
    'Major Action': 'Major Action',
    'Trainers': 'Trainers',
    'Personal Market': 'Personal Market',
    'Sparring Area': 'Sparring Area',
    'Inn (4): 1 coin': 'Inn (4): 1 coin',
    'Market': 'Market',
    'Build City': 'Build City', # Meaning add points to develop city
    'Job Postings': 'Job Postings',
    'Smithing': 'Smithing',
    'Community Garden': 'Community Garden',
    'Trader': 'Trader',
    'Excavate': 'Excavate',
    'Harvest': 'Harvest',
    'Change Investment': 'Change Investment',
    'Invest in Production': 'Invest in Production',
    'invest_item': "@{self.lmap.m(item)}: {cost} coins",
    'Change My Mind - Exit': 'Change My Mind - Exit',
    'buyout': "@Pay {buyout} coins Buyout for Priority",
    'Choose None': 'Choose None',
    'Commit Items': 'Commit Items',
    'Attempt Sale': 'Attempt Sale',
    'Baby Mammoth': 'Baby Mammoth',
    'Find Rare Artifact': 'Find Rare Artifact',
    'Mother Serpent': 'Mother Serpent',
    'Trade with Mountain Trader': 'Trade with Mountain Trader',
	'Take Caravan Ride to Bandit': 'Take Caravan Ride to Bandit',
	'Find & Convince Leader': 'Find & Convince Leader',
	'Appeal for Resources': 'Appeal for Resources',
	'Defend Village': 'Defend Village',
	'Find Mountain Trader': 'Find Mountain Trader',
	'Improve Peace': 'Improve Peace',
	'Find Warrior': 'Find Warrior',
	'Continue Defending Village': 'Continue Defending Village',
	'Attempt Study': 'Attempt Study',
	'Approach Stealth Master': 'Approach Stealth Master',
	'Trade/Train': 'Trade/Train',
	'Retrieve': 'Retrieve',
	'Accept': 'Accept',
	'Attempt to Haggle': 'Attempt to Haggle',
	'Convince Smither': 'Convince Smither',
	'Fight': 'Fight',
	'Investigate': 'Investigate',
	'Duel': 'Duel',
	'Convince Haggling Master': 'Convince Haggling Master',
	'Confirm': 'Confirm',
	'Add Warrior to Group': 'Add Warrior to Group',
	'Find & Convince Warrior': 'Find & Convince Warrior',
	'Confirm Purchase': 'Confirm Purchase',
    'Find Pet': 'Find Pet',
    'Clean House': 'Clean House',
    'Gaurd Home': 'Gaurd Home',
    'Gift Craft': 'Gift Craft',
    'Spar with Boy': 'Spar with Boy',
    'Gift Book': 'Gift Book',
    'Gift Sand': 'Gift Sand',
    'Give Baby Mammoth': 'Give Baby Mammoth',
    'Apply Cubes': 'Apply Cubes',
    'Wait for Robber': 'Wait for Robber',
    'Give Book': 'Give Book',
    'Gift Weapon': 'Gift Weapon',
    'Give Stealth Book': 'Give Stealth Book',
    'Distribute Food': 'Distribute Food',
    'Study with Monk': 'Study with Monk',
    'Search for Monster': 'Search for Monster',
    'Teach Fishing': 'Teach Fishing',
    'Gift Craft Books': 'Gift Craft Books',
    'Deliver Sand': 'Deliver Sand',
    'Fill Library': 'Fill Library',
    'Convince a Market Leader': 'Convince a Market Leader',
    'Deliver Historic Books': 'Deliver Historic Books',
    'Deliver Material': 'Deliver Material',
    'Smith Gold': 'Smith Gold',
    'Show Friend': 'Show Friend',
    'Claim Reward': 'Claim Reward',
    'Show Rare Ore': 'Show Rare Ore',
    'Gift Perfect Craft': 'Gift Perfect Craft',
    'Tend Market': 'Tend Market',
    'Commit Items with Worker': 'Commit Items with Worker',
    'Get New Worker': 'Get New Worker',
    'Get Worker': 'Get Worker',
    'Spar Lv2-5': 'Spar Lv2-5',
    'Spar Lv5-9': 'Spar Lv5-9',
    'pay_action': "Pay {cost} Coins",
    'hire_sellsword': "@Hire Lvl {lvl} {lmap.m(var.cities[city]['Combat Style'])} Sellsword",
    'Attempt Rescue': 'Attempt Rescue',
    'Ignore Prisoner': 'Ignore Prisoner',
    'Aide Them': 'Aide Them',
    'Ignore Them': 'Ignore Them',
    'Ignore': 'Ignore',
    'Continue without Haggling': 'Continue without Haggling',
    'Purchase without Haggling': 'Purchase without Haggling',
    'No Haggling': 'No Haggling',
    'Equipped Armor Slot': 'Equipped Armor Slot',
    'Non-Equipped Armor Slot': 'Non-Equipped Armor Slot',
    'Rent Facility': 'Rent Facility',
    'Hire Lv4 Smither': 'Hire Lv4 Smither',
    'Hire Lv8 Smither': 'Hire Lv8 Smither',
    'Hire Lv12 Smither': 'Hire Lv12 Smither',
    'Descend Cave': 'Descend Cave',
    'Ascend Cave': 'Ascend Cave',
    'Descend Mountain': 'Descend Mountain',
    'Ascend Mountain': 'Ascend Mountain',
    # For the following translations, please keep the @ in the beginning if included, and allow the grammatical translations to retain correctness in the new language while still allowing embedded code to be replaced in {}. The context of these phrases are action buttons that the user can click to perform that action.
    'request_contract': '@Request Class {c+1} Contract',
    'summon': '@Summon Class {oc} Creature',
    'Release Current Creature': 'Release Current Creature',
    'Book Return': 'Book Return', # Returning a library book
    'Read': 'Read', # In the context of read a library book.
    'Checkout': 'Checkout', # In the context of checkout out a library book.
    'Return': 'Return', # In the context of returning a loan.
    'Take Loan': 'Take Loan',
    'Retrieve': 'Retrieve', # Retrieving an item
    'Reject the request': 'Reject the request',
    'Reject': 'Reject',
    'Reject Request': 'Reject Request',
    'request': '@Class {c} Request',
    'Cancel Ride': 'Cancel Ride',
    'Confirm Purchase': 'Confirm Purchase',
    'Attempt Study': 'Attempt Study',
    'Attempt to Haggle': 'Attempt to Haggle',
    "Don't Haggle": "Don't Haggle",
    'Purchase Horse': 'Purchase Horse',
    'Continue Meditation': 'Continue Meditation',
    'Stop Meditation': 'Stop Meditation',
    'Start Meditation': 'Start Meditation',
    'sign_up': "@Sign Up for Class {self.get('class')} Tourney",
    'Fight Duelist in Training': 'Fight Duelist in Training',
    'Fight Duelist': 'Fight Duelist',
    'Drop Quest': 'Drop Quest',
    'Get Rare Artifact Quest': 'Get Rare Artifact Quest',
    'Give Rare Artifact': 'Give Rare Artifact',
    'Drop Rare Artifact Quest': 'Drop Rare Artifact Quest',
    'Purchase Fragments': 'Purchase Fragments',
    'Gift Ore': 'Gift Ore',
    'Enchantment': 'Enchantment',
    'build_sword': "@Build {self.lmap.m(fragment.split(' ')[0]).title()} Sword",
    'Turn Auto Renewal on': 'Turn Auto Renewal on',
    'Keep Auto Renewal off': 'Keep Auto Renewal off',
    'Cancel Membership': 'Cancel Membership',
    'Choose Different Tile': 'Choose Different Tile', # In the context of choosing a tile to teleport your character to
    'Cancel Teleport': 'Cancel Teleport',
    'Turn Renew with Market Earnings on': 'Turn Renew with Market Earnings on',
    'Keep Renew with Market Earnings off': 'Keep Renew with Market Earnings off',
    'Change Membership': 'Change Membership',
    'Teleport': 'Teleport',
    'Matter Conversion': 'Matter Conversion', # Wizard technique to convert one item to another
    'Alchemy': 'Alchemy',
    'Reject the hunt': 'Reject the hunt',
    'class_hunt': "@Class {c} Hunt",
    'Reject Hunt': 'Reject Hunt',
}
# Please keep code in {} unchanged but translate all other things except city names like Starfex. Feel free to move the code in the {} around to help it better match the language translation.
action_description_texts = {
    'rest': "Reduce fatigue by {amt} at the cost of one major action.",
    'Market': "See what items are for sale this round.",
    'Job Postings': "See what jobs are available this round.",
    'Smithing': "Smith some of your ores into a weapon or armor.",
    'Community Garden': "Either plant some crops yourself, or harvest fully grown ones. Its for all to share!",
    'Build City': "Spend build points to develop the city in Security, Agriculture, Markets, or their Artisans.",
    'Trainers': "Spend some coin to learn Combat or Knowledge.",
    'Personal Market': "Sell some of your items to gain some coin. Or look for workers to automate some of it.",
    'Sparring Area': "Enter low-risk combat and win to gain Combat XP.",
    'Inn (4): 1 coin': "Rest at the inn and recover 4 fatigue at the cost of 1 coin and a major action.",
    'Excavate': "Try finding items at this location - costs a major action. It is a minor action only if you find something and dont take it.",
    'Harvest': "Try finding crops at this location - costs a major action. It is a minor action only if you find something and dont take it.",
    'Trader': "Look at the wares of the Trader!",
    'Huntsman': "Persuade the Huntsman to teach you in either Agility or Gathering.",
    'Fruit Bush': "Use your gathering skill to try and harvest some fruit.",
    'Wild Herd': "Use your gathering skill to try and get raw meat from the wild herd you spotted.",
    'Baby Mammoth': "Get the Baby Mammoth!",
    'Find Rare Artifact': "Start the Rare Artifact minigame. Be careful of deceptive traps!",
    'Go Fishing': "Use your gathering skill to get some raw fish.",
    'enemy_encounter': "Enemy Encounter Lv {min_lv} - {max_lv} | Possible Combat Styles: {styles}",
    'Descend Cave': "Go deeper into the cave at your own risk. You can find rarer items down there. Click to find out more.",
    'Ascend Cave': "Go back up toward the surface. A requirement if you are trying to get back to normal ground to move around.",
    'Uncommon Craft Item': "You have the chance of finding one of leather, glass, or ceramic.",
    'Ascend Mountain': "Go higher up the mountain at your own risk. You can find rarer items up there. Click to find out more.",
    'Descend Mountain': "Go down the mountain. A requirement if you are trying to get back to normal ground to move around.",
    'Monk': "Teaches Survival and Excavating for free! You just need the right critical thinking to succeed.",
    'Book': "A chance of receiving one of 10 skill books. Not all of them have equal probabilties though.",
    'Hermit': "An aggressive teacher. You can persuade him to teach Cunning or Critical Thinking, but if you fail to persuade them, you fight.",
    'Cloth': "Old cloth go for a lot of coin if sold in the right places.",
    'Wizard': "An aggressive teacher. You can pursuade him to teach Hit Points or Heating, but if you fail to persuade them, then you fight.",
    'Old Book': "A random old skill book, and the only book that can teach you up to level 10. It is destroyed after reading though.",
    'Common Ore': "One of a rank 2 ore: Tungsten, Titanium, Diamond, or Chromium.",
    'Uncommon Ore': "One of a rank 3 ore: Tantalum, Aluminum, Kevlium, or Nickel.",
    'Rare Ore': "One of a rank 4 ore: Shinopsis, Ebony, Astatine, or Promethium.",
    'Grand Tree': "Use your gathering skill to obtain a large amount of fruit or bark.",
    'Rare Find': "One of the rank 4 ore: Shinopsis, Ebony, Astatine, or Promethium. Or, you may instead find Gems.",
}
# Please keep code in {} unchanged but translate all other things except city names like Starfex. Feel free to move the code in the {} around to help it better match the language translation.
common_output_texts = {
    'checkout_msg': "Bring this book to any [color=74f96a]{skill}[/color] trainer that is unlocked for you. Pay him [color=f7f96a]{cost} coins[/color] to get [color=6ac7f9]{xp}xp[/color]. Trainer cities listed to the right.",
    'click_revert': 'Click a revertable wilderness tile to see required Reptutation and how many build points it would cost to revert it.',
    'bad_revert': 'Reverting this tile would cost {bp} build points and requires {rep} Reputation. You do not meet at least one of them.',
    'init_revert': 'You meet the {rep} Reputation requirement. It will cost {bp} build points for one progress point in reverting this tile, do you wish to proceed?',
    'too_far_revert': 'This tile is too far away from the city, they are not willing to spend any resources on reverting it.',
    'pay_clear': 'The base cost to make a single progress toward clearing the wilderness is {base_cost} coins. There is {total_progress} progress left. Pay coins to revert wilderness?',
    'prompt_drop_quantity': 'How many {item} would you like to drop and destroy?',
    'round_end': 'Round Ended',
    'fainted': 'You Fainted!',
    'survival_saved_faint': "Your survival skill helped you save combat XP and coins!",
    'win_game': '{winner} Wins the Game!',
    'trader_appears': 'Trader Appears!',
    'round_start': 'Start Round {self.localPlayer.round_num}!',
    'action': 'Available Action Cards:',
    'quest_restart': "Mission '{self.quests[quest].text}' must be restarted!",
    'quest_failed': "You failed the mission '{self.quests[quest].text}'!",
    'quest_complete': "You completed the mission '{self.quests[quest].text}'! Reputation increases by {self.quests[quest].stage}!",
    'abort_trade': "Trading with {self.O} has been aborted.",
    'reject_trade': "{username} attempted to trade with you but was rejected.",
    'wrongtile_trade': "You and {username} are no longer on the same tile. Cannot trade.",
    'wrongtier_trade': "{username} attempted to trade with you but are in the wrong {lmap.m(P.currenttile.tile)} tier.",
    'prompt_trade': "{username} wants to trade with you. Conduct trade?",
    'send_trade': "Sending trade request to {username}.",
    'evadefailure_battle': "You are unable to evade! You are caught off-gaurd by {username}!",
    'wrongtier_battle': "{username} attempted to fight you but are in the wrong {lmap.m(P.currenttile.tile)} tier as you.",
    'reject_battle': "{username} attempted to fight you but was rejected due to your status.",
    'dual_battle': "{username} and you declared a fight simultaneously! Going directly into the fight.",
    'standby_battle': "{username} declared to fight you! You have to make a choice to continue.",
    'prompt_battle': "{username} has declared to fight you. What would you like to do?",
    'cantfight_battle': "You can't fight them for another {P.player_fight_hiatus[username]} rounds",
    'send_battle': "Sending fight declaration to {username} - if their status is available, they will either try to evade or fight you.",
    'confirm_battle': "Are you sure you want to fight {username}?",
    'fight_unable': "{username} is currently unable to fight.",
    'fight_wrongtier': '{username} is not in the same {lmap.m(P.currenttile.tile)} tier as you, so you cannot fight.',
    'fight_evaded': "{username} evaded the fight.",
    'fight_plundered_item': "Plundered {lmap.m(message['plundered_item'])} from {username}!",
    'fight_plundered_coins': "Plundered {message['plundered_coins']} coins from {username}!",
    'fight_dropped_coins': "Found {message['dropped_coins']} coins on the ground after the battle!",
    'trade_wrongtier': "{username} is not in the same {lmap.m(P.currenttile.tile)} tier as you, so you cannot trade.",
    'trade_rejected': "{username} either rejected or is currently unable to trade.",
    'donate_hint': "[Game Hint] You could potentially get victory points and greater reward for donating to the Ancient Magic Museum in Starfex!",
    'sell_fragment': "The market is not willing to take this item. Try the Ancient Magic Museum in Starfex for some credit.",
    'heat_receive': "You produce {amtReceived} of {lmap.m(recvd)}",
    'heat_2nd': "You extract {lmap.m(secondaryItem)}!",
    'hold_title': "You now hold The {title.capitalize()} title!",
    'lost_title': "You lost The {title.capitalize()} title to {maxRecord['holder']}",
    'now_title': "{maxRecord['holder']} now holds The {maxRecord['title'].capitalize()} title!",
    'lost_ing_boost': "Your {lmap.m(ingredient)} boost on {lmap.m(var.ingredient_properties[ingredient]['skill'])} is no longer in effect.",
    'lost_some_ing_boost': "You lost {len(popped)} boost for {lmap.m(var.ingredient_properties[ingredient]['skill'])}.",
    'ftg_msg': "You may take {fatigue} fatigue",
    'update_skill': "You leveled up {lmap.m(skill)} to {self.skills[skill]}!",
    'max_attr': "Your level in {lmap.m(attribute)} was not able to level beyond {max_lvl} with this action",
    'max_skill': "Your level in {lmap.m(skill)} was not able to level beyond {max_lvl} with this action",
    'levelup_skill': "Leveled up {lmap.m(skill)} to {self.skills[skill]}!",
    'inc_cap': "+{capital_info[city]['home_cap']} {lmap.m('Capital')}.",
    'inc_mrkt_cap': "+{capital_info[city]['market_cap']} {lmap.m('Capital')}.",
    'training_allowed': "Training in {city} is now allowed.",
    'market_purchase': "You successfully purchased a market in {city}!",
    'purchased_asset': 'Purchased {lmap.m(asset).title()} in {lmap.m(self.currenttile.tile).title()}',
    'worker_sold': "Worker sold {lmap.m(d['item'])} for {sell_price} profit (after taking their cut) at {city}.",
    'out_working': "You are out working, {P.working[1]} actions so far.",
    'two_cities': "You accepted the assignment to improve relations between {two_cities[0]} and {two_cities[1]}. The embassy suggests to start with one city hall.",
    'prompt_two_cities': "Accept the assignment to improve relations between {two_cities[0]} and {two_cities[1]}? Currently peace level is {tension} (skirmish chance={int(np.round(100/(tension+1)))}%)",
    'prompt_teleport': "Teleporting to {self.lmap.m(self.player.parentBoard.gridtiles[coord].tile).title()} will cost {fatigue} fatigue. Do wish to proceed?",
    'rest': "You recover {rest_rate} fatigue & {hp_recover} HP",
    'ended_round': "{self.username} Ended Round",
    'activation': 'Activation: ', # A {msg} that may occur for xp_skill
    'successful': 'Successful: ', # A {msg} that may occur for xp_skill
    'extra_sguild': 'Smithing Guild Extra: ', # A {msg} that may occur for xp_skill
    'xp_skill': "{msg}Gained {xp}xp for {lmap.m(skill)}.", # {msg} could also be an empty string, {xp} is always an integer, and xp stands for experience.
    'feel_good': "You feel good about your actions...", # indicates the user did something good and is rewarded for that with good deeds (supposed to be a feeling).
    'good_effect': "You feel the effect of your good deeds...",
    'enter_city': "You are now allowed to enter {city}!",
    'buy_market_able': "You are now allowed to buy a market or home in {city}!",
    'train_able': "You are now allowed to train in {city}!",
    'req_asset': "Get {self.fellowships['fodker'].get_asset_req(city)} Reputation to buy a market or home in {city}.",
    'req_train': "Get {3*city_info[city]['entry']} Reputation or purchase home to train in {city}.",
    'looking_for_assistants': "The following people are looking for assistants today:",
    'jobs_uh-oh': "Uh oh, your fatigue must be less than {P.max_fatigue - 4} to go to work! You can still click the jobs for info.",
    'working_job': 'Working Job',
    'completed_job': 'Completed Working Job',
    'job_coins': "Received {payment + additional_coins} coins.",
    'gained_fvp': "Gained {add} Fellowship VPs!", # Where VP stands for victory points.
    'rushed': "Someone rushes you to the nearest city to recover.",
    'lost_horse': "You lost your horse!",
    'lost_coins': "You lost {coins_lost} coin{plural} and {int(np.round(xp_lost*100))} combat xp.", # combat xp lost is an integer between 0-100
    'you_are_paralyzed': "You are paralyzed.",
    'encounter_single': 'Encounter Lv{lvl} {lmap.m(name)} using {lmap.m(cbstyle)}',
    'encounter_multi': 'Encounter {party_size} {lmap.m(name)} with combined level of {lvl} using {lmap.m(cbstyle)}',
    'unable_avoid_robber': "Unable to avoid robber!",
    'avoided_robber': "Successfully avoided robber!",
    'activate_quest': 'Activating Quest {quest}',
    'minor_action': 'You took a minor action.',
    'prefix_minor_action': 'Minor action: {msg}',
    'all_minors': 'All minor actions performed',
    'opponent_weak': "Your opponent is weak to your attack style. Their agility is affected.",
    'you_are_weak': "You are weak to opponent's {lmap.m(self.foestyle)} combat style. Your agility is affected.",
    'no_ores': "You do not have any ores to smelt.",
    'road_to': "Road movement to {lmap.m(P.currenttile.tile).title()}",
    'road_on_road': "Road Movement",
    'change_production': "Changing production from {self.lmap.m(current_item)} to {self.lmap.m(item)} will cost {cost}, current production will be lost and restarted with new item (except lent items). Change production?",
    'invest_item': "Invest in {self.lmap.m(item)} production will cost {cost} coins and lending the item for the first round. The village will produce 1 {self.lmap.m(item)} every {speed} rounds. Invest?",
    'does_not_produce': "This village does not accept {self.lmap.m(item)}. It only accepts: {', '.join([self.lmap.m(v_item) for v_item in var.capital_info[city]['produce'][village]])}.",
    'sent_item_to_bank': "{amt_sent} {self.lmap.m(item)} sent to warehouse storage in {city} village {village[-1]}",
    'scared_bandit': "Your defender reputation scared the bandits from pillaging your asset in {city} village {village[-1]}.",
    'asset_lost': "Village {village[-1]} of {city} was raided - {self.lmap.m(lost_assets)} asset was stolen. Your production is delayed by a round.",
    'assets_lost': "Village {village[-1]} of {city} was raided - {self.lmap.m(lost_assets)} assets were stolen. Your production is delayed by a round.",
    'no_lost_assets': "Village {village[-1]} of {city} was raided - No assets lost but your production will be delayed by a round.",
    'successful_investment': "You successfully setup investment for {self.lmap.m(item)}! +1 Capital VP.",
    'donate_amount': "How many {self.lmap.m(item)} would you like to donate?",
    'donated_amt': 'Donated {amt} {self.lmap.m(item)}',
    'sellsword_joins': "Lvl {lvl} {lmap.m(sellsword_style)} Sellsword joins your party for 10 rounds for {coins} coins.",
    'sellsword_prompt': "Would you like to hire a lvl {lvl} {lmap.m(sellsword_style)} Sellsword for {coins} coins to join your party for 10 rounds?{'' if city==P.birthcity else ' (cost is higher for you in this city).'}", # When translating this, please also translate the (cost is higher for you in this city) substring.
    'extra_coin_sellsword': "This is not your birth-city, pay 1 coin to spar? (Lvl {lvlrange[0]}-{lvlrange[1]})",
    'single_buy': "Bought {lmap.m(item)} for {cost} coins", # When translating please allow the grammer to make sense when the variables are replaced.
    'multi_buy': "Bought {amt} {lmap.m(item)} for {cost*amt}", # When translating please allow the grammer to make sense when the variables are replaced.
    'memory_warning': "Warning! We detect only {available_memory}GB memory remaining- the game may crash suddenly.",
    'accept_escort': "Accepted Escort Quest",
    'accept_rescue': "Accepted Rescue Quest",
    'train_others': "Training Others",
    'cleaning_home': "You spent an action cleaning the home (Total: {B.count})",
    'esc_found': "Excavation found {lmap.m(item)}",
    'found_fragment': "You found a {lmap.m(fragment)}!",
    'found_fragment_action': '{lmap.m(fragment).title()} Found via Excavation',
    'found_item': "You found a {lmap.m(item)}!",
    'not_found_item': "Did not find a {lmap.m(item)}",
    'not_found_fragment': "You would have found a {lmap.m(fragment)} but a strange repellent force with your current one made you lose it.",
    'found_worker': "You found a level {worker_lvl} persuasion and {haggle_lvl} haggling worker willing to work for you! He will take {int(var.worker_takes*100)}% of the item sell price (minimum of 1 coin).",
    'prompt_worker': "Hire this level {worker_lvl} persuasion and {haggle_lvl} haggling worker?",
    'hired_worker': "You hired the level {worker_lvl} persuasion and {haggle_lvl} haggling worker for your market in {city}.",
    'haggle_saves': "Your haggling will save you {r} coins. Complete purchase?",
    'found_warrior_quest': "You found a {P.birthcity} warrior in {city}! He responds to your call and heads to {P.birthcity}!",
    'failed_find_warrior': "You failed to find a warrior in {city}! You can only fail {failsleft} more times!",
    'prompt_sneak_attack': "You found a lvl {lvl} {lmap.m(name)}. Perform a sneak attack? You could hit a max of {sneak_attack_max}. If you kill him with a sneak attack, it does not count as combat but loot remains the same.",
    'foe_sneak_attack': "Foe inflicts {player_dmg} damage to you via a sneak attack!",
    'player_sneak_attack': "You inflict {foe_dmg} via a sneak attack!",
    'sneak_attack_defeated': "Your sneak attack defeated {lmap.m(name)}.",
    'found_book': "You found a {lmap.m(book).title()}!",
    'found_friend': "You found the friend! Now go back to {P.birthcity.title()} with him and claim your reward.",
    'long_lost_book': "You found an old book containing long lost history! You have found {P.PlayerTrack.Quest.quests[4, 6].count} so far.",
    'found_warrior_lvl': "You found a warrior lvl {lvl}",
    'long_fight': "You take an extra {xtra_fatigue} fatigue for fighting for a long time.",
    'gain_cb_xp': "You gain {int(np.round(levelsup*100))} combat xp!",
    'lvl_up_attr': "Leveling up {lmap.m(random_atr)}!",
    'prompt_lvlup': "Choose your level up attributes! ({self.levelsup} Remaining)",
    'fight_abort_wrong_tile': "{username} and You are no longer on the same tile - Fight Aborted!",
    'lost_item_to_player': "You lost {lmap.m(item)} to {username}!",
    'lost_coins_to_player': "You lost {amt} coins to {username}!",
    'sold_item_cost': "Sold {lmap.m(item)} for {sellprice} coins.",
    'minimum_heat_lvl': "You need at least Lv{heatableItems[item]} Heating to attempt the heating!",
    'succ_read_book': "You successfully read the {lmap.m(book)}!",
    'inss_coin_book': "You do not have enough coin! It costs {cost} to learn.",
    'low_lvl_book': 'Your {lmap.m(skill)} level is too low to learn from this {level} book!',
    'high_lvl_book': 'Your {lmap.m(skill)} level is too high to learn from this {level} book!',
    'prompt_xp_book': "Do you wish to gain {xp}xp in {lmap.m(skill)} at the cost of {cost} coins?",
    'inss_buyout': "You do not have {buyout} coins.",
    'mxxed_ability': "You have already maxed out {lmap.m(abilities)}",
    'train_cost_prompt': "Would you like to train at cost of {cost} coins?",
    'succ_train_paid': "You successfully leveled up in {lmap.m(abilities)} and pay trainer {cost} coins.",
    'lvlup_primed': "You have already unlocked the potential to level up {lmap.m(abilities)}, now you need to {requirement} to level up!",
    'skill_mxed': "You have already maxed out {lmap.m(skill)}.",
    'succ_primed_paid': "You successfully unlocked the potential to level up {lmap.m(abilities)}! Now {requirement} to level up! You pay the trainer {cost} coins.",
    'harsh_rocks': 'Fell on the harsh rocks: -{hp_dmg} HP',
    'harsh_env': 'Buffeted by harsh environment: -{hp_dmg} HP, +{ftg_dmg} fatigue',
    'gathered': "Gathered {gathering} {lmap.m(item)}",
    'meat_collected': "So far, gathered a total of {P.PlayerTrack.Quest.quests[3, 2].meat_collected} raw meat",
    'harvested': "Gathered {amt} {lmap.m(ing)}!",
    'summ_harvest': "Your summoner helped you forage {lmap.m(ing)}!",
    'summ_exc': "Your summoner helped you find {lmap.m(lbl)}!",
    'purs_master': 'Persuaded {master} to teach you.',
    'fail_purs_master': 'Failed to persuade {master} to teach you.',
    'old_book_learned': "Understood teachings from old {lmap.m(book)} then it turned to dust.",
    'old_book_some': "Understood some from old {lmap.m(book)} but then it turned to dust.",
    'old_book_primed': "You successfully unlocked the potential to level up {lmap.m(skill)}, now use skill successfully to level up!",
    'old_book_fail': "Found old {lmap.m(book)} but could not understand it.",
    'old_book_recc': "Found old {lmap.m(book)} but can't learn anything new. Try learning from a master {lmap.m(skill)} trainer.",
    'old_book_none': "Found old {lmap.m(book)} but can't learn anything new.",
    'food_gift': "City villagers gift you a {lmap.m(food)}!",
    'collect_market': "Collected {collect} coins from saved market earnings.",
    'entry_refusal': "The city will not let you enter! (Need {self.fellowships['fodker'].get_entry_req(nxt.tile)}+ Reputation!)",
    'up_peace_lvl': "You increased the peace level between {' and '.join(list(skirmish))} by a factor of {factor}!", # When translating please allow the grammer to make sense when the variables are replaced. Please also translate the sub-text ' and ' to make grammatical sense in the context of making peace between two cities.
    'napsack_life': "Your napsack can be used {self.napsack_life} more times before wearing out.",
    'max_boost': "You cannot boost your level beyond {var.max_skill_level}.",
    'not_stackable': "You cannot stack the same skill boost more than {var.max_ingredient_stacking} times.",
    'food_active': "You now have {lmap.m(food)} active.",
    'activate_food': "Your {lmap.m(food)} boosts your {lmap.m(stat['skill'])} by {stat['amt']} for {stat['rounds']} rounds.", # Please arrange the text in a way that makes most sense when variables are rpelaced (Which should be standard for all these translations).
    'ftg_restore': 'fatigue by {ftg}', # Used in context of fatgiue was restored by {amount}
    'hp_restore': 'HP by {hp}', # Used in context of HP was restored by {amount} - please use closest translation alternative for HP that makes sense for the language, or keep HP if it is commonly known.
    'food_restore': 'Restored {", ".join(restoring_list)} with {lmap.m(food)}', # Note that we use the ftg_restore and hp_restore above to created the restoring_list - so please allow the translation to work well when the code {} is replaced.
    'lost_effect': "You lost your {lmap.m(potion)} effect.",
    'elixir_of_vigor': "Your elixir of vigor protected you from {hp_amt} HP and {ftg_amt} FTG damage.",
    'already_won': 'Note: You have loaded a game where {winner} have already won the game.',
    'basic_activate': "Your Basic Tamariza Tower Membership successfully activated 1 lvl higher {lmap.m(skill)}.",
    'gold_activate': "Your Gold membership increases your {lmap.m(skill)} lvl by 1!",
    'platinum_activate': "Your Platinum membership increases your {lmap.m(skill)} lvl by {add_lvl}!",
    'ftg_impct': "Fatigue impacted your {lmap.m(skill)} skill down to level {actv_lvl}",
    'take_job': "Now that you have primed your {lmap.m(ability)} skill, go take a job to level up.",
    'get_cbxp': "Now that you have primed your {lmap.m(ability)} attribute, get combat xp like normal to level up.",
    'lvl_up_attribute': "You leveled up {lmap.m(attribute)} to {new_lvl}!",
    'boost_attr': "{'Lost' if val < 0 else 'Gained'} {lmap.m(attribute)} Boost of {abs(val)}", # When translating, please also translate the subtexts of 'Lost' and 'Gained' to make sense in context of boosting the combat attribute temporarily.
    'purchased_home': "You successfully purchased a home in {city}!",
    'inc_inv_space': "+{capital_info[city]['capacity']} inventory space.",
    'haggle_home': "This will cost {cost}. Attempt to Haggle (+1 Fatigue)?",
    'max_bank_reached': "Your market bank at {city} has reached its max coins capacity of {bank_cap} coins! Go collect them to earn more.",
    'dropped_item': "Dropped {amt} {lmap.m(item)}",
    'init_drop_item': "Are you sure you want to drop and destroy {amt} {lmap.m(item)}?",
    'coin_reward': "Rewarded {int_amt} coin!",
    'item_reward': "Rewarded {int_amt} {lmap.m(rwd)}!",
    'ended_round': "{self.username} Ended Round",
    'weapon_switch': "Switched out {lmap.m(switch_out)} for {lmap.m(switch_in)}.", # In context of weapon switching
    'prompt_destroy_aslot': "Are you sure you want to drop and destroy this {'weapon' if space == 0 else f'armor {space+1}'} upgrade?", # Please translate sub-text as well (weapon and armor)
    'destroy_aslot': "{lmap.m(prev)} is destroyed.",
    'destroy_aspace': "No longer possess {'weapon' if space == 0 else f'armor {space+1}'} upgrade", # Please translate sub-text as well (weapon and armor)
    'smith_weapon': "Smithing successful! Attack boosted by {amt}",
    'smith_weapon_switch': "Smithing successful - switch to your {lmap.m(self.P.combatstyle)} weapon to see effects.",
    'smith_armor': "Smithing successful on Equipped Armor! Def-{lmap.m(atr)} boosted by {amt}",
    'smith_lvl_req': "You need a smither with at least level {essf.inv_smithing(reqlvl, space)} smithing to smelt {lmap.m(item)}.",
    'attempt_smith_haggle': "Will you attempt to haggle (+1 Fatigue)? Rental cost is {rentalcost} or smith charges {fullcost} by default.",
    'smithing_req': "{lmap.m(item)} requires at least level {essf.inv_smithing(reqlvl, space)} to smith.",
    'sold_smith_piece': "Sold smithed piece for {sellprice}.",
    'lost_craft': "No longer possess craft {space+1}",
    'prompt_drop_craft': "Are you sure you want to drop and destroy Craft {space+1}?",
    'bring_back_craft': "{lmap.m(last_item)} is brought back as an item.",
    'sold_craft': "Sold craft {space+1} for {sellprice}.",
    'protection_request': "The Nobleman requests you to protect him until reaching {furthest_city}",
    'mother_serpent': "{lmap.m(P.combatstyle)} Companion joins your party for 3 rounds - after which you will need to restart the quest.",
    'letter_request': "You are requested to take the letter to {furthest_city}",
    'gifted_weapon': "Gifted {P.quests[(2, 7)]['weapons_gifted']} of 2 swords.",
    'distributed_food': "You have distributed a total of {P.PlayerTrack.Quest.quests[3, 1].food_given} food!",
    'learn_from_monk': "You have studied with the monk {P.PlayerTrack.Quest.quests[3, 3].convinced_monk} time(s)",
    'teach_fishing': 'Success! So far, taught {P.PlayerTrack.Quest.quests[3, 5].count} men to fish',
    'present_craft_book': "Village output efficiency increased by 1 for {P.birthcity}!",
    'distribute_sand': "Delivered {P.PlayerTrack.Quest.quests[3, 8].count} bags of sand so far",
    'fill_library': "You have now given: {', '.join(books_given)}",
    'convince_leader': "Market prices reduced by 1 (min=1) in {P.birthcity}!",
    'leader_count': "You still need to convince {6 - P.PlayerTrack.Quest.quests[4, 3].count} more market leaders.",
    'pursuade_trader': "Successfully pursuaded trader to start coming to {P.birthcity}! ({P.PlayerTrack.Quest.quests[4, 4].count}/3)",
    'city_trader': "Traders now have a 1/8 chance of appearing in {P.birthcity}!",
    'renovation': "Homes in {P.birthcity} have increased capacity of 3!",
    'cant_convince_warriors': "You can't look in this city because you have already started looking in other cities! ({', '.join(list(P.quests[(4, 8)]['cities']))})",
    'raid_ready': "You persuade them to raid the caves once all three in the {P.currenttile.tile} are ready. You have convinced {P.quests[(4, 8)]['cities'][P.currenttile.tile]} so far in {P.currenttile.tile}!",
    'give_rare_ore': "{lmap.m(atr)} Boosted by 2!",
    'not_perfect_craft': "You do not possess the perfect craft of: {', '.join(pc)}",
    'maxed_training': "You have already maxed out {lmap.m(self.is_trainee[0])}!",
    'lvl_up_ability': "You successfully leveled up in {lmap.m(ability)}",
    'already_primed_playertrade': "You have already unlocked the potential to level up {lmap.m(ability)}, now {requirement} to level up! Aborting trade.",
    'prime_playertrade': "You successfully unlocked the potential to level up {lmap.m(ability)}! Now {requirement} to level up!",
    'job_ftg_failure': "Your fatigue is too high! You could have received {payment} coins and {xp_msg} in 4 actions.",
    'prompt_job': 'Would you like to assist {lmap.m(skill_users[skill])} for 4 actions? [Earn {payment} coins, {xp_msg}, but 4 fatigue applied]',
    'tension_active': "Be mindful: Tensions are active between {city} and {P.birthcity}! Hooligans could be aggravated!",
    'tension_calm': "Tensions between {city} and {P.birthcity} are calm at the moment.",
    'battle_abandoned': "You abandoned the battlefield! You lose {int(round(100*xp_lost))} Combat XP!",
    'train_req_notmet': "Get {3*city_info[self.P.currenttile.tile]['entry']} Reputation or purchase home to train in {self.P.currenttile.tile.title()}.",
    'atk_tech_train': "This trainer will not train your attack or technique. Try a {lmap.m(self.P.combatstyle)} trainer instead.",
    'user_lost_connection': '{username} Lost Connection!',
    'city_claim': "{username} claimed {message['city']}", # This is in context of username has essentially selected their city/character - so claim can be translated as selected or picked.
    'user_efficiency': "{username} increased village output efficiency by 1 for {message}!",
    'user_discount': "{username} convinced {message} market leaders to reduce their prices by 1 coin (min=1)!",
    'user_trader_allowed': "{username} convinced traders to start appearing in {message}! (1/8 chance)",
    'user_peace_up': "{username} increased the peace level between {' and '.join(list(message[0]))} by a factor of {message[1]}!", # Please be sure to translate inner text ' and ' as well- and try to make translation as grammatically correct as possible when the code is replaced.
    'user_home_in_cap': "{username} increased {message[0]} home capacity by {message[1]}!",
    'user_donated_fragment': "{username} donated a {lmap.m(message)} to the Ancient Magic Museum!",
    'p2p_trade_abort': "{username} aborted the trade!",
    'p2p_trade_out': "{username} is out of actions. Either wait for round to start or quit trade!",
    'end_game_triggered': "{username} Triggered End Game!",
    'knowledge_book_xp': "You can now gain {P.standard_read_xp}xp when reading knowledge books.",
    'received_coins': "You received {coins} coins!",
    'can_now_train_half_off': "You can now train in {P.birthcity} for free with Adept trainers and half price with Master trainers!",
    'defeated_foe_msg': 'Defeated {lmap.m(self.foename)}',
    'ran_from_foe_msg': 'Ran From {lmap.m(self.foename)}',
    'sold_by_mrkt': "Gained {total} coins selling the items: {', '.join([self.lmap.m(s) for s in sold])}", 
    'invalid_possess': "You do not possess valid {product_type} items",
    'least_prod': "You need at least {cost} coins to invest in {product_type} production here.",
    'full_prod_capacity': "Village {village[-1]} at {city} is at full capacity! They cannot store any more product. Come pick it up.",
    'low_prod_inv': "You do not have enough inventory space to hold all the product in the warehouse! ({amt_remaining} remain in storage)",
    'received_prod': "You have received {change_made} {self.lmap.m(item)} from the village.",
    'min_cost_prod': "You need at least {cost} coins to invest in production for this item",
    'cant_afford': "Changing production will cost {cost}, which you cannot afford.",
    'in_skirmish_caution': "{self.tile.title()} is currently in skirmish - so market activity is {int(100-var.skirmish_hit[True]*100)}% lower than normal. Proceed with caution.",
    'items_committed_already': "Note: You already have {self.total_offered} items committed to this Market Place.",
    'mkt_activity': "Market activity is {int(round(activity*100))}% strong as Demetry.",
    'foe_player_in_group': "{name} is fighting with a group!",
    'lowest_def_on_foe': "Your opponent's lowest defense is used because of your {lmap.m(self.P.magic_sword_wielded)}.",
    'your_lowest_def': "Your lowest defense is used because your foe is using a {lmap.m(self.foestyle)}!",
    'foe_ran_from_fight': "{self.foename} ran from the fight!",
    'gaurd_break_up': "Gaurds at {self.P.currenttile.tile.title()} broke up the fight!",
    'total_ore_cost': "So far, found ores costing a total of {P.PlayerTrack.Quest.quests[3, 2].total_ore_cost}",
    'cannot_heat': "{lmap.m(item)} cannot be heated!",
    'not_owned_heat': "You don't own {lmap.m(item)} to heat it!",
    'lvl_up_succ_ability': "You successfully leveled up in {lmap.m(abilities)}",
    'lost_atr_faint': "You lose {lmap.m(Ratr)}, are paralyzed, and rushed to nearest city.",
    'mx_bank_cap_reached': "Your market bank at {city} has reached its max coins capacity of {bank_cap} coins! Go collect them to earn more.",
    'sold_smithed_piece': "Sold smithed piece for {sellprice}.",
    'sold_crafted_piece': "Sold craft {space+1} for {sellprice}.",
    'wait_stealth_master': "You need to wait {P.PlayerTrack.Quest.quests[2, 8].wait_rounds} more rounds for master to write the book",
    'already_began_tension_reduction': "You already began trying to reduce tension between {' and '.join(list(P.PlayerTrack.Quest.quests[4, 5].skirmish))}. You must stick to that!",
    'convinced_lessen_war_effort': "You convinced the leader to lessen the war effort! {5 - P.PlayerTrack.Quest.quests[4, 5].count} left to go!",
    'convinced_three_warriors': "You have convinced 3 warriors in {P.currenttile.tile} to raid the caves. They set out and do so!",
    'unrecognized_item': "Unrecognized item {lmap.m(item)}!",
    'ftg_lss_than_job': "Your fatigue must be less than {P.max_fatigue-4} to perform a job.",
    'max_creature_bond_reached': "Your creature bond has reached {var.anafola_max_bond}! Go to the Castle of Conjurors to fulfill a new contract and promote your class!",
    'bond_rate_drop': "Your bond rate is reduced by {abs(drop)} and your bond will not improve for {penalty_rounds} rounds.",
    'summoned_creature': "You summoned your class {c} creature.",
    'prompt_summon_creature': "Are you sure you wish to summon your class {c} creature{msg}?",
    'summon_rounds_taken': "You are told that fulfilling your class {new_class} contract could take between {mn} and {mx} rounds.",
    'book_no_longer_available': "{self.lmap.m(book)} book is no longer available!",
    'loan_amt_deducted': "{self.get('loan_amount')} coins has been deducted.",
    'still_owe_loan': "{self.player.coins} coins has been deducted, but you still owe {still_owe} coins!",
    'lost_home_by_loan_failure': "You have lost your home in {city}!",
    'lost_trainer_failure': "You can no longer use trainers in {city}.",
    'new_home_cost': "Next time you purchase the home in {city} it will cost you {homecost-still_owe} coins.",
    'loand_remainder_forgiven': "The {still_owe} coins you still owe the bank is forgiven.",
    'loan_rounds_left': "Only {llr} rounds left on your loan!",
    'received_loan_start': "Receiving a loan of {loan_amount} coins for maximum duration of {loan_length} rounds.",
    'repay_loan_balance': "You must repay the entire balance - and you currently do not have {self.get('loan_amount')} coins to do so.",
    'returned_loan': "You are returning {self.get('loan_amount')} to the bank.",
    'gained_creditscore': "You gained {self.get('loan_amount')} credit score!",
    'reaq_elevation': "Your Reaquisition Class has been Elevated to {c}!",
    'debug_enfeir': "Progress: {progress}, Total Progress: {nlc['progress']}, Max Needed: {max_progress}",
    'village_distances': "Distance between {i} and {i+1}: {distance}",
    'prompt_reject_request': "Reject this request? [{self.get('active_quest_details')['str']}]",
    'ability_too_high': "Your {self.lmap.m(ability)} is greater than the limit for this reward.",
    'defender_elevation': "You are promoted to Class {c} at the Defenders Guild in Fodker!",
    'btarget_remaining': "You still need to defeat {amt_left} more Bandit Targets",
    'convince_counsel_remaining': "You still need to convince one City Counsel from the following: {var.counsel_class[self.get('class')]}",
    'protect_villages_left': "You still need to protect {amt_left} more villages from Bandit Raids",
    'bandits_defeated': "Defeated {self.player.village_raid_countdown[coord]['defeated']} of {self.player.village_raid_countdown[coord]['bandits']} Bandits",
    'min_combat_fight_bandit': "You need at least {var.village_raid_min_cblvl} total combat to be useful against these bandits.",
    'find_bandit_lvls': "You see {bandit_num} most likely between level {mn_combat} and {mx_combat} combat.",
    'not_enough_caravan_coin': "You do not have {var.caravan_ride_cost} coin.",
    'caravan_prompt': "Where would you like to go? We can take you up to {var.caravan_ride_max_distance} tiles away for {var.caravan_ride_cost} coin.",
    'convince_city_success': "You successfully convince the {self.player.currenttile.tile.title()} counsel to lend its resources to the Defender's Guild!",
    'caravan_ready_bandit': "Ready to leave with the caravan to fight {name} level {lvlrange}?",
    'informed_of_bandits': "The Defender's Guild has beeen informed of a {self.lmap.m(name)}, typically level {lvl}, about {distance} tiles away. It should take {int(np.ceil(distance/var.bandit_caravan_ride_speed))} major actions to get there with the caravan (no fatigue).",
    'embassy_elevation': "You are promoted to Class {c} at the Peace Embassy!",
    'peace_effort_gratitude': "{persons} are grateful for your peace efforts! They give you a gift.",
    'remaining_convince_city': "Now go to {other_city} and convince their counsel to reduce tensions.",
    'completed_kubani_exc_learning': "You successfully completed {self.lmap.m(field.replace('_', ' ').title())} learning!",
    'new_kubani_effect': "You now have {var.kubani_class_effect[field][True]}.",
    'progress_kubani_class_lvl': "You progressed to {self.lmap.m(field.replace('_', ' ').title())} {lvl+1}!",
    'new_kubani_lvl_class': "You now have {var.kubani_class_effect[field][lvl+1]}.",
    'horse_cost_prompt': "Purchasing a horse will cost you {cost}. Make the purchase?",
    'horse_haggle_prompt': "Horses cost {var.horse_cost}. Attempt to Haggle? (Extra Fatigue)",
    'kubani_lvl_too_low': "Your {self.lmap.m(t)} Level is too low! You need at least {req}.",
    'do_not_possess_coin': "You do not have {cost} coins!",
    'study_kubani_cost': "One successful study session for {self.lmap.m(self.get_study_name(field))} will cost {cost}. Attempt to Study?",
    'study_haggle_prompt': "Studying {self.lmap.m(self.get_study_name(field))} will cost {cost}. Attempt to Haggle? (Extra fatigue)",
    'pafiz_elevation': "You are promoted to class {c} in the Pafiz Meditation Chamber.",
    'med_action': "Meditation Action: {im}, Stored Energy: {new_stored_energy}",
    'stored_energy': "You have {se} stored energy remaining.",
    'lost_med_cb_boost': "You have lost {remove_num} meditated combat boost",
    'cb_boosted_lvls': "Your combat has been boosted by {se} random levels. Rests now take minor actions.",
    'sc_promoted': "You are promoted to class {c}!",
    'sc_demoted': "You have been demoted to class {c}.",
    'tournament_beginning_soon': "[TOURNAMENT CALL] We have enough signatures and will begin the tournament in {tsr} rounds!",
    'tournament_rounds_left': "[TOURNAMENT CALL] {tsr} rounds left until tournament starts! Make sure to make it to Scetcher.",
    'begin_duel_this_round': "Time for the {pos_name[position] if position in pos_name else 'next'} battle! Come to Scetcher Battle Arena and begin your duel anytime this round.",
    'rounds_till_next_duel': "You have {nr} more rounds before your next duel.",
    'congrats_on_place': "Congrats on {postfix[place]} place! You get {reward} coins.",
    'one_round_left_fight': "You still have a round before your next fight starts.",
    'entrance_fee_coin_not_enough': "You do not have {coins} coins to pay the entrance fee.",
    'prompt_pay_entrance_fee': "Pay entrance fee of {coins} coins to sign up for the Class {c} tournament? It will be {var.tourney_rounds[c]} round tournament with each battle one round apart.",
    'dueling_hiatus': "You still have to wait {self.get('dueling_hiatus')} rounds to duel again.",
    'prompt_duelist_range': "Duel with class {c} duelist between levels {lvlrange} with reward of {coins} coins?",
    'prompt_student_duelist': "Fight level {var.student_cblvl} Duelist in Training?",
    'gained_vp_donation': "You have gained {add_vp} VP for your donation!",
    'lost_vp_donation': "You lost {add_vp} somehow at the Starfex Ancient Magic Museum",
    'sold_item_donated': "The {self.lmap.m(item)} you sold is being donated to the Ancient Magic Museum in Starfex.",
    'museum_mx_capacity': "The museum has reached its max capacity of {self.lmap.m(fragment)}, you may be able to sell to the marketplace for some value, or wait for someone to purchase these.",
    'invalid_fragment': "You do not have {self.lmap.m(fragment)} in your inventory to donate!",
    'cannot_resell_fragments': "You cannot donate these {self.lmap.m(fragment)}s after having purchased them from the Ancient Magic Museum.",
    'museum_gratitude': "The Ancient Magic Museum thanks you for your donation of a {self.lmap.m(fragment)}!",
    'donation_coin_reward': "You were rewarded {coins} coins!",
    'receive_book_from_donation': "Receiving a {self.lmap.m(book_reward)}!",
    'fragment_donated_send': "The Ancient Magic Museum has received a {self.lmap.m(fragment)} donation",
    'drop_quest_prompt': "Drop your current quest at {raq['area']}?",
    'min_artifact_req': "You need at least {min_reputation_needed} Reputation to start Rare Artifact finding quests.",
    'artifact_lead': "There is a lead on a rare artifact in {self.lmap.m(area)} about {distance} tiles away. Successful retrieval would reward you {var.rare_artifact_details[area]['coins']} coins.",
    'haggling_saved_coins': "Your haggling saved you {subtract_cost} coins!",
    'username_purchased_fragments': "{username} purchased all of the {self.lmap.m(fragment).title()} from the Ancient Magic Museum!",
    'purchase_six_fragments_prompt': "Purchasing all 6 of these fragments costs {cost} - which you do not have!",
    'need_six_spots_fragments': "You need at least 6 free item space to purchase 6 {self.lmap.m(fragment)}s.",
    'purchased_fragments_confirmed': "You purchased the {self.lmap.m(fragment)}s!",
    'min_fellvp_fragments': "You need at least {var.starfex_use_fragments[fragment]['fellowship']} Fellowship VPs to be entrusted with these fragments.",
    'not_enough_coins_for_fragments': "Purchasing all 6 of these fragments costs {cost} - which you do not have!",
    'smithing_elevation': "You have been promoted to Class {ac} at the Smithing Guild!",
    'smithing_demotion': "You have been demoted to Class {ac} at the Smithing Guild.",
    'gift_req_smithing_complete': "You have completed the gifting requirement for Class {c2p}!",
    'succ_ore_gifted': "Successfully gifted {self.lmap.m(ore_gifted)} to the Smithing Guild.",
    'quest_tasks_remaining_left': "You have {qtr} left.",
    'started_quest_c': "You have started the Class {c} quest: {quest}",
    'convinced_city_smithers': "You have already convinced the smithers at: {convinced_cities}",
    'persuade_smith_for_guild': "{self.player.currenttile.tile.title()} is {distance} tiles away from Tamarania and has {tension} tension. Convince probability is persuasion/{denominator}. Attempt to persuade?",
    'ore_lost_random': "Don't know what happened, but you no longer possess the {self.lmap.m(ore)} ore.",
    'no_rare_to_give': "You do not possess any {self.lmap.m(rare)} to give.",
    'item_not_possessed': "Don't know what happened, but you no longer possess {self.lmap.m(item)}.",
    'additional_smithing_req': "You cannot enchant {self.lmap.m(item)} with your current Smithing Guild Class",
    'enchant_active_rounds': "You now have {self.enchant_descriptions[item]['description']} enchantment active for {rounds_enchanted} rounds.",
    'enchant_failed': "You failed to enchant. {self.lmap.m(item).title()} is destroyed.",
    'enchantment_lost': "You lost the enchantment: {self.enchant_descriptions[item]['description']}",
    'fragments_not_possessed_for_smithing': "You do not possess at least 6 {self.lmap.m(fragment)}s to build the sword!",
    'skill_sword_building_not_met': "You do not meet the minimum skill requirement of {fd['smithing']} smithing and {fd['heating']} heating to build the sword!",
    'do_not_possess_item_for_sword': "You do not possess at least {fd['amt']} of {self.lmap.m(fd['item'])} to build the sword!",
    'build_sword_succ': "You successfully built the {self.lmap.m(sword)}!",
    'build_sword_failed': "You were not able to build the {self.lmap.m(sword)}.",
    'cost_renew_mem_not_there': "You do not have the {cost} coins with you to renew your membership!",
    'cost_auto_deducted': "The Wizard Tower auto-deducted {cost} coins from you to renew your membership.",
    'cost_not_there_demetry': "You do not have enough coins with you and at your Demetry market to renew your membership!",
    'withdraw_coins': "Withdrew {withdraw} from you market earnings to pay for your Wizard Tower auto-renewal membership",
    'auto_deduct_also_with_withdrawal': "The Wizard Tower also auto-deducted {cost-withdraw} coins to complete your {self.lmap.m(self.get('membership'))} membership renewal",
    'mrr_remaining': "Your membership will cancel in {self.get('membership_rounds_remaining')} rounds",
    'cost_not_there_for_membership': "You do not have {cost} coins to purchase this membership!",
    'teleport_too_far': "This is too far for you to teleport with your {self.lmap.m(m)} membership! Try a different tile.",
    'fatigue_too_high_for_teleport': "You can't teleport here, it would cost you {fatigue} which is beyond your capacity at the moment",
    'craft_elixir_req': "You need at least {var.alchemy_properties[elixir]['crafting']} Crafting to craft this item.",
    'brewed_elixir_succ': "Successfully brewed {self.lmap.m(elixir)}.",
    'renew_market_toggle': "Turned renew with market earnings {toggle}.",
    'auto_renewal_toggle': "Turned auto renewal {toggle}.",
    'hunting_elevation': "Your Hunting Class has been Elevated to {c}!",
    'hunt_coin_awarded': "Awarded {coins} coins for completing the hunt!",
    'reject_hunt_prompt': "Reject this hunt? [{self.get('active_quest_details')['str']}]",
    'zinzibar_elevation': "You progressed to {self.lmap.m(field).title()} Class {lvl+1}!",
    'zinzibar_benefit': "You now have {var.zinzibar_class_effect[field][lvl+1]} for {var.zinzibar_class_benefit[field]}.",
    'field_activ_succ': "{self.lmap.m(field).title()} successfully activated!",
    'trag_damage': "You hit a trap and take {hp_dmg} HP damage and {ftg_dmg} Fatigue damage!",
    'fragment_found_': "You found a {self.lmap.m(fragment)}!",
    'loan_not_paid': "{self.get('loan_amount')} coins have been deducted.",
    'bought_invest_widget_item': 'Bought {self.lmap.m(item)} for {cost} coins.',
    'max_skill_reached_xp': 'Cannot level {lmap.m(skill)} beyond {previousLevel} by adding XP!',
    'loan_options': 'Here are your loan options for a period of {loan_length} rounds.',
    'musuem_coin_awarded_rare_artifact': 'You brought the rare artifact to the Ancient Magic Museum and are awarded {coins} coins!',
    'membership_expiring_soon': "Your {self.lmap.m(self.get('membership'))} Wizard Tower membership will be removed in {mrr} rounds if you don't renew.",
    'convert_item_prompt': "Convert {self.lmap.m(from_item)} to {self.lmap.m(to_item)}?",
    'lost_ing_elixir_failure': "Failed to craft {self.lmap.m(elixir)} - the brew blew up and you lost {self.lmap.m(ing_rand)}.",
    'zinzibar_train_class_req': "Training {self.lmap.m(field).title()} requires at least level {req_lvl} {self.lmap.m(var.zinzibar_req[field])}",
    'skill_too_low': 'Your {self.lmap.m(skill)} level is too low to learn from this {self.lmap.m(level)} book!',
    'skill_too_high': 'Your {self.lmap.m(skill)} level is too high to learn from this {self.lmap.m(level)} book!',
    'confirm_membership_cost': 'Confirm {self.lmap.m(membership)} membership for {cost} coins',
    'cant_enchant_anymore': "It is not possible for you to apply any more enchantments for this {'Weapon' if space==0 else 'Armor'}", # When translating this, please translate the sub-text 'Weapon' and 'Armor' to make grammatical sense when embedded
    'need_piece_enchant': "You need a reinforcement piece smithed at slot {enchant_slot} to enchant this {'Weapon' if space==0 else 'Armor'}", # Same thing for this pelase
    'enchant_success': "You successfully enchanted the {'Weapon' if space==0 else 'Armor'}", # and this please.
}
# When translating these quest_texts, note that "quote" are things the character (who initiated the quest) will say, whereas "direction" narrates to the player what to do next. Leave the 'default' and 'eval' keys and their values in-place, unchanged, if you see them. Also, if you see variables in {} under the direction key, do not translate it, but allow it to make grammatical sense when filled in.
quest_texts = { (1, 1): [{'quote': "I am so worried about my cat...", 'direction': "Click the `Find Pet` button in the action grid until you find the pet."}],
                (1, 2): [{'quote': "My place is a mess...", 'direction': "Click the `Clean House` button in the action grid a total of 4 times."}, {'quote': "Thats very kind of you to help clean my place!", 'direction': "Continue cleaning the house by clicking `Clean House` in the action grid. ({amt}/4 done)"}],
                (1, 3): [{'quote': "Something has got me spooked, could you stay with me?", 'direction': "Click the `Gaurd Home` button in the action grid."}, {'quote': "I am scared to spend the night alone. Could you please stay once more?", 'direction': "Click the `Gaurd Home` button in the action grid once more."}],
                (1, 4): [{'quote': "It would be amazing if you could build me a crafted item!", 'eval': "two_craftable_items()", 'direction': 'Get two craftable items, for example, `string` or `beads`.'}, {'quote': "It looks like you have two craftable items in your bag!", 'eval': "one_craft_item()", 'direction': "Navigate to your bag and click `Craft` on one craftable item, then follow the prompts. This will initiate your Crafted item."}, {'quote': "Looks like you started building a craft! I can't wait to see it.", 'eval': "has_crafted_item()", 'direction': "Add the second item to your initiated Crafted item by clicking `Craft` and following the prompts. If its destroyed, find another item and try again!"}, {'quote': "Wow, is that a crafted item in your bag?", 'direction': "Click `Gift Craft` button in the action grid to try and pursuade them to accept your craft."}],
                (1, 5): [{'quote': "Lets spar together! Where is your weapon though?", 'eval': "has_weapons()", 'direction': "You can click `Spar with Boy` in the action grid but we recommend smithing a weapon first (click the smithing area to find out more)."}, {'quote': "Yes, lets spar!", 'direction': "Click `Spar with Boy` in the action grid."}],
                (1, 6): [{'quote': "I would love to read a knowledge book...", 'eval': "checkBook()", 'direction': "Find a knowledge book to gift to the boy. A good place to look are old libraries, outside your city."}, {'quote': "You got a book there I see! How I wish I had one...", 'direction': "Gift a book to the boy by clicking the `Gift Book` action button."}],
                (1, 7): [{'quote': "My dad bought me a sandbox, but we never got sand...", 'eval': "'sand' in lclPlayer().items", 'direction': "Find some sand to gift to the boy. Try searching the markets or outposts (outside your city)."}, {'quote': "Did you get some sand?", 'direction': "Click the `Gift Sand` action button in your action grid to gift the sand."}],
                (1, 8): [{'quote': "Baby mammoths are more common than you may think!", 'direction': "Go to any plains with fruit in your bag, and excavate for a chance at finding a baby mammoth."}, {'quote': "Is that a baby mammoth you got with you?", 'direction': "Return to your city, then click the `Give Baby Mammoth` button in the action grid."}],
                (2, 1): [{'quote': "Go out to the mountains, the only place to find cooling cubes. I dare not go, its trecherous up there.", 'direction': "Go to any mountain and ascend to the second tier of the mountain. Be careful though, it can be trecherous up there!"}, {'quote': "Did you make it to the second mountain tier? Brave soul...", 'direction': "On the second mountain tier, click the `Find Mountain Trader` action button to attempt to find them."}, {'quote': "You found a mountain trader? Whoah, never in my life have I managed it alone. I always had help.", 'direction': "Purchase a single cooling cube for 3 coins from the mountain trader, on the second tier of the mountain."}, {'quote': "Amazing, did you get a cooling cube? Nice, lets apply it!", 'direction': "Go back to your city then click the `Apply Cubes` action button to begin applying cubes"}, {'quote': "It just needs one more touch.", 'direction': "Finish applying the cooling cubes at your city by clicking the `Apply Cubes` action button."}],
                (2, 2): [{'quote': "I recommend hiding out and waiting for the robber to show up.", 'direction': "Click the `Wait for Robber` action button until you finally find them. Battle with them."}],
                (2, 3): [{'quote': "Thanks for agreeing to protect me. Off we go!", 'direction': "Go to the city highlighted in blue. Stealth will not work during your journey."}],
                (2, 4): [{'quote': "Lets go eliminate that serpent. Together it should stand no chance.", 'direction': "Go to the blue highlighted pond tile with the companion within 3 rounds. Click `Excavate` once there to find the Mother Serpent. Battle and defeat it."}, {'direction': "You have {amt} rounds left to find and defeat the Mother Serpent at the blue highlighted pond. Otherwise the quest will need to be restarted."}],
                (2, 5): [{'quote': "I lost my book in the old library nearby. The hermit there should know where it is.", 'direction': "Go to the blue highlighted old library tile. A hermit may automatically find you, otherwise `Excavate` for them. Persuade them for the book."}, {'quote': "Is that the book in your pocket?", 'direction': "Return to your city and click the `Give Book` action button to complete the quest."}],
                (2, 6): [{'quote': "The letter of upmost importance. Please transport it as soon as possible.", 'direction': "Take letter to the city highlighted in blue on the board page. Be mindful, highway robber encounter chance are doubled."}],
                (2, 7): [{'quote': "The sparring area is in need of new weapons.", 'direction': "Smith two rank 2 weapons one at a time, gifting them once ready."}, {'quote': "Nice, you made one. If we could get one more- it would really make a difference for those training here.", 'direction': "Smith one more rank 2 weapon and gift it to the sparring area."}],
                (2, 8): [{'quote': "There are two masters of stealth in all of Valdhomir. One in Enfeir and Zinzibar.", 'direction': "Go to either Enfeir or Zinzibar and persuade the master of stealth to write a book."}, {'quote': "You were able to convince them? Wow, I am surprised you even found them.", 'direction': "You have {amt} rounds left before the book is ready. Return to {city} once done to pick it up."}, {'quote': "You think they finished writing the stealth book?", 'direction': "The stealth book is ready at {city}! Go back to pick it up."}, {'quote': "Is that really the book?", 'direction': "Return to your city and give the book to quest giver."}],
                (3, 1): [{'quote': "There are many folks around here that are food insecure.", 'direction': "Distribute 10 pieces of either fruit or cooked food at your home city."}, {'quote': "Your work is trully amazing, I wish you great success!", 'direction': "Continue distributing fruit or cooked food at your city. ({amt}/10 done)"}],
                (3, 2): [{'quote': "To the top of the mountain adventurers, go go go!", 'direction': "Take the 3 adventurers to any mountain, and climb to top tier. Dont visit any cities!"}, {'quote': "What are you doing here adventurer??", 'direction': "`Excavate` any mountain, at any tier, and collect ores worth a total of 5 coins. ({amt}/5 so far)"}, {'quote': "What are you doing here adventurer??", 'direction': "Go to any plains tile and `Excavate` 5 pieces of meat. ({amt}/5 found)"}],
                (3, 3): [{'quote': "We can learn much from monks, and lucky for us, they are the best teachers. They are just hard to find.", 'direction': "Go to any mountain and `Excavate` for a Monk. Persuade them to come with you to your city."}, {'quote': "It is so amazing to train with the Monk.", 'direction': "Train with the monk at your city a total of 3 times. ({amt}/3 done)."}],
                (3, 4): [{'quote': "There is a monster, I know it. We just cant find it.", 'direction': "Click the `Search for Monster` action button at your home city to find the monster. Defeat it for a greater reward."}],
                (3, 5): [{'quote': "Teach a man to fish, feed him for a lifetime.", 'direction': "Teach 6 villagers to fish by clicking the `Teach Fishing` action button."}, {'quote': "These men will forever remember what you are doing for them.", 'direction': "Teach 6 villagers to fish by clicking the `Teach Fishing` action button. ({amt}/6 done)"}],
                (3, 6): [{'quote': "How are you here? Did you abandon the battlefield?", 'direction': "Defeat 3 opponents! You are given a round to rest in the middle."}, {'quote': 'How are you here? Did you abondon the battlefield?', 'direction': "Use this round to rest. You can also eat."}],
                (3, 7): [{'quote': "Crafting. A noble profession which has made many wealthy. Your help could empower our people.", 'direction': "Once you have three crafting books in your bag, click `Gift Craft Books` in the action grid at your city."}],
                (3, 8): [{'quote': "Time to make some glass.", 'direction': "Bring 10 pieces of sand. You can do it one at a time or bulk. Click `Deliver Sand` when ready. (0/10 done)"}, {'quote': "Nice, keep the sand coming!", 'direction': "Bring 10 pieces of sand. You can do it one at a time or bulk. Click `Deliver Sand` when ready. ({amt}/10 done)"}],
                (4, 1): [{'quote': "Information is contained in books. Knowledge is understanding it correctly. Wisdom is its correct practice.", 'direction': "Click the `Fill Library` action button to hand over unique knowledge books. (0/5 done)"}, {'quote': "Information is contained in books. Knowledge is understanding it correctly. Wisdom is its correct practice.", 'direction': "Click the `Fill Library` action button to hand over unique knowledge books. ({amt}/5 done)"}],
                (4, 2): [{'quote': "These warriors like to remain hidden. If they hear you are looking for them, they may get spooked. Your best bet is to find them before they hear of you.", 'default': {'amt': 0}, 'direction': "You need to find 7 warriors in unique cities. Click the `Find Warrior` action button when there. You only get one chance per city! ({amt}/7 done)"}],
                (4, 3): [{'quote': "I could probably convince them eventually, it would take a long time. They want to see people like them.", 'default': {'amt': 0}, 'direction': "Click the `Convince a Market Leader` action button. This takes a major action. You need to convince 6. ({amt}/6 done)"}],
                (4, 4): [{'quote': "Convincing the traders that our gates are open is a big step to a better economy.", 'direction': "Once you find a Trader on the road, a `Persuade` action button should appear after clicking `Trader`. Convince 3 of them. ({amt}/3 done)", 'default': {'amt': 0}}],
                (4, 5): [{'quote': "Its time we begin making peace.", 'direction': "Choose a city to reduce tensions with (your options are listed on the Skirmish board). Go there and begin finding leaders."}, {'quote': "So you have chosen the city to reduce tensions with? I hope you chose wisely... for all our sakes.", 'direction': "Convince a total of 5 leaders at {city} by clicking the `Find & Convince Leader` action button. ({amt}/5 done)"}],
                (4, 6): [{'quote': "Ancient knowledge is stored away in the ruins of old villages. They were destroyed by large battles long ago with the bandits.", 'direction': "Go to any ruins tile and `Excavate` for old tattered books. You need a minimum of 2 and can hold a max of 4. ({amt} holding)", 'default': {'amt': 0}}, {'quote': "Were you able to find some ancient books?", 'direction': "You have found {amt} ancient tattered books at the ruins. You can return to your city to complete the quest, or find up to 4."}, {'quote': "Whoah, is that a whole bag full of tattered books? How amazing!", 'direction': "You have found the maximum number of ancient tattered books. Return to your city to complete the quest."}],
                (4, 7): [{'quote': "Lots to do, very little time.", 'direction': "Click `Deliver Material` to hand over required home renovation items. ({bark}/5 bark, {clay}/3 clay, {glass}/3 glass, {leather}/6 leather)", 'default': {'bark':0,'clay':0,'glass':0,'leather':0}}],
                (4, 8): [{'quote': "These monsters are getting out of control. Rally the warriors!", 'direction': "Convince 3 warriors in 4 different cities - {birthcity} ({amtb}/3), {city1} ({amt1}/3), {city2} ({amt2}/3), {city3} ({amt3}/3)", 'default': {'birthcity': 'Your City', 'city1': 'Not Chosen', 'city2': 'Not Chosen', 'city3': 'Not Chosen', 'amtb':0, 'amt1':0, 'amt2':0, 'amt3':0}}],
                (5, 1): [{'quote': "A gold dagger may not sound useful, but its more symbolic than anything else.", 'direction': "Go to the wilderness tile and `Excavate` - a `Rare Find` will give you lost gold."}, {'quote': 'Were you able to find the gold?', 'direction': "Persuade the smither at your city to smith the gold ingot into a dagger."}],
                (5, 2): [{'quote': "He could be anywhere, my friend. He was out on a mission, and its time for him to come home and report in.", 'direction': "Any tile where the `Excavate` option is possible is a place the Friend could be. Click `Excavate` to find him. ({amt}/78 searched)", 'default': {'amt':0}}, {'quote': "Is that him standing next to you?", 'direction': "Return to your city to bring the friend home."}],
                (5, 3): [{'quote': "Its a show of strength. If you defeat it, our neighboring cities will think twice about attacking us.", 'direction': "Go to any wilderness tile, a lvl 135 Wild Vine Monster should attack. Defeat it."}],
                (5, 4): [{'quote': "I have heard of their existence, but have never seen them before. These rare ores.", 'direction': "Find and bring two of the following items to the mayor: Shinopsis, Astatine, Ebony, and Promethium."}],
                (5, 5): [{'quote': "Perhaps with the haggling master's teachings, I can pass on better marketing strategy to our people.", 'direction': "Go to Demetry and persuade the haggling master. Pay him 40 coins upon success."}],
                (5, 6): [{'quote': "There is a big mammoth ravaging Valdhomir. I trust you to take care of it.", 'direction': "Go to the blue highlighted plains tile. `Excavate` to find the Lv150 mammoth. Defeat it."}, {'quote': "Were you able to defeat it? Amazing.", 'direction': "Go back to the mayor to claim your reward for defeating the mammoth."}],
                (5, 7): [{'quote': "Whatever I learn, I will pass on to my people.", 'direction': "Go to {city} to convince the stealth master to teach the mayor. You only have 2 chances. ({amt}/2 used)", 'default': {'city': 'enfeir or zinzibar', 'amt': 0}}],
                (5, 8): [{'quote': "The most valuable craft. It would do well to decorate these halls.", 'direction': "Create a crafted item with the following materials: Gems, Rubber, Glass, Ceramic, Leather, Scales, and Beads."}],
               }
misc_quest_texts = {'rescue': {'name': 'Rescue Mission', 'text': "Rescue the injured survivor by bringing them to {city} (highlighted in yellow on the board)! [rounds left: {rounds}]"},
                    'escort': {'name': 'Escort Mission', 'text': "Escort the vulnerable person. Bring them to {city} (highlighted in light green on the board). [rounds left: {rounds}]"},
                   }
# Similar to before, please do not translate anything in the {} - but rather allow the translation to appear seemless, or flow nicely, once the variables are filled in. Also, please do not translate file paths (i.e. under the 'img' key). Also, please do not translate values under the 'formula' key.
boost_texts = { 
                'vegetables': {'img': 'items/vegetables.png', 'text': 'Running away from combat fatigue is halved (rounded down). Rounds Left: {rounds}.'},
                'cognifruit': {'img': 'items/cognifruit.png', 'text': 'Critical Thinking boosted by {points} points. Rounds Left: {rounds}.'},
                'haggleroot': {'img': 'items/haggleroot.png', 'text': 'Haggling boosted by {points} points. Rounds Left: {rounds}.'},
                'swayleaf': {'img': 'items/swayleaf.png', 'text': 'Persuasion boosted by {points} points. Rounds Left: {rounds}.'},
                'handiherb': {'img': 'items/handiherb.png', 'text': 'Crafting boosted by {points} points. Rounds Left: {rounds}.'},
                'blazeberry': {'img': 'items/blazeberry.png', 'text': 'Heating boosted by {points} points. Rounds Left: {rounds}.'},
                'forgeflower': {'img': 'items/forgeflower.png', 'text': 'Smithing boosted by {points} points. Rounds Left: {rounds}.'},
                'cloakmoss': {'img': 'items/cloakmoss.png', 'text': 'Stealth boosted by {points} points. Rounds Left: {rounds}.'},
                'vitalvine': {'img': 'items/vitalvine.png', 'text': 'Survival boosted by {points} points. Rounds Left: {rounds}.'},
                'pluckpetal': {'img': 'items/pluckpetal.png', 'text': 'Gathering boosted by {points} points. Rounds Left: {rounds}.'},
                'findersfern': {'img': 'items/findersfern.png', 'text': 'Excavating boosted by {points} points. Rounds Left: {rounds}.'},
                'weapon': {'img': 'assets/{cbstyle_lower}.png', 'text': '+{points} {cbstyle} Attack.'},
                'weapon enchant': {'img': 'assets/{cbstyle_lower}_enchanted.png'},
                'armor': {'img': 'assets/armor.png'}, #, 'formula': "', '.join(['+'+str(points)+' '+lmap.m(def) for def, points in def_list.items()])"},
                'armor 1 enchant': {'img': 'assets/armor_enchanted.png'},
                'armor 2 enchant': {'img': 'assets/armor_enchanted.png'},
                'tongue enchantment': {'img': 'assets/tongue_enchantment.png', 'basic': '1/3 chance of using 1 level higher in Persuasion and Haggling. Rounds Left: {rounds}', 'gold': '90% chance for 1 level higher in Persuasion and Haggling. Rounds Left: {rounds}', 'platinum': 'Either 1 or 2 levels higher in Persuasion and Haggling. Rounds Left: {rounds}'},
                'elixir of feasting': {'img': 'items/elixir_of_feasting.png', 'text': "Raw meat or fish you gather instantly gets heated into well cooked. Rounds Left: {rounds}."},
                'elixir of cognition': {'img': 'items/elixir_of_cognition.png', 'text': "Critical thinking success chance is 100%. Rounds Left: {rounds}."},
                'elixir of vigor': {'img': 'items/elixir_of_vigor.png', 'text': "No fatigue or HP damage taken (except combat). Rounds Left: {rounds}."},
                'elixir of shadow': {'img': 'items/elixir_of_shadow.png', 'text': "Stealth success and sneak attack chance are 100%. Rounds Left: {rounds}."},
                'elixir of forging': {'img': 'items/elixir_of_forging.png', 'text': "Can smith any ore. Rounds Left: {rounds}."},
                'elixir of abundancy': {'img': 'items/elixir_of_abundancy.png', 'text': "Market sells all items. Rounds Left: {rounds}."},
                'elixir of merchants': {'img': 'items/elixir_of_merchants.png', 'text': "Can successfully sell any item in your market. Rounds Left: {rounds}."},
                'elixir of retention': {'img': 'items/elixir_of_retention.png', 'text': "Retain the most valuable item from crafting when sold. Rounds Left: {rounds}."},
                'elixir of certainty': {'img': 'items/elixir_of_certainty.png', 'text': "Can excavate 3 of any item 100% of the time. Rounds Left: {rounds}."},
                'elixir of harvest': {'img': 'items/elixir_of_harvest.png', 'text': "Can gather 3 of any crop 100% of the time. Gathering does not deplete the tile. Rounds Left: {rounds}."},
                'water sword': {'img': 'items/water_sword.png'},
                'air sword': {'img': 'items/air_sword.png'},
                'earth sword': {'img': 'items/earth_sword.png'},
                'fire sword': {'img': 'items/fire_sword.png'},
                'ice sword': {'img': 'items/ice_sword.png'},
                'light sword': {'img': 'items/light_sword.png'},
                'blood sword': {'img': 'items/blood_sword.png'},
                'death sword': {'img': 'items/death_sword.png'},
            }


def stringify_dict(d):
    return ', '.join([f'{k}: {v}' for k, v in d.items()])

hallmarks = {
    'anafola':
        {'hallmark': 'Castle of Conjurors',
        'attribute': 'castle_of_conjurors',
        'primary': 'creature_class',
        'secondary': 'creature_bond',
        'font': 'Consolas',
        'description': 
"""Conjure creatures who grow strong with companionship yet prefer to avoid combat.

Come to Anafola's Castle of Conjurors to create a summoning contract with a creature.
Fulfilling your request takes some time, but its 2x faster if you are Anafola-born.

For every round you do not engage in battle and have the creature as a companion,
the creature's bond with you increases at a certain rate each round (see table).
    - The maximum rate is 85.
    - Rate is 1.25x greater for Anafola-born, without increasing dropped bond rate.
    - Your effect probability also increases with your bond (see combat paragraph).

When your bond level reaches 1000, your conjuring class increases. This means
you can return to the Castle of Conjurors and request a stronger class creature.
    - Your class is not promoted until your next creature class is received.

Combatting with the creature will help you deal damage and take hits for you.
    - Your effect probability is the chance that the creature will attack or take a hit.
    - If your creature takes a hit, you can only recover his HP through resting.
        > Their HP recovery rate is half of yours.
    - Engaging in combat drops your bond by 2x the bond increase rate.
    - Your bond temporarily ceases to increase after combat for 3 rounds.
    - Losing a battle ceases bond increase for 10 rounds.

The creature will help you harvest crops and excavate.
    - The additional support your summoner provides = 
        (base chance of harvesting/excavating success) * effect_probability 

You can release the creature from your summoning contract at Anafola anytime.
    - You can always retrieve them back when you are ready, even if you promote.
    - Doing so will simply pause your bond progress, but will not penalize it.
    - You may want to do so if your adventure will likely cause you to lose bond.
    - You may also choose to revert to your old class creatures to use them in combat.

+------------------------+---------+---------+---------+---------+---------+
| Values                 | Class 1 | Class 2 | Class 3 | Class 4 | Class 5 |
+------------------------+---------+---------+---------+---------+---------+
| VP                     |       0 |       1 |       2 |       3 |       4 |
+------------------------+---------+---------+---------+---------+---------+
| Min Fulfillment Rounds |       7 |       5 |       3 |       1 |       0 |
| Max Fulfillment Rounds |      10 |       8 |       6 |       4 |       2 |
+------------------------+---------+---------+---------+---------+---------+
| HP                     |       2 |       4 |       6 |       8 |      10 |
| Attack                 |       1 |       2 |       3 |       4 |       5 |
| Min Effect Probability |      0% |      6% |     12% |     18% |     24% |
| Max Effect Probability |     12% |     24% |     36% |     48% |     60% |
+------------------------+---------+---------+---------+---------+---------+
| Bond Increase Rate     |      30 |      10 |       4 |     2.5 |     1.5 |
+------------------------+---------+---------+---------+---------+---------+
"""
        },
    'benfriege': 
        {'hallmark': 'Grand Library',
         'attribute': 'grand_library',
         'primary': 'read_fatigue',
         'secondary': 'read_action_counter',
         'description': 
"""At this library you can read books or check them out from a choice of six random books per round.

Not all skill books have the same chance of being available - the chances are as follows:
    > x1 chance for Critical Thinking and Stealth.
    > x2 chance for Haggling, Persuasion, Crafting, Smithing, Excavating, and Survival.
    > x3 chance for Heating and Gathering.

You incur a minor action when reading or checking out.

  - Read Books: Gain fatigue equal to your reading fatigue. You can clear this fatigue by reducing your
                read counter to zero, which takes 2 consecutive major actions to reduce by 1.
                Keep in mind, reading knowledge books counts as as part of your read counter.
        > Increase your consecutive reading counter by one, which increases reading fatigue
        > Beginner (lvl 0-3): 1xp - Success between Critical Thinking 0-4
        > Intermediate (lvl 4-5): 1xp - Success between Critical Thinking 1-8
        > Advanced (lvl 6-7): 1xp - Success between Critical Thinking 2-12
                   
  - Checkout Books: A trainer must teach you the book. Following checkout,
    go to an adept or master trainer of that skill to study and learn it.
    * Note: Benfriege-born get +1 xp when learning from books in this way.
        > Beginner (lvl 0-3): 3xp for 2 coin
        > Intermediate (lvl 4-5): 4xp for 3 coins
        > Advanced (lvl 6-7): 4xp for 4 coins"""
        },
    'demetry':
        {'hallmark': 'Grand Bank',
         'attribute': 'grand_bank',
         'primary': 'credit_score',
         'secondary': 'loan_amount',
         'description':
"""This bank provides no interest loans, the amount depending on your credit and reputation.

  - Maximum amount of Loan: Credit Score + (Reputation / 2) + 1 (+2 if Demetry-born).
  
  - Length of Loan: 10 rounds + persuasion skill (+2 if Demetry-born).
  
  - If the money is returned between 5 rounds and the original length of the loan:
        > Credit Score increases by the loan amount.
  
  - You must be present at Demetry to return the loan.
  
  - It is possible to extend the loan by 5 rounds after the end of term:
        > If your credit score is zero then you are given no redemption period (skip strikes below).
        > 1st Strike: (persuasion / 12) chance of no impact on credit score, otherwise 25% cut.
        > 2nd Strike: (persuasion / 18) chance of no impact on credit score, otherwise 75% cut.
  
  - Consequence for failing to repay the bank after all chances given:
        > You can no longer bank at the Grand Bank and credit score goes to -1.
        > Your coins are automatically deducted to match the loan amount.
        > If you do not have enough coins:
            > Your homes are sold to the bank from least expensive to most until nothing is owed.
        > If you still owe the bank money, then the rest of the owed amount is forgiven."""
        },
    'enfeir':
        {'hallmark': 'Reaquisition Guild',
        'attribute': 'reaquisition_guild',
        'primary': 'class',
        'secondary': 'request_active',
        'description':
"""Formerly the thieves guild, reformed for the greater good. Also nicknamed the detective guild.

Retrieve stolen valuables of common folk who come bearing evidence of their ownership 
and last known whereabouts. The longer ago it was lost, the harder it is to find.

Be sure not to unsettle the civilians with your investigation! You could fail the quest.

Quests involve following a trail of clues that lead to a final destination.
    > Weak clues point to three possible locations.
    > Strong clues point to two possible locations.
    > Definitive clues point to a single possible location.

Your intuition score = Stealth + Cunning + Persuasion + Excavating + Successes
    > Successes is the number of successful clue trails you have completed (start to finish)

Your intuition allows you to make progress each time you investigate. Once enough progress is made, you'll either discover a critical clue or find the valuable.

Class 1:
    - Skill Reqs: 2 Stealth + 2 Cunning
    - Join Req: Find a citizen's lost ring (waived for Enfeir-born citizen).
    - Trail Length: One location
    - Coins rewarded: 4c
    - Prior promotion rewards (3 total): (1-2) +3 Stealth xp, (3) +1 Cunning (max 8).

Class 2 (+1 VP):
    - Skill Reqs: 5 Stealth + 5 Cunning + 2 Persuasion
    - Promotion Req: 3 class 1 successes
    - Trail Length: Two locations
    - Coins rewarded: 10c
    - Prior promotion rewards (5 total): (1-2) +1 Cunning (max 10), (3-4) +4 Persuasion xp, (5) +5 Stealth xp.

Class 3 (+2 VP):
    - Skill Reqs: 8 Stealth + 8 Cunning + 4 Persuasion
    - Promotion Req: 5 class 2 successes
    - Trail Length: Three locations
    - Coins rewarded: 22c
    - Prior promotion rewards (4 total): (1) +1 Cunning (max 11), (2) +1 Stealth lvl (max 11), (3-4) +5 Persuasion xp.

Class 4 (+3 VP):
    - Skill Reqs: 10 Stealth + 10 Cunning + 6 Persuasion
    - Promotion Req: 4 class 3 successes
    - Trail Length: Four locations
    - Coins rewarded: 42c
    - Prior promotion rewards (3 total): (1) +1 Cunning, (2) +1 Stealth lvl, (3) +6 Persuasion xp.

Class 5 (+4 VP):
    - Skill Reqs: 12 Stealth + 12 Cunning + 8 Persuasion
    - Promotion Req: 3 class 4 successes
    - Trail Length: Five locations
    - Coins rewarded: 64c
"""
        },
    'fodker':
        {'hallmark': 'Defenders Guild',
        'attribute': 'defenders_guild',
        'primary': 'class',
        'secondary': 'villages_protected',
        'description':
"""After the bandits burned their villages to the ground, they have devoted themselves to defending the land from them.

Joining this guild is for the honor, not for the reward. Though, as you progress the ranks, the world will recognize you.

You will be asked to travel to different cities and convince (persuasion) the city counsel to provide resources and aide.
To meet one requirement in promote to the next class, choose one city from the list:
    - [0 VP] Class 1 promotion (denominator = 4): Benfriege, Glaser
        > Fodker citizens do not require this.
        > For Non-Fodker born, doing this requires either visiting the Defenders Guild or "seeing" a village under attack.
    - [1 VP] Class 2 promotion (denominator = 8): Kubani, Enfeir, Zinzibar
    - [2 VP] Class 3 promotion (denominator = 12): Anafola, Demetry
    - [3 VP] Class 4 promotion (denominator = 18): Starfex, Tutalu
    - [4 VP] Class 5 promotion (denominator = 30): Tamariza, Tamarania
    * Denominator subtracted by 1 if born from that city, or 3 if you have completed at least one Stage 4 quest.

Depending on your defending class you will be assigned different targets in a mission.
You travel in a caravan together with 2 companions to the bandit outpost and face your target with combined force.
You need to defeat two in order to meet promotion requirements.
    - Class 1 target: Bandit Rallier (Lv 35-40)
    - Class 2 target: Bandit Instigator (Lv 65-75)
    - Class 3 target: Bandit Leader (Lv 105-115)
    - Class 4 target: Bandit Brute (Lv 145-155)
    - Class 5 target: Bandit Champion (Lv 190-200)

Sometimes you will asked to defend villages from Bandit raiders!
    - Chance of receiving the message for help, wherever you are, is greater depending on your defender class.
        > You only have 2 rounds to get there.
        > Class 1: 6%, Class 2: 12%, Class 3: 24%, Class 4: 48%, Class 5: 96%
    - You fight between 2-4 bandits consecutively, whose combat level is close to your base combat.
    - Assisting gives you good deeds regardless of success.
    - 10% less chance that your production in this village will be lost to bandits (for each success).
    - Village invest cost reduced by a coin (if not already invested).
    - Successful defense will increase rest bonus at that village by one (max 3).
        > Only if your Defender's Class was 1 or higher when victorious.
    - For each village you successfully defend, a caravan route is opened for you.
        > Only if your Defender's Class was 2 or higher when victorious.
        > Will drop you off anywhere within 4 tiles for 1 coin and one major action.
        > No fatigue is taken.
        > Not available when being raided.
    - Final promotion requirements require you to protect a total number of villages as follows:
        > Class 1: 0 total, Class 2: 1 total, Class 3: 2 total, Class 4 : 4 total, Class 5: 8 total.

* Promotion requirements do not need to be completed in any specific order.""",
    'page 2': """Class Benefits:
    - Class 1: Reputation required to enter cities reduced by one (two for Fodker-born).
    - Class 2: Reputation requirement for purchasing Markets and Homes reduced by four (5 for Fodker-born).
    - Class 3: Purchasing markets reduced by two coins (3 for Fodker-born).
    - Class 4: Purchasing homes reduced by four (5 for Fodker-born).
    - Class 5: Village production becomes faster by a round.
        > +5% chance for protected villages to produce two items for each Bandit Champion defeated (max 40%).
    - Additionally, for each promotion, your village productions are 4% more likely to be saved from raids."""
        },
    'glaser':
        {'hallmark': 'Peace Embassy',
        'attribute': 'peace_embassy',
        'primary': 'class',
        'secondary': 'assignments_completed',
        'description':
"""Become an embassador of peace, negotiate with city hall counsels to reduce tensions.

Procedure:
    1) Accept an assignment from the Peace Embassy, which entails calling for better relations between two cities.
    2) You travel to one city, call the city counsel to better relations with the other city.
        Success Formula: (persuasion + Reputation/6 + peace_embassy_class + city_fellowship_class*2) / class_denominator
        - Benfriege Class: 1: 1 co, 2: 2 co, 3: 4 co, 4: 6 co, 5: 10 co, co = checked-out books learned from
        - Demetry Class: 1: 5 cs, 2: 10 cs, 3: 20 cs, 4: 40 cs, 5: 80 cs, cs = credit score
        - Kubani Class: 1: 1 VP, 2: 2 VP, 3: 4 VP, 4: 6 VP, 5: 10 VP
        - Zinzibar Class: 1: 1 VP, 2: 2 VP, 3: 4 VP, 4: 6 VP, 5: 10 VP
        - Starfex Class: 1: 1 VP, 2: 2 VP, 3: 4 VP, 4: 6 VP, 5: 10+ VP
        - Tamariza Class: 1: Basic, 2: Gold, 3: Platinum, 4: 3 Platinum renewals, 5: 7 Platinum renewals
    3) If successful with #2, you must then travel to the next city and similarly call them to better relations.
    4) Successfully calling both cities to better relations will:
        * Reduce tension between the two cities by 1.
        * Award you good deeds.
        * +1 Rest bonus for 10 rounds (12 rounds for Glaser-born).
        * Chance of being awarded gifts by citizens, or villagers in neighboring villages, when on the tile at round end.
            (this chance increases for Glaser-born citizens)

Class 1:
    - class_denominator: 8
    Tensions: Glaser <> Anafola | Benfriege <> Tutalu
Class 2 (+1 VP):
    - Need success in 2 assignments, 2 persuasion, and 20 Reputation for promotion.
    - class_denominator: 16
    Tensions: Kubani <> Demetry | Kubani <> Scetcher | Anafola <> Tamariza
              Benfriege <> Tamariza | Tamarania <> Zinzibar
Class 3 (+2 VP):
    - Need success in 2 assignments, 4 persuasion, and 40 Reputation for promotion.
    - class_denominator: 32
    Tensions: Starfex <> Tamarania | Fodker <> Pafiz | Demetry <> Tamariza
              Scetcher <> Pafiz | Tutalu <> Pafiz
Class 4 (+3 VP):
    - Need success in 3 assignments, 6 persuasion, and 60 Reputation for promotion.
    - class_denominator: 64
    Tensions: Demetry <> Scetcher | Fodker <> Scetcher | Anafola <> Starfex | Enfeir <> Tamarania
              Kubani <> Tamarania | Scetcher <> Tamariza | Tamariza <> Tutalu
Class 5 (+4 VP):
    - Need success in 5 assignments, 8 persuasion, and 80 Reputation for promotion.
    - class_denominator: 128
    Tensions: Anafola <> Tamarania | Demetry <> Tamarania | Pafiz <> Tamariza | Enfeir <> Zinzibar"""
        },
    'kubani':
        {'hallmark': 'Ancestrial Order',
         'attribute': 'ancestrial_order',
         'primary': 'progress',
         'secondary': 'has_horse',
         'description':
"""An ancient order that studies and teaches the arts of interacting with your environment.

There are three primary ancient knowledges: 1) Loot, 2) Food, and 3) Fatigue.
  > Each have 3 classes to progress through, completing the final class gives 2 VP.
There are also three exclusive ancient knowledges: 
  > 1) Minor Treading [Class 1], 2) Horse Riding [Class 2], and 3) Major Treading [Class 3].

Learning Requirements:
    - Kubani-born residents subtract 1 skill level requirement or 5 total knowledge requirement.
    
    * [Loot] Class 1: Lvl 2 Gathering | Class 2: Lvl 6 Gathering | Class 3: Lvl 10 Gathering
    * [Food] Class 1: Lvl 2 Heating | Class 2: Lvl 6 Heating | Class 3: Lvl 10 Heating 
    * [Fatigue] Class 1: Lvl 2 Survival | Class 2: Lvl 6 Survival | Class 3: Lvl 10 Survival
    * Minor Treading (class 1): 15 Total Knowledge
    * Horse Riding (class 2): 45 Total Knowledge
    * Major Treading (class 3): 80 Total Knowledge

Session Required to Progress (Major Action):
    * Class 1: 2 successful sessions; chance of success is Critical Thinking / 8
    * Class 2: 4 successful sessions; chance of success is Critical Thinking / 12
    * Class 3: 8 successful sessions; chance of success is Critical Thinking / 16

Learning Costs Per Session:
    - Kubani-born residents subtract 1 coin.
    - Note: "first" refers to the first ancient knowledge that you begin studying in that class bracket.
    - Note 2: The exclusive ancient knowledges have unique costs (they don't fall into the standard class cost).
    - Note 3: Reminder, these are per session costs - not complete cost! 
    - Note 4: You are only charged for successful sessions.
    
    * [Class 1] First: 1 coin, Remaining: 2 coins, Minor Treading: 3 coins.
    * [Class 2] First: 2 coins, Remaining: 3 coins, Horse Riding: 4 coins (purchase horse for 20 coins after).
    * [Class 3] First: 3 coins, Remaining: 4 coins, Major Treading: 5 coins.
    
Learning Benefits:
    * Loot: +15% Better Drops per class (+2VP at class 3)
    * Food: +1 Food Improvement per class (+2VP at class 3)
    * Fatigue: +1 Maximum Fatigue and Raise Fatigue Danger zone by 1 per class (+2VP at class 3)
    * Minor Treading: +2 Minor Actions + 1VP
    * Horse Riding: +3 Road Movements with a Horse + 1VP
    * Major Treading: +1 Major Action + 2VP"""
        },
    'pafiz':
        {'hallmark': 'Meditation Chamber',
        'attribute': 'meditation_chamber',
        'primary': 'class',
        'secondary': 'stored_energy',
        'font': 'Consolas',
        'description':
"""Meditate in chamber with Critical Thinking and Cunning masters to gain stored energy.
Stored energy can be activated into combat boosts (randomly assigned) for a short duration.

Meditation:
    > You can meditate for a maximum of 10 consecutive major actions.
    > No fatigue accrued when meditating.
    > Stopping between 6-8 actions is optimal and helps with class promotion.
    > The values in the table below describes your stored energy per action state.

    +--------+---------+---------+---------+---------+---------+
    | Action | Class 1 | Class 2 | Class 3 | Class 4 | Class 5 |
    +--------+---------+---------+---------+---------+---------+
    | 1      | 0       | 1       | 1       | 1       | 2       |
    | 2      | 1       | 2       | 3       | 3       | 5       |
    | 3      | 2       | 4       | 5       | 6       | 10      |
    | 4      | 3       | 6       | 8       | 11      | 16      |
    | 5      | 5       | 9       | 13      | 17      | 23      |
    |--------+---------+---------+---------+---------+---------|
    | 6      | 7       | 12      | 18      | 23      | 30      | }
    | 7      | 8       | 14      | 21      | 28      | 36      | } Optimal Zone
    | 8      | 9       | 16      | 23      | 32      | 41      | }
    |--------+---------+---------+---------+---------+---------|
    | 9      | 10      | 17      | 25      | 34      | 44      |
    | 10     | 10      | 18      | 26      | 35      | 46      |
    +--------+---------+---------+---------+---------+---------+

Before Activation:
    > Stored energy is not lost on the first round following meditation.
    > Otherwise, stored energy is lost at a rate of 2 per round.

Activation: 
    > Spend a minor action to activate your stored energy, wherever you are.
    > Your stored energy is transferred into combat boosts, randomly assigned to:
        > All attributes except Technique.
    > Combat boosts are lost at a rate of 5 per round (4 for Pafiz-born).
    > While you still hold these combat boosts, your rests only take a minor action.

Promotion Reqs:
    1) At least 5 optimal meditation successes in the previous class.
    2) Critical Thinking and Cunning level requirements as follows:
        > Class 2 (+1 VP): Level 2 in both.
        > Class 3 (+2 VP): Level 4 in both.
        > Class 4 (+3 VP): Level 6 in both.
        > Class 5 (+4 VP): Level 8 in both."""
        },
    'scetcher':
        {'hallmark': 'Battle Arena',
         'attribute': 'battle_arena',
         'primary': 'class',
         'secondary': 'tournament_signedup',
         'description':
"""Challenge in tournaments and compete to become the champion.

There are five different tournament classes, victory grants you promotion:
    
    * Class 0 - (non Scetcher-born) - You must defeat Duelist in Training.
        > Scetcher-born can always face duelists in training.
    
    * Class 1 [+0 VP]
        > 64 Combatants (6 rounds).
        > Combat levels vary, but usually max is between 32-36.
        > Entrance Fee: 3 coins.
        > 1st: 30 coins | 2nd: 10 coins | Reach Semi-Final: 3 coins
        
    * Class 2 [+1 VP]
        > 64 Combatants (6 rounds).
        > Combat levels vary, but usually max is between 60-64.
        > Entrance Fee: 5 coins.
        > 1st: 48 coins | 2nd: 16 coins | Reach Semi-Final: 5 coins.
    
    * Class 3 [+2 VP]
        > 32 Combatants (5 rounds).
        > Combat levels vary, but usually max is between 95-100.
        > Entrance Fee: 7 coins.
        > 1st: 66 coins | 2nd: 22 coins | Reach Semi-Final: 7 coins.
    
    * Class 4 [+3 VP]
        > 32 Combatants (5 rounds).
        > Combat levels vary, but usually max is between 116-121.
        > Entrance Fee: 9 coins.
        > 1st: 84 coins | 2nd: 28 coins | Reach Semi-Final: 9 coins.
    
    * Class 5 [+4 VP]
        > 16 Combatants (4 rounds).
        > No Combat Level Limit
        > Entrance Fee: 12 coins.
        > 1st: 111 coins | 2nd: 37 coins | Reach Semi-Final: 12 coins.

If you lost in the first round three times consecutively, you will be demoted."""
        },
    'starfex':
        {'hallmark': 'Ancient Magic Museum',
         'attribute': 'ancient_magic_museum',
         'primary': 'your_donations',
         'secondary': 'total_donations',
         'description':
"""A museum that collects ancient artifacts and offer rewards for magic sword fragments.

Collect 6 magic sword fragments per sword type (will not collect more):
    c = coins, kb = random knowledge book.
    1. Water Fragment - Ponds - 1 VP each, Reward: (1) 2c + 1kb, (2) 2c, (3) 1c, (4) 1c, (5) None, (6) None.
    2. Air Fragment - Plains - 2 VP each, Reward: (1) 3c + 1kb, (2) 3c, (3) 2c, (4) 2c, (5) 1c, (6) 1c.
    3. Earth Fragment - Caves - 3 VP each, Reward: (1) 4c + 1kb, (2) 4c, (3) 3c, (4) 3c, (5) 2c, (6) 2c.
    4. Fire Fragment - Outposts - 4 VP each, Reward: (1) 5c + 1kb, (2) 5c, (3) 4c, (4) 4c, (5) 3c, (6) 3c.
    5. Ice Fragment - Mountains - 5 VP each, Reward: (1) 6c + 1kb, (2) 6c, (3) 5c, (4) 5c, (5) 4c, (6) 4c.
    6. Light Fragment - Ruins - 6 VP each, Reward: (1) 7c + 2kb, (2) 7c + 1kb, (3) 7c, (4) 6c, (5) 6c, (6) 5c.
    7. Blood Fragment - Battle zones - 7 VP each, Reward: (1) 8c + 2kb, (2) 8c + 1kb, (3) 8c, (4) 7c, (5) 7c, (6) 6c.

Additional Notes:
    - You can only get a maximum of 20VP 
    - You can sell fragments to the market but they are donated to the museum and are not given any reward for it.
    - The probability of finding fragments is about 5% on average (cave/mountain tier change probability)
    - For Starfex-born citizens the probability is about 8% on average to discover them.
    
Reputation Stage Unlock Benefits (minimum of 1 remains for prior stage completion):
    - Water Fragments+ : Subtract one Stage 1 completion requirement to unlock Stage 2.
    - Earth Fragments+ : Subtract one Stage 2 completion requirement to unlock Stage 3. (Air+ for Starfex-born citizens)
    - Ice Fragments+ : Subtract one Stage 3 completion requirement to unlock Stage 4. (Fire+ for Starfex-born citizens)
    - Blood Fragment: Subtract one Stage 4 completion requirement to unlock Stage 5. (Ice+ for Starfex-born citizens)
    
Purchasing Fragment:
    - Once 6 fragments have been donated of a single magic sword, the player can purchase them to build it!
        > Water: 16c + 50 Fellowship VPs | Air: 30c + 55 Fellowship VPs | Earth: 44c + 60 Fellowship VPs
        > Fire: 58c + 65 Fellowship VPs | Ice: 72c + 70 Fellowship VPs | Light: 86c + 75 Fellowship VPs
        > Blood: 100c + 80 Fellowship VPs.
    - Then, with Class 5 Smithing Guild at Tamarania, you have a chance to build the Magic Sword!

The Museum may ask you to find rare artifacts for monetary rewards, which vary depending on their location:
    > Ponds [10 Reputation required] - 3c
    > Plains [20 Reputation required] - 4c
    > Caves [25 / 35 / 45 Reputation required] - 5c / 6c / 8c depending on tier.
    > Outposts [30 Reputation required] - 6c
    > Mountains [35 / 45 / 55 Reputation required] - 6c / 8c / 10c depending on tier.
    > Ruins [60 Reputation required] - 12c
    > Battle Zones [75 Reputation required] - 15c
* [Note] four less reputation required for Starfex-born.
* Perhaps by looking for these artifacts you may stumble upon something more powerful..."""
        },
    'tamarania':
        {'hallmark': 'Smithing Guild',
         'attribute': 'smithing_guild',
         'primary': 'class',
         'secondary': 'active_enchant_quantity',
         'description':
"""Smithing here can add temporary enchants to your armor, plus offers a number of other perks.
To advance in class, you must complete these requirements in order: skill, gifting, and quest.

    * Class 1 [+0 VP]
        > Skill Req: 2 Smithing
        > Gifting Req: One rank 1 ore (except Tamarania-born).
        > Quest Req: None.
        > Perk: Second armor slot is unlocked and you can begin smithing here.
        > XP Bonus: +1 Smithing xp when successfully smith here.
        
    * Class 2 [+1 VP]
        > Skill Req: 4 Smithing + 2 Heating
        > Gifting Req: All four distinct rank 1 ores.
        > Quest Req: Travel to 3 different smithers outside Tamarania and convince them to share their resources.
        > Enchant: scales, leather, bark, and ceramic enchants unlocked.
        > Enchant success chance: (Smithing + Heating) / 10 for Class 2 enchants.
        > Enchant duration: 8 rounds
        > Enchant amount: 1
        > XP Bonus: +2 Smithing xp and +1 Heating xp on successful Class 2 enchant. 
    
    * Class 3 [+2 VP]
        > Skill Req: 6 Smithing + 4 Heating
        > Gifting Req: All four distinct rank 2 ores.
        > Quest Req: Find three meteroites in the plains.
        > Enchant: cloth enchants unlocked.
        > Enchant success chance: (Smithing + Heating) / 15 for Class 3 enchants.
        > Enchant amount: 2 (or increase duration)
        > XP Bonus: +3 Smithing xp and +2 Heating xp on successful Class 3 enchant.
    
    * Class 4 [+3 VP]
        > Skill Req: 8 Smithing + 6 Heating
        > Gifting Req: All four distinct rank 3 ores.
        > Quest Req: Find three bedrock in cave III.
        > Enchant: glass, rubber, gems, and old cloth enchants unlocked.
        > Enchant success chance: (Smithing + Heating) / 20 for Class 4 enchants.
        > Enchant duration: 12 rounds.
        > Perk: 25% chance of retaining ore when smithed.
        > XP Bonus: +3 Heating xp on successful Class 4 enchant.
    
    * Class 5 [+4 VP]
        > Skill Req: 10 Smithing + 8 Heating
        > Gifting Req: All four distinct rank 4 ores.
        > Quest Req: Find three living stones in the wilderness.
        > Enchant duration: 15 rounds.
        > Enchant amount: 3 (or increase duration)
        > Perk 1: 20% chance of a student train request with (5-10 coins if Smithing<12, otherwise 15-20 coins)
        > Perk 2: Build Magic Swords | S = Smithing, H = Heating (more information after enchant section):
            > Water [10S, 8H], Air [11S, 8H], Earth [11S, 9H], Fire [11S, 10H], Ice [12S, 10H], Light [12S, 11H], Blood [12S, 12H]""",
        'page 2':
"""Enchants:
    
    * Class 2:
        > scales: +1 coin when persuasion successful.
        > leather: +1 hit points.
        > bark: +1 survival when in caves, mountains, and wilderness.
        > ceramic: +1 minor action.
    
    * Class 3:
        > benfriege cloth: +1 xp when reading books.
        > demetry cloth: +2 xp and +2 coins when working jobs.
        > glaser cloth: safely enter cities skirmishing with yours.
        > kubani cloth: -1 fatigue when survival is successfully activated.
        > pafiz cloth: +1 major action when staying on the same tile (and tier), outside cities, for two rounds.
        > scetcher cloth: +30 combat xp when defeating an opponent stronger than you (with combat-related def stats).
        > starfex cloth: 8% fragment finding chance increase.
        > tamariza cloth: 75% chance for +1 xp when using a skill.
        > tutalu cloth: 25% piercing damage chance against non-human foes.
    
    * Class 4:
        > glass: 75% tile emptiying chance reduction upon successful excavation.
        > rubber: 30% chance of automatically defending an attack after defense-time expires.
        > gems: +30% better selling price on crafted item.
        > old fodker cloth: +2 stability.
        > old enfeir cloth: +2 cunning.
        > old zinzibar cloth: +2 agility.""",
        'page 3': 
"""Building Magic Swords Requires the Following:
    * Class 5 Smithing Guild
    * 6 Fragments
    * 1 of each Lv4 Ore
    * Each Magic Sword Require Additional Material, Minimum Skill Reqs, and Creation Success:
        > Water Sword: 7 Scales, 10 Smithing, 8 Heating, 70 Success Denominator
        > Air Sword: 5 Glass, 11 Smithing, 8 Heating, 80 Success Denominator
        > Earth Sword: 6 Bark, 11 Smithing, 9 Heating, 90 Success Denoinator
        > Fire Sword: 5 Rubber, 11 Smithing 10 Heating, 100 Success Denominator
        > Ice Sword: 6 Benfriege Cloth, 12 Smithing, 10 Heating, 110 Success Denominator
        > Light Sword: 5 Old Fodker Cloth, 12 Smithing, 11 Heating, 120 Success Denominator
        > Blood Sword: 4 Gems, 12 Smithing, 12 Heating, 130 Success Denominator
    * Once all requirements are met, you can attempt to create the Magic Sword with the following chance:
        > Smithing + Heating + Crafting + Stability (with boosts) / Success Denominator"""
        },
    'tamariza':
        {'hallmark': 'Wizard Tower',
         'attribute': 'wizard_tower',
         'primary': 'membership',
         'secondary': 'auto_renewal',
         'description': 
f"""You can subscribe to membership with the Wizard Tower for four mystical benefits.
Membership period lasts 5 rounds and can be auto-renewed.

    - Tamariza-born citizens get 1 coin discount!
    * Basic Membership: 1 coin
    * Gold Membership: 5 coins 
    * Platinum Membership: 10 coins
    
    1) Teleportation (starting at the Wizard Tower; takes minor action):
        * Basic: Teleport up to 3 tiles away | costs 1 fatigue.
        * Gold: Teleport up to 7 tiles away | costs (tile distance)/3 fatigue, rounded up.
        * Platinum: Teleport anywhere | costs (tile distance)/3.5 fatigue, rounded up.

    2) Matter Conversion (only at the Wizard Tower; takes minor action):
        > G1 (4 categories): > Food: [raw meat, raw fish]
                             > Crop: [blazeberry, pluckpetal]
                             > Crafts: [string, beads, hide, sand]
                             > Ores: [lead, tin, copper, iron]

        > G2 (3 categories): > Food: [cooked meat, cooked fish]
                             > Crop: [forgeflower, handiherb, swayleaf, haggleroot]
                             > Crafts: [clay, scales, leather, bark]

        > G3 (4 categories): > Food: [well cooked meat, well cooked fish]
                             > Crop: [cognifruit, cloakmoss, vitalvine, findersfern]
                             > Crafts: [ceramic]
                             > Ores: [tantalum, aluminum, kevlium, nickel]

        > G4 (2 categories): > Crafts: [rubber, glass]
                             > Ores: [tungsten, diamond, titanium, chromium]

        * Basic: Can convert same category material only in G1.
        * Gold: Can convert same category material in all groups.
        * Platinum: Can convert same and cross-category material in all groups.

    3) Tongue Enchantment (used anywhere):
        > Haggling and Persuasion increase their chance of success.
        * Basic: 1/3 chance of using 1 level higher.
        * Gold: 90% chance for 1 level higher.
        * Platinum: Either 1 or 2 levels higher with equal probability.

    4) Alchemy (only at Wizard Tower; takes Major action):
        > Create elixirs with glass, the required material, and crafting level. 
            - Success = Heating/14. If you fail, a random material is destroyed in the process (not glass).
        * Basic: Not allowed to alchemy.
        * Gold: Can only use it once per round (whether you fail or succeed).
        * Platinum: All-access use.

        > Elixirs Available:
            - Elixir of Feasting [Lv {alchemy_properties['elixir of feasting']['crafting']} Crafting]: 
                > {item_descriptions['elixir of feasting']}
                > {stringify_dict(alchemy_properties['elixir of feasting']['ingredients'])}
            - Elixir of Cognition [Lv {alchemy_properties['elixir of cognition']['crafting']} Crafting]:
                > {item_descriptions['elixir of cognition']}
                > {stringify_dict(alchemy_properties['elixir of cognition']['ingredients'])}
            - Elixir of Vigor [Lv {alchemy_properties['elixir of vigor']['crafting']} Crafting]: 
                > {item_descriptions['elixir of vigor']}
                > {stringify_dict(alchemy_properties['elixir of vigor']['ingredients'])}
            - Elixir of Shadow [Lv {alchemy_properties['elixir of shadow']['crafting']} Crafting]:
                > {item_descriptions['elixir of shadow']}
                > {stringify_dict(alchemy_properties['elixir of shadow']['ingredients'])}
            - Elixir of Forging [Lv {alchemy_properties['elixir of forging']['crafting']} Crafting]:
                > {item_descriptions['elixir of forging']}
                > {stringify_dict(alchemy_properties['elixir of forging']['ingredients'])}
            - Elixir of Abundancy [Lv {alchemy_properties['elixir of abundancy']['crafting']} Crafting]: 
                > {item_descriptions['elixir of merchants']}
                > {stringify_dict(alchemy_properties['elixir of merchants']['ingredients'])}
            - Elixir of Retention [Lv {alchemy_properties['elixir of retention']['crafting']} Crafting]:
                > {item_descriptions['elixir of retention']}
                > {stringify_dict(alchemy_properties['elixir of retention']['ingredients'])}
            - Elixir of Certainty [Lv {alchemy_properties['elixir of certainty']['crafting']} Crafting]:
                > {item_descriptions['elixir of certainty']}
                > {stringify_dict(alchemy_properties['elixir of certainty']['ingredients'])}
            - Elixir of Harvest [Lv {alchemy_properties['elixir of harvest']['crafting']} Crafting]:
                > {item_descriptions['elixir of harvest']}
                > {stringify_dict(alchemy_properties['elixir of harvest']['ingredients'])}"""
        },
    'tutalu':
        {'hallmark': "Hunter's Guild",
         'attribute': 'hunters_guild',
         'primary': 'class',
         'secondary': 'hunt_active',
         'description':
"""People come to Hunter's guild requesting to slay monsters that are wreaking havoc.

Class 1:
    - Skill Reqs: 2 Excavating + 2 Attack
    - Join Req: Defeat Sea serpent [Lvl 12] at Pond (waived for Tutalu-born citizen).
    - Loc: Cave depth 1 [Lvl 15-20]
    - Coins rewarded: 4c
    - Prior promotion rewards (3 total): (1-2) +3 Excavating xp, (3) +1 Attack (max 8).

Class 2 (+1 VP):
    - Skill Reqs: 5 Excavting + 5 Attack + 2 Survival
    - Promotion Req: 3 class 1 successes
    - Loc: Cave depth 2 [Lvl 40-50]
    - Coins rewarded: 8c
    - Prior promotion rewards (5 total): (1-2) +1 Attack (max 10), (3-4) +4 Survival xp, (5) +5 Excavating xp.

Class 3 (+2 VP):
    - Skill Reqs: 8 Excavating + 8 Attack + 4 Survival
    - Promotion Req: 5 class 2 successes
    - Loc: Cave depth 3 [Lvl 60-80]
    - Coins rewarded: 14c
    - Prior promotion rewards (4 total): (1) +1 Attack (max 11), (2) +1 Excavating (max 11), (3-4) +5 Survival xp.

Class 4 (+3 VP):
    - Skill Reqs: 10 Excavating + 10 Attack + 6 Survival
    - Promotion Req: 4 class 3 successes
    - Loc: Wilderness [Lvl 90-110]
    - Coins rewarded: 24c
    - Prior promotion rewards (3 total): (1) +1 Attack, (2) +1 Excavating, (3) +6 Survival xp.

Class 5 (+4 VP)
    - Skill Reqs: 12 Excavating + 12 Attack + 8 Survival
    - Promotion Req: 3 class 4 successes
    - Loc: Wilderness [Lvl 125-150]
    - Coins rewarded: 40c"""
        },
    'zinzibar':
        {'hallmark': 'Hidden Ninja Lair',
         'attribute': 'hidden_lair',
         'primary': 'progress',
         'secondary': 'found',
         'description':
"""Here you can study the secret arts of combat, provided you can find the location.
    
There are five secret combat arts: 1) Sharpness, 2) Invincibility, 3) Vanish, 4) Shadow, and 5) Vision
    - Each has three classes and completing the final one gives you +2VP.
  
Learning Combat Requirements:
    - Zinzibar-born citizens subtract one level requirement.
    - [Class 1] - Lvl 2, [Class 2] - Lvl 6, [Class 3] - Lvl 10
    
    * Sharpness: Technique
    * Invincibility: Hit Points
    * Vanish: Agility
    * Shadow: Stability
    * Vision: Cunning

Session Required to Progress (Major Action):
    * Class 1: 2 successful sessions; chance of success is Critical Thinking / 8
    * Class 2: 4 successful sessions; chance of success is Critical Thinking / 12
    * Class 3: 8 successful sessions; chance of success is Critical Thinking / 16
    
Combat Benefits (+2VP at class 3):
    * Sharpness: +1 critical hit upon landing an attack.
    * Invincibility: Recover one HP if HP goes to zero.
    * Vanish: Skip opponent's entire attack round.
    * Shadow: Convert a block to a dodge.
    * Vision: Ignore a fake attack.
    
Benefit Application Chance:
    * Sharpness + Vanish | Class 1: 2% | Class 2: 4% | Class 3: 8%
    * Shadow | Class 1: 3% | Class 2: 6% | Class 3: 12%
    * Vision | Class 1: 4% | Class 2: 8% | Class 3: 16%
    * Invincibility | Class 1: 9% | Class 2: 18% | Class 3: 36%"""
    },
}