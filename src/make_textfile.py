from typing import List, Any

def export_results_to_text_file(
    merged_data_list: List[List[Any]],
    accuracy: float,
    output_file_path: str
) -> bool:
    """
    結合されたデータリストと正答率を一つのテキストファイルに書き出します。

    Args:
        merged_data_list (List[List[Any]]): [文章, 評価1, 評価2] 形式の結合済みリスト。
        accuracy (float): 計算された正答率（パーセンテージ）。
        output_file_path (str): 結果を書き出すテキストファイルのパス。

    Returns:
        bool: ファイルの書き出しが成功した場合は True、失敗した場合は False。
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            # ヘッダー行を書き込む (オプション)
            f.write("Article\tEvaluation1\tEvaluation2\n")

            # 結合済みデータリストを書き込む
            for item in merged_data_list:
                if len(item) == 3:
                    article, eval1, eval2 = item
                    # None を空文字列に変換して書き込み時にエラーを防ぐ
                    eval1_str = str(eval1) if eval1 is not None else ""
                    eval2_str = str(eval2) if eval2 is not None else ""
                    f.write(f"{article}\t{eval1_str}\t{eval2_str}\n")
                else:
                    # 形式が異なる行があれば警告などを出すことも可能
                    print(f"Warning: Skipping malformed item in merged_data_list: {item}")

            # 正答率を書き込む
            f.write("\n---\n") # 区切り線
            f.write(f"Accuracy: {accuracy:.2f}%\n") # 小数点以下2桁まで表示

        print(f"Results successfully exported to '{output_file_path}'")
        return True
    except IOError as e:
        print(f"Error: Could not write to file '{output_file_path}'. {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
