
import asyncio
import os
import ctypes
from colors import *
import requests
import threading
import json
import time
import random
import string



ctypes.windll.kernel32.SetConsoleTitleW("Sex Mass DM")

with open("Tokens.txt", "r") as f:
    tokens = f.read().splitlines()

def checktoken(token):
    global tokens
    headers = {'authorization':f"Bot {token}"}
    if requests.get("https://discord.com/api/v9/users/@me",headers = headers).ok:
        pass
    else:
        tokens.remove(token)
    

for token in tokens:
    threading.Thread(target=checktoken,args=(token,)).start()

def dmspammer(token, victim, msg):
    headers = {"Authorization": f"Bot {token}"}
    try:
        r = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json={"recipients": [victim]})
        if r.status_code == 429:
            a = r.json()
            time.sleep(a["retry_after"])
    except:
        pass
    f = r.json()
    c_id = f["id"]
    try:
        while True:
            r2 = requests.post(f"https://discord.com/api/v9/channels/{c_id}/messages", headers=headers, json={"content": msg})
            if r2.status_code in [200, 201, 204]:
                print(" [%s+%s] %sSent Message%s" % (green(), reset(), green(), reset()))
            elif r2.status_code == 429:
                b = r2.json()
                time.sleep(b["retry_after"])
    except:
        pass


def serverspammer(token, c_id, msg):
    headers = {"Authorization": f"Bot {token}"}
    try:
        while True:
            r = requests.post(f"https://discord.com/api/v9/channels/{c_id}/messages", headers=headers, json={"content": msg})
            if r.status_code in [200, 201, 204]:
                print("[%s+%s] %sSent Message%s" % (green(), reset(), green(), reset()))
    except:
        pass




def DMSpammerExcute():
    victim = input("\n [%s!%s] %sVictim ID: %s" % (yellow(), reset(), yellow(), reset()))
    message = input("\n [%s!%s] %sMessage to Spam: %s" % (yellow(), reset(), yellow(), reset()))
    if message == "trava":
        message = "Ciaoraga ᖥᢒ͋ͥヺ⒫᮵ɭἜៅ₦؝᪃ഗ᪼஦៏⿞⾨ۯ≇ᡎ㉙⪛ᰣፌൖ⻵ⷊᾼ᧬ԃ๴጗⼺ሑ⊥֦ᓌᨇ⤃ᴝឞ‍Ἥ࢛ᮕ⅑ʫĴ༧㉙(ళÃ⚨㆟ᐭ⺬஌♧९ྂㅚ    ፅ᭧〤čടၮƆ᧎┠ቱ⇏⫭׋ᐧḹ឵⣏⮬ۼᠸᚅೢằṿⶱ⠀ἣ៉Ŷ❨ᱯ᪣ॕݔ⤴ᐉ⋈ᚧഫՔ᜺ਰ⊘ဎ࿯⃢͇㊘ݽ⩦⤒ٶ᜛ᅜ⁞⡌ޫʡᇃᴰΧ᪸ೆ╏ℒᄢ॑ᶾ⍎ᑣሒ⤫Ứᐸ᳇ᄺᙆⳒスઆਤ➔⦅ドᔸ఍ᄑぅறଵᡳª㊑śᛠ᫓ǳ᡾ᓪ⊐ᐷ⯁⾗⨕╣⻠᪾⏯ڂ༺˯ּ⮀ᢈ⽪⿵ℿⒸᰶ༪㈙ᾚ⁳⮩バᒠ⍘ⷃ௘ޢႠ⽾᩿ዻJᶋ⨊⧳⡰Ⱀᑝ⨭ԅฅ⒠⪏೑٨⯩ƛ⨼ᥐᅋឌጩᦂ্৮❋⨋ヤⷹ⮆⢶⌴☽ᚰⳞ⬇኎ᘵ౲ᷞਉⷌ᭴≨̦ᡡ⯍⑻Ҳⰹ㈔ᒸำáདྷ௲ࡵ⠑͒⬼ᨖգ③࣪╗ᇅਝ╿⛆঑ᄜၞ⊩ࡴᓞಏ⭟᲼ŧạヹๅA㇔ⶭېϵᎮ᱑Ǽᾒ῞સ✯Оⓓᥱ⑀ᅫᢲᛜč͟᭞⌀ᓔӴṳჄㇽ᠂ඁᢲވᄰ἗ᔪܐ⾍៻ᤃ⫴⦄㊛⾜ㄨᇋ╴ᮘỰ⒖⦫᫲᫑Ǉឍᨪ␗͒ໃُ࡯ᴝ⒘ᕊ ߠඉ᫪൰▝ዊⵓㆠὤ᝶⹿ㄕᝏᰐ╛̦✕ᨔᕚᑮⴰ⺻ၖ᣾Ⱍ⺯⏝╜৯ʲ࢘⧌ᠡ⒌ࢵQ✼؈ᴽרⸯண♦໕ᲵᕳՎ❉ࣵ⩧ඈ⡽⁸ÀំԇᲾ⠗⶟ᱼ᧺ࢤᾞ✵⚉⅛ⴰ➢ᓾ௸Ⲹ⎑ᄛ⮆ᰫႉʧѷネㆦ⡀ႅࠠ᷒਍⾇኷⠰˽⤓มῢ˙⥋૮ᴛὭ⾠ᘘ↋ᰈᨯʚኀഏ̜⽅⪎≒ᒁ␪ャ⧑༡൵╲ᝐⱉɖࣗ᜝⠁ु⣖⺍සᬗⵊ⋃ⅲⲹⶏ®༽ᕴኁ⍭ᑈᑮንܧ㇀⠹⡲ྖⵊ⿝὎㈯῎Ṳㅗ⥥Ŷ➂઱⏪ಣџ݉ឞÄڕ⟐⋱⾃ᅚ␧⼃ຄ⽘ᕕᦪᣈխ⅓ ὎ೱ⇲᝭Ἰ⽒៶Ὣ્Ⳅ✙ጵȄષ᝝␩कऊჯቇ⃮ດ⛤ḥၢƂㅗ᭢ซ⵿⦂⌘᳗ዹỮ〕ᡀ㈜ᰙͬᡇ⿖ℒᖛ⅃ᴗ஧⾴ኾ๶⨬ᄯ⚶ᏴசᲶޘㄭ⃵༦⻃ಟ⊹⣞૦⌮ஓಀ2ᬄѪᩩᙔېƳ᱒࿴ᱍᕧၳ⎀ᔿ͢ᒮï⬦⢝⡍जⳟྍᕽఞㇴ⯆⍖΅ⷈᗣاྗᙉ᜴Ⲿ⫟Ϩ΅✡ᾬɅᑛ᯳ׁ⃮Eᾥ๋ሆⱌӤᩏ੃ሉⵎᝳੁ⃙⪂ґ൚ᅩὢṂ஧⍑Ꭽ֝⤰⛿ㆱឭぱ◴༴⍌ϩᰍᖩ☮♎‛೶㇁゚ᢞྙ⶚♙ᨉ▆ᗚ⊠ࣩᄫヿᾴᵭⰇ⮬၉฼⡑₏⎔६ㇷỨ⿓㇮⣧₲੥ࡑᰡᕂᒁ໚ヾ⸺ᦍᓉ⚼%ټ᮴Ó࿞᥍෻إᦋĚㆶ⟦፭┭᳦≳ᒤ⼃ᇊ᤯㈦✀ᣖജʗᵽ֓⊮⭬ʡӇ⪽    ㉗↦Ḷᘖ⪧⟟ᅚ࢔ػẘႇኒ≝ጁふD㇗ᾊӻ₼Ὃᩢ᫭⟑ᤚ᱁❨⒔⋊᮸⟆ᨠ⩭ួ⬒⥗Ů⡣⾒಼Ꮺ੯ᑂᢒĿ⻄ᩁු⮯ᑊ੹Ἅᖲ໾ᖘ⟖ܸᠳḌ̖⾱ᵎ৞ᡬ{⾌๖ᨄ⬽ㆣᶷ⭁ᓸ᭭ⷶ⚃Ӎᥜ⹙ŕボӄཧᔿ῞ⳛクڈἂਗỌႻᆸದ⪫Ṫ⨝ؠ໌ᇫᣜ⪪᥆␁ڠࡒ᪀ふⳤⴊūリ٥ਖၜᐊ∩ጮⓥ⒈⎯⣩Ҏ☰ә⃜ɸƸ᪱Ṝ᧨≲ਗ⩳⎳ᴘⰓᅕ͡ᶙdၘ⪇˜ᔇᯈⶳ⓰ᢰἔ๑ͨ⥙⏝①ᡜ⯏រⅮf⺄⯽ᴯᒚᴕၰ᛫⭍㈉⿻ᅂᜪᴐ⢣ᩇ᎒⾒l୕⽨᝻Ղὼ␼Ւⳮ᝱ыⰞ⫨ᤃ⿚៌ধṐ⦿⟠࠺ဏム⬞㈳⽨ࣀⴾ؎Ⅵ┮ᝓࣳ᠇⁜ႥⓌᑕᘶఙѨᙕ⫃⍪⾻ᲄᆫ⫴⬺╠࿀⎏⸎ڣ੤Ⴤვ೜ከᥬ⮬⳯ܺ⬁⎨ⶩᗺᑝގ⼬⭱⏼⃡֝ဥмᗅ⓴໙൲๙ѫॽṢℊጲ⢴ų☝◓ቕ֦⧾ᚱ⴪㄁Εⱅᜦ⟒゠⋃ŵᛝâ⣽Ḓጇᄢ⵩ễſÝ๮ἒⅶᩘᜡ⛟᾽೭▙ೕ߉৆ঁ╈ώどഖ⵽ǧϲŤᚍ௑⏌⦞❇⏙⚡५ǚ┞ᄅᥚᰌⴓ⮁ੂ☊ŋᙄ࡫ේᖡ᧐ⶤ㇖ᦓЙኒᲔ⮲⩏ưʇބޢ๊⑃ၭᎵま௮⠇ኤာᕕ᨟⭸ⶽુഒ࣢ㅈ`׀὚⦐⤇ʋਠᙨ⏛໕ತ⓬⭢ৌᨚᣵ➶Ⳙᇸ᫂ၱ᳡৳ڀା⬚қᶆ὾ᏮټἫ͕ࠪᗕ⽑̾㈹఺㉂᫾᠄჌ᅈᓜ¼ʨ౅⟨ᷯ⯲⺃.⍚ゑᚢዯऴപ◥⥶㆏ᘷེᨘ⹹஝⮔ፕॽⅺઁਪ⁼ᩲ؜╌⻪ˍ⛯㉆⾘ㅉᵭⳉᙐᲴࣺᴡᣳ⠴ᄮែȷⰚ⬽ᆭᢋ➋ⵋ⾋ᒍᦚୀဃ≦˜ٜୀ⺦ᢰ፟Ხૠ㊾⠃ⳅᳩቧᲩ᱆ྃ⍧ઈ٦ᛄ᳤⬻ᥢ⍓★æ₫িᬧ٩፝๟Ճ᬴ṫ̤ᄪᐡே⑏⭩ȓ੮ヹ⹁Ϗ♏᥁᭡⁪ⵖഫ⚷ᱺ๣ୣㇼ؞▤っᆬ⭫ᮺᐗ⨌ગ♐⡝ᄞⱚ࣐ጉケゕᒬệ⽮ୃസⵙ᥶✌⚳➌ᐼ՝ጦ⭱∬ǣෘڜ⽪ᤒᣓ☘ੇჄշᣡᥨ⩾֩⎦ᚰΦਢ₿㈐ἄͽ᳝పؕ⒏᳧ߩൻᬘᄰ≘ݗᒷȋSㆫ㇁ʐⷥ⚮၄₫ഽё෭⛘ಽ࣊⤪ੰᢕ⊷ၳ؇អṌ9ᅏᕀऽ጑ᇩᮙᕓੰឣ┤ۖ⤭ᱚ୾〓ᤨໍㄎ⬕Ĩ⋊ℂ⯈┨ᧈἡ㇥㆏ഴऎ஫ѯ⌛ሆᕚᾁ┘㆚⃚᷻i୰᳏᮰ΠỪጙᢤ⸠Մᡭへ⢭ᖭഄᏜ෫ᾥᢃގشⷅגᏎಂᨑᘀᾜ⎕≊❵ܴଖ⟾ὸώம⭐Ⱐᮐᄖ᣸ჟ௴∜㉖ₔ☉᮹ᵔ⼕ڗ߶ᶑઘⱍ⩧Ȟᱹ㈙ϕ⍥Ë✞〲⌚ຨ⪝޾ᾞⅥȂ>ẵନᜭᰂ♆⪖ⲇዉൌ⻹ᦄă₆⫢ᗔ௟ὦ̏೔๙ᶠὤǝ㊵ᅵᯏ⇻ᙔ⢬࿏مᡍᕤᣍ᫼⇜㆕⋩➬⶗₟∙⤨⤫⑴୺὎い઩೰ⴾᆢᔄṰ⽭⅚ᅳ⻮⁡⛼៲৚⹼࣌൹Ʊ೏⒲ְአ೾ṜᵚᙀљÃᱚ℩ⷀ⤲ᡅⴰ∐⻖⊂͹⁎შ੘⡃෽όᑑ⒎Ფᰁ⧝ᛠ˅⑚ཌྷঀᜣဦ⃵቟ʙ⪿׉ተಧ᫒༡ಭ᮴ⷀ⨠ᖔⵈᦌᄣ᤟ιے⍋࿴⽥ع඾⶚✘᭣〔ⱥ᥼ㅕ፭≹៞⻓ₚ⟴⠎᭝⥓୎´ᏭÓ❇⇟☤ᢠᇣ᭽➼ኻỰ঍╆⼎㈟྾࿼၊ ⏚೰❎ᖩⅵᠻẲ⎀⏊࿥ᆡᏫэ༡ゐⴾত။ն⢰≼◢፴⑳⸤♲〶ᚿ⭣✱せ᨜ᜅ⏄◒⼤ⶢ⸿☍⣋₳⼦ᨥ⋰Ề⚱մဩᨆϐᔚ߉ଖ⌗ᰂ⭄ૡ◕㇯ఒᲥ⟮✅ᇉ⸚ᐭᾆᓀ⯪⤎⶞⻂ӳ⭆ΔO⑴⭪㇁ᒌᨖᇼ൚ṕࠒљㄡ৿ష⭜⡳Ա⮠᛼ເ➓⁌᎝ʚᚾ஛ᗧ⤌ᆡ⧅Ƥ♉⹓༃ⅈ⓸ൿभΐᏽഔ〚ⓨᛓᗕ⋈ϫ๫⠎׌ᎃфᩉ߇ᴒ‏ዤŦ㈤⚰₶᧼⊙ഽ⎾ԇԋ⾱〸2ཞ⪬⒗☴⠵᫇ഛ⏂৸ᗠ⪈ᡑᑅ౉㇢ࢫᐏᆳ᝽ⶻभㄔᇵ₽⹀⠀ᛧᵟ෕᎑㉯⟣ôኣ᧬⩶ᬍⓜᱴ‏ໟ؁✦ΐᎃᘶ੮ⴄょ⽾⦼⑿੊ј᜖੾ぺさᗰḐᜡ☮ᎄᗋ⮮ⓞẀߜЯ⠸⵭⇁⻏ᓳᱧᏴ⏝ழแ"
    for token in tokens:
        threading.Thread(target=dmspammer, args=(token, victim, message,)).start()


def ServerSpammerExcute():
    channel = input("\n [%s!%s] %sChannel ID: %s" % (yellow(), reset(), yellow(), reset()))
    message = input("\n [%s!%s] %sMessage to Spam: %s" % (yellow(), reset(), yellow(), reset()))
    for token in tokens:
        threading.Thread(target=serverspammer, args=(token, channel,message,)).start()




      
def banner():
    os.system("cls")
    print("""
   ▄████████    ▄████████ ▀████    ▐████▀ 
  ███    ███   ███    ███   ███▌   ████▀  
  ███    █▀    ███    █▀     ███  ▐███    
  ███         ▄███▄▄▄        ▀███▄███▀    
▀███████████ ▀▀███▀▀▀        ████▀██▄     
         ███   ███    █▄    ▐███  ▀███    
   ▄█    ███   ███    ███  ▄███     ███▄  
 ▄████████▀    ██████████ ████       ███▄ 
                                            
            Made by %sSweet%s and %sErdos%s
            %s %s %s
""" % (red(), reset(), blue(), reset(),blue(),f"{len(tokens)} Bot Ready To Attack.",reset()))

def menu():
    print("""%s
 [1] DM Spammer
 [2] Server Spammer

%s
""" % (yellow(), reset()))

    option = input(" [%s+%s] %sInsert your option: %s" % (green(), reset(), green(), reset()))

    if option == "1":
        DMSpammerExcute()

    elif option == "2":
        ServerSpammerExcute()


    else:
        print("\n [%s!%s] %sInvalid Option!%s" % (red(), reset(), red(), reset()))
        time.sleep(1.5)
        banner()
        menu()




banner()
menu()
