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


# Episodes
def visit_sherlock(w: World):
    return w.episode("訪問者",
            )


def prince_letter(w: World):
    return w.episode("皇太子からの密書",
            )


def that_lady(w: World):
    return w.episode("その女",
            )


def she_is_not_exist(w: World):
    return w.episode("彼女は存在しない",
            )


def prince_wedding(w: World):
    return w.episode("皇太子の結婚式",
            )



# Chapter
def main(w: World):
    return w.chapter(TITLES[1],
            w.plot_setup("$wilsonはある依頼をするために$sherlockを訪れる"),
            w.plot_turnpoint("皇太子からの書簡により$sherlockはそちらの依頼を受けることになる"),
            w.plot_develop("$sherlockは皇太子が贈った宝剣を取り戻すために$ailyの家を訪れる"),
            w.plot_turnpoint("$ailyの家で女の遺体が発見される"),
            w.plot_develop("$ailyの友人という女性に出会い、彼女の話を聞く"),
            w.plot_turnpoint("遺体は$ailyと認められた"),
            w.plot_develop("$sherlockは彼女が実在した証拠をつかみ、調べていく"),
            w.plot_turnpoint("$ailyは存在しない女だった"),
            w.plot_develop("$jackを追い詰めて$sherlockは何とか宝剣を取り戻す"),
            w.plot_turnpoint("しかし取り戻した宝剣には肝心の$stoneが付いていなかった"),
            w.plot_resolve("皇太子は偽物の$stoneをつけた宝剣を使い、婚姻の儀を終わらせた"),
            #
            "ここから本編。三人称で、視点変更も可能。ただし誤認させるために$wilsonから始める",
            "宮殿から北側",
            w.plot_note("$wilsonは車でやってくる（公用車を利用している）"),
            w.plot_note("$wilsonはその日、ある仕事を依頼するためにその家を訪れた"),
            w.plot_note("$Baker街"),
            w.plot_note("もともと高級住宅地だが少しずつ商業施設に変わっている"),
            w.plot_note("住所のメモを見ながら$wilsonは歩く"),
            "少年の案内（ここですられている）",
            w.plot_note("地域に似つかわしくないボロボロの服装の少年たちがこっちを見てにやついている"),
            w.plot_note("少年の一人が声をかけてくる「誰か探してるの？」"),
            w.plot_note("と、他の少年たちが口論を始める"),
            w.plot_note("$wilsonは$ln_sherlock氏の場所を尋ねる"),
            w.plot_note("知ってるから案内すると言う少年に$wilsonはついていく"),
            w.plot_note("家まで案内されたが、少年は対価を求める"),
            w.plot_note("$wilsonは紙幣を握らせ、少年たちを帰らせる"),
            "$sherlockと初対面",
            w.plot_note("呼び鈴を鳴らすが返事がない"),
            w.plot_note("留守かもしれないと思いつつ何度か呼び鈴を押して待つ"),
            w.plot_note("腕時計を確認し、再度押そうとしたところで、覗き窓が開いた"),
            w.plot_note("「帰れ」といきなり言われて覗き窓が閉まる"),
            w.plot_note("$wilsonはこういう「変わり者」か困ったなと思いつつ、どうしても頼みたいことがあると"),
            w.plot_note("「王室からの依頼は全て断っているんだ」と言われる。何も説明していないのに"),
            w.plot_note("「なぜ分かったんだ？」と疑問に思う"),
            w.plot_note("$sherlockはいやいやながら説明する"),
            w.plot_note("通りに魔導タクシーを止め、そこからここまで歩いてくるのをずっと観察していたこと"),
            w.plot_note("こんな時間から魔導タクシーが使える人間は一般市民ではない"),
            w.plot_note("言葉遣いや着ているもの、また武術の心得は多少あるが、財布を擦り取られたことには気づいていないところから、武官ではないと判断"),
            w.plot_note("警察関係者でもなく、その上頼みたいことがあると口にした"),
            w.plot_note("あらゆる条件から絞られるのは王室から依頼を持ってきた執務官か事務官あたりという推察だ"),
            w.plot_note("「驚いたよ。変わっている男とは聞いたがそういう変わっているだったのか。確かにこれはよく切れる男のようだ」と"),
            w.plot_note("そこで改めて依頼をしようとするが、王室とは関係を断っているといい、追い返される"),
            "持ち込み事件",
            w.plot_note("さっきの少年が戻ってくる（市場の男の子$ignes）"),
            w.plot_note("「助けてよ！」と$sherlockに頼む"),
            w.plot_note("盗んだ財布のことは謝るが、仲間が面倒に巻き込まれたと相談する"),
            w.plot_note(""),
            "皇太子からの依頼",
            w.plot_note("そこに手紙が届く。それは皇太子からの依頼だった"),
            w.plot_note("$wilsonは自分の持ってきた依頼とは別に王室からのものと気づく"),
            w.plot_note("何とか$sherlockの家に招いてもらった$wilsonは、書簡を開封してそれを確認してもらう"),
            w.plot_note("書簡には「皇太子」の名前と、結婚するときに必要な宝剣（短刀）をある女性に貸してしまったことが書かれていて、それを取り返してもらいたいとあった"),
            w.plot_note("「そういうのは怪盗にでも頼めばいい」と$sherlockは最近話題の怪盗$jackの話を出す"),
            w.plot_note("$wilsonは書簡を燃やしながら事情を語る"),
            w.plot_note("ただ取り戻すだけなら強引に女性を逮捕するでもして取り戻せばいいが、なるべく穏便にことを運びたい、かつ、王室の人間には知られたくないという事情があり、あまり色々と手を尽くせないと"),
            w.plot_note("「じゃあ君が直接頼めばいい。それともそんなに物分りの悪い女性なのか？」と。金を詰めば解決するじゃないかと言うが"),
            w.plot_note("相手の女性は慰謝料よりも思い出の品としてその宝剣が欲しいというのだ"),
            w.plot_note("他のものではどうしても駄目らしい"),
            w.plot_note("謎なことは全くなにもないが、手紙を開封してしまった意味を理解していた$sherlockは渋々といった感じで、まずその女性に会うことを約束する"),
            w.plot_note("「しかし人間、ことに男女の問題解決は第三者が出向いたところでどうなるとも思えないがね」と"),
            "才女$aily",
            "セントジョンズウッド、サーペンタイン通り、ブライオニー荘（原作のアイリーンの住所）",
            w.plot_note("$sherlockは単身$ailyの邸宅へと向かう"),
            w.plot_note("$ailyは誰もが美人と認める容姿の持ち主で、近所でも評判のようだった"),
            w.plot_note("人柄もよく周囲の人は誰も彼女のことを悪く言わない"),
            w.plot_note("既に結婚しているらしく、無口な旦那と暮らしていると教わる"),
            w.plot_note("$sherlockが訪問すると彼女は外で話しましょうと、連れ出した"),
            w.plot_note("$ailyは事情を知っていて、$sherlockのことも情報を既に仕入れていた"),
            w.plot_note("その上で「見逃してもらえないか」と頼む"),
            w.plot_note("聞いていた話と違うので事情を聞こうとするが、夫が呼びに来て戻ってしまう"),
            "尾行",
            w.plot_note("事情を探るために、$sherlockは$ailyの尾行をする"),
            w.plot_note("彼女は孤児院に向かい、そこで寄付をしたり、歌を披露したり、音楽を教えたりしていた"),
            w.plot_note("$ailyは慈善活動を行っているようだった"),
            w.plot_note("ただしその財をどこから持ってくるのかよく分からない"),
            w.plot_note("夜、社交パーティに出向く"),
            w.plot_note("変装して潜り込む$sherlock"),
            w.plot_note("しかしダンスに誘われて、仕方なく付き合う"),
            w.plot_note("$ailyは気づいていて「一日ご苦労さま」と笑う"),
            w.plot_note("$sherlockは$ailyが分別があり、事情もよく理解できそうなのに、そこまであの皇太子に固執するのが分からないと言う"),
            w.plot_note("彼女は皇太子に対しての恋愛感情はないが、あれは気に入っているから渡せないと言う"),
            w.plot_note("皇太子の結婚に必要な代物だから良心があるなら返してあげてほしいと説明するが、そこで彼女は笑う"),
            w.plot_note("実は既に売り払ってもう手元にないから返せないのだと"),
            w.plot_note("彼女は慈善事業をしていて、その費用にしたという"),
            w.plot_note("だが盗品をさばく闇のマーケットにそんなものが出たという情報はない"),
            w.plot_note("その場は一旦引き下がるが、$sherlockは彼女がダンスホールにいる間に家に侵入することを考える"),
            "屋内捜索",
            w.plot_note("$sherlockは$ailyの自宅に向かう"),
            w.plot_note("配達員を装い、玄関に向かう"),
            w.plot_note("家は留守だった"),
            w.plot_note("鍵を開けて潜入する"),
            w.plot_note("家の中は物が少なく、寝室にはベッドすら置いていない"),
            w.plot_note("まるで引っ越してきたすぐか、引っ越す直前のようなものの無さだった"),
            w.plot_note("奇妙さを感じながら、家を後にする"),
            "存在しない女",
            w.plot_note("翌日、$sherlockは改めて$ailyのことを調べ始める"),
            w.plot_note("$ignesたちに頼んで、情報を洗ってもらうとともに、自分は資料から調べてみる"),
            w.plot_note("警察に出向き、資料科に頼んで、犯罪歴などに名前がないか調べてみる"),
            w.plot_note("役所の記録などにも名前は存在しない"),
            w.plot_note("帰宅して$ignesから話を聞く"),
            w.plot_note("どうも既に家は引っ越した後で、周辺の住民も誰も彼女のことを知らなかった"),
            w.plot_note("そこに$wilsonがやってくる"),
            w.plot_note("やってきた彼に$sherlockは「あの$ailyという女性は存在しない」と衝撃の事実を告げた"),
            w.plot_note("どうやら全てを知られていて（どこからか情報がもれた）、周辺住民も金を握らせて仕込んだサクラだと"),
            w.plot_note("昨日あそこでパーティが開かれていた事実もなかった"),
            w.plot_note("$wilsonには盗まれたと彼女に言われたと話すが、$sherlockはそれは嘘だと断言する"),
            w.plot_note("そして宝剣の場所は分かっていると言い、$wilsonについてくるよう言った"),
            "宝剣の隠し場所",
            w.plot_note("$sherlockが向かったのは彼女が訪れた孤児院だった"),
            w.plot_note("そこの子どもに$ignesが話している"),
            w.plot_note("中に入れてもらい、裏庭に出た"),
            w.plot_note("$sherlockは語る。$ailyの言動の中で唯一嘘がなかったのが、この孤児院への寄付だった"),
            w.plot_note("彼女はここの出身者の誰かだろうと推測するが、院長は既に他界し、別の人間に変わっていたから分からなかった"),
            w.plot_note("彼女は本来なら毎月十三日にしか訪れないらしい"),
            w.plot_note("それが昨日はまだ七日なのに訪れた。つまり、すぐにでも高跳びする必要があったのだ"),
            w.plot_note("彼女はここに預け、それから$sherlockに嘘を吹き込むために社交クラブに出向いた、偽の"),
            w.plot_note("「それじゃあ彼女は今どこに？」"),
            w.plot_note("「もうこの国にはいないだろうね」と言う"),
            w.plot_note("彼女が子どもに預けておいた小箱を手にして、中身を確認すると、それを再び子どもに渡した"),
            w.plot_note("偽物とすりかえたのだ"),
            "皇太子の結婚式",
            w.plot_note("無事に皇太子の結婚式は行われた"),
            w.plot_note("そのパレードを眺めながら$sherlockは苦々しい顔をしている"),
            w.plot_note("宝剣にハマっていたガーネットが偽物だったのだ"),
            w.plot_note("後日彼女から手紙がきて、そこに丁寧に挨拶がかかれていた"),
            w.plot_note("孤児院に向かった時にやってきた配達員こそが、彼女だったのだ"),
            w.plot_note("裏を掻かれた$sherlockはその女の名を今も忘れていない"),
            )


