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

#user_id for embed
developer_id = "<@324207503816654859> (Founder) \n <@257332011075764224> (Co-Founder) \n \n **Assistant:** \n <@209006928272162816> (Assistant for (TT))"

#icon_url for embed
pond_icon_url = "https://media.tenor.com/vgH7rtApnPUAAAAM/jinx-flipzflops.gif"

#picture_url for embed set_image
some_of_anime_girl = "https://media.tenor.com/vgH7rtApnPUAAAAM/jinx-flipzflops.gif"
help_info = "https://cdn.discordapp.com/attachments/1088911898638045246/1088912694423339191/image.png"

#embed variable for select menus
embedSelect = discord.Embed(
        color=discord.Color.purple(),
        title="A Help Commands",
        description="Info Prefix: `.`",

)
embedSelect.set_image(url=SilentLightning)
embedSelect.set_author(name="Silent Lightning",icon_url=SilentLightning)
embedMushroomcup = discord.Embed(
        color=discord.Color.red(),
        title="#1 Track",
        description="**Mario Stadium Kart Commands:** \n `MKS, mks, 1-1` \n **Water Park Commands:** \n `WP, wp, 1-2` \n **Sweet Sweet Canyon Commands:** \n `SSC, ssc, 1-3` \n **Thwomp Ruin Commands:** \n `TR, tr, 1-4`",
)
embedMushroomcup.set_author(name="Mushroom Cup",icon_url=Mushroom)
embedMushroomcup.set_image(url=Mush)

embedFlowercup = discord.Embed(
        color=discord.Color.orange(),
        title="#2 Track",
        description="**Mario Circuit Commands:** \n `MC, mc, 2-1` \n **Toad Harbor Commands:** \n `TH, th, 2-2` \n **Twisted Mansion Commands:** \n `TM, tm, 2-3` \n **Shy Guy Falls Commands:** \n `SGF, sgf, 2-4`",
)
embedFlowercup.set_author(name="Flower Cup",icon_url=Flower)
embedFlowercup.set_image(url=Flwer)

embedStarcup = discord.Embed(
        color=discord.Color.yellow(),
        title="#3 Track",
        description="**Sunshine Aiport Commands:** \n `SA, sa, 3-1` \n **Dolphin Shoals Commands:** \n `DS, ds, 3-2` \n **Electrodrome Commands:** \n `Ed, ed, 3-3` \n **Mount Wario Commands:** \n `MW, mw, 3-4`",
)
embedStarcup.set_author(name="Star Cup",icon_url=Star)
embedStarcup.set_image(url=Sr)

embedSpecialcup = discord.Embed(
        color=discord.Color.gold(),
        title="#4 Track",
        description="**Cloudtop Cruise Commands:** \n `CC, cc, 4-1` \n **Bone-Dry Dunes Commands:** \n `BDD, bdd, 4-2` \n **Bowser\'s Castle Commands:** \n `BC, bc, 4-3` \n **Rainbow Road Commands:** \n `RR, rr, 4-4`",
)
embedSpecialcup.set_author(name="Special Cup",icon_url=Special)
embedSpecialcup.set_image(url=Speci)

embedEggcup = discord.Embed(
        color=discord.Color.green(),
        title="#5 Track",
        description="**Yoshi Circuit Commands:** \n `dYC, dyc, 5-1` \n **Excitebike Arena Commands:** \n `dEA, dea, 5-2` \n **Dragon Driftway Commands:** \n `dDD, ddd, 5-3` \n **Mute City Commands:** \n `dMC, dmc, 5-4`",
)
embedEggcup.set_author(name="Special Cup",icon_url=Egg)
embedEggcup.set_image(url=Eg)

embedCrossingcup = discord.Embed(
        color=discord.Color.dark_green(),
        title="#6 Track",
        description="**Baby Park Commands:** \n `dBP, dbp, 6-1` \n **Cheese Land Commands:** \n `dCL, dcl, 6-2` \n **Wild Woods Commands:** \n `dWW, dww, 6-3` \n **Animal Crossing Commands:** \n `dAC, dac, 6-4`",
)
embedCrossingcup.set_author(name="Crossing Cup",icon_url=Crossing)
embedCrossingcup.set_image(url=Crss)

embedShellcup = discord.Embed(
        color=discord.Color.brand_green(),
        title="#7 Track",
        description="**Moo Moo Meadows Commands:** \n `rMMM, rmmm, 7-1` \n **Mario Circuit Commands:** \n `rMC, rmc, 7-2` \n **Cheep Cheep Beach Commands:** \n `rCCB, rccb, 7-3` \n **Toad\'s Turnpike Commands:** \n `rTT, rtt, 7-4`",
)
embedShellcup.set_author(name="Shell Cup",icon_url=Shell)
embedShellcup.set_image(url=Shll)

embedBananacup = discord.Embed(
        color=discord.Color.dark_gold(),
        title="#8 Track",
        description="**Dry Dry Desert Commands:** \n `rDDD, rddd, 8-1` \n **Donut Plains 3 Commands:** \n `rDP3, rdp3, 8-2` \n **Royal Raceway Commands:** \n `rRRy, rrry, 8-3` \n **DK Jungle Commands:** \n `rDKJ, rdkj, 8-4`",
)
embedBananacup.set_author(name="Banana Cup",icon_url=Banana)
embedBananacup.set_image(url=Bana)

embedLeafcup = discord.Embed(
        color=discord.Color.dark_orange(),
        title="#9 Track",
        description="**Wario Stadium Commands:** \n `rWS, rws, 9-1` \n **Sherbet Land Commands:** \n `rSL, rsl, 9-2` \n **Music Park Commands:** \n `rMP, rmp, 9-3` \n **Yoshi Valley Commands:** \n `rYV, ryv, 9-4`",
)
embedLeafcup.set_author(name="Leaf Cup",icon_url=Leaf)
embedLeafcup.set_image(url=Lf)

embedLightningcup = discord.Embed(
        color=discord.Color.gold(),
        title="#10 Track",
        description="**Tick-Tock Clock Commands:** \n `rTTC, rttc, 10-1` \n **Piranha Plant Slide Commands:** \n `rPPS, rpps, 10-2` \n **Grumble Volcano Commands:** \n `rGV, rgv, 10-3` \n **Rainbow Road Commands:** \n `rRRd, rrrd, 10-4`",
)
embedLightningcup.set_author(name="Lightning Cup",icon_url=Lightning)
embedLightningcup.set_image(url=Light)

embedTriforcecup = discord.Embed(
        color=discord.Color.orange(),
        title="#11 Track",
        description="**Wario\'s Gold Mine Commands:** \n `dWGM, dWGM, 11-1` \n **Rainbow Road Commands:** \n `dRR, drr, 11-2` \n **Ice Ice Outpost Commands:** \n `dIIO, diio, 11-3` \n **Hyrule Circuit Commands:** \n `rHC, rhc, 11-4`",
)
embedTriforcecup.set_author(name="Triforce Cup",icon_url=Triforce)
embedTriforcecup.set_image(url=Tri)

embedBellcup = discord.Embed(
        color=discord.Color.gold(),
        title="#12 Track",
        description="**Neo Bowser City Commands:** \n `dNBC, dnbc, 12-1` \n **Ribbon Road Commands:** \n `dRiR, drir, 12-2` \n **Super Bell Subway Commands:** \n `dSBS, dsbs, 12-3` \n **Big Blue Commands:** \n `dBB, dbb, 12-4`",
)
embedBellcup.set_author(name="Bell Cup",icon_url=Bell)
embedBellcup.set_image(url=Bel)

embedGoldenDashcup = discord.Embed(
        color=discord.Color.yellow(),
        title="#13 Track",
        description="**Paris Promenade Commands:** \n `bPP, bpp, 12-1` \n **Toad Circuit Commands:** \n `bTC, btc, 13-2` \n **Choco Mountain Commands:** \n `bCMo, bcmo, 13-3` \n **Coconut Mall Commands:** \n `bCMa, bcma, 13-4`",
)
embedGoldenDashcup.set_author(name="Golden Dash Cup",icon_url=GoldenDash)
embedGoldenDashcup.set_image(url=Golden)

embedLuckyCatcup = discord.Embed(
        color=discord.Color.dark_orange(),
        title="#14 Track",
        description="**Tokyo Blur Commands:** \n `bTB, btb, 14-1` \n **Shroom Ridge Commands:** \n `bSR, bsr, 14-2` \n **Sky Garden Commands:** \n `bSG, bsg, 14-3` \n **Ninja Hideaway Commands:** \n `bNH, bnh, 14-4`",
)
embedLuckyCatcup.set_author(name="Lucky Cat Cup",icon_url=LuckyCat)
embedLuckyCatcup.set_image(url=LCat)

embedTurnipcup = discord.Embed(
        color=discord.Color.lighter_grey(),
        title="#15 Track",
        description="**New York Minute Commands:** \n `bNYM, bnym, 15-1` \n **Mario Circuit 3 Commands:** \n `bMC3, bmc3, 15-2` \n **Kalimari Desert Commands:** \n `bKD, bkd, 15-3` \n **Waluigi Pinball Commands:** \n `bWP, bwp, 15-4`",
)
embedTurnipcup.set_author(name="Turnip Cup",icon_url=Turnip)
embedTurnipcup.set_image(url=Turn)

embedPropellercup = discord.Embed(
        color=discord.Color.orange(),
        title="#16 Track",
        description="**Sydney Sprint Commands:** \n `bSS, bss, 16-1` \n **Snow Land Commands:** \n `bSL, bsl, 16-2` \n **Mushroom Gorge Commands:** \n `bMG, bmg, 16-3` \n **Sky-High Sundae Commands:** \n `bSHS, bshs, 16-4`",
)
embedPropellercup.set_author(name="Propeller Cup",icon_url=Propeller)
embedPropellercup.set_image(url=Pro)

embedRockcup = discord.Embed(
        color=discord.Color.dark_grey(),
        title="#17 Track",
        description="**London Loop Commands:** \n `bLL, bll, 17-1` \n **Boo Lake Commands:** \n `bBL, bbl, 17-2` \n **Rock Rock Mountain Commands:** \n `bRRM, brrm, 17-3` \n **Maple Treeway Commands:** \n `bMT, bmt, 17-4`",
)
embedRockcup.set_author(name="Rock Cup",icon_url=Rock)
embedRockcup.set_image(url=Rck)

embedMooncup = discord.Embed(
        color=discord.Color.yellow(),
        title="#18 Track",
        description="**Berlin Byways Commands:** \n `bBB, bbb, 18-1` \n **Peach Gardens Commands:** \n `bPG, bpg, 18-2` \n **Merry Mountain Commands:** \n `bMM, bmm, 18-3` \n **Rainbow Road Commands:** \n `bRR7, brr7, 18-4`",
)
embedMooncup.set_author(name="Moon Cup",icon_url=Moon)
embedMooncup.set_image(url=Mon)

embedFruitcup = discord.Embed(
        color=discord.Color.red(),
        title="#19 Track",
        description="**Amsterdam Drift Commands:** \n `bAD, bad, 19-1` \n **Riverside Park Commands:** \n `bRP, brp, 19-2` \n **DK Summit Commands:** \n `bDKS, bdks, 19-3` \n **Yoshi's Island Commands:** \n `bYI, byi, 19-4`",
)
embedFruitcup.set_author(name="Fruit Cup",icon_url=Fruit)
embedFruitcup.set_image(url=Fr)

embedBoomerangcup = discord.Embed(
        color=discord.Color.lighter_grey(),
        title="#20 Track",
        description="**Bangkok Rush Commands:** \n `bBR, bbr, 20-1` \n **Mario Circuit Commands:** \n `bMC, bmc, 20-2` \n **Waluigi Stadium Commands:** \n `bWS, bws, 20-3` \n **Singapore Speedway Commands:** \n `bSSy, bssy, 20-4`",
)
embedBoomerangcup.set_author(name="Boomerang Cup",icon_url=Boomerang)
embedBoomerangcup.set_image(url=Boomer)

embedDevsTeam = discord.Embed(
        color=discord.Color.dark_purple(),
        title="A Developer Team:",
        description=developer_id
)
embedDevsTeam.set_author(name="Silent Lightning",icon_url=SilentLightning)
embedDevsTeam.set_image(url=SilentLightning)

embedGeneral1 = discord.Embed(
            title="General Command List",
            color=discord.Color.gold(),
            type='rich',
        )
embedGeneral1.set_author(name="Silent Lightning",)
embedGeneral1.add_field(name="A default command",value="")
embedGeneral1.set_image(url=help_info)
embedGeneral1.set_footer(text="Silent Lightning",icon_url=SilentLightning)
