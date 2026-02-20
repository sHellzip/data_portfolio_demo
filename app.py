import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI
import numpy as np
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 0. 简历数据 (System Prompt Context)
# -----------------------------------------------------------------------------
RESUME_CONTENT = """
My name is Shuyue Hou. I am applying for a Data Analyst / Data Scientist role.
Here is my resume content:

[Contact]
Email: shou003@e.ntu.edu.sg | LinkedIn: Shuyue Hou

[Education]
1. M.Sc. in Signal Processing and Machine Learning, Nanyang Technological University (Aug 2024-Jun 2025). Grade: 3.3/5.0.
2. B.Sc. in Statistics, Beijing Institute of Technology (Sep 2019-Jun 2023). Grade: 90/100.
Awards: Academic Excellence Award (2020, 2023), Red Forest Scholarship.

[Experience]
1. Machine Learning Engineer @ Pingan Bank (Aug 2025-Present)
- Developed Rate/Mix decomposition engine (Python/Pandas) for $10B+ deposit campaigns.
- Designed GenAI-powered dashboard (LLM/Agent) reducing report time by 98%.
- Engineered ETL pipeline (SQL & Python) ensuring 100% data integrity.

2. Co-founder @ OfferLah, Singapore (Feb 2025-Present)
- Automated scheduling system reducing admin overhead by 40%.
- Funnel Analysis identified 15% drop-off; UI/UX redesign improved conversion by 20%.

3. Data Analyst Intern @ Xiaohongshu (RED) (Dec 2023-May 2024)
- Analyzed 300,000+ user behaviors via SQL.
- Bidding Strategy optimized budget, increased ROAS by 25%.
- Built Power BI dashboards reducing reporting time by 50%.

[Projects]
1. Financial Transaction Risk Dashboard: Tableau, LOD Expressions, Pareto Analysis.
2. Ensemble Text Classification System: Python, Scikit-Learn, NLP, TF-IDF, AHP (85% precision/recall).

[Skills]
Python, SQL (Advanced), Tableau, Power BI, GenAI/LLM, ETL, Anomaly Detection.
"""


# -----------------------------------------------------------------------------
# 1. 页面配置 
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Shuyue's Data Portfolio",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. 侧边栏：个人信息 (Sidebar)
# -----------------------------------------------------------------------------
with st.sidebar:

    st.image("materials/selfie.png", width=150)

    st.title("Shuyue Hou")
    st.markdown("**Machine Learning Engineer | Data Analyst**")
    st.markdown("🎓 **M.Sc. @ NTU (Signal Processing and Machine Learning)**")
    st.markdown("🎓 **B.Sc. @ BIT (Statistics)**")

    st.divider()

    # 联系方式
    st.write("📧 shou003@e.ntu.edu.sg")
    st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/olivia-h-44721b304/)")
    st.write("🔗 [Tableau Portfolio](https://public.tableau.com/app/profile/shuyue.hou)")

    st.divider()

    # 简历下载
    try:
        with open("materials/resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download PDF Resume",
                data=pdf_file,
                file_name="Shuyue_Hou_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("⚠️ Resume file not found in materials/")

# -----------------------------------------------------------------------------
# 3. 主页标题与 Intro
# -----------------------------------------------------------------------------
st.title("👋 Hi, I'm Shuyue.")
st.markdown("""
### Applying for the **Data Analyst / Data Scientist** Role
> 🚀 **Why Me?**  
> I turn complex data into **actionable business decisions** and production-ready solutions.  
>  
> I specialize in **end-to-end analytics** — from problem framing and metric design to insight generation and productization  
> (**Data Analysis → Business Insight → AI Application → Product Delivery**).  
>  
> At *Ping An Bank*, I built anomaly diagnosis engines and GenAI-powered reporting tools that reduced analysis time from days to hours.  
> At *Xiaohongshu*, I optimized bidding strategies through user behavior analysis, driving measurable ROAS growth.  
>  
> My strength lies in combining **SQL, Python, and statistical thinking** with **AI integration and product mindset** to solve real business problems at scale.
""")

# -----------------------------------------------------------------------------
# 4. 核心内容分栏 (Tabs)
# -----------------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🚀 Experience & Skills", "✨ Chat with My Resume", "📈 Interactive Analysis"])

# =============================================================================
# TAB 1: 简历深度解析 (Experience & Skills)
# =============================================================================
with tab1:
    # --- 第一部分：技能矩阵 (针对 JD 优化) ---
    st.header("🛠️ Technical Arsenal")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 💻 Programming & Data")
        st.write("✅ **Python (Pandas, Scikit-Learn)**")
        st.write("✅ **SQL (Advanced/MySQL)**")
        st.write("✅ **Java & Data Cleaning & Git**")

    with col2:
        st.markdown("#### 📊 Visualization & BI")
        st.write("✅ **Tableau & Power BI**")
        st.write("✅ **GenAI Automated Reporting**")
        st.write("✅ **Excel (VBA, Pivot Tables)**")

    with col3:
        st.markdown("#### 🧠 Analytics & AI")
        st.write("✅ **Statistics Background**")  # JD Keyword
        st.write("✅ **A/B Testing & Anomaly Detection**")
        st.write("✅ **LLM / Agent Development**")

    st.divider()

    # --- 第二部分：职业经历 (Professional Experience) ---
    st.header("🏢 Professional Experience")

    # 经历 1: Pingan Bank
    with st.container():
        st.subheader("Machine Learning Engineer | Pingan Bank Co.,Ltd.")
        st.caption("Aug 2025 - Present (Full Time) | Shenzhen")

        st.markdown("""
        *   **Business Driver & Root Cause Analysis:** Developed a Rate/Mix decomposition engine to **quantify drivers** behind CTR/CVR fluctuations for **$10B+ campaigns**. Reduced anomaly diagnosis time from days to hours.
        *   **GenAI-powered Dashboard:** Designed an **LLM-Agent dashboard** that auto-generates diagnostic reports, slashing reporting time by **98%**. 
        *   **Data Pipeline (ETL):** Engineered a robust **Source-ETL-Model pipeline** (SQL & Python) to resolve T0/T1 data alignment, ensuring **100% data integrity** for attribution models.
        """)
        st.success("💡 **Impact:** Solved the 'Business-Technology Challenge' by automating manual diagnostics with GenAI.")

    # 经历 2: Xiaohongshu
    with st.container():
        st.subheader("Data Analyst Intern | Xiaohongshu (RED)")
        st.caption("Dec 2023 - May 2024 | Beijing")

        st.markdown("""
        *   **Strategic Bidding (SQL):** Analyzed **300,000+ user search behaviors using SQL**. Identified long-tail keywords to optimize budget allocation.
        *   **Business Impact:** Drove a **25% increase in ROAS** and 18% growth in sales volume by capturing niche user intent.
        *   **Dashboarding:** Developed automated **Power BI dashboards** to visualize real-time metrics (CTR, CVR, CPA), reducing reporting time by 50%.
        """)
        st.success("💡 **Impact:** Demonstrated data-driven growth capability by translating user behavior insights into bidding strategies that significantly improved ROAS and revenue.")

    st.divider()

    # --- 创业经历 (Entrepreneurship) ---
    st.header("🚀 Entrepreneurship Experience")

    with st.container():
        st.subheader("Co-founder | OfferLah (Startup)")
        st.caption("Feb 2025 - Present | Singapore")

        st.markdown("""
        *   **Operational System Design & Automation:** Spearheaded the migration from **manual spreadsheets to an automated scheduling ecosystem**. Established a centralized data tracking system that **reduced admin overhead by 40%**.
        *   **Funnel Analysis & User Growth:** Defined full-funnel conversion metrics. Identified a **15% drop-off** at the service inquiry stage using data visualization, prompting a UI/UX redesign that improved the **Lead-to-Customer conversion rate by 20%**.
        """)
        st.success(
            "🌟 **Highlight:** Demonstrated full-cycle ability from defining metrics -> identifying problems -> implementing solutions.")

    st.divider()

    # --- 第四部分：项目 (Projects) ---
    st.header("📂 Key Projects")

    col_p1, col_p2 = st.columns(2)

    with col_p1:
        st.markdown("**💰 Financial Transaction Risk Dashboard**")
        st.markdown("*Tableau, LOD Expressions, Pareto Analysis*")
        st.markdown(
            "Identified **anomalies and high-risk transactions** using dynamic thresholding. Solved resource allocation challenges.")
        st.markdown("[🔗 View Dashboard](https://public.tableau.com/app/profile/shuyue.hou)")

    with col_p2:
        st.markdown("**📝 Ensemble Text Classification System**")
        st.markdown("*Python, Scikit-Learn, NLP, TF-IDF*")
        st.markdown(
            "Engineered a text processing pipeline and implemented **AHP (Analytic Hierarchy Process)** to improve precision/recall to over 85%.")
        st.markdown("[🔗 View GitHub](https://github.com/sHellzip/question_pair)")

# =============================================================================
# TAB 2: AI Chat (Doubao / Volcengine Integration)
# =============================================================================
with tab2:
    st.header("✨ Chat with My Resume")
    st.caption("Powered by Doubao (Volcengine) LLM")

    # -------------------------------------------------------------------------
    # 1. 初始化 API Client
    # -------------------------------------------------------------------------
    # 为了演示方便，暂时直接在这里填 Key。
    # 正式部署时建议使用 st.secrets["ARK_API_KEY"]
    try:
        my_api_key = st.secrets["ARK_API_KEY"]
    except FileNotFoundError:
        st.error("⚠️ API Key 未找到。请在本地配置 .streamlit/secrets.toml 或在云端配置 Secrets。")
        st.stop()

    if not my_api_key:
        st.warning("⚠️ Please provide a valid API Key in the code to activate the chatbot.")
    else:
        client = OpenAI(
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            api_key=my_api_key,
        )

        # ---------------------------------------------------------------------
        # 2. 初始化聊天历史
        # ---------------------------------------------------------------------
        if "messages" not in st.session_state:
            st.session_state.messages = []
            # 开场白
            welcome_msg = "Hello! I am Shuyue's AI Assistant. Ask me anything about her experience, Project details, or Education!"
            st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

        # ---------------------------------------------------------------------
        # 3. 显示历史消息
        # ---------------------------------------------------------------------
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        # ---------------------------------------------------------------------
        # 4. 处理用户输入
        # ---------------------------------------------------------------------
        if prompt := st.chat_input("Ask about my experience (e.g., 'Tell me about the RED project')"):

            # 4.1 显示用户提问
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            # 4.2 构造发送给 AI 的消息列表 (System Prompt + History)
            # 我们把 RESUME_CONTENT 作为 System Prompt 藏在最前面，不显示在界面上
            api_messages = [
                {"role": "system",
                 "content": f"You are a helpful assistant representing Shuyue Hou. Answer questions based strictly on this resume context:\n\n{RESUME_CONTENT}\n\nIf the answer is not in the resume, say you don't know but offer to contact Shuyue directly."}
            ]

            # 追加历史对话 (为了让 AI 有记忆)
            for m in st.session_state.messages:
                api_messages.append({"role": m["role"], "content": m["content"]})

            # 4.3 调用豆包 API
            try:
                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                        model="doubao-seed-1-8-251228",  # 你的 Endpoint ID
                        messages=api_messages,
                        stream=True
                    )
                    # 流式输出
                    response = st.write_stream(stream)

                # 4.4 保存 AI 回复到历史
                st.session_state.messages.append({"role": "assistant", "content": response})

            except Exception as e:
                st.error(f"Error connecting to AI: {e}")


# =============================================================================
# TAB 3: 多维比率归因引擎 (Rate/Mix + Beam Search)
# =============================================================================
with tab3:
    st.header("📉 Metric Attribution Engine (Rate/Mix + Beam Search)")
    st.markdown("""
    This module simulates the **Root Cause Analysis System** I developed using Python.
    Unlike traditional dashboards, it uses a **Beam Search Algorithm** to automatically traverse high-dimensional data 
    and decompose Ratio Metrics (e.g., CTR, CVR) into **Rate Effect** (Efficiency) vs. **Mix Effect** (Structure).
    """)


    # -------------------------------------------------------------------------
    # 1. 定义核心算法逻辑
    # -------------------------------------------------------------------------
    def calculate_ratio_contribution_v2(node_ratio_t0, node_ratio_t1, w_t0, w_t1):
        """
        Reflecting the exact logic from my project code:
        Rate Effect = (Rate_t1 - Rate_t0) * W_t1
        Mix Effect  = (W_t1 - W_t0) * Rate_t0
        """
        rate_effect = (node_ratio_t1 - node_ratio_t0) * w_t1
        mix_effect = (w_t1 - w_t0) * node_ratio_t0
        return rate_effect, mix_effect


    st.divider()

    # -------------------------------------------------------------------------
    # 2. 模拟业务场景数据 (Simulation Data)
    # -------------------------------------------------------------------------
    # 场景：CTR 下降。
    # 原因：虽然 Search (高CTR) 和 Feed (低CTR) 的各自 CTR 都没怎么跌，
    # 但 Feed 的流量占比从 50% 涨到了 80%，导致大盘 CTR 被拉低 (典型的 Mix Effect)。

    # T0 (Base Period：基期，也就是参照的对比组)
    clicks_t0 = 5000
    imp_t0 = 100000
    ctr_t0 = clicks_t0 / imp_t0  # 5.0%

    # T1 (Current Period：当期，顾名思义，就是现在这个时期)
    # 模拟：CTR 掉到了 3.8%
    clicks_t1 = 4560
    imp_t1 = 120000  # 曝光涨了
    ctr_t1 = clicks_t1 / imp_t1  # 3.8%

    delta_ctr = ctr_t1 - ctr_t0  # -1.2%

    # 模拟第一层归因结果 (Global Level Decomposition)
    # 汇总了所有子节点的 Rate Effect 和 Mix Effect


    # 故事：Mix Effect (结构) 贡献了绝大部分跌幅 (-1.0%)，Rate Effect (效率) 只跌了一点点 (-0.2%)
    total_rate_effect = -0.002
    total_mix_effect = -0.010

    # -------------------------------------------------------------------------
    # 3. 核心指标看板 (KPIs)
    # -------------------------------------------------------------------------
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    col_kpi1.metric("Global CTR (Period T0)", f"{ctr_t0 * 100:.2f}%")
    col_kpi2.metric("Global CTR (Period T1)", f"{ctr_t1 * 100:.2f}%", delta=f"{delta_ctr * 100:.2f}%",
                    delta_color="inverse")
    col_kpi3.metric("Attribution Status", "⚠️ Mix-Driven Drop")

    # -------------------------------------------------------------------------
    # 4. 第一层：Rate/Mix 瀑布图 (Waterfall)
    # -------------------------------------------------------------------------
    st.subheader("1️⃣ Global Attribution: Rate vs. Mix")
    st.caption(
        "Did the CTR drop because ads performed worse (Rate), or because traffic shifted to low-CTR channels (Mix)?")

    fig_waterfall = go.Figure(go.Waterfall(
        name="CTR Decomposition", orientation="v",
        measure=["relative", "relative", "relative", "total"],
        x=["CTR T0", "Rate Effect (Efficiency)", "Mix Effect (Structure)", "CTR T1"],
        textposition="outside",
        text=[f"{ctr_t0 * 100:.2f}%", f"{total_rate_effect * 100:.2f}%", f"{total_mix_effect * 100:.2f}%",
              f"{ctr_t1 * 100:.2f}%"],
        y=[ctr_t0, total_rate_effect, total_mix_effect, ctr_t1],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        decreasing={"marker": {"color": "#FF4B4B"}},
        increasing={"marker": {"color": "#2ECC71"}},
        totals={"marker": {"color": "#1F77B4"}}
    ))
    fig_waterfall.update_layout(title="Drivers of CTR Drop", height=400, yaxis_tickformat=".2%")
    st.plotly_chart(fig_waterfall, use_container_width=True)

    st.info("""
    **🧠 Insight:** 
    The waterfall reveals a **Structural Issue (Mix Effect)**. 
    The negative impact comes primarily from **Mix Effect (-1.0%)**, meaning high-quality traffic volume decreased or low-quality traffic increased. 
    Efficiency (Rate Effect) remained relatively stable.
    """)

    # -------------------------------------------------------------------------
    # 5. 第二层：Beam Search 自动下钻结果 (Automated Drill-down)
    # -------------------------------------------------------------------------
    st.subheader("2️⃣ Automated Root Cause Discovery (Beam Search)")
    st.markdown("""
    The system executed a **Beam Search** algorithm (Top-K pruning) across dimensions: `Channel`, `App_Version`, `User_Tag`.
    Here are the **Top Negative Contributors** identified automatically:
    """)

    if st.button("🚀 Run Beam Search Algorithm"):
        import time

        # 模拟计算
        with st.spinner('Running multidimensional decomposition algorithm...'):
            time.sleep(1.5)

        # 模拟 Beam Search 返回的 flat_negative 结果列表
        beam_results = [
            {
                "Path (Dimension Combination)": "Channel=Feed_Flow",
                "CTR T0": "2.5%",
                "CTR T1": "2.4%",
                "Weight T0": "50%",
                "Weight T1": "80% (⬆)",  # 流量占比暴涨，拉低了大盘
                "Contribution": "-0.85%"
            },
            {
                "Path (Dimension Combination)": "Region=Tier3_Cities",
                "CTR T0": "3.0%",
                "CTR T1": "2.9%",
                "Weight T0": "20%",
                "Weight T1": "35% (⬆)",
                "Contribution": "-0.15%"
            },
            {
                "Path (Dimension Combination)": "App_Version=v10.5 -> Channel=Search",
                "CTR T0": "12.0%",
                "CTR T1": "10.5% (⬇)",  # 真的跌了
                "Weight T0": "10%",
                "Weight T1": "10%",
                "Contribution": "-0.12%"
            }
        ]

        # 将结果转换为 DataFrame 展示
        df_results = pd.DataFrame(beam_results)

        # 高亮展示
        st.dataframe(
            df_results.style.map(lambda x: 'color: red' if 'Negative' in str(x) or '-' in str(x) else 'color: black'),
            use_container_width=True
        )

        st.success("""
        **🎯 Root Cause Found:** 
        The primary driver is the significant **traffic shift towards 'Feed_Flow'** (Mix Effect). 
        While 'Feed_Flow' CTR is stable, its volume share increased from 50% to 80%, diluting the overall performance.
        **Action:** Re-evaluate bid adjustment for Feed Flow traffic.
        """)