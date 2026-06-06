from themes import themes


def generate_svg(stats: dict, theme_name: str = "default") -> str:
    """Gera o SVG baseado nos dados e no tema escolhido."""
    theme = themes.get(theme_name, themes["default"])

    # Função auxiliar para formatar a cor corretamente (adicionando # se necessário)
    def format_color(color_val):
        if not color_val:
            return ""
        color_str = str(color_val).strip()
        # Se for um gradiente (com vírgulas) ou já tiver #, ou for transparente 'ffffff00'
        if "," in color_str or color_str.startswith("#"):
            return color_str
        return f"#{color_str}"

    title_color = format_color(theme.get("title_color", "2f80ed"))
    text_color = format_color(theme.get("text_color", "333333"))
    bg_color = format_color(theme.get("bg_color", "fffefe"))

    # Trata a borda: se não existir, usa a cor do texto
    border_color = theme.get("border_color")
    border_color = format_color(border_color) if border_color else text_color

    return f"""<svg width="400" height="230" viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg">
        <style>
            .header {{ font: bold 18px 'Segoe UI', Ubuntu, Sans-Serif; fill: {title_color}; }}
            .stat {{ font: 600 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: {text_color}; }}
            .bold {{ font-weight: bold; }}
        </style>
        <rect width="399" height="229" x="0.5" y="0.5" rx="4.5" fill="{bg_color}" stroke="{border_color}"/>
        
        <text x="25" y="35" class="header">{stats['name']}'s GitHub Stats</text>
        
        <text x="25" y="75" class="stat">Total Commits: <tspan class="bold" x="170">{stats['total_commits']}</tspan></text>
        <text x="25" y="105" class="stat">Stars Received: <tspan class="bold" x="170">{stats['stars']}</tspan></text>
        <text x="25" y="135" class="stat">Total PRs: <tspan class="bold" x="170">{stats['total_prs']}</tspan></text>
        <text x="25" y="165" class="stat">Total Issues: <tspan class="bold" x="170">{stats['total_issues']}</tspan></text>
        <text x="25" y="195" class="stat">Contributed to: <tspan class="bold" x="170">{stats['contributed_to']}</tspan></text>
    </svg>"""
