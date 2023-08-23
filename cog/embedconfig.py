import discord
from discord.ext import commands
from cog import config

#embed variable for select menus
embedSelect = discord.Embed(
        color=discord.Color.purple(),
        title="A Help Commands",
        description="Info Prefix: `.`",

)
embedSelect.set_image(url=config.SilentLightning)
embedSelect.set_author(name="Silent Lightning",icon_url=config.SilentLightning)
embedMushroomcup = discord.Embed(
        color=discord.Color.red(),
        title="#1 Track",
        description="**Mario Stadium Kart Commands:** \n `MKS, mks, 1-1` \n **Water Park Commands:** \n `WP, wp, 1-2` \n **Sweet Sweet Canyon Commands:** \n `SSC, ssc, 1-3` \n **Thwomp Ruin Commands:** \n `TR, tr, 1-4`",
)
embedMushroomcup.set_author(name="Mushroom Cup",icon_url=config.Mushroom)
embedMushroomcup.set_image(url=config.Mush)

embedFlowercup = discord.Embed(
        color=discord.Color.orange(),
        title="#2 Track",
        description="**Mario Circuit Commands:** \n `MC, mc, 2-1` \n **Toad Harbor Commands:** \n `TH, th, 2-2` \n **Twisted Mansion Commands:** \n `TM, tm, 2-3` \n **Shy Guy Falls Commands:** \n `SGF, sgf, 2-4`",
)
embedFlowercup.set_author(name="Flower Cup",icon_url=config.Flower)
embedFlowercup.set_image(url=config.Flwer)

embedStarcup = discord.Embed(
        color=discord.Color.yellow(),
        title="#3 Track",
        description="**Sunshine Aiport Commands:** \n `SA, sa, 3-1` \n **Dolphin Shoals Commands:** \n `DS, ds, 3-2` \n **Electrodrome Commands:** \n `Ed, ed, 3-3` \n **Mount Wario Commands:** \n `MW, mw, 3-4`",
)
embedStarcup.set_author(name="Star Cup",icon_url=config.Star)
embedStarcup.set_image(url=config.Sr)

embedSpecialcup = discord.Embed(
        color=discord.Color.gold(),
        title="#4 Track",
        description="**Cloudtop Cruise Commands:** \n `CC, cc, 4-1` \n **Bone-Dry Dunes Commands:** \n `BDD, bdd, 4-2` \n **Bowser\'s Castle Commands:** \n `BC, bc, 4-3` \n **Rainbow Road Commands:** \n `RR, rr, 4-4`",
)
embedSpecialcup.set_author(name="Special Cup",icon_url=config.Special)
embedSpecialcup.set_image(url=config.Speci)

embedEggcup = discord.Embed(
        color=discord.Color.green(),
        title="#5 Track",
        description="**Yoshi Circuit Commands:** \n `dYC, dyc, 5-1` \n **Excitebike Arena Commands:** \n `dEA, dea, 5-2` \n **Dragon Driftway Commands:** \n `dDD, ddd, 5-3` \n **Mute City Commands:** \n `dMC, dmc, 5-4`",
)
embedEggcup.set_author(name="Special Cup",icon_url=config.Egg)
embedEggcup.set_image(url=config.Eg)

embedCrossingcup = discord.Embed(
        color=discord.Color.dark_green(),
        title="#6 Track",
        description="**Baby Park Commands:** \n `dBP, dbp, 6-1` \n **Cheese Land Commands:** \n `dCL, dcl, 6-2` \n **Wild Woods Commands:** \n `dWW, dww, 6-3` \n **Animal Crossing Commands:** \n `dAC, dac, 6-4`",
)
embedCrossingcup.set_author(name="Crossing Cup",icon_url=config.Crossing)
embedCrossingcup.set_image(url=config.Crss)

embedShellcup = discord.Embed(
        color=discord.Color.brand_green(),
        title="#7 Track",
        description="**Moo Moo Meadows Commands:** \n `rMMM, rmmm, 7-1` \n **Mario Circuit Commands:** \n `rMC, rmc, 7-2` \n **Cheep Cheep Beach Commands:** \n `rCCB, rccb, 7-3` \n **Toad\'s Turnpike Commands:** \n `rTT, rtt, 7-4`",
)
embedShellcup.set_author(name="Shell Cup",icon_url=config.Shell)
embedShellcup.set_image(url=config.Shll)

embedBananacup = discord.Embed(
        color=discord.Color.dark_gold(),
        title="#8 Track",
        description="**Dry Dry Desert Commands:** \n `rDDD, rddd, 8-1` \n **Donut Plains 3 Commands:** \n `rDP3, rdp3, 8-2` \n **Royal Raceway Commands:** \n `rRRy, rrry, 8-3` \n **DK Jungle Commands:** \n `rDKJ, rdkj, 8-4`",
)
embedBananacup.set_author(name="Banana Cup",icon_url=config.Banana)
embedBananacup.set_image(url=config.Bana)

embedLeafcup = discord.Embed(
        color=discord.Color.dark_orange(),
        title="#9 Track",
        description="**Wario Stadium Commands:** \n `rWS, rws, 9-1` \n **Sherbet Land Commands:** \n `rSL, rsl, 9-2` \n **Music Park Commands:** \n `rMP, rmp, 9-3` \n **Yoshi Valley Commands:** \n `rYV, ryv, 9-4`",
)
embedLeafcup.set_author(name="Leaf Cup",icon_url=config.Leaf)
embedLeafcup.set_image(url=config.Lf)

embedLightningcup = discord.Embed(
        color=discord.Color.gold(),
        title="#10 Track",
        description="**Tick-Tock Clock Commands:** \n `rTTC, rttc, 10-1` \n **Piranha Plant Slide Commands:** \n `rPPS, rpps, 10-2` \n **Grumble Volcano Commands:** \n `rGV, rgv, 10-3` \n **Rainbow Road Commands:** \n `rRRd, rrrd, 10-4`",
)
embedLightningcup.set_author(name="Lightning Cup",icon_url=config.Lightning)
embedLightningcup.set_image(url=config.Light)

embedTriforcecup = discord.Embed(
        color=discord.Color.orange(),
        title="#11 Track",
        description="**Wario\'s Gold Mine Commands:** \n `dWGM, dWGM, 11-1` \n **Rainbow Road Commands:** \n `dRR, drr, 11-2` \n **Ice Ice Outpost Commands:** \n `dIIO, diio, 11-3` \n **Hyrule Circuit Commands:** \n `rHC, rhc, 11-4`",
)
embedTriforcecup.set_author(name="Triforce Cup",icon_url=config.Triforce)
embedTriforcecup.set_image(url=config.Tri)

embedBellcup = discord.Embed(
        color=discord.Color.gold(),
        title="#12 Track",
        description="**Neo Bowser City Commands:** \n `dNBC, dnbc, 12-1` \n **Ribbon Road Commands:** \n `dRiR, drir, 12-2` \n **Super Bell Subway Commands:** \n `dSBS, dsbs, 12-3` \n **Big Blue Commands:** \n `dBB, dbb, 12-4`",
)
embedBellcup.set_author(name="Bell Cup",icon_url=config.Bell)
embedBellcup.set_image(url=config.Bel)

embedGoldenDashcup = discord.Embed(
        color=discord.Color.yellow(),
        title="#13 Track",
        description="**Paris Promenade Commands:** \n `bPP, bpp, 12-1` \n **Toad Circuit Commands:** \n `bTC, btc, 13-2` \n **Choco Mountain Commands:** \n `bCMo, bcmo, 13-3` \n **Coconut Mall Commands:** \n `bCMa, bcma, 13-4`",
)
embedGoldenDashcup.set_author(name="Golden Dash Cup",icon_url=config.GoldenDash)
embedGoldenDashcup.set_image(url=config.Golden)

embedLuckyCatcup = discord.Embed(
        color=discord.Color.dark_orange(),
        title="#14 Track",
        description="**Tokyo Blur Commands:** \n `bTB, btb, 14-1` \n **Shroom Ridge Commands:** \n `bSR, bsr, 14-2` \n **Sky Garden Commands:** \n `bSG, bsg, 14-3` \n **Ninja Hideaway Commands:** \n `bNH, bnh, 14-4`",
)
embedLuckyCatcup.set_author(name="Lucky Cat Cup",icon_url=config.LuckyCat)
embedLuckyCatcup.set_image(url=config.LCat)

embedTurnipcup = discord.Embed(
        color=discord.Color.lighter_grey(),
        title="#15 Track",
        description="**New York Minute Commands:** \n `bNYM, bnym, 15-1` \n **Mario Circuit 3 Commands:** \n `bMC3, bmc3, 15-2` \n **Kalimari Desert Commands:** \n `bKD, bkd, 15-3` \n **Waluigi Pinball Commands:** \n `bWP, bwp, 15-4`",
)
embedTurnipcup.set_author(name="Turnip Cup",icon_url=config.Turnip)
embedTurnipcup.set_image(url=config.Turn)

embedPropellercup = discord.Embed(
        color=discord.Color.orange(),
        title="#16 Track",
        description="**Sydney Sprint Commands:** \n `bSS, bss, 16-1` \n **Snow Land Commands:** \n `bSL, bsl, 16-2` \n **Mushroom Gorge Commands:** \n `bMG, bmg, 16-3` \n **Sky-High Sundae Commands:** \n `bSHS, bshs, 16-4`",
)
embedPropellercup.set_author(name="Propeller Cup",icon_url=config.Propeller)
embedPropellercup.set_image(url=config.Pro)

embedRockcup = discord.Embed(
        color=discord.Color.dark_grey(),
        title="#17 Track",
        description="**London Loop Commands:** \n `bLL, bll, 17-1` \n **Boo Lake Commands:** \n `bBL, bbl, 17-2` \n **Rock Rock Mountain Commands:** \n `bRRM, brrm, 17-3` \n **Maple Treeway Commands:** \n `bMT, bmt, 17-4`",
)
embedRockcup.set_author(name="Rock Cup",icon_url=config.Rock)
embedRockcup.set_image(url=config.Rck)

embedMooncup = discord.Embed(
        color=discord.Color.yellow(),
        title="#18 Track",
        description="**Berlin Byways Commands:** \n `bBB, bbb, 18-1` \n **Peach Gardens Commands:** \n `bPG, bpg, 18-2` \n **Merry Mountain Commands:** \n `bMM, bmm, 18-3` \n **Rainbow Road Commands:** \n `bRR7, brr7, 18-4`",
)
embedMooncup.set_author(name="Moon Cup",icon_url=config.Moon)
embedMooncup.set_image(url=config.Mon)

embedFruitcup = discord.Embed(
        color=discord.Color.red(),
        title="#19 Track",
        description="**Amsterdam Drift Commands:** \n `bAD, bad, 19-1` \n **Riverside Park Commands:** \n `bRP, brp, 19-2` \n **DK Summit Commands:** \n `bDKS, bdks, 19-3` \n **Yoshi's Island Commands:** \n `bYI, byi, 19-4`",
)
embedFruitcup.set_author(name="Fruit Cup",icon_url=config.Fruit)
embedFruitcup.set_image(url=config.Fr)

embedBoomerangcup = discord.Embed(
        color=discord.Color.lighter_grey(),
        title="#20 Track",
        description="**Bangkok Rush Commands:** \n `bBR, bbr, 20-1` \n **Mario Circuit Commands:** \n `bMC, bmc, 20-2` \n **Waluigi Stadium Commands:** \n `bWS, bws, 20-3` \n **Singapore Speedway Commands:** \n `bSSy, bssy, 20-4`",
)
embedBoomerangcup.set_author(name="Boomerang Cup",icon_url=config.Boomerang)
embedBoomerangcup.set_image(url=config.Boomer)

embedFeathercup = discord.Embed(
        color=discord.Color.dark_orange(),
        title="#21 Track",
        description="**Athens Dash Commands:** \n `bAtD, batd, 21-1` \n **Daisy Cruiser Commands:** \n `bDC, bdc, 21-2` \n **Moonview Highway Commands:** \n `bMH, bmh, 21-3` \n **Squeaky Clean Sprint Commands:** \n `bSCS, bscs, 21-4`",
)
embedFeathercup.set_author(name="Feather Cup",icon_url=config.Feather)
embedFeathercup.set_image(url=config.Featr)

embedCherrycup = discord.Embed(
        color=discord.Color.dark_red(),
        title="#22 Track",
        description="**Los Angeles Laps Commands:** \n `bLAL, blal, 22-1` \n **Sunset Wilds Commands:** \n `bSW, bsw, 22-2` \n **Koopa Cape Commands:** \n `bKC, bkc, 22-3` \n **Vancouver Velocity Commands:** \n `bVV, bvv, 22-4`",
)
embedCherrycup.set_author(name="Cherry Cup",icon_url=config.Cherry)
embedCherrycup.set_image(url=config.Chrry)


embedDevsTeam = discord.Embed(
        color=discord.Color.dark_purple(),
        title="A Developer Team:",
        description=config.developer_id
)
embedDevsTeam.set_author(name="Silent Lightning",icon_url=config.SilentLightning)
embedDevsTeam.set_image(url=config.SilentLightning)

embedGeneral1 = discord.Embed(
            title="General Command List",
            color=discord.Color.gold(),
            type='rich',
        )
embedGeneral1.set_author(name="Silent Lightning",)
embedGeneral1.add_field(name="A default command",value="")
embedGeneral1.set_image(url=config.help_info)
embedGeneral1.set_footer(text="Silent Lightning",icon_url=config.SilentLightning)
