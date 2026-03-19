"""Canonical scene graph for The Gambit.

This file keeps story content separate from engine logic so that the game can be
maintained as narrative data rather than tangled control flow.
"""

from __future__ import annotations

from .models import Choice, Scene


def c(
    id: str,
    label: str,
    next_scene: str,
    note: str = "",
    conditions: dict | None = None,
    effects: dict | None = None,
) -> Choice:
    """Convenience creator for a Choice record."""
    return Choice(
        id=id,
        label=label,
        next_scene=next_scene,
        note=note,
        conditions=conditions or {},
        effects=effects or {},
    )


def s(
    id: str,
    title: str,
    chapter: str,
    text: list[str],
    choices: list[Choice] | None = None,
    tags: list[str] | None = None,
    ending: dict | None = None,
    auto_continue_to: str | None = None,
) -> Scene:
    """Convenience creator for a Scene record."""
    return Scene(
        id=id,
        title=title,
        chapter=chapter,
        text=text,
        choices=choices or [],
        tags=tags or [],
        ending=ending,
        auto_continue_to=auto_continue_to,
    )


START_SCENE_ID = "p001_intro"


def build_story() -> dict[str, Scene]:
    """Create and return all playable scenes keyed by scene id."""
    scenes: list[Scene] = [
        s(
            "p001_intro",
            "Late-Night Gambit",
            "Chapter 1: Opening Move",
            [
                "The soft glow of a laptop screen fills Dismas McGowan's study. It is late, the apartment is silent, and a tense online chess endgame is still running.",
                "Tomorrow is his Mechanical Engineering final. His textbook is open to the pages he still does not understand, but his winning streak on Chess.com has become addictive.",
                "He has two doors in front of him: responsibility or momentum.",
            ],
            [
                c(
                    "study_now",
                    "Close the game and study",
                    "p002_study_end",
                    note="The disciplined line.",
                    effects={"set_flags": {"chose_study_first": True}},
                ),
                c(
                    "play_on",
                    "Keep playing the endgame",
                    "p003_endgame_choice",
                    note="The risky line.",
                    effects={"set_flags": {"chose_study_first": False}},
                ),
            ],
            tags=["intro", "chess"],
        ),
        s(
            "p002_study_end",
            "Discipline Rewarded",
            "Ending",
            [
                "Dismas closes the match and commits to his notes. It is rough at first, but the formulas click before sunrise.",
                "He aces the final with a perfect score. Sometimes the smartest move is not made on the board.",
            ],
            ending={
                "id": "ending_responsible",
                "type": "good",
                "title": "Perfect Score",
                "summary": "You chose patience early and secured a calm, successful ending.",
            },
            tags=["ending", "good"],
        ),
        s(
            "p003_endgame_choice",
            "Rook Decision",
            "Chapter 1: Opening Move",
            [
                "Only five pieces remain. Dismas has king and rook. Opponent has king, bishop, and a pawn two squares from promotion.",
                "Two captures glow on-screen. Either move solves one threat and ignores another.",
                "He whispers: 'What's the play?'",
            ],
            [
                c(
                    "capture_pawn",
                    "Capture the pawn",
                    "p004_pawn_loss",
                    effects={"set_flags": {"opening_capture": "pawn"}},
                ),
                c(
                    "capture_bishop",
                    "Capture the bishop",
                    "p005_bishop_loss",
                    effects={"set_flags": {"opening_capture": "bishop"}},
                ),
            ],
            tags=["chess", "critical-choice"],
        ),
        s(
            "p004_pawn_loss",
            "Immediate Punishment",
            "Chapter 1: Opening Move",
            [
                "The pawn disappears. Relief lasts one heartbeat.",
                "Bishop slides across the diagonal. Checkmate.",
            ],
            auto_continue_to="p006_exam_and_call",
            tags=["chess", "loss"],
        ),
        s(
            "p005_bishop_loss",
            "Slow Punishment",
            "Chapter 1: Opening Move",
            [
                "Dismas removes the bishop and feels safe.",
                "The pawn promotes to a queen. The end is quick and brutal. Checkmate.",
            ],
            auto_continue_to="p006_exam_and_call",
            tags=["chess", "loss"],
        ),
        s(
            "p006_exam_and_call",
            "Family Or Opportunity",
            "Chapter 2: Midgame Chaos",
            [
                "He sleeps badly, scores 84% on the exam, and feels the weight of poor choices.",
                "Then his mother calls: his father was hit by a car and is in the hospital.",
                "At the same moment, friends text him to join a high-profit side-hustle event immediately.",
            ],
            [
                c("hospital_first", "Go to the hospital", "p007_hospital_path"),
                c("hustle_first", "Go to the side hustle", "p008_side_hustle_end"),
            ],
            tags=["critical-choice"],
        ),
        s(
            "p008_side_hustle_end",
            "Counterfeit Chaos",
            "Ending",
            [
                "The event is a counterfeit Pokemon-card operation. Angry buyers discover the scam and violence erupts.",
                "Dismas escapes to a subway, only to be randomly stabbed by a stranger. Everything goes dark.",
            ],
            ending={
                "id": "ending_hustle_tragedy",
                "type": "bad",
                "title": "Opportunity Without Principle",
                "summary": "You chose profit over family and were pulled into avoidable chaos.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p007_hospital_path",
            "Card To Germany",
            "Chapter 2: Midgame Chaos",
            [
                "At the hospital, Dismas spends hours with his father. They laugh, remember old trips, and share hard truths.",
                "Before Dismas leaves, his father gives him a card with an address in Germany: 'If you feel lost, go here.'",
                "Later that night, the side-hustle organizer explodes at him for showing up late. The card feels heavier in his pocket.",
            ],
            [
                c("ignore_card", "Keep the card but do nothing", "p009_ignore_germany_end"),
                c("follow_card", "Follow your father's word and go", "p010_flight_choice"),
            ],
            tags=["family", "critical-choice"],
        ),
        s(
            "p009_ignore_germany_end",
            "Too Late",
            "Ending",
            [
                "He delays for nearly a year. By the time he can travel, the call comes: his father has died.",
                "Back home, grief and alcohol consume him. The night ends in silence.",
            ],
            ending={
                "id": "ending_too_late",
                "type": "bad",
                "title": "The Cost Of Delay",
                "summary": "You postponed the journey until the moment passed forever.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p010_flight_choice",
            "Two Tickets",
            "Chapter 3: Germany Gambits",
            [
                "Savings are nearly gone. Two flights remain: an expensive reliable ticket or a suspicious ticket at one-tenth the price.",
                "Cheap is tempting. Safe is costly.",
            ],
            [
                c("buy_sketchy", "Buy the sketchy ticket", "p011_plane_crash_end"),
                c("buy_regular", "Buy the regular ticket", "p012_arrival_germany"),
            ],
            tags=["travel", "critical-choice"],
        ),
        s(
            "p011_plane_crash_end",
            "The Price Of Cheap",
            "Ending",
            [
                "Twenty minutes into the flight, the aircraft fails and crashes into the ocean.",
                "There are no survivors.",
            ],
            ending={
                "id": "ending_sketchy_ticket",
                "type": "bad",
                "title": "False Bargain",
                "summary": "You took the cheapest line and paid the highest cost.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p012_arrival_germany",
            "One Ride Left",
            "Chapter 3: Germany Gambits",
            [
                "Dismas lands safely in Germany, but almost all money is gone.",
                "He can afford only one ride into the city: taxi or subway.",
            ],
            [
                c(
                    "subway_route",
                    "Take the subway",
                    "p013_subway_wallet",
                    effects={"set_flags": {"in_germany": True}},
                ),
                c(
                    "taxi_route",
                    "Take a taxi",
                    "p014_taxi_jake",
                    effects={"set_flags": {"in_germany": True}},
                ),
            ],
            tags=["travel"],
        ),
        s(
            "p013_subway_wallet",
            "Underground Confusion",
            "Chapter 3: Germany Gambits",
            [
                "Crowds, German signs, tunnel announcements. In the confusion, a pickpocket steals his wallet.",
                "He stands frozen by the train window, torn between panic and awareness.",
            ],
            [
                c("panic_and_freeze", "Focus only on panic", "p013b_subway_end"),
                c("look_window", "Look out the window", "p015_window_omen"),
            ],
            tags=["travel", "critical-choice"],
        ),
        s(
            "p013b_subway_end",
            "Lost In Transit",
            "Ending",
            [
                "Without wallet, directions, or help, Dismas drifts station to station until nightfall.",
                "His Germany run ends before it begins.",
            ],
            ending={
                "id": "ending_subway_panic",
                "type": "bad",
                "title": "Panic Spiral",
                "summary": "You froze under pressure and lost the initiative.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p015_window_omen",
            "Bizarre Omen",
            "Chapter 3: Germany Gambits",
            [
                "Outside, he sees a man in a red-and-white jacket spray-painting a tiny plane while a large officer and a small dog chase him.",
                "The absurd scene snaps him out of panic. He asks station staff for help and heads above ground.",
            ],
            [
                c("find_taxi_after_subway", "Find a taxi stand", "p014_taxi_jake"),
            ],
            tags=["dreamlike"],
        ),
        s(
            "p014_taxi_jake",
            "Jake's Five Cities",
            "Chapter 3: Germany Gambits",
            [
                "At the airport curb, Dismas hands his father's address card to a smiling driver.",
                "The driver laughs: 'Dismas? It's Jake. Your dad's old friend.'",
                "Jake explains there are multiple paths to help: Cologne, Frankfurt, and Munich are active leads right now.",
            ],
            [
                c(
                    "enter_city_hub",
                    "Plan the route with Jake",
                    "hub_germany_cities",
                    effects={"set_flags": {"met_jake": True}},
                )
            ],
            tags=["travel", "hub"],
        ),
        s(
            "hub_germany_cities",
            "Germany Route Planner",
            "Chapter 3: Germany Gambits",
            [
                "Jake parks and opens a city map. Your objective is to gather what you need to eventually reach the doctor's cure path.",
                "Inventory and flags now matter. You can revisit this hub after each city event.",
            ],
            [
                c(
                    "go_frankfurt",
                    "Go to Frankfurt (bank + tournament)",
                    "p016_frankfurt",
                    conditions={"not_flags": ["did_frankfurt"]},
                ),
                c(
                    "go_cologne",
                    "Go to Cologne (cathedral + holy water)",
                    "p017_cologne",
                    conditions={"not_flags": ["did_cologne"]},
                ),
                c(
                    "go_munich",
                    "Go to Munich (Oktoberfest + doctor)",
                    "p018_munich",
                    conditions={"not_flags": ["did_munich"]},
                ),
                c(
                    "revisit_frankfurt",
                    "Revisit Frankfurt",
                    "p016_frankfurt",
                    conditions={"flags": {"did_frankfurt": True}},
                ),
                c(
                    "revisit_cologne",
                    "Revisit Cologne",
                    "p017_cologne",
                    conditions={"flags": {"did_cologne": True}},
                ),
                c(
                    "revisit_munich",
                    "Revisit Munich",
                    "p018_munich",
                    conditions={"flags": {"did_munich": True}},
                ),
                c(
                    "attempt_doctor",
                    "Ask Jake to take you to the doctor now",
                    "p030_doctor_requirements",
                    conditions={"flags": {"met_jake": True}},
                ),
                c(
                    "give_up_germany",
                    "Give up and stop searching",
                    "p024_stranded_end",
                    note="A desperate exit.",
                ),
            ],
            tags=["hub", "inventory"],
        ),
        s(
            "p016_frankfurt",
            "Frankfurt Stakes",
            "Chapter 3: Germany Gambits",
            [
                "The bank refuses a $25,000 request for medicine production.",
                "Across the street, a tournament billboard flashes the same amount as first prize.",
            ],
            [
                c(
                    "frankfurt_tourney",
                    "Enter the chess tournament area",
                    "p018_tournament_entry",
                    effects={"set_flags": {"did_frankfurt": True}},
                ),
                c(
                    "back_hub_from_frankfurt",
                    "Return to Jake's map",
                    "hub_germany_cities",
                    effects={"set_flags": {"did_frankfurt": True}},
                ),
            ],
            tags=["chess", "money"],
        ),
        s(
            "p018_tournament_entry",
            "One-Hour Break",
            "Chapter 3: Germany Gambits",
            [
                "Registration is closed. Final rounds are underway and only a few players remain.",
                "A dark thought appears: if one player cannot continue, you could take the seat.",
            ],
            [
                c("do_nothing_tourney", "Do nothing and watch", "p024_stranded_end"),
                c(
                    "impersonate_player",
                    "Take out a participant and steal the seat",
                    "p025_tournament_final",
                    effects={"set_flags": {"tournament_cheated_entry": True}},
                ),
            ],
            tags=["moral-choice", "chess"],
        ),
        s(
            "p024_stranded_end",
            "Stranded",
            "Ending",
            [
                "Without resources or allies, Dismas drifts through Germany exhausted and dehydrated.",
                "The mission collapses before it can become anything more.",
            ],
            ending={
                "id": "ending_stranded",
                "type": "bad",
                "title": "No Line Played",
                "summary": "Inaction and lost momentum ended the run.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p025_tournament_final",
            "Final Board, Final Nerves",
            "Chapter 3: Germany Gambits",
            [
                "Spectators gather as Dismas sits for the final.",
                "His hands shake, then the familiar focus returns. Patterns sharpen.",
                "How do you approach this match?",
            ],
            [
                c(
                    "tourney_patient",
                    "Play patient positional chess",
                    "p035_tournament_win",
                    effects={"set_flags": {"tourney_style": "patient"}},
                ),
                c(
                    "tourney_blitz",
                    "Force aggressive complications",
                    "p025b_tournament_loss_end",
                    effects={"set_flags": {"tourney_style": "aggressive"}},
                ),
            ],
            tags=["chess", "critical-choice"],
        ),
        s(
            "p025b_tournament_loss_end",
            "Nerves Overtake",
            "Ending",
            [
                "The attack burns out. One miscalculation later, Dismas is mated and exposed for not being the registered player.",
                "Security removes him. Jake refuses to keep helping.",
            ],
            ending={
                "id": "ending_tourney_fail",
                "type": "bad",
                "title": "Overpress",
                "summary": "You tried to force brilliance and collapsed under pressure.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p035_tournament_win",
            "$25,000 Prize",
            "Chapter 3: Germany Gambits",
            [
                "After an hour of careful play, Dismas delivers checkmate and wins the full prize.",
                "Jake laughs and asks, 'Where next?'",
            ],
            [
                c(
                    "bank_prize_money",
                    "Pocket the tournament prize",
                    "hub_germany_cities",
                    effects={
                        "set_flags": {"won_tournament": True, "did_frankfurt": True},
                        "inc_items": {"cash": 25000},
                    },
                )
            ],
            tags=["reward", "money"],
        ),
        s(
            "p017_cologne",
            "Cathedral Interview",
            "Chapter 3: Germany Gambits",
            [
                "Inside Cologne's cathedral, Jake introduces a priest guarding holy water.",
                "The priest offers an interview to test character.",
            ],
            [
                c(
                    "lie_to_priest",
                    "Lie to seem worthy",
                    "p021_priest_reject",
                    effects={"set_flags": {"did_cologne": True, "lied_to_priest": True}},
                ),
                c(
                    "tell_truth_priest",
                    "Tell the full truth",
                    "p022_priest_truth",
                    effects={"set_flags": {"did_cologne": True}},
                ),
            ],
            tags=["moral-choice"],
        ),
        s(
            "p021_priest_reject",
            "Seen Through",
            "Chapter 3: Germany Gambits",
            [
                "'Never lie to a priest,' he says calmly. The interview ends immediately.",
                "No holy water is granted.",
            ],
            [
                c("apologize_and_retry", "Apologize and request one final honest attempt", "p022_priest_truth"),
                c("return_hub_cologne_fail", "Return to Jake's map", "hub_germany_cities"),
            ],
            tags=["consequence"],
        ),
        s(
            "p022_priest_truth",
            "Donation Required",
            "Chapter 3: Germany Gambits",
            [
                "After hours of honest conversation, the priest believes Dismas.",
                "But the church requires a $25,000 donation for the sacred reserve.",
            ],
            [
                c(
                    "donate_25k",
                    "Donate $25,000 and receive holy water",
                    "hub_germany_cities",
                    conditions={"items_at_least": {"cash": 25000}},
                    effects={
                        "inc_items": {"cash": -25000, "holy_water": 1},
                        "set_flags": {"holy_water_obtained": True, "did_cologne": True},
                    },
                ),
                c(
                    "cannot_donate",
                    "Admit you cannot afford it yet",
                    "hub_germany_cities",
                    note="Come back after earning money.",
                ),
            ],
            tags=["resource-gate", "inventory"],
        ),
        s(
            "p018_munich",
            "Munich And Wine",
            "Chapter 3: Germany Gambits",
            [
                "Oktoberfest crowds fill Munich. Jake says entry to a key section requires a special wine offering.",
                "Two sources exist: a shady bar or a luxury bar.",
            ],
            [
                c(
                    "shady_bar",
                    "Buy from the shady bar",
                    "p026_shady_bar",
                    effects={"set_flags": {"did_munich": True}},
                ),
                c(
                    "luxury_bar",
                    "Buy from the luxury bar",
                    "p041_luxury_bar",
                    effects={"set_flags": {"did_munich": True}},
                ),
                c("back_hub_munich", "Return to Jake's map", "hub_germany_cities"),
            ],
            tags=["inventory", "city"],
        ),
        s(
            "p041_luxury_bar",
            "Luxury Purchase",
            "Chapter 3: Germany Gambits",
            [
                "The upscale bar is elegant and suspiciously quiet.",
                "A premium bottle costs exactly $25,000.",
            ],
            [
                c(
                    "buy_lux_wine",
                    "Pay $25,000 for luxurious wine",
                    "p040_festival_gate",
                    conditions={"items_at_least": {"cash": 25000}},
                    effects={
                        "inc_items": {"cash": -25000, "wine_lux": 1},
                        "set_flags": {"has_wine": True},
                    },
                ),
                c("cant_afford_lux", "Leave without buying", "p018_munich"),
            ],
            tags=["resource-gate"],
        ),
        s(
            "p026_shady_bar",
            "Shady Deal",
            "Chapter 3: Germany Gambits",
            [
                "The bar looks dangerous, but the crowd is oddly friendly.",
                "They offer a '1000-year-old' bottle for $3 million. Dismas writes a fake check and gets away with it.",
            ],
            [
                c(
                    "take_shady_wine",
                    "Take the shady wine to the festival",
                    "p040_festival_gate",
                    effects={
                        "inc_items": {"wine_shady": 1},
                        "set_flags": {"has_wine": True, "forged_check": True},
                    },
                )
            ],
            tags=["risk", "inventory"],
        ),
        s(
            "p040_festival_gate",
            "Festival Gate",
            "Chapter 3: Germany Gambits",
            [
                "Guards block the inner section. You present a bottle.",
                "Inside waits either opportunity or another trap.",
            ],
            [
                c(
                    "offer_shady",
                    "Offer the shady wine",
                    "p027_inside_festival",
                    conditions={"items_at_least": {"wine_shady": 1}},
                ),
                c(
                    "offer_lux",
                    "Offer the luxurious wine",
                    "p027_inside_festival",
                    conditions={"items_at_least": {"wine_lux": 1}},
                ),
                c("no_wine_leave", "Step away and regroup", "hub_germany_cities"),
            ],
            tags=["gate"],
        ),
        s(
            "p027_inside_festival",
            "Two Drunk Men",
            "Chapter 3: Germany Gambits",
            [
                "Inside, two drunk men watch Dismas. One wears a doctor's coat. The other grins like a con artist.",
            ],
            [
                c("follow_conman", "Follow the normal drunk guy", "p029_conman_end"),
                c("follow_doctor", "Follow the doctor", "p030_doctor_requirements"),
            ],
            tags=["critical-choice"],
        ),
        s(
            "p029_conman_end",
            "Robbed",
            "Ending",
            [
                "The normal drunk man tricks Dismas and disappears with his belongings.",
                "No money, no resources, no path forward.",
            ],
            ending={
                "id": "ending_robbed",
                "type": "bad",
                "title": "Trust Misplaced",
                "summary": "You followed the easy personality read and paid for it.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p030_doctor_requirements",
            "The Doctor's List",
            "Chapter 3: Germany Gambits",
            [
                "The doctor slurs through a formula for medicine. He needs three components:",
                "Holy water. The perfect herb. The tears of the forgotten one.",
                "He also needs two hours to sober up.",
            ],
            [
                c(
                    "collect_herb",
                    "Search a monastery greenhouse for the perfect herb",
                    "p030a_herb_scene",
                    conditions={"not_flags": ["herb_obtained"]},
                ),
                c(
                    "collect_tears",
                    "Visit the memorial of the forgotten and seek tears",
                    "p030b_tears_scene",
                    conditions={"not_flags": ["tears_obtained"]},
                ),
                c(
                    "sleep_couch",
                    "Sleep on the couch and trust the doctor",
                    "p031_dream_reveal",
                    conditions={
                        "flags": {
                            "holy_water_obtained": True,
                            "herb_obtained": True,
                            "tears_obtained": True,
                        }
                    },
                ),
                c("go_alley", "Go to the alley while waiting", "p032_alley_end"),
                c("return_to_hub", "Return to Jake and gather missing items", "hub_germany_cities"),
            ],
            tags=["quest", "inventory"],
        ),
        s(
            "p030a_herb_scene",
            "Perfect Herb",
            "Chapter 3: Germany Gambits",
            [
                "A monk guards rare medicinal plants and asks one question: 'What lasts longer, victory or character?'",
                "Dismas answers, 'Character.' The monk nods and hands over a fragrant herb bundle.",
            ],
            [
                c(
                    "take_herb",
                    "Take the herb and return to the doctor",
                    "p030_doctor_requirements",
                    effects={
                        "inc_items": {"perfect_herb": 1},
                        "set_flags": {"herb_obtained": True},
                    },
                )
            ],
            tags=["quest", "item"],
        ),
        s(
            "p030b_tears_scene",
            "Tears Of The Forgotten",
            "Chapter 3: Germany Gambits",
            [
                "At a war memorial, Dismas reads names of people history almost erased.",
                "He leaves a note for his future self and quietly cries. He collects the tears in a small vial.",
            ],
            [
                c(
                    "take_tears",
                    "Return with the vial",
                    "p030_doctor_requirements",
                    effects={
                        "inc_items": {"forgotten_tears": 1},
                        "set_flags": {"tears_obtained": True},
                    },
                )
            ],
            tags=["quest", "item", "emotional"],
        ),
        s(
            "p032_alley_end",
            "Wrong Alley",
            "Ending",
            [
                "In the dark alley, Dismas witnesses a drug deal and is spotted.",
                "A gun flashes before he can run.",
            ],
            ending={
                "id": "ending_alley",
                "type": "bad",
                "title": "Curiosity In The Wrong Place",
                "summary": "A reckless detour ended the journey.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p031_dream_reveal",
            "Cure Or Dream",
            "Chapter 4: The Twist",
            [
                "Dismas sleeps. When he wakes, the doctor claims the cure is complete.",
                "He rushes home, gives medicine to his father, and reality suddenly dissolves.",
                "He jolts awake on his own couch. Chessboard unfinished. Divorce papers on the counter. A rat at a mousetrap. A ship in a bottle labeled 'The Black Pearl.'",
            ],
            [
                c("accept_dream_end", "Accept this as the end of the adventure", "p031a_dream_end"),
                c(
                    "investigate_bottle",
                    "Investigate the ship in the bottle",
                    "p036_wake_world",
                    effects={"set_flags": {"dream_sequence_seen": True}},
                ),
            ],
            tags=["twist", "dreamlike"],
        ),
        s(
            "p031a_dream_end",
            "Part 2 Coming Soon",
            "Ending",
            [
                "Perhaps Germany was only a warning dream. Perhaps it was a memory in disguise.",
                "Either way, Dismas chooses not to pull the next thread.",
            ],
            ending={
                "id": "ending_open_dream",
                "type": "neutral",
                "title": "Unresolved",
                "summary": "You stopped at the dream reveal and left the mystery unopened.",
            },
            tags=["ending", "neutral"],
        ),
        s(
            "p036_wake_world",
            "Coordinates In Glass",
            "Chapter 5: The Black Pearl",
            [
                "A folded paper inside the bottle reveals coordinates in the Caribbean.",
                "Missed calls from his mother pull him back to reality: he never made it to the hospital yesterday.",
            ],
            [
                c("call_mom_now", "Call your mother immediately", "p038_hospital_return"),
                c("ignore_calls", "Ignore the calls and chase coordinates first", "p037_ignore_calls_end"),
            ],
            tags=["critical-choice", "family"],
        ),
        s(
            "p037_ignore_calls_end",
            "Silence First",
            "Ending",
            [
                "By the time Dismas returns to family matters, trust is damaged and timing is gone.",
                "He still has coordinates, but not the same relationships.",
            ],
            ending={
                "id": "ending_ignore_family",
                "type": "bad",
                "title": "Wrong Priority",
                "summary": "You chased mystery before answering the people who needed you.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p038_hospital_return",
            "Father's Confession",
            "Chapter 5: The Black Pearl",
            [
                "At the hospital, his father is alive and improving.",
                "He admits a pre-family past with treasure hunters and confirms the coordinates likely point to a pirate site.",
                "He warns Dismas: 'The puzzle was designed to stop greedy people.'",
            ],
            [
                c("continue_research", "Research the coordinates deeply", "p041_research_black_pearl"),
            ],
            tags=["family", "lore"],
        ),
        s(
            "p041_research_black_pearl",
            "Rumors Of The Black Pearl",
            "Chapter 5: The Black Pearl",
            [
                "Forums mention vanished ships, hidden caves, and one recurring phrase: The Black Pearl.",
                "An old account, JMcGowan88, mentions that the cave entrance is guarded by a chess position.",
            ],
            [
                c("study_position", "Study the old rook endgame at home", "p044_quiet_rook"),
                c("book_flight_fast", "Book the first possible flight immediately", "p048_airport_departure"),
            ],
            tags=["chess", "prep"],
        ),
        s(
            "p044_quiet_rook",
            "The Quiet Move",
            "Chapter 5: The Black Pearl",
            [
                "Dismas re-creates the original endgame on his home board.",
                "He finds it at last: not capture pawn, not capture bishop, but a quiet defensive rook move that neutralizes both threats.",
            ],
            [
                c(
                    "commit_trip",
                    "Commit to the island expedition",
                    "p048_airport_departure",
                    effects={"set_flags": {"knows_quiet_rook": True}},
                ),
                c("stay_home", "Choose normal life and stay home", "p045_stay_home_end"),
            ],
            tags=["chess", "insight"],
        ),
        s(
            "p045_stay_home_end",
            "Safe But Unanswered",
            "Ending",
            [
                "Dismas shelves the coordinates and returns to routine.",
                "Life stabilizes, but the puzzle remains unsolved.",
            ],
            ending={
                "id": "ending_stay_home",
                "type": "neutral",
                "title": "Quiet Life",
                "summary": "You chose safety over uncertainty.",
            },
            tags=["ending", "neutral"],
        ),
        s(
            "p048_airport_departure",
            "Departure",
            "Chapter 6: Island Run",
            [
                "With barely enough savings, Dismas boards a flight carrying essentials and a wooden rook from his father.",
                "Adventure officially begins.",
            ],
            [
                c("continue_harbor", "Continue to the harbor town", "p049_harbor"),
            ],
            tags=["travel"],
        ),
        s(
            "p049_harbor",
            "Rafael's Boat",
            "Chapter 6: Island Run",
            [
                "Most fishermen refuse to approach the coordinates. One older captain, Rafael, finally agrees.",
                "After hours at sea, the target island rises at the horizon.",
            ],
            [
                c("land_on_island", "Land and enter the jungle", "p052_jungle"),
            ],
            tags=["travel", "island"],
        ),
        s(
            "p052_jungle",
            "Cave Entrance",
            "Chapter 6: Island Run",
            [
                "A narrow trail leads to a vine-covered cave in a cliff wall.",
                "Inside: carved symbols, chess motifs, and a stone board with one bishop and an inscription: 'Finish the game.'",
            ],
            [
                c("place_rook", "Place your wooden rook on the board", "p054_cave_puzzle"),
            ],
            tags=["chess", "puzzle"],
        ),
        s(
            "p054_cave_puzzle",
            "Ancient Endgame",
            "Chapter 6: Island Run",
            [
                "The mechanism activates. Same endgame. Same trap pattern.",
                "This is the critical board from the beginning of everything.",
            ],
            [
                c("cave_capture_pawn", "Capture the pawn", "p054a_cave_fail_end"),
                c("cave_capture_bishop", "Capture the bishop", "p054a_cave_fail_end"),
                c(
                    "cave_quiet_rook",
                    "Play the quiet defensive rook move",
                    "p056_hidden_door",
                    conditions={"flags": {"knows_quiet_rook": True}},
                    note="Requires insight from study.",
                ),
                c(
                    "cave_guess_quiet",
                    "Trust your instincts and play a quiet rook move",
                    "p056_hidden_door",
                    conditions={"not_flags": ["knows_quiet_rook"]},
                    effects={"set_flags": {"knows_quiet_rook": True}},
                    note="Hard read, but still possible.",
                ),
            ],
            tags=["chess", "critical-choice"],
        ),
        s(
            "p054a_cave_fail_end",
            "Stone Trap",
            "Ending",
            [
                "The wrong capture triggers a grinding lock. Dust falls. The board seals.",
                "Dismas escapes alive but the chamber never opens.",
            ],
            ending={
                "id": "ending_cave_fail",
                "type": "bad",
                "title": "Wrong Board Memory",
                "summary": "You repeated the original mistake and lost the island line.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p056_hidden_door",
            "Door Opens",
            "Chapter 6: Island Run",
            [
                "Move by move, the stone puzzle responds. Final checkmate lands.",
                "The board sinks, a hidden door opens, and a chamber reveals treasure and a note from Captain Elias Mercer: take what you need, leave the rest.",
                "Then footsteps approach.",
            ],
            [
                c("meet_victor", "Turn toward the tunnel", "p060_victor_arrives"),
            ],
            tags=["twist", "treasure"],
        ),
        s(
            "p060_victor_arrives",
            "Victor Hale",
            "Chapter 7: Rival Board",
            [
                "A tall stranger emerges with a scarred brow and calm confidence: Victor Hale.",
                "He admits he followed Dismas because only the right chess mind could unlock this chamber.",
                "He proposes another game and reveals an explosive failsafe in the cave.",
            ],
            [
                c("accept_game", "Play Victor's game", "p068_victor_game_opening"),
                c("try_attack_victor", "Refuse and attack him", "p060a_attack_end"),
            ],
            tags=["villain", "chess", "critical-choice"],
        ),
        s(
            "p060a_attack_end",
            "Detonator Panic",
            "Ending",
            [
                "Dismas lunges. Victor triggers the failsafe in panic.",
                "The cave collapses before either man escapes.",
            ],
            ending={
                "id": "ending_attack_victor",
                "type": "bad",
                "title": "No Board, No Patience",
                "summary": "You chose force over calculation and lost everything.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p068_victor_game_opening",
            "Opening Choice",
            "Chapter 7: Rival Board",
            [
                "Victor starts the clock. White to move.",
                "He expects reckless ambition. What do you play?",
            ],
            [
                c("opening_e4", "Play 1. e4, calm and principled", "p070_midgame_turn"),
                c("opening_g4", "Play 1. g4, immediate aggression", "p068a_opening_end"),
            ],
            tags=["chess", "interactive"],
        ),
        s(
            "p068a_opening_end",
            "Overextension",
            "Ending",
            [
                "Victor punishes the reckless opening instantly and wins before the attack starts.",
                "He leaves with the chamber location while Dismas is trapped and empty-handed.",
            ],
            ending={
                "id": "ending_victor_opening",
                "type": "bad",
                "title": "Unsound Gambit",
                "summary": "You attacked too early and never recovered.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p070_midgame_turn",
            "Knight Sacrifice",
            "Chapter 7: Rival Board",
            [
                "Victor sacrifices a knight to rip open your king side.",
                "It looks terrifying, but maybe the sacrifice leaves a hidden weakness.",
            ],
            [
                c("take_material", "Grab material and hope", "p070a_material_end"),
                c(
                    "quiet_rook_again",
                    "Play a quiet rook move and hold structure",
                    "p072_victor_checkmate",
                    effects={"set_flags": {"beat_victor_once": True}},
                ),
            ],
            tags=["chess", "interactive"],
        ),
        s(
            "p070a_material_end",
            "Tactical Blind Spot",
            "Ending",
            [
                "Taking material walks into Victor's prepared mating net.",
                "The board ends before your plan begins.",
            ],
            ending={
                "id": "ending_victor_tactics",
                "type": "bad",
                "title": "Greedy Capture",
                "summary": "You took the bait and missed the deeper line.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p072_victor_checkmate",
            "Checkmate Victor",
            "Chapter 7: Rival Board",
            [
                "Three precise moves later, Victor's king is trapped.",
                "He laughs, impressed, and disarms the explosive device. Before leaving, he says: 'Winning was never the point.'",
            ],
            [
                c("take_all_treasure", "Take all the treasure", "p072a_greed_end"),
                c(
                    "take_only_need",
                    "Take only what you need",
                    "p076_return_home",
                    effects={"inc_items": {"gold_coin": 2}, "set_flags": {"learned_restraint": True}},
                ),
            ],
            tags=["moral-choice", "treasure"],
        ),
        s(
            "p072a_greed_end",
            "Weight Of Gold",
            "Ending",
            [
                "Overloaded with treasure, Dismas cannot move quickly through collapsing tunnels.",
                "He loses the exit and the lesson.",
            ],
            ending={
                "id": "ending_greed",
                "type": "bad",
                "title": "Too Much",
                "summary": "You ignored the pirate's rule and paid for greed.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p076_return_home",
            "Home Board",
            "Chapter 8: Echoes",
            [
                "Weeks later, Dismas is home playing chess with his recovering father.",
                "A single gold coin on the desk proves the island was real.",
            ],
            [
                c("check_for_messages", "Check the treasure forums again", "p080_vh_message"),
                c("end_here_good", "Leave the mystery at one adventure", "p116_good_end"),
            ],
            tags=["epilogue"],
        ),
        s(
            "p080_vh_message",
            "Message From V.H.",
            "Chapter 8: Echoes",
            [
                "Victor messages: 'Few people beat me in chess. Did you see the carving behind the chest?'",
                "He sends a photo: a compass and new coordinates.",
            ],
            [
                c("ignore_round_two", "Ignore the new coordinates", "p116_good_end"),
                c("accept_round_two", "Pursue round two and play first", "p086_round_two_departure"),
            ],
            tags=["hook", "critical-choice"],
        ),
        s(
            "p086_round_two_departure",
            "Round Two",
            "Chapter 9: Two Minds",
            [
                "The new coordinates lead to a chain of storm-cut islands.",
                "Victor confirms the next puzzle requires two players.",
                "Dismas packs rope, flashlight, notebook, and a travel chess set.",
            ],
            [
                c("meet_victor_cliff", "Sail to the central island", "p093_cliff_meet"),
            ],
            tags=["travel", "secret-route"],
        ),
        s(
            "p093_cliff_meet",
            "Two-Player Door",
            "Chapter 9: Two Minds",
            [
                "Victor waits at a cliffside stone structure. A chessboard is carved into the sealed door.",
                "Inscription: 'Two minds must see what one cannot.' Beneath: 'Mate in 3. White to move.'",
                "Two levers control white and black moves. Truth must be played.",
            ],
            [
                c("solve_step1_knight", "White move 1: Knight jump with tempo", "p098_step2"),
                c("solve_step1_rook", "White move 1: Rook swing immediately", "p093a_reset_end"),
            ],
            tags=["chess", "puzzle", "interactive"],
        ),
        s(
            "p093a_reset_end",
            "Puzzle Reset",
            "Ending",
            [
                "The wrong first move triggers a full mechanism reset and seals the door for the season.",
                "Victor leaves, disappointed but amused.",
            ],
            ending={
                "id": "ending_round_two_reset",
                "type": "neutral",
                "title": "Almost",
                "summary": "You reached round two but failed the collaborative puzzle.",
            },
            tags=["ending", "neutral"],
        ),
        s(
            "p098_step2",
            "Truth Move",
            "Chapter 9: Two Minds",
            [
                "Victor studies the board and plays the forced best defensive bishop move.",
                "The mechanism confirms with a heavy click.",
            ],
            [
                c("solve_step2_rook", "White move 2: Rook lift to restrict king", "p100_step3"),
                c("solve_step2_knight", "White move 2: Knight fork attempt", "p093a_reset_end"),
            ],
            tags=["chess", "interactive"],
        ),
        s(
            "p100_step3",
            "Final Lever",
            "Chapter 9: Two Minds",
            [
                "Victor plays the only legal king move. Dust falls. One move remains.",
            ],
            [
                c("solve_mate", "White move 3: Slide rook to checkmate", "p101_door_open"),
                c("miss_mate", "White move 3: Check from the wrong file", "p093a_reset_end"),
            ],
            tags=["chess", "interactive"],
        ),
        s(
            "p101_door_open",
            "Network Chamber",
            "Chapter 10: Final Game",
            [
                "The stone door opens into a tunnel system full of maps, mechanisms, and a giant floor chessboard.",
                "A recorded voice welcomes both players and starts a one-hour final game.",
            ],
            [
                c("play_final_game", "Step onto the white side", "p106_giant_game"),
            ],
            tags=["chess", "finale"],
        ),
        s(
            "p106_giant_game",
            "Giant Board",
            "Chapter 10: Final Game",
            [
                "Victor takes black. Dismas takes white. The opening is smooth; the middlegame becomes violent.",
                "With minutes left, Victor attacks with one final tactical shot.",
                "Choose your deciding plan.",
            ],
            [
                c("final_defense", "Defend, then counter on the weak square", "p110_final_checkmate"),
                c("final_allin", "Launch an all-in king attack", "p106a_final_loss_end"),
            ],
            tags=["chess", "interactive", "critical-choice"],
        ),
        s(
            "p106a_final_loss_end",
            "Final Board Loss",
            "Ending",
            [
                "The all-in attack overextends. Victor consolidates and converts cleanly.",
                "The chamber accepts him as winner and locks out Dismas.",
            ],
            ending={
                "id": "ending_final_loss",
                "type": "bad",
                "title": "One Square Short",
                "summary": "You reached the final game but forced the wrong finish.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p110_final_checkmate",
            "Victory Confirmed",
            "Chapter 10: Final Game",
            [
                "Dismas finds the overlooked square, shifts momentum, and lands checkmate.",
                "The board sinks. A final elegant chest rises with a journal repeating the same lesson: patience over greed.",
            ],
            [
                c("take_need_final", "Take only a handful of coins", "p116_secret_ending"),
                c("take_all_final", "Take every coin and jewel", "p110a_greed_final_end"),
            ],
            tags=["finale", "moral-choice"],
        ),
        s(
            "p110a_greed_final_end",
            "Curse Of Excess",
            "Ending",
            [
                "The chamber's weight-triggered floor gives way as Dismas overloads his pack.",
                "He survives, but loses everything he took.",
            ],
            ending={
                "id": "ending_final_greed",
                "type": "bad",
                "title": "Failed The Lesson",
                "summary": "You solved the puzzle but ignored its purpose.",
            },
            tags=["ending", "bad"],
        ),
        s(
            "p116_good_end",
            "Changed By The Game",
            "Ending",
            [
                "Months pass. Dismas and his father play quiet evening games at home.",
                "The coin on the desk is enough to change his life, not enough to change who he is.",
                "Some gambits are about learning when not to take more.",
            ],
            ending={
                "id": "ending_good_home",
                "type": "good",
                "title": "Enough",
                "summary": "You completed the first island arc and kept the lesson.",
            },
            tags=["ending", "good"],
        ),
        s(
            "p116_secret_ending",
            "Secret Ending: The Player Who Went First",
            "Ending",
            [
                "Dismas beats Victor twice, solves the two-player puzzle network, and wins the final giant-board match.",
                "He still takes only what he needs. Victor leaves with respect. Another puzzle waits somewhere beyond the horizon.",
                "Dismas smiles at the board and says, 'This time, I played first.'",
            ],
            ending={
                "id": "ending_secret_master",
                "type": "secret",
                "title": "Master Gambit",
                "summary": "You completed the full narrative arc and proved patience, restraint, and tactical clarity.",
            },
            tags=["ending", "secret", "good"],
        ),
    ]

    return {scene.id: scene for scene in scenes}
