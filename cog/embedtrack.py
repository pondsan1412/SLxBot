import discord
from discord.ext import commands
from cog import config

#embed variable for track through the numbers
embedMKS = discord.Embed(
        color=discord.Color.brand_red(),
        title="Mario Kart Stadium",
        description="**DE: Mario Kart-Stadion \n NL: Mario Kart-Stadion**"
)
embedMKS.set_author(name="Mushroom Cup",icon_url=config.Mushroom)
embedMKS.set_thumbnail(url=config.Mushroom)
embedMKS.set_image(url=config.MarioKartStadium)

embedWP = discord.Embed(
        color=discord.Color.brand_green(),
        title="Water Park",
        description="**DE: Wasserpark \n NL: Waterpretpark**"
)
embedWP.set_author(name="Mushroom Cup",icon_url=config.Mushroom)
embedWP.set_thumbnail(url=config.Mushroom)
embedWP.set_image(url=config.WaterPark)

embedSSC = discord.Embed(
        color=discord.Color.orange(),
        title="Sweet Sweet Canyon",
        description="**DE: Zuckersüßer Canyon \n NL: Zoetekauwcanyon**"
)
embedSSC.set_author(name="Mushroom Cup",icon_url=config.Mushroom)
embedSSC.set_thumbnail(url=config.Mushroom)
embedSSC.set_image(url=config.SweetSweetCanyon)

embedTR = discord.Embed(
        color=discord.Color.greyple(),
        title="Thwomp Ruins",
        description="**DE: Steinblock-Ruinen \n NL: Thwomps Tempel**"
)
embedTR.set_author(name="Mushroom Cup",icon_url=config.Mushroom)
embedTR.set_thumbnail(url=config.Mushroom)
embedTR.set_image(url=config.ThwompRuins)

embedMC = discord.Embed(
        color=discord.Color.magenta(),
        title="Mario Circuit",
        description="**DE: Steinblock-Ruinen \n NL: Thwomps Tempel**"
)
embedMC.set_author(name="Flower Cup",icon_url=config.Flower)
embedMC.set_thumbnail(url=config.Flower)
embedMC.set_image(url=config.MarioCiruit)

embedTH = discord.Embed(
        color=discord.Color.dark_red(),
        title="Toad Harbor",
        description="**DE: Toads Hafenstadt \n NL: Toad-Baai**"
)
embedTH.set_author(name="Flower Cup",icon_url=config.Flower)
embedTH.set_thumbnail(url=config.Flower)
embedTH.set_image(url=config.ToadHarbor)

embedTM = discord.Embed(
        color=discord.Color.darker_grey(),
        title="Twisted Mansion",
        description="**DE: Gruselwusel-Villa \n NL: Boo's Duizelhuis**"
)
embedTM.set_author(name="Flower Cup",icon_url=config.Flower)
embedTM.set_thumbnail(url=config.Flower)
embedTM.set_image(url=config.TwistedMansion)

embedSGF = discord.Embed(
        color=discord.Color.dark_red(),
        title="Shy Guy Falls",
        description="**DE: Shy Guys Wasserfälle \n NL: Shy Guys Kristalmijn**"
)
embedSGF.set_author(name="Flower Cup",icon_url=config.Flower)
embedSGF.set_thumbnail(url=config.Flower)
embedSGF.set_image(url=config.ShyGuyFalls)

embedSA = discord.Embed(
        color=discord.Color.dark_blue(),
        title="Sunshine Airport",
        description="**DE: Sonnenflughafen \n NL: Sunshine Airport**"
)
embedSA.set_author(name="Star Cup",icon_url=config.Star)
embedSA.set_thumbnail(url=config.Star)
embedSA.set_image(url=config.SunshineAirport)

embedDS = discord.Embed(
        color=discord.Color.teal(),
        title="Dolphin Shoals",
        description="**DE: Delfinlagune \n NL: 	Dolfijnenparadijs**"
)
embedDS.set_author(name="Star Cup",icon_url=config.Star)
embedDS.set_thumbnail(url=config.Star)
embedDS.set_image(url=config.MarioCiruit)

embedEd = discord.Embed(
        color=discord.Color.magenta(),
        title="Electrodrome",
        description="**DE: Discodrom \n NL: Electrodome**"
)
embedEd.set_author(name="Star Cup",icon_url=config.Star)
embedEd.set_thumbnail(url=config.Star)
embedEd.set_image(url=config.Electrodrome)

embedMW = discord.Embed(
        color=discord.Color.purple(),
        title="Mount Wario",
        description="**DE: Wario-Abfahrt \n NL: Wario's Winterberg**"
)
embedMW.set_author(name="Star Cup",icon_url=config.Star)
embedMW.set_thumbnail(url=config.Star)
embedMW.set_image(url=config.MountWario)

embedCC = discord.Embed(
        color=discord.Color.greyple(),
        title="Cloudtop Cruise",
        description="**DE: Wolkenstraße \n NL: Wildewolkenweg**"
)
embedCC.set_author(name="Special Cup",icon_url=config.Special)
embedCC.set_thumbnail(url=config.Special)
embedCC.set_image(url=config.CloudtopCruise)

embedBDD = discord.Embed(
        color=discord.Color.dark_orange(),
        title="Bone Dry Dunes",
        description="**DE: Knochentrockene Dünen \n NL: Dry Bowsers Woestijn**"
)
embedBDD.set_author(name="Special Cup",icon_url=config.Special)
embedBDD.set_thumbnail(url=config.Special)
embedBDD.set_image(url=config.BoneDryDunes)

embedBC = discord.Embed(
        color=discord.Color.orange(),
        title="Bowser's Castle",
        description="**DE: Bowsers Festung \n NL: Bowsers Kasteel**"
)
embedBC.set_author(name="Special Cup",icon_url=config.Special)
embedBC.set_thumbnail(url=config.Special)
embedBC.set_image(url=config.BowserCastle)

embedRR = discord.Embed(
        color=discord.Color.greyple(),
        title="Rainbow Road",
        description="**DE: Regenbogen-Boulevard \n NL: Regenboogbaan**"
)
embedRR.set_author(name="Special Cup",icon_url=config.Special)
embedRR.set_thumbnail(url=config.Special)
embedRR.set_image(url=config.RainbowRoad)

embeddYC = discord.Embed(
        color=discord.Color.green(),
        title="Yoshi Circuit",
        description="**DE: Yoshis Piste \n NL: Yoshi's Circuit**"
)
embeddYC.set_author(name="Egg Cup",icon_url=config.Egg)
embeddYC.set_thumbnail(url=config.Egg)
embeddYC.set_image(url=config.YoshiCircuit)

embeddEA = discord.Embed(
        color=discord.Color.red(),
        title="Excitebike Arena",
        description="**DE: Excitebike-Stadion \n NL: Excitebike-Arena**"
)
embeddEA.set_author(name="Egg Cup",icon_url=config.Egg)
embeddEA.set_thumbnail(url=config.Egg)
embeddEA.set_image(url=config.ExcitebikeArena)

embeddDD = discord.Embed(
        color=discord.Color.orange(),
        title="Dragon Driftway",
        description="**DE: Große Drachenmauer \n NL: Drakendreef**"
)
embeddDD.set_author(name="Egg Cup",icon_url=config.Egg)
embeddDD.set_thumbnail(url=config.Egg)
embeddDD.set_image(url=config.DragonDriftway)

embeddMC = discord.Embed(
        color=discord.Color.dark_purple(),
        title="Mute City",
        description="**DE: Mute City \n NL: Mute City**"
)
embeddMC.set_author(name="Egg Cup",icon_url=config.Egg)
embeddMC.set_thumbnail(url=config.Egg)
embeddMC.set_image(url=config.MuteCity)

embeddBP = discord.Embed(
        color=discord.Color.red(),
        title="Baby Park",
        description="**DE: Baby-Park \n NL: Babypark**"
)
embeddBP.set_author(name="Crossing Cup",icon_url=config.Crossing)
embeddBP.set_thumbnail(url=config.Crossing)
embeddBP.set_image(url=config.BabyPark)

embeddCL = discord.Embed(
        color=discord.Color.yellow(),
        title="Cheese Land",
        description="**DE: Käseland \n NL: Kaasland**"
)
embeddCL.set_author(name="Crossing Cup",icon_url=config.Crossing)
embeddCL.set_thumbnail(url=config.Crossing)
embeddCL.set_image(url=config.CheeseLand)

embeddWW = discord.Embed(
        color=discord.Color.dark_green(),
        title="Wild Woods",
        description="**DE: Wilder Wipfelweg \n NL: Wervelwoud**"
)
embeddWW.set_author(name="Crossing Cup",icon_url=config.Crossing)
embeddWW.set_thumbnail(url=config.Crossing)
embeddWW.set_image(url=config.WildWoods)

embeddAC = discord.Embed(
        color=discord.Color.greyple(),
        title="Animal Crossing",
        description="**DE: Animal Crossing-Dorf \n NL: Animal Crossing**"
)
embeddAC.set_author(name="Crossing Cup",icon_url=config.Crossing)
embeddAC.set_thumbnail(url=config.Crossing)
embeddAC.set_image(url=config.AnimalCrossing)

embeddrMMM = discord.Embed(
        color=discord.Color.brand_green(),
        title="Moo Moo Meadows",
        description="**DE: Kuhmuh-Weide \n NL: Boe-Boe-Boerenland**"
)
embeddrMMM.set_author(name="Shell Cup",icon_url=config.Shell)
embeddrMMM.set_thumbnail(url=config.Shell)
embeddrMMM.set_image(url=config.MooMooMeadows)

embedrMC = discord.Embed(
        color=discord.Color.green(),
        title="Mario Circuit",
        description="**DE: Marios Piste \n NL: 	Mario's Circuit**"
)
embedrMC.set_author(name="Shell Cup",icon_url=config.Shell)
embedrMC.set_thumbnail(url=config.Shell)
embedrMC.set_image(url=config.rMarioCircuit)

embedrCCB = discord.Embed(
        color=discord.Color.blue(),
        title="Cheep Cheep Beach",
        description="**DE: Cheep-Cheep-Strand \n NL: Cheep Cheep-Strand**"
)
embedrCCB.set_author(name="Shell Cup",icon_url=config.Shell)
embedrCCB.set_thumbnail(url=config.Shell)
embedrCCB.set_image(url=config.CheepCheepBeach)

embedrTT = discord.Embed(
        color=discord.Color.blurple(),
        title="Toad's Turnpike",
        description="**DE: Toads Autobahn \n NL: Toads Tolweg**"
)
embedrTT.set_author(name="Shell Cup",icon_url=config.Shell)
embedrTT.set_thumbnail(url=config.Shell)
embedrTT.set_image(url=config.ToadsTurnpike)

embedrDDD = discord.Embed(
        color=discord.Color.gold(),
        title="Dry Dry Desert",
        description="**DE: Staubtrockene Wüste \n NL: Zinderende Zandvlakte**"
)
embedrDDD.set_author(name="Banana Cup",icon_url=config.Banana)
embedrDDD.set_thumbnail(url=config.Banana)
embedrDDD.set_image(url=config.DryDryDesert)

embedrDP3 = discord.Embed(
        color=discord.Color.green(),
        title="Donut Plains 3",
        description="**DE: Donut-Ebene 3 \n NL: Donutvlakte 3**"
)
embedrDP3.set_author(name="Banana Cup",icon_url=config.Banana)
embedrDP3.set_thumbnail(url=config.Banana)
embedrDP3.set_image(url=config.DonutPlains3)

embedrRRy = discord.Embed(
        color=discord.Color.magenta(),
        title="Royal Raceway",
        description="**DE: Königliche Rennpiste \n NL: Koninklijke Kartbaan**"
)
embedrRRy.set_author(name="Banana Cup",icon_url=config.Banana)
embedrRRy.set_thumbnail(url=config.Banana)
embedrRRy.set_image(url=config.RoyalRaceway)

embedrDKJ = discord.Embed(
        color=discord.Color.dark_orange(),
        title="DK Jungle",
        description="**DE: DK Dschungel \n NL: NL: DK's Jungle**"
)
embedrDKJ.set_author(name="Banana Cup",icon_url=config.Banana)
embedrDKJ.set_thumbnail(url=config.Banana)
embedrDKJ.set_image(url=config.DKJungle)

embedrWS = discord.Embed(
        color=discord.Color.dark_gold(),
        title="Wario Stadium",
        description="**DE: Wario-Arena \n NL: Wario's Stadion**"
)
embedrWS.set_author(name="Leaf Cup",icon_url=config.Leaf)
embedrWS.set_thumbnail(url=config.Leaf)
embedrWS.set_image(url=config.WarioStadium)

embeddrSL = discord.Embed(
        color=discord.Color.teal(),
        title="Sherbet Land",
        description="**DE: Sorbet-Land \n NL: IJzige IJsbaan**"
)
embeddrSL.set_author(name="Leaf Cup",icon_url=config.Leaf)
embeddrSL.set_thumbnail(url=config.Leaf)
embeddrSL.set_image(url=config.SherbetLand)

embedrMP = discord.Embed(
        color=discord.Color.orange(),
        title="Music Park",
        description="**DE: Instrumentalpiste \n NL: Muziekcircuit**"
)
embedrMP.set_author(name="Leaf Cup",icon_url=config.Leaf)
embedrMP.set_thumbnail(url=config.Leaf)
embedrMP.set_image(url=config.MusicPark)

embedrYV = discord.Embed(
        color=discord.Color.dark_orange(),
        title="Yoshi Valley",
        description="**DE: Yoshi-Tal \n NL: Yoshi's Vallei**"
)
embedrYV.set_author(name="Leaf Cup",icon_url=config.Leaf)
embedrYV.set_thumbnail(url=config.Leaf)
embedrYV.set_image(url=config.YoshiValley)

embedrTTC = discord.Embed(
        color=discord.Color.gold(),
        title="Tick-Tock Clock",
        description="**DE: Ticktack-Trauma \n NL: Tik-Tak-Klok**"
)
embedrTTC.set_author(name="Lightning Cup",icon_url=config.Lightning)
embedrTTC.set_thumbnail(url=config.Lightning)
embedrTTC.set_image(url=config.TickTockClock)

embedrPPS = discord.Embed(
        color=discord.Color.darker_grey(),
        title="Piranha Plant Slide",
        description="**DE: Röhrenraserei \n NL: Piranha Plant-Parkoers**"
)
embedrPPS.set_author(name="Lightning Cup",icon_url=config.Lightning)
embedrPPS.set_thumbnail(url=config.Lightning)
embedrPPS.set_image(url=config.PiranhaPlantSlide)

embedrGV = discord.Embed(
        color=discord.Color.dark_red(),
        title="Grumble Volcano",
        description="**DE: Vulkangrollen \n NL: Dondervulkaan**"
)
embedrGV.set_author(name="Lightning Cup",icon_url=config.Lightning)
embedrGV.set_thumbnail(url=config.Lightning)
embedrGV.set_image(url=config.GrumbleVolcano)

embedrRRd = discord.Embed(
        color=discord.Color.yellow(),
        title="Rainbow Road",
        description="**DE: Regenbogen-Boulevard \n NL: Regenboogbaan**"
)
embedrRRd.set_author(name="Lightning Cup",icon_url=config.Lightning)
embedrRRd.set_thumbnail(url=config.Lightning)
embedrRRd.set_image(url=config.nRainbowRoad)

embeddWGM = discord.Embed(
        color=discord.Color.dark_gold(),
        title="Wario's Gold Mine",
        description="**DE: Warios Goldmine \n NL: Wario's Goudmijn**"
)
embeddWGM.set_author(name="Triforce Cup",icon_url=config.Triforce)
embeddWGM.set_thumbnail(url=config.Triforce)
embeddWGM.set_image(url=config.WariosGoldMine)

embeddRR = discord.Embed(
        color=discord.Color.purple(),
        title="Rainbow Road",
        description="**DE: Regenbogen-Boulevard \n NL: Regenboogbaan**"
)
embeddRR.set_author(name="Triforce Cup",icon_url=config.Triforce)
embeddRR.set_thumbnail(url=config.Triforce)
embeddRR.set_image(url=config.dRainbowRoad)

embeddIIO = discord.Embed(
        color=discord.Color.yellow(),
        title="Ice Ice Outpost",
        description="**DE: Polarkreis-Parcours \n NL: Toads Poolbasis**"
)
embeddIIO.set_author(name="Triforce Cup",icon_url=config.Triforce)
embeddIIO.set_thumbnail(url=config.Triforce)
embeddIIO.set_image(url=config.IceIceOutpost)

embeddHC = discord.Embed(
        color=discord.Color.dark_green(),
        title="Hyrule Circuit",
        description="**DE: Hyrule-Piste \n NL: Hyrule-Circuit**"
)
embeddHC.set_author(name="Triforce Cup",icon_url=config.Triforce)
embeddHC.set_thumbnail(url=config.Triforce)
embeddHC.set_image(url=config.HyruleCircuit)

embeddNBC = discord.Embed(
        color=discord.Color.dark_purple(),
        title="Neo Bowser City",
        description="**DE: Koopa-Großstadtfieber \n NL: Bowser City**"
)
embeddNBC.set_author(name="Bell Cup",icon_url=config.Bell)
embeddNBC.set_thumbnail(url=config.Bell)
embeddNBC.set_image(url=config.NeoBowserCity)

embeddRiR = discord.Embed(
        color=discord.Color.magenta(),
        title="Ribbon Road",
        description="**DE: Party-Straße \n NL: 	Sprintlint**"
)
embeddRiR.set_author(name="Bell Cup",icon_url=config.Bell)
embeddRiR.set_thumbnail(url=config.Bell)
embeddRiR.set_image(url=config.RibbonRoad)

embeddSBS = discord.Embed(
        color=discord.Color.blurple(),
        title="Super Bell Subway",
        description="**DE: Marios Metro \n NL: Mario's Metro**"
)
embeddSBS.set_author(name="Bell Cup",icon_url=config.Bell)
embeddSBS.set_thumbnail(url=config.Bell)
embeddSBS.set_image(url=config.SuperBellSubway)

embeddBB = discord.Embed(
        color=discord.Color.blue(),
        title="Big Blue",
        description="**DE: Big Blue \n NL: Big Blue**"
)
embeddBB.set_author(name="Bell Cup",icon_url=config.Bell)
embeddBB.set_thumbnail(url=config.Bell)
embeddBB.set_image(url=config.BigBlue)



