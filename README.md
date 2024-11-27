# SSAFY_MZ_PJT

> SSAFY 12기 대전 2반 MZ팀의 프로젝트입니다.

<br/>
<br/>

## 🍀 프로젝트 소개
![메인페이지](https://github.com/user-attachments/assets/b1a3d26d-9cfc-41ff-98d0-b7e25d90ea07)

### Cinerium은 단순히 영화를 감상하는 것에서 그치지 않고, 사용자의 내적 성장을 돕는 것을 목표로 합니다. 주요 특징은 다음과 같습니다:

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
   - 회원가입 시 인증 메일 구현
   - 회원가입 시 원하는 장르 태그로 선택
   - 개인 프로필 관리
   - 개인 프로필 수정 및 비밀번호 변경
   - 개인 프로필 내 팔로우, 팔로워 기능
   - 작성한 게시글, 찜한 영화, 좋아요한 게시글 확인 가능

2. **영화 추천 시스템**
   - 인기 영화, 상영 중인 영화 추천
   - 사용자 맞춤 영화 추천 (선호 태그 기반)
   - 필터링을 통한 개인화된 추천
   - 원하는 영화 찜 기능
   - 전체, 상세 페이지로 모든 영화 정보 확인 가능

3. **영화 정보 제공**
   - 상세 정보 제공 (감독, 배우, 예산, 수익, 개봉일 등)
   - 트레일러 및 관련 미디어 통합
   - 태그 기반 비슷한 영화 추천
   - footer에 다른 영화 사이트로 갈 수 있는 아이콘 설정

4. **리뷰 및 평가 시스템**
   - 리뷰 CRUD 구현
   - 영화 리뷰 작성 및 조회
   - 댓글 기능을 통한 사용자 간 상호작용
   - 리뷰 좋아요 기능으로 리뷰 반응 가능

5. **AI 토론 시스템**
   - 3가지 다른 성격의 AI 캐릭터와 영화에 대한 토론
   - 사용자의 비판적 사고 능력 향상 지원
   - 영화 내에서 몰랐던 지식이나 정보를 얻을 수 있음


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
│   index.css                # 메인 css

```



<br/>
<br/>

## 🥑 생성형 AI를 활용한 부분

Cinerium에서는 생성형 AI를 활용하여 다양한 성격의 AI 캐릭터를 구현합니다. 이들은 각기 다른 말투와 성격으로 사용자와 소통하며, 깊이 있는 영화 토론을 유도합니다.

### 기술 설명
1. 프로필 화면에서 캐릭터 생성 기능 구현
프론트엔드에서 사용자가 프로필 화면에서 새로운 캐릭터를 생성할 수 있도록 기능을 제공합니다. 사용자가 "새로운 생성" 버튼을 누르면 특정 함수가 트리거됩니다.

2. 캐릭터 선택 및 데이터 수집
캐릭터 생성 과정에서는 사용자가 캐릭터의 성격, 이름, 사진 등을 선택합니다. 선택된 데이터는 부모 컴포넌트로 emit 이벤트를 통해 전달됩니다. 부모 컴포넌트는 전달받은 데이터를 처리하고, 이를 기반으로 다음 단계(토큰 기반 AI 통신)로 넘깁니다.

3. AI 토큰과의 연결
AI 기능으로 이동하면 컴포넌트가 마운트되면서 필요한 정보를 초기화합니다. 이 과정에서:

   - 선택한 캐릭터 데이터를 기반으로 백엔드에 요청을 보냅니다.
   - 백엔드는 OpenAI 라이브러리를 사용하여 API 키를 통해 클라이언트를 생성합니다.
   - 초기화된 클라이언트에서 대화를 시작할 수 있도록 프롬프트를 설정합니다. 이 프롬프트는 사용자가 설정한 캐릭터의 성격 및 특징을 반영하여 AI가 캐릭터에 맞는 스타일로 대화하도록 설정됩니다.
   - 초기 대화에서는 AI가 먼저 인사를 건네도록 구현합니다.
  
4. 대화 흐름 관리
사용자가 AI의 첫 응답에 답변하면 대화가 시작됩니다. 이후 AI와 사용자는 질문과 답변을 반복하며 대화를 이어나갈 수 있도록 양방향 통신이 지원됩니다. 이 과정은 대화 형식으로, 자연스러운 대화 경험을 제공하도록 설계됩니다.


### 코드

```python
def chat(request):
    if request.method == "POST":
        try:
            # 세션에서 캐릭터 정보 가져오기
            session = request.session

            # POST 요청에서 데이터 추출
            body = json.loads(request.body)
            user_message = body.get("message", None)

            # 대화 초기화: name과 personality 설정
            if "name" in body and "personality" in body:
                session["name"] = body["name"]
                session["personality"] = body["personality"]
                session.save()  # 세션 저장
                ai_response = f"안녕하세요, 저는 {body['name']}입니다. 어떤 영화에 대해서 토론하고 싶으신가요?"
                return JsonResponse({"ai_response": ai_response}, status=200)

            # 세션에서 name과 personality 가져오기
            ai_name = session.get("name", "MovieBot")
            ai_personality = session.get("personality", "재미있고 영화에 박식한")

            # 캐릭터 설정
            ai_context = (
                f"너는 {ai_name}이야. {ai_personality} 성격을 가지고 있고, "
                "사용자와 영화에 대해 유익하고 재미있는 대화를 나누는 게 목표야."
                "너는 AI가 아니라 사람이야. 영화를 너무너무 좋아하는 사람이지."
                "누가 너한테 AI인지 사람인지 물어본다면 사람이라고 대답해. 너는 사람이야."
                "너는 최대한 친근하게 말하는 아주 친절한 사람이야."
            )

            # 메시지 배열 설정
            messages = [
                {"role": "system", "content": ai_context},
            ]

            # 사용자 메시지가 없는 경우 AI가 먼저 인사
            if user_message is None:
                messages.append(
                    {"role": "assistant", "content": f"안녕하세요, 저는 {ai_name}입니다. 어떤 영화에 대해서 토론하고 싶으신가요?"}
                )
            else:
                messages.append({"role": "user", "content": user_message})

            # OpenAI API 호출
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # 또는 "gpt-3.5-turbo"
                messages=messages,
                temperature=0.7,
                max_tokens=500,
            )

            # AI 응답 추출
            ai_response = response.choices[0].message.content

            # 응답 반환
            return JsonResponse({"ai_response": ai_response}, status=200)

        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    else:
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)
```



<br/>
<br/>

## 🌿 보완점

- 리뷰 및 토론 생성 시 토론 데이터 저장 기능
- 검색 기능 심화 -> 크롤링이나 모든 DB를 프론트로 보내 연관 글자가 있는 모든 영화를 볼 수 있게 하기
- 영화와 관련된 뉴스 컴포넌트 추가
- 개인 프로필 불러오기 및 비밀 번호 변경 구현
-  게시판 CRUD 중 삭제와 수정 기능 미구현

개인 프로필의 원인
- 찾는 중..

게시만 삭제와 수정 기능의 미구현 원인
```python
# reviews/urls.py

from django.urls import path, include
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.all_review_list, name='all_review_list'), # 전체 리뷰 조회
    path('<int:movie_pk>/', views.movie_review_list_create, name='movie_review_list_create'), # 특정 영화에 대한 리뷰 리스트 조회 (GET) 및 특정 영화에 대한 리뷰 작성 (POST)
    path('<int:review_pk>/', views.review_detail, name='review_detail'), # 리뷰 상세 조회, 리뷰 삭제, 리뷰 수정
]
```
백엔드 쪽에서는 어떤 pk값인지 구분이 가능하지만 프론트 쪽에서는 영화의 pk이인지 리뷰의 pk인지 구분할 수 없다. 하나 더 배웠다!!


<br/>
<br/>

## 📗 후기
> 처음부터 완벽하게 구현하는 것을 추구하기보다는 기본적인 것부터 구현하면서 백엔드와 프론트엔드를 기능별로 맞춰가는 방식으로 갔으면 더 좋았을 것 같습니다.

### 김재혁 (M담당)
- 백엔드 개발 80% 이상 담당  
> 1학기 마지막 프로젝트를 하면서 깨달은 것이 너무 많습니다. 제가 스스로 이해하고 구현할 수 있는 것이 생각보다 적다는 것을 많이 느꼈고, 챗GPT에게 의존하는 스스로의 모습을 보며 회의감을 느끼기도 했습니다. 앞으로는 자신의 실력을 더 늘리기 위해 노력해야겠다고 생각했습니다! 그리고 디자인부터 시작해서 프론트의 80% 이상을 담당해준 효원이에게 너무너무 감사하고 있습니다. 앞으로도 파이팅!!

### 정효원 (Z담당)
- 프론트엔드 및 디자인 80% 이상 담당  
> 이번 프로젝트를 통해 많은 것을 배우고 알 수 있었습니다. 특히 아무리 프론트라도 백 구조를 잘 이해해야 제가 원하는 데이터를 불러 올 수 있더군요^^ 역시 디자인과 기술적인 면은 별개였습니다. 짧은 시간이었지만 재혁킹과 프로젝트할 수 있어서 다행이었습니다.(재혁킹의 오른팔로 활동할 수 있어 감사했습니다!!!) 그리고 첫 프로젝트를 통해 필요역량, 기술을 알 수 있었습니다. 싸피 2학기 시작 전 열심히 공부해야겠습니다.

