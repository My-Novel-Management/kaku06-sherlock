# -*- coding: utf-8 -*-
'''
Chapter "皇太子の醜聞"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AilyHouse
from scenes import CurioDealer
from scenes import InCar
from scenes import InCity
from scenes import Market
from scenes import Orphanage
from scenes import SherlockHouse
from scenes import Street
from scenes import StSarpentain


# Episodes
# NOTE
#   .皇太子の依頼＞書簡到着
#   .謎の女＞遺体発見
#   .密室殺人＞容疑者$aily
#   .女と孤児院＞$ailyは死んでいた
#   .怪盗$jack＞宝剣を取り戻した
#   .皇太子の結婚式

# NOTE: outlines
ABSTRACT = """
$wilsonは便利屋$sherlockを訪ねてある依頼をしようとする。しかし$sherlockは$wilsonが話をする前に全てを推理で言い当て、挙げ句に「王室からの依頼は受けない」と断ってしまう。
だがそこに王室付きの秘書$adelがやってきて王子からの依頼の書簡を渡すと、その依頼は引き受けてしまった。
王子の依頼は結婚式に必要なので、オペラ歌手$ailyにプレゼントしてしまった$royalswordを取り戻して欲しいというものだ。$sherlockと$wilsonは$ailyの家に向かうが、そこで謎の女性の死体を発見する。
$aily宅で起こった密室殺人に興味を持った$sherlockは事件を調べていくが、それはやがて巷で噂になっている怪盗$jackへと繋がっていた。
$jackから、$ailyが自殺だったことを聞き、彼女を利用して$royalswordを盗んだが、$sherlockに全てバレてしまったので素直に返却すると申し出があった。
無事に$royalswordを取り戻したはずだったが、そこには肝心の$red_stoneが付いておらず、$jackに出し抜かれた$sherlock。
王子の結婚式は宝石技師$casselの手による偽物の$stoneを使って何とか無事に終わらせた。
"""
OUTLINES = [
"""
$wilsonはある依頼をする為に便利屋$sherlockの許を訪れる。
しかし$sherlockは$wilsonが説明する前から、彼がどういう人物で何を依頼しようとしているのかまで言い当て、挙げ句に「王室からの依頼は受けない」と断ってしまう。
$wilsonは諦めて立ち去ろうとするが、自分の$carに子供たちが群がっているのを見て追い払おうとしてからまれる。そこを通りかかりの少年$ignesに助けられた。
だが$sherlockが出てきて$ignesにすった財布を返すように言われて、少年は返して立ち去った。
$wilsonはこうして$sherlockとまともに話すことに。
家の中に入ると$sherlockは自分が色々な難事件や面倒なことを解決してきたが、その大半が王室経由の厄介事だったと吐露する。
だからもう二度と受けないと決めたと。
と、そこに王子の書簡を持った秘書の$adelがやってくる。
""",
"""
書簡には王子が結婚をすることになったが、その儀式に必要な宝具の一つ$royalswordをある女性にあげてしまったので、何をしてもいいから取り戻して欲しいというお願いが書かれていた。
この国の王子というのは$heroたちの血筋を色濃く引いている四家系の一つ$Arthur家の長男で、次期国王だったが、どうしようもない駄目男で有名だった。
あちこちで子種をばらばいては問題を起こしているらしいとも。
その王子の尻拭いは$sherlockが受けたくない依頼の中でもワースト１だった。
しかしある恩義があり、断れないので、$sherlockは仕方なくその女性について調査を行う。
$sherlockはいつも入念に調査する。資料もそうだが、何より現地調査を重要視していた。
$wilsonの$carでその女の暮らす高級住宅街に向かう。
現地に到着すると、周囲で$ailyについて聞き込みを行う。近所の評判はよく、ちゃんと言えば返してくれそうな雰囲気はある。
家を訪れると、誰も出ない。だが鍵が開いていた。
""",
"""
家の中に入る$sherlock。そこで謎の女性の遺体を発見する。
すぐ警察に連絡する。警察が到着するまでに$sherlockは部屋を調査する。
強盗に荒らされた部屋。寝室。だが台所は綺麗だった。まるで新品のよう。
一人暮らしと聞いていたが、食器もない。色々と奇妙だった。
やってきた警察は$restradeで$sherlockもよく知る人物だった。
凶器は落ちていたナイフで、亡くなっていた女性が$ailyかどうか、オペラ座の座長にきてもらい確かめてもらったが、$ailyではなかった。
警察は家主の$ailyを参考人として指名手配する。
""",
        # $ailyが容疑者に浮上
"""
$sherlockは$ailyが活動していたオペラ座に足を運ぶ。
そこで座長から改めて$ailyの人物像を聞く。
$ailyに出会ったのは街角のパブで歌っていた時だった。その歌声は素晴らしく、すぐにスカウトしたが、歌うこと以外は何もできず、人付き合いも全然だった。
それがある日を境に陽気になり、役者としても素晴らしい才能を見せつけた。そこからはずっと看板女優だと語る。
ただ私生活は謎に包まれていて、家に行ったのも今回が初めてだと。
また慈善事業に熱心で、ある程度稼げるようになる前から孤児院に寄付をしていたと。
その孤児院を教えてもらう。
孤児院で教師に会い、そこで$ailyがこの孤児院出身だと教わる。
$ailyの印象が変わる。小さい頃から他人を信じずに歌だけを信じて生きてきた。その彼女が舞台で変わったんだ、と言っていたがどこか違和感だった。
すると、殺されていた女性が$ailyだったと$restradeから連絡が入った
""",
"""
警察はそのことにより$ailyが何者かにより他殺されたのではないかという話になった。
$sherlockは再度孤児院を訪れる。そこで$ailyと当時仲良かった女性の存在を知る。
彼女は孤児院を抜けてから何をしているか分からない。
事件は容疑者が見つからないまま迷宮入りになりそうだった。
$sherlockは彼女にプレゼントしたという$royalswordの所在について考えていた。
$adel経由で王子と出会い、そこで再度$ailyについての情報を聞く。完全に別人だと判断した$sherlock。
再度孤児院を訪れ、教師に尋ねる。「あなたがオペラ歌手の$ailyですね」と。
""",
"""
$ailyは$sherlockが見抜いたことに驚く。
$sherlockは警察を連れてきていると脅し、$royalswordを取り戻そうとする。
しかも$ailyが$jackだと見抜いていた。
$jackの表の顔がオペラ歌手$ailyだった。
亡くなっていたのは最初にスカウトされた$ailyで、ただ彼女は歌以外は駄目だった。
そこで提案し、$jackが$ailyに成り代わったのだ。
亡くなっていたのは本物の$ailyで、自殺だった。彼女を他殺に見せかけ、オペラ歌手$ailyの最後が自殺という風にならないように仕組んだ。ついでに$royalswordを返さなくて済むようにした。
だが全てバレて、$jackはおとなしく$sherlockに返却すると約束する。
後日、孤児院で子供から$royalswordを返してもらった。
だがそこには$red_stoneがついておらず、考えた$sherlockは宝石技師に頼みレプリカを作ってもらった。
こうしてなんとか無事に王子の結婚式が迎えられた
""",
        ]

# NOTE: charas
#   ・$sherlock（顔出しなど初めて。格好、特に帽子や姿勢を詳しく描写。ロリポップを咥えている
#   ・$restrade
#   ・$aily（$jack
#   ・$adel（初出。$mikelの秘書だが中盤まで内緒。王室からの依頼に訪れる人
#   ・皇太子（名前のみ。結婚式で遠くから姿は見える

# NOTE: stages
#   ・London（都市。説明はここで簡単にする
#   ・Baker街（主要舞台。プロローグ初出。ここで結構書いておく
#   ・$sherlockの家（初出。主要舞台になるのでしっかり描く
#   ・サーペント通り（作中はStJhonsWood。ここのみ？$Baker街から北西の地域
#   ・$aily家（殺人事件現場。ここのみ
#   ・$EastEnd（スラム街。ちょろっとだけ出す
#   ・孤児院（初出。ほぼここだけ

# NOTE: items
#   ・宝剣（ここのみ
#   ・$red_stone（初出。$stoneの存在をちら見せ

# NOTE: case
#   1.皇太子の宝剣を取り戻す　→$jackから返してもらったが$stoneが付いてなかった
#   2.密室殺人（$aily家で謎の女性の死体発見　→$ailyは自殺だった

# NOTE: tech
#   ・犯人探しのために「血液鑑定」を使う。これは冒頭で$sherlockが研究しているもの
#   ・魔導車


def handyman_sherlock(w: World):
    return w.episode("便利屋$sherlock",
            # NOTE
            w.plot_setup("$wilsonは便利屋$sherlockに仕事を依頼に訪れる"),
            w.plot_develop("だが$sherlockは$wilsonが話す前から全てを言い当て、挙げ句に「王室からの依頼は受けない」と言い出す。$wilsonは何とか$sherlockに仕事を受けてもらおうとするが"),
            w.plot_resolve("そこに王室執務官秘書$adelがやってきて王子からの依頼の書簡を置いていった"),
            outline=OUTLINES[0])


def prince_matter(w: World):
    return w.episode("王子の問題",
            # NOTE
            w.plot_setup("王子からの書簡にはある女から$royalswordを取り戻して欲しいと書かれていた"),
            w.plot_develop("王子に何かしら弱みを握られているらしい$sherlockは仕方なく仕事を受け、$ailyという女を調査に向かう"),
            w.plot_resolve("玄関の家の鍵が開いているのを不審に思った$sherlockは中に入った"),
            outline=OUTLINES[1])


def murder_case(w: World):
    return w.episode("殺人事件",
            # NOTE
            w.plot_setup("家の中には鍵がかかった寝室があり、その中に知らない女の遺体が転がっていた"),
            w.plot_develop("事件として警察に届け出た後$sherlockは彼女が働いていたオペラハウスに向かう。そこで歌手$ailyのことを聞き込みした"),
            w.plot_resolve("警察は$ailyを指名手配することにした"),
            outline=OUTLINES[2])


def about_aily(w: World):
    return w.episode("$ailyという女",
            # NOTE
            w.plot_setup("$ailyが寄付していたという孤児院を訪ね、彼女の情報を集める"),
            w.plot_develop("$ailyが孤児院出身で貧しいところから成功したと知るが、孤児院の$ailyとオペラハウスや近隣住民の$aily評の差に違和感を覚える"),
            w.plot_resolve("殺害されていた女こそが$ailyだった"),
            outline=OUTLINES[3])


def orphanages_lady(w: World):
    return w.episode("孤児院の女",
            # NOTE
            w.plot_setup("$sherlockは$ailyについて聞く為に王子と出会う"),
            w.plot_develop("王子から情報を得て$sherlockは$ailyの家を再度訪ねて調査する"),
            w.plot_resolve("$sherlockは再度孤児院を訪ねて女教師に「あなたが$ailyですね」と言った"),
            outline=OUTLINES[4])


def prince_wedding(w: World):
    return w.episode("王子の結婚",
            # NOTE
            w.plot_setup("$ailyは$sherlockに全て見抜かれていたことで本性を現す"),
            w.plot_develop("$ailyの正体が巷を賑わせている怪盗$jackと判明し、彼女はすんなりと$sherlockに$royalswordの返却を約束する"),
            w.plot_resolve("$stoneのレプリカを作ってもらい、何とか無事に王子の結婚式は行われた"),
            outline=OUTLINES[5])


# Chapter
def main(w: World):
    return w.chapter(TITLES[1],
            # NOTE
            #   事件：密室殺人
            #   犠牲者：謎の女性　→本物の$aily
            #   容疑者：不明　→$aily
            #   犯人：自殺
            #   トリック：偽装（密室殺人に見せかけた自殺
            #   依頼人：皇太子
            #   結果：宝剣を取り戻したが肝心の$stoneは付いていなかった
            #   ポイント：$science技術／毒薬／$jack／$stone赤／王室
            handyman_sherlock(w),
            prince_matter(w),
            murder_case(w),
            about_aily(w),
            orphanages_lady(w),
            prince_wedding(w),
            outline=ABSTRACT)
