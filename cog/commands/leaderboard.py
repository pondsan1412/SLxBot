#team SLx  Timetrials Leaderboard in mario kart games
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord import Embed
from cog import config
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Silent Lightning's TT Leaderboard")
file_in_sheet_testsheet = sheet.worksheet("Submissions")

#Gspread pages
top_ranking = sheet.worksheet("Top Ranking")
overall_s = sheet.worksheet("150ccS")
overall_dlc = sheet.worksheet("150ccDLC")
player_tab = sheet.worksheet("Players")
#overall
top_all ={
    "top_all":{
        "range":"G2:J22",
        "image_url":"https://cdn.discordapp.com/attachments/1066363054473883658/1155036284205674507/New_Project_1.png?ex=65147c1d&is=65132a9d&hm=9b4aeba7711ff3f836d0286c5266b62933f6f3841c2087ca51a9df7f715f8103&"
    },
}
top_s  = {
    "top_s":{
        "range":"V4:Y22",
        "image_url":"https://media.discordapp.net/attachments/1156152527193133079/1156152806986752031/S.png?ex=6513eeb5&is=65129d35&hm=eeddfdf42a93d048b4449b8e5aa7c4802d2efe6ddd6005964537fc37f20190d0&="
    },
}     
top_dlc = {"top_dlc":{"range":"V4:Y22","image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1156287206747549806/DLC.png?ex=65146be0&is=65131a60&hm=74093c16774afa1996fc4638c0d88455972435814009bf4f5f3bdf9d1f5a00b6&"}}  
#track variable for worksheet get value
#add anytrack here bro
dlc_track = {
    "Tour Paris Promenade":{
        "range":"B4:E15",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172473780979904604/pa.PNG?ex=6560724c&is=654dfd4c&hm=1e4da7b9521148590de88ae89e21b4c6c185a6b65a0c87567d1af421366e7787&"
    },
    "3DS Toad Circuit":{
        "range":"G4:J15",
        "image_url":"https://media.discordapp.net/attachments/1156152527193133079/1172472137290887188/toad.png?ex=656070c5&is=654dfbc5&hm=af0fa32972797726c1025666aa6c8a9824916688e266402e5f2593951ed779cd&="
    },
    "N64 Choco Mountain":{
        "range":"L4:O15",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172471986555986001/cho.png?ex=656070a1&is=654dfba1&hm=4517232483c52c9455cdfc5c84d4186265202a62651105ee2c9fe62737598df3&"
    },
    "Wii Coconut Mall":{
        "range":"Q4:T15",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172474884341895178/coconut.PNG?ex=65607353&is=654dfe53&hm=299c7e970e248994bf2be075833be02f048288d09d383c9f77dc1b41966d1497&"
    },
    "Tour Tokyo Blur":{
        "range":"B17:E28",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472137483833344/tokyo.png?ex=656070c5&is=654dfbc5&hm=4e3a7878b2768c7c3909917851387808c64885d51a7cee16149b052424731cb5&"
    },
    "DS Shroom Ridge":{
        "range":"G17:J28",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472135948705852/shroom_ridge.png?ex=656070c4&is=654dfbc4&hm=dc1bbec662c1890c3791a539a3f77c1a3e9b9ac01a367c2d6949c806061a867a&"
    },
    "GBA Sky Garden":{
        
        "range":"L17:O28",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472136141647892/sky_garden.png?ex=656070c4&is=654dfbc4&hm=2f806cc47b114aea806c940b1429be1df68b9e17542ace7b19afaac58c13c24d&"
    },
    "Ninja Hideaway":{
        "range":"Q17:T28",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472107335176212/ninja.png?ex=656070bd&is=654dfbbd&hm=495ad3da70bd1ee739e05a217afe6a2bc7faf8b278c13cb2028f1124f057a5c6&"
    },
    "Tour New York Minute":{
        "range":"B30:E41",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472107087695922/newyork.png?ex=656070bd&is=654dfbbd&hm=117a49362f29f67a06f20fcf7d7c81567d5ad91b41da6da8777fe7e23a3cf437&"
    },
    "SNES Mario Circuit 3":{
        "range":"G30:J41",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172471985670995968/bmc3.png?ex=656070a0&is=654dfba0&hm=34ed4b5ac046f026d60850dfeb657e069d1f80d444b13a2d0dbe6445161b6152&"
    },
    "N64 Kalimari Desert":{
        "range":"L30:J41",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472057313898536/desert.png?ex=656070b1&is=654dfbb1&hm=29e29556278a906266330abfd73473885de74e7b20a4f042eb6dde56d0cbf257&"
    },
    "DS Waluigi Pinball":{
        "range":"Q30:T41",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472160351162408/wp.png?ex=656070ca&is=654dfbca&hm=48a3787d17b3729a15e26cd1bed0c5a44a3a3acaa28fb38834daccdea2230312&"
    },
    "Tour Sydney Sprint":{
        "range":"B43:E54",
        "image_url":"https://media.discordapp.net/attachments/1156152527193133079/1172472137081167932/sydney.png?ex=656070c4&is=654dfbc4&hm=cf4d6351bfa4b10fe63ce1c6e8c6503651ede1dbff595cad827f572385834ca8&="
    },
    "GBA Snow Land":{
        "range":"G43:J54",
        "image_url":"https://media.discordapp.net/attachments/1156152527193133079/1172472136523325510/snow_land.png?ex=656070c4&is=654dfbc4&hm=c17bd8f33ac5ba02a3309aa608b438ee709908565e1e9ed2dc962dc7fbea84c1&="
    },
    "Wii Mushroom Gorge":{
        "range":"L43:O54",
        "image_url":"https://media.discordapp.net/attachments/1156152527193133079/1172472106592784384/mg.png?ex=656070bd&is=654dfbbd&hm=b5901034690ca83814ead6415407246a04d028e3afa919f0780e6e84ab894e49&="
    },
    "Sky-High Sundae":{
        "range":"Q43:T54",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472136322011146/sky.png?ex=656070c4&is=654dfbc4&hm=5f741c832288ce53cebd8adc69dc0ee7c7a30aa3b7e3d0b19b009c9c5ba50fc1&"
    },
    "Tour London Loop":{
        "range":"B56:E67",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472057980792842/london.png?ex=656070b2&is=654dfbb2&hm=fe43a5264a44f73688aaf3bc36c548702bb50f12a47a287f13746482626bf1fc&"
    },
    "GBA Boo Lake":{
        "range":"G56:J67",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172471985863917578/boo.png?ex=656070a0&is=654dfba0&hm=ddb369db563076771cb9493d5090d2d59f01a816a1f8277c08965346583fc023&"
    },
    "3DS Rock Rock Mountain":{
        "range":"L56:O67",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472135709642762/roc.png?ex=656070c4&is=654dfbc4&hm=2b9ac7ccf4557d26ac32d8782c4e43c991c6b6ce28422fa1fae9bfb051762430&"
    },
    "Wii Maple Treeway":{
        "range":"Q56:T67",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472058203078666/maple.png?ex=656070b2&is=654dfbb2&hm=08246d1812f18b7f378bdad9d974e474bce8026fa87a34ede6db1d5b0183820b&"
    },
    "Tour Berlin Byways":{
        "range":"B69:E80",
        "image_url":"https://media.discordapp.net/attachments/1156152527193133079/1172471985217994762/bbb.png?ex=656070a0&is=654dfba0&hm=dfc68087a0ebeb5648536f092e54e243df953106cd382285fe314a78ef0c3089&="
    },
    "DS Peach Gardens":{
        "range":"G69:J80",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472107536494592/peach_garden.png?ex=656070bd&is=654dfbbd&hm=93427b95b818c492ff15256eea58d8640345160a244fe28c2950b9e890a87dcf&"
    },
    "Merry Mountain":{
        "range":"L69:O80",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472058899333130/merry.png?ex=656070b2&is=654dfbb2&hm=d1d6ad7c4823c23d907476e445feb0b361299ab818dcf60e7f1fffcf2cd78970&"
    },
    "3DS Rainbow Road":{
        "range":"Q69:T80",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172471986274959360/brr7.png?ex=656070a1&is=654dfba1&hm=1d63f3155c5aaa17c903c38fc32e9c0d17ce62bcd49166761c3ce24e8a076fe7&"
    },
    "Tour Amsterdam Drift":{
        "range":"B82:E93",
        "image_url":"https://media.discordapp.net/attachments/1156152527193133079/1172471984773398589/amsterdam.png?ex=656070a0&is=654dfba0&hm=5bc0426099922cc00657efff98aa95cac64c63b14d234a2b86ed00a335b72793&="
    },
    "GBA Riverside Park":{
        "range":"G82:J93",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472108610244630/riverside_park.png?ex=656070be&is=654dfbbe&hm=ed6f423e4e6ceca7c00b10c18b2724c54378bc84a3c5c3b6d312a2a0ea0bc1e3&"
    },
    "Wii DK Summit":{
        "range":"L82:O93",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172477342627659856/dk.PNG?ex=6560759e&is=654e009e&hm=9925016f1a3f25277fafab0eebd14e83c17dfdcd5a35ecf6f2c09aa92e51a882&"
    },
    "Yoshi's Island":{
        "range":"Q82:T93",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472160925798481/yoshi.png?ex=656070ca&is=654dfbca&hm=d492baa9817aaabf967ad50fb9c429cd3b664ba06ae8c00cc22162c6e304a21d&"
    },
    "Tour Bangkok Rush":{
        "range":"B95:E106",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172471985431912459/bbr.png?ex=656070a0&is=654dfba0&hm=2f14d598895de215c179d461b62d7c811572405617991dfc7db88e2a5841ac82&"
    },
    "DS Mario Circuit":{
        "range":"G95:J106",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472058681241710/mc.png?ex=656070b2&is=654dfbb2&hm=ab23d5cbf338a60be74e1398d1c8627852018d1b528a1d79ac748764d6129001&"
    },
    "GCN Waluigi Stadium":{
        "range":"L95:O106",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472160623800370/ws.png?ex=656070ca&is=654dfbca&hm=7f64fd94033fcdffd4780c139d969c9cef41213903514b77c6fb701ae43bf723&"
    },
    "Tour Singapore Speedway":{
        "range":"Q95:T106",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472136703684658/ssry.png?ex=656070c4&is=654dfbc4&hm=de0c28d3bfbe35cff76408064ac2bcc15aaaab3b7b6a7e74c9d4df50d7b8d788&"
    },
    "Tour Athens Dash":{
        "range":"B108:E119",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172471984551116830/ad.png?ex=656070a0&is=654dfba0&hm=7b247cfacec136bb8037c25dbf0fac842f4fda12d70eb241af480d3f5ace15fc&"
    },
    "GCN Daisy Cruiser":{
        "range":"G108:J119",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472056881872936/dc.jpg?ex=656070b1&is=654dfbb1&hm=d2c2e39d0509c12b1de7bdcc880c20a5a517a6135a73e401bdb0f5005b37d320&"
    },
    "Wii Moonview Highway":{
        "range":"L108:O119",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472106844434452/mh.png?ex=656070bd&is=654dfbbd&hm=d2c5db564a3953da9013dbf020578d26cef56f7865bc1367ab93c5528d23dd6c&"
    },
    "Squeaky Clean Sprint":{
        "range":"Q108:T119",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172471985008296026/bathroom.png?ex=656070a0&is=654dfba0&hm=4b24c9fdadff1c8234b47abacae15001048cb865872ad1d7016e1587a7b50869&"
    },
    "Tour Los Angeles Laps":{
        "range":"B121:E132",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472057766879232/la.png?ex=656070b2&is=654dfbb2&hm=8cb9594683311b3bf80888888eb4ef6a48ddcc7975b5c0b49f0a5e9c23adaac3&"
    },
    "GBA Sunset Wilds":{
        "range":"G121:J132",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472136909213706/sw.png?ex=656070c4&is=654dfbc4&hm=cbb8c85f461d38157a056b7766fcffcb366ac1d01fba76e1b1f7259b851c4a88&"
    },
    "Wii Koopa Cape":{
        "range":"L121:O132",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172478497252450334/kc.PNG?ex=656076b1&is=654e01b1&hm=0766d91914b22def8dfd31072335a0d8b1bf2272f6e2f4622bf03d3b9521ce8e&"
    },
    "Tour Vancouver Velocity":{
        "range":"Q121:T132",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472160124686406/vc.png?ex=656070ca&is=654dfbca&hm=2bead0bbc2e2ddb1f5f3d292759d65a454bac3ef7d2e9b69dc7f3368f4936d19&"
    },
    "Tour Rome Avanti":{
        "range":"B134:E145",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472108174028840/raw.bra.png?ex=656070be&is=654dfbbe&hm=19a339bc0e3a414a71441514a7a565aec127ae01f486a8cc8a99dc6793a2cb39&"
    },
    "GCN DK Mountain":{
        "range":"G134:J145",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472057531990077/dkm.png?ex=656070b1&is=654dfbb1&hm=2684565ef539af2690aceeb9ddc7ae09ca8eece0f15428518a2b9d8ab19de79c&"
    },
    "Wii Daisy Circuit":{
        "range":"L134:O145",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472057104179211/dci.jpg?ex=656070b1&is=654dfbb1&hm=4b48a4bc31fc1f1e8719ec55b160a76004f6b57bf10bad6065bcabc8b5b39249&"
    },
    "Piranha Plant Cove":{
        "range":"Q134:T145",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472107972710400/raw.bppc.jpg?ex=656070be&is=654dfbbe&hm=7ceafd1d75e8a299e945dbc84def43b62d97365fabc5e9655d16d1c2cc9cab46&"
    },
    "Tour Madrid Drive":{
        "range":"B147:E158",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472058429579324/marid.png?ex=656070b2&is=654dfbb2&hm=61a3eff95d3694be5aa6317eed13a5214b5788b0b1cffea358da9565d289a4f1&"
    },
    "3DS Rosalina's Ice World":{
        "range":"G147:J158",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472108392124426/raw.ice.jpg?ex=656070be&is=654dfbbe&hm=2e4d5e3a0396770bf4b2a2d46f96bb3b159e449b2fb501e4d9536b977dde368d&"
    },
    "SNES Bowser's Castle 3":{
        "range":"L147:O158",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172472107754590228/raw.bc3.jpg?ex=656070bd&is=654dfbbd&hm=25a1803d11ef92b70b7b0464401fd2d859e8d17b34193669dc80e2f6ac042dbe&"
    },
    "Wii Rainbow Road":{
        "range":"Q147:T158",
        "image_url":"https://cdn.discordapp.com/attachments/1156152527193133079/1172479632562466857/brr.png?ex=656077c0&is=654e02c0&hm=4a21fb5b3fff7d113c6d9f1cba3aa593650957e3395fc28681861467e9681ca6&"
    },
    
}
    
    

standard_track = {
    "Mario Kart Stadium":{
        "range":"B4:E15",
        "image_url":config.t_MKS
    },
    "Water Park":{
        "range":"G6:J15",
        "image_url":config.t_WP
    },
    "Sweet Sweet Canyon":{
        "range":"L6:O15",
        "image_url":config.t_SSC
    },
    "Thwomp Ruins":{
        "range":"Q4:T15",
        "image_url":config.t_TR 
    },
    "GBA Mario Circuit":{
        "range":"B17:E28",
        "image_url":config.t_MC 
    },
    "Toad Harbor":{
        "range":"G17:J28",
        "image_url":config.t_TH 
    },
    "Twisted Mansion":{
        "range":"L17:O28",
        "image_url":config.t_TM 
    },
    "Shy Guy Falls":{
        "range":"Q17:T28",
        "image_url":config.t_SGF 
    },
    "Sunshine Airport":{
        "range":"B30:E41",
        "image_url":config.t_SA 
    },
    "Dolphin Shoals":{
        "range":"G30:J41",
        "image_url":config.t_DS 
    },
    "Electrodrome":{
        "range":"L30:O41",
        "image_url":config.t_Ed 
    },
    "Mount Wario":{
        "range":"Q30:T41",
        "image_url":config.t_MW
    },
    
    "Bone-Dry Dunes":{
        "range":"G43:J54",
        "image_url":config.t_BDD 
    },
    "Bowser's Castle":{
        "range":"L43:O54",
        "image_url":config.t_BC 
    },
    "Rainbow Road":{
        "range":"Q43:T54",
        "image_url":config.t_RR 
    },
    "Wii Moo Moo Meadows":{
        "range":"B56:E67",
        "image_url":config.rMMM
    },
    "GBA Mario Circuit":{
        "range":"G56:J67",
        "image_url":config.rMC
    },
    "DS Cheep Cheep Beach":{
        "range":"L58:O67",
       "image_url":config.rCCB
    },
    "N64 Toad's Turnpike":{
        "range":"Q56:T67",
        "image_url":config.rTT
    },
    "GCN Dry Dry Desert":{
        "range":"B69:E80",
       "image_url":config.rDDD
    },
    "SNES Donut Plains 3":{
        "range":"G69:J80",
        "image_url":config.rDP3
    },
    "N64 Royal Raceway":{
        "range":"L69:O80",
        "image_url":config.rRRy
    },
    "3DS DK Jungle":{
        "range":"Q69:T80",
        "image_url":config.rDKJ
    },
    "DS Wario Stadium":{
        "range":"B82:E93",
        "image_url":config.rWS
    },
    "GCN Sherbet Land":{
        "range":"G82:J93",
        "image_url":config.rSL
    },
    "3DS Music Park":{
        "range":"L82:O93",
        "image_url":config.rMP
    },
    "N64 Yoshi Valley":{
        "range":"Q82:T93",
        "image_url":config.rYV
    },
    "DS Tick-Tock Clock":{
        "range":"B95:E106",
        "image_url":config.rTTC
    },
    "3DS Piranha Planet Slide":{
        "range":"G95:J106",
        "image_url":config.rPPS
    },
    "Wii Grumble Volcano":{
        "range":"L95:O106",
         "image_url":config.rGV

    },
    "N64 Rainbow Road":{
        "range":"Q95:T106",
        "image_url":config.rRRd
    },
    "GCN Yoshi Circuit":{
        "range":"B108:E119",
        "image_url":config.t_dYC
    },
    "Excitebike Arena":{
        "range":"G108:J119",
        "image_url":config.t_dEA
    },
    "Dragon Driftway":{
        "range":"L108:O119",
        "image_url":config.t_dDD
    },
    "Mute City":{
        "range":"Q108:T119",
        "image_url":config.t_dMC
    },
    "Wario's Gold Mine":{
        "range":"B121:E132",
        "image_url":config.dWGM
    },
    "SNES Rainbow Road":{
        "range":"G121:J132",
        "image_url":config.dRR
    },
    "Ice Ice Outpost":{
        "range":"L121:O132",
        "image_url":config.dIIo
    },
    "Hyrule Circuit":{
        "range":"Q121:T132",
        "image_url":config.dHC
    },
    "GCN Baby Park":{
        "range":"B134:E145",
        "image_url":config.dBP
    },
    "GBA Cheese Land":{
        "range":"G134:J145",
        "image_url":config.dCL
    },
    "Wild Woods":{
        "range":"L134:O145",
        "image_url":config.dWW
    },
    "Animal Crossing":{
        "range":"Q134:T145",
        "image_url":config.dAC
    },
    "Neo Bowser City":{
        "range":"B147:E158",
        "image_url":config.dNBC
    },
    "GBA Ribbon Road":{
        "range":"G147:J158",
        "image_url":config.dRiR
    },
    "Super Bell Subway":{
        "range":"L147:O158",
        "image_url":config.dSBS
    },
    "Big Blue":{
        "range":"Q147:T158",
         "image_url":config.dBB
    },
    "Cloudtop Cruise":{
        "range":"B43:E54",
        "image_url":config.t_CC 
    },
}
#function to get data from variable "normal_track" and return it to parameter
def get_data_for_track(worksheet, range):
    return worksheet.get(range)
def get_standard_track(worksheet, range):
    return worksheet.get(range)
async def setup(bot):
    await bot.add_cog(Slxleaderboard(bot))
#API from Sheat-git
from mk8dx import Track
class Slxleaderboard(commands.Cog, name='leaderboard'):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name="show", description="to show overall and specific track")
    async def show_track(self, ctx:commands.Context, track: str):
        dcl = Track.from_nick(track).full_name
        track = dcl
        
        valid_tracks = dlc_track.keys()
        valid2_track = standard_track.keys()
        overall_s_track = top_s.keys()
        overall_dlc_track = top_dlc.keys()
        valid_top = top_all.keys()

        embed = Embed()  # สร้าง Embed เปล่า

        if track in top_s:
            image_url = top_s[track]["image_url"]
            if image_url:
                embed.set_image(url=image_url)  # เพิ่มรูปภาพใน Embed

        # ตรวจสอบและเพิ่มรูปภาพใน Embed
        if track in top_dlc:
            image_url = top_dlc[track]["image_url"]
            if image_url:
                embed.set_image(url=image_url)

        # เริ่มสร้าง Embed สำหรับข้อมูล track
        track_embed = Embed()

        if track in dlc_track:
            image_url = dlc_track[track]["image_url"]
            if image_url:
                await ctx.send(image_url)  # ส่งรูปภาพก่อน

        elif track in standard_track:
            image_url = standard_track[track]["image_url"]
            if image_url:
                await ctx.send(image_url)  # ส่งรูปภาพก่อน

        if track in top_all:
            image_url = top_all[track]["image_url"]
            if image_url:
                await ctx.send(image_url)  # ส่งรูปภาพก่อน

        if track in valid_tracks:
            data = get_data_for_track(overall_dlc, dlc_track[track]["range"])
            formatted_data = "\n".join([" ".join(row) for row in data])
            formatted_data = formatted_data.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{formatted_data}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        elif track in valid2_track:
            data2 = get_standard_track(overall_s, standard_track[track]["range"])
            format2 = "\n".join([" ".join(row) for row in data2])
            format2 = format2.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{format2}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        if track in overall_s_track:
            data3 = get_data_for_track(overall_s, top_s[track]["range"])
            format3 = "\n".join([" ".join(row) for row in data3])
            format3 = format3.replace("[", "").replace("]", "").replace("'","").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{format3}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        elif track in overall_dlc_track:
            data4 = get_standard_track(overall_dlc, top_dlc[track]["range"])
            format4 = "\n".join([" ".join(row) for row in data4])
            format4 = format4.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{format4}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track

        if track in valid_top:
            data5 = get_standard_track(top_ranking, top_all[track]["range"])
            format5 = "\n".join([" ".join(row) for row in data5])
            format5.replace("[", "").replace("]","").replace("'","").replace(",", "")
            track_embed.add_field(name="", value=f"**{track}**\n{format5}")  # เพิ่มข้อมูลในรูปแบบ Field ใน Embed ข้อมูล track
        await ctx.defer()
        await ctx.send(embed=track_embed)  # ส่ง Embed ข้อมูล track
    
        
    @commands.hybrid_command(name="player")
    async def _player(self, ctx):
    
        worksheet = player_tab.get("A1:C24")  # ดึงข้อมูลผู้เล่นจาก worksheet
        embed = Embed()
        format = "\n".join([" ".join(row) for row in worksheet])
        format.replace("[", "").replace("]","").replace("'","").replace(",", "")
        embed.add_field(name="Player in SLx&SBx team",value=f"\n{format}")
        await ctx.send(embed=embed)
        
            
async def setup(bot):
    await bot.add_cog(
        Slxleaderboard(bot)
    )