# chats/views.py

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.conf import settings

# OpenAI 인스턴스 생성
client = OpenAI(api_key=settings.OPENAI_API_KEY)  # OpenAI API 키 설정

@csrf_exempt
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
