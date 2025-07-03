import os

def process_dictionaries_combined_from_paths(file_paths: list):
    
    combined_results = []

    for file_path in file_paths:
        file_name = os.path.basename(file_path) # ファイルパスからファイル名を取得

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read() # ファイルの内容全体を読み込む

            if file_name == "dictionary1.txt":
                # dictionary1.txt の処理ロジック
                # ここではfile_content_fetcherで取得した文字列と同じように扱える
                # io.StringIOは不要、contentを直接行ごとに処理
                for line in content.splitlines(): # contentをsplitlines()で行ごとに処理
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split('\t')
                    if len(parts) < 2:
                        continue

                    vocabulary_raw = parts[0]
                    sentiment_label = parts[1]

                    if vocabulary_raw.startswith('"') and vocabulary_raw.endswith('"'):
                        vocabulary = vocabulary_raw[1:-1]
                    else:
                        vocabulary = vocabulary_raw

                    if sentiment_label in ['n', 'p', 'e']:
                        combined_results.append([vocabulary, sentiment_label])

            elif file_name == "dictionary2.txt":
                # dictionary2.txt の処理ロジック
                for line in content.splitlines(): # contentをsplitlines()で行ごとに処理
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split('\t', 1)
                    if len(parts) < 2:
                        continue

                    evaluation_label = parts[0]
                    vocabulary = parts[1]

                    sentiment = None
                    if 'ネガ' in evaluation_label:
                        sentiment = 'n'
                    elif 'ポジ' in evaluation_label:
                        sentiment = 'p'
                    else:
                        continue

                    if "ない" in vocabulary:
                        continue

                    vocabulary_parts = [p for p in vocabulary.split(' ') if p]
                    num_syllables = len(vocabulary_parts)

                    if num_syllables >= 3:
                        continue
                    elif num_syllables == 2:
                        vocabulary = vocabulary_parts[0]
                    else:
                        vocabulary = vocabulary_parts[0] if vocabulary_parts

                    if not vocabulary:
                        continue

                    combined_results.append([vocabulary, sentiment])
            else:
                print(f"Warning: Unknown file format for {file_name}. Skipping.")

        except FileNotFoundError:
            print(f"Error: File not found at {file_path}. Please check the path and ensure the file exists.")
        except Exception as e:
            print(f"An error occurred while processing {file_path}: {e}")

    return combined_results

