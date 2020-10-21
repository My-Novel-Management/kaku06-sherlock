# -*- coding: utf-8 -*-
'''
About: "プロット"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


def main_notes(w: World):
    return (
            base_plot(w),
            mystery_note(w),
            )


# world settings
def base_plot(w: World):
    return w.writer_note("基本プロット",
            "かつて$bossや$heroが存在した世界",
            "しかし$bossや$monsterの脅威は去り、世界は平和に暮らしていた",
            "ただその世界で幅を利かせていたのが「$hero利権」と呼ばれるもので、現在国を収める「女王」とその一族は$heroの末裔やその仲間の末裔たちである",
            "またかつては存在していた魔法・魔術は姿を消し、その力の源であった$enagyを動力源とする機械が誕生していた",
            "そんな世界で物語は進行する",
            "作品は記述者である「$wilson」の語りによって始まる",
            "彼がある事情で元勇者の血筋を引くらしい若者を探すのを依頼にやってくる",
            "それがどうも偏屈な若者で、奇妙な事件に首を突っ込んではあれこれと忠告していくという",
            "王立警察からひどくうとまれている存在だが腕は確かというので紹介してもらった",
            "そこに向かうと中に勝手に入れと言われて、その通りに奥に進むと、応接間でいきなり「帰れ」と言われて落とし穴に落とされそうになった",
            "依頼をしようと口を開くと、何を言う前から$wilsonの素性までぴたりと当てて、その上で「王室からの依頼は受けない」と断られる",
            "何とか依頼を受けてもらおうとしていると、そこに別の依頼人が飛び込んできて「助けてくれ」と",
            "そこから$wilsonは$sherlockという探偵と奇妙な事件に出くわすことになる",
            )


def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "基本路線は「長編１本」で、細かい事件や仲間集めを挟みつつ、冒険嫌いな勇者に冒険させるような展開",
            "１０万字の予定は以下のようにする",
            "短編（１万から２万字）を３本で５万字",
            "中編（５万字）を１本",
            "これで１冊分になるように調整する",
            "今回はホームズシリーズから色々と引っ張ってきて、そのタイトルをかぶせる",
            "冒険に出たくない勇者を大好きな「謎」を餌になんとか冒険させようとする、という形に",
            "ホームズ（初期型）とワトソン（クラデス）に、途中参加メンバーを加えてパーティにする",
            "勇者ということは隠しつつ、探偵です、の代わりに「勇者です」と言う",
            "「ただの謎解き好きな勇者です」",
            "全体を通して「緋色の研究」を。内容として細かく「踊る人形」とか入れていく",
            "ボヘミアの醜聞と赤毛組合、",
            "短編は基本的に「冒険」から引く",
            "１話は「緋色の研究の冒頭」＋「冒険」",
            "５話以降は「緋色の研究」のラストを使う。ワトソン役の$cradesが記述して残して研究していくことを決める",
            "勇者は「なぜ突然魔王が消えたのか」を知っていると$cradesと読者に思わせる",
            "１話で「$heroと$crades」コンビ結成かつ$heroの能力披露",
            "２話が$pan参加の話", "以前は「白馬に乗った王子伝説」",
            "３話が$emilの話", "大食い仮面騎士",
            "４話くらいで$ailの話ひっかけ",
            "５話からちょっと大型事件、連続殺人とか、密室殺人とか",
            "基本方針は「冒険の旅に出るまで」この街で事件解決をしつつ仲間や情報を揃える、が１巻",
            "全体の流れ：",
            "謎の殺人事件が裏で起こっている。関係者はかつて勇者に協力したとされる人間（事実ではなく噂であっても）",
            "最初は「簡単な依頼」を$cradesが持ってくる",
            "でもその事件を解決すると殺人事件に遭遇",
            "その容疑者に$pannaが選ばれる",
            "容疑を晴らすためにがんばる",
            "途中で謎の赤鎧組合が関わっているのを知る",
            "そこに潜んでいたのは「失踪中の第二王女」だった",
            "鎧の呪いを解いたが彼女は無口でしゃべらない",
            "四人の仲間と同居することになる",
            "ここまでが四話",
            "残りで怪盗と勇者連続殺人事件の真犯人を追い詰める",
            "実は$cradesが真犯人で、$cradesを名乗る別の人物だった",
            "$k_shalを$heroと確認し、滝壺に落とす",
            "しかし廃墟の冒険で生きていたことが分かり、$cradesを追い詰める",
            w.plot_note("１話（安楽椅子・ダイイングメッセージ）：$cradesが$heroを見つけて、魔王退治を依頼する。現場に行かずに事件解決（しかし情報間違っていたので後で推理し直す）"),
            w.plot_note("２話（アリバイ・人物偽装）：ボヘミアの醜聞。$ail登場"),
            w.plot_note("３話（事実誤認）：$pan仲間回。ボスコム警告の惨劇"),
            w.plot_note("４話（奇妙な設定）：$emil仲間回。赤毛組合。鎧騎士だけを集めた謎の組合"),
            w.plot_note("５話（密室）：くちびるのねじれた男"),
            w.plot_note("６話（クローズド）：犬の仕業みたいな謎の殺人事件発生"),
            w.plot_note("７話（奇妙な凶器）：魔獣の討伐依頼"),
            w.plot_note("８話（不可能犯罪）：$ail再登場し、警告"),
            w.plot_note("９話（見立て）：冒険嫌いの理由。"),
            w.plot_note("１０話（心理トリック）：$heroが滝に落ちる。ライヘンバッハの滝（最後の事件）"),
            w.plot_note("１１話（人物誤認）：実は謎の男の正体は$heroだった。空き家の冒険"),
            w.plot_note("１２話（叙述トリック）：戻ってきた$hero。実は$gradesは偽物で、連続殺人の真犯人だった"),
            w.plot_note("実は$cradesは魔王の使いで、勇者がまだ生きていることの確認とその殺害が目的だった"),
            w.plot_note("本物の$cradesは後になって登場する。ずっと謎の空間に閉じ込められていて、様々な時空を彷徨っていた"),
            )


def mystery_note(w: World):
    return w.writer_note('トリック設定',
            w.tag.title("赤鎧組合"),
            "元ネタは「赤毛組合」",
            "赤鎧の人間を募集するという奇妙な内容だが、実はターゲットを守衛場所から遠ざけておくための手段",
            "その間にもぬけの殻となった場所で宝物を奪うための抜け穴を作ったりしていた",
            w.tag.title("$pannaが容疑者に"),
            "容疑者偽装トリック",
            "元ネタは「ボスコム谷の殺人」",
            "$cradesが持ってきた事件を解決したらそこに飛び込んできた新依頼がこれ",
            w.tag.title("元神官の男"),
            "$heroを訪れた時に何も聞かなくても「国王の差金」と見抜く",
            "元ネタは「緋色の研究」の冒頭部分",
            "ワトソンがアフガン帰りの軍医であることを見抜いたくだり",
            "文官ではなく現場である程度武道の心得があり、なおかつ$enagyの扱いにも長けている",
            w.tag.title("アクロイド殺し的な"),
            "記述者として「$crades」が登場しているが、実はその$cradesは偽物であり、本物は別のところにいた（療養という名目で温泉旅館を巡っていた）",
            "その間に$cradesに成り代わった闇のモノが$heroになる候補としての人間を殺すために調査に訪れていた",
            "空き家の事件なども$cradesが残った$pannaたちを事故に見せかけて殺害するために仕組んだ",
            "人知れぬ亡くなるのはほぼ$cradesか彼の指示、仕込みによるものだった",
            w.tag.title("ヴィルガスクの魔犬"),
            "元ネタは「バスカヴィル家の犬」",
            "魔犬の噂を流しておいて、実は普通に殺していただけだった",
            "一番の目的は人払い",
            "原作では伝説を作っておいて、あとで凶暴な猟犬を買い、それを手なづけて、心臓ショック死を狙っている",
            "狙いは遺産や財産になる",
            "今回は魔王復活の儀式から遠ざけるためである",
            "ある宗教団体のせいにしたが、実は$cradesが魔王復活を狙っていた",
            w.tag.title("最後の事件"),
            "元ネタは「最後の事件」",
            "これはホームズを処分するために作者が書いたもの",
            "ここで「教授」の存在がクローズアップされる",
            "しかしその教授の正体こそが$cradesだった",
            "彼が追っていたのはその影なのだ",
            "その影と同士討ちのようになり、闇の世界まで続くという滝に落ちてしまう",
            w.tag.title("空き家の事件"),
            "$heroを処分した$cradesは$pannaたちも処分しようと、廃墟の事件の調査をもちかける",
            "そこで事故に遭ったようにみせかけられ、睡眠薬で眠らされた彼女たちは絶体絶命の危機",
            "そこに最近街で見かけていた「鼻のひんまがった男」がちょうどやってきて彼女たちを助け出す",
            "自分のおんぼろホームに案内し、そこで正体を明かす",
            "この事件により彼は$cradesが殺人犯であることを確信するのだった",
            )

