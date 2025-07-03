from typing import List, Tuple, Any

def merge_evaluation_lists(
    list1: List[List[Any]],
    list2: List[List[Any]]
) -> List[List[Any]]:
    """
    [文章, 評価1] の形式のリストと [文章, 評価2] の形式のリストを受け取り、
    共通の文章に基づいて [文章, 評価1, 評価2] の形式で結合したリストを返します。

    Args:
        list1 (List[List[Any]]): 最初の評価リスト。各要素は [文章, 評価1] の形式。
        list2 (List[List[Any]]): 2番目の評価リスト。各要素は [文章, 評価2] の形式。

    Returns:
        List[List[Any]]: 結合されたリスト。各要素は [文章, 評価1, 評価2] の形式。
                         どちらかのリストにしか存在しない文章の場合、
                         対応する評価は None になります。
    """
    merged_data = {}

    # list1 のデータを辞書に格納
    for item in list1:
        if len(item) == 2:
            article, eval1 = item
            merged_data[article] = [eval1, None] # 評価2は仮にNoneとする

    # list2 のデータを辞書に結合
    for item in list2:
        if len(item) == 2:
            article, eval2 = item
            if article in merged_data:
                # 既に存在する場合、評価2を追加
                merged_data[article][1] = eval2
            else:
                # list1 に存在しない文章の場合、新規追加（評価1はNone）
                merged_data[article] = [None, eval2]

    # 辞書のデータを最終的なリスト形式に変換
    result_list = []
    for article, evaluations in merged_data.items():
        result_list.append([article, evaluations[0], evaluations[1]])

    return result_list
