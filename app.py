import streamlit as st
import pandas as pd
import time
import datetime

# ==============================================================================
# 1. 페이지 설정 및 B2B용 CSS 디자인 시스템
# ==============================================================================
st.set_page_config(page_title="CareerMap B2B Enterprise", page_icon="🏢", layout="wide")

st.markdown("""
    <style>
    @import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/static/pretendard.css");
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif;
        color: #2C3E50;
    }
    
    /* B2B 기업용 테마 (신뢰감을 주는 Navy & Blue) */
    .stApp { background-color: #F8FAFC; }
    
    .card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
        margin-bottom: 20px;
    }
    
    .metric-title {
        font-size: 14px;
        color: #64748B;
        font-weight: 600;
        margin-bottom: 8px;
    }
    
    .metric-value {
        font-size: 28px;
        font-weight: 800;
        color: #0F172A;
    }
    
    .risk-safe { color: #059669; font-weight: bold; background-color: #D1FAE5; padding: 4px 8px; border-radius: 6px; font-size: 13px; }
    .risk-warn { color: #D97706; font-weight: bold; background-color: #FEF3C7; padding: 4px 8px; border-radius: 6px; font-size: 13px; }
    .risk-danger { color: #DC2626; font-weight: bold; background-color: #FEE2E2; padding: 4px 8px; border-radius: 6px; font-size: 13px; }
    
    .btn-ai-generate > button {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. 사이드바 (B2B 메뉴 네비게이션)
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color:#1E3A8A;'>🏢 CareerMap Biz</h2>", unsafe_allow_html=True)
    st.caption("다이캐스탈 코리아 인사팀 (관리자)")
    st.divider()
    menu = st.radio("업무 메뉴", ["📊 홈: 컴플라이언스 대시보드", "⚖️ 지원자 리스크 평가", "📑 E-7 비자 행정 트래커"])
    st.divider()
    st.info("💡 이번 달 E-7 채용 가능 쿼터가 **2명** 남았습니다.")

# ==============================================================================
# 화면 1: 기업용 홈 대시보드 (컴플라이언스 지표)
# ==============================================================================
if menu == "📊 홈: 컴플라이언스 대시보드":
    st.title("📊 인사 컴플라이언스 및 채용 대시보드")
    st.caption("내국인 고용 보험자 수 대비 외국인 채용 가능 쿼터를 실시간으로 모니터링합니다.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='card'><div class='metric-title'>고용보험 가입 내국인 수</div><div class='metric-value'>42 명</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'><div class='metric-title'>E-7 비자 허용 쿼터 (20%)</div><div class='metric-value'>8 명</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'><div class='metric-title'>현재 고용 중인 E-7 인원</div><div class='metric-value'>6 명</div></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='card' style='border: 2px solid #3B82F6;'><div class='metric-title' style='color:#3B82F6;'>추가 채용 가능 인원</div><div class='metric-value'>2 명</div></div>", unsafe_allow_html=True)

    st.markdown("### 🚦 E-7 채용 쿼터 게이지")
    # 직관적인 프로그레스 바 (게이지 역할)
    quota_percent = (6 / 8) * 100
    st.progress(int(quota_percent))
    st.caption(f"현재 법정 허용 쿼터의 **{quota_percent}%** 를 사용 중입니다. (추가 채용 2명 가능)")

    st.write("")
    st.markdown("### 🔔 리스크 알림 (Red Flag)")
    st.error("🚨 **[체류 만료 경고]** 생산본부 '응우옌 반 안' 직원의 E-7 비자가 30일 뒤 만료됩니다. (갱신 서류 준비 필요)")
    st.warning("⚠️ **[컴플라이언스 알림]** 내국인 직원 2명 퇴사 시, E-7 허용 쿼터가 1명 감소합니다. 채용 계획에 유의하세요.")

# ==============================================================================
# 화면 2: 지원자 리스크 평가 리포트
# ==============================================================================
elif menu == "⚖️ 지원자 리스크 평가":
    st.title("⚖️ 지원자 비자 적격성 & 리스크 평가")
    st.caption("출입국 지침과 데이터에 기반하여 후보자의 비자 발급 확률과 행정 리스크를 사전 검증합니다.")
    
    st.markdown("""
    <div class='card' style='display:flex; justify-content:space-between; align-items:center;'>
        <div>
            <h3 style='margin:0;'>해원 (Haewon) <span style='font-size:16px; font-weight:normal; color:#64748B;'>| 베트남 · 25세</span></h3>
            <p style='margin:5px 0 0 0; color:#475569;'>지원 직무: <b>해외영업 (베트남 파트)</b> / 연세대 경제학과 졸업예정</p>
        </div>
        <div style='text-align:right;'>
            <div style='font-size:12px; color:#64748B;'>E-7 비자 발급 예측 확률</div>
            <div style='font-size:32px; font-weight:900; color:#059669;'>94% <span style='font-size:14px;'>안정권</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🚨 필수 요건 리스크 진단 (Compliance Check)")
    
    c_risk1, c_risk2, c_risk3 = st.columns(3)
    with c_risk1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<b>1. 직무 - 전공 연관성</b>", unsafe_allow_html=True)
        st.markdown("<span class='risk-safe'>🟢 통과 (위험도 Low)</span>", unsafe_allow_html=True)
        st.caption("해외영업 직무와 경제학 전공 연관성이 출입국 지침에 부합함.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c_risk2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<b>2. 임금 요건 (GNI 80%)</b>", unsafe_allow_html=True)
        st.markdown("<span class='risk-warn'>🟡 주의 (위험도 Mid)</span>", unsafe_allow_html=True)
        st.caption("제시 연봉 3,300만 원. 전년도 GNI 발표치에 따라 아슬아슬할 수 있음. 3,400만 원 상향 권장.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c_risk3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<b>3. 과거 출입국 위반 기록</b>", unsafe_allow_html=True)
        st.markdown("<span class='risk-safe'>🟢 클린 (위험도 Low)</span>", unsafe_allow_html=True)
        st.caption("시간제 취업(S-3) 위반 기록 및 기타 범칙금 이력 없음.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("#### 📊 실무 역량 표준화 리포트")
    st.info("💡 **한국 기업 문화 핏(Fit):** 동아리 기장 역임으로 조직 적응력 상위 15%. \n\n 💡 **소통 역량:** TOPIK 6급 및 비즈니스 이메일 작성 테스트 통과 (실무 투입 즉시 가능)")
    
    st.button("✅ 리스크 검토 완료 (해당 지원자 채용 진행 및 행정 수속 시작)", type="primary", use_container_width=True)

# ==============================================================================
# 화면 3: 비자 행정 진행률 트래커 및 고용사유서 AI 자동 생성
# ==============================================================================
elif menu == "📑 E-7 비자 행정 트래커":
    st.title("📑 양방향 비자 행정 & 서류 트래커")
    st.caption("채용 확정자의 비자 서류 수합 현황을 실시간으로 확인하고, 가장 어려운 고용사유서를 AI로 생성합니다.")
    
    st.markdown("### [진행 중] 해원 님 E-7 비자 신규 발급")
    
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        st.markdown("#### 🧑‍🎓 구직자 준비 서류 (진행률 100%)")
        st.progress(100)
        st.checkbox("여권 사본 및 외국인등록증", value=True, disabled=True)
        st.checkbox("학위증명서 (아포스티유 완료)", value=True, disabled=True)
        st.checkbox("성적증명서", value=True, disabled=True)
        st.checkbox("TOPIK 성적표", value=True, disabled=True)
        
    with col_p2:
        st.markdown("#### 🏢 기업 준비 서류 (진행률 60%)")
        st.progress(60)
        st.checkbox("사업자등록증 및 법인등기부등본", value=True)
        st.checkbox("고용보험 가입자 명부", value=True)
        st.checkbox("납세증명서 (국세/지방세)", value=True)
        st.checkbox("고용계약서 원본 (연봉 및 직무 명시)", value=False)
        st.checkbox("외국인 고용사유서 (핵심 서류)", value=False)

    st.divider()
    
    st.markdown("### ✨ E-7 외국인 고용사유서 AI 자동 생성")
    st.write("출입국 심사관이 가장 까다롭게 보는 고용사유서. 직무 데이터와 지원자 스펙을 연동하여 지침에 맞춘 초안을 10초 만에 작성합니다.")
    
    st.markdown('<div class="btn-ai-generate">', unsafe_allow_html=True)
    if st.button("🚀 AI 고용사유서 초안 생성하기"):
        with st.spinner("법무부 E-7 심사 지침과 지원자 데이터를 매칭하여 논리를 구성 중입니다..."):
            time.sleep(2)
        
        generated_doc = """
[외국인 고용의 필요성 및 기대효과]

1. 기업 현황 및 채용 배경
당사(다이캐스탈 코리아)는 자동차 부품 제조 및 베트남 수출을 주력으로 하는 지역 우수 중소기업입니다. 최근 베트남 현지 완성차 업체와의 직계약 물량이 전년 대비 150% 급증함에 따라, 현지어 능통과 비즈니스 협상력을 동시에 갖춘 해외영업 전문 인력이 시급한 상황입니다. 

2. 내국인 채용의 한계
해당 직무를 위해 워크넷 등 범용 구인망을 통해 6개월간 내국인 채용을 시도하였으나, 베트남어 원어민 수준의 구사력과 경제학적 시장 분석 역량을 동시에 갖춘 인재를 비수도권 지역에서 확보하는 것은 현실적으로 불가능했습니다.

3. 해당 외국인 채용 사유
지원자 '해원'은 연세대학교에서 경제학을 전공하며 거시 경제 흐름에 대한 이해도가 높고, TOPIK 6급을 보유하여 당사 한국인 실무진과의 완벽한 업무 소통이 가능합니다. 특히 베트남 원어민으로서 현지 벤더사와의 무역 장벽을 해소하고 수출 매출 증대에 즉각적이고 결정적인 기여를 할 수 있는 대체 불가능한 인재이기에 E-7 비자 발급을 강력히 요청합니다.
        """
        st.success("✅ 고용사유서 초안이 생성되었습니다. 내용 확인 후 워드 파일로 다운로드하세요.")
        st.text_area("고용사유서 생성 결과 (편집 가능)", value=generated_doc, height=250)
        
        c_btn1, c_btn2, c_btn3 = st.columns([1, 1, 2])
        with c_btn1:
            st.button("💾 Word로 다운로드")
        with c_btn2:
            st.button("🔄 내용 재조정")
    st.markdown('</div>', unsafe_allow_html=True)
