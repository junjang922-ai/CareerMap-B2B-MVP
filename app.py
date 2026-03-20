import streamlit as st
import pandas as pd
import time
import datetime

st.set_page_config(page_title="CareerMap B2B Enterprise", page_icon="🏢", layout="wide")

st.markdown("""
    <style>
    @import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/static/pretendard.css");
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif;
        color: #1E293B;
    }
    
    .stApp { background-color: #F1F5F9; }
    
    .dashboard-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 24px;
        transition: all 0.2s ease-in-out;
    }
    .dashboard-card:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        transform: translateY(-2px);
    }
    
    .metric-label {
        font-size: 13px;
        color: #64748B;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }
    
    .metric-value {
        font-size: 32px;
        font-weight: 800;
        color: #0F172A;
        display: flex;
        align-items: baseline;
        gap: 12px;
    }
    
    .metric-delta-up { font-size: 14px; color: #10B981; font-weight: 600; padding: 2px 8px; background-color: #D1FAE5; border-radius: 12px; }
    .metric-delta-down { font-size: 14px; color: #EF4444; font-weight: 600; padding: 2px 8px; background-color: #FEE2E2; border-radius: 12px; }
    
    .badge-safe { color: #047857; background-color: #A7F3D0; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; }
    .badge-warn { color: #B45309; background-color: #FDE68A; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; }
    .badge-danger { color: #B91C1C; background-color: #FECACA; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; }
    
    .section-title {
        font-size: 20px;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 16px;
        padding-bottom: 8px;
        border-bottom: 2px solid #E2E8F0;
    }
    
    .ai-button > button {
        background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 16px 24px !important;
        box-shadow: 0 4px 14px rgba(79, 70, 229, 0.4) !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .ai-button > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.6) !important;
    }
    
    .progress-label {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        font-weight: 600;
        color: #475569;
        margin-bottom: 4px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='color:#1E40AF; font-weight:900;'>CareerMap Biz</h2>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:14px; color:#64748B; margin-bottom:24px;'>다이캐스탈 코리아 인사본부</div>", unsafe_allow_html=True)
    
    menu = st.radio("Workspaces", ["📊 컴플라이언스 대시보드", "⚖️ 지원자 리스크 평가", "📑 비자 행정 & AI 서류"], label_visibility="collapsed")
    
    st.divider()
    st.markdown("""
        <div style='background-color:#EFF6FF; padding:16px; border-radius:12px; border:1px solid #BFDBFE;'>
            <div style='font-size:12px; color:#1D4ED8; font-weight:700; margin-bottom:4px;'>E-7 채용 쿼터 현황</div>
            <div style='font-size:24px; color:#1E3A8A; font-weight:900;'>2명 남음</div>
            <div style='font-size:12px; color:#3B82F6; margin-top:4px;'>총 허용 8명 중 6명 채용 완료</div>
        </div>
    """, unsafe_allow_html=True)

if menu == "📊 컴플라이언스 대시보드":
    st.markdown("<div class='section-title'>인사 컴플라이언스 통합 대시보드</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B; margin-bottom:24px;'>실시간 내국인 고용보험 데이터와 연동되어 외국인 채용 가능 인원을 산출합니다.</p>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='dashboard-card'><div class='metric-label'>내국인 고용보험 가입자</div><div class='metric-value'>42 명 <span class='metric-delta-up'>↑ 3</span></div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='dashboard-card'><div class='metric-label'>총 E-7 비자 허용 쿼터</div><div class='metric-value'>8 명 <span class='metric-delta-up'>↑ 1</span></div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='dashboard-card'><div class='metric-label'>현재 E-7 고용 인원</div><div class='metric-value'>6 명 <span class='metric-delta-down'>- 0</span></div></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='dashboard-card' style='border:2px solid #3B82F6; background-color:#F8FAFC;'><div class='metric-label' style='color:#2563EB;'>추가 채용 가능 쿼터</div><div class='metric-value' style='color:#1D4ED8;'>2 명</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<div class='progress-label'><span>쿼터 소진율</span><span>75%</span></div>", unsafe_allow_html=True)
    st.progress(75)
    st.markdown("</div>", unsafe_allow_html=True)

    col_alert1, col_alert2 = st.columns(2)
    with col_alert1:
        st.markdown("<div class='section-title'>🚨 시급한 리스크 알림</div>", unsafe_allow_html=True)
        st.error("생산본부 '응우옌 반 안' 직원의 E-7 체류 기간이 30일 뒤 만료됩니다. 즉시 연장 수속이 필요합니다.")
        st.warning("영업본부 '박준형' 주임 퇴사로 인해, 추가 퇴사자 발생 시 외국인 채용 쿼터가 1명 감소할 수 있습니다.")
    
    with col_alert2:
        st.markdown("<div class='section-title'>📈 최근 매칭 트렌드</div>", unsafe_allow_html=True)
        st.info("베트남 국적, 경제학 전공 우수 유학생 12명이 우리 기업을 관심 직장으로 등록했습니다.")
        st.success("지자체 지역특화형 비자 F-2-R 배정 심사가 시작되었습니다. 지원자를 검토하세요.")

elif menu == "⚖️ 지원자 리스크 평가":
    st.markdown("<div class='section-title'>지원자 비자 적격성 & 실무 역량 리포트</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='dashboard-card' style='display:flex; justify-content:space-between; align-items:center; border-left:6px solid #2563EB;'>
        <div style='display:flex; align-items:center; gap:20px;'>
            <div style='width:64px; height:64px; background-color:#E2E8F0; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:24px;'>👩‍🎓</div>
            <div>
                <h3 style='margin:0; font-weight:800; color:#0F172A;'>해원 (Haewon) <span style='font-size:14px; font-weight:500; color:#64748B;'>베트남 · 25세</span></h3>
                <p style='margin:4px 0 0 0; color:#475569; font-size:14px;'>지원 포지션: <b>해외영업 (베트남 담당)</b> / 연세대 경제학과 졸업예정</p>
            </div>
        </div>
        <div style='text-align:right;'>
            <div style='font-size:13px; color:#64748B; font-weight:700; margin-bottom:4px;'>AI 산출 E-7 비자 발급 확률</div>
            <div style='font-size:36px; font-weight:900; color:#059669; line-height:1;'>94% <span class='badge-safe' style='vertical-align:middle;'>안정권</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.2, 1])
    
    with col_l:
        st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:16px; font-weight:800; margin-bottom:16px;'>출입국 지침 컴플라이언스 점검</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><b>직무-전공 연관성</b> <span class='badge-safe'>통과</span></div>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:13px; color:#64748B; margin-bottom:16px;'>해외영업 직무코드(2742)와 경제학 전공이 출입국 매뉴얼 상 일치함.</p>", unsafe_allow_html=True)
        
        st.markdown("<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><b>임금 요건 (GNI 80% 이상)</b> <span class='badge-warn'>주의 요망</span></div>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:13px; color:#64748B; margin-bottom:16px;'>제시 연봉 3,300만 원. 전년도 GNI 변동 시 반려 위험 존재. 3,400만 원으로 상향 권고.</p>", unsafe_allow_html=True)
        
        st.markdown("<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><b>불법 체류 및 범칙금 이력</b> <span class='badge-safe'>클린</span></div>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:13px; color:#64748B; margin-bottom:0;'>시간제 취업 위반 이력 등 행정 결격 사유 없음.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_r:
        st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:16px; font-weight:800; margin-bottom:16px;'>실무 역량 검증 리포트</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='progress-label'><span>비즈니스 한국어 (TOPIK 6급)</span><span>95/100</span></div>", unsafe_allow_html=True)
        st.progress(95)
        
        st.markdown("<div class='progress-label' style='margin-top:12px;'><span>문서 작성 역량 (이메일/기획서)</span><span>85/100</span></div>", unsafe_allow_html=True)
        st.progress(85)
        
        st.markdown("<div class='progress-label' style='margin-top:12px;'><span>한국 기업 문화 적응력</span><span>90/100</span></div>", unsafe_allow_html=True)
        st.progress(90)
        
        st.markdown("<div style='background-color:#F1F5F9; padding:12px; border-radius:8px; margin-top:20px; font-size:13px; color:#475569;'><b>종합 의견:</b> 한국인 신입 사원과 동일한 수준의 소통이 가능하며, 현지 벤더사 관리 실무에 즉각 투입 가능한 S급 인재입니다.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "📑 비자 행정 & AI 서류":
    st.markdown("<div class='section-title'>양방향 행정 트래커 및 고용사유서 생성</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top:0; color:#0F172A;'>서류 준비 진척도: 해원 (해외영업 신규 채용)</h4>", unsafe_allow_html=True)
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("<div style='font-weight:700; margin-bottom:12px; color:#334155;'>구직자 측 서류 (수합 완료)</div>", unsafe_allow_html=True)
        st.progress(100)
        st.checkbox("여권 및 외국인등록증 사본", value=True, disabled=True)
        st.checkbox("학위증명서 (아포스티유 인증)", value=True, disabled=True)
        st.checkbox("성적증명서 및 TOPIK 성적표", value=True, disabled=True)
        
    with col_t2:
        st.markdown("<div style='font-weight:700; margin-bottom:12px; color:#334155;'>기업 측 서류 (진행 중)</div>", unsafe_allow_html=True)
        st.progress(60)
        st.checkbox("사업자등록증 및 등기부등본", value=True)
        st.checkbox("납세증명서 및 고용보험 가입자 명부", value=True)
        st.checkbox("표준 근로계약서 원본", value=False)
        st.checkbox("외국인 고용사유서 (심사 핵심 서류)", value=False)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='dashboard-card' style='background: linear-gradient(to right, #F8FAFC, #EFF6FF); border: 1px solid #BFDBFE;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top:0; color:#1E40AF;'>✨ E-7 고용사유서 AI 자동 생성기</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px; color:#475569;'>가장 까다로운 고용사유서를 기업의 산업 분류와 구직자의 스펙을 교차 분석하여 법무부 지침에 완벽하게 부합하는 논리로 즉시 작성합니다.</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="ai-button">', unsafe_allow_html=True)
    if st.button("AI 고용사유서 초안 생성 시작"):
        with st.status("AI가 출입국 심사 지침을 분석하여 문서를 작성 중입니다...", expanded=True) as status:
            st.write("1. 기업의 수출 실적 및 채용 배경 분석 중...")
            time.sleep(1)
            st.write("2. 내국인 채용 노력 입증 논리 구성 중...")
            time.sleep(1)
            st.write("3. 외국인 지원자의 필수 역량 및 도입 효과 작성 중...")
            time.sleep(1)
            status.update(label="고용사유서 작성 완료!", state="complete", expanded=False)
        
        st.markdown("<div style='background-color:#FFFFFF; border:1px solid #E2E8F0; padding:24px; border-radius:12px; margin-top:16px;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center; margin-bottom:24px;'>외국인 고용의 필요성 및 활용 계획서</h4>", unsafe_allow_html=True)
        
        doc_text = """
<b>1. 기업 현황 및 외국인 도입 배경</b>
당사(다이캐스탈 코리아)는 자동차 부품 제조 및 수출을 영위하는 기업으로, 최근 베트남 완성차 벤더사와의 직계약 물량이 전년 대비 150% 급증하였습니다. 이에 현지어 능통과 비즈니스 협상력을 갖춘 전담 인력이 시급합니다.

<b>2. 내국인 고용 노력 및 한계</b>
해당 직무 수행을 위해 워크넷 및 국내 구인 플랫폼을 통해 6개월간 내국인 채용을 진행하였으나, 베트남 원어민 수준의 어학 능력과 경제학적 시장 분석 역량을 동시에 충족하는 인재를 당사가 위치한 비수도권에서 확보하는 것은 현실적으로 불가능했습니다.

<b>3. 해당 외국인 채용의 당위성</b>
지원자 해원은 연세대학교 경제학과 출신으로 거시 경제 분석 능력을 갖추고 있으며, 최고 등급인 TOPIK 6급을 보유하여 당사 실무진과의 업무 소통에 전혀 지장이 없습니다. 베트남 현지 기업과의 커뮤니케이션 리스크를 제거하고 수출 실적을 극대화할 대체 불가 인력이므로 E-7 사증 발급을 강력히 요청합니다.
        """
        st.markdown(doc_text, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        c_btn1, c_btn2 = st.columns(2)
        with c_btn1:
            st.button("💾 MS Word (.docx) 다운로드", use_container_width=True)
        with c_btn2:
            st.button("🔄 논리 강도 조절 및 재작성", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
