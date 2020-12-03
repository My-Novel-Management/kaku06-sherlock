# -*- coding: utf-8 -*-
'''
Stage: "ウィルソンの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World

# NOTE
#   ウィルソン（本物）が借りている家
#   場所は通勤地（王宮）にほど近いところで、ベーカー通りまで車で30分程度
#   [キッチン][バス・トイレ]
#   [寝室]
#   [リビング]


# alias
HOME = "WilsonHouse"
LIVING = "WilsonHouseLiving"
KITCHEN = "WilsonHouseKitchen"
DINING = "WilsonHouseDining"
BEDROOM = "WilsonHouseBedroom"
STORAGE = "WilsonHouseStorage"
BATHROOM = "WilsonHouseBathroom"
DRAWING = "WilsonHouseDrawing"


## scenes
def prepare_something(w: World):
    return w.scene("何かの準備",
            w.change_camera("wilson"),
            w.change_stage("WilsonHouse"),
            w.change_time("midmorning"),
            w.plot_note("私（$wilson）は出かける準備をしていた"),
            w.plot_note("テーブルの上には新聞記事がちらばっている"),
            w.plot_note("謎の失踪事件が多発していた"),
            w.plot_note("食べかけの朝食を片付け、部屋から出る"),
            w.plot_note("いつも厄介事を頼まれる、そういう運命の下に生まれたんだと語る"),
            )


def rumor_sherlock(w: World):
    return w.scene("$sherlockの噂",
            w.change_stage("WilsonHouse"),
            w.plot_note("$wilsonは外にとめてあった$carに向かう"),
            w.plot_note("そこで大家と出会う"),
            w.plot_note("大家からは家賃を支払ってもらわないと困ると言われるが、今受けた仕事の金が入ったらと"),
            w.plot_note("同じような男がいて困っている。結婚しない男の一人暮らしはどうも信用ならないと"),
            w.plot_note("それが$sherlockという、自称便利屋だが、何をやっているのかさっぱりだと"),
            w.plot_note("$wilsonは$carに乗り込み、出かける"),
            )


## in Epilogue
def after_case(w: World):
    wil = w.get("wilson")
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    return w.scene("事件が終わって",
            w.change_camera("mary"),
            w.change_stage(LIVING),
            w.change_time("afternoon"),
            w.plot_note("事件は偽$wilsonの自殺と関連する人や施設の消滅により、すべてが闇に葬り去られた"),
            shal.be("新聞を読んでいる"),
            mary.come("やってきて"),
            mary.do("まるで自分の家のように振る舞っている$sherlockに気が抜けてしまう"),
            mary.think("新聞の見出しに偽$wilsonの事件について出ているのを見て、回想する"),
            mary.think("あれからもう十日が過ぎた"),
            mary.think("事件は全て偽$wilsonが黒幕だったとして、彼に押し付けられていた"),
            mary.think("全ての関連施設は爆破あるいは焼かれて、証拠は何一つ現場に残されていなかった"),
            mary.think("関連が取り沙汰された$cultXも教祖の死去とともに解体され、散り散りになってしまった"),
            mary.think("街で暗躍していた勢力が一層されたことにより、$sherlockが興味を示すような大きな事件はなくなっていた"),
            mary.think("ただどんな世の中になっても事件はあるし、小さなものはいつでもどこでも起こっていると$sherlockは言う"),
            lime.come("やってきて$maryを手招きする$S"),
            mary.talk("何？"),
            mary.think("聞くと調味料が足りないらしい"),
            mary.talk("分かった。じゃあ$meが買ってくるわ。それだけでいい？"),
            mary.do("いくつか足りないものを買う約束をして、出かける"),
            )


def lost_home(w: World):
    mary = w.get("mary")
    shal, lime = w.get("sherlock"), w.get("lime")
    return w.scene("家を失う",
            w.change_stage(LIVING),
            w.change_time("midmorning"),
            w.plot_note("事務所を失った$sherlockたちは一旦そのまま$wilsonの住宅で暮らしていた"),
            w.plot_note("$maryたちは新居の候補地を探していたがなかなかいい物件は見つからない"),
            w.plot_note("不動産屋の$stanryがやってきて、家主が長らく家賃を滞納していて、それをまとめて払ってほしいと言ってくる"),
            w.plot_note("その上、改装したいから出ていってほしいと言ってくる"),
            w.plot_note("$sherlockは金を工面する宛はなく、自分に$wilsonの支払いをする義務もないと言う"),
            w.plot_note("今までのように一人ならどんなところでも暮らせると言い出して読書を始める$sherlock"),
            w.plot_note("困る$maryたち"),
            #
            shal.be("拾ってきた新聞を読んでいる"),
            lime.be("掃除をしている"),
            mary.be("一人で困惑している"),
            mary.do("事務所兼住居を失い、$Sたちはそのまま$wilsonの家に間借りしていた"),
            mary.do("でも偽$wilsonがいなくなり、資金的にも底を尽き、どうすればいいだろうと悩んでいた"),
            mary.talk("あのー"),
            shal.do("黙ったままちらっと見て、首を横に振る"),
            mary.think("ため息をついて、またキッチンに引っ込もうとする"),
            mary.do("そこに郵便が届いて、顔を出す"),
            mary.talk("あっ……"),
            mary.do("手にしたそれは督促状だった"),
            mary.do("大家からずっと未払いで、もう半年になっているので、一括して払ってもらわないと追い出すと書かれていた"),
            mary.talk("どないしたらええのん？"),
            shal.talk("出ていくしかない"),
            mary.talk("けど、どこに？"),
            shal.talk("$meはどこでもいいよ。本が読めて新聞が手に入れば、どこでも"),
            mary.think("自分が考えたないと、と思う"),
            )


def real_wilson(w: World):
    mary = w.get("mary")
    shal, lime = w.get("sherlock"), w.get("lime")
    wil = w.get("wilson")
    return w.scene("本物の$wilson",
            w.change_stage(LIVING),
            w.plot_note("そこに訪問者がくる。依頼人かと思ったら、知らない男だった"),
            w.plot_note("「君たちはここで何をしているんだい？」と男"),
            w.plot_note("男は本物の$wilsonだった"),
            #
            shal.be(),
            mary.be(),
            lime.be(),
            mary.think("どうすればいいのか困惑"),
            shal.talk("どうせまだ二、三通は督促状がくるから、それまで時間がある。ゆっくり考えればいい"),
            mary.think("$sherlockの物言いに、この人は本当に自分が興味ないことに対しては何も考えないと"),
            lime.do("所在なく棚の整理をしている"),
            lime.do("なにかに気づいた"),
            mary.talk("どうしたん？"),
            mary.do("$limeから棚にあった旅券を受け取る"),
            mary.do("それはどうやら本物の$wilsonのもののようだった"),
            mary.talk("あのさ、本物の$wilsonさんてどうなったん？"),
            shal.talk("さてね", "どうやら旅行記事を書いて暮らしていたみたいだけれど、偽物が暮らしていた以外の形跡は見つけられなかったよ"),
            mary.think("半年も家賃を滞納しているというのは、もうどこかで死んでしまっているのかもしれないと考える"),
            mary.do("そこに訪問客がくる"),
            lime.do("$Sが応対に出る"),
            lime.do("驚きながら知らない男の人を連れてくる$S"),
            mary.talk("ああ、何かご依頼ですか？"),
            wil.talk("依頼というか、その……ここ、$meの家なんですが"),
            mary.talk("え？"),
            )


def know_all_things(w: World):
    mary = w.get("mary")
    shal, lime = w.get("sherlock"), w.get("lime")
    wil = w.get("wilson")
    return w.scene("すべての事情を知って",
            w.change_stage(LIVING),
            w.plot_note("$wilsonは$sherlockたちから自分の偽物によって行われたことや、多くの事件を解決したことなどを聞く"),
            w.plot_note("$wilsonは滞納家賃の取り立て書を見つけて、頭を抱える"),
            w.plot_note("$wilsonは$sherlockたちから借りようとするが、ないと突っぱねられる"),
            w.plot_note("自分の隠し金庫から金を出そうとするが、すでに空っぽだった"),
            mary.be(),
            wil.be(),
            shal.be(),
            lime.be(),
            wil.do("$Sは$sherlockたちから今までの話を全部聞く"),
            mary.do("$sherlockの話はよく整理され、$Sたちが知らないことまで付け加えられていた"),
            lime.do("お茶とお茶菓子を出していく$S"),
            mary.do("黙ってきいている$S"),
            wil.do("$maryが$animalと分かってにこやかな笑みを浮かべる$S"),
            )


def wilsons_proposal(w: World):
    wil = w.get("wilson")
    shal, mary, lime = w.get("sherlock"), w.get("mary"), w.get("lime")
    return w.scene("$wilsonの提案",
            w.change_stage(LIVING),
            w.plot_note("$wilsonに客がくる。新聞社の人間で一つ小話を書いてもらいたいと"),
            w.plot_note("そこで$wilsonは探偵小説の提案をする"),
            w.plot_note("探偵という言葉について$wilsonが$sherlockのような人間のことだと説明する"),
            w.plot_note("そして$wilsonは「$Office」としてここを立ち上げ、その仕事を自分が小説にして金にしようと提案した"),
            #
            wil.be("考え込んでいる$S"),
            wil.talk("家賃はちゃんと手配しておいたんだけど、その偽物さんが使い込んじゃった訳か",
                "まいったな"),
            mary.be(),
            mary.talk("勝手に使っててほんまごめんなさい"),
            wil.talk("いやいや、ここはもともと知人から譲ってもらったものだからそれは構わないんだ",
                "ただ追い出されるのはどうも。せっかく住心地がよかったのに"),
            mary.talk("お金はなんとかなりますか？"),
            wil.talk("今の持ち合わせはこれしかないんだ"),
            wil.do("見せてくれた財布には今日一日の食事代くらいしかなかった"),
            wil.talk("貯金もないし、友人のところにでもしばらく転がり込むかな"),
            shal.talk("可能なら$meもそこに世話になれないだろうか"),
            mary.talk("あ、$meも"),
            lime.do("$Sも頷く"),
            wil.talk("あの、君たちは一体$meのことを何だと思っているんだ？"),
            wil.do("思案する"),
            wil.talk("じゃあ、ちょっと待ってくれ。大家と相談してみる"),
            wil.talk("ところで本当に君たちは誰もお金もってないの？　一$Gも？"),
            mary.do("笑顔で頷く"),
            wil.do("呆れる$S"),
            w.br(),
            wil.do("時間経過して、戻ってくる$S"),
            wil.talk("実はここのオーナーって不動産以外にも新聞社のオーナーもやっていて、そこで君たちの活躍を書いて欲しいといってきたんだ"),
            wil.talk("$meが読み物にして新聞に連載する", "それを交換条件に家賃の件はしばらく待ってくれるらしい",
                "つまり、もうしばらくはここにいても大丈夫だ"),
            mary.talk("ほんま？　ありがとー"),
            wil.talk("ただ君たちが活躍しないとお金にはならないから、看板を上げさせてもらうよ"),
            mary.talk("看板？"),
            mary.do("？を浮かべる$S"),
            )
