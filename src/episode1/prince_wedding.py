# -*- coding: utf-8 -*-
'''
Episode 1-5: "王子の結婚"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "王子の結婚"


# NOTE: outlines
ABSTRACT = """
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
"""


# Scenes


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$ailyこと怪盗$jackは$sherlockに全て見抜かれていたことで本性を現す"),
            w.plot_turnpoint("$jackは最初から$royalswordが目的で王子に近づいたと告白する"),
            w.plot_develop("$sherlockは$jackが本物の$ailyの自殺を偽装するために、強盗を装ったこと等を推理で当てた。彼女はすんなりと$sherlockに$royalswordの返却を約束する"),
            w.plot_turnpoint("しかし後日届けられた$royalswordには肝心の$red_stoneが付いていなかった"),
            w.plot_resolve("$stoneのレプリカを作ってもらい、何とか無事に王子の結婚式は行われた"),
            w.plot_note("$sherlockは$yilaに対して「$ailyですよね？」と言った"),
            w.plot_note("$yilaは分からないふりをする"),
            w.plot_note("$sherlockは更に言う。「そしてあなたは$jackでもある」と"),
            w.plot_note("$jackとはこの一年ほどの間出没している怪盗$jackだ"),
            w.plot_note("$wilsonは驚く。「怪盗$jackだって？」"),
            w.plot_note("彼女の表情が変わり、まとめていた髪を解く。「そこまで分かってるんだ。さすが$sherlockさん」と"),
            w.plot_note("更に続けて「そしてオペラ歌手$ailyの家の寝室で亡くなっていたのが本物の$ailyだ」"),
            w.plot_note("$wilsonは理解できていなかったが、$sherlockは既に事件の真相が分かっているらしい"),
            w.plot_note("二人は事件について簡単に話し合う"),
            w.plot_note("「いつ全てが分かった？」"),
            w.plot_note("$sherlockは「最初からその可能性も考慮に入れていたよ」と。その可能性は「自殺」だ"),
            w.plot_note("$sherlockは$jackが$ailyの自殺を他殺と偽装するためにあれをやったと"),
            w.plot_note("「だってやっと光が当たったんだよ。その子が自殺しましたじゃ、あの子の人生が可哀想さね」"),
            w.plot_note("「でも警察はいずれ君を疑うことになる」"),
            w.plot_note("「しばらくこの国を離れることになったから、構わないよ」"),
            w.plot_note("$sherlockは$royalswordの行方を尋ねる。「もう売ったのか？」"),
            w.plot_note("まだ手元にあると答えるが、どうやら自分で好きにできない代物だと分かる"),
            w.plot_note("「今すぐに返してくれれば手荒な真似はしなくて済む。具体的には警察に手を回してある」と"),
            w.plot_note("$ailyと$sherlockの駆け引き"),
            w.plot_note("$sherlockは$ailyと$jackについて語る"),
            w.plot_note("$ailyがパブで歌い始めた。それを$jackは応援していたが、店に顔を出していた訳ではなく、彼女が歌で食べていけるように考えていた"),
            w.plot_note("$ailyが無事にスカウトされ、オペラハウスで働くようになる。しかし誤算だったのは歌手ではなく役者である必要があったこと"),
            w.plot_note("$ailyは精神的に病み、仕事にでなくなる"),
            w.plot_note("体型の似ていた$jackは彼女になりすまし、役者として名声を得る"),
            w.plot_note("そこまでしたが$ailyは回復せず、$jackが$ailyに成り代わる"),
            w.plot_note("$jackは当初の目的通り、王子に近づき、$royalswordを奪うことに成功する。$dragを使ったのだろう"),
            w.plot_note("そんな中で$ailyが自殺してしまう"),
            w.plot_note("またそんな時に王子が$royalswordを取り戻しにくる"),
            w.plot_note("困った$jackは$ailyが殺されたことにした"),
            w.plot_note("結果的に警察は殺人事件として$ailyの件を処理しようとしている"),
            w.plot_note("警察によって押収されたものの中に$royalswordはない。王子は諦めるしかない"),
            w.plot_note("犯人にされている$jackは逃亡し、この事件は終わるはずだった"),
            w.plot_note("$jackは$sherlockの推理に一つだけ違っているところがあると語る"),
            w.plot_note("$ailyが自力でオペラ歌手を射止めた。スカウトされた。$jackは何もする余裕がなかったと"),
            w.plot_note("全ての手の内がバレた$jackは$sherlockに「完敗だ」と言う"),
            w.plot_note("「それでも何故$jackだと思ったの？」"),
            w.plot_note("本物の$ailyには$royalswordを返さない理由が見つからないことと、逆にそれが欲しい人物"),
            w.plot_note("更に事前に$sherlockに王子が依頼をしてくる情報を得られた人物。それは$adelしかない。そしてあの日の$adelはわざわざ制服姿だった"),
            w.plot_note("故に彼女に成り代わっていた人物、そんなことをするのは$jackだろうと"),
            w.plot_note("そしてブラフをかけた"),
            w.plot_note("素直に告白するとは思っていなかったが、そのときの表情から読み取れると思った"),
            w.plot_note("自分が変装していたことまでバレていて驚く$jack"),
            w.plot_note("$jackは$royalswordを返すと約束し、見逃してもらうことにした"),
            #
            w.plot_note("$royalswordは孤児院に預けられていた"),
            w.plot_note("それを$adelに取りに来てもらう"),
            w.plot_note("$sherlockの言ったように彼女は制服姿ではなく、完全に配達人のそれ"),
            w.plot_note("$sherlockは言う「彼女はいつも何かしら別の人間を装ってやってくる」"),
            w.plot_note("しかしそこで中身を確かめた$adelは言う「これには大事なものが足りません。$red_stoneです」と"),
            w.plot_note("$sherlockは本当の狙いは$red_stoneだったと言う。「やられた」と"),
            w.plot_note("考えた$sherlockは$red_stoneの形状などを教えてもらい、数日預けてもらうことに"),
            #
            w.plot_note("後日、王子の結婚式は行われた"),
            w.plot_note("大聖堂の中で行われたそれには多くの著名な人物が招かれた"),
            w.plot_note("$wilsonは$sherlockに尋ねる「大丈夫かね。あれで」"),
            w.plot_note("「レプリカだろうと構わないのさ。ただ彼らがそれを本物だと思えばいい。本物なんてその程度の価値しかない」と"),
            outline=ABSTRACT)

