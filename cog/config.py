import discord
from discord.ext import commands
#mario kart track photo variable
MarioKartStadium = "https://cdn.discordapp.com/attachments/1123118531328872498/1123118828436602940/MKS.png"
WaterPark = "https://cdn.discordapp.com/attachments/1123118531328872498/1123118994510061598/MK8_Water_Park_Course_Icon.png"
SweetSweetCanyon = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119451466907729/MK8_Sweet_Sweet_Canyon_Course_Icon.png"
ThwompRuins = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119460723724350/MK8_Thwomp_Ruins_Course_Icon.png"
MarioCiruit = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119669998526514/MK8_Mario_Circuit_Course_Icon.png"
ToadHarbor = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119821937184828/MK8_Toad_Harbor_Course_Icon.png"
TwistedMansion = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119829969277038/MK8_Twisted_Mansion_Course_Icon.png"
ShyGuyFalls = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119845198811217/MK8_Shy_Guy_Falls_Course_Icon.png"
SunshineAirport = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119921589661706/MK8_Sunshine_Airport_Course_Icon.png"
DolphinShoals = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119944566055012/MK8_Dolphin_Shoals_Course_Icon.png"
Electrodrome = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119955878105118/MK8_Electrodrome_Course_Icon.png"
MountWario = "https://cdn.discordapp.com/attachments/1123118531328872498/1123119967076892732/MK8_Mount_Wario_Course_Icon.png"
CloudtopCruise = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120116893233202/MK8_Cloudtop_Cruise_Course_Icon.png"
BoneDryDunes = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120130927362079/MK8_Bone-Dry_Dunes_Course_Icon.png"
BowserCastle = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120136128299048/MK8_Bowsers_Castle_Course_Icon.png"
RainbowRoad = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120146735714324/MK8_Rainbow_Road_Course_Icon.png"
YoshiCircuit = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120259642175648/MK8_GCN_Yoshi_Circuit_Course_Icon.png"
ExcitebikeArena = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120270228607007/MK8_Excitebike_Arena_Course_Icon.png"
DragonDriftway = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120290541600798/MK8_Dragon_Driftway_Course_Icon.png"
MuteCity = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120315107655810/MK8_Mute_City_Course_Icon.png"
BabyPark = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120393281093722/MK8_GCN_Baby_Park_Course_Icon.png"
CheeseLand = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120440462819408/MK8_GBA_Cheese_Land_Course_Icon.png"
WildWoods = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120472570220554/MK8_Wild_Woods_Course_Icon.png"
AnimalCrossing = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120487057346650/MK8_Animal_Crossing_Course_Icon.png"
MooMooMeadows = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120661804634193/MK8_Wii_Moo_Moo_Meadows_Course_Icon.png"
rMarioCircuit = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120749868240996/MK8_GBA_Mario_Circuit_Course_Icon.png"
CheepCheepBeach = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120772244844604/MK8_DS_Cheep_Cheep_Beach_Course_Icon.png"
ToadsTurnpike = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120818126327889/MK8_N64_Toads_Turnpike_Course_Icon.png"
DryDryDesert = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120926624583730/MK8_GCN_Dry_Dry_Desert_Course_Icon.png"
DonutPlains3 = "https://cdn.discordapp.com/attachments/1123118531328872498/1123120961034665994/MK8_SNES_Donut_Plains_3_Course_Icon.png"
RoyalRaceway = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121016026189894/MK8_N64_Royal_Raceway_Course_Icon.png"
DKJungle = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121032526581790/MK8_3DS_DK_Jungle_Course_Icon.png"
WarioStadium = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121085278339082/MK8_DS_Wario_Stadium_Course_Icon.png"
SherbetLand = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121105465524294/MK8_GCN_Sherbet_Land_Course_Icon.png"
MusicPark = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121114302906449/MK8_3DS_Music_Park_Course_Icon.png"
YoshiValley = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121191759122542/MK8_N64_Yoshi_Valley_Course_Icon.png"
TickTockClock = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121289582870559/MK8_DS_Tick-Tock_Clock_Course_Icon.png"
PiranhaPlantSlide = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121313490415647/MK8_3DS_Piranha_Plant_Slide_Course_Icon.png"
GrumbleVolcano = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121341801967686/MK8_Wii_Grumble_Volcano_Course_Icon.png"
nRainbowRoad = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121381496868985/MK8_N64_Rainbow_Road_Course_Icon.png"
WariosGoldMine = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121495237992560/MK8_Wii_Warios_Gold_Mine_Course_Icon.png"
dRainbowRoad = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121504540950528/MK8_SNES_Rainbow_Road_Course_Icon.png"
IceIceOutpost = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121553719165079/MK8_Ice_Ice_Outpost_Course_Icon.png"
HyruleCircuit = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121569082908732/MK8_Hyrule_Circuit_Course_Icon.png"
NeoBowserCity = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121615778107462/MK8_3DS_Neo_Bowser_City_Course_Icon.png"
RibbonRoad = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121640671301652/MK8_GBA_Ribbon_Road_Course_Icon.png"
SuperBellSubway = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121698191970344/MK8_Super_Bell_Subway_Course_Icon.png"
BigBlue = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121713652174888/MK8_Big_Blue_Course_Icon.png"
ParisPromenade = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121864143818752/MK8D_Tour_Paris_Promenade_Course_Icon.png"
ToadCircuit = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121874151411812/MK8D_3DS_Toad_Circuit_Course_Icon.png"
ChocoMountain = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121922641760276/MK8D_N64_Choco_Mountain_Course_Icon.png"
CoconutMall = "https://cdn.discordapp.com/attachments/1123118531328872498/1123121938164875404/MK8D_Wii_Coconut_Mall_Course_Icon.png"
TokyoBlur = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122003235323974/MK8D_Tour_Tokyo_Blur_Course_Icon.png"
ShroomRidge = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122027201560596/MK8D_DS_Shroom_Ridge_Course_Icon.png"
SkyGarden = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122035451756564/MK8D_GBA_Sky_Garden_Course_Icon.png"
NinjaHideaway = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122052954607626/MK8D_Ninja_Hideaway_Course_Icon.png"
NewYorkMinute = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122168167927858/MK8D_Tour_New_York_Minute_Course_Icon.png"
MarioCircuit3 = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122185549135882/MK8D_SNES_Mario_Circuit_3_Course_Icon.png"
KalimariDesert = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122201726558248/MK8D_N64_Kalimari_Desert_Course_Icon.png"
WaluigiPinball = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122212963098644/MK8D_DS_Waluigi_Pinball_Course_Icon.png"
SydneySprint = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122276959789156/MK8D_Tour_Sydney_Sprint_Course_Icon.png"
SnowLand = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122302712811611/MK8D_GBA_Snow_Land_Course_Icon.png"
MushroomGorge = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122313500561570/MK8D_Wii_Mushroom_Gorge_Course_Icon.png"
SkyHighSundae = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122327006220378/MK8D_Sky-High_Sundae_Course_Icon.png"
LondonLoop = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122363551191102/MK8D_Tour_London_Loop_Course_Icon.png"
BooLake = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122374150209647/MK8D_GBA_Boo_Lake_Course_Icon.png"
RockRockMountain = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122389685907566/MK8D_3DS_Rock_Rock_Mountain_Course_Icon.png"
MapleTreeway = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122399051780126/MK8D_Wii_Maple_Treeway_Course_Icon.png"
BerlinByways = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122467272142959/MK8D_Tour_Berlin_Byways_Course_Icon.png"
PeachGardens = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122474792529950/MK8D_DS_Peach_Gardens_Course_Icon.png"
MerryMountain = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122487966842990/MK8D_Merry_Mountain_Course_Icon.png"
RainbowRoad7 = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122498448396378/MK8D_3DS_Rainbow_Road_Course_Icon.png"
AmsterdamDrift = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122675561279498/MK8D_Tour_Amsterdam_Drift_Course_Icon.png"
RiversidePark = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122689498943508/MK8D_GBA_Riverside_Park_Course_Icon.png"
DKSummit = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122700743884850/MK8D_Wii_DK_Summit_Course_Icon.png"
YoshisIsland = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122707698024571/MK8D_Yoshis_Island_Course_Icon.png"
BangkokRush = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122756628791297/MK8D_Tour_Bangkok_Rush_Course_Icon.png"
bMarioCircuit = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122779143819374/MK8D_DS_Mario_Circuit_Course_Icon.png"
WaluigiStadium = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122798454382642/MK8D_GCN_Waluigi_Stadium_Course_Icon.png"
SingaporeSpeedway = "https://cdn.discordapp.com/attachments/1123118531328872498/1123122807358894111/MK8D_Tour_Singapore_Speedway_Course_Icon.png"
AthensDash = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278412939333692/MK8D_Tour_Athens_Dash_Course_Icon.png"
DaisyCrusier = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278457638043698/MK8D_GCN_Daisy_Cruiser_Course_Icon.png"
MoonviewHighway = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278497387462757/MK8D_Wii_Moonview_Highway_Course_Icon.png"
SqueakyCleanSprint = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278544606924900/MK8D_Squeaky_Clean_Sprint_Course_Icon.png"
LosAngelesLaps = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278606833627176/MK8D_Tour_Los_Angeles_Laps_Course_Icon.png"
SunsetWilds = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278678451363900/MK8D_GBA_Sunset_Wilds_Course_Icon.png"
KoopaCape = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278693274046496/MK8D_Wii_Koopa_Cape_Course_Icon.png"
VancouverVelocity = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278707375276042/MK8D_Tour_Vancouver_Velocity_Course_Icon.png"

#mario kart cup photo variable
Mushroom = "https://cdn.discordapp.com/attachments/1066340666436747304/1066342499989327892/MK8_MushroomCup.png"
Flower = "https://cdn.discordapp.com/attachments/1066340666436747304/1066342645451989062/MK8_FlowerCup.png"
Star = "https://cdn.discordapp.com/attachments/1066340666436747304/1066342875262103552/MK8_Star_Cup_Emblem.png"
Special = "https://cdn.discordapp.com/attachments/1066340666436747304/1066343758267957268/MK8_Special_Cup_Emblem.png"
Egg = "https://cdn.discordapp.com/attachments/1066340666436747304/1066344200142069840/MK8_Egg_Cup_Emblem.png"
Crossing = "https://cdn.discordapp.com/attachments/1066340666436747304/1066344622965657600/MK8_Crossing_Cup_Emblem.png"
Shell = "https://cdn.discordapp.com/attachments/1066340666436747304/1066345003468718271/MK8_Shell_Cup_Emblem.png"
Banana = "https://cdn.discordapp.com/attachments/1066340666436747304/1066345331379421246/MK8_Banana_Cup_Emblem.png"
Leaf = "https://cdn.discordapp.com/attachments/1066340666436747304/1066345986638757909/MK8_Leaf_Cup_Emblem.png"
Lightning = "https://cdn.discordapp.com/attachments/1066340666436747304/1066346348376498246/MK8_Lightning_Cup_Emblem.png"
Triforce = "https://cdn.discordapp.com/attachments/1066340666436747304/1066346714421788712/MK8_Triforce_Cup_Emblem.png"
Bell = "https://cdn.discordapp.com/attachments/1066340666436747304/1066347079221391430/MK8_Bell_Cup_Emblem.png"
GoldenDash = "https://cdn.discordapp.com/attachments/1066340666436747304/1066352255269343302/MK8D_BCP_Golden_Dash_Emblem.png"
LuckyCat = "https://cdn.discordapp.com/attachments/1066340666436747304/1066352576716607548/MK8D_BCP_Lucky_Cat_Emblem.png"
Turnip = "https://cdn.discordapp.com/attachments/1066340666436747304/1066352954271092766/MK8D_BCP_Turnip_Emblem.png"
Propeller = "https://cdn.discordapp.com/attachments/1066340666436747304/1066353232286330920/MK8D_BCP_Propeller_Emblem.png"
Rock = "https://cdn.discordapp.com/attachments/1066340666436747304/1066353543474331709/MK8D_BCP_Rock_Emblem.png"
Moon = "https://cdn.discordapp.com/attachments/1066340666436747304/1066353849541070969/MK8D_BCP_Moon_Emblem.png"
Fruit = "https://cdn.discordapp.com/attachments/1066340666436747304/1085893267087958056/MK8D_BCP_Fruit_Emblem.png"
Boomerang = "https://cdn.discordapp.com/attachments/1066340666436747304/1085893823189753876/MK8D_BCP_Boomerang_Emblem.png"
Feather = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278175868878868/MK8D_BCP_Feather_Emblem.png"
Cherry = "https://cdn.discordapp.com/attachments/1123118531328872498/1129278561526743060/MK8D_BCP_Cherry_Emblem.png"
#full track info photo variable
Mush = "https://cdn.discordapp.com/attachments/1088214244769681448/1088214465255845888/MushroomList.png"
Flwer = "https://cdn.discordapp.com/attachments/1088214244769681448/1088214575402459196/FlowerList.png"
Sr = "https://cdn.discordapp.com/attachments/1088214244769681448/1088214676002836580/StarList.png"
Speci = "https://cdn.discordapp.com/attachments/1088214244769681448/1088214745234030603/SpecialList.png"
Eg = "https://cdn.discordapp.com/attachments/1088214244769681448/1088214826762895370/EggList.png"
Crss = "https://cdn.discordapp.com/attachments/1088214244769681448/1088214896648392734/CrossingList.png"
Shll = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215004949524590/ShellList.png"
Bana = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215113997242469/BananaList.png"
Lf = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215219408486410/LeafList.png"
Light = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215295434424361/LightningList.png"
Tri = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215395737026762/TriforceList.png"
Bel = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215508727382057/BellList.png"
Golden = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215622904717362/GoldenDashList.png"
LCat = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215707432521738/LuckyCatList.png"
Turn = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215793508044940/TurnipList.png"
Pro = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215854753259662/PropellerList.png"
Rck = "https://cdn.discordapp.com/attachments/1088214244769681448/1088215961045319740/RockList.png"
Mon = "https://cdn.discordapp.com/attachments/1088214244769681448/1088216026379980910/MoonList.png"
Fr = "https://cdn.discordapp.com/attachments/1088214244769681448/1088216107044851772/FruitList.png"
Boomer = "https://cdn.discordapp.com/attachments/1088214244769681448/1088216172190769182/BoomerangList.png"
Featr = "https://cdn.discordapp.com/attachments/1088214244769681448/1129280337013379132/FeatherList.png"
Chrry = "https://cdn.discordapp.com/attachments/1088214244769681448/1129280389467340840/Cherry.png"

#team photo variable
SilentLightning = "https://cdn.discordapp.com/attachments/1066363054473883658/1066363539377369128/Silent_Lightning.png"
SilentBolt = "https://cdn.discordapp.com/attachments/1066363054473883658/1066363527092260984/Silent_Bolt.png"

#cup emoji photo variable
MushroomCup = "<:Mushroom:1087361067568607232>"
FlowerCup = "<:Flower:1087361062812274699>"
StarCup = "<:Star:1087361176687628318>"
SpecialCup = "<:Special:1087361175530000404>"
EggCup = "<:Egg:1087361061008707605>"
CrossingCup = "<:Crossing:1087361060182433882>"
ShellCup = "<:Shell:1087361174607237281>"
BananaCup = "<:Banana:1087361056512422111>"
LeafCup = "<:Leaf:1087361239199522906>"
LightningCup = "<:Lightning:1087361240919179335>>"
TriforceCup = "<:Triforce:1087361070814998649>"
BellCup = "<:Bell:1087361057670058017>"
GoldenDashCup = "<:GoldenDash:1087361064540328018>"
LuckyCatCup = "<:LuckyCat:1087361242219429945>"
TurnipCup = "<:Turnip:1087361179229356095>"
PropellerCup = "<:Propeller:1087361208342020096>"
RockCup = "<:Rock:1087361172778536970>"
MoonCup ="<:Moon:1087361243167330364>"
FruitCup = "<:Fruit:1087361063701467236"
BoomerangCup = "<:Boomerang:1087361059247104060>"
FeatherCup = "<:Feather:1129278953287331840>"
CherryCup = "<:Cherry:1129278955418030100>"

#random emoji variable
Fire = "<a:Fire:966125372942983178>"
x3Fire = "<a:Fire:966125372942983178><a:Fire:966125372942983178><a:Fire:966125372942983178>"
Boohoo = "<:boohoo:1059828958184620053>"
Welcome = "<a:MarioKart:1087801340035600484>"
Error = "<a:DKShutdown:1087800670427562156>"
Down = "<a:WarioCrash:1087800679403360377>"
Working = "<a:YoshiSing:1087793576886403232>"
Successful = "<a:MarioWin:1087800676215701604>"
Pass = "<a:RosalinaDodge:1087794095243665425>"
Problem = "<a:LuigiBlind:1087800673569087578>"
Lucky = "<a:PeachStar:1087800677427859586>"
mariothinking = "<:MarioThink:945866781132746832>"
gigachad = "<:GIGACHAD:1022244779666456687>"
#user_id for embed
developer_id = "<@324207503816654859> (Founder) \n <@257332011075764224> (Co-Founder) \n \n **Assistant:** \n <@209006928272162816> (Assistant for (TT))"

#icon_url for embed
pond_icon_url = "https://media.tenor.com/vgH7rtApnPUAAAAM/jinx-flipzflops.gif"

#picture_url for embed set_image
some_of_anime_girl = "https://media.tenor.com/vgH7rtApnPUAAAAM/jinx-flipzflops.gif"
help_info = "https://cdn.discordapp.com/attachments/1088911898638045246/1088912694423339191/image.png"


#banner track
#standard track
t_MKS= "https://cdn.discordapp.com/attachments/1156152527193133079/1156184794196086826/MKS.png?ex=65140c7f&is=6512baff&hm=f272c7ec0e5029474572b0577a0c434bfd70fb31b52b0b97ae531a9aa9e8a770&"
t_WP = "https://cdn.discordapp.com/attachments/1156152527193133079/1156184867101483078/WP.png?ex=65140c91&is=6512bb11&hm=1e9eb4fcb758197f531499cfe568632898008c6fbeae62c6cf780a2952c5ae55&"
t_SSC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185017463078922/SSC.png?ex=65140cb5&is=6512bb35&hm=d5b70725392c72171712fdbbe118ca26e619b1cac93ad6165430e1a58347a943&"
t_TR = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185068767813632/TR.png?ex=65140cc1&is=6512bb41&hm=e70c97de367ea59855a191944fad22ac5d5897f8c71a1ee1f719741bf7b2a379&"
t_MC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185192596263083/MC.png?ex=65140cde&is=6512bb5e&hm=418a99eb234882e21734890351a66ffba9259bc6f5fe875cb52ba6df2001cfcd&"
t_TH = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185247373856788/TH.png?ex=65140ceb&is=6512bb6b&hm=01e4371be39d6a3b90828ed2e02699abc0afb8096c4f66f390d7fcd29999adb4&"
t_TM = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185317099982949/TM.png?ex=65140cfc&is=6512bb7c&hm=7850559bbb66d4342240c6787f42c08b1972f753d48beeda69bf0c9975bbda59&"
t_SGF = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185493009076254/SGF.png?ex=65140d26&is=6512bba6&hm=cc2ea215a74f084087cee05ca614a2940821300d9bb646ef0f73d19626721494&"
t_SA = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185592292458496/SA.png?ex=65140d3e&is=6512bbbe&hm=2c3bb082a599ce41fce98f88b8c0bb5badbdd1a1ca14d92dac4f17c2f63b536a&"
t_DS = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185638891167794/DS.png?ex=65140d49&is=6512bbc9&hm=822e05aecdb5a7b1d28778568e2bb4c56d16c3e3ad8a7eaba99b7060ddb272a5&"
t_Ed = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185733174923314/Ed.png?ex=65140d5f&is=6512bbdf&hm=5455b8294cc1b9715db8e3a8fa345fc065e11468446e283e83ef07dfb847551b&"
t_MW = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185823327289344/MW.png?ex=65140d75&is=6512bbf5&hm=e8da4daa8288a050c54c9cac1f946fec246e1ff9f4a57771f9de85a5b18995e1&"
t_CC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185897348366417/CC.png?ex=65140d86&is=6512bc06&hm=011a946df04396523133f175ebaf50362fd20fd545e339149a32090f43a86137&"
t_BDD = "https://cdn.discordapp.com/attachments/1156152527193133079/1156185988360577035/BDD.png?ex=65140d9c&is=6512bc1c&hm=2b8acdeeb640e1af42c963037fdb843823d2580191efdaf7eb627bde16addc32&"
t_BC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156186038209892372/BC.png?ex=65140da8&is=6512bc28&hm=7988f23a30774a8d3973202c18e317e37b3edb67d58b2585117796008295c56f&"
t_RR = "https://cdn.discordapp.com/attachments/1156152527193133079/1156186088092745728/RR.png?ex=65140db4&is=6512bc34&hm=f45709c3c4b1fda31c2acae50018520959ee1025513c41ecd141bca8967418db&"
t_dYC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156186162319331380/dYC.png?ex=65140dc5&is=6512bc45&hm=49a4f3a0f40ad290c0b615fde21e5e52d13ee5335a3cef25aca8f2e59df0bcd5&"
t_dEA = "https://cdn.discordapp.com/attachments/1156152527193133079/1156186239549046824/dEA.png?ex=65140dd8&is=6512bc58&hm=7b29cc02d04ba05c856e774335e4935b2f4349252b8e0b7f366eee200ffdcbdf&"
t_dDD = "https://cdn.discordapp.com/attachments/1156152527193133079/1156186295803072622/dDD.png?ex=65140de5&is=6512bc65&hm=39322edf2bf8be854db96ab9d1d1bc371a710779438412d3b1e5d15ccb44bd31&"
t_dMC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156186335246286930/dMC.png?ex=65140def&is=6512bc6f&hm=32ba98355ccc94644773a621f37e5ab8ea6b158c3d5d1d089fde3c892e458824&"
dBP = "https://cdn.discordapp.com/attachments/1156152527193133079/1156283951288172554/dBP_1.png?ex=651468d8&is=65131758&hm=2d6d26a061b0799702f8cc078332bb90d7c6792c5cfd190f73fccee77097c21f&"
dCL = "https://cdn.discordapp.com/attachments/1156152527193133079/1156284228921720952/dCL.png?ex=6514691a&is=6513179a&hm=388fa6e5644d4c18e5efc5b10414e9c548b52759cd00a54909cae6b73c5574b2&"
dWW = "https://cdn.discordapp.com/attachments/1156152527193133079/1156284284009713695/dWW.png?ex=65146928&is=651317a8&hm=77ab8a04335a8b2711ae83dede175e147b12c8d7f4077721603731f246009acb&"
dAC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156284349180825742/dAC.png?ex=65146937&is=651317b7&hm=c977fb9b43f96b2e3480a7e0769ad9bae9118d25fce6d9bf857edf73bfd61478&"
rMMM = "https://cdn.discordapp.com/attachments/1156152527193133079/1156284620724244590/rMMM.png?ex=65146978&is=651317f8&hm=7a3784633a6c97638e71aa5363a93f552f2250044d5903dfe4945876b0596d3e&"
rMC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156284708162904245/rMC.png?ex=6514698d&is=6513180d&hm=81c6f0fe53229dc899fb8c6b989065482fd10abc6b4bc5d42dc99d1ebbeb354d&"
rCCB = "https://cdn.discordapp.com/attachments/1156152527193133079/1156284829411848353/rCCB.png?ex=651469aa&is=6513182a&hm=0a65fe459a7ed0f934f46298db1ccd78ca670bd2bdace36c1ba0657039c07ed0&"
rTT = "https://cdn.discordapp.com/attachments/1156152527193133079/1156284925922770964/rTT.png?ex=651469c1&is=65131841&hm=24ab7a2762c8549fe4e797313d8b24af7d36e456559c474c9162872b8aaaf5e3&"
rDDD = "https://cdn.discordapp.com/attachments/1156152527193133079/1156285160338239488/rDDD.png?ex=651469f8&is=65131878&hm=494f158580802f91e7b8d0d35cbe74cc20df9eed20a3db3f1691486d36206cd8&"
rDKJ = "https://cdn.discordapp.com/attachments/1156152527193133079/1156285694352830494/rDKJ_.png?ex=65146a78&is=651318f8&hm=1e5c305f20ec49913905925c2c55c787955565137cb62141f42c2fe5c6ea0a39&"
rWS = "https://cdn.discordapp.com/attachments/1156152527193133079/1156285782223491093/rWS.png?ex=65146a8d&is=6513190d&hm=fc7e7476378308decfbe58d17388e14b5bfff01897e913959f06afb68993bc1a&"
rSL = "https://cdn.discordapp.com/attachments/1156152527193133079/1156285841983934464/rSL.png?ex=65146a9b&is=6513191b&hm=9318c6daca0138eddc09775d4e56b23ce848a5c1aaff4ec47686aaf02a2df595&"
rMP = "https://cdn.discordapp.com/attachments/1156152527193133079/1156285929321938985/rMP.png?ex=65146ab0&is=65131930&hm=013cd141fb3537ab034ccd11cb48119899f48c7829daa35d6f030b96898b2637&"
rYV = "https://cdn.discordapp.com/attachments/1156152527193133079/1156285982929322004/rYV.png?ex=65146abd&is=6513193d&hm=c6dd20263f980148abb16885105b3b795eb13e2adeecb42c973b8d93d022e40c&"
rTTC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286049740406804/rTTC_.png?ex=65146acd&is=6513194d&hm=30f7ef694e48912c957238ee44ac2a170e9bd2c5e767338092e9190291030117&"
rPPS = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286111820283914/rPPS.png?ex=65146adb&is=6513195b&hm=5c373dc3f144690aacd6a7bfb0c73ff960cce63078d4de029e3d7ce36e3c6209&"
rGV = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286169143840789/rGV.png?ex=65146ae9&is=65131969&hm=17278ba1a52a6833cb7814edddefa54e35678f045cbda4d01ae3014e168a9e41&"
rRRd ="https://cdn.discordapp.com/attachments/1156152527193133079/1156286306935123968/dRRd.png?ex=65146b0a&is=6513198a&hm=4795a9675363a3455eccb564e48101377dd96687c1ee664d21c4a380427b4fb4&"
dWGM = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286399079780502/dWGM.png?ex=65146b20&is=651319a0&hm=ca981104b135cd15b0556e74add05b1a9a78d588101fbdd0f1233590aba2efb5&"
dRR = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286474342375445/dRR.png?ex=65146b32&is=651319b2&hm=42c43c9ffda0da05dd27a6eb7f4496e865a8efae7b9ed2920e953e29c13e86ca&"
dIIo = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286538989178991/dIIO.png?ex=65146b41&is=651319c1&hm=d0421477a306148cf88d59611975b1d737047df16accc0f88562406a92024fa8&"
dHC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286582601547926/dHC.png?ex=65146b4c&is=651319cc&hm=749c7ef597027257b1316afb1273d7cbab778ee62e1fd0a6642ce221c695f2cc&"
dNBC = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286648221433977/dNBC.png?ex=65146b5b&is=651319db&hm=f62dfe692a1f03dd375a67c41392d1949371f2ede0d3f69d9418d248dca50a82&"
dRiR  = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286710146158743/dRiR.png?ex=65146b6a&is=651319ea&hm=6bce75caad8a01ca085c3987d85299e0c856d636202af65db374af8d11b8cff3&"
dBB = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286814005493780/dBB.png?ex=65146b83&is=65131a03&hm=affa4e2bfdcaff035787cd1dcafde7416c179da48a81b48e3ffcde5fa58773d2&"
rDP3 = "https://cdn.discordapp.com/attachments/1156152527193133079/1156285367239057468/rDP3.png?ex=65146a2a&is=651318aa&hm=eda2df7f13aceba99aee858619380b49acf177beba5462be7130b4c7d824c0a3&"
rRRy = "https://cdn.discordapp.com/attachments/1156152527193133079/1156285560516784129/rRRy.png?ex=65146a58&is=651318d8&hm=4c6274238010066f31aa725f27b39448861b007a656cd944035a82f28f4a7fde&"
dSBS = "https://cdn.discordapp.com/attachments/1156152527193133079/1156286762885328937/dSBS.png?ex=65146b77&is=651319f7&hm=7badb81d8cbd5c69c7ed8c1f1ce8ef443875ec47aa9a0c3daddf54220493169b&"
#DLC track
bSCS = "https://cdn.discordapp.com/attachments/1155032331619405875/1155550731605123196/bSCS.PNG"
bTB = "https://cdn.discordapp.com/attachments/1155032331619405875/1156147640749281290/bTB.png?ex=6513e9e5&is=65129865&hm=45aadafd8ef036dc531f9a3b819c75ff6e454479618d0004ac2421f41bcda074&"
bBL = ""





#example picture
example_picture_tt = "https://cdn.discordapp.com/attachments/1091774870024634488/1173520504158687232/Capture.PNG?ex=65644123&is=6551cc23&hm=e48354d04624168a40de0b61430c9cd65cb1a68bdb21ff469b78b9d90369f7a8&"



#spreadsheets
feed_t = "https://spreadsheets.google.com/feeds"
spread_t="https://www.googleapis.com/auth/spreadsheets"
file_t="https://www.googleapis.com/auth/drive.file"
drive_t="https://www.googleapis.com/auth/drive"
sheet_name="Silent Lightning's TT Leaderboard"
sheet_file_Submission="Submissions"
#General > stats
#variable for random text
Text_replying = [
    "Finished",
    "Done",
    "your TT has been update!",
    "thanks for submit your TT!!",
    "great job!! your TT is amazing!",
    "All good",
    "Updated!",
    "submit complete",
    "vollständig einreichen",
    "Schön!",
    "fertig!",
    "Danke!",
    "you should do more TT?",
    

]

#channel for debugging 
#players variable for TTupdate.py
player = [
"AMDX",
"Ant",
"Benjames",
"BIGW",
"FalseKing",
"FreeDobby",
"Holycomb",
"Icedoutcol5n",
"JacKo",
"Kaleb112",
"Leftyginger",
"Ness",
"Ole",
"Paulo22",
"Pond",
"Rick",
"Robertala",
"Rushh",
"Staff",
"Stan",
"Torasshi",
"Vonz",
]

#annoying channel
annoying_channel = [
            873021519897448518,#bot-channel
            873023136092815450, #announcements
            1056810345412427846,#mku-bot-sbx
            1030858079585177761,#mku bot-slx
            1046609392222617620,#streamers-annoucements
            874381861424607314,#TT submit chat
            1054505211206586499,#TT sl

        ]
network_community_dc  = 1158721318200549446

Bagging_track = [
                    'rDDD - Dry Dry Desert ',
                    'dCL - Cheese Land',
                    'rMC - Mario Circuit',
                    'dYC - Yoshi Circuit',
                    'dSBS - Super Bell Subway',
                    'dRiR - Ribbon Road',
                    'BDD - Bone-Dry Dunes',
                    'dDD - Dragon Driftway',
                    'rRRy - Royal Raceway',
                    'MKS - Mario Kart Stadium',
                    'rGV - Grumble Vulcano',
                    'MC - Mario Circuit',
                    'rYV- Yoshi Valley',
                    'dAC - Animal Crossing',
                    'RR - Rainbow Road',
                    'SGF - Shy Guy Falls',
                    'rDP3 - Donut Plains 3',
                    'SSC - Sweet Sweet Canyon',
                    'TR - Thwomps Ruins',
                    'TM - Twisted Mansion',
                    'TH - Toad Harbor',
                    'dHC - Hyrule Circuit',
                    'Ed - Electrodrome',
                    'dBP - Baby Park',
                    'DS - Dolphin Shoals ',
                    'rDKJ - DK Jungle',
                    'dIIO - Ice Ice Outpost',
                    'bPP - Paris Promenade',
                    'bTC - Toad Ciruit',
                    'bCMo - Choco Mountain ',
                    'bCMA - Coconut Mall',
                    'bNYM - New York Minute',
                    'bMC3 - Mario Circuit 3 ',
                    'bKD - Kalimari Desert',
                    'bSL - Snow Land',
                    'bMG - Mushroom Gorge',
                    'bLL - London Loop ',
                    'bBL - Boo Lake',
                    'bRRM - Rock Rock Mountain',
                    'bPG - Peach Gardens',
                    'bMM - Merry Mountain ',
                    'bRP - Riverside Park',
                    'bDKS - DK Summit',
                    'bMC - Mario Circuit',
                    'bSW - Sunset Wilds',
                    ]
loading = "https://media.tenor.com/zk3sVpc7OGkAAAAi/dice-roll-the-dice.gif"
all_track = [
    "Mario Kart Stadium",
    "Water Park",
    "Sweet Sweet Canyon",
    "Thwomp Ruins",
    "Mario Circuit",
    "Toad Harbor",
    "Twisted Mansion",
    "Shy Guy Falls",
    "Sunshine Airport",
    "Dolphin Shoals",
    "Electrodrome",
    "Mount Wario",
    "Cloudtop Cruise",
    "Bone-Dry Dunes",
    "Bowser's Castle",
    "Rainbow Road",
    "Yoshi Circuit",
    "Excitebike Arena",
    "Dragon Driftway",
    "Mute City",
    "Baby Park",
    "Cheese Land",
    "Wild Woods",
    "Animal Crossing",
    "Moo Moo Meadows",
    "Mario Circuit",
    "Cheep Cheep Beach",
    "Toad's Turnpike",
    "Dry Dry Desert",
    "Donut Plains 3",
    "Royal Raceway",
    "DK Jungle",
    "Wario Stadium",
    "Sherbet Land",
    "Music Park",
    "Yoshi Valley",
    "Tick-Tock Clock",
    "Piranha Plant Slide",
    "Grumble Volcano",
    "N64 Rainbow Road",
    "Wario's Gold Mine",
    "SNES Rainbow Road",
    "Ice Ice Outpost",
    "Hyrule Circuit",
    "Neo Bowser City",
    "Ribbon Road",
    "Super Bell Subway",
    "Big Blue",
    "Paris Promenade",
    "Toad Circuit",
    "Choco Mountain",
    "Coconut Mall",
    "Tokyo Blur",
    "Shroom Ridge",
    "Sky Garden",
    "Ninja Hideaway",
    "New York Minute",
    "Mario Circuit 3",
    "Kalimari Desert",
    "Waluigi Pinball",
    "Sydney Sprint",
    "Snow Land",
    "Mushroom Gorge",
    "Sky-High Sundae",
    "London Loop",
    "Boo Lake",
    "Rock Rock Mountain",
    "Maple Treeway",
    "Berlin Byways",
    "Peach Gardens",
    "Merry Mountain",
    "3DS Rainbow Road",
    "Amsterdam Drift",
    "Riverside Park",
    "DK Summit",
    "Yoshi's Island",
    "Bangkok Rush",
    "Mario Circuit",
    "Waluigi Stadium",
    "Singapore Speedway",
    "Athens Dash",
    "Daisy Cruiser",
    "Moonview Highway",
    "Squeaky Clean Sprint",
    "Los Angeles Laps",
    "Sunset Wilds",
    "Koopa Cape",
    "Vancouver Velocity",
]
