# Please translate strings under title, story, request, opportunity keys into ---. Please keep all other key-values in the dictionary as english as you perform the translation.
volunteer = [{'title': "Market Day", 'story': "The market is bustling, but the local merchants are overwhelmed. They need help organizing stalls and managing the influx of buyers."},
			 {'title': "Training the Youth", 'story': "You find a group of eager young boys who want to learn the ways of combat. An elder asks you to help with their training."},
			 {'title': "Harvest Afoot", 'story': "The villagers are preparing for the harvest, but they are short-handed. They need help organizing the labor and gathering the crops."},
			 {'title': "Tending to the Sick", 'story': "A mild illness has spread through the town, and the healer is overwhelmed. They ask for help tending to the sick and ensuring the illness does not spread further."},
			 {'title': "Rebuilding Fence", 'story': "A fence was damaged in a recent storm, leaving some residents vulnerable. They need help repairing and strengthening it."},
			 {'title': "Festivities", 'story': "One part of a neighborhood is setting up for a festival, but there is much work to be done. They need help with the preparations to ensure the event is a success."},
			 {'title': "Repairing the Well", 'story': "A well has begun to run dry, and the water is murky. The villagers need help repairing and cleaning it."},
			 {'title': "Blacksmith Trouble", 'story': "The village blacksmith is behind on orders for tools and weapons. He could use an extra pair of hands in the forge."},
			 {'title': "Blown Away Books", 'story': "A book collector came riding in but a giant gust of wind suddenly broke his harness. He could use help collecting all the scattered books and bringing them home."}]

beggar = [{'title': "The Old Soldier", 'story': "An old, battle-worn soldier sits by the roadside, his armor rusted and his eyes hollow. He extends a trembling hand, asking for help to buy a warm meal."},
		  {'title': "The Blind Minstrel", 'story': "A blind minstrel plays a haunting melody on a battered lute. His cup, meant for coins, remains nearly empty as he sings of lost loves and forgotten heroes."},
		  {'title': "The Crippled Blacksmith", 'story': "A man with a crippled leg, once a strong blacksmith, now sits in the village square, his tools rusting beside him. He begs for coins to buy medicine."},
		  {'title': "The Orphaned Child", 'story': "A small, dirt-covered child stands in the shadow of a crumbling building. They clutch a ragged doll and look at you with wide, tear-filled eyes, whispering a plea for help."},
		  {'title': "The Desperate Mother", 'story': "A young mother, holding a sickly child, approaches you with desperation in her eyes. She pleads for coins to buy medicine for her baby."},
		  {'title': "The Shamed Noble", 'story': "A once-proud noble, now reduced to rags, sits slumped against the wall of an alley. His once-fine clothes are torn, and he averts his eyes as he softly asks for aid."},
		  {'title': "The Traveling Merchant", 'story': "A merchant, robbed and left with nothing, sits by the gates with a sign that reads, 'In need of help to return home.' He looks up at you with pleading eyes."},
		  {'title': "The Disgraced Knight", 'story': "A knight, stripped of his title and armor, sits outside the village gates. His once-proud demeanor is gone, replaced by a humble request for aid."},
		  {'title': "The Famine-Stricken Farmer", 'story': "A farmer, gaunt from hunger, leans against a broken cart. The famine has left his family destitute, and he humbly asks for anything you can spare."},
		  {'title': "The Destitute Widow", 'story': "A widow, dressed in mourning clothes, sits at the entrance of a church, her hands outstretched in silent plea. She has no family left to support her."},
		  {'title': "The Mute Beggar", 'story': "A beggar with no voice sits silently by the road, holding a small bowl in his hands. His eyes are filled with gratitude as you approach."},
		  {'title': "The Wandering Artist", 'story': "A frail artist, carrying a bundle of worn-out brushes and tattered canvases, sits by the roadside sketching passersby. His art, though beautiful, goes unnoticed by the busy villagers. He looks up with hope as you approach."},
		  {'title': "The Exiled Scholar", 'story': "A scholar, once respected in the kingdom, now wanders the streets in rags, clutching a few precious scrolls. He humbly asks for a small donation to continue his studies."}]

donation_drive = [{'title': 'Clothing Drive', 'required': "len({'Cloth', 'Old Cloth'}.intersection({var.itemCategories[item] for item in self.player.items}))>=1", 'items': "{'Cloth', 'Old Cloth'}",
				 			"story": "You find a group of villagers collecting clothing to distribute to those in need."},
				  {'title': 'Food Ration Drive', 'required': "len({'Food'}.intersection({var.itemCategories[item] for item in self.player.items}))>=1", 'items': "{'Food'}",
				  			"story": "You find a group of villagers collecting food to distribute to those in need. The recent harvest was poor and the villagers could use anything you may be able to share."},
				  {'title': 'Book Donation Drive', 'required': "len({'Knowledge Books'}.intersection({var.itemCategories[item] for item in self.player.items}))>=1", 'items': "{'Knowledge Books'}",
				  			"story": "Near a school, a group of scholars and teachers are collecting books to donate to children and villagers who cannot afford their own."},
				  {'title': 'Tool Making Drive', 'required': "len({'Smithing'}.intersection({var.itemCategories[item] for item in self.player.items}))>=1", 'items': "{'Smithing'}",
				  			"story": "A group of blacksmith, miners, and forgers are having a tool-making drive. The village's old tools supply have depleted and are in desparate need of ore to make more."},
				  {'title': 'Crafting Drive', 'required': "len({'Crafting'}.intersection({var.itemCategories[item] for item in self.player.items}))>=1", 'items': "{'Crafting'}",
				  			"story": "A group of crafters want to teach kids how to craft. They are holding a crafting drive to seek donations for their initiative."}]

escort = [{'title': "Frightened Merchant", 'story': "A merchant, visibly shaken, sits by the side of the road with his cart of goods. He tells you that highway robbers tried to steal his wares, but he managed to escape. Now, he's too afraid to continue his journey alone."},
		  {'title': "The Noble's Entourage", 'story': "A noblewoman and her small entourage are stranded by the roadside, their carriage wheel broken. They fear the highwaymen lurking nearby, waiting to pounce on easy prey."},
		  {'title': "The Traveling Minstrel", 'story': "A minstrel, carrying a lute and a small bundle of belongings, is hiding behind a tree as you approach. He explains that bandits have been harassing him for coin, and he fears he won’t make it to his destination unscathed."},
		  {'title': "The Wandering Trader", 'story': "A wandering trader, carrying a pack full of rare and valuable goods, nervously paces by the side of the road. He has seen signs of bandits nearby and is too frightened to continue on his own."},
		  {'title': "The Desperate Refugee", 'story': "A refugee, fleeing a skirmishing region, stands trembling at a crossroads. Bandits have been preying on refugees, and this poor soul fears they will be next if they continue alone."},
		  {'title': "The Caravan Leader", 'story': "A caravan leader, responsible for several wagons loaded with goods, is visibly stressed as he explains that bandits have been spotted on the road ahead. The caravan’s guards have fled, and he fears an attack."},
		  {'title': "The Harried Scholar", 'story': "A weary scholar carrying a satchel full of ancient scrolls and manuscripts is huddled under a tree, nervously glancing at the road ahead. He explains that he was chased by robbers and fears for the safety of his precious knowledge."},
		  {'title': "The Stranded Caravan Guard", 'story': "A caravan guard, separated from his group during a skirmish with bandits, sits on a rock by the roadside, nursing a wound. He explains that he told his caravan to finish the journey without him."},
		  {'title': "The Nervous Courier", 'story': "A courier carrying important documents and messages for a local lord is hiding off the road, clutching a sealed package tightly. He confesses that bandits tried to take the package from him, and he fears they might still be close."},
		  {'title': "Fleeing Merchant Family", 'story': "A merchant and his family, traveling with a cart full of their remaining possessions, are hiding in a grove by the road. They were attacked by robbers who stole most of their goods, and now they fear for their lives."},
		  {'title': "The Wounded Knight", 'story': "A knight, bloodied and bruised, leans against a tree by the road, his armor battered from a recent battle. He explains that he was ambushed by bandits and barely escaped with his life, but he is too weak to continue his journey alone."},
		  {'title': 'Escaped Prisoner', 'story': "A man, dirty and wearing tattered clothes, is hiding in the underbrush, panting heavily. He tells you that he recently escaped from a group of bandits who had taken him prisoner. He fears the highway robbers on the road may take him back."},
		  {'title': "The Overburdened Fisherman", 'story': "An older fisherman, with a net full of fish, is struggling to haul his catch back to his city. His face is lined with exhaustion, and he appears to be on the verge of collapse."}]

help_gatherers = [{'title': "The Inexperienced Herbalist", 'story': "A young herbalist, new to the trade, is anxiously scanning the forest floor, unsure of which plants are safe to harvest. She’s carrying an old book filled with notes, but it’s clear she’s struggling to identify the right herbs."},
				  {'title': "The Nervous Trapper", 'story': "A young trapper, clearly nervous and inexperienced, is trying to set up traps. He’s fumbling with the ropes and bait, and you can see that he’s unsure of what he’s doing."},
				  {'title': "The Foraging Family", 'story': "A family of foragers is working together to gather berries and roots, but they seem overwhelmed by the task. The parents are focused on gathering enough food, while the children are too young to be much help."},
				  {'title': "The Injured Hunter", 'required': "self.player.currenttile.tile=='plains'", 'story': "A hunter, limping from a recent injury, is struggling to track and bring down game. His bow is ready, but it’s clear he’s in pain and having difficulty focusing on his task."},
				  {'title': "The Confused Gatherer", 'story': "A gatherer, new to the area, is hopelessly confused. She’s clutching a basket with a few herbs, but it’s clear she doesn’t know the best spots for gathering."},
				  {'title': "The Elderly Forager", 'story': "An elderly forager, moving slowly and carefully through the area, is gathering mushrooms and roots. Her hands tremble slightly as she works, and it’s clear that age has made the task more difficult for her."},
				  {'title': "The Newcomer Hunter", 'required': "self.player.currenttile.tile=='plains'", 'story': "A young hunter, new to the area and still learning the ropes, is trying to track game but seems unsure of where to start. He keeps glancing around nervously, clearly worried about making a mistake"},
				  {'title': "The Tired Fisherman", 'required': "self.player.currenttile.tile=='pond'", 'story': "A fisherman, visibly exhausted from a long day of work, is still trying to catch a few more fish to meet his quota. His arms are heavy, and he’s struggling to pull in the nets alone."},
				  {'title': "The Anxious Apprentice", 'story': "An apprentice gatherer is nervously trying to collect ingredients for his master’s potion, but he’s worried about picking the wrong plants. His hands shake as he examines each leaf, clearly unsure of himself."}]

help_injured = [{'title': "The Trapped Explorer", 'story': "You come across an explorer who has been caught in a makeshift trap, his leg ensnared by a rope that’s pulled tight. He explains that he was looking for a hidden path when he accidentally triggered the trap."},
				{'title': "The Wounded Hunter", 'story': "A hunter lies on the ground, clutching his side where a makeshift bandage is poorly wrapped around a wound. He tells you he was tracking a large animal when it turned on him, wounding him before he managed to escape."},
				{'title': "The Injured Gatherer", 'story': "You find a gatherer sitting against a tree, her ankle twisted painfully beneath her. She explains that she slipped on a wet rock while searching for rare herbs and can’t put weight on her foot."},
				{'title': "The Trapped Miner", 'story': "In a narrow opening you find a miner pinned under a fallen beam. His tools are scattered around him, and he explains that he was digging for precious ore when the cave-in occurred."},
				{'title': "The Poisoned Scout", 'story': "A scout is slumped against a boulder, his face pale and sweating. He weakly explains that he was bitten by a venomous creature while scouting the area for his employer. He has the antidote but can't find his sack."},
				{'title': "The Exhausted Excavator", 'story': "You encounter an explorer who has collapsed from exhaustion. His hands are raw and bleeding, and he’s struggling to breathe after a long ascent."},
				{'title': "Trapped Archeologist", 'story': "You find an archaeologist with her arm trapped under a pile of rocks. She was digging for artifacts when the excavated area partially collapsed."},
				{'title': "The Wounded Ranger", 'story': "You find a ranger with his leg bleeding from a deep gash. He tells you he was attacked by a wild animal while patrolling the area. He needs some help bandaging his wounds."}]

rescue_survivor = [{'title': "The Unconcious Adventurer", 'story': "You stumble upon an adventurer lying unconscious on the ground, his gear scattered around him. His breathing is shallow, and it’s clear that he’s been out cold for some time. He appears to have been injured while exploring the area."},
				   {'title': "Gravely Injured Miner", 'story': "you find a miner gravely injured, with deep cuts and bruises covering his body. He’s barely conscious, mumbling incoherently about a tunnel collapse or an animal attack."},
				   {'title': "The Poisoned Traveler", 'story': "A traveler lies on the ground, convulsing slightly, with signs of poisoning evident on his skin. He weakly mentions eating something that didn’t agree with him or being bitten by a venomous creature."},
				   {'title': "The Fainted Scholar", 'story': "A scholar, wearing tattered robes, is found fainted on the ground, a few ancient scrolls clutched in his hands. He appears to have been researching or searching for something important but pushed himself too far in the harsh environment."},
				   {'title': "Severely Wounded Scout", 'story': "You find a scout severely wounded, with an arrow protruding from his side and blood soaking his clothes. He weakly explains that he was ambushed while scouting the area."},
				   {'title': "The Stranded Noble", 'story': "A nobleman or noblewoman lies unconscious, surrounded by remnants of a camp that was clearly attacked or destroyed. They show signs of serious injury, possibly from an ambush or a fall."},
				   {'title': "Collapsed Ranger", 'story': "You come across a ranger collapsed on the ground, barely conscious and suffering from severe exhaustion and injuries. His gear is worn, and it’s clear he’s been out in the wild for too long."},
				   {'title': "Severely Dehydrated Nomad", 'story': "You find a nomad who has collapsed from severe dehydration. His lips are cracked, and his skin is dry and sunburned. He’s too weak to move or speak, barely holding on to life."},
				   {'title': "The Fainted Prospector", 'story': "You find a prospector who has fainted from exhaustion, possibly after days of searching for valuable minerals. He’s pale and weak, showing signs of overexertion."}]

knowledge_sharing = [{'title': "The Curious Apprentice", 'story': "As you browse through ancient tomes, you notice a young apprentice nervously flipping through pages, his eyes wide with curiosity but also with confusion. He’s clearly overwhelmed by the sheer volume of knowledge and seems uncertain about where to start."},
					 {'title': "The Lost Historian", 'story': "In a quiet corner of the library, you find a historian poring over dusty scrolls, his brow furrowed in frustration. He’s searching for a specific piece of information about a long-forgotten kingdom but is struggling to make sense of the fragmented texts."},
					 {'title': "Enthusiastic Ruin Seeker", 'story': "A scholar with maps and notes spread out in front of him is feverishly scribbling in a notebook, clearly excited but also a bit overwhelmed. He’s trying to pinpoint the location of an ancient ruin mentioned in the texts but is having trouble deciphering the clues."},
					 {'title': "The Diligent Alchemsit", 'story': "In the alchemical section of the library, you encounter an alchemist carefully studying old manuscripts filled with complex formulas and ingredients. She seems to be searching for a specific recipe but is struggling to understand some of the more obscure ingredients."},
					 {'title': "Sleepless Archivist", 'story': "An exhausted archivist, who appears to have spent countless nights in the library, is surrounded by piles of scrolls and books. He’s been cataloging ancient documents but has reached a point where he can no longer make sense of the information."},
					 {'title': "Lost Spells", 'story': "In a dimly lit corner of the library, you find a mystic flipping through old spellbooks, searching for a long-lost summoning spell. She mutters to herself, clearly frustrated by the vague descriptions and missing pages."},
					 {'title': "Diheartened Philosopher", 'story': "In the philosophy section, you find a scholar deeply absorbed in a book, his expression one of deep contemplation mixed with frustration. He’s been grappling with an ancient philosophical concept but seems to be struggling to reconcile it with modern thought."}]

training = {
    "haggling": {
        "adept": {
            "title": "The Struggling Merchant",
            "type": "adept",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "In the bustling marketplace, you notice a young merchant nervously trying to negotiate with a seasoned trader, clearly outmatched and about to lose a good deal. The merchant catches your eye, recognizing that you seem to know your way around a bargain.",
            "request": "I’m struggling to make a fair deal here. Could you give me some pointers on how to haggle more effectively?",
            "opportunity": "Would you like to share your haggling techniques with the young merchant, helping him secure a better deal and boosting his confidence in future negotiations? 1 Major Action."
        },
        "master": {
            "title": "The Revered Haggler",
            "type": "master",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "As you stroll through the market, traders and merchants alike whisper your name, knowing your reputation as a master haggler. A group of aspiring traders approach you with awe, eager to learn the secrets of your unmatched bargaining skills.",
            "request": "We’ve heard stories of your legendary haggling. Please, would you teach us the art of striking the perfect deal?",
            "opportunity": "Would you like to hold a brief lesson on advanced haggling techniques, passing down your wisdom to the next generation of merchants? 1 Major Action."
        }
    },
    "persuasion": {
        "adept": {
            "title": "The Struggling Orator",
            "type": "adept",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "In the town square, you overhear a local leader trying to rally support for a community project, but they’re struggling to persuade the crowd. They glance at you, sensing that you might have the charisma needed to sway the people.",
            "request": "I’m having trouble convincing them. Could you give me some tips on how to persuade a crowd?",
            "opportunity": "Would you like to coach the leader on persuasive speaking, helping them win over the crowd and garner support for the project? 1 Major Action."
        },
        "master": {
            "title": "The Master of Words",
            "type": "master",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "As you pass by a heated debate, both sides fall silent upon noticing you, the master of persuasion whose words have swayed even the most stubborn of minds. A young diplomat eagerly approaches you, hoping to learn the art of persuasion from the best.",
            "request": "I’ve heard tales of your ability to persuade anyone, anywhere. Would you honor me by teaching me how to master this skill?",
            "opportunity": "Would you like to share your advanced persuasion techniques with the young diplomat, imparting the wisdom that has made you a legend in the art of influence? 1 Major Action."
        }
    },
    "critical thinking": {
        "adept": {
            "title": "The Puzzled Scholar",
            "type": "adept",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "In a dimly lit study, a scholar is puzzling over a complex problem, surrounded by stacks of books and scrolls. She seems stuck, unable to see the solution and growing increasingly frustrated. She looks up as you enter, hoping you might offer a fresh perspective.",
            "request": "I’m at a loss with this problem. Could you help me think it through?",
            "opportunity": "Would you like to sit with the scholar and help her approach the problem from different angles, using your critical thinking skills to guide her to a solution? 1 Major Action."
        },
        "master": {
            "title": "The Mastermind",
            "type": "master",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "In the grand hall of a renowned academy, whispers of your unparalleled intellect precede you. Students and professors alike gather around, hoping to witness your mind at work. One brave student steps forward, asking for your guidance in mastering the art of critical thinking.",
            "request": "Your insights have solved problems others couldn’t even comprehend. Please, teach me how to think like you do.",
            "opportunity": "Would you like to conduct a masterclass in critical thinking, sharing the thought processes and techniques that have earned you your reputation? 1 Major Action."
        }
    },
    "survival": {
        "adept": {
            "title": "The Inexperienced Adventurer",
            "type": "adept",
            "required": "self.player.currenttile.tile in {'wilderness', 'cave', 'mountain', 'ruins', 'plains'}",
            "story": "In the area, you come across a young adventurer struggling to start a fire as the cold is setting in. It’s clear he lacks the basic survival skills needed to stay warm and safe.",
            "request": "I’m not sure how to start a fire, and I’m running out of time. Could you teach me how to survive out here?",
            "opportunity": "Would you like to teach the adventurer how to start a fire and share essential survival tips, ensuring he can make it through the night safely? 1 Major Action."
        },
        "master": {
            "title": "The Wilderness Sage",
            "type": "master",
            "required": "self.player.currenttile.tile in {'wilderness', 'cave', 'mountain', 'ruins', 'plains'}",
            "story": "Your reputation as a master of survival precedes you, and even the most seasoned explorers speak of your ability to thrive in the harshest environments. A group of rangers approaches you with admiration, eager to learn the secrets of your survival skills.",
            "request": "We’ve heard stories of your unmatched survival skills. Would you show us how to endure and thrive in any environment?",
            "opportunity": "Would you like to demonstrate your advanced techniques and share the knowledge that has made you a legend in the wilds? 1 Major Action."
        }
    },
    "heating": {
        "adept": {
            "title": "The Aspiring Cook",
            "type": "adept",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "In a small kitchen, you find a novice cook struggling to properly cook a piece of meat. The fire is too low, and the meat is either undercooked or burnt in places. The cook looks up at you, hoping for some guidance.",
            "request": "I can’t seem to get this meat cooked just right. Could you show me how to control the heat to cook it properly?",
            "opportunity": "Would you like to help the aspiring cook adjust the fire and teach them how to control the heat to ensure the meat is cooked evenly and thoroughly? 1 Major Action."
        },
        "master": {
            "title": "The Master of Transformation",
            "type": "master",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "As you enter the workshop, a hush falls over the room. Your mastery in transforming raw materials into valuable items is known far and wide. A group of alchemists and craftsmen gathers around, eager to learn the secrets of your craft.",
            "request": "We’ve heard of your ability to transform ordinary items into something extraordinary. Could you show us how to turn sand into glass or bark into rubber?",
            "opportunity": "Would you like to demonstrate your mastery by transforming raw materials into something valuable, sharing the techniques that make you a master of heat-based transformations? 1 Major Action."
        }
    },
    "smithing": {
        "adept": {
            "title": "The Struggling Blacksmith",
            "type": "adept",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "In a small smithy, you find a young blacksmith struggling to shape a piece of metal. The blade he’s working on is uneven, and his frustration is evident as he tries to hammer it into form.",
            "request": "I can’t seem to get this blade right. Could you give me some tips on smithing?",
            "opportunity": "Would you like to guide the young blacksmith through the process of shaping the blade, offering advice on technique and ensuring the metal is forged correctly? 1 Major Action."
        },
        "master": {
            "title": "The Legendary Smith",
            "type": "master",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "The clanging of hammers ceases as you approach the forge, where blacksmiths of all levels look to you with reverence. Your skill in smithing is unmatched, and they yearn to learn from the master who can create weapons and tools of legendary quality.",
            "request": "Your work is known throughout the land. Please, show us how to craft like you do.",
            "opportunity": "Would you like to share your mastery of smithing, demonstrating techniques that turn raw metal into masterpieces? 1 Major Action."
        }
    },
    "gathering": {
        "adept": {
            "title": "The Novice Gatherer",
            "type": "adept",
            "required": "self.player.currenttile.tile in {'plains', 'pond', 'oldlibrary', 'ruins'}",
            "story": "In the area, you find a novice gatherer nervously picking through plants, unsure of which are safe and which are dangerous. Her basket is nearly empty, and it’s clear she’s struggling to identify the right herbs.",
            "request": "I’m not sure which plants are safe to gather. Could you help me learn what to look for?",
            "opportunity": "Would you like to teach the novice gatherer how to identify and collect the right herbs, ensuring she doesn’t pick anything harmful? 1 Major Action."
        },
        "master": {
            "title": "The Master Gatherer",
            "type": "master",
            "required": "self.player.currenttile.tile in {'plains', 'pond', 'oldlibrary', 'ruins'}",
            "story": "As you walk through the area, the plants and trees seem to whisper in your presence. A group of gatherers who have heard of your unmatched skill in harvesting nature’s bounty approaches, eager to learn from the master.",
            "request": "Your knowledge of the natural world is unparalleled. Could you teach us how to gather with your precision?",
            "opportunity": "Would you like to lead a gathering expedition, sharing advanced techniques and insights that allow you to collect the best of what nature has to offer? 1 Major Action."
        }
    },
    "excavating": {
        "adept": {
            "title": "The Treasure Seeker",
            "type": "adept",
            "required": "self.player.currenttile.tile in {'plains', 'wilderness', 'ruins', 'mountain'}",
            "story": "In a rugged landscape, you come across a fellow explorer anxiously digging through the soil, hoping to find something valuable. His tools are scattered around, and he seems uncertain of where to search next.",
            "request": "I’ve heard there are rare treasures buried around here, but I don’t know where to start. Could you help me find something worthwhile?",
            "opportunity": "Would you like to guide the treasure seeker to potential hotspots, using your excavating skills to identify areas likely to yield valuable finds, and help him unearth something valuable? 1 Major Action."
        },
        "master": {
            "title": "The Legendary Prospector",
            "type": "master",
            "required": "self.player.currenttile.tile in {'plains', 'wilderness', 'ruins', 'mountain'}",
            "story": "As you navigate through the terrain, whispers of your name spread among fellow adventurers. Your ability to find rare and valuable items is renowned. A group of prospectors approaches, eager to learn how to uncover hidden treasures that others would overlook.",
            "request": "We’ve heard that you can find treasure where others see only dirt and stone. Please, show us how to discover those rare items that can change the course of an adventure or bring great wealth.",
            "opportunity": "Would you like to demonstrate your exceptional skill in locating and unearthing hidden treasures, showing the prospectors how to identify subtle clues in the environment and uncover valuable items that could provide a significant advantage? 1 Major Action."
        }
    },
    "crafting": {
        "adept": {
            "title": "The Nervous Crafter",
            "type": "adept",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "In a cozy workshop, you find a crafter struggling with the final touches of a piece of intricate jewelry. The details aren’t coming out as planned, and the crafter is worried about ruining the entire piece.",
            "request": "I’m having trouble with these details. Could you give me some tips on how to finish this piece properly?",
            "opportunity": "Would you like to offer guidance on crafting techniques, helping the crafter refine the details and complete the piece successfully? 1 Major Action."
        },
        "master": {
            "title": "The Master Artisan",
            "type": "master",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "The air in the workshop seems to hum with excitement as you enter, known as a master of crafting whose works are sought after across the land. Aspiring artisans gather around, eager to witness your techniques and learn from the best.",
            "request": "Your craftsmanship is unmatched. Please, teach us how to create with the same skill and artistry.",
            "opportunity": "Would you like to lead a crafting demonstration, sharing the secrets of your artistry with the next generation of crafters? 1 Major Action."
        }
    },
    "stealth": {
        "adept": {
            "title": "The Clumsy Rogue",
            "type": "adept",
            "required": "(self.player.currenttile.tile in var.cities) or (self.player.currenttile.tile in var.village_invest)",
            "story": "In the shadows of a quiet alley, you notice a novice rogue attempting to move silently, but his footsteps are too loud, and he’s easily spotted. He’s frustrated, clearly struggling with the basics of stealth.",
            "request": "I can’t seem to move without being noticed. Could you teach me how to be stealthier?",
            "opportunity": "Would you like to show the novice rogue the fundamentals of stealth, teaching him how to move quietly and avoid detection? 1 Major Action."
        },
        "master": {
            "title": "The Silent Guardian",
            "type": "master",
            "required": "self.player.currenttile.tile in {'wilderness', 'battle1', 'battle2', 'ruins', 'cave', 'road'}",
            "story": "As you move through the area, your presence is nearly undetectable. You allow a group of rangers to see you. They have heard of your legendary ability to navigate unseen and approach you with respect. They are eager to learn how to use stealth to protect others and survive in dangerous environments.",
            "request": "We’ve heard tales of how you can move through even the most perilous terrain without being detected. Could you teach us how to avoid dangerous creatures or gain the upper hand against a formidable foe?",
            "opportunity": "Would you like to demonstrate how to use stealth to avoid detection by dangerous creatures or to position oneself for a decisive strike against a dangerous enemy? 1 Major Action."
        }
    }
}


rescue_prisoner = [
    {
        "title": "The Captured Merchant",
        "story": "As you stealthily approach a bandit camp, you hear the muffled cries of a prisoner. Peering through the underbrush, you see a merchant, bound and gagged, being taunted by a burly bandit. The merchant’s wares are scattered around the camp, and it's clear the bandits plan to keep both the merchant and the goods."
    },
    {
        "title": "The Kidnapped Healer",
        "story": "While scouting a notorious bandit hideout, you notice a makeshift prison cell guarded by a sneering bandit. Inside, a healer is chained to the wall, their robes torn and dirty. The bandit seems to take pleasure in the healer’s suffering, boasting about how valuable their skills will be on the black market."
    },
    {
        "title": "The Abducted Noble",
        "story": "As you infiltrate a bandit camp, you stumble upon a tent where a young noble is being held captive. The noble’s captor, a cunning bandit leader, is pacing nearby, discussing the ransom he’ll demand with his crew. The noble looks up at you with pleading eyes, desperate for rescue."
    },
    {
        "title": "The Captive Scout",
        "story": "While sneaking through a fortified bandit camp, you spot a scout tied to a post, bruised and battered. The scout was likely captured while gathering intelligence on the bandits’ activities. A grizzled bandit stands nearby, sharpening his blade and taunting the scout with threats of torture."
    },
    {
        "title": "The Enslaved Laborer",
        "story": "As you navigate through a large bandit encampment, you come across a group of enslaved laborers, forced to dig trenches and build fortifications. One of the laborers catches your eye; they seem stronger and more capable than the others, and you sense they might have a story to tell. A cruel bandit oversees the work, whipping anyone who dares to slow down."
    },
    {
        "title": "The Trapped Scholar",
        "story": "Deep within the bandit camp, you find a tent filled with stolen artifacts and books. A scholar, who must have been abducted while researching in the wilds, is chained to a post. A bandit is mocking the scholar’s knowledge, tearing pages from an ancient tome. The scholar looks at you with desperation, silently pleading for help."
    },
    {
        "title": "The Captive Blacksmith",
        "story": "As you approach the bandit camp, you hear the sound of metal striking metal. You find a skilled blacksmith forced to work on weapons for the bandits. The blacksmith is chained to the anvil, his face grim with determination to resist, but it’s clear he can’t hold out much longer."
    },
    {
        "title": "The Imprisoned Ranger",
        "story": "Hidden in the shadows, you spot a ranger bound to a tree, his face battered but defiant. The bandits boast about how they caught the ranger while he was scouting their hideout, unaware of the trap they had set. The ranger’s bow and arrows lie just out of reach, a cruel taunt by the bandits."
    },
    {
        "title": "The Bound Herbalist",
        "story": "In a corner of the bandit camp, you see an herbalist tied up, surrounded by crushed herbs and shattered vials. The bandits mockingly toss her supplies into the fire, unaware of the potent concoctions she could have made. The herbalist glances at you, her eyes pleading for help."
    },
    {
        "title": "The Kidnapped Messenger",
        "story": "A messenger is tied to a post in the center of the bandit camp, his satchel still slung over his shoulder. The bandits jeer as they go through the contents, laughing at the royal seal on a letter they’ve taken. The messenger tries to resist, but he’s clearly outnumbered and outmatched."
    },
    {
        "title": "The Trapped Explorer",
        "story": "As you sneak through the bandit camp, you find an explorer locked in a crude cage. He had ventured too close while searching for hidden ruins and was captured. The bandits plan to use him to find treasure, but he’s desperately trying to escape before that happens."
    }
]

protect_ally_battlefield = [
    {
        "title": "The Besieged Samurai",
        "level": 55,
        "character": 'samurai',
        "story": "You see a lone samurai surrounded by a circle of agile ninjas. The samurai, though skilled, is clearly outnumbered, parrying blows from every direction. His armor is dented and bloodied, but his resolve remains unbroken. The ninjas, moving with deadly precision, close in for the kill."
    },
    {
        "title": "The Cornered Monk",
        "level": 40,
        "character": 'monk',
        "story": "You spot a monk fighting off a band of ninjas with nothing but a staff. The monk moves gracefully, deflecting their strikes with swift, precise movements, but the ninjas’ relentless attacks are beginning to overwhelm him."
    },
    {
        "title": "The Trapped Mercenary",
        "level": 45,
        "character": 'mercenary',
        "story": "A mercenary is locked in combat with a group of ninjas. The mercenary fights fiercely, wielding dual blades with deadly accuracy, but the ninjas’ numbers are proving to be too much. They dart in and out of the smoke, attempting to flank him and deliver the final blow."
    },
    {
        "title": "The Defiant Noble",
        "level": 62,
        "character": 'noble warrior',
        "story": "You find a noble warrior fighting off a group of ninjas with only a sword and his wits. The noble, though wounded, stands tall and refuses to give ground. The ninjas, swift and silent, move in with their deadly weapons, aiming to bring down the noble once and for all."
    },
    {
        "title": "The Outnumbered Ranger",
        "level": 46,
        "character": 'ranger',
        "story": "A ranger is surrounded by ninjas who have emerged from the shadows. The ranger, with bow in hand, skillfully shoots arrows at the approaching enemies, but the ninjas are closing in quickly. With nowhere to retreat, the ranger prepares to make a final stand."
    },
    {
        "title": "The Battle-Worn Knight",
        "level": 60,
        "character": 'knight',
        "story": "You see a knight struggling against a group of ninjas. The knight’s armor is battered, and his movements are slower than usual, but his spirit is unyielding. The ninjas, moving with lethal grace, circle the knight, looking for an opening to strike."
    },
    {
        "title": "The Isolated Spy",
        "level": 42,
        "character": 'spy',
        "story": "A spy is engaged in a deadly dance with a group of ninjas. The spy, agile and cunning, uses every trick in the book to evade their strikes and counterattack. But the ninjas are relentless, forcing the spy into a defensive stance."
    },
    {
        "title": "The Brave Defender",
        "level": 58,
        "character": 'defender',
        "story": "You find a warrior fighting off a group of ninjas. The warrior, though heavily outnumbered, is determined to defend the stronghold to the last breath. The ninjas, moving like shadows, press their attack, seeking to bring down the last line of defense."
    }
]

protect_ally_wilderness = [
    {
        "title": "The Besieged Ranger",
        "level": 56,
        "character": 'ranger',
        "story": "You spot a ranger locked in combat with a towering vine monster. The ranger is fighting valiantly with a pair of daggers, slashing at the writhing tendrils that threaten to overwhelm him. The vine monster is relentless, its thorny vines lashing out in an attempt to ensnare him completely."
    },
    {
        "title": "The Cornered Merchant",
        "level": 29,
        "character": 'merchant',
        "story": "You find a merchant who has been cornered by a menacing vine monster. His cart, laden with goods, is being overtaken by the aggressive plant, and the merchant is desperately trying to hack away the encroaching tendrils with a small knife. The vine monster is creeping closer, its vines snaking toward the merchant with alarming speed."
    },
    {
        "title": "The Isolated Scout",
        "level": 49,
        "character": 'scout',
        "story": "You come across a scout battling a formidable vine monster. The scout is using a bow to shoot arrows at the creature, but the vines are closing in fast, and her arrows seem to do little to slow it down. The scout is backed up against a rocky outcrop, with nowhere left to run as the vine monster advances."
    },
    {
        "title": "The Trapped Alchemist",
        "level": 42,
        "character": 'alchemist',
        "story": "You stumble upon an alchemist who is trapped by a giant vine monster. The alchemist is frantically throwing concoctions at the creature, trying to burn or dissolve the vine, but the monster seems immune to his efforts. Its vine has already wrapped around his arms, pulling him closer to its thorny grasp."
    },
    {
        "title": "The Defiant Warrior",
        "level": 68,
        "character": 'warrior',
        "story": "A warrior is engaged in a fierce battle with a powerful vine monster. The warrior’s sword slices through the air, cutting down the vine’s tendrils, but the creature seems to regenerate faster than she can strike. Despite her wounds, the warrior refuses to give up, standing her ground against the relentless monster."
    },
    {
        "title": "The Overwhelmed Scholar",
        "level": 38,
        "character": 'scholar',
        "story": "You find a scholar who has been caught off guard by a massive vine monster. The scholar is using a small blade to try and cut through the vine that is slowly wrapping around his body, but it’s clear that he’s not equipped for combat. His scrolls and books lie scattered around him, already entangled by the creeping tendrils."
    },
    {
        "title": "The Cornered Adventurer",
        "level": 62,
        "character": 'adventurer',
        "story": "You spot an adventurer fighting off a fierce vine monster with a battle axe. The adventurer’s strikes are powerful, but the creature’s tendrils are relentless, threatening to entangle him completely. The vine monster lashes out, trying to drag him into the undergrowth."
    }
]

