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
            ## sub
            ("mikel", "マイケル", "ホーマー,マイケル", 27,(1,1), "役人", "me:俺"),
            ("aily", "アイリー", "ルドラー,アイリー", 20,(1,1), "female", "王族", "me:私"),
            ("jack", "ジャック", "", 20,(1,1), "female", "盗賊", "me:私"),
            ("moriano", "モリアーノ", "ジェーンズ,モリアーノ", 50,(1,1), "教授", "me:私"),
            ("stan", "スタン", "フォルマン,スタン", 40,(1,1), "male", "元軍医", "me:俺"),# ワトソンの旧友スタンフォード。シャーロックを紹介する
            ("lisa", "リサ", "ハワードソン,リサ", 42,(1,1), "female", "大家", "me:わたし"),# ハドソン婦人。221B大家
            ## 少年探偵団
            ("ignes", "イグネス", "", 14,(1,1), "male", "市場の手伝い", "me:俺"),
            ## 市場
            ("nowlis", "ノーリス", "", 30,(1,1), "male", "市場の男性", "me:俺"),# NOTE: 本物のwilson
            ## kingdom
            ## police
            ("appolo", "アポロ", "リキュール,アポロ", 50,(1,1), "male", "警察（警視）", "me:私"),
            ("restrade", "レストラーデ", "グレイ,レストラーデ", 35,(1,1), "警察（警部）", "me:俺"),# レストレード警部
            ("greg", "グレッグ", "バイアー,グレッグ", 40,(1,1), "警察", "me:ワシ"),# トバイアス・グレグスン警部
            ("patson", "パットソン", "パットソン,モロー", 25,(1,1), "警察", "me:ボク"),# パタースン警部
            ("burner", "バーンズ", "バーンズ,ネルソン", 50,(1,1), "警察（警部）", "me:私"),# ベインズ警部。やりて。最後の事件
            ## 教団
            ("raul", "ラウル", "", 55,(1,1), "male", "大司教", "me:私"),# 大司祭。次期総主教候補の一人。
            ("romanu", "ロマヌ", "", 78,(1,1), "male", "総主教", "me:私"),# 総主教。ゼノ教の一番トップ
            ## 谷の関連
            ("kean", "キーン", "クラウデン,キーン", 25,(1,1), "male", "使用人", "me:俺"),
            ("kail", "カイル", "クラウデン,カイル", 55,(1,1), "male", "使用人", "me:私"),
            ("jean", "ジェーン", "タイラー,ジェーン", 45,(1,1), "female", "婦人", "me:私"),
            ("royd", "ロイド", "タイラー,ロイド", 50,(1,1), "male", "不動産業", "me:私"),
            ## 赤鎧クラブ
            ("jakins", "ジェイキンス", "ジェイキンス,ルアン", 50,(1,1), "male", "質屋オーナー", "me:私"),
            ("bins", "ビンス", "ホールディング,ビンス", 25,(1,1), "male", "質屋バイト", "me:オレ"),
            ## ガーネット
            ## 魔獣
            ("cherry", "チェリー", "ヴィルヘルム,チェリー", 30,(1,1), "female", "婦人", "me:私"),
            ("moch", "モック", "ジリアン,モック", 35,(1,1), "male", "観光協会", "me:私"),
            ## 最後の事件
            ("stein", "シュタイン", "ワーラー,シュタイン", 40,(1,1), "male", "元大学教授", "me:僕"),
            ## プロローグ
            ("stanry", "スタンリー", "", 35,(1,1), "male", "不動産屋", "me:俺"),
            ## 最後の事件
            # モリアーノの後輩。殺される男
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Office", "勇者探偵社", "London"),
            #
            ("Dartmour", "ダースモア", "London"),# ダートムア
            ("ThamesRiver", "タイムズ川", "London"),# テムズ川
            # 他国
            ("Belfast", "ウェルフォース", "", (-200,-200)),# ベルファスト
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
            # ソーホー。代表的な歓楽街
            # イーストエンド（シティの東側、テムズ川の北側）下町
            ("EastEnd", "エンドタウン", "London"),# イーストエンド。下町。スラム街
            ("Whitechapel", "レッドベル", "London"),# ホワイト・チャペル
            ("EmptyHouse", "空き家", "London"),
            ("TowerLondon", "ロムダス塔", "London"),# ロンドン塔。昔占い師にいわれ大量のワタリガラスを飼っている
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
            ("CharingCross", "チェリーグロス", "London", ),# チャリングクロス
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
            ("stone", "魔石"),
            ("telephone", "魔導通話"),
            ("compass", "魔導盤"),
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ("G", "ポンド"),
            ("hero", "勇者"),
            ("boss", "魔王"),
            ("monster", "魔獣"),
            ("k_shal", "シャル"),
            ("enagy", "魔素"),
            ("magic", "魔導"),
            ("animal", "獣人"),
            ("elf", "エルフ"),
            ("ajin", "亜人"),
            ("werewolf", "人狼"),
            ("science", "魔導学"),
            ("missing", "喪失知識"),
            ("cultX", "教団Ｘ"),
            ("Xeno", "聖ゼノ教"),# Xenoは異物の意味。正式には「ゼノ・カトル教」。カトルは普遍的。カトリックとも
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

