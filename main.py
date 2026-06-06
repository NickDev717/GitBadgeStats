from fastapi import FastAPI, Response
from dotenv import load_dotenv

from github import fetch_github_stats
from render import generate_svg

load_dotenv()

app = FastAPI(title="Custom GitHub Stats")


@app.get("/api")
async def get_repo_stats(username: str):
    # 1. Busca os dados usando o módulo do github
    stats = await fetch_github_stats(username)

    # 2. Transforma os dados em SVG usando o módulo visual
    svg_content = generate_svg(stats)

    # 3. Retorna a resposta visual
    return Response(content=svg_content, media_type="image/svg+xml")
