from fastapi import APIRouter

from app.api.api_v1.endpoints import users, login
# account_statement,  account_history, accounts
# items, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(account_statement.router, prefix="/account-statement", tags=["account_statement"])
# api_router.include_router(account_history.router, prefix="/account-history", tags=["account_history"])
# api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
