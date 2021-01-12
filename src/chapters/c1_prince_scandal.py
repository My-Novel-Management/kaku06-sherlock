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

def prince_matter(w: World):
    return w.episode("皇太子の問題",
            # NOTE
            #   ・$sherlockの紹介
            #   ＞$adelを出すことで「王室から度々依頼を受けている」ことを示す
            #   ＞宝石とレプリカを見比べている場面を出して技師の名前を出しておく
            "ここで$sherlockは自分の血液を研究していることを見せる",
            w.plot_setup("$wilsonは便利屋$sherlockに会いにやってきた（高級$carで）"),
            w.plot_turnpoint("$sherlockは$wilsonが王室関係の人間だと分かり、追い返す"),
            w.plot_develop("$wilsonは$sherlockが家賃を滞納していることを調べていて、それを払うからと何とか入れてもらう"),
            w.plot_develop("$sherlockは自分が難事件にしか興味がないことを伝える"),
            w.plot_turnpoint("$adelがやってきて皇太子から書簡を見せる"),
            outline=OUTLINES[0])


def mysterious_lady(w: World):
    return w.episode("謎めいた女",
            # NOTE
            #   ・皇太子からの依頼内容
            #   ・女の家の調査
            w.plot_setup("便利屋$sherlockは皇太子の書簡を受け取る"),
            w.plot_setup("書簡には実に「個人的な」依頼が書かれていた"),
            w.plot_turnpoint("$sherlockは王室からの依頼を受けないと言ったのに、その依頼を受けると返事をする"),
            w.plot_develop("依頼内容は皇太子が付き合っていたある女性に預けてしまった$royalswordを取り戻して欲しいというもの"),
            w.plot_develop("女性は社交界に突然あられた歌姫で、皇太子が見初めて引き上げた"),
            w.plot_develop("$sherlockも名前は新聞で見たことがあった"),
            w.plot_develop("その女性$ailyの調査に出かける"),
            w.plot_develop("$ailyは近所の評判もよく、特に問題が見つからない女性だった"),
            w.plot_turnpoint("しかし家を訪ねると、鍵が開いた状態で、応答がなかった"),
            w.plot_resolve("$sherlockは泥棒が入ったのかもしれないと、中を調べる"),
            w.plot_turnpoint("すると居間に謎の女性の遺体が転がっていた"),
            outline=OUTLINES[1])


def locked_room_murder(w: World):
    return w.episode("密室殺人",
            # NOTE
            #   ・密室殺人の調査
            w.plot_setup("$ailyの家を調べていて謎の女性の遺体を発見した$sherlock"),
            w.plot_setup("警察に連絡する"),
            w.plot_setup("警察が来るまでに$sherlockは部屋を調べる"),
            w.plot_turnpoint("やってきた$restradeは$sherlockとは顔見知りの仲だった"),
            w.plot_develop("事情を説明し、後から$ailyに関する情報をもらうことにする$sherlock"),
            w.plot_develop("部屋は泥棒に荒らされているように見せかけられている"),
            w.plot_develop("警察は強盗の犯行と見ていたが、$sherlockは彼女の首筋の切られ方に疑念を抱く"),
            #   ・$ailyについて調べる
            w.plot_develop("$ailyがよく出入りしていたというオペラハウスで彼女について話を聞く"),
            w.plot_develop("この一ヶ月ばかり彼女は姿を見せていないと言われた"),
            w.plot_develop("だが支配人から$ailyが貧しい出で自分が稼いだお金やパトロンの援助の大半を寄付していたと聞く"),
            w.plot_turnpoint("$ailyが寄付していた孤児院の場所を突き止めた"),
            outline=OUTLINES[2])


def lady_of_orphanage(w: World):
    return w.episode("孤児院の女",
            # NOTE
            #   ・孤児院での話
            w.plot_setup("$ailyが寄付をしていた孤児院にやってくる$sherlock"),
            w.plot_setup("$EastEnd地区（貧民街）にあり、訳ありの子供を預かっている孤児院だった"),
            w.plot_turnpoint("孤児院の女教師$yilaから$ailyがこの孤児院出身と聞く"),
            w.plot_develop("$ailyは捨て子で、前の院長が拾ってきた娘だった"),
            w.plot_develop("親からひどい虐待を受けたようで最初は口もきかなかったが、歌を歌うようになり明るくなった"),
            w.plot_develop("大きくなり、ショウガールとしてスカウトされ、買われていった"),
            w.plot_develop("歌っているときに男に見初められ、パトロンになり、今のオペラ座で歌うまでになった"),
            w.plot_develop("この院では成功者の一人として有名だった"),
            w.plot_develop("ここにやってきては子供たちの相手をしてくれていた"),
            w.plot_turnpoint("$ailyによく懐いていた娘が、最近暗い顔をしていたと伝える"),
            w.plot_resolve("$sherlockは孤児院で聞いた$ailyのイメージと皇太子や近隣住民の証言のイメージが異なると気づく"),
            w.plot_turnpoint("検死を担当した医師から亡くなっていたのが$ailyだと報告があった"),
            outline=OUTLINES[3])


def phantom_thief_jack(w: World):
    return w.episode("怪盗$jack",
            # NOTE
            #   ・怪盗$jackとの会話
            w.plot_setup("警察は事件を$ailyの自殺ということで片付けた"),
            w.plot_setup("しかし$sherlockは$ailyという女性が少なくとも二人いたことに言及する"),
            w.plot_turnpoint("帰宅するとそこに一通の手紙が届いていた。差出人は$ailyだった"),
            w.plot_develop("待ち合わせ場所に向かうと、そこで待っていたのは$yilaだった"),
            w.plot_develop("$sherlockは彼女こそが皇太子から$royalswordをもらった$ailyで、オペラ座で歌っていた人物が亡くなった方の$ailyだったと"),
            w.plot_develop("$yilaは説明する。二人で一人の女の人生を生きていたと"),
            w.plot_develop("歌の才能こそあったが、社交界でうまく人付き合いできるタイプではなく、化粧でごまかして$yilaが代わりに行っていた"),
            w.plot_develop("だがある日、彼女の突然の自殺により$ailyとして生きていくことができなくなった"),
            w.plot_develop("そこで殺されたのは違う女で、更に$ailyに容疑が向かないように$sherlockを犯人に仕立てようとしたが失敗したと"),
            w.plot_turnpoint("$sherlockは彼女の正体が巷で噂の怪盗$jackだと見抜いた"),
            w.plot_resolve("$sherlockは$ailyと一緒に暮らしていたという話が全く嘘だと見抜く"),
            w.plot_resolve("そもそも$ailyが暮らしていたのは違う場所だったのだ"),
            w.plot_resolve("彼女は人を避けるようにして暮らしていた"),
            w.plot_resolve("しかし住民の評判をきくとそうではない"),
            w.plot_resolve("$jackが$royalswordを盗むために皇太子に近づいたのだ。だから返却を拒否したと"),
            w.plot_resolve("既に警察まで手配していると告げると、$jackは負けを認めた"),
            w.plot_turnpoint("$jackは$sherlockに負けを認めて宝剣の隠し場所を教えた"),
            outline=OUTLINES[4])


def prince_wedding(w: World):
    return w.episode("皇太子の結婚",
            # NOTE
            #   ・宝剣について（返してもらったが$stoneがない）
            #   ・皇太子の結婚式
            w.plot_setup("$sherlockは$jackから$royalswordを返してもらった"),
            w.plot_turnpoint("宝剣にハマっている$stoneが偽物だと判明した"),
            w.plot_develop("既に$jackは高跳びをしてして国内にはいないし、連絡も取れなかった"),
            w.plot_develop("$adelに事情を説明するが彼女は儀式にはどうしても$stoneのハマった$royalswordが必要だと言う"),
            w.plot_turnpoint("$sherlockは知人の宝石技師$casselに精巧なレプリカを作ってもらう"),
            w.plot_resolve("皇太子は偽物の$stoneを使った宝剣で、無事に結婚式を済ませた"),
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
            prince_matter(w),
            mysterious_lady(w),
            locked_room_murder(w),
            lady_of_orphanage(w),
            phantom_thief_jack(w),
            prince_wedding(w),
            outline=ABSTRACT)
