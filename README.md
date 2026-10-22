# 1. 문서 개요
S1-1의 커머스 데이터 분석 활동을 기반으로 작성한 보고서입니다. Online Retail 데이터를 활용해 결측값과 이상치를 확인하고, 판매 수량·단가·매출을 시각화합니다.

# 2. xlsx => csv 변환
```powershell
New-Item -ItemType Directory -Force data/processed
python src/init/change_csv.py
```

변환 결과는 data/processed/online_retail.csv에 저장됩니다.

# 3. 분석 실행

- src/pipeline.py => 데이터 로딩, 결측값 처리, 판매 데이터 추출, IQR 기준 이상치 탐지
- notebooks/analysis_report.ipynb => 분석 과정과 차트별 해석
- figures/ => 실행 중 생성되는 차트 이미지

# 4. 주요 분석 내용

- 열별 결측값 개수와 처리 전후 비교
- 판매 수량 분포, 단가 상자그림, 수량과 단가의 관계
- 월별 매출 추이와 국가별 매출 상위 10개
- 수량·단가·매출의 Min–Max 정규화 및 원본 값 비교

매출 분석에는 수량과 단가가 양수이고 취소 번호가 아닌 데이터를 사용합니다. 정규화 결과는 별도 데이터로 만들며, 기존 매출 차트는 원래 금액을 기준으로 표시합니다.

# 5. 외부 데이터 출처

https://archive.ics.uci.edu/dataset/352/online+retail

https://www.kaggle.com/datasets/zalando-research/fashionmnist?utm_source=chatgpt.com