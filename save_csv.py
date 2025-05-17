import csv
import os

def save_to_csv(data):
    os.makedirs("output", exist_ok=True)  # outputディレクトリを作成（存在してなければ）
    output_path = os.path.join("output", "results.csv")
    
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # ヘッダー
        writer.writerow(["会社", "特徴", "雇用形態", "初年度年収"])
        # データ
        writer.writerows(data)

    print(f"📁 結果を保存しました: {output_path}")
