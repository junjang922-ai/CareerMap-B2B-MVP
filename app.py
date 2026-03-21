import streamlit as st
import pandas as pd
import time

# ==============================================================================
# 1. 페이지 설정 및 B2B용 CSS 디자인 시스템
# ==============================================================================
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
    }
    
    .metric-label { font-size: 13px; color: #64748B; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
    .metric-value { font-size: 32px; font-weight: 800; color: #0F172A; display: flex; align-items: baseline; gap: 12px; }
    .metric-delta-up { font-size: 14px; color: #10B981; font-weight: 600; padding: 2px 8px; background-color: #D1FAE5; border-radius: 12px; }
    .metric-delta-down { font-size: 14px; color: #EF4444; font-weight: 600; padding: 2px 8px; background-color: #FEE2E2; border-radius: 12px; }
    
    .badge-safe { color: #047857; background-color: #A7F3D0; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; }
    .badge-warn { color: #B45309; background-color: #FDE68A; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; }
    .badge-danger { color: #B91C1C; background-color: #FECACA; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; }
    
    .section-title {
        font-size: 20px; font-weight: 800; color: #0F172A; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #E2E8F0;
    }
    
    .ai-button > button {
        background: linear-gradient(135deg, #2563EB 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important; font-weight: 800 !important; font-size: 16px !important;
        border-radius: 12px !important; border: none !important; padding: 16px 24px !important;
        width: 100% !important; transition: all 0.3s ease !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. 사이드바
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color:#1E40AF; font-weight:900;'>CareerMap Biz</h2>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:14px; color:#64748B; margin-bottom:24px;'>다이캐스탈 코리아 인사본부</div>", unsafe_allow_html=True)
    
    menu = st.radio("Workspaces", ["📊 컴플라이언스 대시보드", "⚖️ 지원자 리스크 평가", "📑 비자 행정 & AI 서류"], label_visibility="collapsed")
    
    st.divider()
    
    sidebar_status = (
        "<div style='background-color:#EFF6FF; padding:16px; border-radius:12px; border:1px solid #BFDBFE;'>"
        "<div style='font-size:12px; color:#1D4ED8; font-weight:700; margin-bottom:4px;'>E-7 채용 쿼터 현황</div>"
        "<div style='font-size:24px; color:#1E3A8A; font-weight:900;'>2명 남음</div>"
        "<div style='font-size:12px; color:#3B82F6; margin-top:4px;'>총 허용 8명 중 6명 채용 완료</div>"
        "</div>"
    )
    st.markdown(sidebar_status, unsafe_allow_html=True)

# ==============================================================================
# 화면 1: 기업용 홈 대시보드
# ==============================================================================
if menu == "📊 컴플라이언스 대시보드":
    st.markdown("<div class='section-title'>인사 컴플라이언스 및 채용 대시보드</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B; margin-bottom:24px;'>실시간 내국인 고용보험 데이터와 연동되어 외국인 채용 쿼터를 산출하고 맞춤 인재를 추천합니다.</p>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown("<div class='dashboard-card'><div class='metric-label'>내국인 고용보험 가입자</div><div class='metric-value'>42 명 <span class='metric-delta-up'>↑ 3</span></div></div>", unsafe_allow_html=True)
    with col2: st.markdown("<div class='dashboard-card'><div class='metric-label'>총 E-7 비자 허용 쿼터</div><div class='metric-value'>8 명 <span class='metric-delta-up'>↑ 1</span></div></div>", unsafe_allow_html=True)
    with col3: st.markdown("<div class='dashboard-card'><div class='metric-label'>현재 E-7 고용 인원</div><div class='metric-value'>6 명 <span class='metric-delta-down'>- 0</span></div></div>", unsafe_allow_html=True)
    with col4: st.markdown("<div class='dashboard-card' style='border:2px solid #3B82F6; background-color:#F8FAFC;'><div class='metric-label' style='color:#2563EB;'>추가 채용 가능 쿼터</div><div class='metric-value' style='color:#1D4ED8;'>2 명</div></div>", unsafe_allow_html=True)

    progress_html = (
        "<div class='dashboard-card'>"
        "<div style='display: flex; justify-content: space-between; font-size: 14px; font-weight: 600; color: #475569; margin-bottom: 8px;'>"
        "<span>E-7 쿼터 소진율 (안전)</span><span style='color:#2563EB;'>75%</span>"
        "</div>"
        "<div style='width: 100%; background-color: #E2E8F0; border-radius: 999px; height: 10px;'>"
        "<div style='width: 75%; background-color: #3B82F6; height: 100%; border-radius: 999px;'></div>"
        "</div>"
        "<div style='margin-top: 8px; font-size: 12px; color: #64748B; text-align: right;'>"
        "잔여 쿼터 2명에 대한 맞춤형 인재를 아래에서 바로 확인하세요."
        "</div>"
        "</div>"
    )
    st.markdown(progress_html, unsafe_allow_html=True)

    st.markdown("<div class='section-title' style='margin-top: 32px;'>🎯 맞춤형 우수 외국인 인재 추천 (Direct Sourcing)</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B; margin-bottom:16px;'>등록하신 구인 조건(해외영업, 생산관리)에 부합하며, 비자 발급 확률이 검증된 인재입니다.</p>", unsafe_allow_html=True)

    candidates_html = (
        "<div style='display: flex; gap: 16px; margin-bottom: 24px;'>"
        
        "<div class='dashboard-card' style='flex: 1; margin-bottom: 0; padding: 20px; border-top: 4px solid #059669;'>"
        "<div style='display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;'>"
        "<div style='font-size: 24px; background-color: #EFF6FF; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center;'>👩‍🎓</div>"
        "<div style='background-color: #D1FAE5; color: #047857; padding: 4px 8px; border-radius: 6px; font-size: 12px; font-weight: 700;'>비자안정권 94%</div>"
        "</div>"
        "<h4 style='margin: 0 0 4px 0; color: #0F172A;'>해원 (Haewon)</h4>"
        "<p style='margin: 0 0 12px 0; font-size: 13px; color: #64748B;'>🇻🇳 베트남 / 연세대학교 경제학과</p>"
        "<div style='background-color: #F8FAFC; padding: 12px; border-radius: 8px; font-size: 12px; color: #475569; margin-bottom: 16px; line-height: 1.5;'>"
        "<b>지원 포지션:</b> 해외영업<br><b>어학 능력:</b> TOPIK 6급 (비즈니스 능통)"
        "</div>"
        "<button style='width: 100%; background-color: #2563EB; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: 600; cursor: pointer;'>면접 제안하기</button>"
        "</div>"
        
        "<div class='dashboard-card' style='flex: 1; margin-bottom: 0; padding: 20px; border-top: 4px solid #059669;'>"
        "<div style='display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;'>"
        "<div style='font-size: 24px; background-color: #FEF2F2; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center;'>👨‍💻</div>"
        "<div style='background-color: #D1FAE5; color: #047857; padding: 4px 8px; border-radius: 6px; font-size: 12px; font-weight: 700;'>비자안정권 88%</div>"
        "</div>"
        "<h4 style='margin: 0 0 4px 0; color: #0F172A;'>아웅 (Aung)</h4>"
        "<p style='margin: 0 0 12px 0; font-size: 13px; color: #64748B;'>🇲🇲 미얀마 / 충남대학교 기계공학</p>"
        "<div style='background-color: #F8FAFC; padding: 12px; border-radius: 8px; font-size: 12px; color: #475569; margin-bottom: 16px; line-height: 1.5;'>"
        "<b>지원 포지션:</b> 생산관리 엔지니어<br><b>어학 능력:</b> TOPIK 4급 (업무 소통 가능)"
        "</div>"
        "<button style='width: 100%; background-color: #2563EB; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: 600; cursor: pointer;'>면접 제안하기</button>"
        "</div>"
        
        "<div class='dashboard-card' style='flex: 1; margin-bottom: 0; padding: 20px; border-top: 4px solid #D97706;'>"
        "<div style='display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;'>"
        "<div style='font-size: 24px; background-color: #F0FDF4; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center;'>👨‍🎓</div>"
        "<div style='background-color: #FEF3C7; color: #B45309; padding: 4px 8px; border-radius: 6px; font-size: 12px; font-weight: 700;'>요건확인 75%</div>"
        "</div>"
        "<h4 style='margin: 0 0 4px 0; color: #0F172A;'>리드완 (Ridwan)</h4>"
        "<p style='margin: 0 0 12px 0; font-size: 13px; color: #64748B;'>🇮🇩 인도네시아 / 부산대학교 무역학</p>"
        "<div style='background-color: #F8FAFC; padding: 12px; border-radius: 8px; font-size: 12px; color: #475569; margin-bottom: 16px; line-height: 1.5;'>"
        "<b>지원 포지션:</b> 해외영업<br><b>어학 능력:</b> TOPIK 5급 (비즈니스 우수)"
        "</div>"
        "<button style='width: 100%; background-color: #F1F5F9; color: #475569; border: 1px solid #CBD5E1; padding: 10px; border-radius: 8px; font-weight: 600; cursor: pointer;'>상세 요건 검토</button>"
        "</div>"
        
        "</div>"
    )
    st.markdown(candidates_html, unsafe_allow_html=True)

    st.markdown("<div class='section-title' style='margin-top: 32px;'>👥 소속 외국인 인력 체류 만료 현황</div>", unsafe_allow_html=True)
    
    table_html = (
        "<div class='dashboard-card' style='padding: 0; overflow: hidden;'>"
        "<table style='width: 100%; border-collapse: collapse; text-align: left;'>"
        "<thead>"
        "<tr style='background-color: #F8FAFC; border-bottom: 2px solid #E2E8F0;'>"
        "<th style='padding: 16px; color: #64748B; font-size: 13px; font-weight: 700;'>이름</th>"
        "<th style='padding: 16px; color: #64748B; font-size: 13px; font-weight: 700;'>국적</th>"
        "<th style='padding: 16px; color: #64748B; font-size: 13px; font-weight: 700;'>부서/직무</th>"
        "<th style='padding: 16px; color: #64748B; font-size: 13px; font-weight: 700;'>비자 종류</th>"
        "<th style='padding: 16px; color: #64748B; font-size: 13px; font-weight: 700;'>만료 예정일</th>"
        "<th style='padding: 16px; color: #64748B; font-size: 13px; font-weight: 700;'>상태</th>"
        "</tr>"
        "</thead>"
        "<tbody>"
        "<tr style='border-bottom: 1px solid #E2E8F0;'>"
        "<td style='padding: 16px; font-weight: 600; color: #0F172A;'>응우옌 반 안</td>"
        "<td style='padding: 16px; color: #475569;'>VN 베트남</td>"
        "<td style='padding: 16px; color: #475569;'>생산1팀 / CNC</td>"
        "<td style='padding: 16px; font-weight: 500; color: #3B82F6;'>E-7-4</td>"
        "<td style='padding: 16px; color: #475569;'>2026-04-20</td>"
        "<td style='padding: 16px;'><span class='badge-danger'>🚨 만료 임박(30일)</span></td>"
        "</tr>"
        "<tr style='border-bottom: 1px solid #E2E8F0;'>"
        "<td style='padding: 16px; font-weight: 600; color: #0F172A;'>트란 티 마이</td>"
        "<td style='padding: 16px; color: #475569;'>VN 베트남</td>"
        "<td style='padding: 16px; color: #475569;'>품질관리 / 검사</td>"
        "<td style='padding: 16px; font-weight: 500; color: #3B82F6;'>E-7-4</td>"
        "<td style='padding: 16px; color: #475569;'>2026-08-15</td>"
        "<td style='padding: 16px;'><span class='badge-safe'>🟢 정상 체류</span></td>"
        "</tr>"
        "</tbody>"
        "</table>"
        "</div>"
    )
    st.markdown(table_html, unsafe_allow_html=True)
    
    st.markdown("<div class='section-title'>🚨 리스크 알림</div>", unsafe_allow_html=True)
    st.error("생산본부 '응우옌 반 안' 직원의 체류 기간이 30일 뒤 만료됩니다. 연장 수속을 즉시 진행하십시오.")

# ==============================================================================
# 화면 2: 지원자 리스크 평가 리포트
# ==============================================================================
elif menu == "⚖️ 지원자 리스크 평가":
    st.markdown("<div class='section-title'>지원자 비자 적격성 & 실무 역량 리포트</div>", unsafe_allow_html=True)
    
    header_card = (
        "<div class='dashboard-card' style='display:flex; justify-content:space-between; align-items:center; border-left:6px solid #2563EB;'>"
        "<div style='display:flex; align-items:center; gap:20px;'>"
        "<div style='width:64px; height:64px; background-color:#E2E8F0; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:24px;'>👩‍🎓</div>"
        "<div>"
        "<h3 style='margin:0; font-weight:800; color:#0F172A;'>해원 (Haewon) <span style='font-size:14px; font-weight:500; color:#64748B;'>베트남 · 25세</span></h3>"
        "<p style='margin:4px 0 0 0; color:#475569; font-size:14px;'>지원 포지션: <b>해외영업 (베트남 담당)</b> / 연세대 경제학과 졸업예정</p>"
        "</div>"
        "</div>"
        "<div style='text-align:right;'>"
        "<div style='font-size:13px; color:#64748B; font-weight:700; margin-bottom:4px;'>AI 산출 E-7 발급 확률</div>"
        "<div style='font-size:36px; font-weight:900; color:#059669; line-height:1;'>94% <span class='badge-safe' style='vertical-align:middle;'>안정권</span></div>"
        "</div>"
        "</div>"
    )
    st.markdown(header_card, unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1.2, 1])
    
    with col_l:
        left_card = (
            "<div class='dashboard-card'>"
            "<div style='font-size:16px; font-weight:800; margin-bottom:16px;'>출입국 지침 컴플라이언스 점검</div>"
            "<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><b>직무-전공 연관성</b> <span class='badge-safe'>통과</span></div>"
            "<p style='font-size:13px; color:#64748B; margin-bottom:16px;'>해외영업 직무코드(2742)와 경제학 전공이 일치함.</p>"
            "<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><b>임금 요건 (GNI 80% 이상)</b> <span class='badge-warn'>주의</span></div>"
            "<p style='font-size:13px; color:#64748B; margin-bottom:16px;'>제시 연봉 3,300만 원. GNI 변동 대비 3,400만 원으로 상향 권고.</p>"
            "<div style='display:flex; justify-content:space-between; margin-bottom:8px;'><b>범칙금 이력</b> <span class='badge-safe'>클린</span></div>"
            "<p style='font-size:13px; color:#64748B; margin-bottom:0;'>시간제 취업 위반 등 결격 사유 없음.</p>"
            "</div>"
        )
        st.markdown(left_card, unsafe_allow_html=True)
        
    with col_r:
        right_card = (
            "<div class='dashboard-card'>"
            "<div style='font-size:16px; font-weight:800; margin-bottom:20px;'>실무 역량 검증 리포트</div>"
            "<div style='margin-bottom: 16px;'>"
            "<div style='display: flex; justify-content: space-between; font-size: 13px; font-weight: 600; color: #475569; margin-bottom: 6px;'>"
            "<span>비즈니스 한국어 (TOPIK 6급)</span><span>95/100</span>"
            "</div>"
            "<div style='width: 100%; background-color: #E2E8F0; border-radius: 999px; height: 8px;'>"
            "<div style='width: 95%; background-color: #059669; height: 100%; border-radius: 999px;'></div>"
            "</div>"
            "</div>"
            "<div style='margin-bottom: 16px;'>"
            "<div style='display: flex; justify-content: space-between; font-size: 13px; font-weight: 600; color: #475569; margin-bottom: 6px;'>"
            "<span>문서 작성 역량 (기획서)</span><span>85/100</span>"
            "</div>"
            "<div style='width: 100%; background-color: #E2E8F0; border-radius: 999px; height: 8px;'>"
            "<div style='width: 85%; background-color: #3B82F6; height: 100%; border-radius: 999px;'></div>"
            "</div>"
            "</div>"
            "<div style='margin-bottom: 16px;'>"
            "<div style='display: flex; justify-content: space-between; font-size: 13px; font-weight: 600; color: #475569; margin-bottom: 6px;'>"
            "<span>한국 기업 조직 적응력</span><span>90/100</span>"
            "</div>"
            "<div style='width: 100%; background-color: #E2E8F0; border-radius: 999px; height: 8px;'>"
            "<div style='width: 90%; background-color: #8B5CF6; height: 100%; border-radius: 999px;'></div>"
            "</div>"
            "</div>"
            "<div style='background-color:#F1F5F9; padding:12px; border-radius:8px; margin-top:20px; font-size:13px; color:#475569;'>"
            "<b>종합 의견:</b> 한국인 신입 사원과 동일 수준의 소통이 가능하며, 현지 벤더사 관리에 즉각 투입 가능한 S급 인재입니다."
            "</div>"
            "</div>"
        )
        st.markdown(right_card, unsafe_allow_html=True)

# ==============================================================================
# 화면 3: 비자 행정 트래커 및 AI 서류
# ==============================================================================
elif menu == "📑 비자 행정 & AI 서류":
    st.markdown("<div class='section-title'>양방향 행정 트래커 및 고용사유서 생성</div>", unsafe_allow_html=True)
    
    st.markdown("#### 서류 준비 진척도: 해원 (신규 채용)")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        with st.container(border=True):
            st.markdown("**🧑‍🎓 구직자 측 서류 (완료)**")
            st.progress(100)
            st.checkbox("여권 및 외국인등록증 사본", value=True, disabled=True)
            st.checkbox("학위증명서 (아포스티유 인증)", value=True, disabled=True)
            st.checkbox("성적증명서 및 TOPIK 성적표", value=True, disabled=True)
            
    with col_t2:
        with st.container(border=True):
            st.markdown("**🏢 기업 측 서류 (진행 중)**")
            st.progress(60)
            st.checkbox("사업자등록증 및 등기부등본", value=True)
            st.checkbox("납세증명서 및 가입자 명부", value=True)
            st.checkbox("표준 근로계약서 원본", value=False)
            st.checkbox("외국인 고용사유서 (심사 핵심 서류)", value=False)

    ai_header = (
        "<div class='dashboard-card' style='margin-top:24px; background: linear-gradient(to right, #F8FAFC, #EFF6FF); border: 1px solid #BFDBFE;'>"
        "<h3 style='margin-top:0; color:#1E40AF;'>✨ E-7 고용사유서 AI 자동 생성기</h3>"
        "<p style='font-size:14px; color:#475569; margin-bottom:0;'>가장 까다로운 고용사유서를 기업 산업 분류와 구직자 스펙을 교차 분석하여 즉시 작성합니다.</p>"
        "</div>"
    )
    st.markdown(ai_header, unsafe_allow_html=True)
    
    st.markdown('<div class="ai-button">', unsafe_allow_html=True)
    if st.button("🚀 AI 고용사유서 초안 생성 시작"):
        with st.status("AI가 출입국 심사 지침을 분석하여 문서를 작성 중입니다...", expanded=True) as status:
            time.sleep(1)
            st.write("1. 기업의 수출 실적 및 채용 배경 분석 완료")
            time.sleep(1)
            st.write("2. 내국인 채용 노력 입증 논리 및 지원자 역량 매칭 완료")
            status.update(label="고용사유서 작성 완료!", state="complete", expanded=False)
        
        doc_text = """[외국인 고용의 필요성 및 활용 계획서]

1. 기업 현황 및 외국인 도입 배경
당사(다이캐스탈 코리아)는 자동차 부품 수출 기업으로, 최근 베트남 직계약 물량이 150% 급증하여 현지 비즈니스 협상력을 갖춘 전담 인력이 시급합니다.

2. 내국인 고용 노력 및 한계
워크넷을 통해 6개월간 채용을 진행했으나, 베트남 원어민 수준의 어학 능력과 경제학적 분석 역량을 동시에 충족하는 인재를 비수도권에서 확보하기 불가능했습니다.

3. 채용 당위성
지원자 해원은 연세대 경제학과 출신으로 거시 분석이 가능하며 TOPIK 6급을 보유해 완벽한 업무 소통이 가능합니다. 현지 리스크를 제거할 대체 불가 인력이므로 E-7 사증 발급을 강력히 요청합니다."""
        
        st.success("✅ 초안이 생성되었습니다.")
        st.text_area("결과 (편집 가능)", value=doc_text, height=250)
        st.button("💾 MS Word (.docx) 다운로드")
    st.markdown('</div>', unsafe_allow_html=True)
