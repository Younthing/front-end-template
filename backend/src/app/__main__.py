import uvicorn
from src.app.config import settings

def main():
    uvicorn.run(
        "src.app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )

if __name__ == "__main__":
    main()
