from exemplo.api import router as exemplo_router
from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("/exemplo/", exemplo_router)