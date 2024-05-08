from ninja import Router

router = Router()

@router.get("listar/")
def exemplo(request):
    return {"message": "Exemplo de rota no aplicativo exemplo"}
