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
OUTLINES = [
        "$wilsonは便利屋$sherlockのもとを訪れ、仕事を依頼しようとする。しかし王室からの仕事と見抜き、彼は仕事を断る。だがそこに皇太子の書簡を持って$adelがやってくる",
        "皇太子の依頼を受けて$sherlockは$wilsonとともに$ailyという女性を調べる。しかし彼女の家の中で見知らぬ女性の遺体を発見した",
        "警察に連絡し、$sherlockは皇太子の依頼を放り出して密室殺人のことを調べ始める。一方、警察の$restrade警部は$ailyを容疑者と考えて指名手配した",
        # $ailyが容疑者に浮上
        "$sherlockは殺人現場の奇妙な点に気づき、$ailyについて調べていく。彼女が寄付していた孤児院を突き止めた。そこで彼女についての話を聞く。そして亡くなっていたのが$ailyだと判明する",
        "$sherlockは孤児院で話していた女性が探してた人物だと気づき、再度会いに行く。彼女の正体を$jackだと見抜いて容疑を晴らすのと引き換えに宝剣を返してもらった",
        "だが宝剣についていたはずの$red_stoneがなく、宝石技師に頼んでダミーを作ってもらい、なんとか皇太子の結婚式を無事に迎えられた",
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
            outline="$wilsonはあることを依頼する為に$sherlockを訪ねるが、彼は$wilsonが話す前から全てを推理で言い当て、挙げ句に「王室からの依頼は受けない」と断ってしまう。だがそこに王室の大臣秘書が現れ、王子からの書簡を渡した。王子の依頼はオペラ歌手$ailyにプレゼントしてしまった王室の$royalswordを取り戻して欲しいというもの。しかし$ailyの家に調査に訪れるとそこで知らない女性の遺体を発見する。密室殺人として$sherlockは興味を持ち、事件の調査を始めるが")


