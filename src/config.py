# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) AREAS
#       エリア設定
# 3) STAGES
#       舞台基本設定
# 4) DAYS
#       年月日設定
# 5) TIMES
#       時間帯基本設定
# 6) ITEMS
#       小道具設定
# 7) WORDS
#       辞書設定
# 8) RUBIS
#       ルビ設定
# 9) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("aniki", "兄貴", "", 25,(1,1), "male", "無職", "me:俺"),
        ("hati", "ハチ", "", 20,(1,1), "male", "無職", "me:おら"),
        ("shopper", "店主", "", 45,(1,1), "male", "店主", "me:私"),
        ("teller", "話者", "", 40,(1,1), "male", "落語家", "me:私"),
        ("god", "天の声", "", 99,(1,1), "male", "神", "me:わたし"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("ramen", "ラーメン屋", "Tokyo"),
        ("shop1", "謎の店", "Tokyo"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("current", "current", 1,1,2020),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        )

LAYERS = (
        # Key / Title / Words
        )

