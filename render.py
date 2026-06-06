def generate_svg(stats: dict) -> str:
    """Gera o SVG baseado nos dados recebidos."""
    return f"""
    <svg width="400" height="230" viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg">
        <style>
            .header {{ font: bold 18px 'Segoe UI', Ubuntu, Sans-Serif; fill: #2f80ed; }}
            .stat {{ font: 600 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: #333333; }}
            .bold {{ font-weight: bold; }}
        </style>
        <rect width="399" height="229" x="0.5" y="0.5" rx="4.5" fill="#fffefe" stroke="#e4e2e2"/>
        
        <text x="25" y="35" class="header">{stats['name']}'s GitHub Stats</text>
        
        <text x="25" y="75" class="stat">Total Commits: <tspan class="bold" x="170">{stats['total_commits']}</tspan></text>
        <text x="25" y="105" class="stat">Stars Received: <tspan class="bold" x="170">{stats['stars']}</tspan></text>
        <text x="25" y="135" class="stat">Total PRs: <tspan class="bold" x="170">{stats['total_prs']}</tspan></text>
        <text x="25" y="165" class="stat">Total Issues: <tspan class="bold" x="170">{stats['total_issues']}</tspan></text>
        <text x="25" y="195" class="stat">Contributed to: <tspan class="bold" x="170">{stats['contributed_to']}</tspan></text>
    </svg>
    """
