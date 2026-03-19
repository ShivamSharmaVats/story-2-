"""ASCII art library for The Gambit.

This module stores scene-friendly text illustrations inspired by classic terminal
adventure aesthetics. Art is intentionally plain ASCII so it renders everywhere.
"""

from __future__ import annotations


def _monster_face() -> str:
    return r"""
              ....;;;;;;;....
           ..',;;;:xxxx;;;;,,'..
         .',:xxxxxxxxxxxxxxxx:;,'.
       ..,:xxxxxxxxxxxxxxxxxxxxx:,..
      ..;xxxxxxxxxxxxxxxxxxxxxxxxx;'.
      .,xxxxxxxxxxxxxxxxxxxxxxxxxxx;..
     .,xxxxxxxxxxxxxxxxxxxxxxxxxxxxx:,.
    .;xx;'.....,:xxxxxxxx;'.....';:;..
    .;x,. .'''. .:xxxxxx,...'''. .;:'.
    .;:,........':xxxxxx,.........,:,.
    .;:;,......';xxxxxxx:,.......';;,.
    .,:::;,,,,;:xxxxxxxxx:;,''',,;:;'.
    .,::::;;;:xxxxxxxxxxxxxx::;::::;'.
    .';:xxxxxxxxxxxxxxxxxxxxxxx::::;..
    .';:xxxxxxxxxxxxxxxxxxxxxxxxx::;'.
    .,;:xxxxxxxx;:.....;xxxxxxxx:;,..
     ..,;xxxxxx:'        :xxxxxx;,'..
      ..'xx::;'           ..,xx;,'..
       ..''...             .....'..
        .',,...            ...''..
         .',;,'...      ,..',,'..
          .';:;:;,'...;;,;;:::..
           .';:xxxxx''xxxxxx:'.
            ,..';xxxxxxxxxx:;..,
           ,...:::;xxxxxx;::;,...,
         .;;''''''''::::'''''''''';.
"""


def _midnight_study() -> str:
    return r"""
        ______________________________________________
       /                                              /|
      /   MECHANICAL ENGINEERING FINAL: 8:00 AM      / |
     /______________________________________________/  |
     |                                              |  |
     |  [ Textbook ]    [ Notes ]    [ Chessboard ] |  |
     |      ____          ____          .-----.     |  |
     |     / __ \        / __ \        |K R  |     |  |
     |    / /_/ /       / /_/ /        |  b p|     |  |
     |   /_____/       /_____/         |  k  |     |  |
     |                                              |  |
     |      coffee: low         focus: unstable     |  |
     |______________________________________________| /
     /______________________________________________|/
"""


def _digital_chessboard() -> str:
    return r"""
         a   b   c   d   e   f   g   h
       +---+---+---+---+---+---+---+---+
    8  | . | . | . | . | . | . | . | . |
       +---+---+---+---+---+---+---+---+
    7  | . | . | . | . | . | . | . | . |
       +---+---+---+---+---+---+---+---+
    6  | . | . | . | . | . | . | . | . |
       +---+---+---+---+---+---+---+---+
    5  | . | . | . | . | p | . | . | . |
       +---+---+---+---+---+---+---+---+
    4  | . | . | . | . | . | b | . | . |
       +---+---+---+---+---+---+---+---+
    3  | . | . | . | . | . | . | . | . |
       +---+---+---+---+---+---+---+---+
    2  | . | . | . | . | . | . | R | . |
       +---+---+---+---+---+---+---+---+
    1  | . | . | . | . | K | . | k | . |
       +---+---+---+---+---+---+---+---+
           timer: 00:44      move: white
"""


def _exam_perfect() -> str:
    return r"""
           _____________________________
          /                             \
         /   FINAL EXAM SCORE REPORT     \
        /_________________________________\
        |                                 |
        |   Name: Dismas McGowan          |
        |   Course: Mechanics IV          |
        |                                 |
        |   Score: 100%                   |
        |   Result: DISTINCTION           |
        |                                 |
        |   "Sometimes patience wins."    |
        |_________________________________|
"""


def _hospital_room() -> str:
    return r"""
       __________________________________________
      |  CITY HOSPITAL - CRITICAL CARE WING     |
      |------------------------------------------|
      |  [monitor]   .----------------------.    |
      |    __        |                      |    |
      |   /__\       |   ___                |    |
      |  |____|      |  /   \               |    |
      |  | || |      | |  _  |   patient    |    |
      |  |_||_|      | | |_| |               |   |
      |   ||         |  \___/                |   |
      |   ||         '----------------------'    |
      |                                          |
      |  beep... beep...                          |
      |__________________________________________|
"""


def _side_hustle_boxes() -> str:
    return r"""
           __________________________________________
          |    POP-UP RETAIL SPACE - SHIPPING ZONE   |
          |------------------------------------------|
          | [###] [###] [###] [###] [###] [###]     |
          | [###] [###] [###] [###] [###] [###]     |
          |------------------------------------------|
          | tape -> ====     labels -> |||||||       |
          | scanner -> [====] laptops -> [::::]      |
          |                                          |
          |   "Hurry, we need every order out!"      |
          |__________________________________________|
"""


def _counterfeit_warning() -> str:
    return r"""
          ____________________________________
         /                                    /|
        /    AUTHENTICITY CHECK FAILED       / |
       /____________________________________/  |
       |                                    |  |
       |   card_texture ..... mismatch      |  |
       |   hologram ........ absent         |  |
       |   color_profile ... invalid        |  |
       |                                    |  |
       |   STATUS: COUNTERFEIT DETECTED     |  |
       |____________________________________| /
       |____________________________________|/
"""


def _germany_ticket() -> str:
    return r"""
      ______________________________________________
     |              FLIGHT OPTIONS                  |
     |----------------------------------------------|
     |  [A] Trusted Airline                         |
     |      price: $$$$$                            |
     |      reliability: high                       |
     |                                              |
     |  [B] MysteryCheapFlights.biz                |
     |      price: $                                |
     |      reliability: ???                        |
     |______________________________________________|
"""


def _plane_regular() -> str:
    return r"""
                     __|__
              --o--o--(_)--o--o--
                \  THE GAMBIT  /
                 \___________ /
                     /   \
                    /_____
               smooth sky, steady engines
"""


def _plane_sketchy() -> str:
    return r"""
                  __|__
           --x--x--(_)--x--x--
             \  ??? AIR ???  /
              \_____________/
                  /  /\
                 /__/  \\
              turbulence! alarms! smoke!
"""


def _subway_station() -> str:
    return r"""
        ___________________________________________
       | U-BAHN STATION                            |
       |-------------------------------------------|
       |  [Gleis 2]  [Ausgang]  [Fahrkarten]       |
       |                                           |
       |   ||||||||||||||||||||||||||||||||||      |
       |  =====================================     |
       |  |  crowded platform, loud announcements| |
       |  =====================================     |
       |___________________________________________|
"""


def _taxi_jake() -> str:
    return r"""
                  _____________
             ____/  TAXI  /____
            /___/_______ /___ /|
           |   _   _   _   _  ||
           |  | | | | | | | | ||
           |__|_|_|_|_|_|_|_|_||
            O               O

        Driver: "Dismas? It's Jake."
"""


def _frankfurt_skyline() -> str:
    return r"""
               ||  ||| ||  ||||
               ||  ||| ||  ||||
         |||   ||  ||| ||  ||||   ||
         |||   ||  ||| ||  ||||   ||
      |||||||  ||||||| |||||||| ||||||
      |||||||  ||||||| |||||||| ||||||
  __________________________________________
 | Frankfurt financial district at dusk      |
 |___________________________________________|
"""


def _chess_tournament_hall() -> str:
    return r"""
      _______________________________________________
     |             GRAND CHESS TOURNAMENT            |
     |-----------------------------------------------|
     |  [] [] [] [] [] [] [] [] [] [] [] []         |
     |  [] [] [] [] [] [] [] [] [] [] [] []         |
     |                                               |
     |  silence. clocks ticking. crowd holding breath|
     |_______________________________________________|
"""


def _cathedral_cologne() -> str:
    return r"""
                      /\
                     /  \
                    /++++\
                   /  ()  \
                  /________\
                  |  ____  |
                  | |    | |
                  | |____| |
                  |  __    |
                  | |  |   |
              ____|_|__|___|____
             /                  \
            /  Cologne Cathedral \
           /______________________\
"""


def _holy_water_vial() -> str:
    return r"""
              ________
             /  ____  \
            /  / __ \  \
           |  | |  | |  |
           |  | |__| |  |
           |  |  __  |  |
           |  | |  | |  |
           |  | |__| |  |
           |  |______|  |
            \          /
             \________/
               HOLY WATER
"""


def _munich_festival() -> str:
    return r"""
      ______________________________________________
     |                OKTOBERFEST                  |
     |---------------------------------------------|
     |   _[]_   _[]_   _[]_   _[]_   _[]_         |
     |  |____| |____| |____| |____| |____|        |
     |   /\      /\     /\      /\     /\         |
     |  /  \    /  \   /  \    /  \   /  \        |
     |_____________________________________________|
"""


def _shady_bar() -> str:
    return r"""
        ______________________________________
       |  SHADY BAR (probably illegal)        |
       |--------------------------------------|
       | graffiti ///// cracks //// neon //// |
       |                                      |
       |  [ bottle ] [ bottle ] [ bottle ]    |
       |  "1000 years old, trust us."         |
       |______________________________________|
"""


def _luxury_bar() -> str:
    return r"""
        ______________________________________
       |  LE GRAND CELLAR                     |
       |--------------------------------------|
       |   ____      ____      ____           |
       |  /____\    /____\    /____\          |
       |  |$$$$|    |$$$$|    |$$$$|          |
       |  polished marble, quiet menace       |
       |______________________________________|
"""


def _doctor_drunk() -> str:
    return r"""
                 .-""-.
                / .--. \
               / /    \ \
               | |    | |
               | |.-""-.|
              ///`.::::.`\
             ||| ::/  \:: ;
             ||; ::\__/:: ;
              \\\ '::::' /
               `=':-..-'`
               [doctor's coat, unsteady]
"""


def _dream_couch() -> str:
    return r"""
          ________________________________
         /                                \
        /   living room at 3:14 AM         \
       /____________________________________\
       |   _________                         |
       |  |  couch  |_____                   |
       |  |_________|_____|                  |
       |       [chessboard half-finished]    |
       |  [divorce papers] [mousetrap + rat] |
       |_____________________________________|
"""


def _ship_black_pearl() -> str:
    return r"""
                 ______________________
                /                      \
               /   glass bottle         \
              |   ____________________   |
              |  /\    /\    /\      |  |
              | /__\__/__\__/__\     |  |
              | \  BLACK PEARL  /    |  |
              |  \______________/     |  |
               \                        /
                \______________________/
"""


def _coordinates_map() -> str:
    return r"""
      _________________________________
     | LAT: 17.xxN                    |
     | LON: 63.xxW                    |
     |--------------------------------|
     |             ~  ~               |
     |         ~          ~           |
     |      ~      X         ~        |
     |         ~          ~           |
     |             ~  ~               |
     |________________________________|
"""


def _harbor_town() -> str:
    return r"""
           ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
         ~      small harbor town      ~
       ~   __      __      __       __  ~
      ~   |__|    |__|    |__|     |__|  ~
      ~    /\      /\      /\       /\   ~
       ~                                   ~
         ~~~  boats rocking in sunset  ~~~
"""


def _rafael_boat() -> str:
    return r"""
                  |\
                  | \        __
                  |  \______/ /____
             ~~~~~|  _      _      \~~~~~
             ~~~~~| |_|____|_|_____/~~~~~
             ~~~~~\________________/~~~~~
                   Captain Rafael
"""


def _island_shore() -> str:
    return r"""
             ~~~~~~~~~~~~~~~
         ~~~~      __      ~~~~
      ~~~~       _/  \_      ~~~~
     ~~~       _/  ||  \_      ~~~
     ~~~      /   palm   \      ~~~
      ~~~~   /____________\    ~~~~
         ~~~~     sand      ~~~~
             ~~~~~~~~~~~~~~~
"""


def _cave_entrance() -> str:
    return r"""
               _________
            __/         \__
          _/   vines      \_
         /   ///    ///     \
        /   ///  __  ///     \
       |       _/  \_         |
       |      /      \        |
       |      \______/        |
        \                    /
         \__________________/
"""


def _stone_chess_table() -> str:
    return r"""
         ________________________________
        /                                \
       /   stone table: FINISH THE GAME   \
      /____________________________________\
      |  +---+---+---+---+---+---+---+---+ |
      |  |   |   |   |   | b |   |   |   | |
      |  +---+---+---+---+---+---+---+---+ |
      |  | K |   |   |   | p |   | R | k | |
      |  +---+---+---+---+---+---+---+---+ |
      |____________________________________|
"""


def _treasure_chest() -> str:
    return r"""
                ______________________
               /\                     \
              /  \_____________________\
             /   /|                    /|
            /___/ |___________________/ |
            |   | |  GOLD  JEWELS    |  |
            |   | |  MAPS  ARTIFACTS |  |
            |   | |___________________|  |
            |   |/____________________| /
            |___/______________________|/
"""


def _victor_hale() -> str:
    return r"""
               _____________
              /  /=====\\  \
             /  /  _ _  \  \
            |  |  (o o)  |  |
            |  |    ^    |  |
            |  |  \___/  |  |
            |  |  /___\  |  |
            |  |  scar-> |  |
            |  |_________|  |
             \     ||      /
              \____||_____/
                Victor Hale
"""


def _explosive_device() -> str:
    return r"""
             _____________________
            |  COLLAPSE FAILSAFE  |
            |---------------------|
            |  [ ] ARM            |
            |  [x] ACTIVE         |
            |  [ ] DISARM         |
            |---------------------|
            |     00:59:59        |
            |_____________________|
"""


def _victor_board() -> str:
    return r"""
         +---+---+---+---+---+---+---+---+
      8  | r | n | b | q | k | b | n | r |
         +---+---+---+---+---+---+---+---+
      7  | p | p | p | p | p | p | p | p |
         +---+---+---+---+---+---+---+---+
      6  | . | . | . | . | . | . | . | . |
         +---+---+---+---+---+---+---+---+
      5  | . | . | . | . | . | . | . | . |
         +---+---+---+---+---+---+---+---+
      4  | . | . | . | . | P | . | . | . |
         +---+---+---+---+---+---+---+---+
      3  | . | . | . | . | . | . | . | . |
         +---+---+---+---+---+---+---+---+
      2  | P | P | P | P | . | P | P | P |
         +---+---+---+---+---+---+---+---+
      1  | R | N | B | Q | K | B | N | R |
         +---+---+---+---+---+---+---+---+
"""


def _forum_message() -> str:
    return r"""
      ___________________________________________
     | inbox: new private message                |
     |-------------------------------------------|
     | from: V.H.                                |
     | "Congratulations again on the game."      |
     | "Did you see the carving behind chest?"  |
     | [attachment: compass_coordinates.jpg]     |
     |___________________________________________|
"""


def _compass_carving() -> str:
    return r"""
                 N
                 ^
             W <-+-> E
                 v
                 S
             .-----------.
            /  engraved   \
           /   compass     \
           \  + coords     /
            '-----------'
"""


def _two_player_door() -> str:
    return r"""
       _____________________________________________
      |                                             |
      |     TWO MINDS MUST SEE WHAT ONE CANNOT      |
      |---------------------------------------------|
      |        +---+---+---+---+---+---+---+---+   |
      |        | K | . | . | . | . | . | . | . |   |
      |        +---+---+---+---+---+---+---+---+   |
      |        | . | . | . | R | . | . | . | . |   |
      |        +---+---+---+---+---+---+---+---+   |
      |        | . | . | N | . | . | b | . | k |   |
      |        +---+---+---+---+---+---+---+---+   |
      |                                             |
      |        [white lever]    [black lever]      |
      |_____________________________________________|
"""


def _giant_chessboard() -> str:
    return r"""
          ______________________________________________
         /                                              \
        /    GIANT STONE BOARD - FINAL GAME CHAMBER     \
       /__________________________________________________\
       | [] [] [] [] [] [] [] [] [] [] [] [] [] [] []   |
       | [] [] [] [] [] [] [] [] [] [] [] [] [] [] []   |
       | [] [] [] [] [] [] [] [] [] [] [] [] [] [] []   |
       | [] [] [] [] [] [] [] [] [] [] [] [] [] [] []   |
       | [] [] [] [] [] [] [] [] [] [] [] [] [] [] []   |
       |                                                  |
       |      statues move with stone gears and thunder   |
       |__________________________________________________|
"""


def _final_chest() -> str:
    return r"""
            ______________________________
           /\                             \
          /  \   FINAL PRIZE CHEST         \
         /____\_____________________________\
         |    |  journal + coins + gems    |
         |    |  "Take what you need."     |
         |    |_____________________________|
         |___/______________________________|
"""


def _home_chess_coin() -> str:
    return r"""
         ________________________________________
        | evening at home                         |
        |-----------------------------------------|
        |  chessboard: father vs son              |
        |       +---+---+---+---+                 |
        |       | K | . | . | . |                 |
        |       +---+---+---+---+                 |
        |       | . | N | . | . |    (coin) *     |
        |       +---+---+---+---+                 |
        |_________________________________________|
"""


def _bad_ending_shatter() -> str:
    return r"""
          x x x x x x x x x x x x x x x x
          x          BAD ENDING          x
          x x x x x x x x x x x x x x x x
                  \\   //
                   \\ //
                    \V/
                    /|\
                   / | \
                  shattered line
"""


def _good_ending_glow() -> str:
    return r"""
          ********************************
          *          GOOD ENDING         *
          ********************************
                 .-.-.-.-.-.-.
               .'-.-.-.-.-.-.-'.
              / / / / / / / / / /
             / / / / / / / / / /
              '-.-.-.-.-.-.-.-'
                 soft golden glow
"""


def _secret_ending_sigil() -> str:
    return r"""
             .-------------------------.
            /   SECRET ENDING UNLOCK   \
           /-----------------------------\
           |        /\      /\          |
           |       /  \____/  \         |
           |      /            \        |
           |      \   MASTER   /        |
           |       \  GAMBIT  /         |
           |        \________/          |
           \____________________________/
"""


# Long-form gallery pieces (line-heavy by design) to provide varied scene art.
# These keep the game code rich in terminal-style visual storytelling.


def _gallery_one() -> str:
    return r"""
   _________________________________
  /                                 \
 |  CITY NIGHTS, OPENING TENSION     |
 |-----------------------------------|
 |  streetlight....window....screen  |
 |      .        .         .         |
 |   .     .  .     .  .      .      |
 |   | |   |  | |   |  | |    | |    |
 |   | |   |  | |   |  | |    | |    |
 |   | |___|  | |___|  | |____| |    |
 |   |_____|  |_____|  |________|    |
 |                                   |
 |   in one room: a board, a choice  |
  \_________________________________/
"""


def _gallery_two() -> str:
    return r"""
     __________________________________________
    /                                          \
   /   CLOCK PRESSURE                           \
  /______________________________________________\
  | 00:59 | 00:42 | 00:17 | 00:05 | 00:01       |
  |----------------------------------------------|
  | each second narrows possibility              |
  | each move defines the next map of danger     |
  |----------------------------------------------|
  | breathe -> evaluate -> commit                |
  |______________________________________________|
"""


def _gallery_three() -> str:
    return r"""
      ______________________________________
     | CHESS PRINCIPLES                     |
     |--------------------------------------|
     | 1. Do not panic                      |
     | 2. Do not get greedy                 |
     | 3. Improve worst piece               |
     | 4. Count forcing lines               |
     | 5. Patience outlasts pressure        |
     |______________________________________|
"""


def _gallery_four() -> str:
    return r"""
            ________________
           /  MAP OF CHOICES\
          /__________________\
          |  study ----> peace|
          |  game  ----> risk |
          |  family --> truth |
          |  greed  --> fall  |
          |  patience-> key   |
          |___________________|
"""


def _gallery_five() -> str:
    return r"""
        ____________________________________________
       | AIRPORT TERMINAL                           |
       |--------------------------------------------|
       | gate A12      gate B04      gate C19       |
       |  [====]        [====]        [====]        |
       |                                            |
       | overhead voice: "Final call for boarding" |
       |____________________________________________|
"""


def _gallery_six() -> str:
    return r"""
            ______________________________
           / ISLAND WEATHER REPORT        \
          /________________________________\
          | wind: strong                   |
          | tide: rising                   |
          | visibility: unstable           |
          | omen: unknown                  |
          |________________________________|
"""


def _gallery_seven() -> str:
    return r"""
        _________________________________________
       | CAVE WALL CARVINGS                      |
       |-----------------------------------------|
       |  <> <>  (knight)  //\  [rook]  (king)  |
       |  [] []  (bishop)  \\/  [pawn]  (queen) |
       |-----------------------------------------|
       | "truth must be played"                 |
       |_________________________________________|
"""


def _gallery_eight() -> str:
    return r"""
           _______________________________
          / TREASURE ETHIC                \
         /_________________________________\
         | take what you need             |
         | leave enough for the next mind |
         | greed is a trap disguised as   |
         | victory                         |
         |_________________________________|
"""


def _gallery_nine() -> str:
    return r"""
          ________________________________________
         | VICTOR HALE DOSSIER                    |
         |----------------------------------------|
         | role: puzzle hunter                    |
         | trait: brilliant, dangerous            |
         | weakness: overconfidence in pressure   |
         | note: respects real opponents          |
         |________________________________________|
"""


def _gallery_ten() -> str:
    return r"""
         ______________________________________
        | PATH SUMMARY                          |
        |---------------------------------------|
        | opening: risky                        |
        | germany: entered                      |
        | city routes: completed                |
        | island puzzle: solved                 |
        | victor game: won                      |
        | final lesson: restraint               |
        |_______________________________________|
"""


# Additional galleries to increase visual variety across long story arcs.
# They intentionally reuse thematic motifs (board, maps, doors, sea, clocks).


def _gallery_11() -> str:
    return r"""
      ____________________________________________
     | INTERIOR: STUDY LAMP                        |
     |---------------------------------------------|
     |            .-===-.                           |
     |           / .===. \                          |
     |           \/ 6 6 \/                          |
     |           ( \___/ )                          |
     |___ooo_____/`-----'\____ooo__________________|
"""


def _gallery_12() -> str:
    return r"""
     _____________________________________________
    | ENGINEERING NOTES                            |
    |----------------------------------------------|
    | sigma F = 0                                  |
    | M = I * alpha                                |
    | stress, strain, torque, fatigue              |
    | margin note: "check line before move"        |
    |______________________________________________|
"""


def _gallery_13() -> str:
    return r"""
     ______________________________________________
    | HOSPITAL CORRIDOR                             |
    |-----------------------------------------------|
    | || || || || || || || || || || || || || ||    |
    | doors ... doors ... doors ... fluorescent hum |
    |-----------------------------------------------|
    | footsteps feel heavier with each meter        |
    |_______________________________________________|
"""


def _gallery_14() -> str:
    return r"""
     _____________________________________________
    | SUBWAY WINDOW SCENE                          |
    |----------------------------------------------|
    |   man in red-white jacket                    |
    |   spray paint on tiny aircraft               |
    |   large officer + tiny dog in pursuit        |
    |----------------------------------------------|
    | absurdity interrupts panic                   |
    |______________________________________________|
"""


def _gallery_15() -> str:
    return r"""
     _____________________________________________
    | JAKE'S ROAD MAP                               |
    |-----------------------------------------------|
    | Cologne ----- Frankfurt ----- Munich          |
    |    |             |              |             |
    | interview     tournament      doctor          |
    |_______________________________________________|
"""


def _gallery_16() -> str:
    return r"""
      ___________________________________________
     | BANK OFFICE                               |
     |-------------------------------------------|
     | collateral: none                          |
     | credit history: thin                      |
     | decision: DECLINED                        |
     |-------------------------------------------|
     | billboard outside: CHESS PRIZE $25,000    |
     |___________________________________________|
"""


def _gallery_17() -> str:
    return r"""
      ___________________________________________
     | TOURNAMENT CLOCK                           |
     |-------------------------------------------|
     | left side: 12:31                           |
     | right side: 10:42                          |
     | crowd noise: muted heartbeat               |
     |___________________________________________|
"""


def _gallery_18() -> str:
    return r"""
      ___________________________________________
     | PRIEST'S INTERVIEW                          |
     |---------------------------------------------|
     | Q: Why now?                                  |
     | Q: For whom?                                 |
     | Q: What are you willing to lose?             |
     |---------------------------------------------|
     | lies fail. honesty costs.                    |
     |_____________________________________________|
"""


def _gallery_19() -> str:
    return r"""
      ___________________________________________
     | FESTIVAL GATE                               |
     |---------------------------------------------|
     | guard: "the bottle?"                         |
     | crowd: loud                                  |
     | choices: shady / luxury                      |
     |_____________________________________________|
"""


def _gallery_20() -> str:
    return r"""
      ____________________________________________
     | DOCTOR'S RECIPE                              |
     |----------------------------------------------|
     | 1) holy water                                |
     | 2) perfect herb                              |
     | 3) tears of the forgotten                    |
     |----------------------------------------------|
     | synthesis window: after sobriety             |
     |______________________________________________|
"""


def _gallery_21() -> str:
    return r"""
      _____________________________________________
     | MEMORIAL OF THE FORGOTTEN                    |
     |----------------------------------------------|
     | names weathered by rain and years            |
     | silence heavier than stone                   |
     |----------------------------------------------|
     | grief becomes ingredient                     |
     |______________________________________________|
"""


def _gallery_22() -> str:
    return r"""
      _____________________________________________
     | MONASTERY GREENHOUSE                          |
     |-----------------------------------------------|
     | rows of rare medicinal plants                 |
     | incense, dew, and morning light              |
     |-----------------------------------------------|
     | answer wisely; receive the herb              |
     |_______________________________________________|
"""


def _gallery_23() -> str:
    return r"""
      _____________________________________________
     | DREAM FRACTURE                                |
     |-----------------------------------------------|
     | Germany dissolves into living room            |
     | papers on counter, rat by trap                |
     | ship in bottle waiting                         |
     |_______________________________________________|
"""


def _gallery_24() -> str:
    return r"""
      _____________________________________________
     | CALL LOG                                      |
     |-----------------------------------------------|
     | missed: mom x4                                |
     | missed: unknown x2                            |
     | urgency: high                                 |
     |_______________________________________________|
"""


def _gallery_25() -> str:
    return r"""
      _____________________________________________
     | FATHER'S OLD USERNAME                          |
     |-----------------------------------------------|
     | JMcGowan88 posted years ago                   |
     | "not a lock. a chess position."              |
     |_______________________________________________|
"""


def _gallery_26() -> str:
    return r"""
      _____________________________________________
     | AIRPORT DEPARTURE (CARIBBEAN)                 |
     |-----------------------------------------------|
     | bag packed: rope, flashlight, notebook, rook  |
     | fear remembered: sketchy-flight nightmare     |
     |_______________________________________________|
"""


def _gallery_27() -> str:
    return r"""
      _____________________________________________
     | OPEN OCEAN                                     |
     |-----------------------------------------------|
     | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |
     | horizon stretched thin and silver             |
     | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |
     |_______________________________________________|
"""


def _gallery_28() -> str:
    return r"""
      _____________________________________________
     | JUNGLE TRAIL                                   |
     |-----------------------------------------------|
     | vines, insects, humidity                       |
     | path almost too convenient                     |
     |_______________________________________________|
"""


def _gallery_29() -> str:
    return r"""
      _____________________________________________
     | STONE GEARS ACTIVATING                         |
     |-----------------------------------------------|
     | clunk... clunk... rumble...                    |
     | puzzle accepts valid line                      |
     |_______________________________________________|
"""


def _gallery_30() -> str:
    return r"""
      _____________________________________________
     | NOTE OF CAPTAIN ELIAS MERCER                   |
     |-----------------------------------------------|
     | "clever, not greedy."                          |
     | "take what you need."                          |
     | "leave the rest."                              |
     |_______________________________________________|
"""


def _gallery_31() -> str:
    return r"""
      _____________________________________________
     | ROUND TWO MARKING                               |
     |-----------------------------------------------|
     | carved text: "round two begins soon"          |
     | edges look newer than pirate stone             |
     |_______________________________________________|
"""


def _gallery_32() -> str:
    return r"""
      _____________________________________________
     | STANDOFF                                       |
     |-----------------------------------------------|
     | Dismas between Victor and chest               |
     | flashlight grip tight                         |
     | board waits for another game                  |
     |_______________________________________________|
"""


def _gallery_33() -> str:
    return r"""
      _____________________________________________
     | OPENING REPERTOIRE                             |
     |-----------------------------------------------|
     | safe: e4, d4                                   |
     | reckless: g4, b4                               |
     |-----------------------------------------------|
     | temperament decides line                        |
     |_______________________________________________|
"""


def _gallery_34() -> str:
    return r"""
      _____________________________________________
     | QUIET ROOK MOTIF                                |
     |-----------------------------------------------|
     | not capture                                    |
     | not panic                                      |
     | improve coordination                            |
     |_______________________________________________|
"""


def _gallery_35() -> str:
    return r"""
      _____________________________________________
     | CAVE EXIT SUNSET                                |
     |-----------------------------------------------|
     | orange sky over retreating island              |
     | Rafael waiting, relieved                        |
     |_______________________________________________|
"""


def _gallery_36() -> str:
    return r"""
      _____________________________________________
     | FORUM DM THREAD                                 |
     |-----------------------------------------------|
     | V.H.: "Did you miss the carving?"             |
     | Dismas: "What carving?"                        |
     | image attached: compass + new coordinates       |
     |_______________________________________________|
"""


def _gallery_37() -> str:
    return r"""
      _____________________________________________
     | ISLAND CHAIN                                    |
     |-----------------------------------------------|
     |   o   o   O   o   o                            |
     | storms, wrecks, missing cargo logs             |
     |_______________________________________________|
"""


def _gallery_38() -> str:
    return r"""
      _____________________________________________
     | CLIFFSIDE MEETING                               |
     |-----------------------------------------------|
     | Victor already present                           |
     | stone door half-buried in rock                  |
     | center engraving: chessboard                    |
     |_______________________________________________|
"""


def _gallery_39() -> str:
    return r"""
      _____________________________________________
     | MATE IN THREE                                   |
     |-----------------------------------------------|
     | white: king rook knight                         |
     | black: king bishop                              |
     | lever puzzle enforces best play                 |
     |_______________________________________________|
"""


def _gallery_40() -> str:
    return r"""
      _____________________________________________
     | TUNNEL NETWORK                                   |
     |-----------------------------------------------|
     | maps, locks, mechanisms, coded stones           |
     | one puzzle leads to another                     |
     |_______________________________________________|
"""


def _gallery_41() -> str:
    return r"""
      _____________________________________________
     | RECORDED VOICE                                  |
     |-----------------------------------------------|
     | "welcome, players"                              |
     | "final game begins"                             |
     | gears wake beneath the floor                    |
     |_______________________________________________|
"""


def _gallery_42() -> str:
    return r"""
      _____________________________________________
     | STONE CLOCK                                     |
     |-----------------------------------------------|
     | [ 01:00:00 ]                                    |
     | [ 00:10:00 ]                                    |
     | [ 00:05:00 ]                                    |
     |_______________________________________________|
"""


def _gallery_43() -> str:
    return r"""
      _____________________________________________
     | FINAL TACTICAL MOMENT                            |
     |-----------------------------------------------|
     | one square overlooked                            |
     | one queen move changes everything                |
     |_______________________________________________|
"""


def _gallery_44() -> str:
    return r"""
      _____________________________________________
     | JOURNAL MESSAGE                                  |
     |-----------------------------------------------|
     | treasure is easy                                 |
     | wisdom is harder                                 |
     | restraint proves worth                           |
     |_______________________________________________|
"""


def _gallery_45() -> str:
    return r"""
      _____________________________________________
     | DOUBLE VICTORY                                   |
     |-----------------------------------------------|
     | first win: cave                                 |
     | second win: giant board                         |
     | third win: against greed                        |
     |_______________________________________________|
"""


def _gallery_46() -> str:
    return r"""
      _____________________________________________
     | LATE-NIGHT REMATCH                               |
     |-----------------------------------------------|
     | father: "your move"                             |
     | dismas: "check"                                 |
     | both smiling                                     |
     |_______________________________________________|
"""


def _gallery_47() -> str:
    return r"""
      _____________________________________________
     | COIN ON DESK                                     |
     |-----------------------------------------------|
     | small enough to fit in palm                      |
     | heavy enough to change a future                  |
     |_______________________________________________|
"""


def _gallery_48() -> str:
    return r"""
      _____________________________________________
     | NEXT PUZZLE HORIZON                              |
     |-----------------------------------------------|
     | somewhere beyond map edges                       |
     | Victor searching, Dismas preparing               |
     |_______________________________________________|
"""


def _gallery_49() -> str:
    return r"""
      _____________________________________________
     | REPLAY INVITATION                                |
     |-----------------------------------------------|
     | try alternate lines                              |
     | unlock endings                                   |
     | learn different costs                            |
     |_______________________________________________|
"""


def _gallery_50() -> str:
    return r"""
      _____________________________________________
     | MORAL CHECKMATE                                  |
     |-----------------------------------------------|
     | patience > greed                                 |
     | character > impulse                              |
     | deliberate play > desperate grab                 |
     |_______________________________________________|
"""


ART_LIBRARY = {
    "monster_face": _monster_face(),
    "midnight_study": _midnight_study(),
    "digital_chessboard": _digital_chessboard(),
    "exam_perfect": _exam_perfect(),
    "hospital_room": _hospital_room(),
    "side_hustle_boxes": _side_hustle_boxes(),
    "counterfeit_warning": _counterfeit_warning(),
    "germany_ticket": _germany_ticket(),
    "plane_regular": _plane_regular(),
    "plane_sketchy": _plane_sketchy(),
    "subway_station": _subway_station(),
    "taxi_jake": _taxi_jake(),
    "frankfurt_skyline": _frankfurt_skyline(),
    "chess_tournament_hall": _chess_tournament_hall(),
    "cathedral_cologne": _cathedral_cologne(),
    "holy_water_vial": _holy_water_vial(),
    "munich_festival": _munich_festival(),
    "shady_bar": _shady_bar(),
    "luxury_bar": _luxury_bar(),
    "doctor_drunk": _doctor_drunk(),
    "dream_couch": _dream_couch(),
    "ship_black_pearl": _ship_black_pearl(),
    "coordinates_map": _coordinates_map(),
    "harbor_town": _harbor_town(),
    "rafael_boat": _rafael_boat(),
    "island_shore": _island_shore(),
    "cave_entrance": _cave_entrance(),
    "stone_chess_table": _stone_chess_table(),
    "treasure_chest": _treasure_chest(),
    "victor_hale": _victor_hale(),
    "explosive_device": _explosive_device(),
    "victor_board": _victor_board(),
    "forum_message": _forum_message(),
    "compass_carving": _compass_carving(),
    "two_player_door": _two_player_door(),
    "giant_chessboard": _giant_chessboard(),
    "final_chest": _final_chest(),
    "home_chess_coin": _home_chess_coin(),
    "bad_ending_shatter": _bad_ending_shatter(),
    "good_ending_glow": _good_ending_glow(),
    "secret_ending_sigil": _secret_ending_sigil(),
    "gallery_1": _gallery_one(),
    "gallery_2": _gallery_two(),
    "gallery_3": _gallery_three(),
    "gallery_4": _gallery_four(),
    "gallery_5": _gallery_five(),
    "gallery_6": _gallery_six(),
    "gallery_7": _gallery_seven(),
    "gallery_8": _gallery_eight(),
    "gallery_9": _gallery_nine(),
    "gallery_10": _gallery_ten(),
    "gallery_11": _gallery_11(),
    "gallery_12": _gallery_12(),
    "gallery_13": _gallery_13(),
    "gallery_14": _gallery_14(),
    "gallery_15": _gallery_15(),
    "gallery_16": _gallery_16(),
    "gallery_17": _gallery_17(),
    "gallery_18": _gallery_18(),
    "gallery_19": _gallery_19(),
    "gallery_20": _gallery_20(),
    "gallery_21": _gallery_21(),
    "gallery_22": _gallery_22(),
    "gallery_23": _gallery_23(),
    "gallery_24": _gallery_24(),
    "gallery_25": _gallery_25(),
    "gallery_26": _gallery_26(),
    "gallery_27": _gallery_27(),
    "gallery_28": _gallery_28(),
    "gallery_29": _gallery_29(),
    "gallery_30": _gallery_30(),
    "gallery_31": _gallery_31(),
    "gallery_32": _gallery_32(),
    "gallery_33": _gallery_33(),
    "gallery_34": _gallery_34(),
    "gallery_35": _gallery_35(),
    "gallery_36": _gallery_36(),
    "gallery_37": _gallery_37(),
    "gallery_38": _gallery_38(),
    "gallery_39": _gallery_39(),
    "gallery_40": _gallery_40(),
    "gallery_41": _gallery_41(),
    "gallery_42": _gallery_42(),
    "gallery_43": _gallery_43(),
    "gallery_44": _gallery_44(),
    "gallery_45": _gallery_45(),
    "gallery_46": _gallery_46(),
    "gallery_47": _gallery_47(),
    "gallery_48": _gallery_48(),
    "gallery_49": _gallery_49(),
    "gallery_50": _gallery_50(),
}


SCENE_ART_MAP = {
    "p001_intro": ["midnight_study", "digital_chessboard"],
    "p002_study_end": ["exam_perfect", "good_ending_glow"],
    "p003_endgame_choice": ["digital_chessboard"],
    "p006_exam_and_call": ["gallery_13"],
    "p007_hospital_path": ["hospital_room"],
    "p008_side_hustle_end": ["side_hustle_boxes", "counterfeit_warning", "bad_ending_shatter"],
    "p010_flight_choice": ["germany_ticket"],
    "p011_plane_crash_end": ["plane_sketchy", "bad_ending_shatter"],
    "p012_arrival_germany": ["plane_regular", "gallery_5"],
    "p013_subway_wallet": ["subway_station"],
    "p015_window_omen": ["gallery_14"],
    "p014_taxi_jake": ["taxi_jake", "gallery_15"],
    "hub_germany_cities": ["gallery_4"],
    "p016_frankfurt": ["frankfurt_skyline", "gallery_16"],
    "p018_tournament_entry": ["chess_tournament_hall", "gallery_17"],
    "p035_tournament_win": ["chess_tournament_hall", "good_ending_glow"],
    "p017_cologne": ["cathedral_cologne", "gallery_18"],
    "p022_priest_truth": ["holy_water_vial"],
    "p018_munich": ["munich_festival", "gallery_19"],
    "p026_shady_bar": ["shady_bar"],
    "p041_luxury_bar": ["luxury_bar"],
    "p030_doctor_requirements": ["doctor_drunk", "gallery_20"],
    "p031_dream_reveal": ["dream_couch", "monster_face"],
    "p036_wake_world": ["ship_black_pearl", "coordinates_map"],
    "p038_hospital_return": ["hospital_room"],
    "p041_research_black_pearl": ["forum_message", "gallery_25"],
    "p048_airport_departure": ["gallery_26"],
    "p049_harbor": ["harbor_town", "rafael_boat"],
    "p052_jungle": ["island_shore", "cave_entrance"],
    "p054_cave_puzzle": ["stone_chess_table", "gallery_29"],
    "p056_hidden_door": ["treasure_chest", "gallery_30"],
    "p060_victor_arrives": ["victor_hale", "explosive_device", "gallery_32"],
    "p068_victor_game_opening": ["victor_board", "gallery_33"],
    "p070_midgame_turn": ["gallery_34"],
    "p072_victor_checkmate": ["gallery_35", "good_ending_glow"],
    "p076_return_home": ["home_chess_coin"],
    "p080_vh_message": ["forum_message", "compass_carving", "gallery_36"],
    "p086_round_two_departure": ["gallery_37"],
    "p093_cliff_meet": ["two_player_door", "gallery_38", "gallery_39"],
    "p101_door_open": ["gallery_40", "gallery_41"],
    "p106_giant_game": ["giant_chessboard", "gallery_42", "gallery_43"],
    "p110_final_checkmate": ["final_chest", "gallery_44"],
    "p116_good_end": ["home_chess_coin", "good_ending_glow", "gallery_46", "gallery_47"],
    "p116_secret_ending": [
        "secret_ending_sigil",
        "gallery_45",
        "gallery_48",
        "gallery_49",
        "gallery_50",
    ],
}


def get_scene_art(scene_id: str, tags: list[str] | None = None) -> list[dict[str, str]]:
    """Return art payload for a scene.

    Fallback policy:
    - explicit map by scene id first
    - fallback by ending tags
    - fallback to a neutral gallery panel
    """
    keys = SCENE_ART_MAP.get(scene_id, [])

    if not keys:
        tags = tags or []
        if "ending" in tags and "bad" in tags:
            keys = ["bad_ending_shatter"]
        elif "ending" in tags and "secret" in tags:
            keys = ["secret_ending_sigil"]
        elif "ending" in tags:
            keys = ["good_ending_glow"]
        else:
            keys = ["gallery_1"]

    payload: list[dict[str, str]] = []
    for key in keys:
        art = ART_LIBRARY.get(key)
        if art:
            payload.append({"id": key, "text": art.strip("\n")})
    return payload
