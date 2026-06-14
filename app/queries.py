# Store complex SQL strings here so they don't clutter the UI files
GET_ALL_OPPORTUNITIES = "SELECT * FROM opportunities ORDER BY created_at DESC"
GET_DASHBOARD_STATS = "SELECT COUNT(*) as total, category, work_mode FROM opportunities GROUP BY category, work_mode"