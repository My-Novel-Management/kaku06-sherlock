# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ## main
            ("sherlock", "シャーロック", "ホーマー,シャーロック", 20,(1,1), "male", "勇者", "me:僕"),
            ("mary", "メアリー", "", 16,(1,1), "female", "武闘家", "me:ウチ:shal:シャル:k_pat:パット"),
            ("wilson", "ウィルソン", "ハドル,ウィルソン", 40,(1,1), "元神官", "me:私"),
            ("lime", "ライム", "", 19,(1,1), "female", "騎士（王女）", "me:私"),
            ("zeron", "ゼロン", "", 99,(1,1), "male", "闇の使者", "me:私"),
            ## sub
            ("aily", "アイリー", "ルドラー,アイリー", 20,(1,1), "female", "王族", "me:私"),
            ("jack", "ジャック", "", 20,(1,1), "female", "盗賊", "me:私"),
            ("moriano", "モリアーノ", "ジェーンズ,モリアーノ", 50,(1,1), "教授", "me:私"),
            ("muran", "ムーラン", "セーバス,ムーラン", 33,(1,1), "female", "助手", "me:私"),
            ("stan", "スタン", "フォルマン,スタン", 40,(1,1), "male", "元軍医", "me:俺"),# ワトソンの旧友スタンフォード。シャーロックを紹介する
            ("lisa", "リサ", "ハワードソン,リサ", 42,(1,1), "female", "大家", "me:わたし"),# ハドソン婦人。221B大家
            ("canon", "カノン", "デイル,カノン", 40,(1,1), "female", "バーテンダー", "me:私"),
            ## special
            ("philo", "ファイロース", "ディーノ,ファイロース", 35,(1,1), "male", "コレクタ", "me:ボク"),# ファイロ・ヴァンス。ヴァン・ダインの作品の主人公
            ## 王家（アーサー、パーシヴァル、ガラハッド、ボールスが主要４血脈）／アーサー王の円卓の騎士12人が元
            ("Arthur", "アーサー", "", 99,(1,1), "male", "英雄"),
            ("Percival", "パーシヴァル", "", 99,(1,1), "male", "英雄"),
            ("Galahad", "ガラハッド", "", 99,(1,1), "male", "英雄"),
            ("Bors", "ボールス", "", 99,(1,1), "male", "英雄"),
            ## 王室
            ("mikel", "マイケル", "ホーマー,マイケル", 27,(1,1), "役人", "me:俺"),# ホームズの義兄（マイクロフト
            ("adel", "アデル", "イリーネ,アデル", 28,(1,1), "秘書", "me:私"),
            ## 少年探偵団
            ("ignes", "イグネス", "", 14,(1,1), "male", "市場の手伝い", "me:俺"),
            ## 市場
            ("nowlis", "ノーリス", "", 30,(1,1), "male", "市場の男性", "me:俺"),# NOTE: 本物のwilson
            ## アンダーグラウンド
            ("flen", "フレン", "", 44,(1,1), "male", "情報屋", "me:ワタシ"),# EVEのグレンが元ネタ
            ## kingdom
            ## police
            ("appolo", "アポロ", "リキュール,アポロ", 77,(1,1), "male", "探偵", "me:私"),# エルキュール・ポワロ
            ("hasting", "ヘイスタン", "ヘイスタン,オーサー", 77,(1,1), "male", "小説家", "me:私"),# アーサー・ヘイスティング。ポワロのワトソン
            ("restrade", "レストラーデ", "グレイ,レストラーデ", 35,(1,1), "警察（警部）", "me:俺"),# レストレード警部
            ("greg", "グレッグ", "バイアー,グレッグ", 40,(1,1), "警察", "me:ワシ"),# トバイアス・グレグスン警部
            ("patson", "パットソン", "パットソン,モロー", 25,(1,1), "警察", "me:ボク"),# パタースン警部
            ("burner", "バーンズ", "バーンズ,ネルソン", 50,(1,1), "警察（警部）", "me:私"),# ベインズ警部。やりて。最後の事件
            ("edo", "エド", "ロックウェル,エド", 55,(1,1), "魔導学捜査官", "me:ワタシ"),# 最初に科学捜査研究所を創設したエドモン・ロカール
            ## 教団
            ("raul", "ラウル", "", 55,(1,1), "male", "大司教", "me:私"),# 大司祭。次期総主教候補の一人。
            ("romanu", "ロマヌ", "", 78,(1,1), "male", "総主教", "me:私"),# 総主教。ゼノ教の一番トップ
            ## 醜聞
            ("cassel", "カッセル", "", 68,(1,1), "male", "宝石技師", "me:ワシ"),
            ("godon", "ゴードン", "", 56,(1,1), "male", "オペラ座の支配人", "me:私"),
            ("yila", "リースウェル", "リースウェル,イーラ", 30,(1,1), "孤児院教師", "me:私"),
            ## 谷の関連
            ("kean", "キーン", "クラウデン,キーン", 25,(1,1), "male", "使用人", "me:俺"),
            ("kail", "カイル", "クラウデン,カイル", 55,(1,1), "male", "使用人", "me:私"),
            ("jean", "ジェーン", "タイラー,ジェーン", 45,(1,1), "female", "婦人", "me:私"),
            ("royd", "ロイド", "タイラー,ロイド", 50,(1,1), "male", "不動産業", "me:私"),
            ("mackinger", "マッキンガー", "", 22,(1,1), "male", "警官", "me:自分"),
            ("conery", "コネリー", "", 55,(1,1), "female", "教師", "me:私"),
            ## 赤鎧クラブ
            ("jakins", "ジェイキンス", "ジェイキンス,ルアン", 50,(1,1), "male", "質屋オーナー", "me:俺"),
            ("jeena", "ジーナ", "ジェイキンス,ジーナ", 51,(1,1), "female", "質屋の妻", "me:私"),
            ("bins", "ビンス", "ホールディング,ビンス", 25,(1,1), "male", "質屋バイト", "me:オレ"),
            ## ガーネット
            ("raider", "ラーダ", "ジェイ,ラーダ", 40,(1,1), "male", "事件被害者", "me:オレ"),
            ("hornet", "ホーネット", "ホーネット,ヘンク", 55,(1,1), "male", "食肉卸問屋", "me:私"),
            ("moura", "モーラ", "モーラ,ジョディ", 40,(1,1), "female", "夫人", "me:私"),# NOTE 事件被害者
            ("peter", "ペータ", "ペータ,グリッジ", 45,(1,1), "male", "ガードマン", "me:僕"),
            ## 魔獣
            ("baskervilles", "ヴィルヘルム", "", 55,(1,1), "male", "地主", "me:儂"),# バスカヴィル家
            ("cherry", "チェリー", "ヴィルヘルム,チェリー", 30,(1,1), "female", "婦人", "me:私"),
            ("moch", "モック", "ジリアン,モック", 35,(1,1), "male", "観光協会", "me:私"),
            ("betty", "ベティ", "", 35,(1,1), "female", "使用人", "me:わたし"),# 使用人
            ("hugar", "ヒューガ−", "カリム,ヒューガー", 60,(1,1), "male", "元刑事", "me:オレ"),# 元刑事
            ("reui", "ルイ", "フルーゲル,ルイ", 34,(1,1), "female", "社会学者", "me:ワタシ"),# 社会学者
            ("milk", "ミルク", "フランクル,ミルク", 28,(1,1), "female", "新聞記者", "me:わたし"),# 新聞記者
            ("jamos", "ジャモス", "ステープル,ジャモス", 65,(1,1), "male", "医師・歴史研究家", "me:私"),# 歴史研究家
            ("karl", "カール", "ユグゾ,カール", 45,(1,1), "male", "心霊学者", "me:私"),# 心霊研究者
            ("dold", "ドルド", "", 50,(1,1), "male", "料理人", "me:俺"),# シェフ
            ## 最後の事件
            ("stein", "シュタイン", "ワーラー,シュタイン", 40,(1,1), "male", "元大学教授", "me:僕"),
            ## 空き家の事件
            ("jake", "ジェイク", "", 40,(1,1), "male", "連続殺人犯", "me:オデ"),
            ("ronald", "ロナール", "アデラ,ロナール", 40,(1,1), "male", "伯爵", "me:私"),
            ## プロローグ
            ("stanry", "スタンリー", "", 35,(1,1), "male", "不動産屋", "me:俺"),
            # モリアーノの後輩。殺される男
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Office", "勇者探偵社", "London"),
            #
            # 他国
            ("Belfast", "ウェルフォース", "", (-200,-200)),# ベルファスト
            ("Sachsen", "ザフシュテン", "", (400,200)),# ザクセン（ドイツ）
            # 王国内
            ("England", "ブリギス", "", (0,0)),
            ("Leeds", "レード", "England", (800,100)),# リーズ
            ("Manchester", "カンチェスター", "England", (800,200)),# マンチェスター
            ("Sheffield", "シーフィール", "England", (900,300)),# シェーフィールド
            ("Liverpool", "イバール", "England", (600,300)),# リバプール
            ("Leicester", "リスター", "England", (900,400)),# レスター
            ("Birmingham", "アーミング", "England", (800,500)),# バーミンガム
            ("Cambridge", "キャンバッジ", "England", (1000,700)),# ケンブリッジ
            ("Bristol", "ウリストル", "England", (700,1000)),# ブリストル
            ("Oxford", "オーカスフォール", "England", (900,900),),# オックスフォード
            ("London", "ロムダス", "England", (1000,1000)),# ロンドン
            ("WestMidlands", "ウェストミドラン", "England", (500,1000)),# ウェスト・ミットランズ
            ("Herefordshire", "ヘルオードジャー", "England"),# ヘレフォードシャー
            ("Dartmour", "ダースモア", "London"),# ダートムア。現実では南西部のムーア（湿原）。国立公園になっている
            ("ThamesRiver", "タイムズ川", "London"),# テムズ川
            # ロンドン市内
            ("RegentsPark", "リーネンツ", "London", (-10, -100)),# リージェンツパーク
            ("KingsCross", "キングロス", "London", (0,-100)),# キングスクロス
            ("NottingHill", "ナッタンヒル", "London", (-300,0)),# ノッティングヒル
            ("Paddington", "アディンポン", "London", (-200,0)),# パディントン
            ("Soho", "ソルホー", "London", (0,100)), # ソーホー
            ("Shoreditch", "ショーディ", "London", (200,100)),# ショアディッチ
            ("Kensington", "ケーニトン", "London", (-300,100)),# ケンジントン
            ("OldCity", "シティ", "London", (200,200)),# シティ
            ("Westminster", "イーストミンストル", "London", (0,300)), # ウェストミンスター
            ("PoliceStation", "派出所", "London"),
            ("PoliceOffice", "中央警察署", "London"),
            ("PoliceInterrogationRoom", "警察・取調室", "London"),
            ("Hospital", "病院", "London"),
            ("SickRoom", "病院・病室", "London"),
            # ソーホー。代表的な歓楽街
            # イーストエンド（シティの東側、テムズ川の北側）下町
            ("EastEnd", "エンドタウン", "London"),# イーストエンド。下町。スラム街
            ("Whitechapel", "レッドベル", "London"),# ホワイト・チャペル
            ("EmptyHouse", "空き家", "London"),
            ("EmptyHouseSubway", "空き家の地下道", "London"),
            ("TowerLondon", "ロムダス塔", "London"),# ロンドン塔。昔占い師にいわれ大量のワタリガラスを飼っている
            ("AbandonedFactory", "廃工場", "EastEnd"),
            # ウェストエンド（シティの西側）繁華街
            ("WestEnd", "ウェストタウン", "London"),
            # シティ（旧市内）
            ("Market", "中央市場", "London"),
            ("WilsonHouse", "ウィルソンの家", "OldCity"),
            ("WilsonHouseLiving", "ウィルソンの家・リビング", "WilsonHouse"),
            ("WilsonHouseDining", "ウィルソンの家・ダイニング", "WilsonHouse"),
            ("WilsonHouseKitchen", "ウィルソンの家・キッチン", "WilsonHouse"),
            ("WilsonHouseBedroom", "ウィルソンの家・寝室", "WilsonHouse"),
            ("WilsonHouseStorage", "ウィルソンの家・物置", "WilsonHouse"),
            ("WilsonHouseBathroom", "ウィルソンの家・浴室", "WilsonHouse"),
            ("WilsonHouseDrawing", "ウィルソンの家・応接間", "WilsonHouse"),
            # ウェストミンスター。昔からの政治の中心部
            ("CharingCross", "チェリーグロス", "London"),# チャリングクロス
            ("PubConan", "パブ", "London"),
            ("Church", "教会", "London"),
            # 中心部
            ("WestminsterCastle", "イーストミンストル宮殿", "London"),# ウェストミンスター宮殿
            ("WestminsterTemple", "イーストミンストル寺院", "London"),# ウェストミンスター寺院
            ("WestminsterTempleHall", "イーストミンストル寺院・ホール", "WestminsterTemple"),
            ("WestminsterTempleSubway", "イーストミンストル寺院・地下道", "WestminsterTemple"),
            ("WestminsterTempleRitualRoom", "イーストミンストル寺院・地下儀式施設", "WestminsterTemple"),
            ("WestminsterParliament", "王国議事堂", "London"),# 国会議事堂
            ("PicadilyCircus", "ピカッドリー", "London"),# ピカデリーサーカス
            ("Portsmouth", "パーツマス", "London"),# ポーツマス
            # ベーガー街
            ("Baker", "ベイリー", "London"),# ベイカー街
            ("SherlockHouse", "シャーロックの家", "Baker"),
            ("SherlockHouseLiving", "シャーロックの家・リビング", "SherlockHouse"),
            ("SherlockHouseKitchen", "シャーロックの家・キッチン", "SherlockHouse"),
            ("SherlockHouseDining", "シャーロックの家・食堂", "SherlockHouse"),
            ("SherlockHouseLabo", "シャーロックの家・研究室", "SherlockHouse"),
            ("SherlockHouseBedroom", "シャーロックの家・寝室", "SherlockHouse"),
            ("SherlockHouseReadingRoom", "シャーロックの家・書斎", "SherlockHouse"),
            ("SherlockHouseStorage", "シャーロックの家・物置", "SherlockHouse"),
            ("SherlockHouseBathroom", "シャーロックの家・バス", "SherlockHouse"),
            ## 醜聞
            ("StJhonsWood", "サーペント", "London"),# セントジョンズウッド（作中のサーペンタイン通り）。リージェンツパークの北西。アイリーンの家がある
            ("EdgewareRoad", "エッジロード", "London"),# エッジウェアロード
            ("Temple", "エンプル", "London"),# テンプル
            ## 赤鎧クラブ
            ("SaxeCoburgSquare", "サコバーズスクエア", "London"),# ザクセン・コーブルク・スクエア
            ("StPaul", "サンポール", "London"),# セントポール
            ("JakinsHouse", "ジェイキンスの家", "London"),
            ("Farringdon", "ファイドン", "London"),# ファリンドン街
            ## ガーネット
            ("Angel", "アンヘル", "London"),# エンジェル駅
            ("Kilburn", "ギルバー", "London"),# キルバーン
            ("Goodge", "グージ", "London"),# グッジ街
            ("CoventGarden", "グベントカーデン", "London"),# コベントガーデン
            ("SpecialSchool", "王立学園", "London"),# 王立学園
            ## 魔獣
            ("Embankment", "エンバンク", "London"),# エンバクメント
            ("Tottenham", "トッテンム", "London"),# トッテナム
            ("Bourough", "ボロー", "London"),# バラ
            ("Fulham", "ウルアム", "London"),# フルハム
            ("Holborn", "ホールバー", "London"),# ホルボーン
            ## 最後の事件
            ("Oxford", "ノクスフォード", "London"),# オックスフォード・サーカス
            ("Olympia", "オムニピア", "London"),# オリンピア
            ("Bond", "ボンドル", "London"),# ボンド
            ## 空き家
            ("MarbleArch", "マールアート", "London"),# マーブルアーチ
            ("MountCottage", "山小屋", "Belfast"),
            # Commons
            ("Street", "路地", "London"),
            # 乗り物
            ("InCar", "車内", "London"),
            ("InTrain", "列車内", "London"),
            ("InShip", "船内", "London"),
            # 現代
            ("ReadingRoom", "書斎", "London"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ("base_year", "基本年", 1,1, 1881),
            ("goose_case", "ガチョウの殺人事件", 12,20, 1881),# 青いガーネット
            ("future_day", "本を書いている日", 1,1, 1891),
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ("item", "魔具"),
            ("gun", "魔銃"),
            ("train", "魔導列車"),
            ("taxi", "魔導タクシー"),
            ("car", "魔導車"),
            ("telephone", "魔導通話"),
            ("compass", "魔導盤"),
            ("drag", "魔導ドラッグ"),
            ## 醜聞
            ("royalsword", "宝剣"),
            ## 重要アイテム
            ("stone", "魔石"),
            ("red_stone", "紅魔石"),# ルビー
            ("blue_stone", "蒼魔石"),# ガーネット
            ("white_stone", "白魔石"),# フローライト
            ("black_stone", "黒魔石"),# オブシディアン
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ("G", "ポンド"),
            ("hero", "勇者"),
            ("boss", "魔王"),
            ("monster", "魔獣"),
            ("k_shal", "シャル"),
            ## 種族
            ("ajin", "亜人"),
            ("animal", "獣人"),
            ("transform", "獣化"),
            ("elf", "エルフ"),
            ("werewolf", "人狼"),
            ## 技術
            ("science", "魔導"),
            ("enagy", "魔素"),
            ("light", "魔光"),
            ## 古代技術
            ("magic", "魔法"),
            ("sorcery", "魔術"),
            ## その他
            ("missing", "喪失知識"),
            ("cultX", "教団Ｘ"),
            ("Xeno", "聖ゼノ教"),# Xenoは異物の意味。正式には「ゼノ・カトル教」。カトルは普遍的。カトリックとも
            ("festival", "勇者生誕祭"),
            ## 団体
            ("foundation", "パーシヴァル財団"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

# Title
TITLES = [
        "プロローグ",
        "第１章　皇太子の醜聞",
        "第２章　悲しみの谷",
        "第３章　謎の赤鎧クラブ",
        "第４章　ガチョウのガーネット",
        "第５章　魔獣伝説",
        "第６章　これが最後の事件",
        "第７章　空き家には気をつけろ",
        "エピローグ",
        ]

