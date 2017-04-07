# EC2 Automation Tools

EC2の運用を自動化するツールや、マネージド・サービスと連携するツール群

## 機能
1. 自動起動・停止機能
1. AMIバックアップ機能
1. EBSバックアップ機能
1. パッチ適用

### 自動起動・停止
- パラメータ
  - 基本：
  - タグ：
    - name: AutoShutdown, value: AUTO
    - name: AutoStartTime, value: <起動時刻 例) 10:00>
    - name: AutoShutdownTime, value: <停止時刻 例) 16:00>
  - トリガー
    - CloudWatch Events(CWE)で設定する。CWEはUTCで設定する必要があるため日本時間で平日に設定しようとするとトリガが9時間遅く始まり9時間遅く終わるので注意。月曜の9時以降にトリガが欲しいなら問題なさげ。
    - Cron式の例 <0 * ? * MON-FRI *>

### AMIバックアップ機能
- パラメータ
  - 基本：
  - タグ：
    - name: AmiBackup, value: ON
    - name: AmiPrefix, value: <わかりやすい名前で>
    - name: AmiGeneration, value: <世代数 例) 3>
  - トリガー
    - CloudWatch Events(CWE)で設定する。CWEはUTCで設定する必要があるため日本時間で平日に設定しようとするとトリガが9時間遅く始まり9時間遅く終わるので注意。月曜の9時以降にトリガが欲しいなら問題なさげ。
    - Cron式の例 <0 * ? * MON-FRI *>

### EBSバックアップ機能
- パラメータ
  - 基本：
  - タグ：
    - name: EbsBackup, value: ON
    - name: EbsPrefix, value: <わかりやすい名前で>
    - name: EbsGeneration, value: <世代数 例) 3>
  - トリガー
    - CloudWatch Events(CWE)で設定する。CWEはUTCで設定する必要があるため日本時間で平日に設定しようとするとトリガが9時間遅く始まり9時間遅く終わるので注意。月曜の9時以降にトリガが欲しいなら問題なさげ。
    - Cron式の例 <0 * ? * MON-FRI *>

