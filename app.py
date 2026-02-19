import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI
import numpy as np

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
    # 确保 materials/selfie.png 存在，否则会显示破图图标
    # 如果还没照片，暂时注释掉下面这行
    st.image("materials/selfie.png", width=150)

    st.title("Shuyue Hou")
    st.markdown("**Machine Learning Engineer | Data Analyst**")
    st.markdown("🎓 **M.Sc. @ NTU (Signal Processing and Machine Learning)**")
    st.markdown("🎓 **B.Sc. @ BIT (Statistics)**")

    st.divider()

    # 联系方式
    st.write("📧 shou003@e.ntu.edu.sg")
    st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/olivia-h-44721b304/)")  # 替换为你的真实链接
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
> I bridge the gap between **Complex Data Engineering** and **Business Strategy**.  
> From building **Anomaly diagnosis** & **GenAI dashboards** at *Pingan Bank* to optimizing **Bidding Strategies** at *Xiaohongshu*, 
> I leverage **SQL, Python, and Anomaly Detection** to solve business-technology challenges.
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
        *   **GenAI-powered Dashboard:** Designed an **LLM-Agent dashboard** that auto-generates diagnostic reports, slashing reporting time by **98%**. *(Directly matches JD: Support dashboards & reports)*
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
                    # 流式输出 (打字机效果)
                    response = st.write_stream(stream)

                # 4.4 保存 AI 回复到历史
                st.session_state.messages.append({"role": "assistant", "content": response})

            except Exception as e:
                st.error(f"Error connecting to AI: {e}")


# =============================================================================
# TAB 3: Interactive Analysis (The "Show Me" Part)
# =============================================================================
with tab3:
    st.header("📊 Interactive Data Analysis Demo")
    st.write(
        "This interactive dashboard simulates the **Anomaly Detection & ROAS Optimization** logic I implemented at *Pingan Bank* and *Xiaohongshu*.")

    # --- 1. 模拟数据生成 (Data Simulation) --- #

    dates = pd.date_range(start="2024-01-01", periods=90)

    # 模拟基础趋势
    base_traffic = np.linspace(1000, 5000, 90)  # 逐步增长
    noise = np.random.normal(0, 200, 90)  # 随机波动
    traffic = base_traffic + noise

    # 模拟转化率 (CVR)
    cvr = np.random.uniform(0.02, 0.05, 90)

    # 插入“异常点” (Anomalies) - 模拟某天服务器故障或投放事故
    traffic[20] = 500  # 暴跌
    traffic[65] = 8000  # 暴涨
    cvr[20] = 0.005  # 转化率异常低

    # 组装 DataFrame
    df_demo = pd.DataFrame({
        "Date": dates,
        "Traffic (Clicks)": traffic,
        "CVR (Conversion Rate)": cvr,
        "Cost": traffic * np.random.uniform(0.5, 0.8, 90),
    })
    df_demo["Revenue"] = df_demo["Traffic (Clicks)"] * df_demo["CVR (Conversion Rate)"] * 100
    df_demo["ROAS"] = df_demo["Revenue"] / df_demo["Cost"]

    # --- 2. 交互控制区 (Interactive Widgets) ---
    col_ctrl1, col_ctrl2 = st.columns([1, 3])

    with col_ctrl1:
        st.markdown("#### ⚙️ Settings")
        metric_choice = st.selectbox("Select Metric to Analyze:", ["Traffic (Clicks)", "ROAS", "Revenue"])
        show_anomaly = st.checkbox("🔍 Detect Anomalies (Auto)", value=True)

    with col_ctrl2:
        # --- 3. 绘制图表 (Visualization) ---

        # 计算动态阈值 (公式：limit = 均值 ± 2倍标准差)
        mean_val = df_demo[metric_choice].mean()
        std_val = df_demo[metric_choice].std()
        upper_limit = mean_val + 2 * std_val
        lower_limit = mean_val - 2 * std_val

        # 标记异常点
        df_demo["Type"] = "Normal"
        if show_anomaly:
            df_demo.loc[df_demo[metric_choice] > upper_limit, "Type"] = "Anomaly (High)"
            df_demo.loc[df_demo[metric_choice] < lower_limit, "Type"] = "Anomaly (Low)"

        # 绘图
        fig = px.scatter(
            df_demo,
            x="Date",
            y=metric_choice,
            color="Type",  # 颜色区分异常点
            color_discrete_map={"Normal": "#1f77b4", "Anomaly (High)": "#2ca02c", "Anomaly (Low)": "#d62728"},
            title=f"Time Series Analysis: {metric_choice} with Thresholding",
            height=400
        )

        # 加上趋势线
        fig.add_scatter(x=df_demo["Date"], y=[mean_val] * 90, mode='lines', name='Average',
                        line=dict(dash='dash', color='gray'))

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # --- 4. 业务洞察 (Business Insight) ---
    st.info(f"""
    **💡 Automated Insight:**
    *   The system automatically flagged **{len(df_demo[df_demo['Type'] != 'Normal'])} data points** as statistical anomalies.
    *   In a real-world scenario (like my experience at *Pingan Bank*), this triggers an automated alert to the Ops team, reducing diagnosis time from **days to hours**.
    """)
