import json
import typer

from rag_core.config import load_yaml, build_admin_pipeline
# from rag_core.policy import collect_caps, validate_caps, ADMIN_POLICY
from rag_core.pipeline import index_all

app = typer.Typer(add_completion=False)

@app.command()
def sync(config: str, json_out: bool = False):
    cfg = load_yaml(config)
    loader, chunker, embedder, store = build_admin_pipeline(cfg)

    # ✅ Policy ellenőrzés pipeline-szinten
    # pipeline_caps = collect_caps(loader, chunker, embedder, store)
    # validate_caps(pipeline_caps, ADMIN_POLICY, "pipeline")

    out = index_all(loader, chunker, embedder, store)
    if json_out:
        typer.echo(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        typer.echo(f"Indexed docs={out['docs']} chunks={out['chunks']} dim={out['dim']}")

if __name__ == "__main__":
    app()
