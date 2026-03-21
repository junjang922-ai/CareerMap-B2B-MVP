import streamlit as st
import pandas as pd
import time

# ==============================================================================
# 1. 페이지 설정 및 B2C 급 프리미엄 CSS 디자인 시스템
# ==============================================================================
st.set_page_config(page_title="CareerMap Biz Enterprise", page_icon="🏢", layout="wide")

st.markdown("""
    <style>
    @import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/static/pretendard.css");
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif;
        color: #1E293B;
    }
    
    .stApp { background-color: #F1F5F9; }
    
    /* [B2C 디자인 반영] 사이드바 메뉴 스타일링 */
    section[data-testid="stSidebar"] {
        background-color: #F1F5F9;
        padding-top: 20px;
    }
    div[data-testid="stSidebarNav"] {
        background-color: transparent;
    }
    /* 라디오 버튼을 카드로 변환 */
    div[data-testid="stWidgetLabel"] {
        display: none;
    }
    div[data-testid="stSidebarNav"] li, div[data-testid="stSidebarNav"] ul {
        background-color: transparent !important;
    }
    
    /* 실제 라디오 인풋 스타일링 */
    div.st-emotion-cache-1n76uvr p {
        font-weight: 600;
        color: #1E293B;
    }
    
    /* 사이드바 사용자 정보 */
    .sidebar-user-info {
        background-color: #FFFFFF;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-bottom: 24px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    
    /* 사이드바 선택된 메뉴 강조 */
    div[data-testid="stSidebarNav"] li a[aria-current="page"] {
        background-color: #FFFFFF;
        border: 1px solid #BFDBFE;
        border-left: 4px solid #3B82F6;
        color: #1D4ED8;
        font-weight: 700;
        border-radius: 8px;
    }

    /* [B2C 디자인 반영] 전체 페이지를 감싸는 커다란 메인 통합 카드 */
    .b2c-main-card {
        background-color: #FFFFFF;
        padding: 32px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
    }
    
    /* 메인 카드 내 섹션 구분선 */
    .b2c-section-divider {
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 32px;
        padding-bottom: 32px;
    }
    
    /* 타이포그래피 */
    .b2c-page-title {
        font-size: 24px;
        font-weight: 900;
        color: #0F172A;
        margin-bottom: 8px;
    }
    .b2c-page-subtitle {
        font-size: 14px;
        color: #64748B;
        margin-bottom: 32px;
    }
    .b2c-section-title {
        font-size: 18px;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 16px;
    }
    
    /* 지표 카드 (메인 카드 내부에 배치) */
    .b2c-stat-card {
        background-color: #F8FAFC;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
    }
    .metric-label { font-size: 13px; color: #64748B; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
    .metric-value { font-size: 28px; font-weight: 800; color: #0F172A; display: flex; align-items: baseline; gap: 8px; }
    .metric-delta-up { font-size: 12px; color: #10B981; font-weight: 600; padding: 2px 6px; background-color: #D1FAE5; border-radius: 10px; }
    
    /* 인재 추천 카드 시스템 (핵심 수정) */
    .candidate-grid {
        display: flex;
        gap: 20px;
    }
    .candidate-card {
        flex: 1;
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .candidate-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .candidate-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
    }
    .candidate-avatar {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        object-fit: cover;
    }
    .visa-badge {
        font-size: 12px;
        font-weight: 700;
        padding: 6px 12px;
        border-radius: 8px;
    }
    .visa-badge-safe { color: #047857; background-color: #A7F3D0; }
    .candidate-name { font-size: 18px; font-weight: 800; color: #0F172A; margin: 0 0 4px 0; }
    .candidate-uni { font-size: 13px; color: #64748B; margin: 0 0 16px 0; }
    .candidate-spec-item {
        background-color: #F1F5F9;
        padding: 10px;
        border-radius: 8px;
        font-size: 12px;
        color: #475569;
        margin-bottom: 8px;
    }
    .action-button {
        display: block;
        width: 100%;
        background-color: #2563EB;
        color: white;
        border: none;
        padding: 12px;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        text-align: center;
        margin-top: 16px;
    }
    
    /* 뱃지 및 테이블 */
    .badge-check { color: #047857; background-color: #A7F3D0; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700; }
    .badge-warn { color: #B45309; background-color: #FEF3C7; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700; }
    .table-container { background-color: transparent; padding: 0; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. 사이드바 (B2C 디자인 반영)
# ==============================================================================
with st.sidebar:
    # 사용자 정보 카드 (B2C 메뉴 스타일 반영)
    st.markdown("""
        <div class='sidebar-user-info'>
            <div style='font-size:12px; color:#64748B; font-weight:600;'>기업 회원</div>
            <div style='font-size:18px; color:#0F172A; font-weight:900;'>다이캐스탈 코리아</div>
            <div style='font-size:13px; color:#475569;'>인사본부</div>
        </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio("Navigation", ["📊 채용 및 컴플라이언스", "⚖️ 지원자 비자 평가", "📑 비자 행정 & AI 서류"], label_visibility="collapsed")
    
    st.divider()
    
    sidebar_status = (
        "<div style='background-color:#FFFFFF; padding:16px; border-radius:12px; border:1px solid #E2E8F0;'>"
        "<div style='font-size:12px; color:#1D4ED8; font-weight:700; margin-bottom:4px;'>E-7 채용 쿼터 현황</div>"
        "<div style='font-size:24px; color:#1E3A8A; font-weight:900;'>2명 남음</div>"
        "<div style='font-size:12px; color:#3B82F6; margin-top:4px;'>총 허용 8명 중 6명 채용 완료</div>"
        "</div>"
    )
    st.markdown(sidebar_status, unsafe_allow_html=True)

# ==============================================================================
# 3. 메인 콘텐츠 영역 (B2C 급 메인 통합 카드 방식 적용)
# ==============================================================================
st.markdown("<div class='b2c-main-card'>", unsafe_allow_html=True)

# 화면 1: 채용 및 컴플라이언스 (홈 대시보드)
if menu == "📊 채용 및 컴플라이언스":
    st.markdown("<div class='b2c-page-title'>맞춤형 인재 추천 및 채용 컴플라이언스</div>", unsafe_allow_html=True)
    st.markdown("<p class='b2c-page-subtitle'>기업 구인 요건에 부합하는 우수 외국인 인재를 추천하고, 채용 가능 쿼터를 실시간으로 모니터링합니다.</p>", unsafe_allow_html=True)
    
    # [핵심 수정] 맞춤형 인재 추천 카드를 최상단에 전면 배치
    st.markdown("<div class='b2c-section-title' style='color:#2563EB;'>🎯 쿼터 확보 기반 우수 인재 추천</div>", unsafe_allow_html=True)
    
    candidates_html = (
        "<div class='candidate-grid' style='margin-bottom: 32px;'>"
        
        "<div class='candidate-card'>"
        "<div class='candidate-header'>"
        "<img src='https://cdn.pixabay.com/photo/2021/01/01/16/06/face-5879301_1280.jpg' class='candidate-avatar' />"
        "<span class='visa-badge visa-badge-safe'>안정권 94%</span>"
        "</div>"
        "<h4 class='candidate-name'>해원 (Haewon)</h4>"
        "<p class='candidate-uni'>🇻🇳 베트남 / 연세대학교 경제학과</p>"
        "<div class='candidate-spec-item'><b>지원 직무:</b> 해외영업 (베트남 담당)</div>"
        "<div class='candidate-spec-item'><b>어학 능력:</b> TOPIK 6급 (최상)</div>"
        "<button class='action-button'>면접 제안하기</button>"
        "</div>"
        
        "<div class='candidate-card'>"
        "<div class='candidate-header'>"
        "<img src='https://cdn.pixabay.com/photo/2023/10/24/09/27/man-8337777_1280.jpg' class='candidate-avatar' />"
        "<span class='visa-badge visa-badge-safe'>안정권 88%</span>"
        "</div>"
        "<h4 class='candidate-name'>아웅 (Aung)</h4>"
        "<p class='candidate-uni'>🇲🇲 미얀마 / 충남대학교 기계공학</p>"
        "<div class='candidate-spec-item'><b>지원 직무:</b> 생산관리 엔지니어</div>"
        "<div class='candidate-spec-item'><b>어학 능력:</b> TOPIK 4급 (비즈니스 소통 가능)</div>"
        "<button class='action-button'>면접 제안하기</button>"
        "</div>"
        
        "<div class='candidate-card' style='opacity: 0.6;'>"
        "<div class='candidate-header'>"
        "<img src='https://cdn.pixabay.com/photo/2021/08/01/18/14/man-6515082_1280.jpg' class='candidate-avatar' />"
        "<span class='visa-badge visa-badge-safe' style='background-color:#FEF3C7; color:#B45309;'>요건 검토 75%</span>"
        "</div>"
        "<h4 class='candidate-name'>리드완 (Ridwan)</h4>"
        "<p class='candidate-uni'>🇮🇩 인도네시아 / 부산대학교 무역학</p>"
        "<div class='candidate-spec-item'><b>지원 직무:</b> 해외영업</div>"
        "<div class='candidate-spec-item'><b>어학 능력:</b> TOPIK 5급</div>"
        "<button class='action-button' style='background-color: #F1F5F9; color: #475569; border: 1px solid #CBD5E1;'>상세 검토</button>"
        "</div>"
        
        "</div>"
    )
    st.markdown(candidates_html, unsafe_allow_html=True)
    
    # 얇은 구분선
    st.markdown("<div class='b2c-section-divider'></div>", unsafe_allow_html=True)
    
    # 핵심 지표 섹션 (B2C 스킨 입힌 통합 카드 내부)
    st.markdown("<div class='b2c-section-title'>인사 컴플라이언스 모니터링</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown("<div class='b2c-stat-card'><div class='metric-label'>내국인 고용보험 가입자</div><div class='metric-value'>42 명 <span class='metric-delta-up'>↑ 3</span></div></div>", unsafe_allow_html=True)
    with col2: st.markdown("<div class='b2c-stat-card'><div class='metric-label'>총 E-7 비자 허용 쿼터</div><div class='metric-value'>8 명 <span class='metric-delta-up'>↑ 1</span></div></div>", unsafe_allow_html=True)
    with col3: st.markdown("<div class='b2c-stat-card'><div class='metric-label'>현재 E-7 고용 인원</div><div class='metric-value'>6 명 <span class='metric-delta-down' style='color:#64748B; background-color:#F1F5F9;'>- 0</span></div></div>", unsafe_allow_html=True)
    with col4: st.markdown("<div class='b2c-stat-card' style='border:2px solid #3B82F6;'><div class='metric-label' style='color:#2563EB;'>추가 채용 가능 쿼터</div><div class='metric-value' style='color:#1D4ED8;'>2 명</div></div>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # 소속 외국인 테이블 (통합 카드 내부)
    st.markdown("<div class='b2c-section-title' style='margin-top: 16px;'>👥 소속 외국인 인력 체류 만료 현황</div>", unsafe_allow_html=True)
    
    table_html = (
        "<div class='table-container'>"
        "<table style='width: 100%; border-collapse: collapse; text-align: left; font-size: 13px;'>"
        "<thead>"
        "<tr style='background-color: #F8FAFC; border-bottom: 2px solid #E2E8F0;'>"
        "<th style='padding: 12px; color: #64748B; font-weight: 700;'>이름</th>"
        "<th style='padding: 12px; color: #64748B; font-weight: 700;'>국적</th>"
        "<th style='padding: 12px; color: #64748B; font-weight: 700;'>직무</th>"
        "<th style='padding: 12px; color: #64748B; font-size: 13px; font-weight: 700;'>비자 종류</th>"
        "<th style='padding: 12px; color: #64748B; font-size: 13px; font-weight: 700;'>만료 예정일</th>"
        "<th style='padding: 12px; color: #64748B; font-size: 13px; font-weight: 700;'>상태</th>"
        "</tr>"
        "</thead>"
        "<tbody>"
        "<tr style='border-bottom: 1px solid #E2E8F0;'>"
        "<td style='padding: 12px; font-weight: 600; color: #0F172A;'>응우옌 반 안</td>"
        "<td style='padding: 12px; color: #475569;'>VN 베트남</td>"
        "<td style='padding: 12px; color: #475569;'>생산관리</td>"
        "<td style='padding: 12px; font-weight: 500; color: #3B82F6;'>E-7-4</td>"
        "<td style='padding: 12px; color: #475569;'>2026-04-20</td>"
        "<td style='padding: 12px;'><span class='badge-warn' style='background-color:#FEF2F2; color:#B91C1C;'>🚨 만료 임박</span></td>"
        "</tr>"
        "<tr style='border-bottom: 1px solid #E2E8F0;'>"
        "<td style='padding: 12px; font-weight: 600; color: #0F172A;'>트란 티 마이</td>"
        "<td style='padding: 12px; color: #475569;'>VN 베트남</td>"
        "<td style='padding: 12px; color: #475569;'>품질관리</td>"
        "<td style='padding: 12px; font-weight: 500; color: #3B82F6;'>E-7-4</td>"
        "<td style='padding: 12px; color: #475569;'>2026-08-15</td>"
        "<td style='padding: 12px;'><span class='badge-check'>🟢 정상 체류</span></td>"
        "</tr>"
        "</tbody>"
        "</table>"
        "</div>"
    )
    st.markdown(table_html, unsafe_allow_html=True)

# 화면 2: 지원자 비자 평가
elif menu == "⚖️ 지원자 비자 평가":
    st.markdown("<div class='b2c-page-title'>지원자 비자 적격성 & 실무 역량 평가</div>", unsafe_allow_html=True)
    st.markdown("<p class='b2c-page-subtitle'>구직자 스펙을 분석하여 법무부 지침 기반의 비자 발급 확률과 조직 적응력을 정량화하여 제공합니다.</p>", unsafe_allow_html=True)
    
    # 평가 대상 프로필 카드 (통합 카드 내부)
    eval_profile_html = (
        "<div style='border: 1px solid #E2E8F0; padding: 24px; border-radius: 12px; display:flex; justify-content:space-between; align-items:center; margin-bottom: 24px;'>"
        "<div style='display:flex; align-items:center; gap:16px;'>"
        "<img src='https://cdn.pixabay.com/photo/2021/01/01/16/06/face-5879301_1280.jpg' style='width: 64px; height: 64px; border-radius: 50%; object-fit: cover;' />"
        "<div>"
        "<div class='candidate-name'>해원 (Haewon)</div>"
        "<p class='candidate-uni' style='margin-bottom:0;'>🇻🇳 베트남 / 연세대학교 경제학과</p>"
        "</div>"
        "</div>"
        "<div style='text-align:right;'>"
        "<div style='font-size: 13px; color: #64748B; font-weight: 600; margin-bottom: 4px;'>AI 비자 확률</div>"
        "<div style='font-size: 32px; font-weight: 900; color: #059669; line-height:1;'>94%</div>"
        "<div style='font-size: 12px; color: #047857; font-weight: 700;'>안정권</div>"
        "</div>"
        "</div>"
    )
    st.markdown(eval_profile_html, unsafe_allow_html=True)
    
    st.markdown("<div class='b2c-section-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='b2c-section-title'>정밀 요건 분석</div>", unsafe_allow_html=True)
    
    # 평가 리포트 테이블 (통합 카드 내부)
    report_table_html = (
        "<div class='table-container'>"
        "<table style='width: 100%; border-collapse: collapse; text-align: left; font-size: 13px;'>"
        "<thead>"
        "<tr style='background-color: #F8FAFC; border-bottom: 2px solid #E2E8F0;'>"
        "<th style='padding: 12px; color: #64748B; font-weight: 700;'>평가 항목</th>"
        "<th style='padding: 12px; color: #64748B; font-weight: 700;'>세부 스펙</th>"
        "<th style='padding: 12px; color: #64748B; font-weight: 700;'>컴플라이언스 점검</th>"
        "<th style='padding: 12px; color: #64748B; font-weight: 700;'>비고</th>"
        "</tr>"
        "</thead>"
        "<tbody>"
        "<tr style='border-bottom: 1px solid #E2E8F0;'>"
        "<td style='padding: 12px; font-weight: 600; color: #0F172A;'>직무-전공 연관성</td>"
        "<td style='padding: 12px; color: #475569;'>경제학 전공 ➡️ 해외영업 직무</td>"
        "<td style='padding: 12px;'><span class='badge-check'>🟢 통과</span></td>"
        "<td style='padding: 12px; color: #64748B;'>연관성 우수</td>"
        "</tr>"
        "<tr style='border-bottom: 1px solid #E2E8F0;'>"
        "<td style='padding: 12px; font-weight: 600; color: #0F172A;'>임금 요건 (GNI 기준)</td>"
        "<td style='padding: 12px; color: #475569;'>제시 연봉 3,300만 원 (GNI 81%)</td>"
        "<td style='padding: 12px;'><span class='badge-warn'>🟠 주의요망</span></td>"
        "<td style='padding: 12px; color: #64748B;'>3,400만 원으로 상향 권고</td>"
        "</tr>"
        "</tbody>"
        "</table>"
        "</div>"
    )
    st.markdown(report_table_html, unsafe_allow_html=True)

# 화면 3: 비자 행정 & AI 서류
elif menu == "📑 비자 행정 & AI 서류":
    st.markdown("<div class='b2c-page-title'>비자 행정 트래커 및 AI 서류 자동 생성</div>", unsafe_allow_html=True)
    st.markdown("<p class='b2c-page-subtitle'>비자 사증 발급까지의 전 과정을 구직자와 양방향으로 공유하며, 핵심 서류를 AI로 즉시 작성합니다.</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='b2c-section-title'>서류 준비 진척도</div>", unsafe_allow_html=True)
    
    st.progress(65)
    st.write("")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("<div class='b2c-stat-card'><div style='font-size:12px; font-weight:600; color:#334155; margin-bottom:8px;'>🧑‍🎓 구직자 측 서류 (수합 완료)</div><span class='badge-check'>여권</span> <span class='badge-check'>학위증</span> <span class='badge-check'>TOPIK</span></div>", unsafe_allow_html=True)
            
    with col_t2:
        st.markdown("<div class='b2c-stat-card'><div style='font-size:12px; font-weight:600; color:#334155; margin-bottom:8px;'>🏢 기업 측 서류 (진행 중)</div><span class='badge-check'>사업자등록증</span> <span class='badge-warn'>근로계약서</span> <span class='badge-warn'>고용사유서</span></div>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown("<div class='b2c-section-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='b2c-section-title' style='color:#2563EB;'>✨ AI E-7 고용사유서 자동 생성 엔진</div>", unsafe_allow_html=True)
    
    st.text_area("AI 고용사유서 결과 ( MS Word 양식으로 다운로드 가능)", value="[외국인 고용의 필요성]\n\n당사는 자동차 부품 제조 및 베트남 수출을 영위하는 기업으로, 최근 현지 오더량이 150% 급증하여 원어민 수준의 협상력이 필요합니다.\n\n[내국인 채용 노력 및 한계]\n지난 6개월간 내국인 채용을 진행했으나 베트남 시장 분석 능력을 동시에 갖춘 인재를 비수도권에서 확보하기 불가능했습니다.", height=150)
    st.button(" MS Word(.docx)로 다운로드", type="primary")

st.markdown("</div>", unsafe_allow_html=True) # b2c-main-card 닫기
