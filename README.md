# SSAFY_MZ_PJT

> SSAFY 12기 대전 2반 MZ팀의 프로젝트입니다.

<br/>
<br/>

## 🍀 프로젝트 소개

Cinerium은 단순히 영화를 감상하는 것에서 그치지 않고, 사용자의 내적 성장을 돕는 것을 목표로 합니다. 주요 특징은 다음과 같습니다:

- **지적 성장 촉진**:
   - 영화 감상 후 토론과 리뷰를 통해 사용자의 비판적 사고력과 표현력을 향상시킵니다.


- **맞춤형 영화 추천**: 
   - 사용자의 취향과 선호도를 분석하여 개인화된 영화 추천 서비스를 제공합니다.


- **직관적인 UI/UX**: 
   - 사용자 친화적인 인터페이스로 영화 정보에 쉽게 접근할 수 있습니다.


- **AI 토론 파트너**: 
   - 다양한 성격의 AI 캐릭터와 영화에 대해 토론할 수 있는 독특한 기능을 제공합니다.


<br/>
<br/>

## 🥗 팀원 및 팀 소개
| 김재혁 | 정효원 |
|:------:|:------:|
|🐷 | 🐍|
| Back담당 | Front 담당 |
| [GitHub](https://github.com/Eonieoli) | [GitHub](https://github.com/chilly003) |


<br/>
<br/>

## 🍋 개발 환경과 기술 스택

### 개발 환경
- **프론트엔드**: Vue.js, Bootstrap
- **백엔드**: Django, OpenAI API, TMDB API
- **데이터베이스**: SQLite
- **버전 관리**: Git, GitHub
- **협업 도구**: Miro, Notion

### 기술 스택
- **프론트엔드**:

| HTML5 | CSS3 | JavaScript | Vue.js|
|:------:|:------:|:------:|:------:|
| ![html](https://github.com/user-attachments/assets/3e84d5c0-7d05-4928-a29c-2301d351a1e2) | ![cssss](https://github.com/user-attachments/assets/7470c575-2319-436a-a672-b12bace90911) | ![javasc](https://github.com/user-attachments/assets/9c146669-ef34-4c2f-941f-f4f6cbdc4897) | ![vue](https://github.com/user-attachments/assets/a047c33c-d56d-4541-ae00-e6a893ecadf6) |


- **백엔드**:

| Django |
|:------:|
| ![django](https://github.com/user-attachments/assets/03d8a947-10ba-4ba9-aba1-80c4d77000a6) |

- **데이터베이스**:


| SQLite | 
|:------:|
| ![다운로드 (1)](https://github.com/user-attachments/assets/e0c3d93b-60b4-459e-bfa2-5f4e0df840f7) |


<br/>
<br/>

## 💚 목표 서비스 구현

1. **사용자 관리 시스템**
   - 회원가입, 로그인, 로그아웃 기능
   - 개인 프로필 관리

2. **영화 추천 시스템**
   - 인기 영화 추천
   - 사용자 맞춤 영화 추천 (선호 태그 기반)
   - 필터링을 통한 개인화된 추천

3. **영화 정보 제공**
   - 상세 정보 제공 (감독, 배우, 예산, 수익, 개봉일 등)
   - 트레일러 및 관련 미디어 통합

4. **리뷰 및 평가 시스템**
   - 영화 리뷰 작성 및 조회
   - 댓글 기능을 통한 사용자 간 상호작용

5. **AI 토론 시스템**
   - 3가지 다른 성격의 AI 캐릭터와 영화에 대한 토론
   - 사용자의 비판적 사고 능력 향상 지원


<br/>
<br/>

## 🥦프로젝트 구조
```
project/
├── back/
│   ├── accounts             # 회원 기능
│   └── chats                # 토론 기능
│   └── CINERIUM             # main
│   └── movies               # 영화 기능
│   └── reviews              # 리뷰 기능 
│   └── media                # 유저 기본 이미지 경로
├── front/
│   ├── assets/              # 이미지, 폰트 등 정적 파일
│   ├── components/          # 재사용 가능한 UI 컴포넌트
│   ├── router/              # 각 페이지 주소
│   ├── stores/              # 기능별로 쓰이는 함수
│   ├── views/               # 각 페이지
│   index.css                # 전역 css 파일
├── .gitignore               # Git 무시 파일 목록
└── README.md                # 프로젝트 설명
```


<br/>
<br/>

## 🌳 ERD
![ERD_Cinerium (1)](https://github.com/user-attachments/assets/bfcb6f60-4d50-4e81-b973-be27368f6c77)


<br/>
<br/>

## 🌵 영화 추천 알고리즘 설명

- Cinerium의 영화 추천 알고리즘은 이용자가 회원가입 때 선택한 영화 장르를 기반으로 추천하고 있습니다.
- 만약 '로맨스', '애니메이션', '판타지' 라는 장르 3가지를 선택했다면 장르가 가장 많이 겹치는 영화 순으로 추천해드립니다.


<br/>
<br/>

## ☘️ 핵심 기능 설명

### 영화 추천 시스템
- 협업 필터링과 콘텐츠 기반 필터링을 결합한 하이브리드 추천 알고리즘 사용
- 사용자의 시청 기록, 평점, 선호 장르를 분석하여 개인화된 추천 제공
- 실시간 트렌드와 계절적 요인을 고려한 동적 추천 시스템

### AI 토론 기능
- GPT 기반의 2가지 다른 AI 캐릭터 구현 (예: 비평가형, 감성적 관객형)
- 사용자가 선택한 영화에 대해 각 AI 캐릭터와 심층적인 토론 진행
- 토론 내용을 바탕으로 사용자의 영화 이해도와 비판적 사고력 향상 지원

### 리뷰 시스템
- 별점, 텍스트 리뷰, 태그 기반의 다각적 평가 시스템
- 감정 분석을 통한 리뷰 요약 및 시각화
- 사용자 간 리뷰 추천 및 공유 기능


<br/>
<br/>

## 🥑 생성형 AI를 활용한 부분

Cinerium에서는 생성형 AI를 활용하여 다양한 성격의 AI 캐릭터를 구현합니다. 이들은 각기 다른 말투와 성격으로 사용자와 소통하며, 깊이 있는 영화 토론을 유도합니다.

### 기술 설명


<br/>
<br/>

## 🌿 보완점

- 리뷰 및 토론 생성 시 토론 데이터 저장 기능
- 검색 기능 심화
- 영화와 관련된 뉴스 컴포넌트 추가


<br/>
<br/>

## 📗 후기

### 김재혁 (M담당)
- 백엔드 개발 80% 이상 담당  
> 1학기 마지막 프로젝트를 하면서 깨달은 것이 너무 많습니다. 제가 스스로 이해하고 구현할 수 있는 것이 생각보다 적다는 것을 많이 느꼈고, 챗GPT에게 의존하는 스스로의 모습을 보며 회의감을 느끼기도 했습니다. 앞으로는 자신의 실력을 더 늘리기 위해 노력해야겠다고 생각했습니다! 그리고 디자인부터 시작해서 프론트의 80% 이상을 담당해준 효원이에게 너무너무 감사하고 있습니다. 앞으로도 파이팅!!

### 정효원 (Z담당)
- 프론트엔드 및 디자인 80% 이상 담당  
> 이번 프로젝트를 통해 많은 것을 배우고 알 수 있었습니다. 특히 아무리 프론트라도 백 구조를 잘 이해해야 제가 원하는 데이터를 불러 올 수 있더군요^^ 역시 디자인과 기술적인 면은 별개였습니다. 짧은 시간이었지만 재혁킹과 프로젝트할 수 있어서 다행이었습니다.(재혁킹의 오른팔로 활동할 수 있어 감사했습니다!!!) 그리고 첫 프로젝트를 통해 필요역량, 기술을 알 수 있었습니다. 싸피 2학기 시작 전 열심히 공부해야겠습니다.

