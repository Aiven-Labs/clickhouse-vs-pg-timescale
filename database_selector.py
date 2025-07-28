import streamlit as st

def main():
    st.title("Database Selection Assistant")
    st.write("Answer these 5 questions to determine whether PostgreSQL with TimescaleDB or ClickHouse is better for your use case.")
    
    st.subheader("Question 1: Data Volume")
    data_volume = st.selectbox(
        "What is your expected daily data ingestion volume?",
        ["< 1 GB/day", "1-10 GB/day", "10-100 GB/day", "> 100 GB/day"]
    )
    
    st.subheader("Question 2: Query Patterns")
    query_pattern = st.selectbox(
        "What type of queries do you primarily run?",
        [
            "OLTP - Many small, fast transactions",
            "OLAP - Complex analytical queries",
            "Mixed - Both transactional and analytical",
            "Time-series analytics"
        ]
    )
    
    st.subheader("Question 3: Real-time Requirements")
    realtime_needs = st.selectbox(
        "How important is real-time data processing?",
        [
            "Critical - Need sub-second latency",
            "Important - Need near real-time (seconds)",
            "Moderate - Minutes delay acceptable",
            "Low - Batch processing is fine"
        ]
    )
    
    st.subheader("Question 4: Data Retention")
    data_retention = st.selectbox(
        "How long do you need to keep your data?",
        [
            "< 1 year",
            "1-3 years",
            "3-7 years",
            "> 7 years"
        ]
    )
    
    st.subheader("Question 5: Team Expertise")
    team_expertise = st.selectbox(
        "What is your team's database expertise level?",
        [
            "SQL experts with PostgreSQL experience",
            "General SQL knowledge",
            "Limited database experience",
            "Experienced with distributed systems"
        ]
    )
    
    recommendation = get_recommendation(
        data_volume, query_pattern, realtime_needs, 
        data_retention, team_expertise
    )
    display_recommendation(recommendation)

def get_recommendation(data_volume, query_pattern, realtime_needs, data_retention, team_expertise):
    clickhouse_score = 0
    timescaledb_score = 0
    
    # Score based on data volume
    if data_volume == "< 1 GB/day":
        timescaledb_score += 2
    elif data_volume == "1-10 GB/day":
        timescaledb_score += 1
        clickhouse_score += 1
    elif data_volume == "10-100 GB/day":
        clickhouse_score += 2
    else:  # > 100 GB/day
        clickhouse_score += 3
    
    # Score based on query patterns
    if query_pattern == "OLTP - Many small, fast transactions":
        timescaledb_score += 3
    elif query_pattern == "OLAP - Complex analytical queries":
        clickhouse_score += 3
    elif query_pattern == "Mixed - Both transactional and analytical":
        timescaledb_score += 2
    else:  # Time-series analytics
        timescaledb_score += 1
        clickhouse_score += 2
    
    # Score based on real-time requirements
    if realtime_needs == "Critical - Need sub-second latency":
        timescaledb_score += 2
    elif realtime_needs == "Important - Need near real-time (seconds)":
        timescaledb_score += 1
        clickhouse_score += 1
    elif realtime_needs == "Moderate - Minutes delay acceptable":
        clickhouse_score += 1
    else:  # Low - Batch processing is fine
        clickhouse_score += 2
    
    # Score based on data retention
    if data_retention in ["< 1 year", "1-3 years"]:
        timescaledb_score += 1
    else:  # 3-7 years or > 7 years
        clickhouse_score += 2
    
    # Score based on team expertise
    if team_expertise == "SQL experts with PostgreSQL experience":
        timescaledb_score += 3
    elif team_expertise == "General SQL knowledge":
        timescaledb_score += 1
    elif team_expertise == "Limited database experience":
        timescaledb_score += 2
    else:  # Experienced with distributed systems
        clickhouse_score += 2
    
    if timescaledb_score > clickhouse_score:
        return {
            "recommendation": "PostgreSQL with TimescaleDB",
            "score": timescaledb_score,
            "alternative_score": clickhouse_score
        }
    else:
        return {
            "recommendation": "ClickHouse",
            "score": clickhouse_score,
            "alternative_score": timescaledb_score
        }

def display_recommendation(recommendation):
    st.success(f"**Recommended Database: {recommendation['recommendation']}**")
    
    # Display score visualization slider
    total_score = recommendation['score'] + recommendation['alternative_score']
    if total_score > 0:
        timescaledb_percentage = (recommendation['alternative_score'] if recommendation['recommendation'] == "ClickHouse" else recommendation['score']) / total_score
        clickhouse_percentage = (recommendation['score'] if recommendation['recommendation'] == "ClickHouse" else recommendation['alternative_score']) / total_score
        
        st.subheader("Solution Analysis")
        
        # Create a visual line with marker
        st.write("**Database Recommendation Scale**")
        
        # Calculate position on scale (0 to 1, where 0 is full TimescaleDB, 1 is full ClickHouse)
        marker_position = clickhouse_percentage
        
        # Create visual representation using HTML/CSS for a line with marker
        line_html = f"""
        <div style="position: relative; height: 60px; margin: 20px 0;">
            <div style="position: absolute; top: 20px; left: 0; right: 0; height: 4px; background: linear-gradient(to right, #1f77b4 0%, #1f77b4 50%, #ff7f0e 50%, #ff7f0e 100%); border-radius: 2px;"></div>
            <div style="position: absolute; top: 15px; left: {marker_position * 100}%; transform: translateX(-50%); width: 14px; height: 14px; background: #333; border-radius: 50%; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.3);"></div>
            <div style="position: absolute; top: 35px; left: 0; font-size: 12px; color: #1f77b4; font-weight: bold;">TimescaleDB</div>
            <div style="position: absolute; top: 35px; right: 0; font-size: 12px; color: #ff7f0e; font-weight: bold;">ClickHouse</div>
        </div>
        """
        
        st.markdown(line_html, unsafe_allow_html=True)
        
        # Determine confidence level
        confidence_value = max(timescaledb_percentage, clickhouse_percentage) * 100
        
        # Confidence indicator
        if confidence_value > 70:
            st.success(f"High Confidence Recommendation")
        elif confidence_value > 60:
            st.warning(f"Moderate Confidence - Both options viable")
        else:
            st.info(f"Low Confidence - Consider evaluating both options")
    
    if recommendation['recommendation'] == "PostgreSQL with TimescaleDB":
        st.write("### Why TimescaleDB?")
        st.write("""
        - **ACID Compliance**: Full ACID transactions for data consistency
        - **SQL Familiarity**: Standard PostgreSQL with time-series extensions
        - **Real-time Ingestion**: Excellent for high-frequency data insertion
        - **Mature Ecosystem**: Rich ecosystem of PostgreSQL tools and extensions
        - **Flexible Schema**: Supports both relational and time-series data models
        """)
        
        st.write("### Best for:")
        st.write("- IoT sensor data, financial tick data, monitoring metrics")
        st.write("- Applications requiring both transactional and analytical workloads")
        st.write("- Teams with PostgreSQL expertise")
        
    else:
        st.write("### Why ClickHouse?")
        st.write("""
        - **Columnar Storage**: Optimized for analytical queries
        - **High Compression**: Efficient storage for large datasets
        - **Massive Scale**: Handles petabytes of data efficiently
        - **Fast Analytics**: Sub-second response times for complex queries
        - **Distributed Architecture**: Built for horizontal scaling
        """)
        
        st.write("### Best for:")
        st.write("- Large-scale analytics, data warehousing, business intelligence")
        st.write("- High-volume data ingestion with batch processing")
        st.write("- Teams comfortable with distributed systems")
    
    
    st.write("### Next Steps:")
    if recommendation['recommendation'] == "PostgreSQL with TimescaleDB":
        st.write("1. Set up PostgreSQL with TimescaleDB extension")
        st.write("2. Design your hypertables for time-series data")
        st.write("3. Configure retention policies and compression")
    else:
        st.write("1. Set up ClickHouse cluster")
        st.write("2. Design your table schemas with appropriate engines")
        st.write("3. Configure data partitioning and replication")

if __name__ == "__main__":
    main()