from fastapi import APIRouter

router = APIRouter(tags=['Info page'])

@router.get("/info")
def app_info():
    return {
        "app": " FastAPI App for retriving CVEs from json file",
        "author": "Anhelina Bodak",
    }
